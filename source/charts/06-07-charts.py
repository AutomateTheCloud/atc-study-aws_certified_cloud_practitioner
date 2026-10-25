#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for Simulation S7 (elasticity with Auto Scaling) as SVG.

Usage: python3 -I source/charts/06-07-charts.py
Writes images/06-07-*.svg. Orders are made-up teaching figures from
guide/06-running-applications/07-sim-elasticity-with-auto-scaling.md, built on the
December peak of 120 orders an hour from Module 02. Prices are US East (N. Virginia),
from the AWS Price List offer files retrieved 2026-10-24 (research repo,
sources/raw/pricing/compute-networking-us-east-1-summary.tsv).
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import line_key, make_style, svg, swatch, top_rounded  # noqa: E402

ORDERS = [2, 1, 1, 0, 0, 1, 4, 10, 25, 45, 70, 95, 120, 110, 90, 80, 85, 100, 75, 50, 30, 15, 8, 4]
PER_INSTANCE = 20  # orders an hour one instance handles (Module 02)
MIN, MAX, FIXED = 2, 8, 6

RUN = [min(MAX, max(MIN, math.ceil(o / PER_INSTANCE))) for o in ORDERS]

STYLE = make_style(rules_extra="""
  .line-dash { stroke: var(--ink2); stroke-width: 1.5; fill: none; stroke-dasharray: 5 4; }""")


def day_capacity():
    assert sum(RUN) == 76 and max(RUN) == 6, "must match the model answer"
    w, h, left, top, pw, ph, ymax = 680, 400, 56, 112, 470, 236, 7
    body = [
        '<text class="title" x="16" y="28">Instances Auto Scaling runs on a December Saturday</text>',
        '<text class="sub" x="16" y="48">Hour by hour, against a fixed fleet sized for the noon peak (made-up orders)</text>',
    ]
    swatch(body, 16, 76, "s1", "Instances running (Auto Scaling)")
    line_key(body, 260, 76, "line-ink", "Fixed fleet: 6 all day")
    line_key(body, 450, 76, "line-dash", "Minimum: 2")
    for v in range(0, ymax + 1):
        y = top + ph - ph * v / ymax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{y:.1f}" y2="{y:.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{y + 4:.1f}" text-anchor="end">{v}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 14}">Instances</text>')
    band = pw / 24
    unit = ph / ymax
    bw = 13
    for i, n in enumerate(RUN):
        x = left + band * i + (band - bw) / 2
        body.append(f'<path class="s1" d="{top_rounded(x, top + ph - n * unit, bw, n * unit)}"><title>{i:02d}:00, {ORDERS[i]} orders: {n} instances</title></path>')
        if i % 3 == 0:
            body.append(f'<text class="tick" x="{left + band * i + band / 2:.1f}" y="{top + ph + 18}" text-anchor="middle">{i:02d}:00</text>')
    for n, cls, label in ((FIXED, "line-ink", "Fixed: 6"), (MIN, "line-dash", "Minimum: 2")):
        y = top + ph - n * unit
        body.append(f'<line class="{cls}" x1="{left}" x2="{left + pw}" y1="{y:.1f}" y2="{y:.1f}"/>')
        body.append(f'<text class="lab" x="{left + pw + 8}" y="{y + 4:.1f}">{label}</text>')
    xn = left + band * 12 + band / 2
    body.append(f'<text class="lab" x="{xn:.1f}" y="{top + ph - 6 * unit - 10:.1f}" text-anchor="middle">noon: 120 orders</text>')
    svg("06-07-day-capacity.svg", w, h,
        "Instances the Auto Scaling group runs each hour, against a fixed fleet of six",
        "Column chart, 24 hours from midnight, made-up orders. Instances running: 2 from midnight to 08:00, then 3, 4, 5, "
        "6 at noon and 6 at 13:00, then 5, 4, 5, 5, 4, 3, and 2 from 20:00 to midnight: 76 instance-hours. "
        "A flat line at 6 shows a fixed fleet sized for the noon peak, 144 instance-hours. A dashed line at 2 marks the minimum, one per Availability Zone.",
        body, style=STYLE)


if __name__ == "__main__":
    day_capacity()
