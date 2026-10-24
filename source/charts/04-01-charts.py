#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 04.01 (security of vs in the cloud) as SVG.

Usage: python3 -I source/charts/04-01-charts.py
Writes images/04-01-*.svg. Every cell traces to an AWS statement cited in
guide/04-shared-responsibility-and-access/01-security-of-vs-in-the-cloud.md:
the Shared Responsibility Model page (EC2, S3), the comparison table in the
Amazon RDS User Guide, and the Lambda Developer Guide (what Lambda is, runtimes,
security). Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# AWS = categorical slot 1 (blue), you = slot 2 (orange), from the house palette.
# Cells carry a light tint of the slot with ink text, so the words, not the color,
# say who does the task; the slot color draws the cell border.
STYLE = make_style(
    light_extra=" --aws-fill:#d9e8fb; --you-fill:#fbe1d6; --none-fill:#f1f0ec;",
    dark_extra=" --aws-fill:#1b3554; --you-fill:#4d2716; --none-fill:#252523;",
    rules_extra="""
  .aws { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .you { fill: var(--you-fill); stroke: var(--s2); stroke-width: 1.5; }
  .none { fill: var(--none-fill); stroke: var(--axis); stroke-width: 1; stroke-dasharray: 3 3; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 11.5px; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .rowl { fill: var(--ink); font-size: 12.5px; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .theline { stroke: var(--ink); stroke-width: 3; fill: none; stroke-dasharray: 8 5; stroke-linecap: round; }
  .linelab { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .bracket { stroke: var(--ink2); stroke-width: 1.5; fill: none; }""")


def cell(body, x, y, w, h, who, main, sub=None):
    """A rounded cell: `who` is aws, you or none; main text bold, optional sub line(s)."""
    body.append(f'<rect class="{who}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="5"/>')
    if sub:
        body.append(f'<text class="cellt" x="{x + w / 2:.1f}" y="{y + 18:.1f}" text-anchor="middle">{main}</text>')
        text_lines(body, x + w / 2, y + 33, sub, cls="cells", dy=14, anchor="middle")
    else:
        body.append(f'<text class="cellt" x="{x + w / 2:.1f}" y="{y + h / 2 + 4.5:.1f}" text-anchor="middle">{main}</text>')


def of_and_in():
    """Big picture: the layers, who owns each, and a bakery example beside each."""
    w = 680
    lx, lw = 40, 330          # layer boxes
    ex = lx + lw + 18         # example column
    body = [
        '<text class="title" x="16" y="28">Security of the cloud and security in the cloud</text>',
        '<text class="sub" x="16" y="48">AWS secures the layers below the line; you secure what you put above it</text>',
    ]
    you_layers = [
        ("Your data, and who can reach it", "Orders and cake photos; who may read or change them"),
        ("Your settings and encryption choices", "Firewall rules, storage settings, MFA on your sign-ins"),
        ("Operating system and software you install, on services such as EC2",
         "The web server's operating system and the website software"),
    ]
    aws_layers = [
        ("Software that runs AWS's services: compute, storage, database, networking",
         "What keeps the database service and the storage service running"),
        ("Host operating system and virtualization",
         "The layer that splits one physical machine into many virtual servers"),
        ("Hardware and the global infrastructure: Regions, Availability Zones, edge locations",
         "AWS's buildings, machines, power and cooling"),
    ]
    y = 70
    body.append(f'<text class="head" x="{lx}" y="{y + 12}">Security in the cloud: you</text>')
    body.append(f'<text class="small" x="{ex}" y="{y + 12}">At the bakery, for example</text>')
    y += 24
    top_you = y
    for name, example in you_layers:
        lines = wrap(name, 44)
        h = 20 + 16 * len(lines)
        body.append(f'<rect class="you" x="{lx}" y="{y}" width="{lw}" height="{h}" rx="5"/>')
        text_lines(body, lx + 12, y + 22, lines, cls="rowl", dy=16)
        text_lines(body, ex, y + 18, wrap(example, 36), cls="small", dy=15)
        y += h + 6
    bot_you = y - 6
    body.append(f'<path class="bracket" d="M{lx - 10},{top_you} L{lx - 16},{top_you} L{lx - 16},{bot_you} L{lx - 10},{bot_you}"/>')
    body.append(f'<text class="small" transform="translate({lx - 22},{(top_you + bot_you) / 2:.0f}) rotate(-90)" text-anchor="middle">You</text>')
    ly = y + 30
    body.append(f'<text class="linelab" x="{w - 16}" y="{ly - 12}" text-anchor="end">The line: where it sits depends on the service</text>')
    body.append(f'<line class="theline" x1="16" x2="{w - 16}" y1="{ly}" y2="{ly}"/>')
    y = ly + 16
    body.append(f'<text class="head" x="{lx}" y="{y + 12}">Security of the cloud: AWS</text>')
    y += 24
    top_aws = y
    for name, example in aws_layers:
        lines = wrap(name, 44)
        h = 20 + 16 * len(lines)
        body.append(f'<rect class="aws" x="{lx}" y="{y}" width="{lw}" height="{h}" rx="5"/>')
        text_lines(body, lx + 12, y + 22, lines, cls="rowl", dy=16)
        text_lines(body, ex, y + 18, wrap(example, 36), cls="small", dy=15)
        y += h + 6
    bot_aws = y - 6
    body.append(f'<path class="bracket" d="M{lx - 10},{top_aws} L{lx - 16},{top_aws} L{lx - 16},{bot_aws} L{lx - 10},{bot_aws}"/>')
    body.append(f'<text class="small" transform="translate({lx - 22},{(top_aws + bot_aws) / 2:.0f}) rotate(-90)" text-anchor="middle">AWS</text>')
    y += 16
    body.append(f'<text class="note" x="16" y="{y}">Drawn this way for EC2. On services where AWS runs more for you, such as RDS, Lambda and S3, the line sits higher.</text>')
    h = y + 20
    svg("04-01-of-and-in.svg", w, h,
        "Security of the cloud (AWS) and security in the cloud (you), as layers",
        "Six layers in a stack, split by a dashed line. Above the line, security in the cloud, done by you: "
        "your data and who can reach it (the bakery's orders and cake photos); your settings and encryption "
        "choices (firewall rules, storage settings, MFA); the operating system and software you install on "
        "services such as EC2 (the web server's operating system and website software). The line is labeled: "
        "where it sits depends on the service. Below the line, security of the cloud, done by AWS: the software "
        "that runs AWS's services; the host operating system and virtualization; hardware and the global "
        "infrastructure of Regions, Availability Zones and edge locations. A note says the stack is drawn for "
        "EC2, and that the line sits higher on RDS, Lambda and S3.", body, style=STYLE)


RDS_ROWS = [  # (task, on-premises, EC2, RDS): the RDS User Guide's comparison table, top row first
    ("Application optimization", "you", "you", "you"),
    ("Scaling", "you", "you", "aws"),
    ("High availability", "you", "you", "aws"),
    ("Database backups", "you", "you", "aws"),
    ("Database software patching", "you", "you", "aws"),
    ("Database software install", "you", "you", "aws"),
    ("Operating system patching", "you", "you", "aws"),
    ("Operating system installation", "you", "you", "aws"),
    ("Server maintenance", "you", "aws", "aws"),
    ("Hardware lifecycle", "you", "aws", "aws"),
    ("Power, network and cooling", "you", "aws", "aws"),
]


def who_does_what():
    """The RDS User Guide's three-way comparison, as a grid with the line drawn per column."""
    w = 680
    left, cw, gap, rh = 214, 146, 6, 26
    rg = 8
    cols = ["On-premises", "Database on EC2", "Amazon RDS"]
    body = [
        '<text class="title" x="16" y="28">Who does each database task, in three setups</text>',
        '<text class="sub" x="16" y="48">The line moves up as AWS takes on more. From the Amazon RDS User Guide, checked 2026-10-24.</text>',
    ]
    top = 92
    for i, c in enumerate(cols):
        cx = left + i * (cw + gap) + cw / 2
        body.append(f'<text class="head" x="{cx:.1f}" y="{top - 12}" text-anchor="middle">{c}</text>')
    for r, (task, *who) in enumerate(RDS_ROWS):
        y = top + r * (rh + rg)
        body.append(f'<text class="rowl" x="{left - 12}" y="{y + rh / 2 + 4.5:.1f}" text-anchor="end">{task}</text>')
        for i, wv in enumerate(who):
            x = left + i * (cw + gap)
            cell(body, x, y, cw, rh, wv, "You" if wv == "you" else "AWS")
    # the line in each column: below the last "you" row
    for i in range(3):
        last_you = max([r for r, row in enumerate(RDS_ROWS) if row[1 + i] == "you"], default=-1)
        y = top + (last_you + 1) * (rh + rg) - rg / 2
        x = left + i * (cw + gap)
        body.append(f'<line class="theline" x1="{x - 2}" x2="{x + cw + 2}" y1="{y}" y2="{y}"/>')
    yb = top + len(RDS_ROWS) * (rh + rg) + 10
    counts = [sum(1 for row in RDS_ROWS if row[1 + i] == "aws") for i in range(3)]
    body.append(f'<text class="small" x="{left - 12}" y="{yb + 4}" text-anchor="end">Tasks AWS does</text>')
    for i, n in enumerate(counts):
        cx = left + i * (cw + gap) + cw / 2
        body.append(f'<text class="head" x="{cx:.1f}" y="{yb + 4}" text-anchor="middle">{n} of 11</text>')
    yb += 26
    body.append(f'<text class="note" x="16" y="{yb}">The dashed line marks where your tasks end in each column. Even on RDS, the top row stays yours:</text>')
    body.append(f'<text class="note" x="16" y="{yb + 16}">AWS names it "query tuning", making your database requests run well.</text>')
    h = yb + 32
    svg("04-01-who-does-what.svg", w, h,
        "Who does each database task: on-premises, a database on EC2, and Amazon RDS",
        "A grid of 11 tasks by three setups. On-premises: you do all 11. Database on EC2: AWS does server "
        "maintenance, hardware lifecycle, and power, network and cooling (3 of 11); you do application "
        "optimization, scaling, high availability, database backups, database software patching and install, "
        "and operating system patching and installation. Amazon RDS: AWS does 10 of 11; you keep application "
        "optimization, which AWS calls query tuning. A dashed line in each column marks where your tasks end, "
        "and it moves up from the bottom (on-premises) to near the top (RDS).", body, style=STYLE)


SERVICES = ["Amazon EC2", "Amazon RDS", "AWS Lambda", "Amazon S3"]
LAYERS = [  # layer name, then per service: (who, main, sub lines)
    ("Your data, and who can access it", [
        ("you", "You", ["your data, permissions,", "firewall settings"]),
        ("you", "You", ["your data, who can", "connect"]),
        ("you", "You", ["your data, the", "function's role"]),
        ("you", "You", ["your data, encryption", "options, permissions"]),
    ]),
    ("Your code, and how well it runs", [
        ("you", "You", ["software you install"]),
        ("you", "You", ["query tuning"]),
        ("you", "You", ["your code and the", "libraries it uses"]),
        ("none", "None", ["no code of yours", "runs in S3"]),
    ]),
    ("Platform software: database engine, language runtime", [
        ("you", "You", ["install and patch"]),
        ("aws", "AWS", ["installs and patches"]),
        ("aws", "AWS", ["updates the runtime;", "you leave old ones"]),
        ("aws", "AWS", ["runs the platform"]),
    ]),
    ("Operating system", [
        ("you", "You", ["the guest OS:", "install and patch"]),
        ("aws", "AWS", ["installs and patches"]),
        ("aws", "AWS", ["patches the servers"]),
        ("aws", "AWS", ["runs it"]),
    ]),
    ("Servers, virtualization, hardware", [("aws", "AWS", None)] * 4),
    ("Buildings, power, cooling, network", [("aws", "AWS", None)] * 4),
]
LINE_BELOW = [3, 1, 1, 1]  # index of the last layer each service leaves to you (S3's "none" row sits above the line)
SOURCES = ["Shared Responsibility", "RDS User Guide", "Lambda Developer", "Shared Responsibility"]
SOURCES2 = ["Model page", "", "Guide", "Model page"]


def the_line_moves():
    w = 680
    left, cw, gap = 186, 118, 6
    rg = 10
    body = [
        '<text class="title" x="16" y="28">The line moves with the service</text>',
        '<text class="sub" x="16" y="48">Who does each layer, from AWS\'s own statements for each service (checked 2026-10-24)</text>',
    ]
    top = 90
    for i, s in enumerate(SERVICES):
        cx = left + i * (cw + gap) + cw / 2
        body.append(f'<text class="head" x="{cx:.1f}" y="{top - 12}" text-anchor="middle">{s}</text>')
    y = top
    row_y = []
    for name, cells in LAYERS:
        nsub = max(len(c[2]) if c[2] else 0 for c in cells)
        lab = wrap(name, 26)
        rh = max(26 + 14 * nsub + (6 if nsub else 8), 15 * len(lab) + 10)
        row_y.append((y, rh))
        text_lines(body, left - 12, y + rh / 2 + 4.5 - 7.5 * (len(lab) - 1), lab,
                   cls="rowl", dy=15, anchor="end")
        for i, (who, main, sub) in enumerate(cells):
            cell(body, left + i * (cw + gap), y, cw, rh, who, main, sub)
        y += rh + rg
    # the stepped line: under row LINE_BELOW[i] in column i, joined by verticals
    pts = []
    for i, r in enumerate(LINE_BELOW):
        ry, rh = row_y[r]
        ly = ry + rh + rg / 2
        x0 = left + i * (cw + gap) - (0 if i == 0 else gap / 2)
        x1 = left + i * (cw + gap) + cw + (0 if i == 3 else gap / 2)
        pts.append((x0, ly))
        pts.append((x1, ly))
    d = "M" + " L".join(f"{x:.1f},{yv:.1f}" for x, yv in pts)
    body.append(f'<path class="theline" d="{d}"/>')
    y += 2
    for i in range(4):
        cx = left + i * (cw + gap) + cw / 2
        body.append(f'<text class="note" x="{cx:.1f}" y="{y + 10}" text-anchor="middle">{SOURCES[i]}</text>')
        if SOURCES2[i]:
            body.append(f'<text class="note" x="{cx:.1f}" y="{y + 24}" text-anchor="middle">{SOURCES2[i]}</text>')
    body.append(f'<text class="note" x="{left - 12}" y="{y + 10}" text-anchor="end">Source</text>')
    y += 46
    body.append(f'<text class="small" x="16" y="{y}">The dashed line is lowest on EC2 and higher on the others. The top row never moves: on every</text>')
    body.append(f'<text class="small" x="16" y="{y + 17}">service, your data and who can access it are yours.</text>')
    h = y + 32
    svg("04-01-the-line-moves.svg", w, h,
        "Where the line falls on Amazon EC2, Amazon RDS, AWS Lambda and Amazon S3",
        "A grid of six layers by four services, with a dashed line separating your layers from AWS's. "
        "Your data and who can access it: you, on all four (EC2: your data, permissions and firewall settings; "
        "RDS: your data and who can connect; Lambda: your data and the function's role; S3: your data, encryption "
        "options and permissions). Your code and how well it runs: EC2, software you install; RDS, query tuning; "
        "Lambda, your code and the libraries it uses; S3, none, because no code of yours runs in S3. Platform "
        "software: EC2, you install and patch it; RDS, AWS installs and patches it; Lambda, AWS updates the runtime "
        "and you move off old ones; S3, AWS runs the platform. Operating system: EC2, you install and patch the "
        "guest OS; RDS, AWS; Lambda, AWS patches the servers; S3, AWS. Servers, virtualization and hardware, and "
        "buildings, power, cooling and network: AWS on all four. The line sits below the operating system on EC2, "
        "and below your code on RDS, Lambda and S3. Sources: the Shared Responsibility Model page for EC2 and S3, "
        "the RDS User Guide, and the Lambda Developer Guide.", body, style=STYLE)


if __name__ == "__main__":
    of_and_in()
    who_does_what()
    the_line_moves()
