#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for Simulation S8 (a packet's journey through the bakery's VPC) as SVG.

Usage: python3 -I source/charts/07-06-charts.py
Writes images/07-06-bakery-network.svg (the simulation's network), images/07-06-checkpoints.svg
(the order of checks for a request and its reply) and images/07-06-trace-grid.svg (the model
answer to Part 1). Facts from the Amazon VPC User Guide, retrieved 2026-10-23: the route table
delivers traffic to the subnet, the network ACL decides whether it enters or leaves the subnet,
and the security group decides whether it reaches the resource ("Network ACLs", "Infrastructure
security in Amazon VPC"); network ACL rules are evaluated from the lowest number and the first
match applies; network ACLs are stateless and security groups stateful ("Security groups",
"Network ACLs"); a subnet without a route to an internet gateway can't reach the internet
("Enable internet access for a VPC using an internet gateway"). The addresses, rules and
packets are made up; 192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24 are ranges reserved
for documentation.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# AWS's Availability Zone = slot 1 (blue) tint; the bakery's own resources = slot 2 (orange)
# tint, as in Modules 03 and 04. Pass/stop is carried by words and a thick outline, never color alone.
STYLE = make_style(
    light_extra=" --az-fill:#d9e8fb; --you-fill:#fbe1d6; --card:#fcfcfb; --no-fill:#f1f0ec;",
    dark_extra=" --az-fill:#1b3554; --you-fill:#4d2716; --card:#1a1a19; --no-fill:#252523;",
    rules_extra="""
  .vpc { fill: none; stroke: var(--ink); stroke-width: 2; }
  .net { fill: none; stroke: var(--ink2); stroke-width: 1.5; stroke-dasharray: 6 4; }
  .az { fill: var(--az-fill); stroke: var(--s1); stroke-width: 1.2; }
  .you { fill: var(--you-fill); stroke: var(--s2); stroke-width: 1.5; }
  .card { fill: var(--card); stroke: var(--ink2); stroke-width: 1; }
  .gw { fill: var(--card); stroke: var(--ink); stroke-width: 2; }
  .ok { fill: var(--card); stroke: var(--ink2); stroke-width: 1; }
  .stop { fill: var(--you-fill); stroke: var(--ink); stroke-width: 3; }
  .auto { fill: var(--no-fill); stroke: var(--muted); stroke-width: 1; stroke-dasharray: 4 3; }
  .hl { fill: var(--card); stroke: var(--ink); stroke-width: 3; }
  .link { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .flow { stroke: var(--ink); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink); }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .bold { fill: var(--ink); font-size: 12px; font-weight: 700; }
  .small { fill: var(--ink2); font-size: 12px; }
  .tiny { fill: var(--ink2); font-size: 11px; }
  .chip { fill: var(--ink); font-size: 11.5px; }
  .chipb { fill: var(--ink); font-size: 11.5px; font-weight: 700; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

DEFS = ('<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        'orient="auto-start-reverse"><path class="arrowhead" d="M0,0 L10,5 L0,10 Z"/></marker></defs>')


def network():
    """The simulation's network: the internet, the gateway, and AZ a's two subnets."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">The bakery\'s network in this simulation</text>',
        '<text class="sub" x="16" y="48">US East (N. Virginia). Only AZ a is drawn; AZ b holds a matching pair of subnets.</text>',
    ]
    # the internet
    body.append('<rect class="net" x="16" y="72" width="150" height="388" rx="10"/>')
    body.append('<text class="boxt" x="91" y="94" text-anchor="middle">The internet</text>')
    outside = [(118, ["Customer", "192.0.2.44"]), (198, ["Bad range", "203.0.113.0/24"]),
               (278, ["Update site", "192.0.2.200"])]
    for y, lines in outside:
        body.append(f'<rect class="card" x="28" y="{y}" width="126" height="48" rx="6"/>')
        body.append(f'<text class="bold" x="91" y="{y + 20}" text-anchor="middle">{lines[0]}</text>')
        body.append(f'<text class="small" x="91" y="{y + 37}" text-anchor="middle">{lines[1]}</text>')
        body.append(f'<line class="link" x1="154" y1="{y + 24}" x2="180" y2="{y + 24}"/>')
    body.append('<line class="link" x1="180" y1="142" x2="180" y2="302"/>')
    # VPC, gateway, AZ
    body.append('<rect class="vpc" x="214" y="72" width="450" height="388" rx="8"/>')
    body.append('<text class="boxt" x="650" y="94" text-anchor="end">VPC 10.0.0.0/16</text>')
    body.append('<line class="link" x1="180" y1="222" x2="190" y2="222"/>')
    body.append('<rect class="gw" x="190" y="196" width="74" height="52" rx="5"/>')
    text_lines(body, 227, 218, ["Internet", "gateway"], cls="bold", dy=15, anchor="middle")
    body.append('<rect class="az" x="276" y="104" width="376" height="344" rx="7"/>')
    body.append('<text class="small" x="288" y="122">Availability Zone a</text>')
    subnets = [
        (132, "Public subnet 10.0.1.0/24", "Network ACL: public-nacl",
         "Route table: 10.0.0.0/16 → local; 0.0.0.0/0 → internet gateway",
         ["Web server", "10.0.1.10", "public IP 198.51.100.20", "security group web-sg"]),
        (296, "Private subnet 10.0.3.0/24", "Network ACL: private-nacl",
         "Route table: 10.0.0.0/16 → local, nothing else",
         ["Order database", "10.0.3.20, port 5432", "", "security group db-sg"]),
    ]
    for y, title, nacl, rt, server in subnets:
        body.append(f'<rect class="you" x="288" y="{y}" width="352" height="140" rx="6"/>')
        body.append(f'<text class="boxt" x="300" y="{y + 22}">{title}</text>')
        body.append(f'<text class="small" x="300" y="{y + 44}">{nacl}</text>')
        text_lines(body, 300, y + 64, wrap(rt, 26), cls="tiny", dy=14)
        sx, sy = 486, y + 34
        body.append(f'<rect class="card" x="{sx}" y="{sy}" width="142" height="92" rx="6"/>')
        body.append(f'<text class="bold" x="{sx + 10}" y="{sy + 20}">{server[0]}</text>')
        lines = [t for t in server[1:] if t]
        text_lines(body, sx + 10, sy + 38, lines, cls="tiny", dy=15)
    body.append('<line class="link" x1="264" y1="222" x2="288" y2="222"/>')
    text_lines(body, 16, 486, wrap("Lines show what connects to what. The addresses are made up, from ranges "
                                    "reserved for examples. A real shop would also have a load balancer; the "
                                    "simulation leaves it out to keep the path short.", 104), cls="note", dy=16)
    svg("07-06-bakery-network.svg", w, 530,
        "The bakery's network for Simulation S8: an internet gateway, a public subnet with the web server and a private subnet with the order database",
        "On the left, the internet holds three made-up addresses: a customer at 192.0.2.44, a bad range "
        "203.0.113.0/24, and an update site at 192.0.2.200. All connect to the internet gateway on the edge of "
        "the VPC, 10.0.0.0/16, in US East (N. Virginia). Inside, Availability Zone a holds two subnets; AZ b "
        "holds a matching pair that isn't drawn. The public subnet, 10.0.1.0/24, uses network ACL public-nacl "
        "and a route table with 10.0.0.0/16 to local and 0.0.0.0/0 to the internet gateway; it holds the web "
        "server, private address 10.0.1.10, public IP 198.51.100.20, security group web-sg. The private subnet, "
        "10.0.3.0/24, uses network ACL private-nacl and a route table with only the local route; it holds the "
        "order database at 10.0.3.20, port 5432, security group db-sg. The internet gateway connects to the "
        "public subnet. A note says a real shop would also have a load balancer, left out here.",
        body, style=STYLE)


def checkpoints():
    """The order of checks for a request from the internet, and for its reply."""
    w = 680
    body = [
        DEFS,
        '<text class="title" x="16" y="28">The checks a request and its reply pass through</text>',
        '<text class="sub" x="16" y="48">A customer\'s request to the web server, and the server\'s reply</text>',
    ]
    lanes = [
        (82, "Request in", [
            ("Internet gateway", "public IP → private IP", "ok"),
            ("Route table", "local route delivers it", "ok"),
            ("Network ACL, inbound", "numbered rules, first match", "ok"),
            ("Security group, inbound", "allow rules only", "ok"),
            ("Web server", "", "card"),
        ]),
        (210, "Reply out", [
            ("Web server", "", "card"),
            ("Security group", "reply allowed: it remembers", "auto"),
            ("Network ACL, outbound", "checked again: it forgets", "hl"),
            ("Route table", "0.0.0.0/0 → gateway", "ok"),
            ("Internet gateway", "private IP → public IP", "ok"),
        ]),
    ]
    bw, gap, x0 = 116, 17, 16
    for y, name, steps in lanes:
        body.append(f'<text class="head" x="16" y="{y}">{name}</text>')
        by = y + 14
        for i, (t, sub, cls) in enumerate(steps):
            x = x0 + i * (bw + gap)
            body.append(f'<rect class="{cls if cls != "card" else "you"}" x="{x}" y="{by}" width="{bw}" height="74" rx="6"/>')
            yy = text_lines(body, x + bw / 2, by + 22, wrap(t, 16), cls="bold", dy=14, anchor="middle")
            if sub:
                text_lines(body, x + bw / 2, yy + 2, wrap(sub, 19), cls="tiny", dy=13, anchor="middle")
            if i < len(steps) - 1:
                body.append(f'<line class="flow" x1="{x + bw + 2}" y1="{by + 37}" x2="{x + bw + gap - 2}" y2="{by + 37}" marker-end="url(#arr)"/>')
    body.append('<text class="bold" x="282" y="318">↑ The check people forget: it needs a rule for the reply.</text>')
    ny = text_lines(body, 16, 346, wrap("Dashed: passes without a rule, because a security group is stateful. Thick "
                                         "outline: a stateless network ACL checks the reply like any other packet. "
                                         "Traffic between two subnets passes the sender's security group and network "
                                         "ACL going out, then the receiver's network ACL and security group coming in.",
                                         104), cls="note", dy=16)
    svg("07-06-checkpoints.svg", w, ny + 4,
        "The order of checks for a request from the internet to a web server, and for the server's reply",
        "Two rows of boxes joined by arrows. Request in: the internet gateway translates the public IP to the "
        "private IP; the route table's local route delivers the packet to the subnet; the network ACL checks "
        "its inbound rules, numbered, first match wins; the security group checks its inbound rules, which can "
        "only allow; the packet reaches the web server. Reply out: from the web server, the security group "
        "lets the reply out without a rule because it remembers the request (drawn dashed); the network ACL "
        "checks its outbound rules again, because it forgets (drawn with a thick outline and labeled as the "
        "check people forget); the route table sends 0.0.0.0/0 to the gateway; the internet gateway translates "
        "the private IP back to the public IP. A note says traffic between two subnets passes the sender's "
        "security group and network ACL going out, then the receiver's network ACL and security group coming in.",
        body, style=STYLE)


PACKETS = [  # (name, result, [(text, state)]); state: ok | auto | stop
    ("A. Customer → shop, port 443", "Reply reaches the customer", [
        ("Gateway", "ok"), ("NACL in: rule 100 allows", "ok"), ("web-sg in: 443 allowed", "ok"),
        ("Reply: web-sg remembers", "auto"), ("NACL out: rule 100 allows", "ok"), ("Route 0.0.0.0/0 → gateway", "ok")]),
    ("B. Bad range → shop, port 443", "Blocked at the network ACL", [
        ("Gateway", "ok"), ("NACL in: rule 90 denies", "stop")]),
    ("C. Web server → database, port 5432", "Reply reaches the web server", [
        ("web-sg out: all allowed", "ok"), ("public-nacl out: rule 100", "ok"), ("Local route", "ok"),
        ("private-nacl in: rule 100", "ok"), ("db-sg in: from web-sg", "ok"),
        ("Reply: db-sg remembers", "auto"), ("private-nacl out: rule 100", "ok"), ("public-nacl in: rule 110", "ok")]),
    ("D. Database → update site, port 443", "Blocked leaving the subnet", [
        ("db-sg out: all allowed", "ok"), ("private-nacl out: * denies", "stop")]),
    ("E. Test server 10.0.1.50 → database, port 5432", "Blocked at the security group", [
        ("test-sg out: all allowed", "ok"), ("public-nacl out: rule 100", "ok"), ("Local route", "ok"),
        ("private-nacl in: rule 100", "ok"), ("db-sg in: not web-sg", "stop")]),
]


def trace_grid():
    """Model answer to Part 1: each packet's checkpoints, and where it stops."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Where each packet goes, and where it stops</text>',
        '<text class="sub" x="16" y="48">Model answer to Part 1, read left to right</text>',
    ]
    y = 78
    ch, gap = 26, 6
    for name, result, steps in PACKETS:
        body.append(f'<text class="bold" x="16" y="{y}">{name}</text>')
        body.append(f'<text class="small" x="664" y="{y}" text-anchor="end">{result}</text>')
        x, yy = 16, y + 10
        for text, state in steps:
            mark = {"ok": "✓ ", "auto": "✓ ", "stop": "✗ "}[state]
            label = mark + text + (" (stops here)" if state == "stop" else "")
            cw = len(label) * 6.1 + 18
            if x + cw > w - 16:
                x, yy = 16, yy + ch + gap
            body.append(f'<rect class="{state}" x="{x:.1f}" y="{yy}" width="{cw:.1f}" height="{ch}" rx="5"/>')
            cls = "chipb" if state == "stop" else "chip"
            body.append(f'<text class="{cls}" x="{x + 9:.1f}" y="{yy + 17}">{label}</text>')
            x += cw + gap
        y = yy + ch + 30
    ny = text_lines(body, 16, y - 6, wrap("✓ passes; dashed: a security group lets a reply through without a rule; "
                                          "thick outline and ✗: the rule that stops the packet. Packet D would also "
                                          "find no route to the internet in the private subnet's route table.", 104),
                    cls="note", dy=16)
    svg("07-06-trace-grid.svg", w, ny + 2,
        "Model answer: the checkpoints each of five packets passes, and where it stops",
        "Five rows, one per packet. A, a customer to the shop on port 443: the gateway; the network ACL's "
        "inbound rule 100 allows it; web-sg allows 443; the reply passes web-sg because it remembers the "
        "request; the network ACL's outbound rule 100 allows it; the route 0.0.0.0/0 sends it to the gateway; "
        "it reaches the customer. B, the bad range to the shop on port 443: the gateway, then network ACL "
        "inbound rule 90 denies it, so it stops there. C, the web server to the database on port 5432: web-sg "
        "outbound allows all; public-nacl outbound rule 100 allows it, because 5432 is inside its port range; the local route; private-nacl inbound "
        "rule 100 allows it; db-sg allows it from web-sg; the reply passes db-sg because it remembers; "
        "private-nacl outbound rule 100 and public-nacl inbound rule 110 allow the reply; it reaches the web "
        "server. D, the database to an update site on port 443: db-sg outbound allows all, then private-nacl "
        "outbound denies it with the catch-all rule, and the private route table has no route to the internet "
        "either. E, a test server at 10.0.1.50 to the database on port 5432: its security group allows all "
        "outbound; public-nacl outbound rule 100, the local route and private-nacl inbound rule 100 all allow "
        "it, because it comes from inside the VPC; db-sg stops it, because the test server doesn't carry web-sg.", body, style=STYLE)


if __name__ == "__main__":
    network()
    checkpoints()
    trace_grid()
