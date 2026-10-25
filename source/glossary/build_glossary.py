#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Check reference/glossary.yaml and build guide/99-reference/01-glossary.md from it.

The YAML file is the source of truth; never edit the Markdown page by hand. Each entry has:

  term            the term as the guide writes it (required)
  abbreviation    optional
  definition      one to three plain sentences in our own words, at most 40 words counted
                  as runs of letters and digits (it is a flashcard's back) (required)
  taught_in       repo-relative path of the page that teaches the term (required)
  also_in         optional list of other pages that define or use it
  exam_name       optional; only when the CLF-C02 exam guide's name differs from today's
  confused_with   optional list of terms that also have entries
  not_to_confuse  one sentence on the difference, at most 40 words; required when
                  confused_with is present
  module          two-digit module of taught_in, as a string (required)

Usage, from the repository root:

  python3 source/glossary/build_glossary.py           # check, then write the glossary page
  python3 source/glossary/build_glossary.py --check   # check only; exit 1 if the page is stale

Needs PyYAML (python3 -m pip install pyyaml).
"""

import re
import string
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("build_glossary.py needs PyYAML: python3 -m pip install pyyaml")

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "reference" / "glossary.yaml"
PAGE = ROOT / "guide" / "99-reference" / "01-glossary.md"

REQUIRED = ("term", "definition", "taught_in", "module")
OPTIONAL = ("abbreviation", "also_in", "exam_name", "confused_with", "not_to_confuse")
MAX_DEFINITION_WORDS = 40  # a definition is the back of a flashcard

ATTRIBUTION = (
    '"Glossary" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional '
    "Permission for Internal Training from Automate the Cloud Inc.\n"
    "License: https://creativecommons.org/licenses/by-nc/4.0/\n"
    "Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt"
)


def sort_key(term):
    return term.casefold()


def clean(text):
    """Collapse the whitespace a folded YAML block leaves behind."""
    return " ".join(str(text).split())


def words(text):
    """Words as the flashcard checker counts them: runs of letters and digits, so
    "Standard-IA" is two."""
    return len(re.findall(r"\w+", text))


def sentences(text):
    """Rough sentence count: full stops followed by a space and a capital or a digit."""
    return len(re.findall(r"[.!?](?:\s+(?=[A-Z0-9\"])|$)", text))


def page_title(path, cache={}):
    """The title in a guide page's front matter."""
    if path not in cache:
        text = (ROOT / path).read_text(encoding="utf-8")
        match = re.search(r'^title:\s*"?(.*?)"?\s*$', text, re.MULTILINE)
        cache[path] = match.group(1) if match else path
    return cache[path]


def check(entries):
    """Return a list of problems; an empty list means the file is good."""
    problems = []
    if not isinstance(entries, list):
        return ["the file must be a YAML list of entries"]
    terms = [e.get("term") for e in entries if isinstance(e, dict)]
    known = {t.casefold() for t in terms if t}

    seen = set()
    for i, e in enumerate(entries, 1):
        if not isinstance(e, dict):
            problems.append(f"entry {i}: not a mapping")
            continue
        name = e.get("term", f"entry {i}")
        for field in REQUIRED:
            if not e.get(field):
                problems.append(f"{name}: missing {field}")
        for field in e:
            if field not in REQUIRED + OPTIONAL:
                problems.append(f"{name}: unknown field {field!r}")
        if name.casefold() in seen:
            problems.append(f"{name}: duplicate term")
        seen.add(name.casefold())

        for path in [e.get("taught_in")] + list(e.get("also_in") or []):
            if path and not (ROOT / path).is_file():
                problems.append(f"{name}: no such page {path}")
        if e.get("taught_in") in (e.get("also_in") or []):
            problems.append(f"{name}: also_in repeats taught_in")
        match = re.match(r"guide/(\d\d)-", e.get("taught_in") or "")
        if match and str(e.get("module")) != match.group(1):
            problems.append(f"{name}: module {e.get('module')!r} doesn't match taught_in")

        for other in e.get("confused_with") or []:
            if other.casefold() not in known:
                problems.append(f"{name}: confused_with {other!r} has no entry")
            if other.casefold() == name.casefold():
                problems.append(f"{name}: confused with itself")
        if bool(e.get("confused_with")) != bool(e.get("not_to_confuse")):
            problems.append(f"{name}: confused_with and not_to_confuse must appear together")

        definition = clean(e.get("definition", ""))
        if sentences(definition) > 3:
            problems.append(f"{name}: definition has more than three sentences")
        if words(definition) > MAX_DEFINITION_WORDS:
            problems.append(
                f"{name}: definition has {words(definition)} words; "
                f"the limit is {MAX_DEFINITION_WORDS}"
            )
        if e.get("not_to_confuse"):
            if sentences(clean(e["not_to_confuse"])) > 1:
                problems.append(f"{name}: not_to_confuse should be one sentence")
            if words(clean(e["not_to_confuse"])) > MAX_DEFINITION_WORDS:
                problems.append(
                    f"{name}: not_to_confuse has {words(clean(e['not_to_confuse']))} words; "
                    f"the limit is {MAX_DEFINITION_WORDS}"
                )

    if terms != sorted(terms, key=sort_key):
        problems.append("entries are not sorted alphabetically by term")
    return problems


def link(path):
    """A link from the glossary page to a guide page, with the page's title as its text."""
    return f"[{page_title(path)}](../{path.removeprefix('guide/')})"


def render(entries):
    groups = {}
    for e in entries:
        letter = e["term"][0].upper()
        # Not "#": in Markdown, "## #" is an empty heading (the "#" closes it).
        groups.setdefault(letter if letter in string.ascii_uppercase else "0–9", []).append(e)

    jump = " · ".join(
        f"[{c}](#{c.lower()})" if c in groups else c for c in string.ascii_uppercase
    )
    modules = sorted({e["module"] for e in entries})

    out = [
        "---",
        "# Generated by source/glossary/build_glossary.py from reference/glossary.yaml. Don't edit by hand.",
        "type: reference",
        "id: clf-99-01",
        'title: "Glossary"',
        'reader: "Adult studying alone, possibly new to IT; a page to look terms up in"',
        "tasks: []",
        "objectives: []",
        "pillars: []",
        "---",
        "",
        "# Glossary",
        "",
        f"The {len(entries)} terms this guide has taught so far (modules {', '.join(modules)}), each "
        "with a link to the page that teaches it; the list grows as modules are written.",
        "",
        jump,
        "",
    ]
    for letter in sorted(groups):
        out += [f"## {letter}", ""]
        for e in groups[letter]:
            head = f"**{e['term']}**"
            if e.get("abbreviation"):
                head += f" ({e['abbreviation']})"
            out.append(f"{head}: {clean(e['definition'])}")
            out.append("")
            out.append(f"- Taught in: {link(e['taught_in'])}")
            if e.get("also_in"):
                out.append("- Also in: " + "; ".join(link(p) for p in e["also_in"]))
            if e.get("exam_name"):
                out.append(f"- Exam name: \"{clean(e['exam_name'])}\" in the CLF-C02 exam guide")
            if e.get("confused_with"):
                names = ", ".join(e["confused_with"])
                out.append(f"- Don't confuse with: {names}. {clean(e['not_to_confuse'])}")
            out.append("")
    out += ["---", "", ATTRIBUTION, ""]
    return "\n".join(out)


def main(argv):
    entries = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    problems = check(entries)
    if problems:
        print(f"{SOURCE.relative_to(ROOT)}: {len(problems)} problem(s)", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1
    page = render(entries)
    if "--check" in argv:
        if not PAGE.is_file() or PAGE.read_text(encoding="utf-8") != page:
            print(f"{PAGE.relative_to(ROOT)} is out of date; run build_glossary.py", file=sys.stderr)
            return 1
        print(f"{len(entries)} terms; {PAGE.relative_to(ROOT)} is up to date")
        return 0
    PAGE.write_text(page, encoding="utf-8")
    print(f"{len(entries)} terms written to {PAGE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
