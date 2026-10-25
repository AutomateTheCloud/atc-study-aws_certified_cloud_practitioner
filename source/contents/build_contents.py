#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Build guide/README.md, the guide's contents page, from course.yaml and the pages' front matter.

Sections come from course.yaml's `sections`, in order; each section lists its pages in file order
with their front-matter `title` and a label for their `type`. Never edit guide/README.md by hand.

Usage, from the repository root:

  python3 source/contents/build_contents.py           # write guide/README.md
  python3 source/contents/build_contents.py --check   # exit 1 if guide/README.md is stale

Needs PyYAML.
"""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
GUIDE = ROOT / "guide"
PAGE = GUIDE / "README.md"

TYPES = {
    "brief": "Module brief",
    "lesson": "Lesson",
    "lab": "Lab",
    "sim": "Simulation",
    "check": "Mastery check",
    "task-card": "Task card",
    "reference": "Reference",
    "page": "Page",
}

INTRO = [
    "# Contents",
    "",
    "The guide's pages in reading order. Module 01 is optional: take it if you are new to IT.",
    "",
    "Look up any term in the [glossary](99-reference/01-glossary.md).",
    "",
    "Before your first lab, work through the [guardrails primer]"
    "(https://github.com/AutomateTheCloud/atc-study-aws_account_guardrails/blob/main/primer/00-read-this-first.md).",
    "",
]

ATTRIBUTION = [
    "---",
    "",
    '"Contents" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional '
    "Permission for Internal Training from Automate the Cloud Inc.",
    "License: https://creativecommons.org/licenses/by-nc/4.0/",
    "Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt",
    "",
]


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def render():
    course = yaml.safe_load((ROOT / "course.yaml").read_text(encoding="utf-8"))
    out = list(INTRO)
    for section in course["sections"]:
        folder = GUIDE / section["dir"]
        pages = sorted(p for p in folder.glob("*.md") if p.name != "README.md")
        if not pages:
            continue
        out += [f"## {section['title']}", ""]
        for page in pages:
            front = front_matter(page)
            label = TYPES.get(front.get("type"), "Page")
            title = front.get("title") or page.stem
            out.append(f"- [{title}]({section['dir']}/{page.name}) · {label}")
        out.append("")
    return "\n".join(out + ATTRIBUTION)


def main(argv):
    text = render()
    if "--check" in argv:
        if not PAGE.is_file() or PAGE.read_text(encoding="utf-8") != text:
            print("guide/README.md is out of date; run build_contents.py", file=sys.stderr)
            return 1
        print("guide/README.md is up to date")
        return 0
    PAGE.write_text(text, encoding="utf-8")
    print(f"guide/README.md written: {text.count(chr(10) + '- [')} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
