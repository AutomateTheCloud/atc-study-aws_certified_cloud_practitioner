#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the chart for Simulation S15 (Support plan chooser) as SVG.

Usage: python3 -I source/charts/12-06-charts.py
Writes images/12-06-plan-fees.svg.

Prices, USD a month, from AWS Support pricing (https://aws.amazon.com/premiumsupport/pricing/),
read 2026-10-24:
- Basic: included, no fee.
- Business Support+: the greater of $29 or 9% of monthly AWS charges up to $10K,
  7% from $10K to $80K, 5% from $80K to $250K, 3% over $250K. Per account.
- Enterprise Support: the greater of $5K or 10% up to $150K, 7% from $150K to $500K,
  5% from $500K to $1M, 3% over $1M (standard pricing, not the regional rates).
- Unified Operations: the greater of $50K or 10% up to $1M, 6% from $1M to $5M,
  5% over $5M (commercial Regions, not GovCloud).
The fees on the chart are our arithmetic from those tiers; the page's own worked
example (Business Support+ at $20K = $1.6K) checks the method. The marked bills are
the made-up businesses of the simulation. Our own design: no AWS logos or trade dress.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import line_key, make_style, svg  # noqa: E402

TIERS = {
    "bsp": (29, [(10_000, 0.09), (80_000, 0.07), (250_000, 0.05), (math.inf, 0.03)]),
    "ent": (5_000, [(150_000, 0.10), (500_000, 0.07), (1_000_000, 0.05), (math.inf, 0.03)]),
    "uo": (50_000, [(1_000_000, 0.10), (5_000_000, 0.06), (math.inf, 0.05)]),
}


def fee(plan, bill):
    """Monthly Support fee for a monthly AWS bill: the greater of the minimum or the tiered sum."""
    minimum, tiers = TIERS[plan]
    total, low = 0.0, 0.0
    for high, rate in tiers:
        if bill > low:
            total += (min(bill, high) - low) * rate
        low = high
    return max(minimum, total)


assert round(fee("bsp", 20_000)) == 1_600  # AWS's worked example
assert round(fee("ent", 750_000)) == 52_000  # AWS's worked example
assert round(fee("uo", 1_500_000)) == 130_000  # AWS's worked example

STYLE = make_style(
    light_extra=" --s3:#1baf7a;",
    dark_extra=" --s3:#199e70;",
    rules_extra="""
  .line-s2 { stroke: var(--s2); stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .line-s3 { stroke: var(--s3); stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .mark { stroke: var(--ink2); stroke-width: 1; stroke-dasharray: 4 4; }
  .dot-ink { fill: var(--ink); stroke: var(--surface); stroke-width: 2; }""",
)


def money(v):
    if v >= 1_000_000:
        return f"${v / 1_000_000:g}M"
    if v >= 1_000:
        return f"${v / 1_000:g}K"
    return f"${v:g}"


def plan_fees():
    w, h = 800, 500
    left, top, pw, ph = 86, 96, 540, 330
    xmin, xmax = 100, 2_000_000
    ymin, ymax = 10, 200_000

    def x(v):
        return left + pw * (math.log10(v) - math.log10(xmin)) / (math.log10(xmax) - math.log10(xmin))

    def y(v):
        return top + ph - ph * (math.log10(v) - math.log10(ymin)) / (math.log10(ymax) - math.log10(ymin))

    body = [
        '<text class="title" x="16" y="28">What each paid Support plan costs a month, by the size of the AWS bill</text>',
        '<text class="sub" x="16" y="48">US dollars, AWS Support pricing as of 2026-10-24. Basic costs $0 at any bill.</text>',
        '<text class="sub" x="16" y="66">Both axes are logarithmic: each gridline is 10 times the one before.</text>',
    ]
    for v in [10, 100, 1_000, 10_000, 100_000]:
        body.append(f'<line class="grid" x1="{left}" x2="{left + pw}" y1="{y(v):.1f}" y2="{y(v):.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{y(v) + 4:.1f}" text-anchor="end">{money(v)}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 12}">Support fee a month</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{left + pw}" y1="{top + ph}" y2="{top + ph}"/>')
    for v in [100, 1_000, 10_000, 100_000, 1_000_000]:
        body.append(f'<text class="tick" x="{x(v):.1f}" y="{top + ph + 18}" text-anchor="middle">{money(v)}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2:.1f}" y="{top + ph + 40}" text-anchor="middle">Monthly AWS bill</text>')

    # the made-up businesses' bills, as faint markers
    for bill, label in [(1_200, "Bakery"), (120_000, "Retailer"), (400_000, "Payments")]:
        body.append(f'<line class="mark" x1="{x(bill):.1f}" x2="{x(bill):.1f}" y1="{top}" y2="{top + ph}"/>')
        body.append(f'<text class="tick" x="{x(bill):.1f}" y="{top - 4}" text-anchor="middle">{label}</text>')

    steps = [10 ** (2 + i * (math.log10(xmax) - 2) / 400) for i in range(401)]
    for plan, cls in [("bsp", "line-s1"), ("ent", "line-s2"), ("uo", "line-s3")]:
        pts = " ".join(f"{x(b):.1f},{y(fee(plan, b)):.1f}" for b in steps)
        body.append(f'<polyline class="{cls}" points="{pts}"/>')

    # direct labels at the right end of each line
    # spread the labels at least 20px apart, with a short leader to each line's end
    end = xmax
    ys, prev = [], None
    for plan, name in [("uo", "Unified Operations"), ("ent", "Enterprise"), ("bsp", "Business Support+")]:
        ly = y(fee(plan, end)) + 4
        if prev is not None and ly < prev + 20:
            ly = prev + 20
        prev = ly
        body.append(f'<line class="lead" x1="{x(end) + 2:.1f}" x2="{x(end) + 14:.1f}" y1="{y(fee(plan, end)):.1f}" y2="{ly - 4:.1f}"/>')
        body.append(f'<text class="lab" x="{x(end) + 18:.1f}" y="{ly:.1f}">{name}</text>')

    # the bakery's three prices, with values
    for plan, dy in [("bsp", 18), ("ent", 18), ("uo", 18)]:
        v = fee(plan, 1_200)
        body.append(f'<circle class="dot-ink" cx="{x(1_200):.1f}" cy="{y(v):.1f}" r="5"/>')
        body.append(f'<text class="lab" x="{x(1_200) + 9:.1f}" y="{y(v) + dy:.1f}">{money(round(v))}</text>')

    # legend
    line_key(body, 86, 486, "line-s1", "Business Support+ (from $29)")
    line_key(body, 306, 486, "line-s2", "Enterprise (from $5K)")
    line_key(body, 490, 486, "line-s3", "Unified Operations (from $50K)")

    desc = (
        "Log-log line chart. Business Support+ is flat at $29 until the bill reaches about $322, then rises with it: "
        "$108 at the bakery's $1,200 bill. Enterprise is flat at $5,000 until about $50,000, then rises: "
        "$12,000 at the retailer's $120,000. Unified Operations is flat at $50,000 until $500,000: "
        "it is still $50,000 at the payments company's $400,000. At the bakery's bill, the three plans cost $108, "
        "$5,000 and $50,000."
    )
    svg("12-06-plan-fees.svg", w, h, "Monthly fee of each paid AWS Support plan by monthly AWS bill", desc, body, STYLE)


if __name__ == "__main__":
    plan_fees()
    for b in [300, 1_200, 5_000, 20_000, 120_000, 400_000, 1_500_000]:
        print(b, [round(fee(p, b)) for p in ("bsp", "ent", "uo")])
