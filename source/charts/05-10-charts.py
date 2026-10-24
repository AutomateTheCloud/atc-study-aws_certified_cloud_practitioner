#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for Simulation S6 (Multi-AZ vs read replica vs backups) as SVG.

Usage: python3 -I source/charts/05-10-charts.py
Writes images/05-10-event-grid.svg. (The comparison table the page also shows is
lesson 05.05's images/05-05-three-copies.svg.) Facts from the Amazon RDS User Guide ("Configuring and
managing a Multi-AZ deployment", "Working with DB instance read replicas") and the
Amazon RDS FAQs, checked 2026-10-23: a Multi-AZ DB instance deployment keeps one
synchronous standby that serves no reads and takes over automatically, typically
within one to two minutes, under the same endpoint name; read replicas are
read-only, updated asynchronously (lag varies), reached at their own endpoints and
promoted by hand; automated backups are kept 7 days by default (up to 35) and
restore to any second up to the latest restorable time, typically within the last
five minutes, as a new DB instance. The bakery's events are made up.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --no-fill:#f1f0ec; --ok-fill:#d9e8fb;",
    dark_extra=" --no-fill:#252523; --ok-fill:#1b3554;",
    rules_extra="""
  .no { fill: var(--no-fill); stroke: var(--axis); stroke-width: 1; stroke-dasharray: 3 3; }
  .ok { fill: var(--ok-fill); stroke: var(--s1); stroke-width: 1; }
  .pick { fill: var(--ok-fill); stroke: var(--s2); stroke-width: 3; }
  .head { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .rowl { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .rows { fill: var(--ink2); font-size: 11.5px; }
  .cellt { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 11px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")


COLS = ["Multi-AZ standby", "Read replica", "Automated backups"]
EVENTS = [  # (event, detail, [(state, title, sub) per column])
    ("AZ a loses power", "10:00, a busy Saturday", [
        ("pick", "Solves it", "automatic, 1-2 min"),
        ("ok", "Partly", "manual; may lose writes"),
        ("ok", "Slow", "restore a new database"),
    ]),
    ("Reports slow the site", "month-end, every month", [
        ("no", "No", "standby serves no reads"),
        ("pick", "Solves it", "run reports on it"),
        ("no", "No", "not a live copy"),
    ]),
    ("A wrong DELETE", "15:42, yesterday's orders", [
        ("no", "No", "copies the delete at once"),
        ("no", "No", "copies it shortly after"),
        ("pick", "Solves it", "restore to 15:41"),
    ]),
    ("The Region is down", "all of US East (N. Virginia)", [
        ("no", "No", "both AZs are in the Region"),
        ("ok", "Only if", "it's in another Region"),
        ("ok", "Only if", "copied to another Region"),
    ]),
]


def event_grid():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Which copy saves the bakery from each event?</text>',
        '<text class="sub" x="16" y="48">Model answer to Part 1. Events are made up; the behaviors are RDS\'s.</text>',
    ]
    left, top, cw, ch, gap = 176, 112, 160, 56, 6
    for j, name in enumerate(COLS):
        cx = left + j * (cw + gap) + cw / 2
        text_lines(body, cx, top - 32, wrap(name, 20), cls="head", dy=15, anchor="middle")
    for i, (ev, det, cells) in enumerate(EVENTS):
        y = top + i * (ch + gap)
        body.append(f'<text class="rowl" x="16" y="{y + 24}">{ev}</text>')
        body.append(f'<text class="rows" x="16" y="{y + 41}">{det}</text>')
        for j, (state, t, s) in enumerate(cells):
            x = left + j * (cw + gap)
            body.append(f'<rect class="{state}" x="{x}" y="{y}" width="{cw}" height="{ch}" rx="5"/>')
            body.append(f'<text class="cellt" x="{x + cw / 2}" y="{y + 23}" text-anchor="middle">{t}</text>')
            body.append(f'<text class="cells" x="{x + cw / 2}" y="{y + 40}" text-anchor="middle">{s}</text>')
    y = top + len(EVENTS) * (ch + gap) + 14
    body.append(f'<text class="note" x="16" y="{y}">Thick outline: the copy that solves it. Dashed: doesn\'t help. Thin: helps partly, or only if set up for it.</text>')
    svg("05-10-event-grid.svg", w, y + 16,
        "Which RDS copy protects the bakery from each of four events",
        "A grid of four made-up events against three kinds of copy. AZ a loses power: the Multi-AZ standby "
        "solves it, automatically in one to two minutes; a read replica helps partly, because you promote it by "
        "hand (manual) and may lose writes; automated backups are slow, because you restore a new database. Reports slow "
        "the site: the standby doesn't help because it serves no reads; a read replica solves it, by running the "
        "reports; backups don't help, because they aren't a live copy. A wrong DELETE at 15:42: the standby "
        "copies the delete at once and the replica shortly after, so neither helps; automated backups solve it "
        "by restoring to 15:41. The whole Region is down: the standby doesn't help, because both AZs are in the "
        "Region; a read replica helps only if it is in another Region; backups help only if copied to another "
        "Region.", body, style=STYLE)


if __name__ == "__main__":
    event_grid()
