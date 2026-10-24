#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 12.01 (AWS Support plans) as SVG.

Usage: python3 -I source/charts/12-01-charts.py
Writes images/12-01-*.svg. Facts come from AWS pages cited in
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
from chartkit import line_key, make_style, svg, text_lines, wrap  # noqa: E402

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


def response_grid():
    """Severity levels against plans: only the top row differs between paid plans."""
    w = 700
    body = [
        '<text class="title" x="16" y="28">First-response targets by case severity</text>',
        f'<text class="sub" x="16" y="48">Technical cases only; checked {CHECKED}. Only the highlighted row differs between the paid plans</text>',
    ]
    cols = ["Basic", "Business Support+", "Enterprise Support", "Unified Operations"]
    rows = [
        ("Business-critical system down", ["—", "Under 30 min", "Under 15 min", "Under 5 min"], True),
        ("Production system down", ["—", "Under 1 hour", "Under 1 hour", "Under 1 hour"], False),
        ("Production system impaired", ["—", "Under 4 hours", "Under 4 hours", "Under 4 hours"], False),
        ("System impaired", ["—", "Under 12 hours", "Under 12 hours", "Under 12 hours"], False),
        ("General guidance", ["—", "Under 24 hours", "Under 24 hours", "Under 24 hours"], False),
    ]
    lx, lw = 16, 200
    cw = (w - 32 - lw) / 4
    top = 70
    rh = 42
    for i, c in enumerate(cols):
        x = lx + lw + i * cw
        parts = c.split(" ", 1) if " " in c else [c]
        for j, part in enumerate(parts):
            body.append(f'<text class="head" x="{x + cw / 2:.1f}" y="{top + 2 + 16 * j + (8 if len(parts) == 1 else 0)}" text-anchor="middle">{part}</text>')
    y = top + 28
    for label, vals, hi in rows:
        body.append(f'<text class="head" x="{lx}" y="{y + rh / 2 + 5:.1f}">{label}</text>')
        for i, v in enumerate(vals):
            x = lx + lw + i * cw
            if i == 0:
                cls = "none"
            else:
                cls = "hi" if hi else "n"
            body.append(f'<rect class="{cls}" x="{x + 3:.1f}" y="{y + 3}" width="{cw - 6:.1f}" height="{rh - 6}" rx="5"/>')
            body.append(f'<text class="cells" x="{x + cw / 2:.1f}" y="{y + rh / 2 + 5:.1f}" text-anchor="middle">{v}</text>')
        y += rh
    y += 22
    y = text_lines(body, 16, y, [
        "Basic: no technical cases at all, so no technical response target. Account, billing and quota cases are open",
        "to every plan. Unified Operations' 5 minutes comes from an Incident Management Engineer.",
        "AWS: \"We will make every reasonable effort to respond to your initial request within the corresponding timeframes.\"",
    ], cls="note", dy=15)
    svg("12-01-response-grid.svg", w, y + 2,
        "First-response targets for technical support cases, by severity and plan",
        "A grid with five severity rows and four plan columns. Basic has a dash in every row: it has no technical "
        "cases. Business-critical system down, highlighted: Business Support+ under 30 minutes, Enterprise "
        "Support under 15 minutes, Unified Operations under 5 minutes from an Incident Management Engineer. "
        "Every other row is the same for the three paid plans: production system down under 1 hour; production "
        "system impaired under 4 hours; system impaired under 12 hours; general guidance under 24 hours. A note "
        "quotes AWS: it will make every reasonable effort to respond to the initial request within these times. "
        f"Checked {CHECKED}.",
        body, style=STYLE)


def bs_plus_fee(bill):
    tiers = [(10_000, 0.09), (80_000, 0.07), (250_000, 0.05), (float("inf"), 0.03)]
    return max(29.0, tiered(bill, tiers))


def enterprise_fee(bill):
    tiers = [(150_000, 0.10), (500_000, 0.07), (1_000_000, 0.05), (float("inf"), 0.03)]
    return max(5000.0, tiered(bill, tiers))


def tiered(bill, tiers):
    fee, low = 0.0, 0.0
    for high, rate in tiers:
        if bill > low:
            fee += (min(bill, high) - low) * rate
        low = high
    return fee


def fee_vs_bill():
    """What each paid plan costs a month, against the monthly AWS bill."""
    w, h = 700, 420
    left, top, pw, ph = 76, 112, 590, 230
    xmax, ymax = 20_000, 6_000
    body = [
        '<text class="title" x="16" y="28">Monthly Support fee against the monthly AWS bill, one account</text>',
        f'<text class="sub" x="16" y="48">The greater of the plan\'s minimum and its percentage of the bill; US dollars, as of {CHECKED}</text>',
    ]
    line_key(body, 16, 74, "line-s1", "Business Support+")
    line_key(body, 180, 74, "line-s2", "Enterprise Support")

    def X(v):
        return left + pw * v / xmax

    def Y(v):
        return top + ph - ph * v / ymax

    for v in range(0, ymax + 1, 1000):
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{Y(v) + 4:.1f}" text-anchor="end">${v:,}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 12}">Support fee a month</text>')
    for v in range(0, xmax + 1, 5000):
        body.append(f'<text class="tick" x="{X(v):.1f}" y="{top + ph + 18}" text-anchor="middle">${v:,}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2:.1f}" y="{top + ph + 38}" text-anchor="middle">AWS bill a month, before credits and discounts</text>')
    pts = [i * 100 for i in range(0, xmax // 100 + 1)]
    body.append('<path class="line-s2" d="M' + " L".join(f"{X(b):.1f},{Y(enterprise_fee(b)):.1f}" for b in pts) + '"/>')
    body.append('<path class="line-s1" d="M' + " L".join(f"{X(b):.1f},{Y(bs_plus_fee(b)):.1f}" for b in pts) + '"/>')
    # Direct labels at the right end.
    body.append(f'<text class="lab" x="{X(xmax) - 4:.1f}" y="{Y(5000) - 10:.1f}" text-anchor="end">Enterprise: $5,000 minimum until the bill passes $50,000</text>')
    b20 = bs_plus_fee(xmax)
    body.append(f'<text class="lab" x="{X(xmax) - 4:.1f}" y="{Y(b20) - 10:.1f}" text-anchor="end">Business Support+: ${b20:,.0f} at a $20,000 bill</text>')
    # The bakery's made-up bill.
    bakery = 1200
    fb = bs_plus_fee(bakery)
    body.append(f'<circle class="dot-ink" cx="{X(bakery):.1f}" cy="{Y(fb):.1f}" r="5"/>')
    body.append(f'<text class="lab" x="{X(bakery) + 10:.1f}" y="{Y(fb) - 56:.1f}">The bakery: a $1,200 bill, ${fb:,.0f} a month</text>')
    body.append(f'<line class="lead" x1="{X(bakery) + 4:.1f}" y1="{Y(fb) - 6:.1f}" x2="{X(bakery) + 10:.1f}" y2="{Y(fb) - 52:.1f}"/>')
    y = top + ph + 64
    y = text_lines(body, 16, y, [
        "Unified Operations starts at $50,000 a month, off this scale. Business Support+ is charged per account; Enterprise on",
        "the total across enrolled accounts. The bakery's bill is made up. From AWS Support Plan Pricing.",
    ], cls="note", dy=15)
    svg("12-01-fee-vs-bill.svg", w, max(h, y + 2),
        "Monthly Support fee against the monthly AWS bill for Business Support+ and Enterprise Support",
        "A line chart. The horizontal axis is the monthly AWS bill from $0 to $20,000; the vertical axis is the "
        "monthly Support fee from $0 to $6,000. Enterprise Support is a flat line at its $5,000 minimum across "
        "the whole range; it stays there until the bill passes $50,000. Business Support+ starts at its $29 "
        "minimum, rises at 9% of the bill to $900 at a $10,000 bill, then at 7% to $1,600 at a $20,000 bill. A "
        "dot marks the bakery's made-up bill of $1,200 a month, where Business Support+ costs $108. Unified "
        f"Operations starts at $50,000 a month, off the scale. Prices as of {CHECKED}, from AWS Support Plan Pricing.",
        body, style=STYLE)


if __name__ == "__main__":
    plan_ladder()
    response_grid()
    fee_vs_bill()
