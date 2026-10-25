#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for Simulation S13 (purchasing-option tree) as SVG.

Usage: python3 -I source/charts/11-07-charts.py
Writes images/11-07-*.svg. The hourly instance counts are the made-up December
Saturday from Simulation S7 (guide/06-running-applications/07-sim-elasticity-with-auto-scaling.md).
Prices are US East (N. Virginia), Linux, shared tenancy, from the AWS Price List
offer file for Amazon EC2 retrieved 2026-10-24 (research repo,
sources/raw/pricing/compute-networking-us-east-1-summary.tsv): t3.small On-Demand
$0.0208 an hour; t3.small 1-year Standard Reserved Instance, No Upfront, $0.013 an
hour effective. 8,760 hours a year.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, swatch, top_rounded  # noqa: E402

RUN = [2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 6, 5, 4, 5, 5, 4, 3, 2, 2, 2, 2]  # from S7
OD, RI, YEAR = 0.0208, 0.013, 8760
BASE = 2

STYLE = make_style(rules_extra="""
  .seg-gap { stroke: var(--surface); stroke-width: 2; }
  .vlab { fill: var(--ink); font-size: 12px; font-variant-numeric: tabular-nums; }
  .ann { fill: var(--ink); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")


def baseline():
    assert sum(RUN) == 76
    w, left, top, pw, ph, ymax = 680, 56, 112, 560, 220, 7
    body = [
        '<text class="title" x="16" y="28">Commit to the floor, pay On-Demand for the peaks</text>',
        '<text class="sub" x="16" y="48">The bakery\'s web servers through the December Saturday from Simulation S7 (made-up orders)</text>',
    ]
    swatch(body, 16, 80, "s1", "Baseline: 2 servers every hour, covered by a commitment")
    swatch(body, 420, 80, "s2", "Peak servers, On-Demand")
    for v in range(0, ymax + 1):
        y = top + ph - ph * v / ymax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{y:.1f}" y2="{y:.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{y + 4:.1f}" text-anchor="end">{v}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 14}">Servers running</text>')
    band = pw / 24
    unit = ph / ymax
    bw = 15
    for i, n in enumerate(RUN):
        x = left + band * i + (band - bw) / 2
        b = min(n, BASE)
        extra = n - b
        if extra:
            body.append(f'<rect class="s1" x="{x:.1f}" y="{top + ph - b * unit:.1f}" width="{bw}" height="{b * unit:.1f}"><title>{i:02d}:00: {b} baseline</title></rect>')
            body.append(f'<path class="s2" d="{top_rounded(x, top + ph - n * unit, bw, extra * unit)}"><title>{i:02d}:00: {extra} On-Demand</title></path>')
            body.append(f'<line class="seg-gap" x1="{x:.1f}" x2="{x + bw:.1f}" y1="{top + ph - b * unit:.1f}" y2="{top + ph - b * unit:.1f}"/>')
        else:
            body.append(f'<path class="s1" d="{top_rounded(x, top + ph - b * unit, bw, b * unit)}"><title>{i:02d}:00: {b} baseline</title></path>')
        if i % 3 == 0:
            body.append(f'<text class="tick" x="{left + band * i + band / 2:.1f}" y="{top + ph + 18}" text-anchor="middle">{i:02d}:00</text>')
    xp = left + band * 12.5
    body.append(f'<text class="ann" x="{xp + 20:.1f}" y="{top + ph - 6.6 * unit:.1f}">Noon: 2 committed + 4 On-Demand</text>')
    y = top + ph + 46
    for line in (
        "Of the day's 76 server-hours, 48 sit under the baseline and 28 are peak hours.",
        "Made-up orders from Simulation S7; one server handles about 20 orders an hour, minimum 2.",
    ):
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 15
    svg("11-07-baseline.svg", w, y + 4,
        "Hour-by-hour web servers on a December Saturday, split into a committed baseline and On-Demand peaks",
        "A stacked column chart for 24 hours. Every hour has 2 servers in blue, the baseline covered by a commitment. "
        "From 09:00 to 19:00 extra servers in orange run On-Demand: 1 at 09:00, 2 at 10:00, 3 at 11:00, 4 at noon "
        "and 13:00, 3 at 14:00, 2 at 15:00, 3 at 16:00 and 17:00, 2 at 18:00 and 1 at 19:00. Of the day's 76 "
        "server-hours, 48 are baseline and 28 are peak. Made-up orders from Simulation S7.", body, style=STYLE)


if __name__ == "__main__":
    baseline()
