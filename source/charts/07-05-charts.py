#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for Lab 09 (build a small VPC) as SVG.

Usage: python3 -I source/charts/07-05-charts.py
Writes images/07-05-lab-vpc.svg: the network the lab builds. Facts from the Amazon VPC
User Guide, retrieved 2026-10-23: a subnet sits in one Availability Zone ("Subnets for
your VPC"); a subnet whose route table has a route to an internet gateway is a public
subnet, one without is private ("Enable internet access for a VPC using an internet
gateway"); network ACLs work at the subnet level and security groups are attached to
resources ("Network ACLs", "Security groups"). Prices: AWS Price List offer files for
US East (N. Virginia), retrieved 2026-10-24 (AmazonEC2: NAT gateway $0.045 per hour;
AmazonVPC: public IPv4 address $0.005 per hour).
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# AWS's Availability Zones = slot 1 (blue) tint; what the learner builds = slot 2 (orange)
# tint, the meaning those colors carry in Modules 03 and 04. Words name every box.
STYLE = make_style(
    light_extra=" --az-fill:#d9e8fb; --you-fill:#fbe1d6; --card:#fcfcfb;",
    dark_extra=" --az-fill:#1b3554; --you-fill:#4d2716; --card:#1a1a19;",
    rules_extra="""
  .region { fill: none; stroke: var(--ink2); stroke-width: 1.5; stroke-dasharray: 6 4; }
  .vpc { fill: none; stroke: var(--ink); stroke-width: 2; }
  .az { fill: var(--az-fill); stroke: var(--s1); stroke-width: 1.2; }
  .you { fill: var(--you-fill); stroke: var(--s2); stroke-width: 1.5; }
  .card { fill: var(--card); stroke: var(--ink2); stroke-width: 1; }
  .hl { fill: var(--card); stroke: var(--ink); stroke-width: 3; }
  .none { fill: var(--card); stroke: var(--muted); stroke-width: 1.2; stroke-dasharray: 4 3; }
  .gw { fill: var(--card); stroke: var(--ink); stroke-width: 2; }
  .flow { stroke: var(--ink); stroke-width: 2; fill: none; }
  .arrowhead { fill: var(--ink); }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .bold { fill: var(--ink); font-size: 12px; font-weight: 700; }
  .small { fill: var(--ink2); font-size: 12px; }
  .tiny { fill: var(--ink2); font-size: 11px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

DEFS = ('<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
        'orient="auto-start-reverse"><path class="arrowhead" d="M0,0 L10,5 L0,10 Z"/></marker></defs>')


def lab_vpc():
    w = 680
    body = [
        DEFS,
        '<text class="title" x="16" y="28">The network you build in Lab 09</text>',
        '<text class="sub" x="16" y="48">One VPC, two subnets in two Availability Zones, and nothing that bills by the hour</text>',
    ]
    # the internet, outside everything
    body.append('<rect class="card" x="150" y="62" width="180" height="28" rx="14"/>')
    body.append('<text class="boxt" x="240" y="81" text-anchor="middle">The internet</text>')
    # Region and VPC
    body.append('<rect class="region" x="16" y="112" width="648" height="500" rx="10"/>')
    body.append('<text class="small" x="652" y="130" text-anchor="end">Region: US East (N. Virginia), us-east-1</text>')
    body.append('<rect class="vpc" x="32" y="142" width="616" height="458" rx="8"/>')
    body.append('<text class="boxt" x="634" y="164" text-anchor="end">VPC clf-lab09-vpc</text>')
    body.append('<text class="small" x="634" y="180" text-anchor="end">10.0.0.0/16, about 65,000 private addresses</text>')
    # internet gateway on the VPC's edge
    body.append('<line class="flow" x1="240" y1="90" x2="240" y2="126" marker-start="url(#arr)" marker-end="url(#arr)"/>')
    body.append('<rect class="gw" x="130" y="128" width="220" height="30" rx="5"/>')
    body.append('<text class="boxt" x="240" y="148" text-anchor="middle">Internet gateway clf-lab09-igw</text>')
    # two AZ columns, each holding one subnet
    ay, ah, aw = 196, 276, 292
    azs = [(48, "Availability Zone us-east-1a"), (340, "Availability Zone us-east-1b")]
    for ax, name in azs:
        body.append(f'<rect class="az" x="{ax}" y="{ay}" width="{aw}" height="{ah}" rx="7"/>')
        body.append(f'<text class="small" x="{ax + 12}" y="{ay + 18}">{name}</text>')
    sy, sh, sw = ay + 28, ah - 40, aw - 24
    subnets = [
        (60, "Public subnet clf-lab09-public-a", "10.0.1.0/24",
         "Route table clf-lab09-public-rt", [("10.0.0.0/16 → local", "card"), ("0.0.0.0/0 → internet gateway", "hl")],
         "The route to the internet gateway makes this subnet public.",
         "Network ACL clf-lab09-public-nacl: deny 203.0.113.0/24, allow HTTPS in, allow replies out"),
        (352, "Private subnet clf-lab09-private-b", "10.0.4.0/24",
         "Main route table (made with the VPC)", [("10.0.0.0/16 → local", "card"), ("no route to the internet", "none")],
         "No route to the internet gateway: this subnet is private.",
         "Default network ACL (made with the VPC): allows all traffic in and out"),
    ]
    for sx, title, cidr, rt, routes, why, nacl in subnets:
        body.append(f'<rect class="you" x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="6"/>')
        body.append(f'<text class="boxt" x="{sx + 12}" y="{sy + 20}">{title}</text>')
        body.append(f'<text class="small" x="{sx + 12}" y="{sy + 36}">{cidr}</text>')
        rx, ry, rw = sx + 12, sy + 48, sw - 24
        body.append(f'<rect class="card" x="{rx}" y="{ry}" width="{rw}" height="82" rx="5"/>')
        body.append(f'<text class="small" x="{rx + 10}" y="{ry + 18}">{rt}</text>')
        for k, (route, cls) in enumerate(routes):
            yy = ry + 26 + k * 26
            body.append(f'<rect class="{cls}" x="{rx + 8}" y="{yy}" width="{rw - 16}" height="22" rx="4"/>')
            tcls = "bold" if cls == "hl" else "small"
            body.append(f'<text class="{tcls}" x="{rx + 16}" y="{yy + 15}">{route}</text>')
        text_lines(body, sx + 12, ry + 102, wrap(why, 38), cls="bold", dy=15)
        text_lines(body, sx + 12, ry + 148, wrap(nacl, 44), cls="tiny", dy=14)
    # the route that makes the subnet public, fed by the gateway
    row_y = sy + 48 + 26 + 26 + 11
    body.append(f'<path class="flow" d="M334,158 L334,{row_y} L{60 + 12 + (aw - 24 - 24) + 2},{row_y}" marker-end="url(#arr)"/>')
    # security groups: part of the VPC, not of a subnet
    gy = ay + ah + 14
    body.append(f'<rect class="card" x="48" y="{gy}" width="584" height="100" rx="7"/>')
    body.append(f'<text class="small" x="60" y="{gy + 20}">Security groups belong to the VPC and are attached to resources, such as a server (none in this lab)</text>')
    sgs = [(60, "clf-lab09-web-sg", "In: HTTPS (443) from anywhere"),
           (346, "clf-lab09-db-sg", "In: port 5432 only from clf-lab09-web-sg")]
    for gx, name, rule in sgs:
        body.append(f'<rect class="you" x="{gx}" y="{gy + 32}" width="274" height="56" rx="6"/>')
        body.append(f'<text class="boxt" x="{gx + 12}" y="{gy + 54}">{name}</text>')
        body.append(f'<text class="small" x="{gx + 12}" y="{gy + 74}">{rule}</text>')
    ny = 636
    ny = text_lines(body, 16, ny, wrap("Not built: a NAT gateway ($0.045 an hour) or an Elastic IP or other public IPv4 "
                                      "address ($0.005 an hour). US East (N. Virginia) prices as of 2026-10-24.", 104),
                    cls="note", dy=16)
    svg("07-05-lab-vpc.svg", w, ny,
        "The network Lab 09 builds: one VPC with a public and a private subnet in two Availability Zones",
        "Outside everything, the internet, joined by a two-way arrow to an internet gateway named clf-lab09-igw on "
        "the edge of the VPC. A dashed box marks the Region, US East (N. Virginia), us-east-1. Inside it, the VPC "
        "clf-lab09-vpc, with the address range 10.0.0.0/16. The VPC holds two Availability Zone columns. In "
        "us-east-1a, the public subnet clf-lab09-public-a, 10.0.1.0/24, uses route table clf-lab09-public-rt with "
        "two routes: 10.0.0.0/16 to local, and 0.0.0.0/0 to the internet gateway. That second route is "
        "highlighted, an arrow runs to it from the internet gateway, and a label says this one route makes the "
        "subnet public. Its network ACL, clf-lab09-public-nacl, denies 203.0.113.0/24, allows HTTPS in and "
        "allows replies out. In us-east-1b, the private subnet clf-lab09-private-b, 10.0.4.0/24, uses the main "
        "route table made with the VPC, with only the local route and no route to the internet, and the default "
        "network ACL, which allows all traffic. Below the subnets, still inside the VPC, two security groups, "
        "which belong to the VPC and are attached to resources: clf-lab09-web-sg allows HTTPS on port 443 in "
        "from anywhere; clf-lab09-db-sg allows port 5432 in only from clf-lab09-web-sg. A note says the lab "
        "builds no NAT gateway ($0.045 an hour) and no Elastic IP or other public IPv4 address ($0.005 an "
        "hour), US East (N. Virginia) prices as of 2026-10-24.", body, style=STYLE)


if __name__ == "__main__":
    lab_vpc()
