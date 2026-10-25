#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 01.04 (data centers and virtualization) as SVG.

Usage: python3 -I source/charts/01-04-charts.py
Writes images/01-04-*.svg. The layers follow the lesson's sources: "What is
virtualization?" (AWS), the Shared Responsibility Model page (host operating system
and virtualization layer on AWS's side), and the EC2 Dedicated Instances page
(default tenancy is shared hardware). Our own design: no AWS logos, icons, trade
dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Provider's layers = slot 1 (blue), the customer's = slot 2 (orange), as in 04.01.
STYLE = make_style(
    light_extra=" --aws-fill:#d9e8fb; --you-fill:#fbe1d6; --none-fill:#f1f0ec;",
    dark_extra=" --aws-fill:#1b3554; --you-fill:#4d2716; --none-fill:#252523;",
    rules_extra="""
  .aws { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .you { fill: var(--you-fill); stroke: var(--s2); stroke-width: 1.5; }
  .other { fill: var(--none-fill); stroke: var(--axis); stroke-width: 1.5; stroke-dasharray: 4 3; }
  .hl { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 3; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 11.5px; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .frame { fill: none; stroke: var(--axis); stroke-width: 1; }
  .theline { stroke: var(--ink); stroke-width: 2.5; fill: none; stroke-dasharray: 8 5; stroke-linecap: round; }
  .linelab { fill: var(--ink); font-size: 12.5px; font-weight: 600; }""")


def cell(body, x, y, w, h, cls, main, sub=None):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="5"/>')
    if sub:
        body.append(f'<text class="cellt" x="{x + w / 2:.1f}" y="{y + 18:.1f}" text-anchor="middle">{main}</text>')
        text_lines(body, x + w / 2, y + 33, sub, cls="cells", dy=14, anchor="middle")
    else:
        body.append(f'<text class="cellt" x="{x + w / 2:.1f}" y="{y + h / 2 + 4.5:.1f}" text-anchor="middle">{main}</text>')


def stack():
    """One physical server split into three virtual servers, with the EC2 responsibility line."""
    w, h = 680, 470
    body = [
        '<text class="title" x="16" y="28">One physical server, three virtual servers</text>',
        '<text class="sub" x="16" y="48">The hypervisor shares out the hardware and keeps each virtual server apart</text>',
    ]
    x0, cw, gap = 24, 196, 12
    vms = [
        ("you", "Virtual server 1", "Linux", "The bakery's website"),
        ("you", "Virtual server 2", "Linux", "The bakery's order database"),
        ("other", "Virtual server 3", "Windows", "Another customer's app"),
    ]
    top = 74
    for i, (cls, name, os_name, app) in enumerate(vms):
        x = x0 + i * (cw + gap)
        body.append(f'<rect class="frame" x="{x - 4}" y="{top}" width="{cw + 8}" height="180" rx="8"/>')
        body.append(f'<text class="head" x="{x + cw / 2}" y="{top + 20}" text-anchor="middle">{name}</text>')
        cell(body, x + 6, top + 32, cw - 12, 58, cls, "Application", wrap(app, 26))
        cell(body, x + 6, top + 100, cw - 12, 58, cls, "Guest operating system", [os_name])
    total = 3 * cw + 2 * gap
    ly = top + 196
    body.append(f'<line class="theline" x1="{x0 - 8}" x2="{x0 + total + 8}" y1="{ly}" y2="{ly}"/>')
    body.append(f'<text class="linelab" x="{x0}" y="{ly + 20}">On a cloud server such as Amazon EC2: the customer runs what is above the line,</text>')
    body.append(f'<text class="linelab" x="{x0}" y="{ly + 37}">the provider runs everything below it</text>')
    hy = ly + 52
    cell(body, x0, hy, total, 52, "hl", "Hypervisor (the virtualization layer)",
         ["Gives each virtual server its share of processor, memory and disk, and keeps them apart"])
    cell(body, x0, hy + 62, total, 52, "aws", "Physical server (the host)",
         ["Processors, memory, disks and network card, in a rack in a data center"])
    text_lines(body, 16, h - 12, ["Solid orange: the bakery's virtual servers. Dashed gray: another customer's, on the same host."], cls="note")
    svg("01-04-virtualization-stack.svg", w, h,
        "One physical server split into three virtual servers by a hypervisor",
        "Bottom to top. A physical server, the host: processors, memory, disks and network card, in a rack in a data "
        "center. On it, highlighted, the hypervisor, the virtualization layer, which gives each virtual server its "
        "share of processor, memory and disk and keeps them apart. A dashed line sits above the hypervisor: on a cloud "
        "server such as Amazon EC2, the customer runs what is above the line and the provider runs everything below it. "
        "Above the line, three virtual servers side by side, each with a guest operating system and an application: "
        "virtual server 1, Linux, the bakery's website; virtual server 2, Linux, the bakery's order database; virtual "
        "server 3, Windows, another customer's app, drawn dashed to show it belongs to someone else on the same host.",
        body, style=STYLE)


if __name__ == "__main__":
    stack()
