#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 12.02 (tools that watch your account) as SVG.

Usage: python3 -I source/charts/12-02-charts.py
Writes images/12-02-*.svg. Facts come from AWS pages cited in
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


def ta_access():
    """Trusted Advisor categories against Support plans: what Basic sees."""
    w = 700
    body = [
        '<text class="title" x="16" y="28">What Trusted Advisor shows on each Support plan</text>',
        f'<text class="sub" x="16" y="48">Six categories, no check counts: AWS\'s pages disagree on them. Checked {CHECKED}</text>',
    ]
    cols = ["Basic|(every account)", "Business|Support+", "Enterprise and|Unified Operations"]
    rows = [
        ("Service limits", ["All checks", "All checks", "All checks"]),
        ("Security", ["A few selected checks, such as root MFA", "All checks", "All checks"]),
        ("Fault tolerance", ["One selected check", "All checks", "All checks"]),
        ("Cost optimization", ["None", "All checks", "All checks"]),
        ("Performance", ["None", "All checks", "All checks"]),
        ("Operational excellence", ["None", "All checks", "All checks"]),
        ("Refresh", ["Security checks by hand", "Automatic", "Automatic"]),
        ("API and EventBridge", ["No", "Yes", "Yes"]),
        ("Trusted Advisor Priority", ["No", "No", "Yes, from your account team"]),
    ]
    lx, lw = 16, 168
    cw = (w - 32 - lw) / 3
    top = 66
    for i, c in enumerate(cols):
        x = lx + lw + i * cw
        for j, part in enumerate(c.split("|")):
            body.append(f'<text class="head" x="{x + cw / 2:.1f}" y="{top + 8 + 16 * j}" text-anchor="middle">{part}</text>')
    y = top + 30
    rh = 40
    for k, (label, vals) in enumerate(rows):
        if k == 6:
            body.append(f'<line class="axis" x1="{lx}" x2="{w - 16}" y1="{y + 3}" y2="{y + 3}"/>')
            y += 8
        body.append(f'<text class="head" x="{lx}" y="{y + rh / 2 + 5:.1f}">{label}</text>')
        for i, v in enumerate(vals):
            x = lx + lw + i * cw
            if v in ("None", "No"):
                cls = "none"
            else:
                cls = "hi" if i == 0 else "n"
            body.append(f'<rect class="{cls}" x="{x + 3:.1f}" y="{y + 3}" width="{cw - 6:.1f}" height="{rh - 6}" rx="5"/>')
            parts = wrap(v, int((cw - 16) / 6.1))
            ty = y + rh / 2 + 5 - (len(parts) - 1) * 7
            for part in parts:
                body.append(f'<text class="cells" x="{x + cw / 2:.1f}" y="{ty:.1f}" text-anchor="middle">{part}</text>')
                ty += 14
        y += rh
    y += 20
    y = text_lines(body, 16, y, [
        "Highlighted: what Basic gets. Dashed: not available. From AWS's Trusted Advisor user guide, check reference and",
        "product page. Basic's selected checks have changed before and can change again: check the live list.",
    ], cls="note", dy=15)
    svg("12-02-ta-access.svg", w, y + 2,
        "Trusted Advisor check categories and features by Support plan",
        "A grid with three plan columns: Basic, on every account; Business Support+; and Enterprise and Unified "
        "Operations. Six category rows. Service limits: all checks on every plan. Security: Basic gets a few "
        "selected checks, such as root MFA and open ports; paid plans get all checks. Fault tolerance: Basic gets "
        "one selected check; paid plans all. Cost optimization, performance and operational excellence: none on "
        "Basic; all checks on paid plans. Three feature rows. Refresh: Basic refreshes security checks by hand; "
        "paid plans refresh automatically. API and EventBridge: no on Basic, yes on paid plans. Trusted Advisor "
        "Priority: only Enterprise and Unified Operations, from the account team. Basic's cells are highlighted; "
        f"unavailable cells are dashed. No check counts are given because AWS's pages disagree. Checked {CHECKED}.",
        body, style=STYLE)


def health_views():
    """One service, AWS Health; two dashboard views; two ways to feed your own tools."""
    w = 700
    body = [
        '<text class="title" x="16" y="28">AWS Health: one dashboard with two views, and two feeds</text>',
        f'<text class="sub" x="16" y="48">The two old dashboard names are now the two views of one dashboard. Checked {CHECKED}</text>',
    ]
    # Outer box: AWS Health.
    body.append('<rect class="plain" x="16" y="66" width="668" height="332" rx="8"/>')
    body.append('<text class="boxt" x="30" y="90">AWS Health: events on AWS\'s side that can affect you</text>')
    # Dashboard box, highlighted, with two views inside.
    body.append('<rect class="hi" x="30" y="104" width="640" height="168" rx="6"/>')
    body.append('<text class="boxt" x="44" y="128">AWS Health Dashboard: free for every customer, no setup</text>')
    card(body, "n", 44, 140, 300, "Service health",
         ["Public events for all services and Regions",
          "No sign-in, no account needed",
          "Service history: the last 12 months",
          "Older name: Service Health Dashboard"], 118)
    card(body, "n", 356, 140, 300, "Your account health",
         ["After you sign in: events that affect your own resources, such as planned maintenance on an instance you run",
          "Also shows the public events",
          "Older name: Personal Health Dashboard"], 118)
    # Feeds.
    card(body, "n", 30, 286, 312, "Amazon EventBridge",
         ["Sends Health events to your own rules and tools",
          "Free for every customer"], 96)
    card(body, "n", 358, 286, 312, "AWS Health API",
         ["Your programs ask AWS Health directly",
          "Business Support+, Enterprise or Unified Operations; on Basic it refuses the call"], 96)
    y = text_lines(body, 16, 420, [
        "AWS announced one dashboard bringing the two older ones together on 2022-02-28. From What is AWS Health?, the",
        "Service health page and AWS's What's New post.",
    ], cls="note", dy=15)
    svg("12-02-health-views.svg", w, y + 2,
        "AWS Health: one dashboard with two views, plus EventBridge and the Health API",
        "An outer box, AWS Health: events on AWS's side that can affect you. Inside it, highlighted, the AWS Health "
        "Dashboard, free for every customer with no setup, holds two views. Service health: public events for all "
        "services and Regions, with no sign-in and no account needed, and 12 months of service history; its older "
        "name was Service Health Dashboard. Your account health: after you sign in, events that affect your own "
        "resources, such as planned maintenance on an instance you run, plus the public events; its older name was "
        "Personal Health Dashboard. Below the dashboard, two feeds. Amazon EventBridge sends Health events to your "
        "own rules and tools, free for every customer. The AWS Health API lets your programs ask AWS Health "
        "directly; it needs Business Support+, Enterprise or Unified Operations, and on Basic it refuses the call. "
        f"AWS announced the single dashboard on 2022-02-28. Checked {CHECKED}.",
        body, style=STYLE)


if __name__ == "__main__":
    big_picture()
    ta_access()
    health_views()
