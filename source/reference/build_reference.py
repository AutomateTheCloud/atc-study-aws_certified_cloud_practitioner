#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Build the generated reference pages in guide/99-reference/ from the guide's own data.

Never edit these pages by hand; change their sources and rerun this script:

  02-names-exam-vs-current.md  the glossary's exam_name fields (reference/glossary.yaml), plus the
                               hand-kept table in reference/names.yaml
  03-commonly-confused.md      the glossary's confused_with and not_to_confuse fields
  04-service-map.md            the exam guide's in-scope services (reference/services.yaml), described
                               from the glossary and linked to the pages that teach them
  06-blueprint-map.md          the tasks in every guide page's front matter

05-cost-traps.md is written by hand, and 01-glossary.md is built by
source/glossary/build_glossary.py.

Usage, from the repository root:

  python3 -I source/reference/build_reference.py           # check the data, then write the pages
  python3 -I source/reference/build_reference.py --check   # check only; exit 1 if a page is stale

Problems in the data stop the build. Notes (a date in names.yaml that its teaching page doesn't
mention, for example) are printed and don't stop it: read them and decide.

Needs PyYAML (python3 -m pip install pyyaml).
"""

import re
import string
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("build_reference.py needs PyYAML: python3 -m pip install pyyaml")

ROOT = Path(__file__).resolve().parents[2]
GUIDE = ROOT / "guide"
OUT = GUIDE / "99-reference"
GLOSSARY = ROOT / "reference" / "glossary.yaml"
NAMES = ROOT / "reference" / "names.yaml"
SERVICES = ROOT / "reference" / "services.yaml"

EXAM_GUIDE = "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
DOMAIN_URL = "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain{d}.html"
TASK_URL = DOMAIN_URL + "#cloud-practitioner-02-task{t}"
LIFECYCLE = "https://docs.aws.amazon.com/general/latest/gr/service-lifecycle.html"

# The exam guide's domains and task statements, by number, with our own short titles (course plan
# section 8). We don't reproduce the exam guide's wording; each task links to it.
DOMAINS = {
    "1": ("Cloud Concepts", 24),
    "2": ("Security and Compliance", 30),
    "3": ("Cloud Technology and Services", 34),
    "4": ("Billing, Pricing, and Support", 12),
}
TASKS = {
    "1.1": "Cloud benefits",
    "1.2": "Well-Architected design principles",
    "1.3": "Migration benefits and strategies",
    "1.4": "Cloud economics",
    "2.1": "Shared responsibility",
    "2.2": "Security, governance and compliance concepts",
    "2.3": "Access management",
    "2.4": "Security components and resources",
    "3.1": "Deploying and operating",
    "3.2": "Global infrastructure",
    "3.3": "Compute",
    "3.4": "Databases",
    "3.5": "Networking",
    "3.6": "Storage",
    "3.7": "AI/ML and analytics",
    "3.8": "Other service categories",
    "4.1": "Pricing models",
    "4.2": "Billing, budgets and cost management",
    "4.3": "Technical resources and Support",
}

TYPE_LABELS = {
    "brief": "Module brief",
    "lesson": "Lesson",
    "lab": "Lab",
    "sim": "Simulation",
    "check": "Mastery check",
    "task-card": "Task card",
    "reference": "Reference",
    "page": "Page",
}

NAME_SECTIONS = {
    "exam": "The exam's name now covers more than one product",
    "closed": "On the exam's list, but closed or closing to new customers",
    "feature": "Retired parts of services on the exam's list",
    "older": "Older names and plans in older study material",
    "distractor": "Wrong answers only: removed, out of scope or shut down",
}
NAME_FIELDS = ("name", "now", "section", "term", "taught_in", "mentions", "source")
SERVICE_FIELDS = ("name", "category", "listed", "term", "taught_in", "does", "note")

READER = "Adult studying alone, possibly new to IT; a page to look things up in"


def attribution(title):
    return (
        f'"{title}" by Automate the Cloud Inc., licensed under CC BY-NC 4.0 with the Additional '
        "Permission for Internal Training from Automate the Cloud Inc.\n"
        "License: https://creativecommons.org/licenses/by-nc/4.0/\n"
        "Permission: https://automatethe.cloud/licenses/atc-internal-training-permission.txt"
    )


def clean(text):
    """Collapse the whitespace a folded YAML block leaves behind."""
    return " ".join(str(text).split())


def cell(text):
    """Text that is safe inside a Markdown table cell."""
    return clean(text).replace("|", "\\|")


def first_sentence(text):
    return re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"])", clean(text))[0]


# A comma followed by one of these words starts a new clause, so the first clause ends there.
CLAUSE_WORDS = (
    "such", "including", "with", "which", "so", "where", "while", "without", "using", "applying",
    "letting", "ready", "then", "but", "plus", "billed", "filtered", "from", "after", "each",
    "free", "delivered", "usually", "called", "in", "on", "and", "it",
)


def first_clause(definition):
    """What a service does, in a few words: the definition's first clause, without a leading
    spelled-out name ("Amazon Simple Queue Service: ...") or a "formerly ..." aside."""
    text = first_sentence(definition).rstrip(".")
    text = re.sub(r"^The AWS service formerly called [^:,]+[:,]\s*", "", text)
    text = re.sub(r"^(?:The )?(?:Amazon|AWS)(?: [A-Z][\w-]*)+[:,]\s+", "", text)
    text = re.sub(r",\s*(?:formerly|previously called|successor to)\b[^,:;]*,?", "", text)
    text = re.sub(r"^(?:it|which)\s+", "", text)
    cuts = r"[:;]\s|\s\(|,\s(?=(?:" + "|".join(CLAUSE_WORDS) + r")\b)"
    for match in re.finditer(cuts, text):
        head = text[: match.start()]
        if len(re.findall(r"\w+", head)) >= 3:
            text = head
            break
    return text[0].upper() + text[1:]


def norm(name):
    """A service name without its Amazon or AWS prefix or a bracketed abbreviation, for matching."""
    name = re.sub(r"\s*\([^)]*\)$", "", name.casefold())
    return re.sub(r"^(amazon|aws)\s+", "", name).strip()


# --- Reading the guide -------------------------------------------------------------------------


def read_pages(notes):
    """Every guide page's front matter, keyed by repo-relative path, in reading order.
    Draft pages and pages whose front matter can't be read are left out (with a note)."""
    pages = {}
    for path in sorted(GUIDE.glob("*/*.md")):
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        try:
            front = yaml.safe_load(match.group(1)) if match else None
        except yaml.YAMLError:
            front = None
        if not isinstance(front, dict) or not front.get("title"):
            notes.append(f"{rel}: no readable front matter; left out")
            continue
        if front.get("draft"):
            continue
        pages[rel] = {
            "title": str(front["title"]),
            "type": front.get("type", "page"),
            "tasks": [str(t) for t in front.get("tasks") or []],
            "text": text,
        }
    return pages


def module_titles(pages):
    """Module number to its brief's title ("Module 05: Storing data: storage and databases")."""
    titles = {}
    for path, page in pages.items():
        match = re.match(r"guide/(\d\d)-", path)
        if match and page["type"] == "brief":
            titles[match.group(1)] = page["title"]
    return titles


def module_of(path):
    match = re.match(r"guide/(\d\d)-", path)
    return match.group(1) if match else "00"


def page_link(path, pages):
    """A link from a 99-reference page to a guide page, with the page's title as its text."""
    return f"[{pages[path]['title']}](../{path.removeprefix('guide/')})"


def glossary_anchor(term):
    """The glossary page's anchor for a term: its letter heading."""
    letter = term[0].upper()
    if letter in string.ascii_uppercase:
        return f"01-glossary.md#{letter.lower()}"
    return "01-glossary.md"


def term_link(term):
    return f"[{term}]({glossary_anchor(term)})"


# --- Checking the data -------------------------------------------------------------------------


def index_glossary(entries):
    by_term = {e["term"].casefold(): e for e in entries}
    return by_term


def check_names(data, glossary, pages, problems, notes):
    if not isinstance(data, dict) or not isinstance(data.get("names"), list):
        problems.append("names.yaml: needs a checked date and a list under names")
        return []
    exam_names = {clean(e["exam_name"]).casefold() for e in glossary.values() if e.get("exam_name")}
    rows = []
    seen = set()
    for i, row in enumerate(data["names"], 1):
        name = clean(row.get("name", f"entry {i}"))
        where = f"names.yaml: {name}"
        for field in ("name", "now", "section", "source"):
            if not row.get(field):
                problems.append(f"{where}: missing {field}")
        for field in row:
            if field not in NAME_FIELDS:
                problems.append(f"{where}: unknown field {field!r}")
        if row.get("section") not in NAME_SECTIONS:
            problems.append(f"{where}: section must be one of {', '.join(NAME_SECTIONS)}")
        if name.casefold() in seen:
            problems.append(f"{where}: duplicate name")
        seen.add(name.casefold())
        if row.get("section") == "exam" and name.casefold() in exam_names:
            problems.append(f"{where}: the glossary already carries this exam name; drop the row")
        if not str(row.get("source", "")).startswith("https://"):
            problems.append(f"{where}: source must be an https:// address")

        if bool(row.get("term")) == bool(row.get("taught_in")):
            problems.append(f"{where}: give term or taught_in, not both or neither")
            continue
        if row.get("term"):
            entry = glossary.get(row["term"].casefold())
            if not entry:
                problems.append(f"{where}: term {row['term']!r} has no glossary entry")
                continue
            path = entry["taught_in"]
        else:
            path = row["taught_in"]
        if path not in pages:
            problems.append(f"{where}: no such page {path}")
            continue

        body = pages[path]["text"]
        mention = clean(row.get("mentions") or name)
        if mention not in body:
            problems.append(f"{where}: its teaching page {path} doesn't mention {mention!r}")
        for date in re.findall(r"\d{4}-\d\d-\d\d", clean(row.get("now", ""))):
            if date not in body:
                notes.append(f"{where}: date {date} isn't on its teaching page {path}")
        rows.append(dict(row, name=name, path=path))
    return rows


def resolve_services(services, entries, pages, problems):
    """Match each service to its glossary entry and teaching page."""
    by_term = {e["term"].casefold(): e for e in entries}
    by_exam, by_abbr, by_norm = {}, {}, {}
    for e in entries:
        if e.get("exam_name"):
            by_exam.setdefault(clean(e["exam_name"]).casefold(), []).append(e)
        if e.get("abbreviation"):
            by_abbr.setdefault(e["abbreviation"].casefold(), []).append(e)
        by_norm.setdefault(norm(e["term"]), []).append(e)
        if e.get("abbreviation"):
            by_norm.setdefault(norm(e["abbreviation"]), []).append(e)

    resolved = []
    seen = set()
    if not isinstance(services, list):
        problems.append("services.yaml: must be a YAML list")
        return resolved
    for i, s in enumerate(services, 1):
        name = s.get("name", f"entry {i}")
        where = f"services.yaml: {name}"
        for field in ("name", "category"):
            if not s.get(field):
                problems.append(f"{where}: missing {field}")
        for field in s:
            if field not in SERVICE_FIELDS:
                problems.append(f"{where}: unknown field {field!r}")
        if name.casefold() in seen:
            problems.append(f"{where}: duplicate service")
        seen.add(name.casefold())

        entry = None
        if s.get("term"):
            entry = by_term.get(s["term"].casefold())
            if not entry:
                problems.append(f"{where}: term {s['term']!r} has no glossary entry")
        elif not s.get("taught_in"):
            key = name.casefold()
            for candidates in (
                by_exam.get(key),
                [by_term[key]] if key in by_term else None,
                by_abbr.get(key),
                by_norm.get(norm(name)),
            ):
                if candidates:
                    if len({c["term"] for c in candidates}) > 1:
                        terms = ", ".join(sorted({c["term"] for c in candidates}))
                        problems.append(f"{where}: matches several glossary terms ({terms}); set term")
                    entry = candidates[0]
                    break
        path = entry["taught_in"] if entry else s.get("taught_in")
        if path and path not in pages:
            problems.append(f"{where}: no such page {path}")
            path = None
        if s.get("taught_in") and not s.get("does"):
            problems.append(f"{where}: a service without a glossary entry needs does")
        resolved.append({"service": s, "entry": entry, "path": path})
    return resolved


# --- Rendering ---------------------------------------------------------------------------------


def front_matter(page_id, title, sources=(), facts_checked=None, source_file=""):
    out = [
        "---",
        f"# Generated by source/reference/build_reference.py from {source_file}. Don't edit by hand.",
        "type: reference",
        f"id: {page_id}",
        f'title: "{title}"',
        f'reader: "{READER}"',
        "tasks: []",
        "objectives: []",
        "pillars: []",
    ]
    if facts_checked:
        out.append(f"facts_checked: {facts_checked}")
    if sources:
        out.append("sources:")
        out += [f'  - "{s}"' for s in sources]
    out += ["---", ""]
    return out


def footer(title):
    return ["---", "", attribution(title), ""]


def render_names(entries, rows, checked, pages):
    title = "Names: the exam's and today's"
    from_glossary = sorted(
        (e for e in entries if e.get("exam_name")),
        key=lambda e: (clean(e["exam_name"]).casefold(), e["term"].casefold()),
    )
    sources = []
    for s in [LIFECYCLE] + [r["source"] for r in rows]:
        if s not in sources:
            sources.append(s)
    out = front_matter(
        "clf-99-02", title, sources, checked, "reference/glossary.yaml and reference/names.yaml"
    )
    out += [
        "# The exam's names and today's names, with where the guide teaches each",
        "",
        "AWS renames, splits and retires services faster than the CLF-C02 exam guide changes. This "
        "page lists every name where the exam guide and AWS today disagree, and the older names you'll "
        "meet in other study material, each with the page that teaches it. Use the exam's name to "
        "answer questions and today's name in the console.",
        "",
        f"> **Dated (checked {checked}):** names and statuses change. Before relying on a row, check "
        f"the service's own documentation and AWS's [lifecycle changes]({LIFECYCLE}) list. The "
        "[AWS changes fast](../00-start-here/04-aws-changes-fast.md) page explains the three stages "
        "AWS uses: closed to new customers, end of support and shut down.",
        "",
        "## The exam guide's name differs from today's",
        "",
        f"{len(from_glossary)} names. The exam may still print the left-hand name; the console shows "
        "the middle one.",
        "",
        "| The exam guide says | Today | Taught in |",
        "|---|---|---|",
    ]
    for e in from_glossary:
        out.append(
            f"| {cell(e['exam_name'])} | **{term_link(e['term'])}**: {cell(first_clause(e['definition']))} "
            f"| {page_link(e['taught_in'], pages)} |"
        )
    for key, heading in NAME_SECTIONS.items():
        section = [r for r in rows if r["section"] == key]
        if not section:
            continue
        out += [
            "",
            f"## {heading}",
            "",
            "| Name | Today | Taught in |",
            "|---|---|---|",
        ]
        for r in sorted(section, key=lambda r: r["name"].casefold()):
            name = f"[{r['name']}]({glossary_anchor(r['term'])})" if r.get("term") else r["name"]
            out.append(f"| {cell(name)} | {cell(r['now'])} | {page_link(r['path'], pages)} |")
    out += [""] + footer(title)
    return "\n".join(out)


def confused_groups(entries):
    """The glossary's confused groups, deduplicated: each entry's group (the term and the terms it
    is confused with) folds into the smallest largest group that contains it."""
    canon = {e["term"].casefold(): e["term"] for e in entries}
    by_term = {e["term"]: e for e in entries}
    sets = {}
    for e in entries:
        if e.get("confused_with"):
            members = frozenset([e["term"]] + [canon[o.casefold()] for o in e["confused_with"]])
            sets.setdefault(members, []).append(e)
    maximal = [s for s in sets if not any(s < t for t in sets)]
    order = lambda s: (len(s), sorted(t.casefold() for t in s))
    groups = {}
    for s, stating in sets.items():
        home = min((t for t in maximal if s <= t), key=order)
        groups.setdefault(home, []).extend(stating)
    result = []
    for members, stating in groups.items():
        stating = sorted(stating, key=lambda e: e["term"].casefold())
        module = min(e["module"] for e in stating)
        paths = sorted({by_term[t]["taught_in"] for t in members})
        result.append({
            "members": sorted(members, key=str.casefold),
            "stating": stating,
            "module": module,
            "paths": paths,
        })
    return sorted(result, key=lambda g: (g["module"], [m.casefold() for m in g["members"]]))


def render_confused(entries, pages):
    title = "Commonly confused terms"
    groups = confused_groups(entries)
    titles = module_titles(pages)
    notes = sum(1 for e in entries if e.get("not_to_confuse"))
    out = front_matter("clf-99-03", title, source_file="reference/glossary.yaml")
    out += [
        "# Commonly confused terms, side by side",
        "",
        f"The exam's wrong answers are often a near neighbor of the right one. These {len(groups)} "
        f"groups gather the {notes} \"don't confuse with\" notes in the [glossary](01-glossary.md), "
        "one group per set of look-alikes, under the module that first sets them side by side. Each "
        "term links to its glossary letter; each group ends with the pages that teach its terms.",
        "",
        "**How to use it:** cover the notes, say how the terms differ, then check. A group you can't "
        "explain is the page to reread.",
        "",
    ]
    module = None
    for g in groups:
        if g["module"] != module:
            module = g["module"]
            heading = titles.get(module, "Start here" if module == "00" else f"Module {module}")
            count = sum(1 for x in groups if x["module"] == module)
            if out[-1] != "":
                out.append("")
            out += [f"## {heading}", "", f"{count} groups." if count > 1 else "1 group.", ""]
        out.append("- " + " · ".join(f"**{term_link(t)}**" for t in g["members"]))
        for e in g["stating"]:
            out.append(f"  - {e['term']}: {clean(e['not_to_confuse'])}")
        out.append("  - Taught in: " + "; ".join(page_link(p, pages) for p in g["paths"]))
    out += [""] + footer(title)
    return "\n".join(out)


def render_services(resolved, pages):
    title = "Service map"
    listed = [r for r in resolved if r["service"].get("listed", True)]
    extra = [r for r in resolved if not r["service"].get("listed", True)]
    missing = [r for r in listed if not r["path"]]
    categories = []
    for r in listed:
        if r["service"]["category"] not in categories:
            categories.append(r["service"]["category"])

    out = front_matter(
        "clf-99-04", title, [EXAM_GUIDE], source_file="reference/services.yaml and reference/glossary.yaml"
    )
    out += [
        "# Service map: every in-scope service, what it does and where it is taught",
        "",
        f"The [CLF-C02 exam guide]({EXAM_GUIDE}) lists {len(listed)} in-scope services in "
        f"{len(categories)} categories; AWS says the list may change and isn't complete. This page "
        "gives each one a line: what it does, in a few words from the [glossary](01-glossary.md), and "
        f"the page that teaches it. The guide teaches {len(listed) - len(missing)} of them so far.",
        "",
        "Names are the exam guide's; where AWS has renamed a service, today's name follows in "
        "brackets. The [names page](02-names-exam-vs-current.md) has the details.",
        "",
        "## Not covered yet",
        "",
    ]
    if missing:
        out += [
            f"{len(missing)} in-scope services aren't taught yet. Each is marked \"not covered yet\" "
            "in its category below.",
            "",
        ]
        out += [f"- {r['service']['name']} ({r['service']['category']})" for r in missing]
    else:
        out.append("None: every in-scope service is taught somewhere in the guide.")

    def row(r):
        s, e = r["service"], r["entry"]
        name = s["name"]
        if e:
            name = f"[{name}]({glossary_anchor(e['term'])})"
            if e.get("exam_name") and clean(e["exam_name"]).casefold() == s["name"].casefold():
                name += f" (now {e['term']})"
        if s.get("does"):
            does = clean(s["does"])
        elif e:
            does = first_clause(e["definition"])
        else:
            does = "—"
        if s.get("note"):
            does += f". {clean(s['note'])}"
        where = page_link(r["path"], pages) if r["path"] else "**Not covered yet**"
        return f"| {cell(name)} | {cell(does)} | {where} |"

    for category in categories:
        members = [r for r in listed if r["service"]["category"] == category]
        out += ["", f"## {category}", "", "| Service | What it does | Taught in |", "|---|---|---|"]
        out += [row(r) for r in members]
    if extra:
        out += [
            "",
            "## Needed by the tasks but not on the list",
            "",
            "Task [3.3](" + TASK_URL.format(d=3, t="3.3") + ") asks about load balancers and auto "
            "scaling, which the service list doesn't name.",
            "",
            "| Service | What it does | Taught in |",
            "|---|---|---|",
        ]
        out += [row(r) for r in extra]
    out += [""] + footer(title)
    return "\n".join(out)


def render_blueprint(pages):
    title = "Blueprint map"
    teaching = {p: v for p, v in pages.items() if v["type"] != "reference"}
    overview = [p for p, v in pages.items() if v["type"] == "reference" and v["tasks"]]
    by_task = {t: [p for p, v in teaching.items() if t in v["tasks"]] for t in TASKS}
    unknown = sorted({t for v in teaching.values() for t in v["tasks"]} - set(TASKS))
    untasked = [p for p, v in teaching.items() if not v["tasks"]]

    out = front_matter(
        "clf-99-06",
        title,
        [EXAM_GUIDE] + [DOMAIN_URL.format(d=d) for d in DOMAINS],
        source_file="the front matter of every guide page",
    )
    out += [
        "# Blueprint map: each exam task and the pages that teach it",
        "",
        f"The [CLF-C02 exam guide]({EXAM_GUIDE}) splits the exam into four domains and "
        f"{len(TASKS)} task statements. This page lists, for each task, every page of this guide "
        "that covers it, as each page's front matter declares. The task titles are our short "
        "names; each number links to the task in the exam guide.",
        "",
    ]
    if overview:
        out += [
            " and ".join(page_link(p, pages) for p in overview)
            + " gives an overview of every task, so it isn't repeated below.",
            "",
        ]
    out += [
        "## Summary",
        "",
        "| Task | Our short title | Pages | Lessons | Labs and simulations |",
        "|---|---|---:|---:|---:|",
    ]
    for t, short in TASKS.items():
        ps = by_task[t]
        lessons = sum(1 for p in ps if pages[p]["type"] == "lesson")
        labs = sum(1 for p in ps if pages[p]["type"] in ("lab", "sim"))
        url = TASK_URL.format(d=t[0], t=t)
        out.append(f"| [{t}]({url}) | {short} | {len(ps)} | {lessons} | {labs} |")

    for d, (name, weight) in DOMAINS.items():
        tasks = [t for t in TASKS if t.startswith(d + ".")]
        unique = {p for t in tasks for p in by_task[t]}
        out += [
            "",
            f"## Domain {d}: {name} ({weight}%)",
            "",
            f"[Domain {d} in the exam guide]({DOMAIN_URL.format(d=d)}). {len(unique)} pages cover "
            f"its {len(tasks)} tasks.",
        ]
        for t in tasks:
            ps = by_task[t]
            out += [
                "",
                f"### Task {t}: {TASKS[t]}",
                "",
                f"Task [{t}]({TASK_URL.format(d=d, t=t)}) in the exam guide. "
                + (f"{len(ps)} pages:" if ps else "No page covers it yet."),
            ]
            if ps:
                out.append("")
                out += [f"- {page_link(p, pages)} · {TYPE_LABELS.get(pages[p]['type'], 'Page')}" for p in ps]
    out += [
        "",
        "## Pages that cover no task statement",
        "",
        "These pages prepare you or go beyond the blueprint, so their front matter lists no task.",
        "",
    ]
    out += [f"- {page_link(p, pages)} · {TYPE_LABELS.get(pages[p]['type'], 'Page')}" for p in untasked]
    if unknown:
        out += ["", "Unknown task numbers in front matter: " + ", ".join(unknown) + "."]
    out += [""] + footer(title)
    return "\n".join(out)


# --- Main --------------------------------------------------------------------------------------


def main(argv):
    problems, notes = [], []
    entries = yaml.safe_load(GLOSSARY.read_text(encoding="utf-8"))
    glossary = index_glossary(entries)
    names = yaml.safe_load(NAMES.read_text(encoding="utf-8"))
    services = yaml.safe_load(SERVICES.read_text(encoding="utf-8"))
    pages = read_pages(notes)

    for e in entries:
        if e["taught_in"] not in pages:
            problems.append(f"glossary: {e['term']}: no such page {e['taught_in']}")
    rows = check_names(names, glossary, pages, problems, notes)
    resolved = resolve_services(services, entries, pages, problems)
    for p, v in pages.items():
        for t in v["tasks"]:
            if t not in TASKS:
                problems.append(f"{p}: unknown task {t!r} in front matter")

    for n in notes:
        print(f"note: {n}", file=sys.stderr)
    if problems:
        print(f"{len(problems)} problem(s) in the reference data", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    checked = str(names.get("checked", ""))
    built = {
        "02-names-exam-vs-current.md": render_names(entries, rows, checked, pages),
        "03-commonly-confused.md": render_confused(entries, pages),
        "04-service-map.md": render_services(resolved, pages),
        "06-blueprint-map.md": render_blueprint(pages),
    }
    if "--check" in argv:
        stale = [n for n, text in built.items()
                 if not (OUT / n).is_file() or (OUT / n).read_text(encoding="utf-8") != text]
        for n in stale:
            print(f"guide/99-reference/{n} is out of date; run build_reference.py", file=sys.stderr)
        if stale:
            return 1
        print(f"{len(built)} reference pages are up to date")
        return 0
    for n, text in built.items():
        (OUT / n).write_text(text, encoding="utf-8")
        print(f"wrote guide/99-reference/{n}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
