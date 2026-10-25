#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 07.01 (your own network) as SVG.

Usage: python3 -I source/charts/07-01-charts.py
Writes images/07-01-*.svg. Facts come from the Amazon VPC User Guide ("How Amazon
VPC works", subnets, route tables, internet gateways, NAT gateways, NAT gateway
pricing), the Amazon VPC FAQ and the PrivateLink guide, checked 2026-10-23: a
subnet sits in one Availability Zone; a subnet is public when its route table
has a route to an internet gateway, and an instance also needs a public IPv4
address (or IPv6) to use it; a public NAT gateway sits in a public subnet with an
Elastic IP address, and connections through it can only start inside the VPC;
an internet gateway has no charge. The price is the US East (N. Virginia) row of the
AWS Price List offer file AmazonVPC, retrieved 2026-10-24 (research repo
sources/raw/pricing/compute-networking-us-east-1-summary.tsv): public IPv4
address $0.005 per hour, in use or idle.
The bakery and its addresses are made up for teaching. Our own design: no AWS
logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Public (reachable from the internet) = slot 1 (blue) tint; private = neutral.
# The one route that makes a subnet public carries the same tint. Words carry
# every meaning; color only repeats it.
STYLE = make_style(
    light_extra=" --pub-fill:#d9e8fb; --priv-fill:#f1f0ec; --bad-fill:#fbe1d6; --s3c:#1baf7a;",
    dark_extra=" --pub-fill:#1b3554; --priv-fill:#252523; --bad-fill:#4d2716; --s3c:#199e70;",
    rules_extra="""
  .pub { fill: var(--pub-fill); stroke: var(--s1); stroke-width: 1.5; }
  .priv { fill: var(--priv-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .bad { fill: var(--bad-fill); stroke: var(--s2); stroke-width: 1.5; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .zone { fill: none; stroke: var(--axis); stroke-width: 1.5; stroke-dasharray: 6 4; }
  .region { fill: none; stroke: var(--ink2); stroke-width: 1.2; }
  .vpc { fill: none; stroke: var(--ink); stroke-width: 1.8; }
  .s3c { fill: var(--s3c); }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .zlab { fill: var(--muted); font-size: 12px; }
  .small { fill: var(--ink2); font-size: 12px; }
  .mono { fill: var(--ink); font-size: 12px; font-family: ui-monospace, "SFMono-Regular", Menlo, monospace; }
  .arrlab { fill: var(--ink2); font-size: 11.5px; font-style: italic; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }
  .cross { stroke: var(--s2); stroke-width: 2.5; stroke-linecap: round; }
  .val { fill: var(--ink); font-size: 13px; font-weight: 600; font-variant-numeric: tabular-nums; }""")


def arrow(body, x1, y1, x2, y2, dashed=False):
    """A straight line with a small filled head at (x2, y2), any direction."""
    dash = ' stroke-dasharray="5 4"' if dashed else ""
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"{dash}/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


def big_picture():
    """The bakery's VPC: two AZs, a public and a private subnet in each, an internet gateway, two route tables."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">The bakery\'s own network: what makes half of it public</text>',
        '<text class="sub" x="16" y="48">A VPC in one Region, with a public and a private subnet in each of two Availability Zones</text>',
    ]
    # The internet and the internet gateway.
    rect(body, "plain", 250, 62, 180, 30, 15)
    body.append('<text class="cellt" x="340" y="82" text-anchor="middle">The internet (customers)</text>')
    rx, ry, rw = 16, 112, 648
    vx, vy, vw = 30, 140, 620
    igw_y = vy - 15
    arrow(body, 334, 93, 334, igw_y - 1)
    arrow(body, 346, igw_y - 1, 346, 93)
    # AZs and subnets.
    zy, zw, zh = vy + 46, 290, 196
    zx = [vx + 14, vx + 14 + zw + 12]
    py, ph = zy + 26, 72
    qy, qh = py + ph + 14, 72
    for i, x in enumerate(zx):
        rect(body, "zone", x, zy, zw, zh)
        body.append(f'<text class="zlab" x="{x + 8}" y="{zy + 16}">Availability Zone {"AB"[i]}</text>')
        rect(body, "pub", x + 10, py, zw - 20, ph)
        body.append(f'<text class="cellt" x="{x + 20}" y="{py + 19}">Public subnet 10.0.{1 + i}.0/24</text>')
        body.append(f'<text class="small" x="{x + 20}" y="{py + 38}">Web server (has a public IPv4 address)</text>')
        body.append(f'<text class="zlab" x="{x + 20}" y="{py + 60}">Uses: the public route table</text>')
        rect(body, "priv", x + 10, qy, zw - 20, qh)
        body.append(f'<text class="cellt" x="{x + 20}" y="{qy + 19}">Private subnet 10.0.{3 + i}.0/24</text>')
        db = "Order database (primary)" if i == 0 else "Order database (standby)"
        body.append(f'<text class="small" x="{x + 20}" y="{qy + 38}">{db}</text>')
        body.append(f'<text class="zlab" x="{x + 20}" y="{qy + 60}">Uses: the private route table</text>')
    # Internet traffic from the gateway to the public subnets only.
    ty = vy + 36
    body.append(f'<path class="arrow" d="M340,{igw_y + 31} L340,{ty} M{zx[0] + zw / 2:.1f},{ty} L{zx[1] + zw / 2:.1f},{ty}"/>')
    for x in zx:
        arrow(body, x + zw / 2, ty, x + zw / 2, py - 1)
    body.append(f'<text class="arrlab" x="{zx[1] + zw / 2 + 8:.1f}" y="{ty - 5}">internet traffic</text>')
    # Route tables.
    ty2 = zy + zh + 16
    tw = zw
    rows = [
        ("Public route table", [("10.0.0.0/16", "local: stays inside the VPC", False),
                                ("0.0.0.0/0", "internet gateway", True)]),
        ("Private route table", [("10.0.0.0/16", "local: stays inside the VPC", False),
                                 (None, "No route to the internet gateway", False)]),
    ]
    for x, (name, routes) in zip(zx, rows):
        rect(body, "plain", x, ty2, tw, 92)
        body.append(f'<text class="cellt" x="{x + 10}" y="{ty2 + 19}">{name}</text>')
        body.append(f'<text class="zlab" x="{x + 10}" y="{ty2 + 37}">Destination</text>')
        body.append(f'<text class="zlab" x="{x + 104}" y="{ty2 + 37}">Target</text>')
        yy = ty2 + 44
        for dest, target, hi in routes:
            if hi:
                rect(body, "pub", x + 4, yy, tw - 8, 20, 4)
            if dest is None:
                body.append(f'<text class="small" x="{x + 10}" y="{yy + 14}">{target}</text>')
            else:
                body.append(f'<text class="mono" x="{x + 10}" y="{yy + 14}">{dest}</text>')
                body.append(f'<text class="small" x="{x + 104}" y="{yy + 14}">{target}</text>')
            yy += 22
    vh = ty2 + 92 + 14 - vy
    rect(body, "vpc", vx, vy, vw, vh, 8)
    body.append(f'<text class="head" x="{vx + 10}" y="{vy + 24}">VPC: the bakery\'s network, 10.0.0.0/16</text>')
    rh = vy + vh + 12 - ry
    rect(body, "region", rx, ry, rw, rh, 8)
    body.append(f'<text class="zlab" x="{rx + 8}" y="{ry + 18}">AWS Region: US East (N. Virginia)</text>')
    # The gateway is drawn last, on top of the VPC border it is attached to.
    rect(body, "pub", 270, igw_y, 140, 30)
    body.append(f'<text class="cellt" x="340" y="{igw_y + 20}" text-anchor="middle">Internet gateway</text>')
    y = ry + rh + 22
    body.append(f'<text class="note" x="16" y="{y}">The highlighted route is the only difference between the two kinds of subnet. Addresses are examples;</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">the bakery is made up for teaching. From the Amazon VPC User Guide, checked 2026-10-23.</text>')
    svg("07-01-big-picture.svg", w, y + 30,
        "The bakery's VPC with public and private subnets in two Availability Zones",
        "The internet sits above an AWS Region, US East (N. Virginia). Arrows run both ways between the internet "
        "and an internet gateway attached to the top of the bakery's VPC, 10.0.0.0/16. Inside the VPC are two "
        "Availability Zones, A and B. Each holds a public subnet (10.0.1.0/24 and 10.0.2.0/24) with a web server "
        "that has a public IPv4 address, and a private subnet (10.0.3.0/24 and 10.0.4.0/24) holding the order "
        "database: the primary in AZ A and the standby in AZ B. Internet traffic from the gateway reaches only "
        "the public subnets. Below, two route tables. The public route table, used by both public subnets, has "
        "10.0.0.0/16 to local (stays inside the VPC) and, highlighted, 0.0.0.0/0 to the internet gateway. The "
        "private route table, used by both private subnets, has only 10.0.0.0/16 to local and no route to the "
        "internet gateway. A note says the highlighted route is the only difference between the two kinds of "
        "subnet.", body, style=STYLE)


def public_or_not():
    """A 2x2 grid: route to the internet gateway (yes/no) by public IPv4 address (yes/no)."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Two things must be true to talk to the internet directly</text>',
        '<text class="sub" x="16" y="48">The route makes the subnet public; the address lets one server use that route</text>',
    ]
    lw = 150
    cw, gap = 247, 10
    xs = [16 + lw + i * (cw + gap) for i in range(2)]
    y0 = 70
    body.append(f'<text class="head" x="{xs[0]}" y="{y0 + 14}">The server has a public IPv4 address</text>')
    body.append(f'<text class="head" x="{xs[1]}" y="{y0 + 14}">The server has no public address</text>')
    rows = [
        ("Route table sends 0.0.0.0/0 to the internet gateway", "Public subnet",
         [("pub", "Reaches the internet, and the internet can reach it",
           "Example: the bakery's web server. Its security group still decides what gets in (07.02)."),
          ("priv", "Can't use the internet gateway",
           "The subnet is public, but this server has no public address for the gateway to translate.")]),
        ("No route to the internet gateway", "Private subnet",
         [("bad", "Still can't reach the internet",
           "There is no route out, so the address does nothing. It still costs $0.005 an hour (2026-10-24)."),
          ("priv", "Private: unreachable from the internet",
           "Example: the order database. To reach out, it would need a NAT gateway route.")]),
    ]
    y = y0 + 28
    ch = 124
    for label, kind, cells in rows:
        text_lines(body, 16, y + 22, wrap(label, 20), cls="cellt", dy=16)
        body.append(f'<text class="zlab" x="16" y="{y + ch - 14}">= {kind}</text>')
        for x, (cls, head, sub) in zip(xs, cells):
            rect(body, cls, x, y, cw, ch)
            yy = text_lines(body, x + 12, y + 22, wrap(head, 32), cls="cellt", dy=16)
            text_lines(body, x + 12, yy + 4, wrap(sub, 38), cls="cells", dy=15)
        y += ch + gap
    y += 14
    body.append(f'<text class="note" x="16" y="{y}">From the Amazon VPC User Guide (subnets; internet gateways), checked 2026-10-23. Price: AWS Price List,</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">US East (N. Virginia), retrieved 2026-10-24. The orange cell is the common mistake: a public address in a private subnet.</text>')
    svg("07-01-public-or-not.svg", w, y + 30,
        "What a server can do, by its subnet's route and its address",
        "A grid of four cells. Columns: the server has a public IPv4 address; the server has no public address. "
        "Rows: the route table sends 0.0.0.0/0 to the internet gateway, which makes a public subnet; there is no "
        "route to the internet gateway, which makes a private subnet. Public subnet with a public address: the "
        "server reaches the internet and the internet can reach it, for example the bakery's web server, whose "
        "security group still decides what gets in. Public subnet with no public address: the server can't use "
        "the internet gateway, because it has no public address to translate. Private subnet with a public "
        "address, marked as the common mistake: the server still can't reach the internet, because there is no "
        "route out; the address does nothing but still costs $0.005 an hour as of 2026-10-24. Private subnet "
        "with no public address: private and unreachable from the internet, for example the order database; to "
        "reach out it would need a route to a NAT gateway.", body, style=STYLE)


if __name__ == "__main__":
    big_picture()
    public_or_not()
