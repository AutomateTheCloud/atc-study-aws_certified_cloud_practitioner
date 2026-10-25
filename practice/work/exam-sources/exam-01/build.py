"""Build the mixed-set pages and the similarity candidates from the item files.

Usage: python3 build.py           # writes the pages into the guide and candidates.jsonl here
       python3 build.py --blind   # also writes blind copies (no answer key) here
"""
import importlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/data/atc/study/atc-study-aws_certified_cloud_practitioner"
OUT = f"{REPO}/guide/90-exam-prep"
sys.path.insert(0, HERE)

DOMAIN_OF = lambda t: int(t.split(".")[0])
DOMAINS = {1: ("Cloud Concepts", 24), 2: ("Security and Compliance", 30),
           3: ("Cloud Technology and Services", 34), 4: ("Billing, Pricing, and Support", 12)}
EXAM = "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02"

ATTR = ('---\n\n"{title}" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional '
        'Permission for Internal Training from Automate the Cloud Inc.\n'
        'License: https://creativecommons.org/licenses/by-nc/4.0/\n'
        'Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt\n')


def task_url(t):
    d = DOMAIN_OF(t)
    return f"{EXAM}/cloud-practitioner-02-domain{d}.html#cloud-practitioner-02-task{t}"


def slug(h):
    s = h.strip().lower()
    s = re.sub(r"[^a-z0-9 _\-]", "", s)
    return s.replace(" ", "-")


def check_link(path, heading):
    """path is relative to guide/90-exam-prep; heading must be an H2/H3 in that file."""
    full = os.path.normpath(os.path.join(OUT, path))
    heads = [l.lstrip("#").strip() for l in open(full) if re.match(r"^#{2,3} ", l)]
    if heading not in heads:
        raise SystemExit(f"heading not found: {path} :: {heading}")
    return f"{path}#{slug(heading)}"


def lesson_label(path):
    full = os.path.normpath(os.path.join(OUT, path))
    m = re.search(r"guide/(\d\d)-[^/]+/(\d\d)-", full)
    title = re.search(r'^title: "(.*)"', open(full).read(), re.M).group(1)
    kind = "Lesson" if "sim-" not in path else "Simulation"
    return f"{kind} {m.group(1)}.{m.group(2)}, {title}" if kind == "Lesson" else title


def band_cuts(n):
    # below 60%: restudy; 60-79%: review; 80% or more: ready
    import math
    ready = math.ceil(0.8 * n - 1e-9)
    review = math.ceil(0.6 * n - 1e-9)
    return review, ready


def score_table(items):
    rows = []
    for d, (name, w) in DOMAINS.items():
        nums = [i + 1 for i, it in enumerate(items) if DOMAIN_OF(it["task"]) == d]
        n = len(nums)
        if n == 0:
            continue
        review, ready = band_cuts(n)
        restudy = f"0 to {review - 1}" if review - 1 > 0 else "0"
        rev = f"{review} to {ready - 1}" if ready - 1 > review else f"{review}"
        if ready - 1 < review:
            rev = "(none)"
        rdy = f"{ready} to {n}" if ready < n else f"{n}"
        rows.append(f"| {d} {name} | {w}% | {n}: {', '.join(map(str, nums))} | {restudy} | {rev} | {rdy} |")
    head = ("| Domain | Share of the exam | Questions in this set | Restudy (below 60%) | Review the linked sections (60–79%) | Ready on this domain (80% or more) |\n"
            "|---|---|---|---|---|---|")
    return head + "\n" + "\n".join(rows)


def render(mod):
    m = importlib.import_module(mod)
    items = m.ITEMS
    tasks = sorted({it["task"] for it in items}, key=lambda t: tuple(map(int, t.split("."))))
    letters = "ABCDE"
    out = []
    fm = ["---", "type: check", f"id: {m.ID}", f'title: "{m.TITLE}"',
          "tasks: [" + ", ".join(f'"{t}"' for t in tasks) + "]", "objectives: []",
          f'reader: "{m.READER}"',
          "prerequisites: [" + ", ".join(m.PREREQS) + "]",
          "pillars: [" + ", ".join(m.PILLARS) + "]",
          "facts_checked: 2026-10-24", "sources:"] + [f'  - "{s}"' for s in m.SOURCES] + ["---", ""]
    out += fm
    out.append(m.INTRO.strip() + "\n")
    out.append("## Questions\n")
    blind = list(out)
    key = []
    for i, it in enumerate(items, 1):
        n = len(it["opts"])
        multi = len(it["ans"]) > 1
        assert (n == 5) == multi, it["id"]
        q = it["q"].strip()
        if multi:
            assert q.endswith("(Select TWO.)"), it["id"]
        block = f"**{i}.** {q}\n\n" + "\n".join(f"- {L}. {o}" for L, o in zip(letters, it["opts"])) + "\n"
        out.append(block)
        blind.append(block)
        link = check_link(*it["link"])
        ans = " and ".join(it["ans"]) if multi else it["ans"]
        key.append(f"**{i}. {ans}** · Task [{it['task']}]({task_url(it['task'])}). {it['exp'].strip()} "
                   f"Reread: [{lesson_label(it['link'][0])}, \"{it['link'][1]}\"]({link}).\n")
    out.append("## Answer key\n")
    out.append("Open the key only when you've answered every question.\n")
    out.append("<details><summary>Answer key</summary>\n")
    out += key
    out.append("</details>\n")
    out.append("## Score by domain\n")
    out.append(m.SCORE_INTRO.strip() + "\n")
    out.append(score_table(items) + "\n")
    out.append(m.SCORE_OUTRO.strip() + "\n")
    out.append(ATTR.format(title=m.TITLE))
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    blind_text = "\n".join(blind)
    # candidates
    cands = []
    for i, it in enumerate(items, 1):
        cands.append({"id": f"{m.ID}-{i:02d}", "question": it["q"].strip(),
                      "options": {L: o for L, o in zip(letters, it["opts"])},
                      "answer": list(it["ans"])})
    return m, text, blind_text, cands, items


def stats(items):
    from collections import Counter
    pos = Counter(c for it in items for c in it["ans"])
    dom = Counter(DOMAIN_OF(it["task"]) for it in items)
    tasks = Counter(it["task"] for it in items)
    multi = sum(len(it["ans"]) > 1 for it in items)
    return f"n={len(items)} multi={multi} domains={dict(sorted(dom.items()))} positions={dict(sorted(pos.items()))} tasks={dict(sorted(tasks.items()))}"


if __name__ == "__main__":
    mods = [a for a in sys.argv[1:] if not a.startswith("--")] or ["items1", "items2", "items3"]
    allc = []
    for mod in mods:
        if not os.path.exists(os.path.join(HERE, mod + ".py")):
            continue
        m, text, blind, cands, items = render(mod)
        open(os.path.join(OUT, m.FILE), "w").write(text)
        open(os.path.join(HERE, f"blind-{m.FILE}"), "w").write(blind)
        allc += cands
        print(m.FILE, stats(items))
    with open(os.path.join(HERE, "candidates.jsonl"), "w") as f:
        for c in allc:
            f.write(json.dumps(c) + "\n")
