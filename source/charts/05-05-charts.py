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


def big_picture():
    """The order database with its standby, a read replica and its backups, each tagged with its job."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">One order database, three kinds of copy, three different jobs</text>',
        '<text class="sub" x="16" y="48">An Amazon RDS database in one Region, as the bakery could set it up</text>',
    ]
    rx, ry, rw = 16, 66, 648
    zw, zy = 196, ry + 32
    bw, bh, by = zw - 20, 100, zy + 70
    zh = 70 + bh + 44
    bky = zy + zh + 12
    rh = bky + 62 + 12 - ry
    body.append(f'<rect class="region" x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="8"/>')
    body.append(f'<text class="zlab" x="{rx + 10}" y="{ry + 18}">AWS Region: US East (N. Virginia)</text>')
    zx = [rx + 12 + i * (zw + 10) for i in range(3)]
    names = ["Availability Zone A", "Availability Zone B", "Availability Zone C"]
    for x, n in zip(zx, names):
        body.append(f'<rect class="zone" x="{x}" y="{zy}" width="{zw}" height="{zh}" rx="6"/>')
        body.append(f'<text class="zlab" x="{x + 8}" y="{zy + 16}">{n}</text>')
    box(body, "pri", zx[0] + 10, by, bw, bh, "Primary", ["Takes every read and write from the website"], 22)
    box(body, "copy", zx[1] + 10, by, bw, bh, "Standby (Multi-AZ)",
        ["Gets every write at once. Serves nothing; takes over if the primary fails"], 22)
    box(body, "copy", zx[2] + 10, by, bw, bh, "Read replica",
        ["Gets changes a little later, so it can lag. Answers read-only queries"], 22)
    body.append(f'<text class="small" x="{zx[0] + 10}" y="{zy + 44}">Website: reads and writes</text>')
    arrow(body, zx[0] + 40, zy + 50, zx[0] + 40, by - 2)
    body.append(f'<text class="small" x="{zx[2] + 10}" y="{zy + 44}">Reports: reads only</text>')
    arrow(body, zx[2] + 40, zy + 50, zx[2] + 40, by - 2)
    # Synchronous copy: primary to standby.
    ay1 = by + 34
    arrow(body, zx[0] + 10 + bw + 1, ay1, zx[1] + 8, ay1)
    body.append(f'<text class="arrlab" x="{zx[1] - 5:.1f}" y="{ay1 - 6}" text-anchor="middle">sync</text>')
    # Asynchronous copy: primary to replica, routed under the standby.
    ay2 = by + bh + 26
    x0, x2 = zx[0] + 10 + bw / 2, zx[2] + 10 + bw / 2
    body.append(f'<path class="arrow" d="M{x0:.1f},{by + bh + 1} L{x0:.1f},{ay2} L{x2:.1f},{ay2} L{x2:.1f},{by + bh + 10}"/>')
    body.append(f'<path class="arrowhead" d="M{x2 - 5:.1f},{by + bh + 10} L{x2 + 5:.1f},{by + bh + 10} L{x2:.1f},{by + bh + 2} Z"/>')
    body.append(f'<text class="arrlab" x="{zx[1] + zw / 2:.1f}" y="{ay2 - 6}" text-anchor="middle">async: can lag behind</text>')
    # Backups: Regional, below the AZs.
    box(body, "copy", rx + 12, bky, rw - 24, 62, "Automated backups and snapshots (stored in Amazon S3, in the Region)",
        ["A daily snapshot plus a log of every change: restore to any second in the retention period (7 days by default, up to 35), or to a snapshot you took."], 80)
    # The three jobs.
    y = ry + rh + 26
    body.append(f'<text class="head" x="16" y="{y}">The job each copy does</text>')
    jobs = [("Standby:", "keeps the database running if its AZ fails (high availability)"),
            ("Read replica:", "takes read-only work off the primary (read scaling)"),
            ("Backups and snapshots:", "go back to before a mistake (point-in-time recovery)")]
    y += 20
    for k, v in jobs:
        body.append(f'<text class="q" x="16" y="{y}">{k}</text>')
        body.append(f'<text class="small" x="176" y="{y}">{v}</text>')
        y += 18
    y += 8
    body.append(f'<text class="note" x="16" y="{y}">From the Amazon RDS User Guide and FAQ, checked 2026-10-23. The bakery\'s setup is made up for teaching.</text>')
    svg("05-05-big-picture.svg", w, y + 14,
        "One Amazon RDS order database with a Multi-AZ standby, a read replica and backups",
        "A Region, US East (N. Virginia), holding three Availability Zones side by side. In AZ A, the primary "
        "takes every read and write from the website. In AZ B, the Multi-AZ standby takes no traffic and waits to "
        "take over if the primary fails; an arrow labeled sync shows it gets every write at once "
        "(synchronously). In AZ C, a read replica answers read-only queries such as reports; an arrow from the "
        "primary to the replica is labeled async: changes arrive a little later, so the replica can lag behind. Below the "
        "AZs, for the whole Region: automated backups and snapshots stored in Amazon S3, a daily snapshot plus a "
        "log of every change, restorable to any second in the retention period (7 days by default, up to 35) or to a snapshot you took. A key "
        "lists each copy's job: the standby keeps the database running if its AZ fails (high availability); the "
        "read replica takes read-only work off the primary (read scaling); backups and snapshots go back to "
        "before a mistake (point-in-time recovery).", body, style=STYLE)


def failover_frames():
    """Three numbered static frames of a Multi-AZ failover."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">A Multi-AZ failover in three frames</text>',
        '<text class="sub" x="16" y="48">The website keeps using the same database name; RDS changes where the name points</text>',
    ]
    fw, gap = 208, 12
    fx = [16 + i * (fw + gap) for i in range(3)]
    top = 66
    frames = [
        ("Before", "Normal running",
         ("pri", "Primary", "AZ A"), ("copy", "Standby", "AZ B"), "A",
         "Every write reaches both, synchronously."),
        ("The failure", "AZ A fails",
         ("bad", "Primary: failed", "AZ A"), ("copy", "Standby", "AZ B"), None,
         "RDS detects the failure and promotes the standby. No one has to act."),
        ("After", "Typically 1 to 2 minutes later",
         ("bad", "Old primary: failed", "AZ A"), ("pri", "Primary now", "AZ B"), "B",
         "The website reconnects to the same name, now pointing at AZ B."),
    ]
    for i, (x, (head, sub, b1, b2, target, note)) in enumerate(zip(fx, frames)):
        body.append(f'<circle class="numc" cx="{x + 12}" cy="{top + 8}" r="11"/>')
        body.append(f'<text class="num" x="{x + 12}" y="{top + 13}" text-anchor="middle">{i + 1}</text>')
        body.append(f'<text class="cellt" x="{x + 30}" y="{top + 13}">{head}</text>')
        body.append(f'<text class="small" x="{x}" y="{top + 36}">{sub}</text>')
        # The name the website uses.
        ny = top + 72
        body.append(f'<rect class="copy" x="{x + 44}" y="{ny}" width="{fw - 88}" height="30" rx="15"/>')
        body.append(f'<text class="cellt" x="{x + fw / 2}" y="{ny + 20}" text-anchor="middle">orders-db</text>')
        body.append(f'<text class="zlab" x="{x + fw / 2}" y="{ny - 4}" text-anchor="middle">the database name the site uses</text>')
        by = ny + 74
        bw, bh = 94, 58
        for j, (cls, label, az) in enumerate((b1, b2)):
            bx = x + j * (bw + 20)
            body.append(f'<rect class="{cls}" x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="6"/>')
            text_lines(body, bx + 8, by + 20, wrap(label, 12), cls="cellt", dy=15)
            body.append(f'<text class="zlab" x="{bx + 8}" y="{by + bh - 8}">{az}</text>')
        if target:
            tx = x + 47 if target == "A" else x + 47 + bw + 20
            arrow(body, x + fw / 2, ny + 31, tx, by - 2)
        else:
            body.append(f'<text class="arrlab" x="{x + fw / 2}" y="{ny + 54}" text-anchor="middle">name being moved</text>')
        if i == 0:
            arrow(body, x + bw + 1, by + bh / 2, x + bw + 19, by + bh / 2)
        text_lines(body, x, by + bh + 22, wrap(note, 32), cls="small", dy=15)
    y = top + 72 + 74 + 58 + 22 + 50
    body.append(f'<text class="note" x="16" y="{y}">Failover time from the Amazon RDS FAQ (checked 2026-10-23): typically one to two minutes from detecting</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">the failure to transactions resuming. RDS doesn\'t fail over for slow queries or corrupted data.</text>')
    svg("05-05-failover-frames.svg", w, y + 30,
        "A Multi-AZ failover in three numbered frames",
        "Three frames side by side. Frame 1, before, normal running: the website uses the database name orders-db, "
        "which points at the primary in AZ A; every write reaches the standby in AZ B synchronously. Frame 2, the "
        "failure: AZ A fails and the primary is marked failed; RDS detects the failure and promotes the standby, "
        "with no one having to act; the name is being moved. Frame 3, after, typically one to two minutes later: "
        "the old primary in AZ A is still failed, the former standby in AZ B is now the primary, and the website "
        "reconnects to the same name, which now points at AZ B. A note says RDS doesn't fail over for slow "
        "queries or corrupted data.", body, style=STYLE)


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
    big_picture()
    failover_frames()
    three_copies()
