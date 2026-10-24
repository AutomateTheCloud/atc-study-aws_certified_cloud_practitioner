#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the chart for Lab 07 (a Lambda function and its logs) as SVG.

Usage: python3 -I source/charts/06-05-charts.py
Writes images/06-05-log-retention.svg. The log volumes are made-up teaching
figures from guide/06-running-applications/05-lab-07-a-lambda-function.md;
change them here and rerun when the lab changes.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg  # noqa: E402

GB_PER_MONTH = 0.5  # made-up: logs the bakery's functions write each month
WEEK_SHARE = 7 / 30  # with 1-week retention, about a week's logs are kept

STYLE = make_style(rules_extra="""
  .line-s2 { stroke: var(--s2); stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .dot-s2 { fill: var(--s2); stroke: var(--surface); stroke-width: 2; }""")


def log_retention():
    months = list(range(1, 13))
    forever = [GB_PER_MONTH * m for m in months]
    week = [round(GB_PER_MONTH * WEEK_SHARE, 2) for _ in months]
    assert forever[-1] == 6.0, "must match the lab text"
    w, h, left, top, pw, ph, ymax = 680, 400, 56, 112, 470, 236, 7
    body = [
        '<text class="title" x="16" y="28">Logs kept forever pile up; logs kept a week don\'t</text>',
        '<text class="sub" x="16" y="48">Log data stored at the end of each month, if the functions write 0.5 GB a month (made-up figures)</text>',
    ]
    # legend
    body.append('<line class="line-s1" x1="16" x2="32" y1="72" y2="72"/><text x="38" y="76">Retention: never expire (the default)</text>')
    body.append('<line class="line-s2" x1="300" x2="316" y1="72" y2="72"/><text x="322" y="76">Retention: 1 week</text>')
    for v in range(0, ymax + 1):
        y = top + ph - ph * v / ymax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{y:.1f}" y2="{y:.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{y + 4:.1f}" text-anchor="end">{v}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 14}">GB stored</text>')
    step = pw / (len(months) - 1)
    for i, m in enumerate(months):
        body.append(f'<text class="tick" x="{left + step * i:.1f}" y="{top + ph + 18}" text-anchor="middle">{m}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2:.1f}" y="{top + ph + 38}" text-anchor="middle">Month</text>')

    def pts(vals):
        return " ".join(f"{left + step * i:.1f},{top + ph - ph * v / ymax:.1f}" for i, v in enumerate(vals))

    body.append(f'<polyline class="line-s1" points="{pts(forever)}"/>')
    body.append(f'<polyline class="line-s2" points="{pts(week)}"/>')
    for i, (a, b) in enumerate(zip(forever, week)):
        x = left + step * i
        body.append(f'<circle class="dot-s1" cx="{x:.1f}" cy="{top + ph - ph * a / ymax:.1f}" r="4"><title>Month {i + 1}, never expire: {a:.1f} GB</title></circle>')
        body.append(f'<circle class="dot-s2" cx="{x:.1f}" cy="{top + ph - ph * b / ymax:.1f}" r="4"><title>Month {i + 1}, 1 week: about {b:.2f} GB</title></circle>')
    xe = left + pw + 10
    body.append(f'<text class="lab" x="{xe}" y="{top + ph - ph * forever[-1] / ymax + 4:.1f}">6 GB, still growing</text>')
    body.append(f'<text class="lab" x="{xe}" y="{top + ph - ph * week[-1] / ymax - 6:.1f}">about 0.1 GB,</text>')
    body.append(f'<text class="lab" x="{xe}" y="{top + ph - ph * week[-1] / ymax + 10:.1f}">flat</text>')
    svg("06-05-log-retention.svg", w, h,
        "Stored log data over a year: never expire against one-week retention",
        "Line chart, made-up figures, months 1 to 12, functions writing 0.5 GB of logs a month. "
        "With retention set to never expire, stored logs grow by 0.5 GB every month, to 6 GB at month 12, and keep growing. "
        "With retention set to one week, stored logs stay flat at about 0.1 GB.",
        body, style=STYLE)


if __name__ == "__main__":
    log_retention()
