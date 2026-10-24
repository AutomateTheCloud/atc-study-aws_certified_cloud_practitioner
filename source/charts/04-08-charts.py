#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the responsibility grid for Simulation S3 (the responsibility slider) as SVG.

Usage: python3 -I source/charts/04-08-charts.py
Writes images/04-08-responsibility-grid.svg. Every cell comes from an AWS-published
statement, cited in guide/04-shared-responsibility-and-access/08-sim-responsibility-slider.md:
the Amazon RDS User Guide's comparison of on-premises, EC2 and RDS management; the
shared responsibility model page (EC2, and S3 as an abstracted service); and the
Lambda developer guide (what Lambda is, runtimes, security). Where those pages publish
no split, the cell says so; never fill one in by guessing.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

COLUMNS = ["On-premises", "EC2", "RDS", "Lambda", "S3"]

# (row label, cells). A cell is (owner, text): owner "aws", "you" or "none".
ROWS = [
    ("Facilities, power, cooling, hardware and servers",
     [("you", "You"), ("aws", "AWS"), ("aws", "AWS"), ("aws", "AWS"), ("aws", "AWS")]),
    ("Operating system: install and patch",
     [("you", "You"), ("you", "You"), ("aws", "AWS"), ("aws", "AWS ¹"), ("aws", "AWS")]),
    ("Database engine or language runtime: install and patch",
     [("you", "You"), ("you", "You"), ("aws", "AWS"), ("aws", "AWS ²"), ("aws", "AWS")]),
    ("Backups, high availability and scaling",
     [("you", "You"), ("you", "You"), ("aws", "AWS"), ("aws", "AWS: scaling ³"), ("none", "Not stated")]),
    ("Your code, its dependencies, and tuning",
     [("you", "You"), ("you", "You"), ("you", "You: tuning"), ("you", "You"), ("none", "No code runs")]),
    ("Your data, its encryption, and who can access it",
     [("you", "You"), ("you", "You"), ("you", "You"), ("you", "You"), ("you", "You")]),
]

NOTES = [
    "¹ For managed runtimes, Lambda applies security updates by default. For functions built as container images, you rebuild from the latest base image.",
    "² Until AWS deprecates the runtime. Moving to a supported runtime is yours.",
    "³ Lambda manages capacity and scaling. The pages we use publish no split for its backups or high availability.",
]

STYLE = make_style(
    light_extra=" --aws:#2a78d6; --you:#eb6834;",
    dark_extra=" --aws:#3987e5; --you:#d95926;",
    rules_extra="""
  .cell { stroke: var(--grid); stroke-width: 1; }
  .c-aws { fill: var(--aws); fill-opacity: 0.16; } .c-you { fill: var(--you); fill-opacity: 0.16; }
  .c-none { fill: var(--surface); }
  .bar-aws { fill: var(--aws); } .bar-you { fill: var(--you); }
  .none-border { fill: none; stroke: var(--muted); stroke-width: 1; stroke-dasharray: 4 3; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .celltext { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .celltext-none { fill: var(--ink2); font-size: 12px; font-style: italic; }
  .small { fill: var(--ink2); font-size: 12px; }""",
)


def responsibility_grid():
    w = 720
    left, top, labw, colw, rowh = 16, 156, 236, 92, 50
    gx = left + labw
    body = [
        '<text class="title" x="16" y="28">The line moves: who does each security task, by service</text>',
        '<text class="sub" x="16" y="48">From AWS-published statements only; a blank AWS page means "not stated", never a guess</text>',
    ]
    # legend: color plus a word, so identity never rests on color alone
    lx, ly = 16, 78
    for cls, label in (("aws", "AWS does it"), ("you", "You (the customer) do it")):
        body.append(f'<rect class="c-{cls}" x="{lx}" y="{ly - 12}" width="16" height="16" rx="3"/>')
        body.append(f'<rect class="bar-{cls}" x="{lx}" y="{ly - 12}" width="4" height="16"/>')
        body.append(f'<text x="{lx + 24}" y="{ly + 1}">{label}</text>')
        lx += 24 + len(label) * 7.2 + 28
    body.append(f'<rect class="none-border" x="{lx}" y="{ly - 12}" width="16" height="16" rx="3"/>')
    body.append(f'<text x="{lx + 24}" y="{ly + 1}">No AWS statement, or not applicable</text>')
    # column heads, with an arrow showing the direction of the slider
    for j, col in enumerate(COLUMNS):
        body.append(f'<text class="head" x="{gx + colw * j + colw / 2:.1f}" y="{top - 12}" text-anchor="middle">{col}</text>')
    ay = top - 36
    body.append(f'<line class="lead" x1="{gx + 8}" x2="{gx + colw * 5 - 8}" y1="{ay}" y2="{ay}"/>')
    body.append(f'<path d="M{gx + colw * 5 - 14},{ay - 4} L{gx + colw * 5 - 8},{ay} L{gx + colw * 5 - 14},{ay + 4}" class="lead" fill="none"/>')
    body.append(f'<text class="small" x="{gx + colw * 2.5:.1f}" y="{ay - 6}" text-anchor="middle">more abstraction: AWS does more of the work</text>')
    for i, (label, cells) in enumerate(ROWS):
        y = top + rowh * i
        lines = wrap(label, 32)
        text_lines(body, left, y + rowh / 2 - 8 * (len(lines) - 1) + 4, lines, cls="lab", dy=16)
        for j, (owner, txt) in enumerate(cells):
            x = gx + colw * j
            tip = f"{label} on {COLUMNS[j]}: {txt.replace('¹', '(note 1)').replace('²', '(note 2)').replace('³', '(note 3)')}"
            body.append(f'<g><title>{tip}</title>')
            body.append(f'<rect class="cell c-{owner}" x="{x + 1}" y="{y + 1}" width="{colw - 2}" height="{rowh - 2}" rx="4"/>')
            if owner == "none":
                body.append(f'<rect class="none-border" x="{x + 3}" y="{y + 3}" width="{colw - 6}" height="{rowh - 6}" rx="4"/>')
                tl = wrap(txt, 12)
                text_lines(body, x + colw / 2, y + rowh / 2 - 7 * (len(tl) - 1) + 4, tl, cls="celltext-none", dy=14, anchor="middle")
            else:
                body.append(f'<rect class="bar-{owner}" x="{x + 1}" y="{y + 1}" width="4" height="{rowh - 2}"/>')
                tl = wrap(txt, 11)
                text_lines(body, x + colw / 2 + 2, y + rowh / 2 - 7 * (len(tl) - 1) + 4, tl, cls="celltext", dy=14, anchor="middle")
            body.append('</g>')
    ny = top + rowh * len(ROWS) + 26
    for note in NOTES:
        ny = text_lines(body, 16, ny, wrap(note, 108), cls="small", dy=16) + 2
    h = int(ny + 8)
    desc = ("A grid with six rows of security tasks and five columns: on-premises, EC2, RDS, Lambda and S3, "
            "in order of more abstraction. Facilities, power, cooling, hardware and servers: you on-premises, AWS "
            "for every service. Operating system install and patch: you on-premises and on EC2; AWS on RDS, Lambda "
            "(note 1) and S3. Database engine or language runtime install and patch: you on-premises and on EC2; "
            "AWS on RDS, Lambda (note 2) and S3. Backups, high availability and scaling: you on-premises and on EC2; "
            "AWS on RDS; on Lambda, AWS for scaling (note 3); on S3, not stated. Your code, its dependencies and "
            "tuning: you everywhere, including query tuning on RDS; on S3 no code runs. Your data, its encryption "
            "and who can access it: you in every column. " + " ".join(NOTES))
    svg("04-08-responsibility-grid.svg", w, h,
        "Who does each security task on-premises and on EC2, RDS, Lambda and S3", desc, body, style=STYLE)


if __name__ == "__main__":
    responsibility_grid()
