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
AWS PrivateLink? (one service, through an interface endpoint). The bakery's setup
is made up for teaching. Our own design: no AWS logos, icons, trade dress or AWS
diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines  # noqa: E402

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


if __name__ == "__main__":
    connection_map()
    private_vs_encrypted()
