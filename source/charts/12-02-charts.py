#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 12.02 (tools that watch your account) as SVG.

Usage: python3 -I source/charts/12-02-charts.py
Writes images/12-02-big-picture.svg. Facts come from AWS pages cited in
guide/12-getting-help/02-tools-that-watch-your-account.md, read 2026-10-24:
- AWS Trusted Advisor and its check reference (six categories: Cost
  optimization, Performance, Security, Fault tolerance, Service limits,
  Operational Excellence; Basic Support: all Service limits checks plus
  selected Security and Fault tolerance checks, Security checks refreshed by
  hand; Business Support+, Enterprise and Unified Operations: all checks, the
  Trusted Advisor API and EventBridge monitoring);
- the Trusted Advisor product page (Trusted Advisor Priority for Enterprise
  Support and Unified Operations);
- What is AWS Health? and AWS Health Dashboard - Service health (dashboard
  free for all customers with no setup; service health page needs no sign-in
  and shows 12 months of history; EventBridge delivery free for all; Health
  API needs Business Support+, Enterprise or Unified Operations);
- the 2022-02-28 What's New post announcing one AWS Health Dashboard that
  brings together the Service Health Dashboard and Personal Health Dashboard;
- Case management, user guide (account and billing, and service limit
  increase cases for everyone; technical cases not on Basic).
No check counts are drawn on purpose: AWS's pages disagree on them.
The bakery is made up for teaching. Our own design: no AWS logos, icons,
trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --hi-fill:#d9e8fb; --n-fill:#f1f0ec; --none-fill:#fbfbf9;",
    dark_extra=" --hi-fill:#1b3554; --n-fill:#252523; --none-fill:#1f1f1e;",
    rules_extra="""
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 2; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .none { fill: var(--none-fill); stroke: var(--axis); stroke-width: 1; stroke-dasharray: 4 3; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .boxt { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .head { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .q { fill: var(--ink); font-size: 12.5px; font-style: italic; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .tag { fill: var(--ink); font-size: 11.5px; font-weight: 600; letter-spacing: 0.4px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }
  .dashline { stroke: var(--axis); stroke-width: 1.5; stroke-dasharray: 6 4; }""")

CH = 6.3  # rough width of one 12px character, for wrapping
CHECKED = "2026-10-24"


def arrow(body, x1, y1, x2, y2):
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def card(body, cls, x, y, w, title, lines, h, q=None):
    """A box with a bold title, an optional italic question and bulleted, wrapped lines."""
    body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    body.append(f'<text class="boxt" x="{x + 10}" y="{y + 22}">{title}</text>')
    ty = y + 40
    if q:
        for part in wrap(q, int((w - 20) / 6.6)):
            body.append(f'<text class="q" x="{x + 10}" y="{ty}">{part}</text>')
            ty += 16
        ty += 6
    for ln in lines:
        for j, part in enumerate(wrap(ln, int((w - 30) / CH))):
            body.append(f'<text class="cells" x="{x + 10 + (0 if j == 0 else 9)}" y="{ty}">{"• " if j == 0 else ""}{part}</text>')
            ty += 15
        ty += 4


def big_picture():
    """Three tools, three directions: your setup, AWS's side, and a person at AWS."""
    w = 700
    body = [
        '<text class="title" x="16" y="28">Three tools, three different things to watch</text>',
        f'<text class="sub" x="16" y="48">Highlighted: the only tool that reports on AWS\'s side rather than yours. Checked {CHECKED}</text>',
    ]
    # Two zones: your account (left) and AWS's side (right), split by a dashed line.
    body.append('<text class="tag" x="16" y="84">YOUR SIDE: YOUR ACCOUNT AND ITS RESOURCES</text>')
    body.append('<text class="tag" x="474" y="84">AWS\'S SIDE</text>')
    body.append('<line class="dashline" x1="456" y1="70" x2="456" y2="430"/>')
    cw = 210
    card(body, "n", 16, 100, cw, "AWS Trusted Advisor",
         ["Checks your settings against AWS's best practices",
          "Six categories, from cost to security",
          "Basic: some checks. Paid plans: all checks"],
         210, q="\"Is anything in our setup wasteful, risky or near a limit?\"")
    card(body, "n", 238, 100, cw, "AWS Support Center",
         ["Where you open cases and request quota increases",
          "Basic: account, billing and quota cases",
          "Paid plans: technical cases too"],
         210, q="\"We need a person at AWS to help.\"")
    card(body, "hi", 474, 100, cw - 0, "AWS Health",
         ["Reports AWS's own events: issues, planned maintenance, account notices",
          "Dashboard: free for everyone",
          "Health API: paid plans"],
         210, q="\"Is AWS having a problem that affects us?\"")
    # The bakery's account at the bottom, with arrows up to the tools.
    body.append('<rect class="plain" x="16" y="350" width="432" height="54" rx="6"/>')
    text_lines(body, 28, 372, ["The bakery's account: EC2 web servers, RDS orders database,",
                               "Lambda functions, S3 photo bucket, the VPC"], cls="cells", dy=15)
    body.append('<rect class="plain" x="474" y="350" width="210" height="54" rx="6"/>')
    text_lines(body, 486, 372, ["AWS's services, Regions and", "data centers"], cls="cells", dy=15)
    arrow(body, 120, 348, 120, 314)
    body.append('<text class="note" x="128" y="336">reads settings</text>')
    arrow(body, 342, 314, 342, 348)
    body.append('<text class="note" x="350" y="336">you ask; a person answers</text>')
    arrow(body, 578, 348, 578, 314)
    body.append('<text class="note" x="586" y="336">reports events</text>')
    y = text_lines(body, 16, 436, [
        "Trusted Advisor looks at what you built; AWS Health looks at what AWS runs. Support Center is where you talk to AWS",
        "Support. From AWS's Trusted Advisor, AWS Health and Support Center documentation.",
    ], cls="note", dy=15)
    svg("12-02-big-picture.svg", w, y + 2,
        "Trusted Advisor, AWS Support Center and AWS Health, and what each one watches",
        "A dashed line splits the picture into your side, your account and its resources, on the left, and AWS's "
        "side on the right. On your side: AWS Trusted Advisor answers \"Is anything in our setup wasteful, risky or "
        "near a limit?\" It checks your settings against AWS's best practices in six categories; Basic gets some "
        "checks and paid plans all. An arrow labeled reads settings runs up to it from the bakery's account, which "
        "holds the EC2 web servers, the RDS orders database, Lambda functions, the S3 photo bucket and the VPC. "
        "AWS Support Center answers \"We need a person at AWS to help\": it is where you open cases and request "
        "quota increases; Basic gets account, billing and quota cases, and paid plans technical cases too. An arrow "
        "labeled you ask, a person answers runs down from it. On AWS's side, highlighted: AWS Health answers \"Is AWS "
        "having a problem that affects us?\" It reports AWS's own events, such as issues, planned maintenance and "
        "account notices; its dashboard is free for everyone and its API needs a paid plan. An arrow labeled "
        f"reports events runs up to it from AWS's services, Regions and data centers. Checked {CHECKED}.",
        body, style=STYLE)



if __name__ == "__main__":
    big_picture()
