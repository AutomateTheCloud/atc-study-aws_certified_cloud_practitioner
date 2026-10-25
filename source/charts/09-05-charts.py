#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 09.05 (compliance and governance) as SVG.

Usage: python3 -I source/charts/09-05-charts.py
Writes images/09-05-*.svg. Facts come from AWS pages checked 2026-10-24: "What is AWS
Artifact?" (AWS's reports and agreements, free; customers produce their own compliance
documents), the Shared Responsibility Model page (security of vs in the cloud), the AWS
Organizations User Guide (what Organizations is; service control policies: maximum
permissions, never grant, limit a member account's root user, don't affect the management
account; general SCP examples, including the Region deny example that exempts global
services), and the AWS Control Tower User Guide (what Control Tower is; how controls work:
preventive controls from SCPs and RCPs, detective controls from AWS Config rules,
proactive controls from CloudFormation hooks). The bakery and its accounts are made up for
teaching. Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Allowed / highlighted = slot 1 (blue) tint; blocked or denied = slot 2 (orange) tint;
# neutral otherwise. Every cell also says what it means in words.
STYLE = make_style(
    light_extra=" --ok-fill:#d9e8fb; --no-fill:#fbe1d6; --n-fill:#f1f0ec;",
    dark_extra=" --ok-fill:#1b3554; --no-fill:#4d2716; --n-fill:#252523;",
    rules_extra="""
  .ok { fill: var(--ok-fill); stroke: var(--s1); stroke-width: 1.5; }
  .no { fill: var(--no-fill); stroke: var(--s2); stroke-width: 1.5; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .zlab { fill: var(--muted); font-size: 12px; }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .key { fill: var(--muted); font-size: 11px; font-weight: 600; letter-spacing: 0.4px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }""")


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


def arrow(body, x1, y1, x2, y2):
    """A straight line with a small filled head at (x2, y2)."""
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


HALVES = [
    ("AWS's controls", "security of the cloud", "n",
     [("EXAMPLES", "Physical security of data centers, hardware, the global network, each service's own infrastructure"),
      ("EVIDENCE", "AWS's audit reports and certificates, such as SOC 2, ISO 27001 and PCI DSS"),
      ("WHERE FROM", "AWS Artifact, free")]),
    ("The bakery's controls", "security in the cloud", "ok",
     [("EXAMPLES", "Its data and where it lives, who has access, how its services are configured, its staff"),
      ("EVIDENCE", "Its own records: CloudTrail activity, AWS Config history and rules, IAM access reports, written policies, training records"),
      ("WHERE FROM", "The bakery itself")]),
]


def two_halves():
    """Big picture: the auditor's question splits into AWS's half and the bakery's half."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Every audit question has an owner</text>',
        '<text class="sub" x="16" y="48">AWS proves its controls; the customer proves its own</text>',
    ]
    rect(body, "plain", 230, 66, 220, 40)
    body.append('<text class="cellt" x="340" y="91" text-anchor="middle">The auditor\'s question</text>')
    cw, gap, top = 316, 16, 132
    xs = [16, 16 + cw + gap]
    arrow(body, 300, 107, xs[0] + cw / 2, top - 2)
    arrow(body, 380, 107, xs[1] + cw / 2, top - 2)
    heights = []
    blocks = []
    for name, sub, cls, rows in HALVES:
        lines = [(k, wrap(v, 44)) for k, v in rows]
        h = 62 + sum(18 + 16 * len(ls) + 8 for _, ls in lines)
        heights.append(h)
        blocks.append((name, sub, cls, lines))
    h = max(heights)
    for x, (name, sub, cls, lines) in zip(xs, blocks):
        rect(body, cls, x, top, cw, h, 8)
        body.append(f'<text class="cellt" x="{x + 14}" y="{top + 26}">{name}</text>')
        body.append(f'<text class="small" x="{x + 14}" y="{top + 44}">{sub}</text>')
        y = top + 70
        for k, ls in lines:
            body.append(f'<text class="key" x="{x + 14}" y="{y}">{k}</text>')
            y = text_lines(body, x + 14, y + 17, ls, cls="small", dy=16) + 8
    y = top + h + 14
    rect(body, "n", 16, y, w - 32, 36, 6)
    body.append(f'<text class="cellt" x="{w / 2}" y="{y + 23}" text-anchor="middle">Compliant only when both halves are covered</text>')
    y += 60
    body.append(f'<text class="note" x="16" y="{y}">From "What is AWS Artifact?" and the Shared Responsibility Model page, checked 2026-10-24. The bakery is made up</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">for teaching.</text>')
    svg("09-05-two-halves.svg", w, y + 30,
        "An auditor's question splits into AWS's half and the bakery's half",
        "At the top, a box labeled the auditor's question, with arrows to two columns. Left column, AWS's "
        "controls, security of the cloud: examples are physical security of data centers, hardware, the global "
        "network and each service's own infrastructure; evidence is AWS's audit reports and certificates, such as "
        "SOC 2, ISO 27001 and PCI DSS; it comes from AWS Artifact, free. Right column, highlighted, the bakery's "
        "controls, security in the cloud: examples are its data and where it lives, who has access, how its "
        "services are configured, and its staff; evidence is its own records, such as CloudTrail activity, AWS "
        "Config history and rules, IAM access reports, written policies and training records; it comes from the "
        "bakery itself. A band across the bottom says: compliant only when both halves are covered.",
        body, style=STYLE)


if __name__ == "__main__":
    two_halves()
