#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphic for Simulation S9 (security findings tour) as SVG.

Usage: python3 -I source/charts/09-08-charts.py
Writes images/09-08-finding-grid.svg: the model answer to Decision 1, eight findings against
the four services that raise them, with what each service read. Facts from AWS documentation,
retrieved 2026-10-24: GuardDuty finding types and their data sources ("GuardDuty finding
types"); Inspector package vulnerability and network reachability findings ("Amazon Inspector
finding types"); Macie sensitive data and policy findings ("Types of Macie findings");
Security Hub CSPM controls EC2.13 and IAM.9 ("Security Hub CSPM controls for Amazon EC2",
"... for IAM"). The findings' details are made up.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg  # noqa: E402

# The marked cell is carried by a thick outline and words, never color alone.
STYLE = make_style(
    light_extra=" --cell:#fcfcfb; --hit:#d9e8fb;",
    dark_extra=" --cell:#1a1a19; --hit:#1b3554;",
    rules_extra="""
  .cell { fill: var(--cell); stroke: var(--grid); stroke-width: 1; }
  .hit { fill: var(--hit); stroke: var(--ink); stroke-width: 2.5; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .rowl { fill: var(--ink); font-size: 12.5px; }
  .rowk { fill: var(--ink); font-size: 12.5px; font-weight: 700; }
  .hitt { fill: var(--ink); font-size: 11.5px; font-weight: 600; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

SERVICES = ["GuardDuty", "Inspector", "Macie", "Security Hub CSPM"]
ROWS = [
    ("A", "Mining domain lookups", 0, "DNS logs"),
    ("B", "Flawed openssl package", 1, "software"),
    ("C", "Personal data in a file", 2, "object contents"),
    ("D", "SSH open to anyone (EC2.13)", 3, "standards check"),
    ("E", "Credentials used outside AWS", 0, "CloudTrail"),
    ("F", "Port 22 reachable from internet", 1, "network paths"),
    ("G", "Block Public Access turned off", 2, "bucket settings"),
    ("H", "Root user has no MFA (IAM.9)", 3, "standards check"),
]


def grid():
    w = 680
    x0, lw, cw, top, rh = 16, 216, 110, 92, 36
    body = [
        '<text class="title" x="16" y="28">Which service raised each finding</text>',
        '<text class="sub" x="16" y="48">The outlined cell names the service and what it read to find the problem</text>',
    ]
    for j, name in enumerate(SERVICES):
        cx = x0 + lw + j * cw + cw / 2
        if name == "Security Hub CSPM":
            body.append(f'<text class="head" x="{cx:.1f}" y="{top - 22}" text-anchor="middle">Security Hub</text>')
            body.append(f'<text class="head" x="{cx:.1f}" y="{top - 7}" text-anchor="middle">CSPM</text>')
        else:
            body.append(f'<text class="head" x="{cx:.1f}" y="{top - 7}" text-anchor="middle">{name}</text>')
    for i, (key, label, hit, read) in enumerate(ROWS):
        y = top + i * rh
        body.append(f'<text class="rowk" x="{x0}" y="{y + 23}">{key}</text>')
        body.append(f'<text class="rowl" x="{x0 + 18}" y="{y + 23}">{label}</text>')
        for j in range(4):
            x = x0 + lw + j * cw
            cls = "hit" if j == hit else "cell"
            body.append(f'<rect class="{cls}" x="{x + 2}" y="{y + 2}" width="{cw - 4}" height="{rh - 4}" rx="4"/>')
            if j == hit:
                body.append(f'<text class="hitt" x="{x + cw / 2:.1f}" y="{y + 23}" text-anchor="middle">{read}</text>')
    yb = top + len(ROWS) * rh + 22
    body.append(f'<text class="note" x="16" y="{yb}">D and F are both about port 22, and C and G both about the photo bucket: '
                'same resource, different service.</text>')
    svg("09-08-finding-grid.svg", w, yb + 18,
        "Eight security findings matched to GuardDuty, Inspector, Macie or Security Hub CSPM",
        "A grid with eight rows and four columns: GuardDuty, Inspector, Macie, Security Hub CSPM. One cell per row "
        "is outlined and says what the service read. A, mining domain lookups: GuardDuty, DNS logs. B, flawed "
        "openssl package: Inspector, software. C, personal data in a file: Macie, object contents. D, SSH open to "
        "anyone (EC2.13): Security Hub CSPM, standards check. E, credentials used outside AWS: GuardDuty, "
        "CloudTrail. F, port 22 reachable from internet: Inspector, network paths. G, Block Public Access turned "
        "off: Macie, bucket settings. H, root user has no MFA (IAM.9): Security Hub CSPM, standards check. A note "
        "says D and F are both about port 22, and C and G both about the photo bucket, yet come from different "
        "services.",
        body, style=STYLE)


if __name__ == "__main__":
    grid()
