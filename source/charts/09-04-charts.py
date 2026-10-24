#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 09.04 (the front door) as SVG.

Usage: python3 -I source/charts/09-04-charts.py
Writes images/09-04-*.svg. Facts come from AWS pages cited in
guide/09-protecting-and-governing/04-the-front-door.md, read 2026-10-24:
- AWS Shield Standard overview (automatic for all customers at no additional
  charge; common network and transport layer DDoS attacks; particular benefit
  for Route 53 hosted zones, CloudFront distributions and Global Accelerator
  standard accelerators);
- AWS Shield Advanced overview and the Shield FAQ (protected resource types: EC2
  Elastic IP addresses, Elastic Load Balancing, CloudFront, Route 53 hosted zones,
  Global Accelerator; you add protection per resource; automatic application
  layer mitigation through an AWS WAF rule group; standard WAF fees for protected
  resources covered; DDoS cost protection as credits through AWS Support);
- Managed DDoS event response with Shield Response Team (SRT) support (the SRT
  needs Shield Advanced plus the Business Support or Enterprise Support plan, as
  the page words it on 2026-10-24);
- AWS WAF developer guide (web requests to CloudFront, API Gateway REST APIs,
  Application Load Balancers and other resources; rules on addresses, countries,
  request content; rate-based rules; managed rule groups);
- AWS Firewall Manager prerequisites (AWS Organizations, an administrator
  account, AWS Config) and the Firewall Manager pricing page.

Prices, USD, from the pricing pages read 2026-10-24:
- AWS Shield pricing: Shield Standard no additional charge; Shield Advanced
  $3,000 a month, 1-year subscription, billed once per payer account, plus data
  transfer usage fees.
- AWS WAF pricing: $5.00 per web ACL a month, $1.00 per rule or rule group a
  month, $0.60 per million requests.
- AWS Firewall Manager pricing: $100 per policy per Region a month (some Regions
  more), its WAF and Shield Advanced policies are included for Shield Advanced
  subscribers; underlying services billed.
The bakery's WAF setup (one web ACL, four rules or rule groups, 2 million requests
a month) is made up for teaching; the monthly total is our arithmetic. Our own
design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --hi-fill:#d9e8fb; --n-fill:#f1f0ec; --alt-fill:#fbe1d6; --zone:#f6f5f1;",
    dark_extra=" --hi-fill:#1b3554; --n-fill:#252523; --alt-fill:#4d2716; --zone:#20201f;",
    rules_extra="""
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 2; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .alt { fill: var(--alt-fill); stroke: var(--s2); stroke-width: 1.5; }
  .none { fill: none; stroke: var(--axis); stroke-width: 1; stroke-dasharray: 3 3; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .zone { fill: var(--zone); stroke: var(--axis); stroke-width: 1.2; stroke-dasharray: 6 4; }
  .vpc { fill: none; stroke: var(--ink2); stroke-width: 1.5; }
  .sg { fill: none; stroke: var(--s1); stroke-width: 2; stroke-dasharray: 7 4; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .cellb { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .zlab { fill: var(--muted); font-size: 12px; font-weight: 600; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .val { fill: var(--ink); font-size: 13px; font-variant-numeric: tabular-nums; }
  .num { fill: var(--ink); font-size: 12px; font-weight: 700; }
  .numc { fill: var(--surface); stroke: var(--ink); stroke-width: 1.5; }
  .zero { stroke: var(--s1); stroke-width: 2; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowd { stroke: var(--ink2); stroke-width: 1.5; fill: none; stroke-dasharray: 5 4; }
  .arrowhead { fill: var(--ink2); }""")

CH = 6.3  # rough width of one 12px character, for wrapping


def arrow(body, x1, y1, x2, y2, cls="arrow"):
    body.append(f'<line class="{cls}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


def marker(body, x, y, n):
    body.append(f'<circle class="numc" cx="{x}" cy="{y}" r="10"/>')
    body.append(f'<text class="num" x="{x}" y="{y + 4}" text-anchor="middle">{n}</text>')


def box(body, cls, x, y, w, h, title, lines=(), anchor="middle"):
    rect(body, cls, x, y, w, h)
    tx = x + w / 2 if anchor == "middle" else x + 8
    body.append(f'<text class="boxt" x="{tx}" y="{y + 18}" text-anchor="{anchor}">{title}</text>')
    text_lines(body, tx, y + 34, list(lines), cls="cells", dy=14, anchor=anchor)


def bullets_height(w, items):
    n = sum(len(wrap(t, int((w - 34) / CH))) for t in items)
    return 30 + 15 * n + 5 * len(items) + 8


def bullets_card(body, cls, x, y, w, h, title, items):
    rect(body, cls, x, y, w, h)
    body.append(f'<text class="boxt" x="{x + 10}" y="{y + 20}">{title}</text>')
    ty = y + 38
    for t in items:
        for j, part in enumerate(wrap(t, int((w - 34) / CH))):
            if j == 0:
                body.append(f'<text class="cells" x="{x + 10}" y="{ty:.1f}">• {part}</text>')
            else:
                body.append(f'<text class="cells" x="{x + 21}" y="{ty:.1f}">{part}</text>')
            ty += 15
        ty += 5


def front_door():
    """Big picture: the layers between the internet and the bakery's web servers."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">The bakery\'s front door, layer by layer</text>',
        '<text class="sub" x="16" y="48">Each numbered layer stops a different kind of bad traffic before it reaches the web servers</text>',
    ]
    # Firewall Manager band across the top.
    top = 66
    rect(body, "n", 16, top, w - 32, 40)
    marker(body, 34, top + 20, 4)
    body.append(f'<text class="boxt" x="52" y="{top + 17}">AWS Firewall Manager</text>')
    body.append(f'<text class="cells" x="52" y="{top + 33}">Applies the same WAF, Shield Advanced and security group policies to all accounts in an organization</text>')
    # Internet.
    y0 = top + 64
    box(body, "plain", 16, y0 + 70, 92, 84, "Internet", ["customers,", "bots and", "attackers"])
    # Edge zone.
    ex, ew = 124, 196
    rect(body, "zone", ex, y0, ew, 250, 8)
    body.append(f'<text class="zlab" x="{ex + 10}" y="{y0 + 18}">AWS EDGE LOCATIONS</text>')
    box(body, "plain", ex + 14, y0 + 30, ew - 28, 50, "Route 53", ["answers DNS lookups"])
    box(body, "plain", ex + 14, y0 + 96, ew - 28, 50, "CloudFront", ["serves pages and photos"])
    rect(body, "hi", ex + 14, y0 + 154, ew - 28, 38)
    marker(body, ex + 30, y0 + 173, 2)
    body.append(f'<text class="boxt" x="{ex + 46}" y="{y0 + 170}">AWS WAF web ACL</text>')
    body.append(f'<text class="cells" x="{ex + 46}" y="{y0 + 185}">checks each web request</text>')
    # Region zone.
    rx, rw = 336, w - 16 - 336
    rect(body, "zone", rx, y0, rw, 250, 8)
    body.append(f'<text class="zlab" x="{rx + 10}" y="{y0 + 18}">US EAST (N. VIRGINIA): THE BAKERY\'S VPC</text>')
    box(body, "plain", rx + 14, y0 + 94, 140, 54, "Load balancer", ["Application Load", "Balancer"])
    rect(body, "hi", rx + 14, y0 + 156, 140, 38)
    marker(body, rx + 30, y0 + 175, 2)
    body.append(f'<text class="boxt" x="{rx + 46}" y="{y0 + 172}">WAF web ACL</text>')
    body.append(f'<text class="cells" x="{rx + 46}" y="{y0 + 187}">if not via CloudFront</text>')
    # Security group ring around web servers.
    sx, sy, sw, sh = rx + 170, y0 + 30, rw - 184, 162
    rect(body, "sg", sx, sy, sw, sh, 10)
    marker(body, sx + 16, sy + 16, 3)
    body.append(f'<text class="cellb" x="{sx + 30}" y="{sy + 20}">Network ACL and</text>')
    body.append(f'<text class="cellb" x="{sx + 30}" y="{sy + 35}">security group</text>')
    box(body, "plain", sx + 14, sy + 54, sw - 28, 92, "Web servers", ["EC2 instances in", "an Auto Scaling", "group, two AZs"])
    # Flows.
    arrow(body, 109, y0 + 112, ex + 13, y0 + 55)
    arrow(body, 109, y0 + 112, ex + 13, y0 + 121)
    body.append(f'<text class="cells" x="{ex + 40}" y="{y0 + 92}">address</text>')
    arrow(body, ex + ew - 14, y0 + 121, rx + 13, y0 + 121)
    arrow(body, rx + 155, y0 + 121, sx + 13, y0 + 121)
    # Shield Standard band underneath, spanning edge and Region.
    by = y0 + 202
    rect(body, "n", ex + 8, by, w - 16 - ex - 8 - 8, 40)
    marker(body, ex + 26, by + 20, 1)
    body.append(f'<text class="boxt" x="{ex + 42}" y="{by + 17}">AWS Shield Standard: on for everyone, no charge</text>')
    body.append(f'<text class="cells" x="{ex + 42}" y="{by + 33}">absorbs common network floods at the edge and in the Region</text>')
    y = y0 + 250 + 24
    steps = [
        (1, "Shield:", "network and transport floods, such as SYN floods and UDP reflection."),
        (2, "WAF:", "bad web requests: SQL injection, cross-site scripting, request floods, blocked addresses or countries."),
        (3, "Network ACL and security group:", "only the ports and addresses you allow (Module 07)."),
        (4, "Firewall Manager:", "the same protections in every account, including new ones."),
    ]
    for n, head, text in steps:
        marker(body, 28, y - 4, n)
        body.append(f'<text class="cellb" x="46" y="{y}">{head}</text>')
        lines = wrap(text, 70)
        y = text_lines(body, 250, y, lines, cls="cells", dy=15) + 6
    y += 6
    y = text_lines(body, 16, y, [
        "From the AWS WAF, AWS Shield and AWS Firewall Manager developer guides, checked 2026-10-24. The bakery is made",
        "up for teaching.",
    ], cls="note", dy=15)
    svg("09-04-front-door.svg", w, y + 4,
        "The layers of protection between the internet and the bakery's web servers",
        "Left: the internet, with customers, bots and attackers. Middle: a zone labeled AWS edge locations, holding "
        "Route 53, which answers DNS for bakery.example, and CloudFront, which serves pages and photos, with an "
        "AWS WAF web ACL attached that checks each web request (layer 2, highlighted). Right: a zone labeled US "
        "East (N. Virginia), the bakery's VPC, holding an Application Load Balancer, with a second WAF web ACL "
        "marked for use if traffic doesn't come through CloudFront (layer 2, highlighted), and a dashed ring for "
        "the network ACL and security group (layer 3) around the web servers, EC2 instances in an Auto Scaling "
        "group across two Availability Zones. Arrows: from the internet to Route 53 for the address and to "
        "CloudFront; from CloudFront to the load balancer; from the load balancer to the web servers. A band underneath the edge and Region zones: layer 1, AWS Shield Standard, on for everyone at no "
        "charge, absorbing common network floods at the edge and in the Region. A band "
        "across the top: layer 4, AWS Firewall Manager, applying the same WAF rules, Shield Advanced and security "
        "group policies to every account in an organization. Key: 1, Shield, network and transport floods such as "
        "SYN floods and UDP reflection; 2, WAF, bad web requests such as SQL injection, cross-site scripting, "
        "request floods and blocked addresses or countries; 3, network ACL and security group, only the ports and "
        "addresses you allow; 4, Firewall Manager, the same protections in every account, including new ones.",
        body, style=STYLE)


COLS = ["Shield Standard", "Shield Advanced", "AWS WAF", "Network ACL or security group", "Firewall Manager"]
# (need, [cell per column]); a cell is (kind, text) with kind main | helps | none.
ROWS = [
    ("Flood of network traffic (SYN flood, UDP reflection)",
     [("main", "Main: automatic"), ("helps", "Adds detection, experts, bill protection"), ("none", "No: not web requests"), ("none", "No: not built for floods"), ("none", "No")]),
    ("Flood of web requests from many addresses",
     [("none", "No: not this layer"), ("helps", "Adds automatic mitigation through WAF"), ("main", "Main: rate-based rule"), ("none", "No: can't read requests"), ("none", "No")]),
    ("SQL injection or cross-site scripting in a form",
     [("none", "No"), ("none", "No"), ("main", "Main: managed rule groups"), ("none", "No: can't read requests"), ("none", "No")]),
    ("Requests from one bad address range",
     [("none", "No"), ("none", "No"), ("main", "Main: IP set rule, for web traffic"), ("main", "Main: network ACL deny, for a subnet"), ("none", "No")]),
    ("The same rules in all of a company's accounts",
     [("none", "No"), ("none", "No"), ("none", "One account at a time"), ("none", "One VPC at a time"), ("main", "Main: one policy for all")]),
    ("Expert help and bill protection during a big attack",
     [("none", "No"), ("main", "Main: SRT and cost protection"), ("none", "No"), ("none", "No"), ("none", "No")]),
]


def attack_matrix():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Which protection stops which attack</text>',
        '<text class="sub" x="16" y="48">Read across a row: the shaded "Main" cell is the first choice; "Adds" cells strengthen it</text>',
    ]
    lw, cw, gap, top = 150, 98, 4, 66
    x0 = 16 + lw
    for i, c in enumerate(COLS):
        lines = wrap(c, 14)
        text_lines(body, x0 + i * (cw + gap) + cw / 2, top + 4, lines, cls="cellb", dy=14, anchor="middle")
    y = top + 36
    for need, cells in ROWS:
        nl = wrap(need, 23)
        cl = [wrap(t, 14 if k == "none" else 12) for k, t in cells]
        h = max(14 * len(nl), 14 * max(len(c) for c in cl)) + 14
        text_lines(body, 16, y + 18, nl, cls="cellb", dy=14)
        for i, ((kind, _), lines) in enumerate(zip(cells, cl)):
            x = x0 + i * (cw + gap)
            cls = {"main": "hi", "helps": "alt", "none": "none"}[kind]
            rect(body, cls, x, y, cw, h, 4)
            text_lines(body, x + 6, y + 17, lines, cls="cells" if kind == "none" else "cellb", dy=14)
        y += h + gap
    y += 14
    y = text_lines(body, 16, y, [
        "Each cell also says Main, Adds or No in words. SRT is the Shield Response Team. From the AWS WAF, AWS Shield and",
        "AWS Firewall Manager developer guides, checked 2026-10-24.",
    ], cls="note", dy=15)
    desc = ["A grid of six needs against five protections: Shield Standard, Shield Advanced, AWS WAF, network ACL or "
            "security group, and Firewall Manager."]
    for need, cells in ROWS:
        desc.append(f"{need}: " + "; ".join(f"{c}, {t}" for c, (_, t) in zip(COLS, cells)) + ".")
    svg("09-04-attack-matrix.svg", w, y + 4, "Which AWS protection stops which kind of attack", " ".join(desc),
        body, style=STYLE)


def shield_tiers():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Shield Standard comes with your account; Shield Advanced is a decision</text>',
        '<text class="sub" x="16" y="48">What each tier gives you, as AWS described it when we checked</text>',
    ]
    std = [
        "No additional charge, and nothing to turn on: every AWS customer has it",
        "Defends against the most common network and transport layer attacks, such as SYN floods and UDP reflection",
        "Strongest for CloudFront, Route 53 hosted zones and Global Accelerator",
        "No people to call, no bill protection, no web-request (layer 7) mitigation",
    ]
    adv = [
        "$3,000 a month with a 1-year subscription, billed once per organization's payer account, plus data transfer fees",
        "You choose the resources: CloudFront, Route 53 hosted zones, load balancers, Elastic IP addresses, Global Accelerator",
        "Adds automatic web-request (layer 7) mitigation through AWS WAF, and covers standard WAF fees on those resources",
        "Shield Response Team (SRT): DDoS experts, around the clock; AWS's page also requires a Business or Enterprise Support plan",
        "DDoS cost protection: credits for scaling charges an attack causes",
    ]
    pw, top = 316, 66
    h = max(bullets_height(pw, std), bullets_height(pw, adv))
    bullets_card(body, "n", 16, top, pw, h, "AWS Shield Standard", std)
    bullets_card(body, "hi", 16 + pw + 16, top, pw, h, "AWS Shield Advanced", adv)
    y = top + h + 24
    y = text_lines(body, 16, y, [
        "Support plans change on 2027-01-01, when Business Support ends; AWS's SRT page still named it on 2026-10-24.",
        "From the AWS Shield developer guide, Shield FAQ and Shield pricing page, checked 2026-10-24. Prices change.",
    ], cls="note", dy=15)
    svg("09-04-shield-tiers.svg", w, y + 4, "AWS Shield Standard compared with AWS Shield Advanced",
        "Two panels. Left: AWS Shield Standard. No additional charge and nothing to turn on: every AWS customer "
        "has it. It defends against the most common network and transport layer attacks, such as SYN floods and "
        "UDP reflection. It is strongest for CloudFront, Route 53 hosted zones and Global Accelerator. It has no "
        "people to call, no bill protection and no web-request (layer 7) mitigation. Right, highlighted: AWS "
        "Shield Advanced. $3,000 a month with a 1-year subscription, billed once per organization's payer "
        "account, plus data transfer fees. You choose the resources to protect: CloudFront, Route 53 hosted "
        "zones, load balancers, Elastic IP addresses and Global Accelerator. It adds automatic web-request (layer "
        "7) mitigation through AWS WAF and covers standard WAF fees on those resources. It brings the Shield "
        "Response Team, DDoS experts available around the clock, and AWS's page also requires a Business or "
        "Enterprise Support plan for them. It adds DDoS cost protection: credits for scaling charges an attack "
        "causes. Note: Support plans change on 2027-01-01, when Business Support ends; AWS's SRT page still named "
        "it on 2026-10-24.", body, style=STYLE)


# Monthly cost, US dollars. WAF: 1 web ACL + 4 rules or rule groups + 2 million requests.
WAF_BAKERY = 5.00 + 4 * 1.00 + 2 * 0.60
COSTS = [
    ("Shield Standard", 0.0, "$0: included for every customer"),
    ("AWS WAF, the bakery's setup", WAF_BAKERY, f"${WAF_BAKERY:.2f}: 1 web ACL, 4 rules, 2 million requests"),
    ("Firewall Manager, 1 policy", 100.0, "$100 per policy per Region (needs an organization)"),
    ("Shield Advanced", 3000.0, "$3,000 + data transfer fees; 1-year subscription"),
]


def monthly_cost():
    w = 680
    left, top, pw, rowh = 196, 84, 300, 40
    xmax = 3000.0
    body = [
        '<text class="title" x="16" y="28">What the front-door protections cost a month</text>',
        '<text class="sub" x="16" y="48">US dollars a month, from AWS\'s pricing pages; the bakery\'s WAF traffic is an example</text>',
    ]
    for i, (lab, usd, note) in enumerate(COSTS):
        y = top + i * rowh
        body.append(f'<text class="lab" x="{left - 12}" y="{y + 18}" text-anchor="end">{lab}</text>')
        if usd == 0:
            body.append(f'<line class="zero" x1="{left}" x2="{left}" y1="{y + 4}" y2="{y + 24}"><title>{lab}: $0</title></line>')
            body.append(f'<text class="val" x="{left + 10}" y="{y + 19}">{note}</text>')
            continue
        bw = max(pw * usd / xmax, 2)
        body.append(f'<path class="s1" d="{right_rounded(left, y + 4, bw, 20)}"><title>{lab}: ${usd:,.2f} a month</title></path>')
        if bw > pw * 0.6:
            body.append(f'<text class="val" x="{left}" y="{y + 40}">{note}</text>')
        else:
            body.append(f'<text class="val" x="{left + bw + 8:.1f}" y="{y + 19}">{note}</text>')
    yb = top + len(COSTS) * rowh + 8
    body.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top}" y2="{yb - 4}"/>')
    y = yb + 16
    y = text_lines(body, 16, y, [
        "A year of Shield Advanced is at least $36,000, about 290 times the bakery's WAF bill. Shield Advanced covers the",
        "standard WAF fees for the resources it protects, and Firewall Manager fees for its WAF and Shield Advanced policies.",
    ], cls="small", dy=17)
    y = text_lines(body, 16, y + 4, [
        "Shield, WAF and Firewall Manager pricing pages, checked 2026-10-24. WAF: $5 per web ACL, $1 per rule or rule",
        "group, $0.60 per million requests, a month. The bakery's numbers are made up; check AWS Pricing Calculator.",
    ], cls="note", dy=15)
    svg("09-04-monthly-cost.svg", w, y + 4, "Monthly cost of Shield Standard, AWS WAF, Firewall Manager and Shield Advanced",
        f"Horizontal bar chart in US dollars a month. Shield Standard: $0, included for every customer. AWS WAF "
        f"for the bakery's example setup of one web ACL, four rules or rule groups and 2 million requests: "
        f"${WAF_BAKERY:.2f}, a bar too thin to see. Firewall Manager, one policy: $100 per policy per Region, and it "
        f"needs an organization. Shield Advanced: $3,000 plus data transfer fees, with a 1-year subscription, the "
        f"full width of the chart. A year of Shield Advanced is at least $36,000, about 290 times the bakery's WAF "
        f"bill. Shield Advanced covers the standard WAF fees for the resources it protects, and Firewall Manager "
        f"fees for its WAF and Shield Advanced policies. Sources: the Shield, WAF and Firewall Manager pricing pages, checked 2026-10-24.",
        body, style=STYLE)


if __name__ == "__main__":
    front_door()
    attack_matrix()
    shield_tiers()
    monthly_cost()
