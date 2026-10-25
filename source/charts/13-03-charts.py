#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 13.03 (migration tools) as SVG.

Usage: python3 -I source/charts/13-03-charts.py
Writes images/13-03-*.svg. Facts come from AWS pages cited in
guide/13-moving-to-aws/03-migration-tools.md, checked 2026-10-24: the availability-change
pages for AWS Application Discovery Service and AWS Migration Hub (closed to new
customers from 2025-11-07; AWS points to AWS Transform), the AWS Transform MGN product
page and FAQs (formerly AWS Application Migration Service), the AWS DMS FAQs, the
DataSync and Snowball pages, and the Elastic Disaster Recovery user guide and FAQs.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, right_rounded  # noqa: E402

# AWS service = slot 1 (blue) tint; the one highlighted element = slot 2 (orange) outline;
# neutral cards for everything else. Words name every part, so color never works alone.
STYLE = make_style(
    light_extra=" --aws-fill:#d9e8fb; --hi-fill:#fbe1d6; --card-fill:#f1f0ec;",
    dark_extra=" --aws-fill:#1b3554; --hi-fill:#4d2716; --card-fill:#252523;",
    rules_extra="""
  .aws { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .card { fill: var(--card-fill); stroke: var(--axis); stroke-width: 1; }
  .hi { fill: var(--hi-fill); stroke: var(--s2); stroke-width: 2.5; stroke-dasharray: 6 4; }
  .panel { fill: none; stroke: var(--axis); stroke-width: 1; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .colh { fill: var(--muted); font-size: 11.5px; font-weight: 600; letter-spacing: 0.5px; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .flow { stroke: var(--ink2); stroke-width: 1.8; fill: none; }
  .flowhi { stroke: var(--s2); stroke-width: 2; fill: none; stroke-dasharray: 5 4; }
  .head-ink { fill: var(--ink2); }
  .head-hi { fill: var(--s2); }
  .dot { fill: var(--s1); stroke: var(--surface); stroke-width: 2; }
  .dothi { fill: var(--s2); stroke: var(--surface); stroke-width: 2; }
  .track { stroke: var(--s1); stroke-width: 3; fill: none; stroke-linecap: round; }
  .val { fill: var(--ink); font-size: 13px; font-variant-numeric: tabular-nums; }""")


def arrow(body, x1, y1, x2, y2, hi=False):
    a = math.atan2(y2 - y1, x2 - x1)
    ex, ey = x2 - 8 * math.cos(a), y2 - 8 * math.sin(a)
    body.append(f'<path class="{"flowhi" if hi else "flow"}" d="M{x1:.1f},{y1:.1f} L{ex:.1f},{ey:.1f}"/>')
    p1 = (x2 - 10 * math.cos(a) + 5 * math.sin(a), y2 - 10 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 10 * math.cos(a) - 5 * math.sin(a), y2 - 10 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="{"head-hi" if hi else "head-ink"}" d="M{x2:.1f},{y2:.1f} L{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z"/>')


def box(body, cls, x, y, w, h, title=None, lines=(), anchor="start"):
    body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    tx = x + w / 2 if anchor == "middle" else x + 10
    yy = y + 18
    if title:
        body.append(f'<text class="boxt" x="{tx}" y="{yy}" text-anchor="{anchor}">{title}</text>')
        yy += 16
    text_lines(body, tx, yy, list(lines), cls="cells", dy=14, anchor=anchor)


def big_picture():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Plan, move, stay ready: one job per tool</text>',
        '<text class="sub" x="16" y="48">Planning tools move nothing. Each moving tool moves one kind of thing.</text>',
    ]
    cw, gap, top = 206, 15, 74
    xs = [16, 16 + cw + gap, 16 + 2 * (cw + gap)]
    heads = ["PLAN", "MOVE", "STAY READY"]
    for x, hd in zip(xs, heads):
        body.append(f'<text class="colh" x="{x}" y="{top}">{hd}</text>')
    y0 = top + 12
    bh, bg = 72, 12
    plan = [
        ("aws", "Migration Evaluator", ["Prices the move:", "the business case"]),
        ("hi", "Application Discovery Svc.", ["Finds servers and", "their dependencies"]),
        ("hi", "Migration Hub", ["Tracks each", "application's migration"]),
    ]
    move = [
        ("aws", "Application Migration", ["Service, now AWS Transform", "MGN: whole servers"]),
        ("aws", "AWS DMS", ["Database data; SCT or DMS", "Schema Conversion first if", "the engine changes"]),
        ("aws", "AWS DataSync", ["Files and objects over", "the network (not Snowball)"]),
    ]
    for col, items in ((0, plan), (1, move)):
        for i, (cls, t, ls) in enumerate(items):
            box(body, cls, xs[col], y0 + i * (bh + bg), cw, bh, t, ls)
    box(body, "aws", xs[2], y0, cw, bh, "Elastic Disaster Recovery", ["Keeps copying servers;", "launch them after a disaster"])
    # closed-to-new-customers note and the arrow to AWS Transform
    ty = y0 + 3 * (bh + bg) + 8
    box(body, "card", xs[0], ty, cw, 56, "AWS Transform", ["What AWS points new", "customers to instead"])
    arrow(body, xs[0] + cw - 24, y0 + 2 * (bh + bg) + bh, xs[0] + cw - 24, ty, hi=True)
    body.append(f'<text class="note" x="{xs[1]}" y="{ty + 18}">Dashed orange outline: closed to new customers</text>')
    body.append(f'<text class="note" x="{xs[1]}" y="{ty + 34}">since 2025-11-07. The exam still names both.</text>')
    body.append(f'<text class="note" x="{xs[1]}" y="{ty + 50}">Checked 2026-10-24.</text>')
    h = ty + 70
    svg("13-03-big-picture.svg", w, h,
        "Migration tools grouped by job: plan, move and stay ready",
        "Three columns. Plan: Migration Evaluator prices the move and builds the business case; AWS Application "
        "Discovery Service finds servers and their dependencies; AWS Migration Hub tracks each application's "
        "migration. Discovery Service and Migration Hub have a dashed outline meaning closed to new customers "
        "since 2025-11-07, and an arrow leads to AWS Transform, which AWS points new customers to instead. Move: "
        "Application Migration Service, now AWS Transform MGN, moves whole servers; AWS DMS moves database data, "
        "with AWS SCT or DMS Schema Conversion first if the engine changes; AWS DataSync moves files and objects over "
        "the network, not Snowball. Stay ready: Elastic Disaster Recovery keeps copying servers so they can be "
        "launched after a disaster.", body, style=STYLE)


def mgn_vs_dms():
    w = 680
    body = [
        '<text class="title" x="16" y="28">What lands in AWS: a whole server, or only the data</text>',
        '<text class="sub" x="16" y="48">Both copy while the source keeps running. They differ in the unit that moves.</text>',
    ]
    pw, top, ph = 316, 64, 330
    panels = [
        (16, "Application Migration Service", "now AWS Transform MGN",
         ["Operating system", "Installed software (incl. a database)", "Disks and data"], "copies the whole server,",
         "block by block", "EC2 instance", ["You still patch the OS and", "the database software"], "Strategy: rehost"),
        (16 + pw + 16, "AWS DMS", "with AWS SCT or DMS Schema Conversion",
         ["Tables and rows", "then every new change", ""], "copies only the data;",
         "schema converted first if needed", "Managed database (RDS, Aurora)", ["AWS runs and patches the", "database software"],
         "Strategy: replatform; database replication"),
    ]
    for (px, name, sub, src, a1, a2, land, after, strat) in panels:
        body.append(f'<rect class="panel" x="{px}" y="{top}" width="{pw}" height="{ph}" rx="8"/>')
        body.append(f'<text class="head" x="{px + 14}" y="{top + 24}">{name}</text>')
        body.append(f'<text class="cells" x="{px + 14}" y="{top + 42}">{sub}</text>')
        body.append(f'<text class="colh" x="{px + 14}" y="{top + 68}">ON-PREMISES</text>')
        box(body, "card", px + 14, top + 76, pw - 28, 64, None, [])
        text_lines(body, px + 24, top + 96, [s for s in src if s], cls="cells", dy=16)
        arrow(body, px + 44, top + 146, px + 44, top + 196)
        body.append(f'<text class="cells" x="{px + 58}" y="{top + 166}">{a1}</text>')
        body.append(f'<text class="cells" x="{px + 58}" y="{top + 182}">{a2}</text>')
        body.append(f'<text class="colh" x="{px + 14}" y="{top + 212}">IN AWS</text>')
        box(body, "aws", px + 14, top + 220, pw - 28, 40, land, [])
        text_lines(body, px + 14, top + 282, after, cls="cells", dy=15)
        body.append(f'<text class="boxt" x="{px + 14}" y="{top + 318}">{strat}</text>')
    svg("13-03-mgn-vs-dms.svg", w, top + ph + 16,
        "Application Migration Service compared with AWS DMS",
        "Two panels. Left, Application Migration Service, now AWS Transform MGN: on-premises, the operating system, "
        "installed software including any database, and the disks; it copies the whole server block by block; in AWS "
        "it lands as an EC2 instance, and you still patch the operating system and the database software. Strategy: "
        "rehost. Right, AWS DMS with AWS SCT or DMS Schema Conversion: on-premises, the tables and rows, then every "
        "new change; it copies only the data, with the schema converted first if the engine changes; in AWS it lands "
        "in a managed database such as RDS or Aurora, where AWS runs and patches the database software. Strategy: "
        "replatform, or database replication.", body, style=STYLE)


def mgn_vs_drs():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Same copying, different ending</text>',
        '<text class="sub" x="16" y="48">Application Migration Service ends at cutover. Elastic Disaster Recovery keeps going.</text>',
    ]

    def lane(y, name, sub, steps, loop):
        body.append(f'<text class="head" x="16" y="{y}">{name}</text>')
        body.append(f'<text class="cells" x="16" y="{y + 17}">{sub}</text>')
        ly = y + 58
        x0, x1 = 40, 600
        n = len(steps)
        xs = [x0 + (x1 - x0) * i / (n - 1) for i in range(n)]
        body.append(f'<line class="track" x1="{x0}" x2="{x1}" y1="{ly}" y2="{ly}"/>')
        for i, (x, (a, b)) in enumerate(zip(xs, steps)):
            last = i == n - 1
            body.append(f'<circle class="{"dothi" if last else "dot"}" cx="{x:.1f}" cy="{ly}" r="7"/>')
            body.append(f'<text class="cells" x="{x:.1f}" y="{ly + 26}" text-anchor="middle">{a}</text>')
            if b:
                body.append(f'<text class="cells" x="{x:.1f}" y="{ly + 41}" text-anchor="middle">{b}</text>')
        if loop:
            # loop back from the end to "replicate"
            body.append(f'<path class="flowhi" d="M{x1:.1f},{ly - 10} C{x1:.1f},{ly - 46} {xs[1]:.1f},{ly - 46} {xs[1]:.1f},{ly - 14}"/>')
            body.append(f'<path class="head-hi" d="M{xs[1]:.1f},{ly - 8} L{xs[1] - 5:.1f},{ly - 18} L{xs[1] + 5:.1f},{ly - 18} Z"/>')
            body.append(f'<text class="boxt" x="{(x1 + xs[1]) / 2:.1f}" y="{ly - 40}" text-anchor="middle">loops: protection never ends</text>')
        else:
            body.append(f'<line class="lead" x1="{x1 + 14}" x2="{x1 + 14}" y1="{ly - 12}" y2="{ly + 12}"/>')
            body.append(f'<text class="boxt" x="{x1 + 22}" y="{ly + 5}">ends</text>')

    lane(84, "Application Migration Service (AWS Transform MGN)", "A one-time move",
         [("Install", "agent"), ("Replicate", "continuously"), ("Launch", "tests"), ("Cut over", ""),
          ("Stop replicating;", "retire the source")], loop=False)
    lane(220, "AWS Elastic Disaster Recovery", "Ongoing protection",
         [("Install", "agent"), ("Replicate", "continuously"), ("Run drills", ""), ("Disaster: recover", "in AWS in minutes"),
          ("Fail back when", "the site is fixed")], loop=True)
    svg("13-03-mgn-vs-drs.svg", w, 350,
        "Application Migration Service and Elastic Disaster Recovery compared as two timelines",
        "Two timelines. Application Migration Service, now AWS Transform MGN, a one-time move: install the agent, "
        "replicate continuously, launch tests, cut over, then stop replicating and retire the source; the line ends. "
        "AWS Elastic Disaster Recovery, ongoing protection: install the agent, replicate continuously, run drills, "
        "and after a disaster recover in AWS within minutes, then fail back when the site is fixed; an arrow loops "
        "back to replication, because protection never ends.", body, style=STYLE)


if __name__ == "__main__":
    big_picture()
    mgn_vs_dms()
    mgn_vs_drs()
