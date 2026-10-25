#!/usr/bin/env python3
"""Check that a prose-humanizing pass changed only prose.

Usage: python3 -I source/tools/humanize_guard.py <before> <after>   (.md, or the glossary .yaml)

Fails (exit 1) and lists every difference in the items a style pass must never touch:
front matter, headings, fenced blocks (mermaid, code), tables, images, links (text and
target), inline code, bold spans (console labels, terms), double-quoted text (quotes from
AWS and on-screen messages), callout labels, numbers and dates, "Long description" paragraphs, answer choices, and the
order of "**You should see:**" / "If something went wrong" markers. For the glossary YAML,
only `definition` and `not_to_confuse` may change, and the same checks run on their text.
"""
import re, sys
from collections import Counter

def parts(text):
    fm = ""
    if text.startswith("---\n"):
        end = text.index("\n---\n", 4) + 5
        fm, text = text[:end], text[end:]
    fences, body, buf, inside = [], [], [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            buf.append(line)
            if inside:
                fences.append("\n".join(buf)); buf = []
            inside = not inside
            continue
        (buf if inside else body).append(line)
    return fm, fences, body

def items(text):
    fm, fences, body = parts(text)
    joined = "\n".join(body)
    out = {
        "front matter": [fm],
        "fenced blocks": fences,
        "headings": [l.strip() for l in body if re.match(r"\s*#{1,6} ", l)],
        "table rows": [l.strip() for l in body if l.lstrip("> ").startswith("|")],
        "images": re.findall(r"!\[[^\]]*\]\([^)]*\)", joined),
        "link targets": re.findall(r"\]\(([^)]+)\)", joined),
        "link texts": re.findall(r"(?<!!)\[([^\]]+)\]\(", joined),
        "inline code": re.findall(r"`[^`\n]+`", joined),
        "bold": re.findall(r"\*\*[^*\n]+\*\*", joined),
        "quoted": re.findall(r"\"[^\"\n]{3,}\"", joined),
        "callout labels": re.findall(r"^\s*>\s*\*\*[^*]+\*\*", joined, re.M),
        "numbers and dates": re.findall(r"\$?\d[\d,.:%/-]*", re.sub(r"\]\([^)]*\)|`[^`]*`", "", joined)),
        "long descriptions": [l.strip() for l in body if l.lstrip("> ").startswith("**Long description")],
        "answer choices": [l.strip() for l in body if re.match(r"\s*(>\s*)?(- )?[A-F][.)] ", l)],
        "step markers": re.findall(r"\*\*You should see:\*\*|If something went wrong", joined),
    }
    return out

PROSE_FIELDS = ("definition", "not_to_confuse")

def yaml_prose(pa, pb):
    """Fail on any change outside the glossary's prose fields; return their text as two pages."""
    import yaml
    ya, yb = (yaml.safe_load(open(p, encoding="utf-8")) for p in (pa, pb))
    strip = lambda e: {k: v for k, v in e.items() if k not in PROSE_FIELDS}
    if len(ya) != len(yb) or any(strip(x) != strip(y) for x, y in zip(ya, yb)):
        print("FAIL: a field other than definition/not_to_confuse, or an entry, changed"); sys.exit(1)
    page = lambda y: "\n\n".join(str(e.get(f, "")) for e in y for f in PROSE_FIELDS)
    return page(ya), page(yb)

def main():
    if sys.argv[1].endswith((".yaml", ".yml")):
        a, b = yaml_prose(*sys.argv[1:3])
    else:
        a, b = (open(p, encoding="utf-8").read() for p in sys.argv[1:3])
    ia, ib = items(a), items(b)
    bad = 0
    for k in ia:
        if k == "step markers":
            if ia[k] != ib[k]:
                bad += 1; print(f"{k}: order or count changed ({len(ia[k])} -> {len(ib[k])})")
            continue
        ca, cb = Counter(ia[k]), Counter(ib[k])
        if ca != cb:
            bad += 1
            lost, new = ca - cb, cb - ca
            print(f"{k}: changed")
            for x in list(lost.elements())[:8]: print(f"   - {x[:140]!r}")
            for x in list(new.elements())[:8]: print(f"   + {x[:140]!r}")
    wa, wb = len(re.findall(r"\w+", a)), len(re.findall(r"\w+", b))
    print(f"words: {wa} -> {wb} ({(wb - wa) * 100 / max(wa, 1):+.1f}%)")
    print("PASS: only prose changed" if not bad else f"FAIL: {bad} protected categories changed")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
