#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 03.01 (Regions, Availability Zones, data centers) as SVG.

Usage: python3 -I source/charts/03-01-charts.py
Writes images/03-01-*.svg. Facts trace to sources cited in
guide/03-aws-around-the-world/01-regions-availability-zones-data-centers.md:
- nesting, distances and links: "Regions and Availability Zones" (aws.amazon.com,
  retrieved 2026-10-23) and the AWS Fault Isolation Boundaries whitepaper (2022);
- where the bakery's parts live: REL10-BP01 and REL11-BP02 of the Well-Architected
  Reliability Pillar, and the Amazon RDS Multi-AZ page.
The number of data centers drawn inside each AZ is illustrative; AWS doesn't publish it.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# AWS infrastructure = slot 1 (blue) tint; the bakery's own resources = slot 2 (orange) tint,
# the same meaning those two colors carry in Module 04. Words, not color, name every box.
STYLE = make_style(
    light_extra=" --az-fill:#d9e8fb; --you-fill:#fbe1d6; --dc-fill:#f1f0ec;",
    dark_extra=" --az-fill:#1b3554; --you-fill:#4d2716; --dc-fill:#252523;",
    rules_extra="""
  .region { fill: none; stroke: var(--ink2); stroke-width: 1.5; }
  .region2 { fill: none; stroke: var(--ink2); stroke-width: 1.5; stroke-dasharray: 6 4; }
  .az { fill: var(--az-fill); stroke: var(--s1); stroke-width: 1.5; }
  .dc { fill: var(--dc-fill); stroke: var(--ink2); stroke-width: 1; }
  .you { fill: var(--you-fill); stroke: var(--s2); stroke-width: 1.5; }
  .gone { fill: none; stroke: var(--muted); stroke-width: 1.2; stroke-dasharray: 4 3; }
  .edge { fill: var(--dc-fill); stroke: var(--ink2); stroke-width: 1; }
  .link { stroke: var(--ink2); stroke-width: 2; fill: none; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .tiny { fill: var(--ink2); font-size: 11px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .minline { stroke: var(--ink); stroke-width: 1.5; stroke-dasharray: 5 4; }""")


def nesting():
    """Big picture: one Region holding three AZs, each holding one or more data centers."""
    w, h = 680, 500
    body = [
        '<text class="title" x="16" y="28">A Region holds Availability Zones; an AZ holds data centers</text>',
        '<text class="sub" x="16" y="48">How AWS\'s global infrastructure nests, drawn as boxes inside boxes (not to scale)</text>',
    ]
    rx, ry, rw, rh = 16, 66, 500, 336
    body.append(f'<rect class="region" x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="10"/>')
    body.append(f'<text class="head" x="{rx + 14}" y="{ry + 22}">Region: one area of the world, for example Europe (Frankfurt)</text>')
    body.append(f'<text class="small" x="{rx + 14}" y="{ry + 40}">At least three Availability Zones, isolated from other Regions</text>')
    dcs = [3, 1, 2]
    aw, ah, gap = 146, 200, 14
    ax0, ay = rx + 18, ry + 56
    centers = []
    for i, n in enumerate(dcs):
        ax = ax0 + i * (aw + gap)
        body.append(f'<rect class="az" x="{ax}" y="{ay}" width="{aw}" height="{ah}" rx="8"/>')
        body.append(f'<text class="boxt" x="{ax + aw / 2}" y="{ay + 20}" text-anchor="middle">Availability Zone</text>')
        text_lines(body, ax + aw / 2, ay + 36, ["own power, cooling", "and network"], cls="tiny", dy=13, anchor="middle")
        dh = 32
        for j in range(n):
            dy = ay + 58 + j * (dh + 6)
            body.append(f'<rect class="dc" x="{ax + 14}" y="{dy}" width="{aw - 28}" height="{dh}" rx="4"/>')
            body.append(f'<text class="small" x="{ax + aw / 2}" y="{dy + 20}" text-anchor="middle">Data center</text>')
        centers.append(ax + aw / 2)
        body.append(f'<text class="tiny" x="{ax + aw / 2}" y="{ay + ah - 12}" text-anchor="middle">{n} data center{"s" if n > 1 else ""} (illustrative)</text>')
    # links between AZs
    ly = ay + ah + 22
    for i in range(2):
        x1 = ax0 + i * (aw + gap) + aw / 2
        x2 = ax0 + (i + 1) * (aw + gap) + aw / 2
        body.append(f'<path class="link" d="M{x1},{ay + ah} L{x1},{ly} L{x2},{ly} L{x2},{ay + ah}"/>')
    body.append(f'<text class="small" x="{rx + rw / 2}" y="{ly + 18}" text-anchor="middle">Linked by fast, redundant private fiber; traffic between AZs is encrypted</text>')
    body.append(f'<text class="small" x="{rx + rw / 2}" y="{ly + 34}" text-anchor="middle">AZs are many kilometers apart, but all within 100 km (60 miles) of each other</text>')
    # another Region
    ox, ow = 532, 132
    body.append(f'<rect class="region2" x="{ox}" y="{ry}" width="{ow}" height="150" rx="10"/>')
    text_lines(body, ox + ow / 2, ry + 26, ["Another Region"], cls="boxt", anchor="middle")
    text_lines(body, ox + ow / 2, ry + 48, wrap("Much farther away than AZs are from each other. Nothing is copied here unless you copy it.", 20),
               cls="tiny", dy=14, anchor="middle")
    # edge locations
    ey = ry + rh + 22
    body.append(f'<text class="head" x="{rx}" y="{ey + 6}">Outside the Regions</text>')
    for k in range(4):
        ex = rx + 170 + k * 122
        body.append(f'<rect class="edge" x="{ex}" y="{ey - 12}" width="110" height="26" rx="13"/>')
        body.append(f'<text class="tiny" x="{ex + 55}" y="{ey + 5}" text-anchor="middle">Edge location</text>')
    body.append(f'<text class="note" x="{rx}" y="{ey + 36}">Edge locations are smaller sites in many more cities, outside the Regions. Lesson 03.04 covers them.</text>')
    svg("03-01-nesting.svg", w, h,
        "How Regions, Availability Zones and data centers nest",
        "A large box labeled Region, one area of the world such as Europe (Frankfurt), with at least three "
        "Availability Zones, isolated from other Regions. Inside it, three Availability Zone boxes, each with its "
        "own power, cooling and network. The first holds three data centers, the second one, the third two; the "
        "counts are illustrative. Lines join the AZs: fast, redundant private fiber, with traffic between AZs "
        "encrypted; AZs are many kilometers apart but all within 100 km (60 miles) of each other. To the right, a "
        "dashed box labeled Another Region: much farther away than AZs are from each other, and nothing is copied there "
        "unless you copy it. Below, outside the Regions, four small boxes labeled Edge location, covered in "
        "lesson 03.04.", body, style=STYLE)


def bakery_layout():
    """Before and after: the bakery's parts in one AZ, then spread over two."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Where the bakery\'s parts live, before and after</text>',
        '<text class="sub" x="16" y="48">Orange boxes are the bakery\'s resources; blue columns are Availability Zones in US East (N. Virginia)</text>',
    ]
    cols = 3
    left, cw, gap = 130, 168, 12

    def panel(y0, title, rows, note):
        body.append(f'<text class="head" x="16" y="{y0}">{title}</text>')
        top = y0 + 14
        n = len(rows)
        rh, rg = 34, 8
        ph = 26 + n * (rh + rg) + 4
        for c in range(cols):
            x = left + c * (cw + gap)
            body.append(f'<rect class="az" x="{x}" y="{top}" width="{cw}" height="{ph}" rx="6"/>')
            body.append(f'<text class="boxt" x="{x + cw / 2}" y="{top + 18}" text-anchor="middle">AZ {"abc"[c]}</text>')
        for r, (label, cells) in enumerate(rows):
            y = top + 26 + r * (rh + rg)
            text_lines(body, left - 10, y + 14, wrap(label, 15), cls="small", dy=13, anchor="end")
            for kind, c0, c1, text in cells:
                x = left + c0 * (cw + gap) + 6
                ww = (c1 - c0 + 1) * cw + (c1 - c0) * gap - 12
                cls = "you" if kind == "you" else "gone"
                body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{ww}" height="{rh}" rx="5"/>')
                body.append(f'<text class="tiny" x="{x + ww / 2}" y="{y + 21}" text-anchor="middle">{text}</text>')
        yn = top + ph + 18
        yn = text_lines(body, 16, yn, wrap(note, 100), cls="small", dy=16)
        return yn + 18

    before = [
        ("Web server (EC2)", [("you", 0, 0, "the only web server")]),
        ("Order database (RDS)", [("you", 0, 0, "the database, no standby")]),
        ("Order functions (Lambda)", [("you", 0, 2, "AWS runs them across AZs for you")]),
        ("Cake photos (S3)", [("you", 0, 2, "stored across at least three AZs")]),
    ]
    after = [
        ("Load balancer", [("you", 0, 1, "spreads orders across healthy servers")]),
        ("Web servers (EC2)", [("you", 0, 0, "web server 1"), ("you", 1, 1, "web server 2")]),
        ("Order database (RDS)", [("you", 0, 0, "primary"), ("you", 1, 1, "standby, takes over")]),
        ("Order functions (Lambda)", [("you", 0, 2, "AWS runs them across AZs for you")]),
        ("Cake photos (S3)", [("you", 0, 2, "stored across at least three AZs")]),
    ]
    y = 80
    y = panel(y, "Before: the server and database sit in one AZ",
              before, "If AZ a fails, the site stops: the web server and the database are both there. "
              "The photos and functions would survive, but nobody could place an order.")
    y = panel(y + 6, "After: a copy of each zonal part in a second AZ",
              after, "If AZ a fails, web server 2 keeps taking orders and the standby database takes over. "
              "Lambda and S3 needed no change.")
    h = y
    svg("03-01-bakery-layout.svg", w, h,
        "The bakery's resources across Availability Zones, before and after adding a second AZ",
        "Two panels, each with three Availability Zone columns, a, b and c, in US East (N. Virginia). Before: the "
        "only web server (EC2) and the order database (RDS, no standby) are both in AZ a; the order functions "
        "(Lambda) and the cake photos (S3) span all three AZs, because AWS runs them across AZs. If AZ a fails, "
        "the site stops, because the web server and database are both there. After: a load balancer spans AZs a "
        "and b and spreads orders across healthy servers; web server 1 is in AZ a and web server 2 in AZ b; the "
        "database has its primary in AZ a and a standby in AZ b that takes over; Lambda and S3 are unchanged. If "
        "AZ a fails, web server 2 keeps taking orders and the standby database takes over.", body, style=STYLE)


if __name__ == "__main__":
    nesting()
    bakery_layout()
