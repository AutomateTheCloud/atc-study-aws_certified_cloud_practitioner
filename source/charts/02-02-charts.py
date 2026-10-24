#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for lesson 02.02 (the bakery's demand curve) as SVG.

Usage: python3 -I source/charts/02-02-charts.py
Writes images/02-02-*.svg. All numbers are the made-up teaching figures from
guide/02-why-the-cloud/00-brief.md and 02-before-and-after-the-demand-curve.md;
change them here and rerun when the lesson changes.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import MONTHS, line_key, month_axes, right_rounded, svg, swatch, top_rounded  # noqa: E402

NEEDED = [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 3, 6]  # servers needed in the busiest hour
OWNED = 3
PRICE = 150  # made-up cost of one server for one month, owned or rented
LOST_SALES = 8000  # made-up value of December orders turned away


def demand_vs_owned():
    w, h, left, top, pw, ph, ymax = 680, 400, 56, 112, 520, 236, 6
    body = [
        '<text class="title" x="16" y="28">The bakery owns 3 servers; demand needs 1 to 6</text>',
        '<text class="sub" x="16" y="48">Servers needed in each month\'s busiest hour (made-up figures)</text>',
    ]
    swatch(body, 16, 76, "s1", "Owned and used")
    swatch(body, 150, 76, "s1l", "Owned but idle")
    swatch(body, 280, 76, "s2", "Needed but not owned: lost sales")
    line_key(body, 520, 76, "line-ink", "Servers owned")
    band = month_axes(body, left, top, pw, ph, ymax, "Servers")
    bw = 24
    unit = ph / ymax
    gap = 2
    for i, need in enumerate(NEEDED):
        x = left + band * i + (band - bw) / 2
        used = min(need, OWNED)
        segs = [("s1", used, "used"), ("s1l", OWNED - used, "idle"), ("s2", max(need - OWNED, 0), "lost")]
        segs = [s for s in segs if s[1] > 0]
        y0 = top + ph
        for j, (cls, n, kind) in enumerate(segs):
            y = y0 - n * unit
            hh = n * unit - (gap if j > 0 else 0)
            tip = f"{MONTHS[i]}: {n} server{'s' if n > 1 else ''} {kind}"
            if j == len(segs) - 1:
                body.append(f'<path class="{cls}" d="{top_rounded(x, y, bw, hh)}"><title>{tip}</title></path>')
            else:
                body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{bw}" height="{hh:.1f}"><title>{tip}</title></rect>')
            y0 = y
    yo = top + ph - OWNED * unit
    body.append(f'<line class="line-ink" x1="{left}" x2="{left + pw}" y1="{yo:.1f}" y2="{yo:.1f}"/>')
    body.append(f'<text class="lab" x="{left + pw + 8}" y="{yo + 4:.1f}">3 owned</text>')
    # selective direct labels: one idle month, the lost-sales peak
    xj = left + band / 2
    body.append(f'<line class="lead" x1="{xj:.1f}" y1="{yo + unit:.1f}" x2="{xj:.1f}" y2="{yo - unit - 14:.1f}"/>')
    body.append(f'<text class="lab" x="{xj - 8:.1f}" y="{yo - unit - 20:.1f}">January: 2 of the 3 owned servers idle</text>')
    xd = left + band * 11 + (band - 24) / 2
    body.append(f'<line class="lead" x1="{xd - 4:.1f}" y1="{yo - 1.5 * unit:.1f}" x2="{xd - 16:.1f}" y2="{yo - 1.5 * unit:.1f}"/>')
    body.append(f'<text class="lab" x="{xd - 20:.1f}" y="{yo - 1.5 * unit + 4:.1f}" text-anchor="end">December: 3 servers short</text>')
    svg("02-02-demand-vs-owned.svg", w, h,
        "Servers needed each month compared with the 3 the bakery owns",
        "Column chart, January to December. Servers needed: 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 3, 6. "
        "A flat line at 3 shows the servers owned. Below the line, the unused part of each column is idle capacity; "
        "in December, 3 more servers are needed than owned, which is lost sales.", body)


def capacity_in_cloud():
    w, h, left, top, pw, ph, ymax = 680, 400, 56, 112, 520, 236, 6
    body = [
        '<text class="title" x="16" y="28">In the cloud, rented servers follow demand</text>',
        '<text class="sub" x="16" y="48">Servers needed and servers rented, each month (made-up figures)</text>',
    ]
    swatch(body, 16, 74, "s1", "Servers needed")
    body.append('<circle class="dot-s1" cx="176" cy="70" r="5" style="fill:var(--ink)"/>')
    body.append('<text x="188" y="74">Servers rented</text>')
    band = month_axes(body, left, top, pw, ph, ymax, "Servers")
    unit = ph / ymax
    for i, need in enumerate(NEEDED):
        x = left + band * i + (band - 24) / 2
        y = top + ph - need * unit
        body.append(f'<path class="s1" d="{top_rounded(x, y, 24, need * unit)}"><title>{MONTHS[i]}: {need} needed, {need} rented</title></path>')
        body.append(f'<circle cx="{x + 12:.1f}" cy="{y:.1f}" r="5" style="fill:var(--ink);stroke:var(--surface);stroke-width:2"><title>{MONTHS[i]}: {need} rented</title></circle>')
    xd = left + band * 11 + band / 2
    body.append(f'<text class="lab" x="{xd - 18:.1f}" y="{top + ph - 6 * unit + 4:.1f}" text-anchor="end">6 rented in December</text>')
    svg("02-02-capacity-in-cloud.svg", w, h,
        "In the cloud, servers rented match servers needed every month",
        "Column chart, January to December, servers needed: 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 3, 6. "
        "A dot on top of every column shows servers rented, always equal to servers needed: no idle servers and no lost sales.", body)


def monthly_cost():
    w, h, left, top, pw, ph, ymax = 680, 400, 64, 112, 500, 236, 1000
    body = [
        '<text class="title" x="16" y="28">Fixed expense stays flat; variable expense follows use</text>',
        '<text class="sub" x="16" y="48">The bakery\'s server cost each month, at a made-up $150 a server-month</text>',
    ]
    line_key(body, 16, 74, "line-ink", "Own 3 servers (fixed)")
    line_key(body, 200, 74, "line-s1", "Rent what each month needs (variable)")
    band = month_axes(body, left, top, pw, ph, ymax, "$ a month", fmt=lambda v: f"${v:,}", step=250)
    xs = [left + band * i + band / 2 for i in range(12)]
    yv = lambda v: top + ph - ph * v / ymax
    owned = [OWNED * PRICE] * 12
    cloud = [n * PRICE for n in NEEDED]
    body.append('<polyline class="line-ink" points="' + " ".join(f"{x:.1f},{yv(v):.1f}" for x, v in zip(xs, owned)) + '"/>')
    body.append('<polyline class="line-s1" points="' + " ".join(f"{x:.1f},{yv(v):.1f}" for x, v in zip(xs, cloud)) + '"/>')
    for x, v, m in zip(xs, cloud, MONTHS):
        body.append(f'<circle class="dot-s1" cx="{x:.1f}" cy="{yv(v):.1f}" r="4"><title>{m}: ${v:,} renting, ${OWNED * PRICE:,} owning</title></circle>')
    body.append(f'<text class="lab" x="{xs[-1] + 10:.1f}" y="{yv(450) + 4:.1f}">$450 owned</text>')
    body.append(f'<text class="lab" x="{xs[-1] - 10:.1f}" y="{yv(900) - 10:.1f}" text-anchor="end">$900 rented</text>')
    body.append(f'<text class="lab" x="{xs[0]:.1f}" y="{yv(150) + 22:.1f}">$150 rented</text>')
    body.append(f'<text class="sub" x="16" y="{h - 14}">Year total: $5,400 owning; $3,750 renting what each month needs.</text>')
    svg("02-02-monthly-cost.svg", w, h,
        "Monthly server cost: owning 3 servers versus renting what each month needs",
        "Line chart, January to December. Owning 3 servers costs $450 every month. Renting what each month needs costs "
        "$150, 150, 300, 300, 300, 300, 150, 150, 300, 300, 450 and 900. Year totals: $5,400 owning, $3,750 renting.", body)


def annual_cost():
    rows = [
        ("Own 3 servers (today)", 3 * 12 * PRICE, LOST_SALES),
        ("Own 6 servers", 6 * 12 * PRICE, 0),
        ("Cloud, rent 6 all year", 6 * 12 * PRICE, 0),
        ("Cloud, rent what each month needs", sum(NEEDED) * PRICE, 0),
    ]
    w, left, top, pw, rowh, xmax = 680, 16, 100, 440, 58, 14000
    h = top + rowh * len(rows) + 40
    body = [
        '<text class="title" x="16" y="28">A year for the bakery: server cost and lost sales</text>',
        '<text class="sub" x="16" y="48">Made-up figures: $150 a server-month; about $8,000 of December orders lost with 3 servers</text>',
    ]
    swatch(body, 16, 76, "s1", "Server cost")
    swatch(body, 140, 76, "s2", "Lost sales")
    sx = lambda v: pw * v / xmax
    for i, (label, cost, lost) in enumerate(rows):
        y = top + i * rowh
        body.append(f'<text class="lab" x="{left}" y="{y + 14}">{label}</text>')
        by = y + 22
        if lost:
            body.append(f'<rect class="s1" x="{left}" y="{by}" width="{sx(cost) - 2:.1f}" height="20"><title>{label}: ${cost:,} server cost</title></rect>')
            body.append(f'<path class="s2" d="{right_rounded(left + sx(cost), by, sx(lost), 20)}"><title>{label}: about ${lost:,} lost sales</title></path>')
            end, txt = left + sx(cost + lost), f"${cost:,} + about ${lost:,} lost"
        else:
            body.append(f'<path class="s1" d="{right_rounded(left, by, sx(cost), 20)}"><title>{label}: ${cost:,} server cost</title></path>')
            end, txt = left + sx(cost), f"${cost:,}"
        body.append(f'<text class="lab" x="{end + 8:.1f}" y="{by + 15}">{txt}</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top + 18}" y2="{top + rowh * len(rows)}"/>')
    svg("02-02-annual-cost.svg", w, h,
        "Yearly server cost and lost sales for four ways the bakery could run its site",
        "Horizontal bar chart. Own 3 servers, today: $5,400 server cost plus about $8,000 lost December sales. "
        "Own 6 servers: $10,800. Cloud, renting 6 all year: $10,800. Cloud, renting what each month needs: $3,750.", body)


if __name__ == "__main__":
    demand_vs_owned()
    capacity_in_cloud()
    monthly_cost()
    annual_cost()
