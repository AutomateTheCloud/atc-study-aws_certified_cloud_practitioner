#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the chart for Lab 16 (cost allocation tags) as SVG.

Usage: python3 -I source/charts/11-06-charts.py
Writes images/11-06-not-retroactive.svg. The daily costs are made-up teaching
figures for the bakery. The behavior shown follows "Activating user-defined cost
allocation tags" and "Using user-defined cost allocation tags" in the AWS Billing
User Guide, checked 2026-10-24: a tag key must be activated before it appears in
cost reports, activation can take up to 24 hours, and costs from before activation
carry no tag value unless a management account requests a backfill.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, swatch, top_rounded  # noqa: E402

# (day label, tagged dollars, untagged dollars); the key becomes active from day 6
DAYS = [("1", 0, 19.8), ("2", 0, 20.4), ("3", 0, 20.1), ("4", 0, 19.6), ("5", 0, 20.2),
        ("6", 16.6, 3.5), ("7", 17.1, 3.4), ("8", 16.4, 3.6), ("9", 16.9, 3.5), ("10", 16.7, 3.4)]
ACTIVE_FROM = 5  # index of day 6

STYLE = make_style(rules_extra="""
  .untag { fill: var(--muted); }
  .seg-gap { stroke: var(--surface); stroke-width: 2; }
  .mark { stroke: var(--ink); stroke-width: 1.5; stroke-dasharray: 4 4; }
  .ann { fill: var(--ink); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")


def not_retroactive():
    w, left, top, pw, ph, ymax = 680, 56, 120, 560, 220, 25
    body = [
        '<text class="title" x="16" y="28">A tag shows costs only from the day it is active</text>',
        '<text class="sub" x="16" y="48">The bakery\'s daily cost in Cost Explorer, grouped by its "team" tag (made-up figures)</text>',
    ]
    swatch(body, 16, 80, "s1", "Cost that carries a team tag value")
    swatch(body, 300, 80, "untag", "Cost with no tag value (shown as no tag key)")
    for v in range(0, ymax + 1, 5):
        y = top + ph - ph * v / ymax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{y:.1f}" y2="{y:.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{y + 4:.1f}" text-anchor="end">${v}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 14}">Dollars a day</text>')
    band = pw / len(DAYS)
    bw = 30
    unit = ph / ymax
    for i, (d, tagged, untagged) in enumerate(DAYS):
        x = left + band * i + (band - bw) / 2
        base = top + ph
        if tagged:
            body.append(f'<rect class="s1" x="{x:.1f}" y="{base - tagged * unit:.1f}" width="{bw}" height="{tagged * unit:.1f}"><title>Day {d}: ${tagged:.2f} tagged</title></rect>')
            base -= tagged * unit
            body.append(f'<line class="seg-gap" x1="{x:.1f}" x2="{x + bw:.1f}" y1="{base:.1f}" y2="{base:.1f}"/>')
        body.append(f'<path class="untag" d="{top_rounded(x, base - untagged * unit, bw, untagged * unit)}"><title>Day {d}: ${untagged:.2f} with no tag value</title></path>')
        body.append(f'<text class="tick" x="{left + band * i + band / 2:.1f}" y="{top + ph + 18}" text-anchor="middle">Day {d}</text>')
    xm = left + band * ACTIVE_FROM
    body.append(f'<line class="mark" x1="{xm:.1f}" x2="{xm:.1f}" y1="{top - 10}" y2="{top + ph}"/>')
    body.append(f'<text class="ann" x="{xm + 6:.1f}" y="{top - 14}">Key active from day 6</text>')
    body.append(f'<text class="ann" x="{xm - 6:.1f}" y="{top - 14}" text-anchor="end">Activated on day 5</text>')
    y = top + ph + 46
    for line in (
        "Days 1 to 5 stay untagged in the report even though the resources carried the tag all along.",
        "Unless a management account requests a backfill. After activation, costs from untagged resources still show no value.",
        "Made-up figures. Behavior per the AWS Billing User Guide, checked 2026-10-24.",
    ):
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 15
    svg("11-06-not-retroactive.svg", w, y + 4,
        "Daily cost grouped by a tag, before and after the tag key is activated",
        "A stacked column chart of the bakery's daily cost over ten days, made-up figures of about $20 a day. On days "
        "1 to 5 every column is one gray segment: cost with no tag value. The tag key is activated on day 5 and is "
        "active from day 6. From day 6 to day 10 each column splits into about $17 that carries a team tag value, in "
        "blue, and about $3.50 with no tag value, in gray. A note says days 1 to 5 stay untagged in the report even "
        "though the resources carried the tag, unless a management account requests a backfill, and that costs from "
        "untagged resources still show no tag value after activation.", body, style=STYLE)


if __name__ == "__main__":
    not_retroactive()
