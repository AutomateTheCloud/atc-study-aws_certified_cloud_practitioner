#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphic for Simulation S2 (choosing DR strategies) as SVG.

Usage: python3 -I source/charts/03-06-charts.py
Writes images/03-06-fit-grid.svg: for three made-up businesses, which of AWS's four
disaster recovery strategies meets each recovery time objective, and which is the
cheapest that does. The strategies' order and typical recovery ranges (hours, tens
of minutes, minutes, real time) come from AWS's disaster recovery whitepaper (2021;
research repo docs/13, A9). The businesses and their objectives are made up.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --no-fill:#f1f0ec; --ok-fill:#d9e8fb;",
    dark_extra=" --no-fill:#252523; --ok-fill:#1b3554;",
    rules_extra="""
  .no { fill: var(--no-fill); stroke: var(--axis); stroke-width: 1; stroke-dasharray: 3 3; }
  .ok { fill: var(--ok-fill); stroke: var(--s1); stroke-width: 1; }
  .pick { fill: var(--ok-fill); stroke: var(--s2); stroke-width: 3; }
  .head { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .rowl { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .rows { fill: var(--ink2); font-size: 11.5px; }
  .cellt { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 11.5px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

COLS = [("Backup and restore", "hours"), ("Pilot light", "tens of minutes"),
        ("Warm standby", "minutes"), ("Multi-site active/active", "real time")]
ROWS = [  # (business, its RTO for losing a Region, first strategy that meets it)
    ("The bakery", "RTO: within a day", 0),
    ("Ticket website", "RTO: about 5 min", 2),
    ("Payment service", "RTO: near zero", 3),
]


def fit_grid():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Which strategy meets each business\'s recovery time?</text>',
        '<text class="sub" x="16" y="48">Choose the cheapest strategy that meets the objective. Businesses and objectives are made up.</text>',
    ]
    left, top, cw, ch, gap = 150, 118, 124, 58, 6
    for j, (name, rng) in enumerate(COLS):
        cx = left + j * (cw + gap) + cw / 2
        text_lines(body, cx, top - 42, wrap(name, 16), cls="head", dy=15, anchor="middle")
        body.append(f'<text class="tick" x="{cx}" y="{top - 6}" text-anchor="middle">{rng}</text>')
    for i, (biz, rto, first) in enumerate(ROWS):
        y = top + i * (ch + gap)
        body.append(f'<text class="rowl" x="16" y="{y + 24}">{biz}</text>')
        body.append(f'<text class="rows" x="16" y="{y + 41}">{rto}</text>')
        for j in range(4):
            x = left + j * (cw + gap)
            if j < first:
                cls, t, s = "no", "Too slow", "misses the RTO"
            elif j == first:
                cls, t, s = "pick", "Choose this", "cheapest that fits"
            else:
                cls, t, s = "ok", "Meets it", "but costs more"
            body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{cw}" height="{ch}" rx="5"/>')
            body.append(f'<text class="cellt" x="{x + cw / 2}" y="{y + 25}" text-anchor="middle">{t}</text>')
            body.append(f'<text class="cells" x="{x + cw / 2}" y="{y + 42}" text-anchor="middle">{s}</text>')
    y = top + 3 * (ch + gap) + 14
    body.append(f'<text class="note" x="16" y="{y}">Columns run from cheapest (left) to most expensive (right). Typical ranges from AWS\'s disaster recovery</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">whitepaper (2021), checked 2026-10-24. Every business also needs point-in-time backups.</text>')
    svg("03-06-fit-grid.svg", w, y + 30,
        "Which disaster recovery strategy meets each business's recovery time objective",
        "A grid of three made-up businesses against AWS's four strategies, ordered from cheapest to most "
        "expensive: backup and restore (hours), pilot light (tens of minutes), warm standby (minutes) and "
        "multi-site active/active (real time). The bakery, RTO within a day: backup and restore is the "
        "choice, the cheapest that meets it; the other three meet it but cost more. Ticket website, RTO about "
        "5 minutes: backup and restore and pilot light are too slow; warm standby is the choice; multi-site "
        "meets it but costs more. Payment service, RTO near zero (no noticeable outage): the first three are too slow; "
        "multi-site active/active is the choice. Every business also needs point-in-time backups.",
        body, style=STYLE)


if __name__ == "__main__":
    fit_grid()
