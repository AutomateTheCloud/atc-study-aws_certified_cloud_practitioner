#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the chart for page 00.04 (AWS changes fast: fourteen months of changes) as SVG.

Usage: python3 -I source/charts/00-04-charts.py
Writes images/00-04-changes-timeline.svg. Dates come from the research repo's
docs/10 (names and status, checked 2026-10-23) and docs/00 section 10 (exam guide
revisions). The exam guide revision has no published date; it is placed at the last
archive snapshot that shows it (2026-09-27). Change the page's table and this list together.
"""
import datetime as dt
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

TODAY = dt.date(2026, 10, 24)
START, END = dt.date(2025, 10, 15), dt.date(2027, 1, 20)

EVENTS = [
    (dt.date(2025, 11, 7), "Snowball, Migration Hub and Application Discovery Service close to new customers"),
    (dt.date(2025, 12, 2), "New Support plans; Developer and Business Support take no new customers"),
    (dt.date(2026, 4, 30), "AWS Audit Manager closes to new accounts"),
    (dt.date(2026, 5, 20), "Amazon Inspector Classic shuts down"),
    (dt.date(2026, 7, 30), "Amazon Kendra closes to new customers"),
    (dt.date(2026, 9, 16), "AWS announces a new sign-up experience"),
    (dt.date(2026, 9, 27), "Exam guide revised by this date; still CLF-C02"),
    (dt.date(2026, 10, 29), "WorkSpaces Secure Browser closes to new customers"),
    (dt.date(2026, 12, 31), "Snowball support ends; Italian and German exams retire after this day"),
    (dt.date(2027, 1, 1), "Developer, Business and Enterprise On-Ramp Support plans end"),
]

STYLE = make_style(rules_extra="""
  .spine { stroke: var(--axis); stroke-width: 2; }
  .ring { fill: var(--surface); stroke: var(--s1); stroke-width: 2; }
  .today { stroke: var(--ink); stroke-width: 1.5; }
  .date { fill: var(--ink2); font-size: 12px; font-variant-numeric: tabular-nums; }
  .zone { fill: var(--muted); font-size: 11px; font-weight: 600; letter-spacing: 0.5px; }""")


def changes_timeline():
    w, spine, top, ph = 680, 120, 92, 600
    gap = 36  # minimum vertical space between event labels
    span = (END - START).days

    def ypos(d):
        return top + ph * (d - START).days / span

    body = [
        '<text class="title" x="16" y="28">Ten changes a learner would meet in about fourteen months</text>',
        '<text class="sub" x="16" y="50">Selected AWS renames, closures and plan changes, Nov 2025 to Jan 2027 (checked 2026-10-23)</text>',
        f'<line class="spine" x1="{spine}" x2="{spine}" y1="{top}" y2="{top + ph}"/>',
    ]
    # month ticks on the left of the spine, every quarter
    d = dt.date(2025, 11, 1)
    while d <= END:
        if d.month in (1, 4, 7, 10) or d == dt.date(2025, 11, 1):
            y = ypos(d)
            body.append(f'<line class="axis" x1="{spine - 6}" x2="{spine}" y1="{y:.1f}" y2="{y:.1f}"/>')
            body.append(f'<text class="tick" x="{spine - 10}" y="{y + 4:.1f}" text-anchor="end">{d.strftime("%b %Y")}</text>')
        d = dt.date(d.year + (d.month == 12), d.month % 12 + 1, 1)
    ty = ypos(TODAY)
    body.append(f'<line class="today" x1="{spine - 8}" x2="{w - 16}" y1="{ty:.1f}" y2="{ty:.1f}"/>')
    body.append(f'<text class="zone" x="{w - 16}" y="{ty - 6:.1f}" text-anchor="end">ALREADY HAPPENED ↑</text>')
    body.append(f'<text class="zone" x="{w - 16}" y="{ty + 15:.1f}" text-anchor="end">ANNOUNCED, STILL TO COME ↓</text>')
    body.append(f'<text class="lab" x="16" y="{ty + 4:.1f}">Today</text>')
    body.append(f'<text class="tick" x="16" y="{ty + 20:.1f}">2026-10-24</text>')

    label_x = spine + 28
    last = -1e9
    for when, text in EVENTS:
        y = ypos(when)
        lines = wrap(text, 52)
        ly = max(y + 4, last + gap)
        # keep labels clear of the "today" line
        if when < TODAY and ly + 17 * (len(lines) - 1) > ty - 12:
            ly = ty - 12 - 17 * (len(lines) - 1)
        if when > TODAY and ly - 12 < ty + 24:
            ly = ty + 36
        future = when > TODAY
        cls = "ring" if future else "dot-s1"
        state = "announced" if future else "happened"
        body.append(f'<circle class="{cls}" cx="{spine}" cy="{y:.1f}" r="6"><title>{when.isoformat()}: {text} ({state})</title></circle>')
        body.append(f'<line class="lead" x1="{spine + 8}" x2="{label_x - 4}" y1="{y:.1f}" y2="{ly - 4:.1f}"/>')
        body.append(f'<text class="date" x="{label_x}" y="{ly:.1f}">{when.isoformat()}</text>')
        text_lines(body, label_x + 82, ly, lines, cls="lab")
        last = ly + 17 * (len(lines) - 1)
    h = int(max(top + ph, last) + 40)
    body.append(f'<text class="tick" x="16" y="{h - 10}">Filled dots: already happened. Rings: announced, still to come.</text>')
    svg(
        "00-04-changes-timeline.svg", w, h,
        "Ten AWS changes between November 2025 and January 2027",
        "Vertical timeline with a line marking today, 2026-10-24. Already happened: "
        "2025-11-07 Snowball, Migration Hub and Application Discovery Service close to new customers; "
        "2025-12-02 new Support plans, and Developer and Business Support take no new customers; "
        "2026-04-30 AWS Audit Manager closes to new accounts; 2026-05-20 Amazon Inspector Classic shuts down; "
        "2026-07-30 Amazon Kendra closes to new customers; 2026-09-16 AWS announces a new sign-up experience; "
        "by 2026-09-27 the exam guide is revised, still CLF-C02. Announced, still to come: "
        "2026-10-29 WorkSpaces Secure Browser closes to new customers; 2026-12-31 Snowball support ends, "
        "and the Italian and German exams retire after this day; 2027-01-01 the Developer, Business and "
        "Enterprise On-Ramp Support plans end.",
        body, STYLE,
    )


if __name__ == "__main__":
    changes_timeline()
