#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 03.03 (surviving failure) as SVG.

Usage: python3 -I source/charts/03-03-charts.py
Writes images/03-03-*.svg. Facts come from AWS's whitepaper "Disaster Recovery of
Workloads on AWS: Recovery in the Cloud" (2021): high availability vs disaster
recovery, the definitions of RTO and RPO, the four strategies and their order from
lowest to highest cost and complexity, and their typical recovery ranges (hours,
tens of minutes, minutes, real time; research repo docs/13, A9). The bakery's times
are made up for teaching. No prices or invented numbers on the strategy chart.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# High availability = categorical slot 1 (blue) tint; disaster recovery = slot 2
# (orange) tint. Every box also says in words which one it is, so color is never alone.
STYLE = make_style(
    light_extra=" --ha-fill:#d9e8fb; --dr-fill:#fbe1d6; --bk-fill:#f1f0ec;",
    dark_extra=" --ha-fill:#1b3554; --dr-fill:#4d2716; --bk-fill:#252523;",
    rules_extra="""
  .ha { fill: var(--ha-fill); stroke: var(--s1); stroke-width: 1.5; }
  .dr { fill: var(--dr-fill); stroke: var(--s2); stroke-width: 1.5; }
  .bk { fill: var(--bk-fill); stroke: var(--ink2); stroke-width: 1.5; stroke-dasharray: 5 4; }
  .step { fill: var(--ha-fill); stroke: var(--s1); stroke-width: 1.5; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .head { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .tag { fill: var(--ink); font-size: 11.5px; font-weight: 600; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }
  .span-rpo { stroke: var(--s2); stroke-width: 3; fill: none; stroke-linecap: round; }
  .span-rto { stroke: var(--s1); stroke-width: 3; fill: none; stroke-linecap: round; }
  .ev { fill: var(--ink); stroke: var(--surface); stroke-width: 2; }
  .evline { stroke: var(--ink2); stroke-width: 1; stroke-dasharray: 3 3; }""")


def arrow(body, x1, y1, x2, y2):
    """A straight line with a small filled head at (x2, y2)."""
    body.append(f'<line class="arrow" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    if x1 == x2:
        d = 1 if y2 > y1 else -1
        body.append(f'<path class="arrowhead" d="M{x2 - 5},{y2 - 8 * d} L{x2 + 5},{y2 - 8 * d} L{x2},{y2} Z"/>')
    else:
        d = 1 if x2 > x1 else -1
        body.append(f'<path class="arrowhead" d="M{x2 - 8 * d},{y2 - 5} L{x2 - 8 * d},{y2 + 5} L{x2},{y2} Z"/>')


RUNGS = [  # (what fails, example, what keeps the site running, kind)
    ("A whole Region", "A disaster or a large outage makes the Region unusable",
     "A copy of the site, or at least of its data, in another Region", "dr"),
    ("One Availability Zone", "A flood or a fire takes out every data center in the AZ",
     "Servers and the database running in two or more AZs", "ha"),
    ("One data center", "A power or cooling failure in one building",
     "The same answer: more than one AZ (an AZ may be just one data center)", "ha"),
    ("One server", "A disk fails or the server crashes",
     "A second server, and automatic replacement of the failed one", "ha"),
]


def ladder():
    """Big picture: the blast-radius ladder, with high availability and DR marked."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">How far a failure reaches, and what keeps the site running</text>',
        '<text class="sub" x="16" y="48">Each rung is a bigger failure. Protection on a lower rung doesn\'t cover the rungs above it.</text>',
    ]
    x0, y = 16, 74
    body.append(f'<text class="head" x="{x0 + 12}" y="{y}">What fails</text>')
    body.append(f'<text class="head" x="{x0 + 206}" y="{y}">What keeps the bakery\'s site running</text>')
    y += 12
    full = w - 32
    for i, (what, example, keep, kind) in enumerate(RUNGS):
        # The rung's box narrows as the failure gets smaller: width shows reach, not a number.
        bw = full - i * 40
        bx = x0 + (full - bw) / 2
        left_lines = wrap(example, 27)
        right_lines = wrap(keep, 40)
        h = max(24 + 15 * len(left_lines), 24 + 15 * len(right_lines)) + 22
        body.append(f'<rect class="{kind}" x="{bx:.1f}" y="{y}" width="{bw:.1f}" height="{h}" rx="6"/>')
        tx, rx = bx + 12, bx + 206
        body.append(f'<text class="cellt" x="{tx:.1f}" y="{y + 19}">{what}</text>')
        text_lines(body, tx, y + 36, left_lines, cls="cells", dy=15)
        text_lines(body, rx, y + 19, right_lines, cls="small", dy=15)
        label = "Disaster recovery" if kind == "dr" else "High availability"
        body.append(f'<text class="tag" x="{rx:.1f}" y="{y + h - 10}">{label}</text>')
        y += h + 8
    # The data rung: not on the ladder, because it reaches every live copy.
    y += 8
    note = ("A mistake or an attack on the data itself, such as a deleted orders table, "
            "isn't on the ladder: it reaches every live copy at once.")
    keep = "A point-in-time backup from before the mistake. Only a backup undoes it."
    lines = wrap(note, 52)
    klines = wrap(keep, 34)
    h = 24 + 15 * max(len(lines), len(klines)) + 8
    body.append(f'<rect class="bk" x="{x0}" y="{y}" width="{full}" height="{h}" rx="6"/>')
    body.append(f'<text class="cellt" x="{x0 + 12}" y="{y + 19}">Off the ladder: the data</text>')
    text_lines(body, x0 + 12, y + 36, lines, cls="cells", dy=15)
    text_lines(body, x0 + 400, y + 19, klines, cls="small", dy=15)
    y += h + 22
    body.append(f'<text class="note" x="16" y="{y}">Our summary of AWS\'s disaster recovery whitepaper (2021) and Regions and AZs pages, checked 2026-10-24.</text>')
    svg("03-03-blast-radius-ladder.svg", w, y + 14,
        "The blast-radius ladder: how far a failure reaches, and what protects against it",
        "Four rungs, from the largest failure at the top to the smallest at the bottom; each box is wider "
        "the further the failure reaches. A whole Region: a disaster or a large outage makes the Region "
        "unusable; protection is a copy of the site, or at least of its data, in another Region; this is "
        "disaster recovery. One Availability Zone: a flood or fire takes out every data center in the AZ; "
        "protection is servers and the database running in two or more AZs; high availability. One data "
        "center: a power or cooling failure in one building; the same protection, more than one AZ, because "
        "an AZ may be just one data center; high availability. One server: a disk fails or the server "
        "crashes; protection is a second server and automatic replacement; high availability. A separate "
        "dashed box, off the ladder: a mistake or an attack on the data itself, such as a deleted orders "
        "table, reaches every live copy at once; only a point-in-time backup from before the mistake "
        "undoes it.", body, style=STYLE)


def timeline():
    """RTO and RPO on one time line, with the bakery's made-up times."""
    w = 680
    left, right = 60, w - 40
    t0, t1 = 0, 16  # hours shown: 00:00 to 16:00

    def x(h):
        return left + (right - left) * (h - t0) / (t1 - t0)

    body = [
        '<text class="title" x="16" y="28">RPO looks back from the failure; RTO looks forward</text>',
        '<text class="sub" x="16" y="48">The bakery\'s order database, one bad day. Times are made up for teaching.</text>',
    ]
    axis_y = 230
    body.append(f'<line class="axis" x1="{left}" x2="{right}" y1="{axis_y}" y2="{axis_y}"/>')
    for hh in range(t0, t1 + 1, 2):
        body.append(f'<line class="axis" x1="{x(hh):.1f}" x2="{x(hh):.1f}" y1="{axis_y}" y2="{axis_y + 5}"/>')
        body.append(f'<text class="tick" x="{x(hh):.1f}" y="{axis_y + 20}" text-anchor="middle">{hh:02d}:00</text>')
    events = [
        (2, ["Last good", "backup"], "the recovery point"),
        (10, ["The database", "is lost"], "orders stop"),
        (14, ["Site taking", "orders again"], "service restored"),
    ]
    for hh, lab, sub in events:
        body.append(f'<line class="evline" x1="{x(hh):.1f}" x2="{x(hh):.1f}" y1="100" y2="{axis_y}"/>')
        body.append(f'<circle class="ev" cx="{x(hh):.1f}" cy="{axis_y}" r="6"/>')
        text_lines(body, x(hh), 72, lab, cls="cellt", dy=16, anchor="middle")
        body.append(f'<text class="small" x="{x(hh):.1f}" y="{axis_y + 38}" text-anchor="middle">{sub}</text>')
    y_rpo, y_rto = 140, 190
    body.append(f'<line class="span-rpo" x1="{x(2):.1f}" x2="{x(10):.1f}" y1="{y_rpo}" y2="{y_rpo}"/>')
    body.append(f'<text class="cellt" x="{(x(2) + x(10)) / 2:.1f}" y="{y_rpo - 10}" text-anchor="middle">Data lost: 8 hours of orders</text>')
    body.append(f'<line class="span-rto" x1="{x(10):.1f}" x2="{x(14):.1f}" y1="{y_rto}" y2="{y_rto}"/>')
    body.append(f'<text class="cellt" x="{(x(10) + x(14)) / 2:.1f}" y="{y_rto - 10}" text-anchor="middle">Downtime: 4 hours</text>')
    yb = axis_y + 66
    body.append(f'<text class="lab" x="16" y="{yb}">RPO: the most data loss the business accepts, measured back from the failure.</text>')
    body.append(f'<text class="lab" x="16" y="{yb + 18}">RTO: the most downtime the business accepts, measured forward from the failure.</text>')
    body.append(f'<text class="note" x="16" y="{yb + 40}">Recovery point objective (RPO) and recovery time objective (RTO), as AWS defines them.</text>')
    svg("03-03-rto-rpo-timeline.svg", w, axis_y + 120,
        "RPO and RTO on a time line of one failure",
        "A time line from 00:00 to 16:00 with three events, made up for teaching. At 02:00, the last good "
        "backup: the recovery point. At 10:00, the bakery's order database is lost and orders stop. At 14:00, "
        "the site is taking orders again: service restored. A span from 02:00 to 10:00 is labeled 'Data lost: "
        "8 hours of orders'. A span from 10:00 to 14:00 is labeled 'Downtime: 4 hours'. Below: RPO is the "
        "most data loss the business accepts, measured back from the failure; RTO is the most downtime the "
        "business accepts, measured forward from the failure.", body, style=STYLE)


STRATEGIES = [  # (name, recovery time label, what runs in the recovery Region)
    ("Backup and restore", "Hours",
     "Backups of data and setup copied there. Everything else is rebuilt after the disaster."),
    ("Pilot light", "Tens of minutes",
     "Data copied continuously; the database runs. App servers are off until needed."),
    ("Warm standby", "Minutes",
     "A smaller copy of the whole site, always running. Scale it up to take over."),
    ("Multi-site active/active", "Real time (near zero)",
     "Full copies in two or more Regions, all serving customers at once."),
]


def strategies():
    """The four DR strategies as a staircase: cost and complexity up, recovery time down."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">The four disaster recovery strategies</text>',
        '<text class="sub" x="16" y="48">Each step costs more to run and is more complex, and recovers faster with less data lost</text>',
    ]
    left, top = 70, 70
    bw, bh, gapx = 140, 150, 6
    rise = 46
    base = top + 3 * rise + bh  # bottom of the lowest box
    for i, (name, rt, what) in enumerate(STRATEGIES):
        bx = left + i * (bw + gapx)
        by = top + (3 - i) * rise
        body.append(f'<rect class="step" x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="6"/>')
        nlines = wrap(name, 18)
        yy = text_lines(body, bx + 10, by + 20, nlines, cls="cellt", dy=16)
        text_lines(body, bx + 10, yy + 4, wrap(what, 21), cls="cells", dy=15)
        body.append(f'<text class="tick" x="{bx + bw / 2}" y="{base + 20}" text-anchor="middle">{rt}</text>')
    right = left + 4 * bw + 3 * gapx
    # x axis: recovery time falls to the right.
    body.append(f'<line class="axis" x1="{left}" x2="{right}" y1="{base + 4}" y2="{base + 4}"/>')
    arrow(body, left, base + 44, right, base + 44)
    body.append(f'<text class="small" x="{left}" y="{base + 62}">Typical recovery time: slower</text>')
    body.append(f'<text class="small" x="{right}" y="{base + 62}" text-anchor="end">faster, and less data lost</text>')
    # y axis: running cost and complexity rise upward. No scale: AWS gives an order, not prices.
    arrow(body, left - 24, base, left - 24, top + 4)
    body.append(f'<text class="small" transform="translate({left - 32},{(base + top) / 2:.0f}) rotate(-90)" '
                f'text-anchor="middle">Running cost and complexity: higher</text>')
    y = base + 88
    body.append(f'<text class="note" x="16" y="{y}">Order and typical ranges from AWS\'s disaster recovery whitepaper (2021), checked 2026-10-24.</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">No prices: the steps show order only. Real times depend on how well the plan is built and tested.</text>')
    svg("03-03-dr-strategies.svg", w, y + 30,
        "The four disaster recovery strategies as a staircase of cost against recovery time",
        "Four boxes rise like stairs from left to right. Moving right, running cost and complexity rise, and "
        "typical recovery time falls. Backup and restore, recovery in hours: backups of data and setup are "
        "copied to the recovery Region, and everything else is rebuilt after the disaster. Pilot light, tens "
        "of minutes: data is copied continuously and the database runs; app servers are off until needed. "
        "Warm standby, minutes: a smaller copy of the whole site is always running and is scaled up to take "
        "over. Multi-site active/active, real time or near zero: full copies in two or more Regions all serve "
        "customers at once. The axes have no scale: AWS gives the order, not prices.", body, style=STYLE)


if __name__ == "__main__":
    ladder()
    timeline()
    strategies()
