#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for Simulation S1 (the bakery's cost comparison) as SVG.

Usage: python3 -I source/charts/02-07-charts.py
Writes images/02-07-*.svg. All numbers are the made-up teaching figures from
guide/02-why-the-cloud/07-sim-demand-curve.md; change them here and rerun when
the simulation changes.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import MONTHS, line_key, make_style, month_axes, right_rounded, svg, swatch, top_rounded  # noqa: E402

NEEDED = [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 3, 6]  # servers needed in the busiest hour
OWN_PRICE = 150  # a server-month, owned
RENT = 250  # a server-month, rented
LOST_ORDERS = 8000  # about, with 3 owned servers

STYLE = make_style(rules_extra="""
  .line-ink2 { stroke: var(--ink2); stroke-width: 2; fill: none; stroke-linecap: round; }""")


def money(v):
    return f"${v:,.0f}"


def demand():
    w, h, left, top, pw, ph, ymax = 680, 400, 56, 112, 470, 236, 7
    body = [
        '<text class="title" x="16" y="28">Servers needed each month, against 3 and 6 owned</text>',
        '<text class="sub" x="16" y="48">Servers needed in each month\'s busiest hour (made-up figures)</text>',
    ]
    swatch(body, 16, 76, "s1", "Servers needed")
    line_key(body, 150, 76, "line-ink", "3 owned today")
    line_key(body, 280, 76, "line-ink2", "6 owned for the peak")
    band = month_axes(body, left, top, pw, ph, ymax, "Servers")
    unit = ph / ymax
    bw = 24
    for i, need in enumerate(NEEDED):
        x = left + band * i + (band - bw) / 2
        y = top + ph - need * unit
        body.append(f'<path class="s1" d="{top_rounded(x, y, bw, need * unit)}"><title>{MONTHS[i]}: {need} needed</title></path>')
    for n, cls, label in ((3, "line-ink", "3 owned today"), (6, "line-ink2", "6 owned for the peak")):
        y = top + ph - n * unit
        body.append(f'<line class="{cls}" x1="{left}" x2="{left + pw}" y1="{y:.1f}" y2="{y:.1f}"/>')
        body.append(f'<text class="lab" x="{left + pw + 8}" y="{y + 4:.1f}">{label}</text>')
    svg("02-07-demand.svg", w, h,
        "Servers the bakery needs each month, against 3 and 6 owned servers",
        "Column chart, January to December, servers needed: 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 3, 6. "
        "A flat line at 3 shows today's three owned servers; only December rises above it. "
        "A flat line at 6 shows owning enough for the December peak; every column is at or below it, most far below.",
        body, style=STYLE)


def option_totals():
    sm = sum(NEEDED)
    rows = [
        ("A: Keep 3 owned servers", 3 * OWN_PRICE * 12, LOST_ORDERS),
        ("B: Own 6 servers, enough for the peak", 6 * OWN_PRICE * 12, 0),
        ("C: Cloud, matching each month's need", sm * RENT, 0),
        ("D: Cloud, but 6 servers left running all year", 6 * 12 * RENT, 0),
    ]
    assert [r[1] for r in rows] == [5400, 10800, 6250, 18000], "must match the model answer"
    w, left, top, pw, rowh, xmax = 680, 16, 100, 480, 58, 20000
    h = top + rowh * len(rows) + 24
    body = [
        '<text class="title" x="16" y="28">A year for the bakery under each option</text>',
        '<text class="sub" x="16" y="48">Made-up figures: $150 a server-month owned, $250 rented, about $8,000 of lost orders</text>',
    ]
    swatch(body, 16, 76, "s1", "Yearly cost to run")
    swatch(body, 170, 76, "s2", "Lost orders")
    sx = lambda v: pw * v / xmax
    for i, (label, cost, lost) in enumerate(rows):
        y = top + i * rowh
        body.append(f'<text class="lab" x="{left}" y="{y + 14}">{label}</text>')
        by = y + 22
        if lost:
            body.append(f'<rect class="s1" x="{left}" y="{by}" width="{sx(cost) - 2:.1f}" height="20"><title>{label}: {money(cost)} to run</title></rect>')
            body.append(f'<path class="s2" d="{right_rounded(left + sx(cost), by, sx(lost), 20)}"><title>{label}: about {money(lost)} of lost orders</title></path>')
            end, txt = left + sx(cost + lost), f"{money(cost)} + about {money(lost)} lost"
        else:
            body.append(f'<path class="s1" d="{right_rounded(left, by, sx(cost), 20)}"><title>{label}: {money(cost)} to run</title></path>')
            end, txt = left + sx(cost), money(cost)
        body.append(f'<text class="lab" x="{end + 8:.1f}" y="{by + 15}">{txt}</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top + 18}" y2="{top + rowh * len(rows)}"/>')
    svg("02-07-option-totals.svg", w, h,
        "Yearly total for the bakery's four options",
        "Horizontal bar chart, made-up figures. A, keep 3 owned servers: $5,400 to run plus about $8,000 of lost "
        "orders, about $13,400. B, own 6 servers: $10,800. C, cloud matching each month's need: $6,250. "
        "D, cloud with 6 servers left running all year: $18,000.", body, style=STYLE)


if __name__ == "__main__":
    demand()
    option_totals()
