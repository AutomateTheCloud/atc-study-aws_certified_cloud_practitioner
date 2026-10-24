#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 03.04 (the edge) as SVG.

Usage: python3 -I source/charts/03-04-charts.py
Writes images/03-04-*.svg. Facts come from AWS's Global Infrastructure and Regions
and AZs pages, the CloudFront key features page, the AWS Fault Isolation Boundaries
whitepaper (which services run at points of presence, and which features such as
AWS WAF for CloudFront run there too), and the What is AWS Local Zones, What is AWS
Wavelength and What is AWS Outposts pages, read 2026-10-23 and 2026-10-24.
The world view is a schematic: no map, and the number and position of shapes are
illustrative, not counts. Our own design: no AWS logos, icons, trade dress or AWS
diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Regions = categorical slot 1 (blue) tint boxes; edge locations = slot 2 (orange)
# dots. Shape (box vs dot) and the legend carry identity as well as color.
STYLE = make_style(
    light_extra=" --reg-fill:#d9e8fb; --card-fill:#f6f5f2;",
    dark_extra=" --reg-fill:#1b3554; --card-fill:#222221;",
    rules_extra="""
  .panel { fill: none; stroke: var(--axis); stroke-width: 1; }
  .region { fill: var(--reg-fill); stroke: var(--s1); stroke-width: 1.5; }
  .az { fill: var(--surface); stroke: var(--s1); stroke-width: 1; }
  .edge { fill: var(--s2); stroke: var(--surface); stroke-width: 2; }
  .user { fill: var(--ink); stroke: var(--surface); stroke-width: 2; }
  .hop { stroke: var(--ink); stroke-width: 2; fill: none; }
  .backbone { stroke: var(--ink2); stroke-width: 1.5; fill: none; stroke-dasharray: 6 4; }
  .card { fill: var(--card-fill); stroke: var(--axis); stroke-width: 1; }
  .cardhi { fill: var(--card-fill); stroke: var(--ink2); stroke-width: 1.5; stroke-dasharray: 5 4; }
  .name { fill: var(--ink); font-size: 15px; font-weight: 600; }
  .key { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .panelt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")


def region(body, x, y):
    """A Region box holding three small Availability Zone squares."""
    body.append(f'<rect class="region" x="{x}" y="{y}" width="74" height="40" rx="5"/>')
    body.append(f'<text class="small" x="{x + 37}" y="{y + 14}" text-anchor="middle">Region</text>')
    for i in range(3):
        body.append(f'<rect class="az" x="{x + 8 + i * 21}" y="{y + 20}" width="16" height="13" rx="2"/>')


def edge(body, x, y):
    body.append(f'<circle class="edge" cx="{x}" cy="{y}" r="5.5"/>')


# Illustrative layout per panel: Region positions and edge-location positions (relative).
PANELS = [
    ("North America", [(22, 58), (112, 150)], [(20, 128), (66, 116), (150, 64), (168, 112), (34, 204),
                                               (96, 226), (158, 214), (120, 40)]),
    ("Europe", [(98, 56), (20, 154)], [(30, 54), (70, 126), (126, 120), (162, 160), (128, 214),
                                       (66, 232), (184, 112), (110, 168)]),
    ("Asia Pacific", [(20, 70), (104, 168)], [(40, 136), (128, 54), (170, 112), (84, 120), (30, 220),
                                              (160, 230), (100, 40), (140, 150)]),
]


def regions_and_edge():
    """Schematic: a few Regions with AZs, many edge locations, one customer's path."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Regions are few and large; edge locations are many and small</text>',
        '<text class="sub" x="16" y="48">A schematic, not a map: the number and position of shapes are illustrative</text>',
    ]
    pw, ph, top, gap = 206, 262, 66, 15
    for i, (name, regs, edges) in enumerate(PANELS):
        px = 16 + i * (pw + gap)
        body.append(f'<rect class="panel" x="{px}" y="{top}" width="{pw}" height="{ph}" rx="8"/>')
        body.append(f'<text class="panelt" x="{px + 12}" y="{top + 20}">{name}</text>')
        for rx, ry in regs:
            region(body, px + rx, top + ry)
        for ex, ey in edges:
            edge(body, px + ex, top + ey)
        if name == "Europe":
            ux, uy = px + 168, top + 236
            ex, ey = px + 128, top + 214      # nearest edge location
            rx, ry = px + 20 + 37, top + 154 + 40  # bottom of a Region box
            body.append(f'<path class="backbone" d="M{ex},{ey} L{rx},{ry}"/>')
            body.append(f'<line class="hop" x1="{ux}" y1="{uy}" x2="{ex + 5}" y2="{ey + 3}"/>')
            body.append(f'<circle class="user" cx="{ux}" cy="{uy}" r="6"/>')
            body.append(f'<text class="small" x="{ux + 9}" y="{uy + 20}" text-anchor="end">A customer</text>')
    # Global network between panels.
    yb = top + ph + 6
    body.append(f'<path class="backbone" d="M{16 + pw / 2},{yb} L{16 + pw / 2},{yb + 14} L{16 + 2 * (pw + gap) + pw / 2},{yb + 14} '
                f'L{16 + 2 * (pw + gap) + pw / 2},{yb}"/>')
    body.append(f'<line class="backbone" x1="{16 + pw + gap + pw / 2}" x2="{16 + pw + gap + pw / 2}" y1="{yb}" y2="{yb + 14}"/>')
    body.append(f'<text class="small" x="{w / 2}" y="{yb + 32}" text-anchor="middle">AWS\'s own global network links Regions and edge locations</text>')
    # Legend.
    ly = yb + 62
    body.append(f'<rect class="region" x="16" y="{ly - 14}" width="22" height="16" rx="3"/>')
    body.append(f'<text class="lab" x="44" y="{ly}">Region, with its Availability Zones inside</text>')
    edge(body, 330, ly - 5)
    body.append(f'<text class="lab" x="342" y="{ly}">Edge location</text>')
    body.append(f'<line class="hop" x1="450" x2="472" y1="{ly - 5}" y2="{ly - 5}"/>')
    body.append(f'<text class="lab" x="478" y="{ly}">Customer to the nearest edge</text>')
    ly2 = ly + 22
    body.append(f'<line class="backbone" x1="16" x2="38" y1="{ly2 - 5}" y2="{ly2 - 5}"/>')
    body.append(f'<text class="lab" x="44" y="{ly2}">AWS network, from the edge to a Region when the edge can\'t answer by itself</text>')
    body.append(f'<text class="note" x="16" y="{ly2 + 24}">For current counts, see AWS\'s Global Infrastructure page. Drawn from AWS pages checked 2026-10-23.</text>')
    svg("03-04-regions-and-edge.svg", w, ly2 + 38,
        "Schematic of Regions and edge locations around the world",
        "A schematic, not a map. Three panels: North America, Europe and Asia Pacific. Each holds two Region "
        "boxes, each with three small Availability Zone squares inside, and about eight small dots for edge "
        "locations, scattered more widely. In the Europe panel, a customer connects by a short solid line to "
        "the nearest edge location; a dashed line runs from that edge location to a Region, labeled in the "
        "legend as the AWS network used when the edge can't answer by itself. Dashed lines under the panels "
        "show AWS's own global network linking Regions and edge locations. The number and position of shapes "
        "are illustrative; current counts are on AWS's Global Infrastructure page.", body, style=STYLE)


CARDS = [
    ("Edge location", False, [
        ("Where", "Many cities worldwide, beside and inside internet providers' networks"),
        ("Runs", "CloudFront, Route 53 and Global Accelerator, plus features that work through them, such as AWS WAF. Not your own servers"),
        ("Use it for", "Delivering content and answering requests close to users"),
    ]),
    ("Local Zone", False, [
        ("Where", "A large city away from the Region it extends"),
        ("Runs", "Selected services, such as compute, storage and databases"),
        ("Use it for", "Single-digit-millisecond latency for users in that city; keeping data there"),
    ]),
    ("Outposts", False, [
        ("Where", "Your own building: your data center or site"),
        ("Runs", "AWS racks or servers that AWS manages; you provide space, power and network"),
        ("Use it for", "Low latency to on-site systems, local processing, keeping data on site"),
    ]),
    ("Wavelength Zone", True, [
        ("Where", "Inside a telecom carrier's 5G network, extending a Region"),
        ("Runs", "Compute and storage, such as EC2 instances"),
        ("Use it for", "Ultra-low latency to phones and other mobile devices"),
    ]),
]


def edge_options():
    """Four cards: where each edge option physically is, what runs there, what it's for."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Four ways AWS reaches beyond its Regions</text>',
        '<text class="sub" x="16" y="48">The question that separates them: where is it, physically?</text>',
    ]
    cw, gap, top = 318, 12, 66
    rows = []
    for i in range(0, 4, 2):
        rows.append(CARDS[i:i + 2])
    y = top
    for row in rows:
        heights = []
        laid = []
        for name, out, items in row:
            lines = [(k, wrap(v, 34)) for k, v in items]
            h = 34 + sum(8 + 15 * len(ls) for _, ls in lines) + (40 if out else 6)
            heights.append(h)
            laid.append((name, out, lines))
        h = max(heights)
        for j, (name, out, lines) in enumerate(laid):
            x = 16 + j * (cw + gap)
            body.append(f'<rect class="{"cardhi" if out else "card"}" x="{x}" y="{y}" width="{cw}" height="{h}" rx="8"/>')
            body.append(f'<text class="name" x="{x + 14}" y="{y + 24}">{name}</text>')
            yy = y + 46
            for k, ls in lines:
                body.append(f'<text class="key" x="{x + 14}" y="{yy}">{k}</text>')
                yy = text_lines(body, x + 92, yy, ls, cls="cells", dy=15) + 8
            if out:
                body.append(f'<text class="key" x="{x + 14}" y="{y + h - 28}">Out of scope for CLF-C02 as a service:</text>')
                body.append(f'<text class="key" x="{x + 14}" y="{y + h - 12}">know it as a wrong answer</text>')
        y += h + gap
    body.append(f'<text class="note" x="16" y="{y + 8}">Our summary of AWS\'s Local Zones, Wavelength, Outposts and CloudFront pages, checked 2026-10-24.</text>')
    svg("03-04-edge-options.svg", w, y + 22,
        "Edge location, Local Zone, Outposts and Wavelength Zone compared",
        "Four cards. Edge location: in many cities worldwide, beside and inside internet providers' networks; "
        "runs CloudFront, Route 53 and Global Accelerator, plus features that work through them such as AWS WAF, "
        "but not your own servers; used for delivering content "
        "and answering requests close to users. Local Zone: in a large city away from the Region it extends; "
        "runs selected services such as compute, storage and databases; used for single-digit-millisecond "
        "latency for users in that city and for keeping data there. Outposts: in your own building; AWS racks "
        "or servers that AWS manages, with you providing space, power and network; used for low latency to "
        "on-site systems, local processing and keeping data on site. Wavelength Zone, drawn with a dashed "
        "border: inside a telecom carrier's 5G network, extending a Region; runs compute and storage such as "
        "EC2 instances; used for ultra-low latency to phones and other mobile devices; out of scope for "
        "CLF-C02 as a service.", body, style=STYLE)


if __name__ == "__main__":
    regions_and_edge()
    edge_options()
