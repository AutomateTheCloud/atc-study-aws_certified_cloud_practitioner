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


def vm_vs_container():
    """Side by side: virtual machines each carry an OS; containers share one."""
    w, h = 680, 420
    body = [
        '<text class="title" x="16" y="28">Virtual machines and containers</text>',
        '<text class="sub" x="16" y="48">Both share one physical server; they differ in what each copy carries</text>',
    ]
    pw, gap, x0, top = 316, 16, 16, 70
    panels = [
        ("Virtual machines", [("you", "App A"), ("you", "App B")], True,
         [("aws", "Hypervisor")],
         ["Each one carries its own operating system", "Behaves like a whole computer",
          "Amazon EC2 rents these (Module 06)"]),
        ("Containers", [("you", "App A + its libraries"), ("you", "App B + its libraries")], False,
         [("aws", "One shared operating system")],
         ["Each one is an app and what it depends on", "No operating system of its own, so lighter",
          "Lesson 06.03 covers them on AWS"]),
    ]
    for i, (title, apps, own_os, mid, notes) in enumerate(panels):
        px = x0 + i * (pw + gap)
        body.append(f'<rect class="frame" x="{px}" y="{top}" width="{pw}" height="{h - top - 16}" rx="8"/>')
        body.append(f'<text class="head" x="{px + 14}" y="{top + 24}">{title}</text>')
        bw = (pw - 42) / 2
        y = top + 38
        for j, (cls, label) in enumerate(apps):
            bx = px + 14 + j * (bw + 14)
            hh = 96 if own_os else 50
            body.append(f'<rect class="frame" x="{bx - 3}" y="{y - 3}" width="{bw + 6}" height="{hh + 6}" rx="6"/>')
            cell(body, bx, y, bw, 44, cls, label if own_os else label.split(" + ")[0],
                 None if own_os else ["+ its libraries"])
            if own_os:
                cell(body, bx, y + 52, bw, 44, cls, "Its own OS")
        if not own_os:
            body.append(f'<text class="note" x="{px + pw / 2}" y="{y + 80}" text-anchor="middle">'
                        'No operating system inside each container</text>')
        y += 108
        for cls, label in mid:
            cell(body, px + 14, y, pw - 28, 40, cls, label)
        y += 48
        cell(body, px + 14, y, pw - 28, 40, "aws", "Physical server")
        y += 66
        for n in notes:
            body.append(f'<text class="small" x="{px + 14}" y="{y}">• {n}</text>')
            y += 20
    svg("01-04-vm-vs-container.svg", w, h,
        "Virtual machines compared with containers",
        "Two panels. Virtual machines: two boxes, app A and app B, each with its own operating system, on a hypervisor, "
        "on a physical server. Notes: each one carries its own operating system; it behaves like a whole computer; "
        "Amazon EC2 rents these (Module 06). Containers: two boxes, app A and app B, each with its libraries and no "
        "operating system of its own, on one shared operating system, on a physical server. Notes: each one is an app "
        "and what it depends on; no operating system of its own, so lighter; lesson 06.03 covers them on AWS.",
        body, style=STYLE)


if __name__ == "__main__":
    stack()
    vm_vs_container()
