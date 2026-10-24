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
from chartkit import line_key, make_style, right_rounded, svg, swatch, top_rounded  # noqa: E402

ORDERS = [2, 1, 1, 0, 0, 1, 4, 10, 25, 45, 70, 95, 120, 110, 90, 80, 85, 100, 75, 50, 30, 15, 8, 4]
PER_INSTANCE = 20  # orders an hour one instance handles (Module 02)
MIN, MAX, FIXED = 2, 8, 6
T3_SMALL = 0.0208  # per hour, Linux, on-demand
ALB = 0.0225  # per hour or partial hour

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


def day_cost():
    fixed, scaled, alb = FIXED * 24 * T3_SMALL, sum(RUN) * T3_SMALL, 24 * ALB
    assert (round(fixed, 2), round(scaled, 2), round(alb, 2)) == (3.0, 1.58, 0.54), "must match the model answer"
    rows = [("Fixed fleet: 6 instances, 144 instance-hours", fixed),
            ("Auto Scaling: 76 instance-hours", scaled)]
    w, left, top, pw, rowh, xmax = 680, 16, 100, 470, 60, 4.5
    h = top + rowh * len(rows) + 24
    body = [
        '<text class="title" x="16" y="28">One December Saturday: what the web tier costs</text>',
        '<text class="sub" x="16" y="48">t3.small at $0.0208 an hour, ALB at $0.0225 an hour; US East (N. Virginia), as of 2026-10-24</text>',
    ]
    swatch(body, 16, 76, "s1", "Instances")
    swatch(body, 120, 76, "s2", "Load balancer hours (same in both)")
    sx = lambda v: pw * v / xmax
    for i, (label, inst) in enumerate(rows):
        y = top + i * rowh
        body.append(f'<text class="lab" x="{left}" y="{y + 14}">{label}</text>')
        by = y + 22
        body.append(f'<rect class="s1" x="{left}" y="{by}" width="{sx(inst) - 2:.1f}" height="20"><title>{label}: instances ${inst:.2f}</title></rect>')
        body.append(f'<path class="s2" d="{right_rounded(left + sx(inst), by, sx(alb), 20)}"><title>Load balancer: ${alb:.2f}</title></path>')
        body.append(f'<text class="lab" x="{left + sx(inst + alb) + 8:.1f}" y="{by + 15}">${inst + alb:.2f} (${inst:.2f} + ${alb:.2f})</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top + 18}" y2="{top + rowh * len(rows)}"/>')
    svg("06-07-day-cost.svg", w, h,
        "One day's web-tier cost: a fixed fleet of six against Auto Scaling",
        f"Horizontal stacked bars, prices as of 2026-10-24. Fixed fleet of 6 instances, 144 instance-hours: ${fixed:.2f} "
        f"of instances plus ${alb:.2f} of load balancer hours, ${fixed + alb:.2f}. Auto Scaling, 76 instance-hours: "
        f"${scaled:.2f} plus ${alb:.2f}, ${scaled + alb:.2f}. Load balancer capacity units and data transfer are left out.",
        body, style=STYLE)


if __name__ == "__main__":
    day_capacity()
    day_cost()
