#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 07.04 (connecting networks and offices) as SVG.

Usage: python3 -I source/charts/07-04-charts.py
Writes images/07-04-*.svg. Facts come from AWS pages cited in
guide/07-connecting-it/04-connecting-networks-and-offices.md, read 2026-10-23:
What is AWS Site-to-Site VPN?, What is AWS Client VPN?, the AWS VPN FAQ, What is
Direct Connect? and the Direct Connect FAQ (dedicated private connection that
bypasses the internet; MACsec as an option; a VPN over it), What is VPC peering?
(one-to-one, non-transitive), What is AWS Transit Gateway? (a hub), and What is
AWS PrivateLink? (one service, through an interface endpoint).

Prices, US East (N. Virginia), USD:
- data transfer: AWS Price List AWSDataTransfer offer file, publicationDate
  2026-09-16 (retrieved 2026-10-23): in from the internet $0.00/GB; out to the
  internet $0.09/GB for the first 10 TB a month after the 100 GB monthly free
  allowance; to most other Regions $0.02/GB (US East (Ohio) $0.01/GB); regional
  transfer across Availability Zones $0.01/GB, charged in each direction.
  Same-AZ transfer and S3 to CloudFront are free per the EC2 and S3 pricing pages.
- NAT gateway data processing $0.045/GB: AmazonEC2 offer file published
  2026-10-23 (retrieved 2026-10-24).
- Site-to-Site VPN connection $0.05/hour; Client VPN endpoint association
  $0.10/hour and connection $0.05/hour; Transit Gateway attachment $0.05/hour plus
  $0.02/GB processed; interface VPC endpoint $0.01/hour per AZ plus $0.01/GB:
  AmazonVPC offer file published 2026-10-16 (retrieved 2026-10-24).
Monthly figures are our arithmetic for a 730-hour month. The bakery's setup is made
up for teaching. Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, text_lines  # noqa: E402

STYLE = make_style(
    light_extra=" --aws-fill:#d9e8fb; --link-fill:#fbe1d6; --prem-fill:#f1f0ec; --net-fill:#ecebe6;",
    dark_extra=" --aws-fill:#1b3554; --link-fill:#4d2716; --prem-fill:#252523; --net-fill:#262624;",
    rules_extra="""
  .aws { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .link { fill: var(--link-fill); stroke: var(--s2); stroke-width: 1.5; }
  .prem { fill: var(--prem-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .net { fill: var(--net-fill); stroke: var(--axis); stroke-width: 1; }
  .zone { fill: none; stroke: var(--axis); stroke-width: 1.5; stroke-dasharray: 6 4; }
  .panel { fill: none; stroke: var(--axis); stroke-width: 1; }
  .cellhi { fill: var(--link-fill); stroke: var(--s2); stroke-width: 2; }
  .cell { fill: var(--prem-fill); stroke: var(--axis); stroke-width: 1; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .arrlab { fill: var(--ink); font-size: 11.5px; font-weight: 600; }
  .arrsub { fill: var(--ink2); font-size: 11px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .flow { stroke: var(--ink); stroke-width: 2; fill: none; }
  .flowp { stroke: var(--s1); stroke-width: 3; fill: none; }
  .flowt { stroke: var(--ink); stroke-width: 2; fill: none; stroke-dasharray: 8 4; }
  .mesh { stroke: var(--ink2); stroke-width: 1.5; }
  .node { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .hub { fill: var(--link-fill); stroke: var(--s2); stroke-width: 2; }
  .val { fill: var(--ink); font-size: 13px; font-variant-numeric: tabular-nums; }
  .zero { stroke: var(--s1); stroke-width: 2; }
  .other { fill: var(--muted); }
  .head-ink { fill: var(--ink); }""")


def box(body, cls, x, y, w, h, title, lines=()):
    body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    body.append(f'<text class="boxt" x="{x + w / 2}" y="{y + 18}" text-anchor="middle">{title}</text>')
    text_lines(body, x + w / 2, y + 34, list(lines), cls="cells", dy=14, anchor="middle")


def line(body, pts, cls="flow", head=False):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    body.append(f'<path class="{cls}" d="{d}"/>')
    if head:
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        a = math.atan2(y2 - y1, x2 - x1)
        p1 = (x2 - 10 * math.cos(a) + 5 * math.sin(a), y2 - 10 * math.sin(a) - 5 * math.cos(a))
        p2 = (x2 - 10 * math.cos(a) - 5 * math.sin(a), y2 - 10 * math.sin(a) + 5 * math.cos(a))
        body.append(f'<path class="head-ink" d="M{x2:.1f},{y2:.1f} L{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z"/>')


def connection_map():
    """Big picture: the bakery's networks and the links between them."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Five ways to connect, on one map of the bakery</text>',
        '<text class="sub" x="16" y="48">Dashed lines cross the public internet inside encryption; the thick blue line avoids it</text>',
    ]
    # On-premises side
    body.append('<text class="small" x="96" y="80" text-anchor="middle">Outside AWS</text>')
    box(body, "prem", 16, 150, 160, 70, "Head office", ["office computers and", "the till server"])
    box(body, "prem", 64, 330, 112, 56, "Owner at home", ["one laptop"])
    # Internet band
    body.append('<rect class="net" x="214" y="96" width="120" height="314" rx="8"/>')
    text_lines(body, 274, 116, ["Public", "internet"], cls="boxt", dy=15, anchor="middle")
    # AWS side
    body.append('<rect class="zone" x="356" y="64" width="308" height="440" rx="10"/>')
    body.append('<text class="small" x="510" y="82" text-anchor="middle">AWS</text>')
    box(body, "aws", 380, 94, 268, 52, "German VPC", ["Europe (Frankfurt)"])
    box(body, "aws", 380, 200, 268, 104, "Site VPC", ["US East (N. Virginia)", "web server, order database"])
    box(body, "aws", 380, 420, 268, 56, "Partner's service", ["in the partner's own AWS account"])
    # Direct Connect location below the internet band
    box(body, "link", 204, 436, 140, 50, "Direct Connect", ["location"])
    # 1 Site-to-Site VPN: head office -> site VPC through the internet (dashed)
    line(body, [(176, 172), (380, 226)], cls="flowt", head=True)
    body.append('<text class="arrlab" x="274" y="160" text-anchor="middle">Site-to-Site VPN</text>')
    body.append('<text class="arrsub" x="274" y="174" text-anchor="middle">network to network</text>')
    # 2 Client VPN: home -> site VPC (dashed)
    line(body, [(176, 352), (380, 280)], cls="flowt", head=True)
    body.append('<text class="arrlab" x="274" y="352" text-anchor="middle">Client VPN</text>')
    body.append('<text class="arrsub" x="274" y="366" text-anchor="middle">one person\'s device</text>')
    # 3 Direct Connect: head office -> DX location -> AWS (thick blue, bypasses the band)
    line(body, [(36, 220), (36, 461), (204, 461)], cls="flowp")
    line(body, [(344, 461), (366, 461), (366, 292), (380, 292)], cls="flowp")
    body.append('<text class="arrlab" x="46" y="416">Direct Connect</text>')
    body.append('<text class="arrsub" x="46" y="430">private line</text>')
    # 4 Peering: site VPC <-> German VPC
    line(body, [(514, 146), (514, 200)])
    body.append('<text class="arrlab" x="524" y="170">VPC peering</text>')
    body.append('<text class="arrsub" x="524" y="184">two whole networks</text>')
    # 5 PrivateLink: site VPC -> partner's one service
    line(body, [(514, 304), (514, 420)], head=True)
    body.append('<text class="arrlab" x="524" y="356">PrivateLink</text>')
    body.append('<text class="arrsub" x="524" y="370">one service only</text>')
    y = 528
    y = text_lines(body, 16, y, [
        "Dashed: an encrypted VPN tunnel over the public internet. Thick blue: Direct Connect, a dedicated line that",
        "doesn\'t use the internet. Thin solid lines: links that stay inside AWS\'s network.",
    ], cls="small", dy=17)
    body.append(f'<text class="note" x="16" y="{y + 4}">The bakery\'s networks are made up for teaching. Drawn from AWS documentation checked 2026-10-23.</text>')
    svg("07-04-connection-map.svg", w, y + 18,
        "Map of the bakery's networks and the five kinds of link between them",
        "Left, outside AWS: the head office, with office computers and the till server, and the owner at home with "
        "one laptop. Middle: a band for the public internet. Right, inside AWS: the German VPC in Europe "
        "(Frankfurt) at the top, the site VPC in US East (N. Virginia) with the web server and order database in "
        "the middle, and a partner's service in the partner's own AWS account at the bottom. A dashed line labeled "
        "Site-to-Site VPN, network to network, runs from the head office across the internet band to the site VPC. "
        "A dashed line labeled Client VPN, one person's device, runs from the owner's laptop across the internet "
        "band to the site VPC. A thick blue line labeled Direct Connect, private line, runs from the head office "
        "down and around the internet band, through a Direct Connect location, into the site VPC. A solid line "
        "labeled VPC peering, two whole networks, joins the site VPC and the German VPC. A solid arrow "
        "labeled PrivateLink, one service only, runs from the site VPC to the partner's service.", body, style=STYLE)


def private_vs_encrypted():
    """A 2 x 2 grid: path (internet or private) by encryption."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Private and encrypted are two different questions</text>',
        '<text class="sub" x="16" y="48">Columns: which path the traffic takes. Rows: whether it is encrypted on the way.</text>',
    ]
    left, top, cw, ch = 150, 92, 254, 118
    body.append(f'<text class="boxt" x="{left + cw / 2}" y="{top - 12}" text-anchor="middle">Over the public internet</text>')
    body.append(f'<text class="boxt" x="{left + cw + 12 + cw / 2}" y="{top - 12}" text-anchor="middle">Private: off the internet</text>')
    text_lines(body, left - 12, top + 52, ["Encrypted"], cls="boxt", anchor="end")
    text_lines(body, left - 12, top + ch + 12 + 46, ["Not encrypted", "unless you", "add it"], cls="boxt", dy=15, anchor="end")
    cells = [
        (0, 0, "cellhi", "AWS VPN, both kinds", ["Site-to-Site: network to network", "Client VPN: one person's device", "Encrypted, but NOT private"]),
        (1, 0, "cell", "Direct Connect plus", ["MACsec on supported connections,", "or a VPN run over it", "Private and encrypted"]),
        (0, 1, "cell", "Plain internet traffic", ["Not a connection option:", "what a link is meant to avoid", ""]),
        (1, 1, "cell", "Direct Connect on its own", ["A dedicated line, off the internet", "Encryption is something you add", "Private"]),
    ]
    for c, r, cls, t, lines in cells:
        x = left + c * (cw + 12)
        y = top + r * (ch + 12)
        body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{cw}" height="{ch}" rx="8"/>')
        body.append(f'<text class="boxt" x="{x + 14}" y="{y + 26}">{t}</text>')
        text_lines(body, x + 14, y + 50, lines[:2], cls="cells", dy=16)
        if lines[2]:
            body.append(f'<text class="arrlab" x="{x + 14}" y="{y + ch - 16}">{lines[2]}</text>')
    y = top + 2 * ch + 12 + 32
    y = text_lines(body, 16, y, [
        "Highlighted: the cell people get wrong. A VPN protects what it carries, but the traffic still crosses the",
        "public internet, so its speed and delay vary with the internet. Private means the path, not the protection.",
    ], cls="small", dy=17)
    body.append(f'<text class="note" x="16" y="{y + 4}">Our summary of AWS\'s VPN and Direct Connect documentation and FAQs, checked 2026-10-23.</text>')
    svg("07-04-private-vs-encrypted.svg", w, y + 18,
        "Grid comparing connection options by path and by encryption",
        "A two-by-two grid. Columns: over the public internet, and private, off the internet. Rows: encrypted, "
        "and not encrypted unless you add it. Encrypted over the internet, highlighted: AWS VPN, both kinds: Site-to-Site "
        "VPN, network to network, and Client VPN for one person's device; encrypted, but not private. "
        "Encrypted and private: Direct Connect plus MACsec on supported connections, or a VPN run over it. Not "
        "encrypted, over the internet: plain internet traffic, not a connection option, what a link is meant to "
        "avoid. Private, not encrypted unless you add it: Direct Connect on its own, a dedicated line off the "
        "internet where encryption is something you add. A note says the highlighted cell is the one people get "
        "wrong: a VPN protects what it carries, but the traffic still crosses the public internet; private means "
        "the path, not the protection.", body, style=STYLE)


def ring(cx, cy, r, n, start=-90):
    return [(cx + r * math.cos(math.radians(start + 360 * i / n)), cy + r * math.sin(math.radians(start + 360 * i / n)))
            for i in range(n)]


def mesh_vs_hub():
    """Two panels: five VPCs fully peered vs five attachments to a transit gateway."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Peering joins pairs; a transit gateway is a hub</text>',
        '<text class="sub" x="16" y="48">Five VPCs that must all reach each other</text>',
    ]
    pw, top, ph = 318, 64, 300
    for i in range(2):
        px = 16 + i * (pw + 12)
        body.append(f'<rect class="panel" x="{px}" y="{top}" width="{pw}" height="{ph}" rx="8"/>')
        cx, cy = px + pw / 2, top + 150
        pts = ring(cx, cy, 92, 5)
        if i == 0:
            body.append(f'<text class="head" x="{px + 14}" y="{top + 24}">VPC peering: 10 connections</text>')
            for a in range(5):
                for b in range(a + 1, 5):
                    body.append(f'<line class="mesh" x1="{pts[a][0]:.1f}" y1="{pts[a][1]:.1f}" x2="{pts[b][0]:.1f}" y2="{pts[b][1]:.1f}"/>')
            text_lines(body, px + 14, top + 268, ["Every pair needs its own connection:",
                                                  "traffic can't hop through a middle VPC."], cls="small", dy=15)
        else:
            body.append(f'<text class="head" x="{px + 14}" y="{top + 24}">Transit Gateway: 5 attachments</text>')
            for x, y in pts:
                body.append(f'<line class="mesh" x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}"/>')
            body.append(f'<rect class="hub" x="{cx - 44}" y="{cy - 18}" width="88" height="36" rx="6"/>')
            text_lines(body, cx, cy - 2, ["Transit", "gateway"], cls="arrsub", dy=12, anchor="middle")
            text_lines(body, px + 14, top + 268, ["Each network attaches once, to the hub.",
                                                  "The hub's route tables decide who reaches whom."], cls="small", dy=15)
        for k, (x, y) in enumerate(pts):
            body.append(f'<rect class="node" x="{x - 22:.1f}" y="{y - 14:.1f}" width="44" height="28" rx="5"/>')
            body.append(f'<text class="boxt" x="{x:.1f}" y="{y + 5:.1f}" text-anchor="middle">{"ABCDE"[k]}</text>')
    y = top + ph + 26
    rows = [(3, 3, 3), (5, 10, 5), (10, 45, 10), (20, 190, 20)]
    body.append(f'<text class="boxt" x="16" y="{y}">Networks</text>')
    body.append(f'<text class="boxt" x="140" y="{y}">Peering connections for a full mesh</text>')
    body.append(f'<text class="boxt" x="440" y="{y}">Transit Gateway attachments</text>')
    for n, m, h in rows:
        y += 20
        body.append(f'<text class="val" x="16" y="{y}">{n}</text>')
        body.append(f'<text class="val" x="140" y="{y}">{m}</text>')
        body.append(f'<text class="val" x="440" y="{y}">{h}</text>')
    text_lines(body, 16, y + 26, ["A full mesh of n networks needs n × (n − 1) ÷ 2 peering connections (our arithmetic).",
                                  "From AWS\'s VPC peering and Transit Gateway documentation, checked 2026-10-23."], cls="note", dy=15)
    svg("07-04-mesh-vs-hub.svg", w, y + 54,
        "VPC peering mesh compared with a Transit Gateway hub",
        "Two panels, each with five VPCs labeled A to E in a ring. VPC peering: every pair is joined by its own "
        "line, 10 connections in all; every pair needs its own connection, because traffic can't hop through a "
        "middle VPC: peering is not transitive. Transit Gateway: each VPC has one line to a transit gateway in the middle, 5 "
        "attachments in all; each network attaches once, and the gateway's route tables decide who reaches whom. "
        "A table below: for 3 networks, 3 peering connections or 3 attachments; for 5, 10 or 5; for 10, 45 or 10; "
        "for 20, 190 or 20. A full mesh of n networks needs n times n minus 1, divided by 2, connections.",
        body, style=STYLE)


# USD per GB, US East (N. Virginia). See the module docstring for sources.
TRANSFER = [
    ("In from the internet", 0.0, "free"),
    ("Within one Availability Zone", 0.0, "free (private addresses)"),
    ("From S3 to CloudFront", 0.0, "free"),
    ("Across Availability Zones", 0.02, "$0.01 out + $0.01 in"),
    ("To another Region", 0.02, "$0.02 to most; $0.01 to Ohio"),
    ("Out to the internet", 0.09, "$0.09 (first 10 TB a month)"),
    ("Through a NAT gateway", 0.045, "+$0.045 processing, on top"),
]


def transfer_by_direction():
    w = 680
    left, top, pw, rowh = 216, 84, 260, 36
    xmax = 0.10
    body = [
        '<text class="title" x="16" y="28">Data in is free; data across AZs, between Regions or out is not</text>',
        '<text class="sub" x="16" y="48">US dollars per GB moved, from US East (N. Virginia), from AWS\'s price lists (see the note)</text>',
    ]
    for i, (lab, usd, note) in enumerate(TRANSFER):
        y = top + i * rowh
        body.append(f'<text class="lab" x="{left - 12}" y="{y + 18}" text-anchor="end">{lab}</text>')
        if usd == 0:
            body.append(f'<line class="zero" x1="{left}" x2="{left}" y1="{y + 4}" y2="{y + 24}"><title>{lab}: $0.00 per GB</title></line>')
            body.append(f'<text class="val" x="{left + 10}" y="{y + 19}">$0.00 — {note}</text>')
            continue
        bw = pw * usd / xmax
        cls = "other" if lab.startswith("Through") else "s1"
        if lab.startswith("Across"):
            half = bw / 2
            body.append(f'<rect class="s1" x="{left}" y="{y + 4}" width="{half - 1:.1f}" height="20"><title>Sending side: $0.01 per GB</title></rect>')
            body.append(f'<path class="s1l" d="{right_rounded(left + half + 1, y + 4, half - 1, 20)}"><title>Receiving side: $0.01 per GB</title></path>')
        else:
            body.append(f'<path class="{cls}" d="{right_rounded(left, y + 4, bw, 20)}"><title>{lab}: ${usd:.3f} per GB</title></path>')
        body.append(f'<text class="val" x="{left + bw + 8:.1f}" y="{y + 19}">{note}</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top}" y2="{top + len(TRANSFER) * rowh - 8}"/>')
    y = top + len(TRANSFER) * rowh + 14
    y = text_lines(body, 16, y, [
        "Across AZs, each side pays $0.01, so a GB moved costs $0.02 in all. The 100 GB a month free out to the internet",
        "is counted across all Regions. The gray bar is a fee that adds to whatever transfer the traffic also pays.",
    ], cls="small", dy=17)
    y = text_lines(body, 16, y + 4, [
        "Transfer: AWSDataTransfer price list published 2026-09-16, checked 2026-10-23. NAT gateway: EC2 price list,",
        "checked 2026-10-24. Prices change; check the AWS pricing pages or AWS Pricing Calculator for today's rates.",
    ], cls="note", dy=15)
    svg("07-04-transfer-by-direction.svg", w, y + 4,
        "Data transfer prices by direction, from US East (N. Virginia)",
        "Horizontal bar chart of US dollars per GB. In from the internet: $0.00, free. Within one Availability "
        "Zone, using private addresses: $0.00. From S3 to CloudFront: $0.00. Across Availability Zones: $0.02 in "
        "all, as $0.01 charged on the sending side plus $0.01 on the receiving side. To another Region: $0.02 to "
        "most Regions, $0.01 to US East (Ohio). Out to the internet: $0.09 for the first 10 TB a month, after "
        "100 GB a month free across all Regions. Through a NAT gateway, shown gray: $0.045 per GB of processing, "
        "added on top of any transfer charge. Sources: the AWSDataTransfer price list published 2026-09-16, "
        "checked 2026-10-23, and the EC2 price list for the NAT gateway, checked 2026-10-24.", body, style=STYLE)


HOURS = 730  # a typical month
LINKS = [
    ("VPC peering connection", 0.0, "no hourly charge; you pay for data moved"),
    ("Interface endpoint, 1 AZ", 0.01, "+ $0.01 per GB processed"),
    ("Site-to-Site VPN connection", 0.05, "+ data out, tunnel IPv4 addresses"),
    ("Transit Gateway attachment", 0.05, "+ $0.02 per GB processed"),
    ("Client VPN, 1 subnet", 0.10, "+ $0.05 an hour per connected user"),
]


def monthly_link_cost():
    w = 680
    left, top, pw, rowh = 216, 84, 190, 38
    xmax = 80.0
    body = [
        '<text class="title" x="16" y="28">What each link costs a month just for being there</text>',
        '<text class="sub" x="16" y="48">US dollars for a 730-hour month in US East (N. Virginia), before any data moves</text>',
    ]
    for i, (lab, rate, extra) in enumerate(LINKS):
        y = top + i * rowh
        usd = rate * HOURS
        body.append(f'<text class="lab" x="{left - 12}" y="{y + 18}" text-anchor="end">{lab}</text>')
        if usd == 0:
            body.append(f'<line class="zero" x1="{left}" x2="{left}" y1="{y + 4}" y2="{y + 24}"/>')
            body.append(f'<text class="val" x="{left + 10}" y="{y + 19}">$0 — {extra}</text>')
            continue
        bw = pw * usd / xmax
        body.append(f'<path class="s1" d="{right_rounded(left, y + 4, bw, 20)}"><title>{lab}: ${rate:.2f} an hour, about ${usd:.2f} a month</title></path>')
        body.append(f'<text class="val" x="{left + bw + 8:.1f}" y="{y + 19}">${usd:.2f} {extra}</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top}" y2="{top + len(LINKS) * rowh - 8}"/>')
    y = top + len(LINKS) * rowh + 14
    y = text_lines(body, 16, y, [
        "Hourly rate × 730 hours (our arithmetic). Direct Connect isn't shown: it charges per port-hour, set by the",
        "port's speed and type, plus data transfer out; see its pricing page.",
    ], cls="small", dy=17)
    y = text_lines(body, 16, y + 4, [
        "From the AmazonVPC price list published 2026-10-16, as of 2026-10-24. Prices change; check AWS Pricing Calculator.",
    ], cls="note", dy=15)
    svg("07-04-monthly-link-cost.svg", w, y + 4,
        "Monthly cost of connection options before any data moves, US East (N. Virginia)",
        "Horizontal bar chart of US dollars for a 730-hour month, before any data moves. VPC peering connection: $0, "
        "no hourly charge; you pay for data moved. Interface endpoint in one Availability Zone: $7.30, plus $0.01 per "
        "GB processed. Site-to-Site VPN connection: $36.50, plus data transfer out and public IPv4 addresses on its tunnel endpoints. Transit Gateway attachment: "
        "$36.50, plus $0.02 per GB processed. Client VPN with one subnet associated: $73.00, plus $0.05 an hour per "
        "connected user. Direct Connect is not shown; it charges per port-hour by port speed and type, plus data "
        "transfer out. From the AmazonVPC price list published 2026-10-16, as of 2026-10-24.", body, style=STYLE)


if __name__ == "__main__":
    connection_map()
    private_vs_encrypted()
    mesh_vs_hub()
    transfer_by_direction()
    monthly_link_cost()
