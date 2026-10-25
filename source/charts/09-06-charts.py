#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 09.06 (a defense map) as SVG.

Usage: python3 -I source/charts/09-06-charts.py
Writes images/09-06-*.svg. The layers and their controls summarize lessons 04.01, 05.02,
06.02, 07.01 to 07.03 and 09.01 to 09.05. Facts come from AWS pages checked 2026-10-24:
the Well-Architected security design principles ("Apply security at all layers"), the
Shared Responsibility Model page, the AWS WAF developer guide (Shield Standard: automatic,
no additional charge, common network and transport layer attacks; WAF: rules on HTTP(S)
requests, rate-based rules; Firewall Manager needs AWS Organizations), the GuardDuty user
guide (threat detection from CloudTrail, VPC Flow Logs and DNS logs), the Macie user guide
(sensitive data and bucket access in S3) and the AWS Organizations user guide (SCPs; an
organization trail member accounts can't turn off). The bakery is made up for teaching.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Stops = slot 1 (blue) tint; finds = slot 2 (orange) tint; limits = neutral.
# Every cell also starts with the word STOPS, FINDS or LIMITS.
STYLE = make_style(
    light_extra=" --ok-fill:#d9e8fb; --no-fill:#fbe1d6; --n-fill:#f1f0ec;",
    dark_extra=" --ok-fill:#1b3554; --no-fill:#4d2716; --n-fill:#252523;",
    rules_extra="""
  .ok { fill: var(--ok-fill); stroke: var(--s1); stroke-width: 1.5; }
  .no { fill: var(--no-fill); stroke: var(--s2); stroke-width: 1.5; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .watch { fill: var(--no-fill); stroke: var(--s2); stroke-width: 2; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .tiny { fill: var(--ink); font-size: 11px; }
  .zlab { fill: var(--muted); font-size: 12px; }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .key { fill: var(--muted); font-size: 10px; font-weight: 700; letter-spacing: 0.5px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }""")


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


LAYERS = [
    ("1  Edge", "where traffic reaches AWS", "Route 53, CloudFront, Shield Standard and Advanced, AWS WAF"),
    ("2  Network", "the bakery's VPC", "Public and private subnets, route tables, network ACLs, security groups"),
    ("3  Compute", "servers and functions", "Patched images and guest operating systems, Amazon Inspector scans"),
    ("4  Data", "what is stored and sent", "Encryption with KMS keys and ACM certificates, S3 Block Public Access and versioning, Macie, backups"),
    ("5  Identity and account", "who can do what", "IAM least privilege, MFA, roles instead of access keys, root user protection"),
    ("6  Organization", "rules over every account", "Separate accounts, SCPs, Control Tower controls, Firewall Manager"),
]
WATCH = ["CloudTrail", "AWS Config", "CloudWatch", "GuardDuty", "Security Hub"]


def defense_map():
    """Big picture: six nested layers, with a 'watch and prove' band across all of them."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">A defense map: six layers, and a watch across all of them</text>',
        '<text class="sub" x="16" y="48">From the internet (top) to the organization (bottom), with the controls at each layer</text>',
    ]
    top = 92
    body.append('<text class="zlab" x="16" y="78">The internet: customers, bots and attackers</text>')
    lx, lw = 16, 500
    bh, gap = 66, 8
    for i, (name, sub, ctrl) in enumerate(LAYERS):
        y = top + i * (bh + gap)
        inset = i * 6
        rect(body, "n", lx + inset, y, lw - 2 * inset, bh, 6)
        body.append(f'<text class="cellt" x="{lx + inset + 12}" y="{y + 22}">{name}</text>')
        body.append(f'<text class="zlab" x="{lx + inset + 12}" y="{y + 40}">{sub}</text>')
        text_lines(body, lx + 206, y + 22, wrap(ctrl, 40), cls="small", dy=15)
    h = len(LAYERS) * (bh + gap) - gap
    wx, ww = 530, 134
    rect(body, "watch", wx, top, ww, h, 8)
    body.append(f'<text class="cellt" x="{wx + ww / 2}" y="{top + 26}" text-anchor="middle">Watch and prove</text>')
    body.append(f'<text class="zlab" x="{wx + ww / 2}" y="{top + 44}" text-anchor="middle">across every layer</text>')
    y = top + 84
    for s in WATCH:
        body.append(f'<text class="cellt" x="{wx + ww / 2}" y="{y}" text-anchor="middle">{s}</text>')
        y += 30
    text_lines(body, wx + ww / 2, y + 10, ["records, findings", "and alarms that", "show what got", "through"], cls="zlab", dy=15, anchor="middle")
    y = top + h + 26
    for line in [
        "Each layer is drawn inside the one above it. Lessons: 07.01 to 07.03 and 09.04 (edge and network),",
        "Module 06 and 09.03 (compute), 05.02 and 09.02 (data), Module 04 and 09.01 (identity and account),",
        "09.05 (organization). The bakery is made up for teaching.",
    ]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg("09-06-defense-map.svg", w, y + 14,
        "Six security layers from the edge to the organization, with a watch across all of them",
        "Six bands, each drawn slightly inside the one above, from the internet at the top to the organization at "
        "the bottom. 1, Edge, where traffic first reaches AWS: Route 53, CloudFront, Shield Standard and Advanced, "
        "AWS WAF. 2, Network, the bakery's VPC: public and private subnets, route tables, network ACLs, security "
        "groups. 3, Compute, servers and functions: patched images and guest operating systems, Amazon Inspector "
        "scans. 4, Data, what is stored and sent: encryption with KMS keys and ACM certificates, S3 Block Public "
        "Access and versioning, Macie, backups. 5, Identity and account, who can do what: IAM least privilege, MFA, "
        "roles instead of access keys, root user protection. 6, Organization, rules over every account: separate "
        "accounts, SCPs, Control Tower controls, Firewall Manager. A highlighted vertical band on the right, "
        "labeled watch and prove across every layer, lists CloudTrail, AWS Config, CloudWatch, GuardDuty and "
        "Security Hub: records, findings and alarms that show what got through.",
        body, style=STYLE)


if __name__ == "__main__":
    defense_map()
