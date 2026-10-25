#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 13.02 (Seven migration strategies) as SVG.

Usage: python3 -I source/charts/13-02-charts.py
Writes images/13-02-*.svg. Facts come from "About the migration strategies" in
AWS Prescriptive Guidance (Guide for AWS large migrations), checked 2026-10-24:
the seven strategies, their other names, AWS's examples, "relocate is the quickest",
"refactor is the most complex and costly". The Amazon EVS example
comes from AWS's "Migrate VMware to the cloud" page, checked 2026-10-24. The three groups in
the big picture are our own way of organizing the seven, not AWS's.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --aws-fill:#d9e8fb; --hi-fill:#fbe1d6; --card-fill:#f1f0ec; --zone1:#ecebe6; --zone2:#f5f4f0;",
    dark_extra=" --aws-fill:#1b3554; --hi-fill:#4d2716; --card-fill:#252523; --zone1:#2a2a28; --zone2:#222221;",
    rules_extra="""
  .card { fill: var(--card-fill); stroke: var(--axis); stroke-width: 1; }
  .move { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .hi { fill: var(--hi-fill); stroke: var(--s2); stroke-width: 2.5; }
  .hirow { fill: none; stroke: var(--s2); stroke-width: 2.5; }
  .band { fill: none; stroke: var(--axis); stroke-width: 1; stroke-dasharray: 4 3; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .grp { fill: var(--ink); font-size: 12px; font-weight: 700; letter-spacing: 0.3px; }
  .rowl { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .zone1 { fill: var(--zone1); } .zone2 { fill: var(--zone2); }
  .zone { fill: var(--muted); font-size: 11px; font-weight: 600; letter-spacing: 0.5px; }
  .val { fill: var(--ink); font-size: 12px; font-variant-numeric: tabular-nums; }""")


def card(body, cls, x, y, w, h, title, lines):
    body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    body.append(f'<text class="boxt" x="{x + 10}" y="{y + 19}">{title}</text>')
    text_lines(body, x + 10, y + 36, lines, cls="cells", dy=14)


GROUPS = [
    ("DOESN'T MOVE", "card", [
        ("Retire", "Switch it off; archive the data you must keep."),
        ("Retain", "Keep it where it is, for now. Revisit later."),
    ]),
    ("MOVES WITHOUT CHANGING THE APPLICATION", "move", [
        ("Rehost", "Lift and shift: each server, as it is, onto Amazon EC2."),
        ("Relocate", "Move a whole platform, such as VMware, to its AWS version; or move a resource to another VPC, Region or account."),
    ]),
    ("CHANGES ON THE WAY", "card", [
        ("Replatform", "Lift, tinker and shift: a few changes, such as moving the database onto Amazon RDS."),
        ("Repurchase", "Drop and shop: replace it with a different product, often software as a service."),
        ("Refactor", "Re-architect: redesign it to use cloud-native features."),
    ]),
]


def big_picture():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Seven migration strategies, one per application</text>',
        '<text class="sub" x="16" y="48">Grouped by what happens to the application. The grouping is ours; the seven names are AWS\'s.</text>',
    ]
    y = 64
    cw, gap = 210, 8
    for label, cls, items in GROUPS:
        lines = [wrap(text, 30) for _, text in items]
        h = 44 + 14 * max(len(ls) for ls in lines)
        body.append(f'<rect class="band" x="10" y="{y}" width="{w - 20}" height="{h + 34}" rx="8"/>')
        body.append(f'<text class="grp" x="20" y="{y + 19}">{label}</text>')
        for i, ((name, _), ls) in enumerate(zip(items, lines)):
            x = 20 + i * (cw + gap)
            card(body, "hi" if name == "Relocate" else cls, x, y + 28, cw, h, name, ls)
        if label.startswith("MOVES"):
            x = 20 + 2 * (cw + gap)
            text_lines(body, x, y + 50, ["Relocate is the seventh R,", "added after AWS's 2016 list", "of six. Older material", "may leave it out."], cls="small", dy=15)
        y += h + 44
    body.append(f'<text class="note" x="16" y="{y + 4}">From "About the migration strategies", AWS Prescriptive Guidance, checked 2026-10-24.</text>')
    svg("13-02-big-picture.svg", w, y + 20,
        "The seven migration strategies, grouped by what happens to the application",
        "Three groups of cards. Doesn't move: Retire, switch it off and archive the data you must keep; Retain, "
        "keep it where it is, for now, and revisit later. Moves without changing the application: Rehost, lift "
        "and shift, each server as it is onto Amazon EC2; Relocate, highlighted, move a whole platform such as "
        "VMware to its AWS version, or move a resource to another VPC, Region or account. A note says relocate "
        "is the seventh R, added after AWS's 2016 list of six, and older material may leave it out. Changes on the "
        "way: Replatform, lift, tinker and shift, a few changes such as moving the database onto Amazon RDS; "
        "Repurchase, drop and shop, replace it with a different product, often software as a service; Refactor, "
        "re-architect, redesign it to use cloud-native features. The grouping is ours; the seven names are AWS's.",
        body, style=STYLE)


COMPARE = [
    ("Also called", ["Lift and shift", "(no other name)", "Lift, tinker and shift; lift and reshape", "Re-architect"]),
    ("What moves", ["Each server, as it is, onto Amazon EC2",
                    "A whole platform at once, to the AWS version of it; or a resource to another VPC, Region or account",
                    "The application, onto better-fitting services",
                    "The application, rebuilt"]),
    ("What changes in the application", ["Nothing", "Nothing, not even how you operate it",
                                         "A few parts, such as the database host or the operating system",
                                         "Its design, to use cloud-native features"]),
    ("AWS's example", ["An application stack from on-premises to AWS",
                       "VMware workloads to Amazon EVS; an RDS database to another account",
                       "SQL Server to Amazon RDS for SQL Server",
                       "A monolith that slows every release"]),
    ("What AWS says about effort", ["Moves many servers without compatibility worries; optimize later",
                                    "The quickest way to migrate and operate a workload",
                                    "A few or many changes, depending on your goals",
                                    "The most complex and costly strategy"]),
]


def four_compared():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Rehost, relocate, replatform, refactor: how much of the application changes</text>',
        '<text class="sub" x="16" y="48">All four move the application to AWS. Read the highlighted row first.</text>',
    ]
    lw, cw, gap = 104, 134, 6
    xs = [16 + lw + i * (cw + gap) for i in range(4)]
    y = 64
    for x, name in zip(xs, ["Rehost", "Relocate", "Replatform", "Refactor"]):
        body.append(f'<rect class="move" x="{x}" y="{y}" width="{cw}" height="30" rx="6"/>')
        body.append(f'<text class="boxt" x="{x + 10}" y="{y + 20}">{name}</text>')
    y += 38
    for row, cells in COMPARE:
        wrapped = [wrap(c, 19) for c in cells]
        h = 14 + 15 * max(len(c) for c in wrapped) + 4
        if row == "What changes in the application":
            body.append(f'<rect class="hirow" x="{xs[0] - 4}" y="{y + 2}" width="{4 * cw + 3 * gap + 8}" height="{h - 4}" rx="5"/>')
        body.append(f'<line class="grid" x1="16" x2="{xs[3] + cw}" y1="{y}" y2="{y}"/>')
        text_lines(body, 16, y + 19, wrap(row, 14), cls="rowl", dy=15)
        for x, c in zip(xs, wrapped):
            text_lines(body, x + 8, y + 19, c, cls="small", dy=15)
        y += h
    body.append(f'<line class="grid" x1="16" x2="{xs[3] + cw}" y1="{y}" y2="{y}"/>')
    y += 22
    body.append(f'<text class="note" x="16" y="{y}">From AWS Prescriptive Guidance (migration strategies) and AWS\'s VMware page, checked 2026-10-24.</text>')
    svg("13-02-four-rs-compared.svg", w, y + 16,
        "Rehost, relocate, replatform and refactor compared",
        "Four columns, rehost, relocate, replatform and refactor, compared on five rows. Also called: lift and "
        "shift; no other name; lift, tinker and shift, or lift and reshape; re-architect. What moves: each server, "
        "as it is, onto Amazon EC2; a whole platform at once to the AWS version of it, or a resource to another "
        "VPC, Region or account; the application, onto better-fitting services; the application, rebuilt. What "
        "changes in the application, highlighted: nothing; nothing, not even how you operate it; a few parts, "
        "such as the database host or the operating system; its design, to use cloud-native features. AWS's "
        "example: an application stack from on-premises to AWS; VMware workloads to Amazon EVS, or an RDS "
        "database to another account; SQL Server to Amazon RDS for SQL Server; a monolith that slows every "
        "release. What AWS says about effort: moves many servers without compatibility worries, optimize later; "
        "the quickest way to migrate and operate a workload; a few or many changes, depending on your goals; the "
        "most complex and costly strategy.", body, style=STYLE)


if __name__ == "__main__":
    big_picture()
    four_compared()
