#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphic for Lab 13 (an Athena query) as SVG.

Usage: python3 -I source/charts/10-04-charts.py
Writes images/10-04-cost-per-query.svg: what one Athena SQL query over data in S3 costs,
by the amount of data it scans, on a log scale. Facts:
- $5 per TB scanned: the worked examples on the Amazon Athena pricing page
  (aws.amazon.com/athena/pricing/), checked 2026-10-24;
- rounded up to the nearest megabyte with a 10 MB minimum per query: stated on the pricing
  page for federated queries, and for all queries in AWS's "Big Data Analytics Options on
  AWS" whitepaper (marked historical), checked 2026-10-24.
Our arithmetic uses 1 TB = 1,000,000 MB, so the figures are approximate.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines  # noqa: E402

STYLE = make_style(rules_extra="""
  .dot-s2 { fill: var(--s2); stroke: var(--surface); stroke-width: 2; }
  .stem { stroke: var(--grid); stroke-width: 2; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

PRICE_PER_TB = 5.0
MIN_MB = 10
# (label, MB actually scanned, highlight)
ROWS = [
    ("This lab's file, under 1 KB", 0.001, True),
    ("10 MB", 10, False),
    ("1 GB", 1_000, False),
    ("100 GB", 100_000, False),
    ("1 TB", 1_000_000, False),
]


def money(v):
    if v >= 1:
        return f"${v:,.2f}"
    if v >= 0.01:
        return f"${v:.2f}"
    s = f"{v:.6f}".rstrip("0")
    return "$" + s


def cost_per_query():
    w = 680
    left, top, pw, rowh = 200, 92, 390, 40
    lo, hi = -5, 1  # log10 of dollars: $0.00001 to $10
    body = [
        '<text class="title" x="16" y="28">What one Athena query costs, by the data it scans</text>',
        '<text class="sub" x="16" y="48">US dollars per query, log scale: each gridline is ten times the one before</text>',
    ]
    nrows = len(ROWS)
    bottom = top + nrows * rowh
    for e in range(lo, hi + 1):
        x = left + pw * (e - lo) / (hi - lo)
        body.append(f'<line class="grid" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 6}" y2="{bottom}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{bottom + 18}" text-anchor="middle">{money(10 ** e)}</text>')
    for i, (lab, mb, hl) in enumerate(ROWS):
        y = top + i * rowh + 14
        billed = max(math.ceil(mb), MIN_MB)
        cost = billed / 1_000_000 * PRICE_PER_TB
        x = left + pw * (math.log10(cost) - lo) / (hi - lo)
        body.append(f'<text class="lab" x="{left - 12}" y="{y + 4}" text-anchor="end">{lab}</text>')
        body.append(f'<line class="stem" x1="{left}" x2="{x:.1f}" y1="{y}" y2="{y}"/>')
        cls = "dot-s2" if hl else "dot-s1"
        tip = f"{lab}: billed as {billed:,} MB, about {money(cost)} per query"
        body.append(f'<circle class="{cls}" cx="{x:.1f}" cy="{y}" r="6"><title>{tip}</title></circle>')
        val = f"about {money(cost)}"
        if hl:
            val += ", billed as 10 MB"
        body.append(f'<text class="lab" x="{x + 12:.1f}" y="{y + 4}">{val}</text>')
    y = bottom + 46
    y = text_lines(body, 16, y, [
        "The orange dot is this lab. Anything under 10 MB is billed as 10 MB, so the lab's tiny file costs",
        "the same as 10 MB. Above that, cost grows in step with the data: a query that reads 1 TB costs $5,",
        "every time it runs. Statements that create or drop tables, and failed queries, are not charged.",
    ], cls="small", dy=17)
    body.append(f'<text class="note" x="16" y="{y + 6}">Per-query pricing: $5 per TB scanned, rounded up to the nearest MB, 10 MB minimum (Amazon Athena pricing,</text>')
    body.append(f'<text class="note" x="16" y="{y + 22}">checked 2026-10-24). S3 storage and requests are billed separately. Our arithmetic; amounts are approximate.</text>')
    h = y + 36
    svg("10-04-cost-per-query.svg", w, h,
        "The cost of one Athena query, by the amount of data it scans",
        "Dot chart on a log scale of US dollars per query, from $0.00001 to $10, at $5 per terabyte scanned with "
        "a 10 megabyte minimum per query. This lab's file, under 1 KB, is highlighted: it is billed as 10 MB and "
        "costs about $0.00005 per query. 10 MB: about $0.00005, the same. 1 GB: about $0.005. 100 GB: about "
        "$0.50. 1 TB: about $5.00. Above the minimum, cost grows in step with the data scanned. Statements that "
        "create or drop tables, and failed queries, are not charged. S3 storage and requests are billed "
        "separately. Prices checked 2026-10-24.",
        body, style=STYLE)


if __name__ == "__main__":
    cost_per_query()
