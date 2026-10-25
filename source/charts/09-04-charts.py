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
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

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


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


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


if __name__ == "__main__":
    attack_matrix()
