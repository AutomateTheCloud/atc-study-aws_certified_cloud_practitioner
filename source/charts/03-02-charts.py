#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 03.02 (choosing a Region) as SVG.

Usage: python3 -I source/charts/03-02-charts.py
Writes images/03-02-*.svg. Facts trace to sources cited in
guide/03-aws-around-the-world/02-choosing-a-region.md:
- Region names, codes and countries: "AWS Regions", AWS Regions and Availability Zones
  User Guide, retrieved 2026-10-23;
- fiber delay: "What is latency?" (aws.amazon.com/what-is/latency/), retrieved 2026-10-23,
  which gives 4.9 microseconds per kilometer of fiber. The round trips below are our
  arithmetic (2 x distance x 4.9 us), a lower bound: real routes are longer and add delay;
- data transfer prices: the AWS Price List AWSDataTransfer offer file, publicationDate
  2026-09-16, first-10-TB tier of data transfer out to the internet, by Region.
The map is a schematic, not geography. Our own design: no AWS logos, icons, trade dress
or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --az-fill:#d9e8fb; --you-fill:#fbe1d6; --zone-fill:#f1f0ec;",
    dark_extra=" --az-fill:#1b3554; --you-fill:#4d2716; --zone-fill:#252523;",
    rules_extra="""
  .area { fill: var(--zone-fill); stroke: var(--axis); stroke-width: 1; }
  .eu { fill: none; stroke: var(--ink); stroke-width: 1.5; stroke-dasharray: 7 4; }
  .reg { fill: var(--az-fill); stroke: var(--s1); stroke-width: 1.5; }
  .regx { fill: var(--surface); stroke: var(--muted); stroke-width: 1.2; }
  .cust { fill: var(--you-fill); stroke: var(--s2); stroke-width: 1.5; }
  .flow { stroke: var(--ink); stroke-width: 2; fill: none; }
  .flowx { stroke: var(--muted); stroke-width: 2; fill: none; stroke-dasharray: 6 4; }
  .arrow { fill: var(--ink); }
  .arrowx { fill: var(--muted); }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .boxt { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .tiny { fill: var(--ink2); font-size: 11px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .other { fill: var(--muted); }""")


def box(body, cls, x, y, w, h, title, sub):
    body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    body.append(f'<text class="boxt" x="{x + w / 2}" y="{y + 17}" text-anchor="middle">{title}</text>')
    text_lines(body, x + w / 2, y + 32, sub, cls="tiny", dy=13, anchor="middle")


def arrow(body, x1, y1, x2, y2, cls="flow", head="arrow"):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 9 * math.cos(a), y2 - 9 * math.sin(a)
    body.append(f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{hx:.1f}" y2="{hy:.1f}"/>')
    p1 = (x2 - 10 * math.cos(a) + 5 * math.sin(a), y2 - 10 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 10 * math.cos(a) - 5 * math.sin(a), y2 - 10 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="{head}" d="M{x2},{y2} L{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z"/>')


def bakery_map():
    """Schematic: the bakery's two groups of customers and the Regions near them."""
    w, h = 680, 470
    body = [
        '<text class="title" x="16" y="28">The bakery\'s customers and the Regions near them</text>',
        '<text class="sub" x="16" y="48">A schematic, not a map: distances and positions are not to scale</text>',
    ]
    # United States area
    body.append('<rect class="area" x="16" y="70" width="250" height="300" rx="12"/>')
    body.append('<text class="head" x="30" y="94">United States</text>')
    box(body, "cust", 40, 112, 200, 46, "US customers", ["order for pickup at the US shop"])
    box(body, "reg", 40, 220, 200, 50, "US East (N. Virginia)", ["us-east-1: the site runs here today"])
    box(body, "reg", 40, 300, 200, 50, "US East (Ohio)", ["us-east-2: another US Region"])
    arrow(body, 140, 160, 140, 218)
    body.append('<text class="tiny" x="148" y="194">short trip</text>')
    # Europe area
    body.append('<rect class="area" x="300" y="70" width="364" height="300" rx="12"/>')
    body.append('<text class="head" x="314" y="94">Europe</text>')
    body.append('<rect class="eu" x="312" y="104" width="340" height="190" rx="10"/>')
    body.append('<text class="boxt" x="640" y="124" text-anchor="end">European Union (EU)</text>')
    box(body, "cust", 326, 134, 150, 46, "German customers", ["order at the German shop"])
    box(body, "reg", 326, 230, 150, 50, "Europe (Frankfurt)", ["eu-central-1, Germany"])
    box(body, "reg", 490, 166, 150, 50, "Europe (Ireland)", ["eu-west-1, Ireland"])
    box(body, "reg", 490, 230, 150, 50, "Europe (Paris)", ["eu-west-3, France"])
    arrow(body, 400, 182, 400, 228)
    body.append('<text class="tiny" x="408" y="210">short trip</text>')
    box(body, "regx", 326, 306, 150, 50, "Europe (London)", ["eu-west-2, UK: not EU"])
    box(body, "regx", 490, 306, 150, 50, "Europe (Zurich)", ["eu-central-2, Switzerland:", "not EU"])
    # the long way
    body.append('<path class="flowx" d="M326,158 C 290,158 290,245 251,245"/>')
    body.append('<path class="arrowx" d="M242,245 L252,240 L252,250 Z"/>')
    text_lines(body, 16, 396, [
        "Dashed arrow: if German orders went to N. Virginia, each request would cross an ocean (more delay),",
        "and German customers' data would leave the EU, which breaks the bakery's rule.",
    ], cls="small", dy=17)
    body.append('<text class="note" x="16" y="446">Blue: Regions that could hold that group\'s data. Gray: in Europe but not in the EU. Region list checked 2026-10-23.</text>')
    svg("03-02-bakery-map.svg", w, h,
        "Schematic of the bakery's customers and nearby AWS Regions",
        "A schematic, not to scale, in two areas. United States: US customers, who order for pickup at the US "
        "shop, with a solid arrow labeled short trip to US East (N. Virginia), us-east-1, where the site runs "
        "today; US East (Ohio), us-east-2, is shown as another US Region. Europe: a dashed boundary marks the "
        "European Union. Inside it, German customers have a solid arrow labeled short trip to Europe "
        "(Frankfurt), eu-central-1, in Germany; Europe (Ireland), eu-west-1, and Europe (Paris), eu-west-3, are "
        "also inside the EU boundary. Blue boxes are Regions that could hold that group of customers' data. Outside the EU boundary but in Europe: Europe (London), eu-west-2, in the "
        "UK, and Europe (Zurich), eu-central-2, in Switzerland, both marked not EU. A dashed arrow runs from the "
        "German customers to N. Virginia; the note says each request would cross an ocean, adding delay, and the "
        "German customers' data would leave the EU, which breaks the bakery's rule.", body, style=STYLE)


US_PER_KM = 4.9  # microseconds per km of fiber, AWS "What is latency?"
DISTANCES = [
    (100, "100 km", "the most two AZs in a Region are apart"),
    (1000, "1,000 km", ""),
    (3000, "3,000 km", ""),
    (6000, "6,000 km", ""),
    (10000, "10,000 km", ""),
]


def latency_by_distance():
    w = 680
    left, top, pw, rowh = 110, 82, 440, 40
    xmax = 100
    body = [
        '<text class="title" x="16" y="28">Distance alone puts a floor under delay</text>',
        '<text class="sub" x="16" y="48">Shortest possible round trip through fiber, in milliseconds (ms), for a straight cable of each length</text>',
    ]
    for i, (km, lab, note) in enumerate(DISTANCES):
        y = top + i * rowh
        ms = 2 * km * US_PER_KM / 1000
        body.append(f'<text class="lab" x="{left - 12}" y="{y + 18}" text-anchor="end">{lab}</text>')
        bw = max(pw * ms / xmax, 2)
        body.append(f'<path class="s1" d="{right_rounded(left, y + 4, bw, 22)}"><title>{lab}: at least {ms:.0f} ms there and back</title></path>')
        val = f"about {ms:.0f} ms" if ms >= 2 else f"about {ms:.0f} ms"
        body.append(f'<text class="lab" x="{left + bw + 8:.1f}" y="{y + 20}">{val}{": " + note if note else ""}</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top}" y2="{top + len(DISTANCES) * rowh - 12}"/>')
    y = top + len(DISTANCES) * rowh + 12
    y = text_lines(body, 16, y, [
        "AWS gives about 4.9 microseconds of delay per kilometer of fiber. A request and its answer travel both",
        "ways, so we doubled it. Real routes bend and pass through equipment, so real delays are higher.",
    ], cls="small", dy=17)
    h = y + 8
    svg("03-02-latency-by-distance.svg", w, h,
        "Shortest possible round-trip delay through fiber, by distance",
        "Horizontal bar chart of the shortest possible round trip through a straight fiber cable, from AWS's "
        "figure of 4.9 microseconds per kilometer, doubled for there and back. 100 km, the most two AZs in a "
        "Region are apart: about 1 ms. 1,000 km: about 10 ms. 3,000 km: about 29 ms. 6,000 km: about 59 ms. "
        "10,000 km: about 98 ms. Real routes are longer and pass through equipment, so real delays are higher.",
        body, style=STYLE)


# First 10 TB a month of data transfer out to the internet, USD per GB,
# AWS Price List AWSDataTransfer offer file published 2026-09-16.
PRICES = [
    ("US East (N. Virginia)", 0.09, True),
    ("Europe (Frankfurt)", 0.09, True),
    ("Europe (Ireland)", 0.09, False),
    ("Asia Pacific (Tokyo)", 0.114, False),
    ("Asia Pacific (Singapore)", 0.12, False),
    ("South America (São Paulo)", 0.15, False),
    ("Africa (Cape Town)", 0.154, False),
]


def transfer_price_by_region():
    w = 680
    left, top, pw, rowh = 196, 80, 340, 34
    xmax = 0.16
    body = [
        '<text class="title" x="16" y="28">The same data costs different amounts to send out of different Regions</text>',
        '<text class="sub" x="16" y="48">US dollars per GB sent to the internet, first 10 TB a month, from AWS\'s price list published 2026-09-16</text>',
    ]
    for i, (name, usd, mine) in enumerate(PRICES):
        y = top + i * rowh
        body.append(f'<text class="lab" x="{left - 12}" y="{y + 17}" text-anchor="end">{name}</text>')
        bw = pw * usd / xmax
        cls = "s1" if mine else "other"
        body.append(f'<path class="{cls}" d="{right_rounded(left, y + 4, bw, 20)}"><title>{name}: ${usd:.3f} per GB</title></path>')
        tag = "  (a bakery Region)" if mine else ""
        body.append(f'<text class="lab" x="{left + bw + 8:.1f}" y="{y + 18}">${usd:.3f}{tag}</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top}" y2="{top + len(PRICES) * rowh - 8}"/>')
    y = top + len(PRICES) * rowh + 12
    y = text_lines(body, 16, y, [
        "Blue bars: the two Regions the bakery uses; gray bars: others. Sending 100 GB costs about $9 from either of them,",
        "and about $15 from São Paulo. The first 100 GB a month across all Regions is free (as of 2026-10-23).",
    ], cls="small", dy=17)
    body.append(f'<text class="note" x="16" y="{y + 4}">Prices change. Check the AWS pricing pages or AWS Pricing Calculator for today\'s rates.</text>')
    h = y + 22
    svg("03-02-transfer-price-by-region.svg", w, h,
        "Price of sending data to the internet from seven Regions, published 2026-09-16",
        "Horizontal bar chart of US dollars per GB for the first 10 TB a month of data sent to the internet, from "
        "AWS's price list published 2026-09-16. US East (N. Virginia): $0.090, a bakery Region. Europe "
        "(Frankfurt): $0.090, a bakery Region. Europe (Ireland): $0.090. Asia Pacific (Tokyo): $0.114. Asia "
        "Pacific (Singapore): $0.120. South America (São Paulo): $0.150. Africa (Cape Town): $0.154. Sending "
        "100 GB costs about $9 from either bakery Region and about $15 from São Paulo; the first 100 GB a month "
        "across all Regions is free as of 2026-10-23.", body, style=STYLE)


if __name__ == "__main__":
    bakery_map()
    latency_by_distance()
    transfer_price_by_region()
