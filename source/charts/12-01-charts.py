#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 12.01 (AWS Support plans) as SVG.

Usage: python3 -I source/charts/12-01-charts.py
Writes images/12-01-plan-ladder.svg. Facts come from AWS pages cited in
guide/12-getting-help/01-support-plans.md, read 2026-10-24:
- Compare AWS Support plans (https://aws.amazon.com/premiumsupport/plans/):
  the four current plans, what each adds, response-time targets per severity,
  and the footnote "We will make every reasonable effort to respond ...";
- AWS Support Plans, user guide (features of each plan; Basic: account and
  billing questions and service quota increases, no technical cases);
- Case management, user guide (severity levels and first-response times);
- AWS Support Plan Pricing (https://aws.amazon.com/premiumsupport/pricing/):
  Business Support+ $29 minimum per account, 9% up to $10K, 7% $10K-$80K,
  5% $80K-$250K, 3% over $250K; Enterprise $5K minimum, 10% up to $150K,
  7% $150K-$500K, 5% $500K-$1M, 3% over $1M; Unified Operations $50K minimum.
The fee is the greater of the minimum and the tiered percentage.
The bakery and its bill are made up for teaching. Our own design: no AWS
logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Slot 1 (blue) tint marks the one highlighted element; everything else is neutral.
STYLE = make_style(
    light_extra=" --hi-fill:#d9e8fb; --n-fill:#f1f0ec; --none-fill:#fbfbf9;",
    dark_extra=" --hi-fill:#1b3554; --n-fill:#252523; --none-fill:#1f1f1e;",
    rules_extra="""
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 2; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .none { fill: var(--none-fill); stroke: var(--axis); stroke-width: 1; stroke-dasharray: 4 3; }
  .boxt { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .price { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .head { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .tag { fill: var(--ink); font-size: 11.5px; font-weight: 600; letter-spacing: 0.4px; }
  .line-s2 { stroke: var(--s2); stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .dot-ink { fill: var(--ink); stroke: var(--surface); stroke-width: 2; }""")

CH = 6.3  # rough width of one 12px character, for wrapping
CHECKED = "2026-10-24"


def plan_ladder():
    """Big picture: four plans as rising steps, each adding to the one below."""
    w = 700
    body = [
        '<text class="title" x="16" y="28">Four AWS Support plans, each including the one before</text>',
        f'<text class="sub" x="16" y="48">Monthly minimum prices as of {CHECKED}. Highlighted: the step where technical help starts</text>',
    ]
    plans = [
        ("Basic", "Free, every account", "n", [
            "Cases about your account and bill",
            "Service quota increase requests",
            "Docs, whitepapers, re:Post",
            "Some Trusted Advisor checks",
            "AWS Health Dashboard",
            "No technical cases",
        ]),
        ("Business Support+", "From $29 a month", "hi", [
            "Technical cases, 24/7, by phone, web and chat",
            "Business-critical system down: under 30 minutes",
            "All Trusted Advisor checks",
            "AWS Health API, Support API",
            "AI help with your account's context",
        ]),
        ("Enterprise Support", "From $5,000 a month", "n", [
            "A designated Technical Account Manager (TAM)",
            "Business-critical: under 15 minutes",
            "Well-Architected reviews",
            "Trusted Advisor Priority",
            "Security Incident Response included",
        ]),
        ("Unified Operations", "From $50,000 a month", "n", [
            "TAM plus designated domain specialists",
            "Critical incidents: under 5 minutes, from an Incident Management Engineer",
            "24/7 workload monitoring",
            "Critical workload reviews",
        ]),
    ]
    cw, gap, x0 = 160, 12, 16
    step = 34
    base = 470
    for i, (name, price, cls, lines) in enumerate(plans):
        x = x0 + i * (cw + gap)
        top = 96 + (3 - i) * step
        body.append(f'<rect class="{cls}" x="{x}" y="{top}" width="{cw}" height="{base - top}" rx="6"/>')
        body.append(f'<text class="boxt" x="{x + 10}" y="{top + 22}">{name}</text>')
        body.append(f'<text class="price" x="{x + 10}" y="{top + 40}">{price}</text>')
        if i > 0:
            body.append(f'<text class="note" x="{x + 10}" y="{top + 58}">Everything to the left, plus:</text>')
            y = top + 78
        else:
            y = top + 62
        for ln in lines:
            parts = wrap(ln, int((cw - 30) / CH))
            for j, part in enumerate(parts):
                prefix = "• " if j == 0 else ""
                body.append(f'<text class="cells" x="{x + 10 + (0 if j == 0 else 9)}" y="{y}">{prefix}{part}</text>')
                y += 15
            y += 4
    y = base + 22
    y = text_lines(body, 16, y, [
        "Response times are AWS's targets for a first reply, not guarantees. Paid plans are billed monthly: the greater",
        "of the minimum and a percentage of your AWS bill. From AWS's Compare AWS Support plans and pricing pages.",
    ], cls="note", dy=15)
    svg("12-01-plan-ladder.svg", w, y + 2,
        "The four current AWS Support plans as rising steps",
        "Four steps rise from left to right, each adding to the one before it. Basic: free for every account; "
        "cases about your account and bill, service quota increase requests, documentation, whitepapers and "
        "re:Post, some Trusted Advisor checks and the AWS Health Dashboard, but no technical cases. Business "
        "Support+, highlighted as the step where technical help starts: from $29 a month; technical cases 24/7 by "
        "phone, web and chat, under 30 minutes for a business-critical system down, all Trusted Advisor checks, "
        "the AWS Health API and Support API, and AI help that uses your account's context. Enterprise Support: "
        "from $5,000 a month; a designated Technical Account Manager, under 15 minutes for business-critical "
        "cases, Well-Architected reviews, Trusted Advisor Priority and Security Incident Response included. "
        "Unified Operations: from $50,000 a month; a TAM plus designated domain specialists, under 5 minutes for "
        "critical incidents from an Incident Management Engineer, 24/7 workload monitoring and critical "
        f"workload reviews. Prices are monthly minimums as of {CHECKED}. Response times are targets for a first "
        "reply, not guarantees.",
        body, style=STYLE)



if __name__ == "__main__":
    plan_ladder()
