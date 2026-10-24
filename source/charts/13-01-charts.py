#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 13.01 (The Cloud Adoption Framework) as SVG.

Usage: python3 -I source/charts/13-01-charts.py
Writes images/13-01-*.svg. Facts come from "An Overview of the AWS Cloud Adoption
Framework" (AWS whitepaper, published 2021-11-22, freshness review 2023-02-19) and
the AWS CAF page, both checked 2026-10-24: the four business outcomes, the four
transformation domains, the six perspectives with their capabilities and common
stakeholders, and the four phases. Capability names are AWS's; the one-line
summaries are ours. Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Neutral cards for every part; slot 1 (blue) tint for the perspectives, the part the
# lesson's objective is about; slot 2 (orange) outline for the one highlighted element.
# Words name every part, so color never carries meaning alone.
STYLE = make_style(
    light_extra=" --aws-fill:#d9e8fb; --hi-fill:#fbe1d6; --card-fill:#f1f0ec;",
    dark_extra=" --aws-fill:#1b3554; --hi-fill:#4d2716; --card-fill:#252523;",
    rules_extra="""
  .persp { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .card { fill: var(--card-fill); stroke: var(--axis); stroke-width: 1; }
  .hi { fill: var(--hi-fill); stroke: var(--s2); stroke-width: 2.5; }
  .hirow { fill: none; stroke: var(--s2); stroke-width: 2.5; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .grp { fill: var(--ink); font-size: 12px; font-weight: 700; letter-spacing: 0.3px; }
  .colh { fill: var(--muted); font-size: 11.5px; font-weight: 600; letter-spacing: 0.5px; }
  .rowl { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .flow { stroke: var(--ink2); stroke-width: 1.8; fill: none; }
  .head-ink { fill: var(--ink2); }""")


def arrow(body, x1, y1, x2, y2):
    """A straight arrow with a filled head at (x2, y2)."""
    a = math.atan2(y2 - y1, x2 - x1)
    ex, ey = x2 - 8 * math.cos(a), y2 - 8 * math.sin(a)
    body.append(f'<path class="flow" d="M{x1:.1f},{y1:.1f} L{ex:.1f},{ey:.1f}"/>')
    p1 = (x2 - 10 * math.cos(a) + 5 * math.sin(a), y2 - 10 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 10 * math.cos(a) - 5 * math.sin(a), y2 - 10 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="head-ink" d="M{x2:.1f},{y2:.1f} L{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z"/>')


def box(body, cls, x, y, w, h, title, lines=(), width=None):
    body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    text_lines(body, x + 10, y + 19, wrap(title, width or 40), cls="boxt", dy=16)
    n = len(wrap(title, width or 40))
    text_lines(body, x + 10, y + 19 + 16 * n, list(lines), cls="cells", dy=14)


OUTCOMES = [
    ("Reduce business risk", "reliability, performance, security"),
    ("Improve ESG performance", "sustainability, transparency"),
    ("Grow revenue", "new products, customers, markets"),
    ("Increase operational efficiency", "lower costs, more productivity"),
]
DOMAINS = [
    ("Technology", "migrate and modernize"),
    ("Process", "digitize, automate, optimize"),
    ("Organization", "teams around products"),
    ("Product", "new offers, revenue models"),
]
PERSPECTIVES = [
    ("Business", "strategy and outcomes", 8),
    ("People", "culture and change", 7),
    ("Governance", "control and oversight", 7),
    ("Platform", "infrastructure and applications", 7),
    ("Security", "compliance and assurance", 9),
    ("Operations", "health and availability", 9),
]


def big_picture():
    w = 680
    body = [
        '<text class="title" x="16" y="28">The AWS CAF in one picture: capabilities enable change, change delivers outcomes</text>',
        '<text class="sub" x="16" y="48">Read from the bottom up. The four phases on the right repeat for each round of change.</text>',
    ]
    left, inner = 16, 500
    # Business outcomes
    y = 74
    body.append(f'<text class="grp" x="{left}" y="{y}">BUSINESS OUTCOMES: WHY THE ORGANIZATION CHANGES</text>')
    y += 10
    bw = (inner - 3 * 8) / 4
    for i, (name, line) in enumerate(OUTCOMES):
        x = left + i * (bw + 8)
        box(body, "card", x, y, bw, 100, name, wrap(line, 16), width=15)
    y += 100
    arrow(body, left + inner / 2, y + 28, left + inner / 2, y + 6)
    body.append(f'<text class="small" x="{left + inner / 2 + 10}" y="{y + 22}">deliver</text>')
    # Transformation domains
    y += 46
    body.append(f'<text class="grp" x="{left}" y="{y}">TRANSFORMATION DOMAINS: WHAT CHANGES, EACH ENABLING THE NEXT</text>')
    y += 10
    dw = (inner - 3 * 22) / 4
    for i, (name, line) in enumerate(DOMAINS):
        x = left + i * (dw + 22)
        cls = "hi" if name == "Process" else "card"
        box(body, cls, x, y, dw, 66, name, wrap(line, 15), width=15)
        if i < 3:
            arrow(body, x + dw + 2, y + 33, x + dw + 20, y + 33)
    body.append(f'<text class="small" x="{left + dw + 22 + 10}" y="{y + 86}">Process is a domain, not a perspective</text>')
    y += 66
    arrow(body, left + inner / 2, y + 44, left + inner / 2, y + 26)
    body.append(f'<text class="small" x="{left + inner / 2 + 10}" y="{y + 42}">enable</text>')
    # Perspectives
    y += 64
    body.append(f'<text class="grp" x="{left}" y="{y}">SIX PERSPECTIVES: WHO MUST BE READY (CAPABILITIES IN EACH)</text>')
    y += 10
    pw = (inner - 2 * 8) / 3
    for i, (name, focus, n) in enumerate(PERSPECTIVES):
        x = left + (i % 3) * (pw + 8)
        yy = y + (i // 3) * 70
        box(body, "persp", x, yy, pw, 62, f"{name} ({n})", wrap(focus, 22), width=22)
    y += 140
    # Phases column
    px, pwid = left + inner + 24, w - (left + inner + 24) - 16
    py = 84
    body.append(f'<text class="grp" x="{px}" y="{py - 10}">PHASES, REPEATED</text>')
    phases = [("Envision", "pick outcomes"), ("Align", "find gaps"), ("Launch", "run pilots"), ("Scale", "expand, sustain")]
    ph, pg = 62, 30
    for i, (name, line) in enumerate(phases):
        yy = py + i * (ph + pg)
        box(body, "card", px, yy, pwid, ph, name, [line], width=16)
        if i < 3:
            arrow(body, px + pwid / 2, yy + ph + 2, px + pwid / 2, yy + ph + pg - 2)
    loop_y = py + 4 * ph + 3 * pg + 22
    body.append(f'<text class="small" x="{px}" y="{loop_y}">then back to</text>')
    body.append(f'<text class="small" x="{px}" y="{loop_y + 16}">Envision for the</text>')
    body.append(f'<text class="small" x="{px}" y="{loop_y + 32}">next round</text>')
    y += 22
    body.append(f'<text class="note" x="16" y="{y}">Our drawing of the AWS CAF whitepaper (2021) and the AWS CAF page, checked 2026-10-24.</text>')
    svg("13-01-big-picture.svg", w, y + 18,
        "The parts of the AWS Cloud Adoption Framework and how they relate",
        "Three layers, read from the bottom up, and a column of phases. Bottom layer, six perspectives, each with "
        "its number of capabilities: Business (8), strategy and outcomes; People (7), culture and change; "
        "Governance (7), control and oversight; Platform (7), infrastructure and applications; Security (9), "
        "compliance and assurance; Operations (9), health and availability. An arrow labeled enable leads up to the "
        "middle layer, four transformation domains in a chain, each enabling the next: Technology (migrate and "
        "modernize), Process (digitize, automate, optimize; highlighted, with the note that process is a domain, "
        "not a perspective), Organization (teams around products), Product (new offers and revenue models). An "
        "arrow labeled deliver leads up to the top layer, four business outcomes: reduce business risk "
        "(reliability, performance, security); improve ESG performance (sustainability, transparency); grow "
        "revenue (new products, customers, markets); increase operational efficiency (lower costs, more "
        "productivity). On the right, four phases in order: Envision (pick outcomes), Align (find gaps), Launch "
        "(run pilots), Scale (expand, sustain), then back to Envision for the next round.", body, style=STYLE)


BG_ROWS = [
    ("Focus", "Strategy and outcomes: make sure cloud spending speeds up the business's goals",
     "Control and oversight: run the cloud initiatives so the benefits arrive and the risks stay small"),
    ("Common stakeholders", "CEO, CFO, COO, CIO, CTO",
     "Chief transformation officer, CIO, CTO, CFO, chief data officer, chief risk officer"),
    ("The question it answers", "What should we change, in what order, and why is it worth it?",
     "Is the change being delivered as planned, are the benefits real, and is spending under control?"),
    ("Portfolio and money", "Portfolio management: choose and order the initiatives, using the 7 Rs to build the business case",
     "Cloud financial management, benefits management, application portfolio management: track spend and licenses, measure results, keep the inventory"),
    ("All its capabilities", "Strategy, portfolio, innovation and product management; strategic partnership; data monetization; business insights; data science",
     "Program and project management; benefits, risk and cloud financial management; application portfolio management; data governance; data curation"),
]


def business_vs_governance():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Business or Governance: deciding what to do, or overseeing how it goes</text>',
        '<text class="sub" x="16" y="48">The CFO and CIO appear in both. Sort a concern by the capability it needs, not the job title.</text>',
    ]
    lw = 132
    cw, gap = 254, 8
    xs = [16 + lw + i * (cw + gap) for i in range(2)]
    y = 66
    for x, name in zip(xs, ["Business perspective (8)", "Governance perspective (7)"]):
        body.append(f'<rect class="persp" x="{x}" y="{y}" width="{cw}" height="32" rx="6"/>')
        body.append(f'<text class="boxt" x="{x + 10}" y="{y + 21}">{name}</text>')
    y += 40
    for row, b, g in BG_ROWS:
        cells = [wrap(b, 36), wrap(g, 36)]
        h = 14 + 15 * max(len(c) for c in cells) + 4
        hi = row == "Portfolio and money"
        if hi:
            body.append(f'<rect class="hirow" x="{xs[0] - 4}" y="{y + 2}" width="{2 * cw + gap + 8}" height="{h - 4}" rx="5"/>')
        body.append(f'<line class="grid" x1="16" x2="{xs[1] + cw}" y1="{y}" y2="{y}"/>')
        text_lines(body, 16, y + 19, wrap(row, 17), cls="rowl", dy=15)
        for x, c in zip(xs, cells):
            text_lines(body, x + 10, y + 19, c, cls="small", dy=15)
        y += h
    body.append(f'<line class="grid" x1="16" x2="{xs[1] + cw}" y1="{y}" y2="{y}"/>')
    y += 22
    body.append(f'<text class="note" x="16" y="{y}">Capability names and stakeholders from the AWS CAF whitepaper (2021), checked 2026-10-24; the summaries are ours.</text>')
    svg("13-01-business-vs-governance.svg", w, y + 16,
        "The Business and Governance perspectives of the AWS CAF compared",
        "Two columns, Business perspective with eight capabilities and Governance perspective with seven, compared "
        "on five rows. Focus: Business is strategy and outcomes, making sure cloud spending speeds up the "
        "business's goals; Governance is control and oversight, running the cloud initiatives so the benefits "
        "arrive and the risks stay small. Common stakeholders: Business, CEO, CFO, COO, CIO and CTO; Governance, "
        "chief transformation officer, CIO, CTO, CFO, chief data officer and chief risk officer. The question it "
        "answers: Business, what should we change, in what order, and why is it worth it; Governance, is the "
        "change being delivered as planned, are the benefits real, and is spending under control. Portfolio and "
        "money, highlighted: Business has portfolio management, choosing and ordering the initiatives and using "
        "the 7 Rs to build the business case; Governance has cloud financial management, benefits management and "
        "application portfolio management, tracking spend and licenses, measuring results and keeping the "
        "inventory. All capabilities: Business, strategy management, portfolio management, innovation management, "
        "product management, strategic partnership, data monetization, business insights, data science; "
        "Governance, program and project management, benefits management, risk management, cloud financial "
        "management, application portfolio management, data governance, data curation. The subtitle notes that "
        "the CFO and CIO appear in both, so sort a concern by the capability it needs, not the job title.",
        body, style=STYLE)


if __name__ == "__main__":
    big_picture()
    business_vs_governance()
