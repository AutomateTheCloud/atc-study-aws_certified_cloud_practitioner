#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 04.05 (credentials and federation) as SVG.

Usage: python3 -I source/charts/04-05-charts.py
Writes images/04-05-*.svg. Durations come from the IAM User Guide (access keys, password
policy), the AWS CLI guide and AWS Security Blog post on `aws login`, and the CloudShell
quotas page; the Secrets Manager and Parameter Store facts from their docs and the Secrets
Manager pricing page. All checked 2026-10-23. Our own design: no AWS logos, icons or trade dress.
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

# label, credential kind, hours shown (None = never ends), note
ROWS = [
    ("Access key on an IAM user", "long", None, "No end: works until someone deletes it"),
    ("IAM user password, default policy", "long", None, "No end: the default never expires it"),
    ("aws login on your computer", "temp", 12, "Renewed every 15 minutes, for up to 12 hours"),
    ("CloudShell session", "temp", 12, "About 12 hours at most; ends after 20 to 30 idle minutes"),
]


def credential_lifetimes():
    w, left, right = 680, 236, 600
    top, bar_h, row_h = 92, 18, 58
    pw = right - left
    hmax = 24
    body = [
        '<text class="title" x="16" y="28">How long a credential keeps working, once issued</text>',
        '<text class="sub" x="16" y="48">Hours, over one day. Long-term credentials run off the end of the chart.</text>',
    ]
    swatch(body, 16, 74, "s2", "Long-term")
    swatch(body, 112, 74, "s1", "Temporary")
    ph = row_h * len(ROWS)
    for v in range(0, hmax + 1, 6):
        x = left + pw * v / hmax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top}" y2="{top + ph}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top + ph + 18}" text-anchor="middle">{v} h</text>')
    desc = []
    for i, (label, kind, hours, note) in enumerate(ROWS):
        y = top + i * row_h + 10
        body.append(f'<text class="lab" x="{left - 10}" y="{y + 13}" text-anchor="end">{label}</text>')
        cls = "s2" if kind == "long" else "s1"
        if hours is None:
            bw = pw + 30
            body.append(f'<path class="{cls}" d="{right_rounded(left, y, bw - 12, bar_h, 0)}"/>')
            ax = left + bw - 12
            body.append(f'<path class="arrow-s2" d="M{ax:.1f},{y - 4} L{ax + 14:.1f},{y + bar_h / 2} L{ax:.1f},{y + bar_h + 4} Z"/>')
        else:
            bw = pw * hours / hmax
            body.append(f'<path class="{cls}" d="{right_rounded(left, y, bw, bar_h)}"/>')
        body.append(f'<text class="small" x="{left}" y="{y + bar_h + 16}">{note}</text>')
        desc.append(f"{label}: {'long-term' if kind == 'long' else 'temporary'}; {note.lower()}")
    h = top + ph + 34
    svg("04-05-credential-lifetimes.svg", w, h,
        "How long four kinds of credential keep working",
        "Horizontal bars on an axis from 0 to 24 hours. " + "; ".join(desc) + ". The two long-term bars run past the "
        "right edge with an arrow; the two temporary bars stop at 12 hours.", body, style=STYLE)


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
    credential_lifetimes()
    secrets_vs_parameters()
