#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 04.02 (inherited, shared and customer-specific controls) as SVG.

Usage: python3 -I source/charts/04-02-charts.py
Writes images/04-02-*.svg. The three kinds of control and AWS's examples come from
the Shared Responsibility Model page (https://aws.amazon.com/compliance/shared-responsibility-model/),
in our own words; the bakery examples are the lesson's own. Our own design: no AWS
logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Same encoding as the 04.01 graphics: AWS = slot 1 (blue) tint, you = slot 2 (orange)
# tint, ink text on both; an empty part is a dashed outline that says "nothing to do".
STYLE = make_style(
    light_extra=" --aws-fill:#d9e8fb; --you-fill:#fbe1d6; --none-fill:#f1f0ec;",
    dark_extra=" --aws-fill:#1b3554; --you-fill:#4d2716; --none-fill:#252523;",
    rules_extra="""
  .aws { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .you { fill: var(--you-fill); stroke: var(--s2); stroke-width: 1.5; }
  .none { fill: var(--none-fill); stroke: var(--axis); stroke-width: 1; stroke-dasharray: 3 3; }
  .panel { fill: none; stroke: var(--axis); stroke-width: 1; }
  .panel-hi { fill: none; stroke: var(--ink2); stroke-width: 2; }
  .name { fill: var(--ink); font-size: 15px; font-weight: 600; }
  .cellt { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .divider { stroke: var(--ink2); stroke-width: 2; stroke-dasharray: 6 4; }""")


def part(body, x, y, w, h, who, title, lines):
    body.append(f'<rect class="{who}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="5"/>')
    body.append(f'<text class="cellt" x="{x + 10:.1f}" y="{y + 18:.1f}">{title}</text>')
    text_lines(body, x + 10, y + 35, lines, cls="cells", dy=15)


KINDS = [
    ("Inherited", False,
     ("aws", "AWS's part", "All of it"),
     ("none", "Your part", "Nothing to do: you inherit it"),
     "AWS's example: physical and environmental controls.",
     "Bakery: no more locking the server room or keeping it cool."),
    ("Shared", True,
     ("aws", "AWS's part", "Its own half, for the infrastructure"),
     ("you", "Your part", "Your own half, for what you run"),
     "AWS's examples: patch management, configuration management, awareness and training.",
     "Bakery: AWS patches its hosts; the bakery patches its web server."),
    ("Customer-specific", False,
     ("none", "AWS's part", "No counterpart"),
     ("you", "Your part", "All of it"),
     "AWS's example: routing or zoning data within specific security environments.",
     "Bakery: the order database accepts connections only from the web server."),
]


def three_kinds():
    w, pw, gap = 680, 210, 14
    body = [
        '<text class="title" x="16" y="28">Three kinds of control, by who does the work</text>',
        '<text class="sub" x="16" y="48">AWS\'s three groups of IT controls in the shared responsibility model</text>',
    ]
    top, ph = 66, 302
    for i, (name, hi, a, b, aws_ex, bakery) in enumerate(KINDS):
        x = 16 + i * (pw + gap)
        body.append(f'<rect class="{"panel-hi" if hi else "panel"}" x="{x}" y="{top}" width="{pw}" height="{ph}" rx="8"/>')
        body.append(f'<text class="name" x="{x + 14}" y="{top + 28}">{name}</text>')
        y = top + 44
        for who, title, desc in (a, b):
            lines = wrap(desc, 26)
            h = 30 + 15 * len(lines)
            part(body, x + 12, y, pw - 24, h, who, title, lines)
            y += h + 8
        y += 10
        y = text_lines(body, x + 14, y, wrap(aws_ex, 30), cls="small", dy=15)
        text_lines(body, x + 14, y + 8, wrap(bakery, 30), cls="small", dy=15)
    y = top + ph + 22
    body.append(f'<text class="note" x="16" y="{y}">Read each panel top to bottom: does AWS do any of it, and do you? Only the middle one says yes to both,</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">and even there each side works on its own things.</text>')
    h = y + 30
    svg("04-02-three-kinds.svg", w, h,
        "Inherited, shared and customer-specific controls, by who does the work",
        "Three panels. Inherited: AWS's part is all of it; your part is nothing to do, because you inherit it. "
        "AWS's example is physical and environmental controls; for the bakery, no more locking the server room "
        "or keeping it cool. Shared, highlighted: AWS does its own half, for the infrastructure; you do your own "
        "half, for what you run. AWS's examples are patch management, configuration management, and awareness and "
        "training; for the bakery, AWS patches its hosts and the bakery patches its web server. Customer-specific: "
        "AWS has no counterpart; your part is all of it. AWS's example is routing or zoning data within specific "
        "security environments; for the bakery, the order database accepts connections only from the web server.",
        body, style=STYLE)


SHARED = [
    ("Patch management",
     "Patches and fixes flaws in its infrastructure: hosts, virtualization, the services' own software",
     "Patches the guest OS and applications you run. Bakery: the web server's OS and website software; "
     "the libraries in the order functions"),
    ("Configuration management",
     "Configures its own infrastructure devices",
     "Configures your OS, databases, applications and resource settings. Bakery: the web server's "
     "security group; Block Public Access on the photo bucket"),
    ("Awareness and training",
     "Trains AWS employees",
     "Trains your own people. Bakery: the owner, her nephew and the new teammate"),
]


def shared_controls():
    w = 680
    lx, cw = 160, 246
    rx = lx + cw + 18
    body = [
        '<text class="title" x="16" y="28">Shared controls: same kind of work, separate contexts</text>',
        '<text class="sub" x="16" y="48">Each side does its own half. No single task is done by both.</text>',
    ]
    top = 88
    body.append(f'<text class="head" x="{lx + cw / 2:.1f}" y="{top - 12}" text-anchor="middle">AWS does, for its infrastructure</text>')
    body.append(f'<text class="head" x="{rx + cw / 2:.1f}" y="{top - 12}" text-anchor="middle">You do, for what you run</text>')
    y = top
    for name, aws_t, you_t in SHARED:
        al, yl = wrap(aws_t, 34), wrap(you_t, 34)
        h = 20 + 15 * max(len(al), len(yl))
        text_lines(body, lx - 12, y + h / 2 + 4.5 - 7.5 * (len(wrap(name, 16)) - 1), wrap(name, 16),
                   cls="head", dy=15, anchor="end")
        body.append(f'<rect class="aws" x="{lx}" y="{y}" width="{cw}" height="{h}" rx="5"/>')
        text_lines(body, lx + 10, y + 21, al, cls="cells", dy=15)
        body.append(f'<rect class="you" x="{rx}" y="{y}" width="{cw}" height="{h}" rx="5"/>')
        text_lines(body, rx + 10, y + 21, yl, cls="cells", dy=15)
        y += h + 10
    mx = lx + cw + 9
    body.append(f'<line class="divider" x1="{mx}" x2="{mx}" y1="{top - 4}" y2="{y - 6}"/>')
    y += 12
    body.append(f'<text class="small" x="16" y="{y}">The dashed divider is the line from lesson 04.01. A question about one specific task, such as patching</text>')
    body.append(f'<text class="small" x="16" y="{y + 17}">the web server\'s operating system, has one answer: one side. The control as a whole is what is shared.</text>')
    h = y + 32
    svg("04-02-shared-controls.svg", w, h,
        "The three shared controls, with AWS's half and your half of each",
        "Three rows, each split into AWS's half and your half by a dashed divider. Patch management: AWS patches "
        "and fixes flaws in its infrastructure; you patch the guest operating system and applications you run, "
        "such as the bakery's web server and the libraries in its order functions. Configuration management: AWS "
        "configures its own infrastructure devices; you configure your operating systems, databases, applications "
        "and resource settings, such as the web server's security group and Block Public Access on the photo bucket. "
        "Awareness and training: AWS trains AWS employees; you train your own people, such as the owner, her nephew "
        "and the new teammate. A note says a question about one specific task has one answer, one side; the control "
        "as a whole is what is shared.", body, style=STYLE)


if __name__ == "__main__":
    three_kinds()
    shared_controls()
