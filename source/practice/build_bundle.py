#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Build the practice bundle's study.yaml from its item files and the glossary.

Sources (never edit study.yaml by hand):

  practice/bundle.yaml          the collection header (id, title, version, license, ...)
  practice/items/NN-*.yaml      questions and concept cards for module NN, written by hand
  reference/glossary.yaml       the glossary; every entry becomes term cards (see glossary_cards)

Each hand-written item carries these build fields, which become tags and references and are
then removed (the OpenWaymark format allows no unknown members):

  page      repo-relative path of the guide page the item is written from (required)
  section   a heading on that page, without the #s (required)
  task      exam task statement it serves, such as "3.6" (required on questions)
  level     recall, understanding or application (required on questions)
  topics    optional list of topic tags, lowercase-with-hyphens

Every other field is passed through as written (id, selection, prompt, choices, ...).

Usage, from the repository root:

  python3 source/practice/build_bundle.py                  # check, then write the bundle
  python3 source/practice/build_bundle.py --check          # check only; exit 1 if stale
  python3 source/practice/build_bundle.py --only 05 --out practice/work/tmp-05
                                                           # one module, for a writer to lint
  python3 source/practice/build_bundle.py --similarity FILE
                                                           # also write questions as JSONL for
                                                           # the dump quarantine's checker

Needs PyYAML.
"""

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
HEADER = ROOT / "practice" / "bundle.yaml"
ITEMS = ROOT / "practice" / "items"
GLOSSARY = ROOT / "reference" / "glossary.yaml"
BUNDLE = ROOT / "practice" / "clf-c02-practice"
GLOSSARY_PAGE = "guide/99-reference/01-glossary.md"
REPO_URL = "https://github.com/AutomateTheCloud/atc-study-aws_certified_cloud_practitioner/blob/main/"

BUILD_FIELDS = ("page", "section", "task", "level", "topics")
LEVELS = ("recall", "understanding", "application")
TAG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ID = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")


class Problems(list):
    def add(self, where, message):
        self.append(f"{where}: {message}")


# ------------------------------------------------------------------ guide pages

_pages = {}


def page(path):
    """Front matter and headings of a guide page."""
    if path not in _pages:
        file = ROOT / path
        if not file.is_file():
            _pages[path] = None
            return None
        text = file.read_text(encoding="utf-8")
        front = yaml.safe_load(text.split("---", 2)[1]) if text.startswith("---") else {}
        headings = set()
        fenced = False
        for line in text.splitlines():
            if line.startswith("```"):
                fenced = not fenced
            elif not fenced and (m := re.match(r"^#{1,4}\s+(.*?)\s*$", line)):
                headings.add(m.group(1))
        _pages[path] = {"front": front, "headings": headings}
    return _pages[path]


def guide_title():
    course = yaml.safe_load((ROOT / "course.yaml").read_text(encoding="utf-8"))
    return course["title"]


def reference(path, section=None):
    info = page(path)
    pid = info["front"]["id"]
    module, number = pid.split("-")[1:3]
    where = f"Module {module}, page {module}.{number}: {info['front']['title']} ({pid})"
    if section:
        where += f", section \"{section}\""
    return {"title": guide_title(), "reference": where, "url": REPO_URL + path}


def page_tags(path):
    pid = page(path)["front"]["id"]
    return [f"module-{pid.split('-')[1]}", pid]


# ------------------------------------------------------------------ hand-written items


def build_item(item, kind, where, problems):
    for field in ("page", "section"):
        if not item.get(field):
            problems.add(where, f"missing {field}")
    if kind == "question":
        for field in ("task", "level"):
            if not item.get(field):
                problems.add(where, f"missing {field}")
    path, section = item.get("page"), item.get("section")
    if path and page(path) is None:
        problems.add(where, f"no such page {path}")
        return None
    if path and section and section not in page(path)["headings"]:
        problems.add(where, f"no heading {section!r} on {path}")

    task = str(item.get("task") or "")
    if task and not re.fullmatch(r"[1-4]\.[1-9]", task):
        problems.add(where, f"task {task!r} isn't like \"3.6\"")
    level = item.get("level")
    if level and level not in LEVELS:
        problems.add(where, f"level {level!r} isn't one of {', '.join(LEVELS)}")

    tags = page_tags(path) if path and page(path) else []
    if task:
        tags += [f"domain-{task[0]}", f"task-{task.replace('.', '-')}"]
    if level:
        tags.append(level)
    tags.append("exam-style" if kind == "question" else "concept")
    for topic in item.get("topics") or []:
        if not TAG.match(str(topic)):
            problems.add(where, f"topic {topic!r} isn't lowercase-with-hyphens")
        elif topic not in tags:
            tags.append(topic)

    out = {k: v for k, v in item.items() if k not in BUILD_FIELDS}
    out["tags"] = tags
    if path and page(path):
        out["references"] = [reference(path, section)]
    if kind == "question":
        check_question(out, where, problems)
    return out


def check_question(q, where, problems):
    choices = q.get("choices") or []
    ids = [c.get("id") for c in choices]
    if len(set(ids)) != len(ids):
        problems.add(where, "duplicate choice id")
    for c in choices:
        if not c.get("variants"):
            problems.add(where, f"choice {c.get('id')!r} has no variants")
    correct = q.get("correct_answers") or []
    for a in correct:
        if a not in ids:
            problems.add(where, f"correct answer {a!r} isn't a choice")
    if q.get("selection") == "multiple" and q.get("selection_count") not in (None, len(correct)):
        problems.add(where, "selection_count doesn't match correct_answers")
    if not q.get("explanation"):
        problems.add(where, "no explanation")


# ------------------------------------------------------------------ glossary cards


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.casefold()).strip("-")
    return s[:56].rstrip("-")


def clean(text):
    return " ".join(str(text).split())


def glossary_cards(entries):
    """Four kinds of card from the glossary, all tagged glossary-term plus the page's tags.

    term-<slug>  the term, to its definition (every entry)
    exam-<slug>  the term, to the name the CLF-C02 exam guide uses (entries with exam_name)
    abbr-<slug>  the abbreviation, to what it stands for (entries with an abbreviation)
    diff-<slug>  the term and what it's confused with, to the difference (entries with
                 confused_with). Entries that name each other give one card, from the
                 entry that comes first.
    """
    cards = []
    pairs = set()
    for e in entries:
        s = slug(e["term"])
        name = e["term"] + (f" ({e['abbreviation']})" if e.get("abbreviation") else "")
        back = clean(e["definition"])
        refs = [reference(e["taught_in"]), {
            "title": guide_title(),
            "reference": f"Glossary: {e['term']}",
            "url": REPO_URL + GLOSSARY_PAGE,
        }]
        base = page_tags(e["taught_in"])
        cards.append({
            "id": f"term-{s}",
            "front": {"text": f"What does **{name}** mean?"},
            "back": {"text": back},
            "tags": base + ["glossary-term"],
            "references": refs,
        })
        if e.get("exam_name"):
            cards.append({
                "id": f"exam-{s}",
                "front": {"text": f"Which name does the CLF-C02 exam guide use for **{e['term']}**?"},
                "back": {"text": f"\"{clean(e['exam_name'])}\""},
                "tags": base + ["glossary-term", "exam-name"],
                "references": refs,
            })
        if e.get("abbreviation"):
            cards.append({
                "id": f"abbr-{s}",
                "front": {"text": f"What does **{e['abbreviation']}** stand for?"},
                "back": {"text": e["term"]},
                "tags": base + ["glossary-term", "abbreviation"],
                "references": refs,
            })
        pair = frozenset(t.casefold() for t in [e["term"]] + list(e.get("confused_with") or []))
        if e.get("not_to_confuse") and pair not in pairs:
            pairs.add(pair)
            others = " or ".join(f"**{o}**" for o in e["confused_with"])
            cards.append({
                "id": f"diff-{s}",
                "front": {"text": f"How is **{e['term']}** different from {others}?"},
                "back": {"text": clean(e["not_to_confuse"])},
                "tags": base + ["glossary-term", "confused-pair"],
                "references": refs,
            })
    return cards


# ------------------------------------------------------------------ output


class Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # the format allows no anchors or aliases
        return True


def _str(dumper, value):
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


Dumper.add_representer(str, _str)


def render(header, questions, cards):
    doc = dict(header)
    doc["format_version"] = str(doc["format_version"])
    doc["created"] = str(doc["created"])
    if doc.get("updated"):
        doc["updated"] = str(doc["updated"])
    if questions:
        doc["questions"] = questions
    if cards:
        doc["flashcards"] = cards
    head = ("# Generated by source/practice/build_bundle.py from practice/bundle.yaml,\n"
            "# practice/items/ and reference/glossary.yaml. Don't edit by hand.\n")
    return head + yaml.dump(doc, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=100)


def similarity_lines(questions):
    """One JSONL line per question, and one more per extra wording of its choices."""
    lines = []
    for q in questions:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        wordings = max(1 + len(c.get("variants") or []) for c in q["choices"])
        for n in range(wordings):
            options, answer = {}, []
            for letter, c in zip(letters, q["choices"]):
                texts = [c["text"]] + [v["text"] for v in c.get("variants") or []]
                options[letter] = texts[min(n, len(texts) - 1)]
                if c["id"] in q["correct_answers"]:
                    answer.append(letter)
            qid = q["id"] if n == 0 else f"{q['id']}#v{n}"
            lines.append(json.dumps({"id": qid, "question": q["prompt"]["text"],
                                     "options": options, "answer": answer}))
    return lines


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--only", help="build only this module's item file (two digits)")
    ap.add_argument("--out", help="bundle folder to write (default practice/clf-c02-practice)")
    ap.add_argument("--similarity", help="also write questions as JSONL to this file")
    args = ap.parse_args(argv)

    problems = Problems()
    header = yaml.safe_load(HEADER.read_text(encoding="utf-8"))
    questions, cards = [], []
    files = sorted(ITEMS.glob("[0-9][0-9]-*.yaml"))
    if args.only:
        files = [f for f in files if f.name.startswith(args.only + "-")]
    for file in files:
        data = yaml.safe_load(file.read_text(encoding="utf-8")) or {}
        unknown = set(data) - {"questions", "flashcards"}
        if unknown:
            problems.add(file.name, f"unknown top-level keys {sorted(unknown)}")
        for q in data.get("questions") or []:
            built = build_item(q, "question", f"{file.name} {q.get('id')}", problems)
            if built:
                questions.append(built)
        for c in data.get("flashcards") or []:
            built = build_item(c, "card", f"{file.name} {c.get('id')}", problems)
            if built:
                cards.append(built)

    entries = yaml.safe_load(GLOSSARY.read_text(encoding="utf-8"))
    if args.only:
        entries = [e for e in entries if str(e["module"]) == args.only]
    cards += glossary_cards(entries)

    seen = set()
    for item in questions + cards:
        if not ID.match(item.get("id") or ""):
            problems.add(str(item.get("id")), "bad id")
        if item.get("id") in seen:
            problems.add(item["id"], "duplicate id")
        seen.add(item.get("id"))

    if problems:
        print(f"{len(problems)} problem(s):", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    out = Path(args.out) if args.out else BUNDLE
    target = (out if out.is_absolute() else ROOT / out) / "study.yaml"
    text = render(header, questions, cards)
    if args.check:
        if not target.is_file() or target.read_text(encoding="utf-8") != text:
            print(f"{target.relative_to(ROOT)} is out of date; run build_bundle.py", file=sys.stderr)
            return 1
        print(f"{len(questions)} questions, {len(cards)} cards; {target.relative_to(ROOT)} is up to date")
        return 0
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    print(f"{len(questions)} questions, {len(cards)} cards written to {target.relative_to(ROOT)}")
    if args.similarity:
        Path(args.similarity).write_text("\n".join(similarity_lines(questions)) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
