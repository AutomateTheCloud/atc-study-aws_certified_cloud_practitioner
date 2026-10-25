#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for lesson 02.04 (what a data center really costs) as SVG.

Usage: python3 -I source/charts/02-04-charts.py
Writes images/02-04-*.svg. All numbers are the made-up teaching figures from the
worked example in guide/02-why-the-cloud/04-what-a-data-center-really-costs.md;
change them here and rerun when the lesson changes.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, swatch, text_lines, top_rounded, wrap  # noqa: E402

MONTHS_TOTAL = 36
NEEDED = [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 3, 6]  # servers needed each month, from lesson 02.02
HARDWARE = 6 * 2000  # paid up front in month 1
ONPREM_MONTHLY = {"Space": 100, "Power and cooling": 80, "Network": 60, "Staff": 200}
LICENSES_A_YEAR = 500
RENT = 250  # a server-month in the cloud, licenses included
CLOUD_STAFF = 100  # a month
PEAK = 6

# Fixed costs are drawn in neutral tones (matching the "owning" line), the variable
# usage bill in series blue, and the cloud left at peak size in series orange.
STYLE = make_style(
    light_extra=" --fixed:#898781; --upfront:#52514e;",
    dark_extra=" --fixed:#898781; --upfront:#c3c2b7;",
    rules_extra="""
  .line-s2 { stroke: var(--s2); stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .fixed { fill: var(--fixed); } .upfront { fill: var(--upfront); }
  .cell { fill: none; stroke: var(--axis); stroke-width: 1; }
  .chip { fill: var(--surface); stroke: var(--muted); stroke-width: 1; }
  .chip-s1 { fill: var(--surface); stroke: var(--s1); stroke-width: 2; }
  .arrow { stroke: var(--s1); stroke-width: 2; fill: none; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .ring { stroke: var(--surface); stroke-width: 2; }""",
)


def money(v):
    return f"${v:,.0f}"


def totals_by_category():
    years = MONTHS_TOTAL // 12
    onprem = [("upfront", "Hardware", HARDWARE)]
    onprem += [("fixed", k, v * MONTHS_TOTAL) for k, v in ONPREM_MONTHLY.items() if k != "Staff"]
    onprem += [("fixed", "Staff", ONPREM_MONTHLY["Staff"] * MONTHS_TOTAL), ("fixed", "Licenses", LICENSES_A_YEAR * years)]
    matched = [("s1", "Usage bill", sum(NEEDED) * years * RENT), ("fixed", "Staff", CLOUD_STAFF * MONTHS_TOTAL)]
    peak = [("s1", "Usage bill", PEAK * MONTHS_TOTAL * RENT), ("fixed", "Staff", CLOUD_STAFF * MONTHS_TOTAL)]
    cols = [("Own 6 servers", onprem), ("Cloud, matched to demand", matched), ("Cloud, left at peak size", peak)]
    assert [sum(s[2] for s in c[1]) for c in cols] == [29340, 22350, 57600], "totals must match the lesson"
    w, h, top, ph, ymax, bw = 680, 470, 128, 270, 60000, 52
    xs = [40, 270, 500]
    body = [
        '<text class="title" x="16" y="28">Where the three-year money goes</text>',
        '<text class="sub" x="16" y="48">Three-year totals by cost category, made-up figures from the worked example</text>',
    ]
    swatch(body, 16, 76, "upfront", "Fixed, paid up front")
    swatch(body, 176, 76, "fixed", "Fixed, paid every month or year")
    swatch(body, 430, 76, "s1", "Variable: follows use")
    base = top + ph
    body.append(f'<line class="axis" x1="16" x2="{w - 16}" y1="{base}" y2="{base}"/>')
    unit = ph / ymax
    for (name, segs), x in zip(cols, xs):
        y0, mids = base, []
        for j, (cls, label, v) in enumerate(segs):
            hh = v * unit
            y = y0 - hh
            drawn = hh - (2 if j > 0 else 0)
            tip = f"{name}: {label} {money(v)}"
            if j == len(segs) - 1:
                body.append(f'<path class="{cls}" d="{top_rounded(x, y, bw, drawn)}"><title>{tip}</title></path>')
            else:
                body.append(f'<rect class="{cls}" x="{x}" y="{y:.1f}" width="{bw}" height="{drawn:.1f}"><title>{tip}</title></rect>')
            mids.append((y + drawn / 2, f"{label} {money(v)}"))
            y0 = y
        total = sum(s[2] for s in segs)
        body.append(f'<text class="lab" x="{x + bw / 2:.1f}" y="{y0 - 10:.1f}" text-anchor="middle" style="font-weight:600">{money(total)}</text>')
        # segment labels to the right, spread to at least 15px apart, with leaders
        placed, last = [], base + 20
        for ym, txt in mids:
            yl = min(ym + 4, last - 15)
            placed.append((ym, yl, txt))
            last = yl
        for ym, yl, txt in placed:
            body.append(f'<line class="lead" x1="{x + bw + 2}" y1="{ym:.1f}" x2="{x + bw + 10}" y2="{yl - 4:.1f}"/>')
            body.append(f'<text class="small" x="{x + bw + 14}" y="{yl:.1f}">{txt}</text>')
        text_lines(body, x + bw / 2, base + 22, wrap(name, 16), cls="lab", anchor="middle")
    svg("02-04-totals-by-category.svg", w, h,
        "Three-year cost by category for owning 6 servers, the cloud matched to demand, and the cloud left at peak size",
        "Stacked column chart, made-up figures. Own 6 servers, $29,340 in all: hardware $12,000 paid up front; "
        "space $3,600, power and cooling $2,880, network $2,160, staff $7,200 and licenses $1,500, all fixed. "
        "Cloud matched to demand, $22,350: usage bill $18,750, variable; staff $3,600, fixed. "
        "Cloud left at peak size, $57,600: usage bill $54,000, variable; staff $3,600, fixed.", body, style=STYLE)


def capex_opex_grid():
    w, h = 680, 400
    gx, gy, cw, ch = 152, 104, 256, 128  # grid origin, cell width and height
    body = [
        '<text class="title" x="16" y="28">Two questions about the same money</text>',
        '<text class="sub" x="16" y="48">Capital or operating: when and how you pay. Fixed or variable: does use change it?</text>',
    ]
    for i, head in enumerate(("Fixed", "Variable")):
        body.append(f'<text class="head" x="{gx + cw * i + cw / 2:.1f}" y="{gy - 12}" text-anchor="middle">{head}</text>')
    body.append(f'<text class="small" x="{gx + cw:.1f}" y="{gy - 32}" text-anchor="middle">Does the cost change with use?</text>')
    for i, (head, sub) in enumerate((("Capital", "big payment up front"), ("Operating", "paid as you go"))):
        yc = gy + ch * i + ch / 2
        body.append(f'<text class="head" x="{gx - 12}" y="{yc - 2:.1f}" text-anchor="end">{head}</text>')
        body.append(f'<text class="small" x="{gx - 12}" y="{yc + 15:.1f}" text-anchor="end">{sub}</text>')
        for j in range(2):
            body.append(f'<rect class="cell" x="{gx + cw * j}" y="{gy + ch * i}" width="{cw}" height="{ch}"/>')

    def chip(x, y, lines, cls="chip"):
        wd = max(len(s) for s in lines) * 6.9 + 20
        hh = 17 * len(lines) + 12
        body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{wd:.1f}" height="{hh}" rx="6"/>')
        text_lines(body, x + 10, y + 20, lines, cls="lab")
        return wd, hh

    # Capital + fixed
    cw1, ch1 = chip(gx + 16, gy + 20, ["Buying four servers"])
    # Capital + variable: empty on purpose
    text_lines(body, gx + cw + 16, gy + 38, ["No example in this lesson"], cls="small")
    # Operating + fixed
    chip(gx + 16, gy + ch + 14, ["Renting space for them"])
    chip(gx + 16, gy + ch + 60, ["Electricity for servers that", "are always on (mostly fixed)"])
    # Operating + variable
    xv, yv = gx + cw + 16, gy + ch + 60
    chip(xv, yv, ["A cloud bill that follows", "how much you use"], cls="chip-s1")
    # the move to pay-as-you-go: from buying servers to the cloud bill
    ax0, ay0 = gx + 16 + cw1 + 4, gy + 20 + ch1 / 2
    ax1, ay1 = xv + 60, yv - 6
    body.append(f'<path class="arrow" d="M{ax0:.1f},{ay0:.1f} C{ax0 + 120:.1f},{ay0:.1f} {ax1:.1f},{ay1 - 90:.1f} {ax1:.1f},{ay1:.1f}"/>')
    body.append(f'<path d="M{ax1 - 6:.1f},{ay1 - 10:.1f} L{ax1:.1f},{ay1:.1f} L{ax1 + 6:.1f},{ay1 - 10:.1f}" class="arrow"/>')
    body.append(f'<text class="lab" x="{ax1 + 12:.1f}" y="{gy + ch - 28}">Moving to pay as you go</text>')
    body.append(f'<text class="small" x="{ax1 + 12:.1f}" y="{gy + ch - 12}">changes both answers</text>')
    body.append(f'<text class="sub" x="16" y="{h - 14}">Rent and always-on electricity are operating expenses, yet fixed: the two pairs are not the same split.</text>')
    svg("02-04-capex-opex-grid.svg", w, h,
        "Capital or operating, fixed or variable: four examples placed in a two-by-two grid",
        "A grid with two columns, fixed and variable, and two rows, capital and operating. Capital and fixed: buying "
        "four servers. Capital and variable: no example in this lesson. Operating and fixed: renting space for the "
        "servers, and electricity for servers that are always on, which is mostly fixed. Operating and variable: a "
        "cloud bill that follows how much you use. An arrow labeled moving to pay as you go runs from buying servers "
        "to the cloud bill.", body, style=STYLE)


if __name__ == "__main__":
    totals_by_category()
    capex_opex_grid()
