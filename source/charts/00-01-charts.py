#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the chart for page 00.01 (welcome: study hours on each path) as SVG.

Usage: python3 -I source/charts/00-01-charts.py
Writes images/00-01-path-hours.svg. The hours are the course plan's estimates
(design/course-plan.md, section 2, "Learner hours"), which hold until the pilot.
Change them there and here together.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg  # noqa: E402

# path, who it is for, estimated hours (before the 3-4 hour guardrails primer)
PATHS = [
    ("Fast path", "already works in IT or with AWS", 25),
    ("Standard path", "most learners", 57),
    ("On-ramp path", "new to IT basics", 62),
]

STYLE = make_style()


def path_hours():
    w, left, top, pw, rowh = 680, 250, 84, 300, 54
    xmax = 70
    h = top + rowh * len(PATHS) + 40
    body = [
        '<text class="title" x="16" y="28">The fast path takes less than half the time of the standard path</text>',
        '<text class="sub" x="16" y="50">Estimated study hours for each path, before the guardrails primer (3 to 4 hours on every path)</text>',
    ]
    ph = rowh * len(PATHS)
    for v in range(0, xmax + 1, 10):
        x = left + pw * v / xmax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 6}" y2="{top + ph - 14}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top + ph + 4}" text-anchor="middle">{v} h</text>')
    for i, (name, who, hours) in enumerate(PATHS):
        y = top + i * rowh
        body.append(f'<text class="lab" x="16" y="{y + 13}">{name}</text>')
        body.append(f'<text x="16" y="{y + 30}">{who}</text>')
        bw = pw * hours / xmax
        body.append(f'<path class="s1" d="{right_rounded(left, y, bw, 22)}"><title>{name}: about {hours} hours</title></path>')
        body.append(f'<text class="lab" x="{left + bw + 8:.1f}" y="{y + 16}">about {hours} h</text>')
    body.append(f'<text class="tick" x="16" y="{h - 12}">Estimates until our pilot. At 5 hours a week: about 6, 12 to 13, and 13 to 14 weeks, including the primer.</text>')
    svg(
        "00-01-path-hours.svg", w, h,
        "Estimated study hours on each path",
        "Horizontal bar chart of estimated study hours, before the guardrails primer. "
        "Fast path, for people who already work in IT or with AWS: about 25 hours. "
        "Standard path, for most learners: about 57 hours. "
        "On-ramp path, for people new to IT basics: about 62 hours. "
        "Every path adds 3 to 4 hours for the guardrails primer.",
        body, STYLE,
    )


if __name__ == "__main__":
    path_hours()
