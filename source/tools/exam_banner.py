#!/usr/bin/env python3
"""Write the "Exam guide" line under each guide page's title, from the page's `tasks`.

Usage, from the repository root:
  python3 -I source/tools/exam_banner.py            write or update every line
  python3 -I source/tools/exam_banner.py --check    exit 1 if any page is out of date

The line sits right after the key message (the first paragraph under the H1), for example:

  **Exam guide:** Domain 3, Cloud Technology and Services (34% of the exam): tasks 3.4 and 3.6.

with each domain and task linked to the CLF-C02 exam guide. Pages without tasks (start-here pages,
reference pages, "Beyond the exam" pages) get no line, and a stale line is removed.
"""
import glob, re, sys

GUIDE = "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/"
DOMAINS = {
    "1": ("Cloud Concepts", 24),
    "2": ("Security and Compliance", 30),
    "3": ("Cloud Technology and Services", 34),
    "4": ("Billing, Pricing, and Support", 12),
}
LABEL = "**Exam guide:**"


def task_link(t):
    d = t.split(".")[0]
    return f"[{t}]({GUIDE}cloud-practitioner-02-domain{d}.html#cloud-practitioner-02-task{t})"


def join(items):
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def banner(tasks):
    by = {}
    for t in sorted(set(tasks), key=lambda x: [int(p) for p in x.split(".")]):
        by.setdefault(t.split(".")[0], []).append(t)
    parts = []
    for d, ts in sorted(by.items()):
        name, weight = DOMAINS[d]
        word = "task" if len(ts) == 1 else "tasks"
        parts.append(f"[Domain {d}, {name}]({GUIDE}cloud-practitioner-02-domain{d}.html) "
                     f"({weight}% of the exam): {word} {join([task_link(t) for t in ts])}")
    return f"{LABEL} " + "; ".join(parts) + "."


def tasks_of(front):
    m = re.search(r"^tasks:\s*\[(.*?)\]\s*$", front, re.M)
    return re.findall(r'"?(\d\.\d)"?', m.group(1)) if m else []


def update(text):
    front_end = text.index("\n---\n", 4) + 5
    front, body = text[:front_end], text[front_end:]
    body = re.sub(r"\n\n" + re.escape(LABEL) + r"[^\n]*", "", body)  # drop a stale line
    tasks = tasks_of(front)
    if not tasks:
        return front + body
    lines = body.split("\n")
    h1 = next(i for i, l in enumerate(lines) if l.startswith("# "))
    i = h1 + 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and re.match(r"(#|>|\||```|<)", lines[i]):
        i = h1 + 1  # no key message: the line goes right under the title
    else:
        while i < len(lines) and lines[i].strip():  # the key message paragraph
            i += 1
    lines[i:i] = ["", banner(tasks)]
    return front + "\n".join(lines)


def main():
    check = "--check" in sys.argv
    stale = 0
    for p in sorted(glob.glob("guide/*/*.md")):
        if "/99-reference/" in p:
            continue
        old = open(p, encoding="utf-8").read()
        if not old.startswith("---\n"):
            continue
        new = update(old)
        if new != old:
            stale += 1
            if check:
                print(f"out of date: {p}")
            else:
                open(p, "w", encoding="utf-8").write(new)
    if check:
        print(f"{stale} page(s) out of date" if stale else "every Exam guide line is up to date")
        sys.exit(1 if stale else 0)
    print(f"{stale} page(s) written")


if __name__ == "__main__":
    main()
