#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 08.01 (four ways in) as SVG.

Usage: python3 -I source/charts/08-01-charts.py
Writes images/08-01-four-ways.svg. Facts come from AWS's pages, checked
2026-10-24: "What is the AWS Management Console?", "What is the AWS CLI?" (the
CLI gives access to the public APIs and lets you write shell scripts), the AWS
SDKs and Tools Reference Guide (SDKs sign requests, retry, and find credentials
such as a role's on their own), and "What is CloudFormation?" (a template
describes the resources; a stack is managed as one unit; templates are reused
across Regions). The "clue words" row is our own teaching summary. Our own
design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# The highlighted row uses the slot 1 (blue) tint; every other cell is neutral.
STYLE = make_style(
    light_extra=" --ok-fill:#d9e8fb; --n-fill:#f1f0ec;",
    dark_extra=" --ok-fill:#1b3554; --n-fill:#252523;",
    rules_extra="""
  .ok { fill: var(--ok-fill); stroke: var(--s1); stroke-width: 1.5; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

COLS = [
    ("Console", [
        "Clicking through pages in a web browser",
        "Seeing what exists, learning, and tasks done once",
        "No: the steps live in someone's memory",
        "visual, browser, one-time",
    ]),
    ("AWS CLI", [
        "Typing commands; saving them as a script",
        "Quick or bulk tasks from a terminal, such as CloudShell",
        "Yes, if saved as a script; it repeats steps, not the end state",
        "command line, terminal, script",
    ]),
    ("AWS SDKs", [
        "Calls written inside your program's code",
        "Applications that use AWS while they run",
        "Yes: the program makes the same calls every time it runs",
        "application code, programming language",
    ]),
    ("Infrastructure as code", [
        "A template file that describes the end state",
        "Building, changing and copying whole setups",
        "Yes: the same file builds the same setup, anywhere",
        "template, repeatable, identical environments",
    ]),
]
ROWS = ["How you work", "Best for", "Repeatable?", "Exam clue words"]
HIGHLIGHT = "Repeatable?"


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


def four_ways():
    """Comparison panels: the four ways in, with the 'Repeatable?' row highlighted."""
    w = 770
    body = [
        '<text class="title" x="16" y="28">Four ways into AWS, compared</text>',
        '<text class="sub" x="16" y="48">All four send requests to the same AWS APIs; read across a row to see how they differ</text>',
    ]
    lw, cw, gap = 100, 156, 6
    xs = [16 + lw + i * (cw + gap) for i in range(4)]
    y = 66
    for x, (name, _) in zip(xs, COLS):
        rect(body, "n", x, y, cw, 32)
        body.append(f'<text class="cellt" x="{x + 8}" y="{y + 21}">{name}</text>')
    y += 40
    right = xs[-1] + cw
    for r, row in enumerate(ROWS):
        cells = [wrap(c[1][r], 20 if row == HIGHLIGHT else 23) for c in COLS]
        h = 14 + 15 * max(len(c) for c in cells) + 4
        if row == HIGHLIGHT:
            for x in xs:
                rect(body, "ok", x - 3, y + 2, cw + 6, h - 4, 5)
        body.append(f'<line class="grid" x1="16" x2="{right}" y1="{y}" y2="{y}"/>')
        text_lines(body, 16, y + 19, wrap(row, 14), cls="rowl", dy=15)
        for x, c in zip(xs, cells):
            text_lines(body, x + 8, y + 19, c, cls="cellt" if row == HIGHLIGHT else "small", dy=15)
        y += h
    body.append(f'<line class="grid" x1="16" x2="{right}" y1="{y}" y2="{y}"/>')
    y += 22
    body.append(f'<text class="note" x="16" y="{y}">On AWS, the infrastructure as code service is AWS CloudFormation (lesson 08.02). AWS CloudShell is a place to run the CLI.</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">From AWS\'s console, CLI, SDK and CloudFormation documentation, checked 2026-10-24. Clue words are our summary.</text>')
    desc = ("Four columns, the AWS Management Console, the AWS CLI, the AWS SDKs and infrastructure as code, compared "
            "on four rows. How you work: clicking through pages in a web browser; typing commands and saving them as "
            "a script; calls written inside your program's code; a template file that describes the end state. Best "
            "for: seeing what exists, learning, and tasks done once; quick or bulk tasks from a terminal such as "
            "CloudShell; applications that use AWS while they run; building, changing and copying whole setups. "
            "Repeatable, highlighted: no, the steps live in someone's memory; yes if saved as a script, which repeats "
            "steps, not the end state; yes, the program makes the same calls every time it runs; yes, the same file "
            "builds the same setup anywhere. Exam clue words: visual, browser, one-time; command line, terminal, "
            "script; application code, programming language; template, repeatable, identical environments. Notes: "
            "on AWS the infrastructure as code service is AWS CloudFormation; AWS CloudShell is a place to run the CLI.")
    svg("08-01-four-ways.svg", w, y + 30, "The four ways into AWS compared", desc, body, style=STYLE)


if __name__ == "__main__":
    four_ways()
