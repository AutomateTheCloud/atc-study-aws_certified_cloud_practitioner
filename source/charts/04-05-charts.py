#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 04.05 (credentials and federation) as SVG.

Usage: python3 -I source/charts/04-05-charts.py
Writes images/04-05-secrets-vs-parameters.svg. The Secrets Manager and Parameter Store
facts come from their docs and the Secrets Manager pricing page. All checked 2026-10-23. Our own design: no AWS logos, icons or trade dress.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, swatch, text_lines, wrap  # noqa: E402

STYLE = make_style(rules_extra="""
  .card { fill: none; stroke: var(--axis); stroke-width: 1; }
  .hl { fill: none; stroke: var(--s1); stroke-width: 2; }
  .name { fill: var(--ink); font-size: 15px; font-weight: 600; }
  .key { fill: var(--muted); font-size: 11px; font-weight: 600; letter-spacing: 0.5px; }
  .small { fill: var(--ink2); font-size: 12px; }
  .arrow-s2 { fill: var(--s2); }""")

STORES = [
    ("AWS Secrets Manager", [
        ("MADE FOR", "Secrets through their whole life: passwords, API keys, tokens"),
        ("ENCRYPTION", "Always, with AWS KMS"),
        ("AUTOMATIC ROTATION", "Yes, on a schedule; built in for some databases"),
        ("COST (CHECKED 2026-10-23)", "Per secret per month, plus API calls"),
    ]),
    ("Systems Manager Parameter Store", [
        ("MADE FOR", "Configuration values: settings, IDs, addresses"),
        ("ENCRYPTION", "Optional: choose the SecureString type"),
        ("AUTOMATIC ROTATION", "No"),
        ("COST (CHECKED 2026-10-23)", "Standard parameters at no additional charge"),
    ]),
]


def secrets_vs_parameters():
    w, cw, gap, top = 680, 320, 8, 66
    body = [
        '<text class="title" x="16" y="28">Two places to keep values your code needs</text>',
        '<text class="sub" x="16" y="48">The deciding row is rotation: only Secrets Manager changes a secret for you</text>',
    ]
    # rows aligned across both cards
    row_heights = []
    for r in range(4):
        n = max(len(wrap(s[1][r][1], 40)) for s in STORES)
        row_heights.append(16 + 16 * n + 10)
    ch = 44 + sum(row_heights) + 4
    desc = []
    for i, (name, rows) in enumerate(STORES):
        x = 16 + i * (cw + gap)
        body.append(f'<rect class="card" x="{x}" y="{top}" width="{cw}" height="{ch}" rx="8"/>')
        body.append(f'<text class="name" x="{x + 14}" y="{top + 27}">{name}</text>')
        y = top + 44
        for r, (key, val) in enumerate(rows):
            if key == "AUTOMATIC ROTATION":
                body.append(f'<rect class="hl" x="{x + 6}" y="{y - 4}" width="{cw - 12}" height="{row_heights[r] - 2}" rx="6"/>')
            body.append(f'<text class="key" x="{x + 14}" y="{y + 12}">{key}</text>')
            text_lines(body, x + 14, y + 29, wrap(val, 40), cls="lab", dy=16)
            y += row_heights[r]
        desc.append(name + ": " + "; ".join(f"{k.lower()}: {v}" for k, v in rows))
    h = top + ch + 12
    svg("04-05-secrets-vs-parameters.svg", w, h,
        "AWS Secrets Manager compared with Parameter Store",
        "Two cards with the same four rows; the automatic rotation row is highlighted on both. " + ". ".join(desc) + ".",
        body, style=STYLE)


if __name__ == "__main__":
    secrets_vs_parameters()
