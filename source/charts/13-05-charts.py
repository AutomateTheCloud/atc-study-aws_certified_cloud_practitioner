#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for Simulation S16 (the chain's application portfolio) as SVG.

Usage: python3 -I source/charts/13-05-charts.py
Writes images/13-05-strategy-map.svg (the model answer to Decision 1: the ten applications
under the seven strategies) and images/13-05-business-vs-governance.svg (the two CAF
perspectives learners confuse, side by side). Strategy names from AWS Prescriptive Guidance,
"About the migration strategies"; perspective capabilities from "An Overview of the AWS Cloud
Adoption Framework" (2021), both retrieved 2026-10-24. The applications are made up.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Group tints: neutral = doesn't move, slot 1 (blue) tint = moves as it is, slot 2 (orange)
# tint = changes on the way. Every group is also named in text, so color is never alone.
STYLE = make_style(
    light_extra=" --g1:#f1f0ec; --g2:#d9e8fb; --g3:#fbe1d6; --card:#fcfcfb;",
    dark_extra=" --g1:#252523; --g2:#1b3554; --g3:#4d2716; --card:#1a1a19;",
    rules_extra="""
  .g1 { fill: var(--g1); stroke: var(--muted); stroke-width: 1; }
  .g2 { fill: var(--g2); stroke: var(--s1); stroke-width: 1.2; }
  .g3 { fill: var(--g3); stroke: var(--s2); stroke-width: 1.2; }
  .card { fill: var(--card); stroke: var(--ink2); stroke-width: 1; }
  .flow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 700; }
  .chip { fill: var(--ink); font-size: 12px; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

DEFS = ('<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        'orient="auto-start-reverse"><path class="arrowhead" d="M0,0 L10,5 L0,10 Z"/></marker></defs>')

COLUMNS = [
    ("Retire", ["Recipe archive"]),
    ("Retain", ["Oven control", "Accounting"]),
    ("Rehost", ["Stock and ordering"]),
    ("Relocate", ["Shop tools"]),
    ("Replatform", ["Loyalty database", "Chain website"]),
    ("Repurchase", ["Email and calendars", "Payroll"]),
    ("Refactor", ["Wholesale portal, after a rehost"]),
]
GROUPS = [("Doesn't move to AWS", 0, 2, "g1"), ("Moves as it is", 2, 4, "g2"), ("Changes on the way", 4, 7, "g3")]


def strategy_map():
    """The ten applications in seven columns, grouped by how much the application changes."""
    left, col_w, gap = 16, 92, 6
    w = left * 2 + 7 * col_w + 6 * gap
    body = [DEFS,
            '<text class="title" x="16" y="28">The chain\'s ten applications by migration strategy</text>',
            '<text class="sub" x="16" y="48">Model answer to Decision 1. Columns run from no move to the most change.</text>']
    top = 66
    gh = 64 + 2 * (44 + 8) + 4
    for label, a, b, cls in GROUPS:
        x = left + a * (col_w + gap)
        gw = (b - a) * col_w + (b - a - 1) * gap
        body.append(f'<rect class="{cls}" x="{x}" y="{top}" width="{gw}" height="{gh}" rx="7"/>')
        body.append(f'<text class="head" x="{x + gw / 2:.1f}" y="{top + 22}" text-anchor="middle">{label}</text>')
    for i, (name, apps) in enumerate(COLUMNS):
        x = left + i * (col_w + gap)
        body.append(f'<text class="boxt" x="{x + col_w / 2:.1f}" y="{top + 50}" text-anchor="middle">{name}</text>')
        y = top + 64
        for app in apps:
            lines = wrap(app, 12)
            h = 14 + 15 * len(lines)
            body.append(f'<rect class="card" x="{x + 4}" y="{y}" width="{col_w - 8}" height="{h}" rx="5"/>')
            text_lines(body, x + col_w / 2, y + 18, lines, cls="chip", dy=15, anchor="middle")
            y += h + 8
    ay = top + gh + 26
    body.append(f'<line class="flow" x1="{left + 10}" x2="{w - left - 10}" y1="{ay}" y2="{ay}" marker-end="url(#arr)"/>')
    body.append(f'<text class="small" x="{left + 10}" y="{ay + 20}">Less change to the application</text>')
    body.append(f'<text class="small" x="{w - left - 10}" y="{ay + 20}" text-anchor="end">More change</text>')
    text_lines(body, 16, ay + 46, wrap("The applications are made up. Repurchase replaces the application with a "
                                        "product; only its data moves. The wholesale portal moves as it is first "
                                        "and is refactored once it runs on AWS.", 110), cls="note", dy=16)
    svg("13-05-strategy-map.svg", w, ay + 80,
        "The chain's ten applications sorted into the seven migration strategies",
        "Seven columns in three groups, ordered from less to more change to the application. Doesn't move to "
        "AWS: Retire holds the recipe archive; Retain holds oven control and accounting. Moves as it is: Rehost "
        "holds stock and ordering; Relocate holds the shop tools. Changes on the way: Replatform holds the "
        "loyalty database and the chain website; Repurchase holds email and calendars, and payroll; Refactor "
        "holds the wholesale portal, after a rehost. A note says repurchase replaces the application with a "
        "product, so only its data moves, and that the wholesale portal moves as it is first and is "
        "refactored once it runs on AWS.",
        body, style=STYLE)


def business_vs_governance():
    """Two CAF perspectives side by side: what each asks, example capabilities, the chain's concerns."""
    w, pw, gap = 680, 316, 16
    body = ['<text class="title" x="16" y="28">Business or Governance? Two perspectives learners mix up</text>',
            '<text class="sub" x="16" y="48">Example capabilities from the AWS CAF overview (2021); the concerns are from Decision 2.</text>']
    panels = [
        ("Business", "g3", "Are we investing in the right things for the business?",
         ["Strategy management", "Portfolio management", "Product management"],
         ["c: Which projects help us win five times the café customers?"]),
        ("Governance", "g2", "Is the work on plan, on budget and within its risk limits, and is it paying off?",
         ["Program and project management", "Benefits management", "Risk management", "Cloud financial management"],
         ["a: How will we know the move paid off?", "g: How do we track the schedule and the risks?"]),
    ]
    for i, (name, cls, question, caps, chain) in enumerate(panels):
        x = 16 + i * (pw + gap)
        body.append(f'<rect class="{cls}" x="{x}" y="64" width="{pw}" height="300" rx="8"/>')
        body.append(f'<text class="head" x="{x + 14}" y="88">{name}</text>')
        y = text_lines(body, x + 14, 112, wrap(question, 40), cls="boxt", dy=17)
        body.append(f'<text class="small" x="{x + 14}" y="{y + 8}">Example capabilities</text>')
        y += 28
        for cap in caps:
            body.append(f'<text class="chip" x="{x + 22}" y="{y}">• {cap}</text>')
            y += 18
        body.append(f'<rect class="card" x="{x + 10}" y="282" width="{pw - 20}" height="72" rx="5"/>')
        body.append(f'<text class="small" x="{x + 20}" y="300">The chain\'s concerns</text>')
        text_lines(body, x + 20, 318, [ln for c in chain for ln in wrap(c, 46)], cls="chip", dy=16)
    svg("13-05-business-vs-governance.svg", w, 380,
        "Business and Governance perspectives of the AWS Cloud Adoption Framework compared",
        "Two panels. Business asks whether the organization is investing in the right things for the business; "
        "example capabilities: strategy management, portfolio management, product management; the chain's "
        "concern c, which projects help win five times the café customers. Governance asks whether the work is on plan, on budget "
        "and within its risk limits, and whether it is paying off; example capabilities: program and project "
        "management, benefits management, risk management, cloud financial management; the chain's concerns a, "
        "how to know the move paid off, and g, how to track the schedule and the risks.",
        body, style=STYLE)


if __name__ == "__main__":
    strategy_map()
    business_vs_governance()
