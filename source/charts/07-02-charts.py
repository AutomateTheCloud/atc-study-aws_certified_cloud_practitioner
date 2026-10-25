#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 07.02 (filtering traffic) as SVG.

Usage: python3 -I source/charts/07-02-charts.py
Writes images/07-02-*.svg. Facts come from the Amazon VPC User Guide (security
groups, security group rules, network ACLs, "Infrastructure security in Amazon
VPC" with its comparison of the two) and the Amazon VPC FAQ, checked 2026-10-23:
traffic from an internet gateway is routed to the subnet, the subnet's network
ACL decides what enters the subnet, then the security group decides what reaches
the instance; security groups are stateful, allow-only, and evaluate all rules;
network ACLs are stateless, allow and deny, and evaluate numbered rules in
ascending order until the first match; the default network ACL allows all
traffic; a new security group has no inbound rules and allows all outbound
traffic; replies go to a high-numbered port on the client (the FAQ's example is
49152-65535). The catch-all "*" rule and the deny-all start of a custom network
ACL are from the Network ACL rules pages of the same guide. Addresses come from
the ranges reserved for documentation. The bakery is made up for teaching. Our
own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Allowed = slot 1 (blue) tint, denied = slot 2 (orange) tint; neutral otherwise.
# Every cell also says "allowed" or "denied" in words.
STYLE = make_style(
    light_extra=" --ok-fill:#d9e8fb; --no-fill:#fbe1d6; --n-fill:#f1f0ec;",
    dark_extra=" --ok-fill:#1b3554; --no-fill:#4d2716; --n-fill:#252523;",
    rules_extra="""
  .ok { fill: var(--ok-fill); stroke: var(--s1); stroke-width: 1.5; }
  .no { fill: var(--no-fill); stroke: var(--s2); stroke-width: 1.5; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .skip { fill: none; stroke: var(--axis); stroke-width: 1; stroke-dasharray: 3 3; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .vpc { fill: none; stroke: var(--ink); stroke-width: 1.8; }
  .subnet { fill: none; stroke: var(--ink2); stroke-width: 1.2; }
  .nacl { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .sg { fill: none; stroke: var(--s1); stroke-width: 2; stroke-dasharray: 7 4; }
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
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .num { fill: var(--ink); font-size: 13px; font-weight: 700; }
  .numc { fill: var(--surface); stroke: var(--ink); stroke-width: 1.5; }
  .numh { fill: var(--s1); stroke: var(--s1); stroke-width: 1.5; }
  .numhl { fill: var(--surface); font-size: 13px; font-weight: 700; }""")


def arrow(body, x1, y1, x2, y2):
    """A straight line with a small filled head at (x2, y2), any direction."""
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


def marker(body, x, y, n, hi=False):
    body.append(f'<circle class="{"numh" if hi else "numc"}" cx="{x}" cy="{y}" r="11"/>')
    body.append(f'<text class="{"numhl" if hi else "num"}" x="{x}" y="{y + 4.5}" text-anchor="middle">{n}</text>')


def packet_path():
    """Big picture: a request and its reply through the network ACL and the security group."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Two checkpoints in, two checkpoints out</text>',
        '<text class="sub" x="16" y="48">A customer\'s request to the bakery\'s web server, and the reply, in four numbered checks</text>',
    ]
    # The customer.
    rect(body, "plain", 16, 128, 84, 88)
    text_lines(body, 58, 160, ["Customer", "on the", "internet"], cls="cellt", dy=16, anchor="middle")
    # VPC, gateway, subnet, network ACL band, security group, server.
    rect(body, "vpc", 112, 72, 552, 236, 8)
    body.append('<text class="head" x="122" y="90">The bakery\'s VPC</text>')
    rect(body, "plain", 124, 128, 80, 88)
    text_lines(body, 164, 160, ["Internet", "gateway"], cls="cellt", dy=16, anchor="middle")
    sx, sy, sw, sh = 232, 100, 420, 196
    rect(body, "subnet", sx, sy, sw, sh)
    body.append(f'<text class="head" x="{sx + 72}" y="{sy + 18}">Public subnet</text>')
    rect(body, "nacl", sx, sy, 60, sh, 6)
    body.append(f'<text class="cellt" transform="translate({sx + 47},{sy + sh / 2}) rotate(-90)" text-anchor="middle">Network ACL</text>')
    gx, gy, gw, gh = 440, 118, 200, 164
    rect(body, "sg", gx, gy, gw, gh, 10)
    body.append(f'<text class="head" x="{gx + 12}" y="{gy + 20}">Security group</text>')
    rect(body, "plain", 490, 162, 130, 72)
    text_lines(body, 555, 194, ["Web server"], cls="cellt", anchor="middle")
    body.append('<text class="small" x="555" y="212" text-anchor="middle">port 443 (HTTPS)</text>')
    # Request, left to right.
    ry = 150
    arrow(body, 101, ry, 123, ry)
    arrow(body, 205, ry, 489, ry)
    body.append(f'<text class="arrlab" x="{sx + 76}" y="{ry - 8}">request</text>')
    marker(body, sx + 18, ry, 1)
    marker(body, gx, ry, 2)
    # Reply, right to left.
    py = 252
    arrow(body, 489, py, 205, py)
    arrow(body, 123, py, 101, py)
    body.append(f'<text class="arrlab" x="{sx + 76}" y="{py + 20}">reply, to the customer\'s</text>')
    body.append(f'<text class="arrlab" x="{sx + 76}" y="{py + 34}">high-numbered port</text>')
    marker(body, gx, py, 3)
    marker(body, sx + 18, py, 4, hi=True)
    # The four checks.
    y = 334
    steps = [
        (1, "Network ACL, inbound rules:", "checked in number order; one must allow HTTPS (TCP port 443) from the customer.", False),
        (2, "Security group, inbound rules:", "one must allow HTTPS; any matching allow rule lets it in.", False),
        (3, "Security group, the reply:", "allowed automatically, because it remembers the request (stateful).", False),
        (4, "Network ACL, outbound rules:", "checked again, as if new; one must allow traffic to the customer's high-numbered port (stateless).", True),
    ]
    for n, head, text, hi in steps:
        marker(body, 28, y - 4, n, hi)
        body.append(f'<text class="rowl" x="48" y="{y}">{head}</text>')
        lines = wrap(text, 62)
        y = text_lines(body, 250, y, lines, cls="small", dy=16) + 8
    y += 6
    body.append(f'<text class="note" x="16" y="{y}">The route table delivers traffic between the gateway and the subnet. From the Amazon VPC User Guide and FAQ, checked</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">2026-10-23. The bakery is made up for teaching.</text>')
    svg("07-02-packet-path.svg", w, y + 30,
        "A request and its reply passing a network ACL and a security group",
        "Left to right: a customer on the internet; the bakery's VPC, holding an internet gateway and a public "
        "subnet. The subnet's left edge is a band labeled network ACL. Inside the subnet, a dashed ring labeled "
        "security group surrounds the web server, which listens on port 443 for HTTPS. A request arrow runs from "
        "the customer through the internet gateway, across the network ACL (check 1) and the security group ring "
        "(check 2) to the server. A reply arrow runs back from the server across the security group (check 3) and "
        "the network ACL (check 4, highlighted) to the gateway and the customer, to the customer's high-numbered "
        "port. The checks: 1, network ACL inbound rules, checked in number order, one must allow HTTPS (TCP port "
        "443) from the customer; 2, security group inbound rules, one must allow HTTPS, and any matching allow rule "
        "lets it in; 3, security group, the reply is allowed automatically because it remembers the request "
        "(stateful); 4, network ACL outbound rules, checked again as if new, one must allow traffic to the "
        "customer's high-numbered port (stateless).", body, style=STYLE)


ROWS = ["Guards", "Rules", "How rules are checked", "Replies", "When you create one", "Its usual job", "Cost"]
COLS = [
    ("Security group",
     ["Each resource it's attached to, such as one web server (instance level)",
      "Allow rules only",
      "All rules together: any allow rule that matches lets traffic through",
      "Allowed automatically: it remembers the request (stateful)",
      "A new group allows nothing in and everything out",
      "The main control: who may reach this resource, on which port",
      "No charge"]),
    ("Network ACL",
     ["A whole subnet: everything that enters or leaves it (subnet level)",
      "Allow and deny rules",
      "In number order: the first rule that matches decides",
      "Checked again: an outbound rule must allow it (stateless)",
      "The default one allows everything; a new custom one denies everything",
      "A second layer: for example, deny an address range for a whole subnet",
      "No charge"]),
]


def sg_vs_nacl():
    """Comparison panels: security group vs network ACL, with the replies row highlighted."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Security group or network ACL: same job, different rules</text>',
        '<text class="sub" x="16" y="48">Both filter traffic in your VPC; read across a row to see how they differ</text>',
    ]
    lw = 150
    cw, gap = 250, 8
    xs = [16 + lw + i * (cw + gap) for i in range(2)]
    y = 66
    for x, (name, _) in zip(xs, COLS):
        rect(body, "n", x, y, cw, 32)
        body.append(f'<text class="cellt" x="{x + 10}" y="{y + 21}">{name}</text>')
    y += 40
    for r, row in enumerate(ROWS):
        cells = [wrap(c[1][r], 34) for c in COLS]
        h = 14 + 15 * max(len(c) for c in cells) + 4
        hi = row == "Replies"
        if hi:
            for x in xs:
                rect(body, "ok", x - 4, y + 2, cw + 8, h - 4, 5)
        body.append(f'<line class="grid" x1="16" x2="{xs[1] + cw}" y1="{y}" y2="{y}"/>')
        text_lines(body, 16, y + 19, wrap(row, 20), cls="rowl", dy=15)
        for x, c in zip(xs, cells):
            text_lines(body, x + 10, y + 19, c, cls="cellt" if hi else "small", dy=15)
        y += h
    body.append(f'<line class="grid" x1="16" x2="{xs[1] + cw}" y1="{y}" y2="{y}"/>')
    y += 22
    body.append(f'<text class="note" x="16" y="{y}">Neither filters traffic to Amazon DNS, DHCP, instance metadata or the Amazon Time Sync Service.</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">From the Amazon VPC User Guide (security groups; network ACLs; infrastructure security), checked 2026-10-23.</text>')
    svg("07-02-sg-vs-nacl.svg", w, y + 30,
        "Security group compared with network ACL",
        "Two columns, security group and network ACL, compared on seven rows. Guards: a security group guards each "
        "resource it's attached to, such as one web server (instance level); a network ACL guards a whole subnet, "
        "everything that enters or leaves it (subnet level). Rules: allow rules only; allow and deny rules. How "
        "rules are checked: all rules together, and any allow rule that matches lets traffic through; in number "
        "order, and the first rule that matches decides. Replies, highlighted: allowed automatically because the "
        "security group remembers the request (stateful); checked again, so an outbound rule must allow them "
        "(stateless). When you create one: a new security group allows nothing in and everything out; the default "
        "network ACL allows everything, and a new custom one denies everything. Usual job: the main control, who "
        "may reach this resource on which port; a second layer, for example denying an address range for a whole "
        "subnet. Cost: no charge for either. A note says neither filters traffic to Amazon DNS, DHCP, instance "
        "metadata or the Amazon Time Sync Service.", body, style=STYLE)


if __name__ == "__main__":
    packet_path()
    sg_vs_nacl()
