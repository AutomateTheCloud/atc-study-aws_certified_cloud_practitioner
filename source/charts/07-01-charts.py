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
an internet gateway has no charge. Prices are US East (N. Virginia) rows of the
AWS Price List offer files AmazonEC2 and AmazonVPC, retrieved 2026-10-24
(research repo sources/raw/pricing/compute-networking-us-east-1-summary.tsv):
NAT gateway $0.045 per hour and $0.045 per GB processed; public IPv4 address
$0.005 per hour, in use or idle. Monthly figures use a month of 730 hours.
The bakery and its addresses are made up for teaching. Our own design: no AWS
logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, swatch, text_lines, wrap  # noqa: E402

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


def igw_vs_nat():
    """Two panels: who can start a connection through an internet gateway and through a NAT gateway."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Internet gateway or NAT gateway: who can start the conversation?</text>',
        '<text class="sub" x="16" y="48">Replies always come back the way the request went; the difference is who may begin</text>',
    ]
    pw = 316
    px = [16, 16 + pw + 16]
    top = 66
    for x, head in zip(px, ["Internet gateway", "NAT gateway"]):
        rect(body, "region", x, top, pw, 330, 8)
        body.append(f'<text class="head" x="{x + 12}" y="{top + 22}">{head}</text>')
    # Left panel: internet, gateway, public subnet with server.
    x = px[0]
    bx, bw = x + 78, 160
    rect(body, "plain", bx, top + 40, bw, 30, 15)
    body.append(f'<text class="cellt" x="{bx + bw / 2}" y="{top + 60}" text-anchor="middle">The internet</text>')
    rect(body, "pub", bx, top + 110, bw, 30)
    body.append(f'<text class="cellt" x="{bx + bw / 2}" y="{top + 130}" text-anchor="middle">Internet gateway</text>')
    rect(body, "pub", x + 30, top + 180, pw - 60, 70)
    body.append(f'<text class="cellt" x="{x + 42}" y="{top + 199}">Public subnet</text>')
    body.append(f'<text class="small" x="{x + 42}" y="{top + 218}">Web server with a public</text>')
    body.append(f'<text class="small" x="{x + 42}" y="{top + 234}">IPv4 address</text>')
    cx = bx + bw / 2
    for y1, y2 in [(top + 71, top + 109), (top + 141, top + 179)]:
        arrow(body, cx - 8, y1, cx - 8, y2)
        arrow(body, cx + 8, y2, cx + 8, y1)
    body.append(f'<text class="arrlab" x="{cx + 20}" y="{top + 94}">either side can start</text>')
    rows_l = ["Who can start: the internet or your server", "Lives: attached to the VPC",
              "Cost: no charge for the gateway itself"]
    text_lines(body, x + 14, top + 280, rows_l, cls="small", dy=17)
    # Right panel: internet, gateway, NAT gateway in a public subnet, server in a private subnet.
    x = px[1]
    bx = x + 78
    rect(body, "plain", bx, top + 40, bw, 30, 15)
    body.append(f'<text class="cellt" x="{bx + bw / 2}" y="{top + 60}" text-anchor="middle">The internet</text>')
    rect(body, "pub", bx, top + 92, bw, 26)
    body.append(f'<text class="cellt" x="{bx + bw / 2}" y="{top + 110}" text-anchor="middle">Internet gateway</text>')
    rect(body, "pub", x + 30, top + 140, pw - 60, 44)
    body.append(f'<text class="cellt" x="{x + 42}" y="{top + 158}">Public subnet</text>')
    body.append(f'<text class="small" x="{x + 42}" y="{top + 176}">NAT gateway (with an Elastic IP)</text>')
    rect(body, "priv", x + 30, top + 206, pw - 60, 44)
    body.append(f'<text class="cellt" x="{x + 42}" y="{top + 224}">Private subnet</text>')
    body.append(f'<text class="small" x="{x + 42}" y="{top + 242}">Server with no public address</text>')
    cx = bx + bw / 2
    for y1, y2 in [(top + 205, top + 185), (top + 139, top + 119), (top + 91, top + 71)]:
        arrow(body, cx + 8, y1, cx + 8, y2)
    body.append(f'<text class="arrlab" x="{cx + 20}" y="{top + 200}">only the server starts</text>')
    # A blocked attempt from the internet.
    arrow(body, cx - 40, top + 71, cx - 40, top + 132, dashed=True)
    body.append(f'<line class="cross" x1="{cx - 47}" y1="{top + 128}" x2="{cx - 33}" y2="{top + 142}"/>')
    body.append(f'<line class="cross" x1="{cx - 33}" y1="{top + 128}" x2="{cx - 47}" y2="{top + 142}"/>')
    body.append(f'<text class="arrlab" x="{x + 12}" y="{top + 82}">can\'t start</text>')
    body.append(f'<text class="arrlab" x="{x + 12}" y="{top + 96}">a connection in</text>')
    rows_r = ["Who can start: only your private server", "Lives: in a public subnet, often one per AZ",
              "Cost: $0.045 an hour + $0.045 per GB"]
    text_lines(body, x + 14, top + 280, rows_r, cls="small", dy=17)
    y = top + 330 + 22
    body.append(f'<text class="note" x="16" y="{y}">From the Amazon VPC User Guide (internet gateways; NAT gateways), checked 2026-10-23. NAT gateway prices:</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">AWS Price List, US East (N. Virginia), retrieved 2026-10-24. The Elastic IP and data transfer are charged on top.</text>')
    svg("07-01-igw-vs-nat.svg", w, y + 30,
        "Internet gateway compared with NAT gateway",
        "Two panels. Left, internet gateway: the internet, then an internet gateway, then a public subnet holding "
        "a web server with a public IPv4 address. Arrows run both ways between each pair, labeled either side can "
        "start. Notes: who can start, the internet or your server; it is attached to the VPC; there is no charge "
        "for the gateway itself. Right, NAT gateway: the internet, an internet gateway, a public subnet holding a "
        "NAT gateway with an Elastic IP address, and below it a private subnet holding a server with no public "
        "address. Arrows run upward only, from the server to the NAT gateway, to the internet gateway, to the "
        "internet, labeled only the server starts. A dashed arrow from the internet is crossed out before it "
        "reaches the NAT gateway, labeled can't start a connection in. Notes: who can start, only your private "
        "server; it lives in a public subnet, often one per AZ; cost $0.045 an hour plus $0.045 per GB processed, US "
        "East (N. Virginia) as of 2026-10-24, with the Elastic IP and data transfer charged on top.",
        body, style=STYLE)


HOURS = 730            # a month of 730 hours, as the guide uses elsewhere
NAT_HOUR = 0.045       # USD per NAT gateway hour, us-east-1, retrieved 2026-10-24
NAT_GB = 0.045         # USD per GB processed
IPV4_HOUR = 0.005      # USD per public IPv4 address hour (an Elastic IP counts)
SCENARIOS = [
    ("One NAT gateway, 10 GB processed", 1, 10),
    ("One NAT gateway, 200 GB processed", 1, 200),
    ("Two NAT gateways (one per AZ), 200 GB in total", 2, 200),
    ("Gateway endpoint instead, for 200 GB to S3", 0, 0),
]


def nat_cost():
    """Stacked horizontal bars: a month of NAT gateway hours, its Elastic IP, and data processed."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">A NAT gateway bills every hour, even when it carries almost nothing</text>',
        '<text class="sub" x="16" y="48">US dollars for a month of 730 hours, US East (N. Virginia) prices as of 2026-10-24</text>',
    ]
    swatch(body, 16, 76, "s1", "NAT gateway hours")
    swatch(body, 176, 76, "s3c", "Its Elastic IP address")
    swatch(body, 356, 76, "s2", "Data processed")
    left, pw = 220, 360
    vmax = 90.0
    top = 98
    # Gridlines.
    for v in range(0, 91, 30):
        x = left + pw * v / vmax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top}" y2="{top + 4 * 56 - 6}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top + 4 * 56 + 10}" text-anchor="middle">${v}</text>')
    rows = []
    for i, (label, n, gb) in enumerate(SCENARIOS):
        parts = [n * HOURS * NAT_HOUR, n * HOURS * IPV4_HOUR, (gb * NAT_GB if n else 0.0)]
        total = sum(parts)
        rows.append((label, parts, total))
        y = top + i * 56 + 8
        text_lines(body, 16, y + 13, wrap(label, 28), cls="lab", dy=16)
        x = left
        segs = [(p, c) for p, c in zip(parts, ["s1", "s3c", "s2"]) if p > 0]
        for j, (p, cls) in enumerate(segs):
            sw = pw * p / vmax
            last = j == len(segs) - 1
            gapw = 0 if last else 2
            if last:
                body.append(f'<path class="{cls}" d="{right_rounded(x, y, sw, 24)}"/>')
            else:
                body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{max(sw - gapw, 1):.1f}" height="24"/>')
            x += sw
        txt = f"${total:,.2f}" if total else "$0: no charge"
        body.append(f'<text class="val" x="{x + 8:.1f}" y="{y + 17}">{txt}</text>')
    y = top + 4 * 56 + 34
    for line in [
        "NAT gateway: $0.045 an hour and $0.045 per GB processed. Public IPv4 address, including an Elastic IP: $0.005 an hour.",
        "Data transfer to the internet is charged on top of all bars (lesson 07.04). A partial hour bills as a full hour.",
        "Source: AWS Price List offer files AmazonEC2 and AmazonVPC, US East (N. Virginia), retrieved 2026-10-24.",
    ]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg("07-01-nat-cost.svg", w, y + 14,
        "Monthly cost of NAT gateways compared with a gateway endpoint",
        "Horizontal stacked bars of US dollars for a month of 730 hours, US East (N. Virginia) prices as of 2026-10-24. "
        + " ".join(
            f"{label}: ${total:,.2f}" + (
                f" (NAT gateway hours ${p[0]:,.2f}, Elastic IP ${p[1]:,.2f}, data processed ${p[2]:,.2f})." if total
                else ", no charge.")
            for label, p, total in rows)
        + " The hourly part is most of the bill at low traffic, and doubles with a second gateway. Data transfer "
        "to the internet is charged on top.", body, style=STYLE)
    return rows


if __name__ == "__main__":
    big_picture()
    public_or_not()
    igw_vs_nat()
    for label, p, total in nat_cost():
        print(f"{label}: {p} = {total:.2f}")
