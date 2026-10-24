#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the chart for page 00.03 (the exam at a glance: domain weights) as SVG.

Usage: python3 -I source/charts/00-03-charts.py
Writes images/00-03-domain-weights.svg. The weights are from the AWS Certified Cloud
Practitioner (CLF-C02) exam guide, checked 2026-10-23. The question counts are our
arithmetic (weight x 50 scored questions, rounded), not AWS figures.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg  # noqa: E402

SCORED = 50
DOMAINS = [
    ("1", "Cloud Concepts", 24),
    ("2", "Security and Compliance", 30),
    ("3", "Cloud Technology and Services", 34),
    ("4", "Billing, Pricing, and Support", 12),
]

STYLE = make_style()


def domain_weights():
    w, left, top, pw, rowh = 680, 250, 84, 250, 52
    xmax = 40
    h = top + rowh * len(DOMAINS) + 40
    body = [
        '<text class="title" x="16" y="28">Security and technology make up almost two-thirds of the exam</text>',
        '<text class="sub" x="16" y="50">CLF-C02 domain weights from the exam guide (checked 2026-10-23)</text>',
    ]
    ph = rowh * len(DOMAINS)
    for v in range(0, xmax + 1, 10):
        x = left + pw * v / xmax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 6}" y2="{top + ph - 12}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top + ph + 6}" text-anchor="middle">{v}%</text>')
    for i, (num, name, pct) in enumerate(DOMAINS):
        y = top + i * rowh
        q = round(pct * SCORED / 100)
        body.append(f'<text class="lab" x="16" y="{y + 13}">Domain {num}</text>')
        body.append(f'<text x="16" y="{y + 30}">{name}</text>')
        bw = pw * pct / xmax
        body.append(f'<path class="s1" d="{right_rounded(left, y, bw, 22)}"><title>Domain {num}, {name}: {pct}%, about {q} scored questions</title></path>')
        body.append(f'<text class="lab" x="{left + bw + 8:.1f}" y="{y + 16}">{pct}% · about {q} questions</text>')
    body.append(f'<text class="tick" x="16" y="{h - 12}">Questions: our arithmetic, weight × 50 scored questions. Each exam form varies.</text>')
    svg(
        "00-03-domain-weights.svg", w, h,
        "CLF-C02 domain weights",
        "Horizontal bar chart of the four exam domains and their weights. "
        "Domain 1, Cloud Concepts: 24%, about 12 of 50 scored questions. "
        "Domain 2, Security and Compliance: 30%, about 15. "
        "Domain 3, Cloud Technology and Services: 34%, about 17. "
        "Domain 4, Billing, Pricing, and Support: 12%, about 6.",
        body, STYLE,
    )


if __name__ == "__main__":
    domain_weights()
