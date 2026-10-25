#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 05.05 (managed or self-managed databases) as SVG.

Usage: python3 -I source/charts/05-05-charts.py
Writes images/05-05-*.svg. Facts come from the Amazon RDS User Guide ("What is
Amazon RDS?", Multi-AZ deployments, read replicas) and the Amazon RDS FAQ, checked
2026-10-23: a Multi-AZ DB instance deployment keeps one synchronous standby in
another AZ of the same Region that serves no reads; failover is automatic, flips
the DB instance's DNS name to the standby and typically completes in one to two
minutes; read replicas are asynchronous, serve reads, can lag, and can be promoted
by hand; automated backups (daily snapshot plus transaction logs, 7-day default
retention, up to 35 days) and manual DB snapshots are stored in S3 and restore to
a new DB instance. The bakery is made up for teaching. Our own design: no AWS
logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# The primary (takes writes) = slot 1 (blue) tint; copies = neutral; the failed
# AZ = slot 2 (orange) outline, always labeled "failed". Words carry every meaning.
STYLE = make_style(
    light_extra=" --pri-fill:#d9e8fb; --copy-fill:#f1f0ec; --bad-fill:#fbe1d6;",
    dark_extra=" --pri-fill:#1b3554; --copy-fill:#252523; --bad-fill:#4d2716;",
    rules_extra="""
  .pri { fill: var(--pri-fill); stroke: var(--s1); stroke-width: 1.5; }
  .copy { fill: var(--copy-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .bad { fill: var(--bad-fill); stroke: var(--s2); stroke-width: 1.5; stroke-dasharray: 5 4; }
  .zone { fill: none; stroke: var(--axis); stroke-width: 1.5; stroke-dasharray: 6 4; }
  .region { fill: none; stroke: var(--ink2); stroke-width: 1.2; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .zlab { fill: var(--muted); font-size: 12px; }
  .small { fill: var(--ink2); font-size: 12px; }
  .q { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .arrlab { fill: var(--ink2); font-size: 11.5px; font-style: italic; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .num { fill: var(--ink); font-size: 14px; font-weight: 700; }
  .numc { fill: var(--surface); stroke: var(--ink); stroke-width: 1.5; }""")


def arrow(body, x1, y1, x2, y2, dashed=False):
    """A straight line with a small filled head at (x2, y2), any direction."""
    import math
    dash = ' stroke-dasharray="5 4"' if dashed else ""
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"{dash}/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def box(body, cls, x, y, w, h, title, lines, chars):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="6"/>')
    yy = text_lines(body, x + 10, y + 19, wrap(title, chars), cls="cellt", dy=16)
    text_lines(body, x + 10, yy + 1, [ln for t in lines for ln in wrap(t, chars + 3)], cls="cells", dy=15)


ROWS = ["How it's copied", "Answers queries?", "Takes over by itself?", "Saves you from a mistaken delete?", "The job"]
COLS = [
    ("Multi-AZ standby",
     ["Every write, synchronously, to another AZ",
      "No (a Multi-AZ DB instance's standby serves nothing)",
      "Yes: automatic failover, typically 1 to 2 minutes",
      "No: the delete reaches it at once",
      "High availability"]),
    ("Read replica",
     ["Changes, asynchronously; it can lag behind",
      "Yes, read-only queries",
      "No: you can promote it by hand, losing any lag",
      "No: the delete reaches it soon after",
      "Read scaling (and a disaster recovery option)"]),
    ("Automated backups and snapshots",
     ["A daily snapshot plus a log of every change; snapshots when you take them",
      "No: you restore it to a new database first",
      "No: a restore is a new database you switch to",
      "Yes: restore to a moment before the mistake",
      "Going back in time (backup)"]),
]


def three_copies():
    """Comparison panels: Multi-AZ standby vs read replica vs backups and snapshots."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Standby, read replica, backup: same data, different jobs</text>',
        '<text class="sub" x="16" y="48">Read down a column to see what each copy can and can\'t do for you</text>',
    ]
    lw = 132
    cw, gap = 168, 6
    xs = [16 + lw + i * (cw + gap) for i in range(3)]
    y = 66
    for x, (name, _) in zip(xs, COLS):
        body.append(f'<rect class="pri" x="{x}" y="{y}" width="{cw}" height="44" rx="6"/>')
        text_lines(body, x + 10, y + 18, wrap(name, 19), cls="cellt", dy=16)
    y += 52
    for r, row in enumerate(ROWS):
        cells = [wrap(c[1][r], 24) for c in COLS]
        rl = wrap(row, 18)
        h = 12 + 15 * max(max(len(c) for c in cells), len(rl)) + 6
        body.append(f'<line class="grid" x1="16" x2="{xs[2] + cw}" y1="{y}" y2="{y}"/>')
        text_lines(body, 16, y + 19, rl, cls="rowl", dy=15)
        for x, c in zip(xs, cells):
            text_lines(body, x + 10, y + 19, c, cls="cellt" if r == len(ROWS) - 1 else "small", dy=15)
        y += h
    body.append(f'<line class="grid" x1="16" x2="{xs[2] + cw}" y1="{y}" y2="{y}"/>')
    y += 22
    body.append(f'<text class="note" x="16" y="{y}">For RDS engines other than Aurora. In Aurora, a read replica can also be the failover target.</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">From the Amazon RDS User Guide and FAQ, checked 2026-10-23.</text>')
    svg("05-05-three-copies.svg", w, y + 30,
        "Multi-AZ standby, read replica and backups compared",
        "Three columns compared on five rows. How it's copied: the Multi-AZ standby gets every write synchronously, "
        "in another AZ; the read replica gets changes asynchronously and can lag behind; backups are a daily "
        "snapshot plus a log of every change, and snapshots are taken when you take them. Answers queries: standby "
        "no; read replica yes, read-only; backups no, you restore to a new database first. Takes over by itself: "
        "standby yes, by automatic failover, typically one to two minutes; read replica no, you can promote it by "
        "hand and lose any lag; backups no, a restore is a new database you switch to. Saves you from a mistaken "
        "delete: standby no, the delete reaches it at once; read replica no, it reaches it soon after; backups "
        "yes, restore to a moment before the mistake. The job: high availability; read scaling and a disaster "
        "recovery option; going back in time. A note says this is for RDS engines other than Aurora; in Aurora a "
        "read replica can also be the failover target.", body, style=STYLE)


if __name__ == "__main__":
    three_copies()
