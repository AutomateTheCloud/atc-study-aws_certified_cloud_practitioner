#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 01.01 (computers and servers) as SVG.

Usage: python3 -I source/charts/01-01-charts.py
Writes images/01-01-*.svg. Facts: the processor carries out instructions and has
cores (AWS, "What is a CPU?"); memory (RAM) is volatile and needs power to hold
data, while storage keeps data without power (AWS, "What is flash memory?");
clients send requests and servers answer them (AWS, "Web server vs application
server"); servers commonly run Linux or Windows Server (Amazon EC2 FAQs). All
checked 2026-10-24. The laptop-versus-server rows are general descriptions of
how the two are usually built. The bakery is made up for teaching. Our own
design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Highlight = slot 1 (blue) tint; everything else neutral. Highlighted items also
# carry words, so color never carries meaning alone.
STYLE = make_style(
    light_extra=" --hi-fill:#d9e8fb; --n-fill:#f1f0ec;",
    dark_extra=" --hi-fill:#1b3554; --n-fill:#252523;",
    rules_extra="""
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 1.8; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .empty { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; stroke-dasharray: 5 4; }
  .frame { fill: none; stroke: var(--ink); stroke-width: 1.8; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .zlab { fill: var(--muted); font-size: 12px; }
  .arrlab { fill: var(--ink2); font-size: 12px; font-style: italic; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }""")


def arrow(body, x1, y1, x2, y2):
    """A straight line with a small filled head at (x2, y2)."""
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


def inside_a_server():
    """Big picture: four hardware parts, the operating system, the applications."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Inside one of the bakery\'s servers</text>',
        '<text class="sub" x="16" y="48">Four hardware parts, the operating system on them, and the programs on top</text>',
    ]
    bx, by, bw = 16, 70, 500
    pad = 12
    # Applications.
    y = by + 34
    body.append(f'<text class="zlab" x="{bx + pad}" y="{y - 8}">Applications</text>')
    aw = (bw - 2 * pad - 10) / 2
    for i, name in enumerate(["The bakery's website", "Order records"]):
        x = bx + pad + i * (aw + 10)
        rect(body, "plain", x, y, aw, 40)
        body.append(f'<text class="cellt" x="{x + aw / 2:.1f}" y="{y + 25}" text-anchor="middle">{name}</text>')
    # Operating system (highlighted).
    y += 72
    body.append(f'<text class="zlab" x="{bx + pad}" y="{y - 8}">Operating system</text>')
    rect(body, "hi", bx + pad, y, bw - 2 * pad, 50)
    body.append(f'<text class="cellt" x="{bx + bw / 2}" y="{y + 21}" text-anchor="middle">Operating system, such as Linux or Windows</text>')
    body.append(f'<text class="small" x="{bx + bw / 2}" y="{y + 39}" text-anchor="middle">shares the parts out to the programs</text>')
    # Hardware.
    y += 82
    body.append(f'<text class="zlab" x="{bx + pad}" y="{y - 8}">Hardware</text>')
    parts = [("Processor", "Does the work"),
             ("Memory", "Holds the work in progress; emptied when the power goes off"),
             ("Storage", "Keeps files and data with the power off"),
             ("Network connection", "Sends and receives data")]
    hw = (bw - 2 * pad - 3 * 8) / 4
    hh = 90
    for i, (name, text) in enumerate(parts):
        x = bx + pad + i * (hw + 8)
        rect(body, "n", x, y, hw, hh)
        title_lines = wrap(name, 11)
        ty = text_lines(body, x + hw / 2, y + 20, title_lines, cls="cellt", dy=15, anchor="middle")
        text_lines(body, x + hw / 2, ty + 2, wrap(text, 16), cls="small", dy=15, anchor="middle")
    net_x = bx + pad + 3 * (hw + 8) + hw
    hy = y
    bh = (y + hh + pad) - by
    rect(body, "frame", bx, by, bw, bh, 10)
    body.append(f'<text class="head" x="{bx + bw - pad}" y="{by + 18}" text-anchor="end">One of the bakery\'s servers</text>')
    # Customers, outside on the right, talking to the network connection.
    cx, cw = 570, 94
    rect(body, "plain", cx, hy + 6, cw, 92)
    text_lines(body, cx + cw / 2, hy + 36, ["Customers'", "phones and", "laptops"], cls="cellt", dy=16, anchor="middle")
    arrow(body, cx - 1, hy + 34, bx + bw + 1, hy + 34)
    arrow(body, bx + bw + 1, hy + 74, cx - 1, hy + 74)
    body.append(f'<text class="arrlab" x="{(bx + bw + cx) / 2:.1f}" y="{hy + 26}" text-anchor="middle">requests</text>')
    body.append(f'<text class="arrlab" x="{(bx + bw + cx) / 2:.1f}" y="{hy + 92}" text-anchor="middle">answers</text>')
    # The network connection sits at the box's right edge.
    body.append(f'<line class="arrow" x1="{net_x:.1f}" y1="{hy + 34}" x2="{bx + bw}" y2="{hy + 34}"/>')
    body.append(f'<line class="arrow" x1="{net_x:.1f}" y1="{hy + 74}" x2="{bx + bw}" y2="{hy + 74}"/>')
    y = by + bh + 26
    body.append(f'<text class="note" x="16" y="{y}">Programs ask the operating system; it uses the hardware for them. The bakery is made up for teaching.</text>')
    svg("01-01-inside-a-server.svg", w, y + 16,
        "The parts of a server: hardware, operating system, applications",
        "A box labeled one of the bakery's servers, in three layers. At the bottom, four hardware parts: processor, "
        "does the work; memory, holds the work in progress and is emptied when the power goes off; storage, keeps "
        "files and data with the power off; network connection, sends and receives data. In the middle, highlighted, "
        "the operating system, such as Linux or Windows, shares the parts out to the programs. At the top, two "
        "applications: the bakery's website and order records. Outside the box on the right, customers' phones and "
        "laptops send requests to the network connection and receive answers.", body, style=STYLE)


def memory_vs_storage():
    """What survives a restart: memory empties, storage keeps."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Memory empties when the power goes off; storage keeps</text>',
        '<text class="sub" x="16" y="48">The same server, while it runs and after a power cut and restart</text>',
    ]
    pw, gap = 300, 48
    top = 74
    mem_items = ["Website program", "Order 1061, being filled in", "Order 1062, being filled in",
                 "Order 1063, being filled in"]
    sto_items = ["Saved order records", "Cake photos", "Operating system"]
    for p, (head, mem) in enumerate([("While the server runs", mem_items), ("After a restart", None)]):
        x = 16 + p * (pw + gap)
        rect(body, "frame", x, top, pw, 330, 10)
        body.append(f'<text class="head" x="{x + 14}" y="{top + 24}">{head}</text>')
        # Memory.
        my = top + 40
        cls = "plain" if mem else "hi"
        rect(body, cls, x + 14, my, pw - 28, 150)
        body.append(f'<text class="cellt" x="{x + 26}" y="{my + 22}">Memory</text>')
        if mem:
            for i, item in enumerate(mem):
                rect(body, "n", x + 26, my + 34 + i * 28, pw - 52, 22, 4)
                body.append(f'<text class="small" x="{x + 36}" y="{my + 50 + i * 28}">{item}</text>')
        else:
            rect(body, "empty", x + 26, my + 34, pw - 52, 106, 4)
            body.append(f'<text class="cellt" x="{x + pw / 2}" y="{my + 84}" text-anchor="middle">Empty</text>')
            body.append(f'<text class="small" x="{x + pw / 2}" y="{my + 102}" text-anchor="middle">orders 1061 to 1063 are lost</text>')
        # Storage.
        sy = my + 166
        rect(body, "plain", x + 14, sy, pw - 28, 112)
        body.append(f'<text class="cellt" x="{x + 26}" y="{sy + 22}">Storage</text>')
        for i, item in enumerate(sto_items):
            rect(body, "n", x + 26, sy + 32 + i * 26, pw - 52, 20, 4)
            body.append(f'<text class="small" x="{x + 36}" y="{sy + 46 + i * 26}">{item}</text>')
    ax = 16 + pw
    arrow(body, ax + 6, top + 165, ax + gap - 6, top + 165)
    text_lines(body, ax + gap / 2, top + 140, ["power", "cut"], cls="arrlab", dy=13, anchor="middle")
    y = top + 330 + 26
    body.append(f'<text class="note" x="16" y="{y}">Programs save to storage so that a restart doesn\'t lose the work. The orders are made up for teaching.</text>')
    svg("01-01-memory-vs-storage.svg", w, y + 16,
        "What a server keeps through a restart",
        "Two panels. While the server runs: memory holds the website program and three orders being filled in, "
        "1061 to 1063; storage holds the saved order records, the cake photos and the operating system. An arrow "
        "labeled power cut leads to the second panel. After a restart: memory, highlighted, is empty and the three "
        "orders are lost; storage still holds the saved order records, the cake photos and the operating system.",
        body, style=STYLE)


def laptop_vs_server():
    """Same four parts, built differently because a server runs all the time for many users."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">A laptop and a server have the same parts, built for different jobs</text>',
        '<text class="sub" x="16" y="48">How each is usually built and kept</text>',
    ]
    rows = [("Used by", "One person at a time", "Many clients at once, over the network"),
            ("Screen and keyboard", "Built in", "Usually none; managed over the network"),
            ("Runs", "Until it sleeps or is switched off", "All the time"),
            ("When a part fails", "One power supply, one disk: it stops", "Often two power supplies and several disks, so one failure doesn't stop it"),
            ("Lives", "On a desk or in a bag", "In a rack in a server room or data center")]
    lx, c1, c2 = 16, 176, 420
    cw1, cw2 = 232, 244
    top = 76
    # Column heads with small drawings.
    # Laptop: a screen and a base.
    rect(body, "n", c1, top, 46, 30, 3)
    body.append(f'<path class="n" d="M{c1 - 6},{top + 34} L{c1 + 52},{top + 34} L{c1 + 46},{top + 40} L{c1},{top + 40} Z"/>')
    body.append(f'<text class="head" x="{c1 + 62}" y="{top + 26}">Laptop</text>')
    # Server: three units stacked in a rack.
    for i in range(3):
        rect(body, "n", c2, top + i * 13, 52, 11, 2)
        body.append(f'<circle cx="{c2 + 44}" cy="{top + i * 13 + 5.5}" r="2" style="fill:var(--ink2)"/>')
    body.append(f'<text class="head" x="{c2 + 66}" y="{top + 26}">Server</text>')
    y = top + 60
    for label, a, b in rows:
        la, lb = wrap(a, 36), wrap(b, 38)
        lines = max(len(la), len(lb), 1)
        h = 14 + 16 * lines
        body.append(f'<line class="grid" x1="16" x2="664" y1="{y:.1f}" y2="{y:.1f}"/>')
        text_lines(body, lx, y + 20, wrap(label, 20), cls="rowl", dy=15)
        text_lines(body, c1, y + 20, la, cls="small", dy=16)
        text_lines(body, c2, y + 20, lb, cls="small", dy=16)
        y += h + 6
    body.append(f'<line class="axis" x1="16" x2="664" y1="{y:.1f}" y2="{y:.1f}"/>')
    y += 10
    rect(body, "hi", 16, y, 648, 44)
    body.append(f'<text class="rowl" x="28" y="{y + 27}">Both</text>')
    body.append(f'<text class="cellt" x="{c1}" y="{y + 27}">A processor, memory, storage and a network connection</text>')
    y += 70
    body.append(f'<text class="note" x="16" y="{y}">Typical builds; models vary. A rack is a tall metal frame that holds many servers.</text>')
    svg("01-01-laptop-vs-server.svg", w, y + 16,
        "A laptop compared with a server",
        "Two columns, laptop and server, on five rows. Used by: one person at a time; many clients at once, over "
        "the network. Screen and keyboard: built in; usually none, managed over the network. Runs: until it sleeps "
        "or is switched off; all the time. When a part fails: one power supply and one disk, so it stops; often two "
        "power supplies and several disks, so one failure doesn't stop it. Lives: on a desk or in a bag; in a rack "
        "in a server room or data center. A highlighted bottom row says both have a processor, memory, storage and "
        "a network connection.", body, style=STYLE)


if __name__ == "__main__":
    inside_a_server()
    memory_vs_storage()
    laptop_vs_server()
