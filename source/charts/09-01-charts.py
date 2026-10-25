#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 09.01 (who did what, how it runs, how it was set) as SVG.

Usage: python3 -I source/charts/09-01-charts.py
Writes images/09-01-*.svg. Facts come from the AWS CloudTrail User Guide ("How
CloudTrail works": Event history keeps 90 days of management events per Region at no
charge; trails deliver log files to an S3 bucket you keep as long as you want), the
Amazon CloudWatch Logs User Guide (log data is kept indefinitely until you set a
retention period for the log group), the AWS Config Developer Guide (configuration
items are kept for 7 years, 2,557 days, by default; you can set 30 to 2,557 days; the
managed rule restricted-ssh), and the IAM User Guide (last accessed information:
service information is tracked for at least 400 days; credential report). All
checked 2026-10-24. The bakery and its change are made up for teaching; addresses
come from the ranges reserved for documentation. Our own design: no AWS logos,
icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, swatch, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --hl-fill:#d9e8fb; --no-fill:#fbe1d6; --n-fill:#f1f0ec;",
    dark_extra=" --hl-fill:#1b3554; --no-fill:#4d2716; --n-fill:#252523;",
    rules_extra="""
  .card { fill: none; stroke: var(--axis); stroke-width: 1; }
  .qbox { fill: var(--hl-fill); stroke: var(--s1); stroke-width: 1.5; }
  .name { fill: var(--ink); font-size: 15px; font-weight: 600; }
  .q { fill: var(--ink); font-size: 13.5px; font-weight: 600; }
  .key { fill: var(--muted); font-size: 11px; font-weight: 600; letter-spacing: 0.5px; }
  .small { fill: var(--ink2); font-size: 12px; }
  .mono { fill: var(--ink); font-size: 11.5px; font-family: ui-monospace, "SFMono-Regular", Menlo, monospace; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow-s2 { fill: var(--s2); }
  .ok { fill: var(--hl-fill); stroke: var(--s1); stroke-width: 1.2; }
  .no { fill: var(--no-fill); stroke: var(--s2); stroke-width: 1.2; }
  .n { fill: var(--n-fill); stroke: var(--axis); stroke-width: 1; }
  .tl { stroke: var(--ink2); stroke-width: 1.5; }
  .chg { stroke: var(--s2); stroke-width: 2; stroke-dasharray: 5 4; }
  .rowl { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .ans { fill: var(--ink2); font-size: 12px; font-weight: 700; letter-spacing: 0.4px; }""")

CARDS = [
    ("AWS CloudTrail", "Who did what, when, and from where?", [
        ("RECORDS", "Each action taken in the account: who, which action, on what, when, from which address"),
        ("BAKERY EXAMPLE", "Who opened SSH on web-sg on Tuesday?"),
        ("FROM DAY ONE", "Event history: on, free, last 90 days per Region"),
    ]),
    ("Amazon CloudWatch", "How is it running, and what happened inside it?", [
        ("RECORDS", "Metrics, logs and alarms from resources and your own code"),
        ("BAKERY EXAMPLE", "Why were orders slow at 6 p.m.?"),
        ("FROM DAY ONE", "Basic metrics from AWS services; logs you send are kept until you set a limit"),
    ]),
    ("AWS Config", "How was it set up, then and now, and is that allowed?", [
        ("RECORDS", "Each resource's settings over time, and whether they pass your rules"),
        ("BAKERY EXAMPLE", "Was SSH open to the internet on March 1?"),
        ("FROM DAY ONE", "Off: you turn recording on, and pay per item recorded"),
    ]),
    ("IAM access reports", "Who can do what, and do they still use it?", [
        ("RECORDS", "When each user, role or policy last used each service; who holds which credentials"),
        ("BAKERY EXAMPLE", "Which permissions has nobody used in 90 days?"),
        ("FROM DAY ONE", "On and free, in the IAM console"),
    ]),
]


def three_questions():
    """Big picture: four records, each answering a different audit question."""
    w, cw, gap = 680, 320, 8
    body = [
        '<text class="title" x="16" y="28">Four records, four different questions</text>',
        '<text class="sub" x="16" y="48">Match the question to the record that can answer it; the highlighted line is the question</text>',
    ]
    wrapw = 44
    # equal-height rows across each pair of cards
    def card_rows(rows):
        return [16 + 16 * len(wrap(v, wrapw)) + 8 for _, v in rows]

    desc = []
    top = 66
    for pair in range(2):
        a, b = CARDS[pair * 2], CARDS[pair * 2 + 1]
        heights = [max(x, y) for x, y in zip(card_rows(a[2]), card_rows(b[2]))]
        qh = 16 * max(len(wrap(a[1], 38)), len(wrap(b[1], 38))) + 14
        ch = 34 + qh + 8 + sum(heights)
        for i, (name, q, rows) in enumerate((a, b)):
            x = 16 + i * (cw + gap)
            body.append(f'<rect class="card" x="{x}" y="{top}" width="{cw}" height="{ch}" rx="8"/>')
            body.append(f'<text class="name" x="{x + 14}" y="{top + 24}">{name}</text>')
            body.append(f'<rect class="qbox" x="{x + 8}" y="{top + 34}" width="{cw - 16}" height="{qh}" rx="6"/>')
            text_lines(body, x + 16, top + 34 + 19, wrap(q, 38), cls="q", dy=16)
            y = top + 34 + qh + 8
            for r, (key, val) in enumerate(rows):
                body.append(f'<text class="key" x="{x + 14}" y="{y + 12}">{key}</text>')
                text_lines(body, x + 14, y + 28, wrap(val, wrapw), cls="small", dy=16)
                y += heights[r]
            desc.append(f"{name}. Question: {q} " + " ".join(f"{k.capitalize()}: {v}." for k, v in rows))
        top += ch + 10
    body.append(f'<text class="note" x="16" y="{top + 8}">From the CloudTrail, CloudWatch, Config and IAM user guides, checked 2026-10-24. The bakery is made up for teaching.</text>')
    svg("09-01-four-records.svg", w, top + 22,
        "Four records that answer four different audit questions",
        "Four cards in a two-by-two grid, each with a highlighted question. " + " ".join(desc), body, style=STYLE)


def one_change_three_views():
    """The same change seen by CloudTrail, Config and CloudWatch."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">One change, seen three ways</text>',
        '<text class="sub" x="16" y="48">Tuesday 14:02 UTC: someone adds a rule to web-sg allowing SSH (port 22) from anywhere</text>',
    ]
    # time line
    tl_y, x0, x1 = 84, 150, 664
    body.append(f'<line class="tl" x1="{x0}" x2="{x1}" y1="{tl_y}" y2="{tl_y}"/>')
    ticks = [("12:00", 0.0), ("14:02", 0.407), ("16:00", 0.8)]
    for lab, f in ticks:
        x = x0 + (x1 - x0) * f
        body.append(f'<line class="tl" x1="{x:.1f}" x2="{x:.1f}" y1="{tl_y - 5}" y2="{tl_y + 5}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{tl_y - 10}" text-anchor="middle">{lab}</text>')
    cx = x0 + (x1 - x0) * 0.407
    body.append('<text class="rowl" x="16" y="88">Tuesday</text>')
    rows_top = 104
    rows = []
    # Row 1: CloudTrail
    y = rows_top
    h1 = 104
    body.append(f'<rect class="card" x="16" y="{y}" width="648" height="{h1}" rx="8"/>')
    body.append(f'<text class="rowl" x="28" y="{y + 22}">CloudTrail</text>')
    body.append(f'<text class="ans" x="28" y="{y + 40}">WHO, WHAT,</text>')
    body.append(f'<text class="ans" x="28" y="{y + 54}">WHEN, WHERE</text>')
    body.append(f'<rect class="no" x="{cx - 8:.1f}" y="{y + 10}" width="{x1 - cx:.1f}" height="{h1 - 20}" rx="6"/>')
    text_lines(body, cx + 2, y + 28, [
        "event: AuthorizeSecurityGroupIngress",
        "user: sam-dev, at 14:02:11 UTC",
        "from: 198.51.100.23",
        "group: web-sg, port 22, from 0.0.0.0/0",
    ], cls="mono", dy=17)
    rows.append("CloudTrail, answering who, what, when and where: one event at 14:02, AuthorizeSecurityGroupIngress, "
                "by user sam-dev at 14:02:11 from address 198.51.100.23, on group web-sg, port 22, from 0.0.0.0/0")
    # Row 2: Config
    y += h1 + 10
    h2 = 122
    body.append(f'<rect class="card" x="16" y="{y}" width="648" height="{h2}" rx="8"/>')
    body.append(f'<text class="rowl" x="28" y="{y + 22}">Config</text>')
    body.append(f'<text class="ans" x="28" y="{y + 40}">WHAT IT</text>')
    body.append(f'<text class="ans" x="28" y="{y + 54}">LOOKED LIKE;</text>')
    body.append(f'<text class="ans" x="28" y="{y + 68}">IS IT ALLOWED?</text>')
    bx_w = cx - x0 - 14
    body.append(f'<rect class="ok" x="{x0}" y="{y + 10}" width="{bx_w:.1f}" height="{h2 - 20}" rx="6"/>')
    text_lines(body, x0 + 10, y + 28, ["web-sg settings,", "before 14:02:", "443 from anywhere", "restricted-ssh:", "compliant"],
               cls="small", dy=16)
    body.append(f'<rect class="no" x="{cx - 8:.1f}" y="{y + 10}" width="{x1 - cx:.1f}" height="{h2 - 20}" rx="6"/>')
    text_lines(body, cx + 2, y + 28, ["web-sg settings, from 14:02:", "443 from anywhere", "22 from anywhere (new)",
                                      "restricted-ssh rule: noncompliant"], cls="small", dy=16)
    rows.append("Config, answering what it looked like and whether it is allowed: before 14:02, web-sg allowed 443 "
                "from anywhere and the rule restricted-ssh was compliant; from 14:02, web-sg allows 443 and, new, 22 "
                "from anywhere, and the rule is noncompliant")
    # Row 3: CloudWatch
    y += h2 + 10
    h3 = 132
    body.append(f'<rect class="card" x="16" y="{y}" width="648" height="{h3}" rx="8"/>')
    body.append(f'<text class="rowl" x="28" y="{y + 22}">CloudWatch</text>')
    body.append(f'<text class="ans" x="28" y="{y + 40}">HOW IT\'S</text>')
    body.append(f'<text class="ans" x="28" y="{y + 54}">BEHAVING</text>')
    # a small bar series of failed SSH sign-ins per 15 minutes
    vals = [0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 20, 34, 38, 41, 40, 39, 42, 40, 41, 38]
    base = y + h3 - 14
    ph = h3 - 62
    n = len(vals)
    bw = (x1 - x0) / n
    vmax = 45
    for i, v in enumerate(vals):
        if v == 0:
            continue
        bh = ph * v / vmax
        body.append(f'<path class="s2" d="M{x0 + i * bw + 2:.1f},{base:.1f} L{x0 + i * bw + 2:.1f},{base - bh:.1f} '
                    f'L{x0 + (i + 1) * bw - 2:.1f},{base - bh:.1f} L{x0 + (i + 1) * bw - 2:.1f},{base:.1f} Z"/>')
    body.append(f'<line class="axis" x1="{x0}" x2="{x1}" y1="{base}" y2="{base}"/>')
    body.append(f'<text class="small" x="{x0}" y="{y + 20}">Failed SSH sign-ins on the web server, per 15 minutes,</text>')
    body.append(f'<text class="small" x="{x0}" y="{y + 36}">from its own log, sent to CloudWatch Logs by the agent</text>')
    rows.append("CloudWatch, answering how it is behaving: a bar chart of failed SSH sign-ins on the web server per 15 "
                "minutes, from its own log sent to CloudWatch Logs; zero before the change, then rising to about 40 "
                "per 15 minutes within an hour of 14:02")
    y += h3
    # the change marker across all rows
    body.append(f'<line class="chg" x1="{cx - 8:.1f}" x2="{cx - 8:.1f}" y1="{tl_y}" y2="{y}"/>')
    y += 22
    body.append(f'<text class="note" x="16" y="{y}">Made-up change for teaching; the address is from a range reserved for documentation. restricted-ssh is an</text>')
    body.append(f'<text class="note" x="16" y="{y + 15}">AWS Config managed rule; the failed sign-ins appear only if the bakery sends the server\'s log to CloudWatch.</text>')
    svg("09-01-one-change-three-views.svg", w, y + 28,
        "The same security group change as CloudTrail, Config and CloudWatch record it",
        "A time line for Tuesday from 12:00 to 16:00 with a dashed marker at 14:02, when someone adds a rule to the "
        "security group web-sg allowing SSH, port 22, from anywhere. Three rows below. " + ". ".join(rows) + ".",
        body, style=STYLE)


# label, days (None = no limit by default), note
KEEP = [
    ("CloudTrail Event history", 90, "90 days, fixed; free"),
    ("IAM last accessed (services)", 400, "At least 400 days"),
    ("AWS Config history", 2557, "7 years by default; you can set 30 days to 7 years"),
    ("CloudTrail trail, in your S3 bucket", None, "As long as you keep the files (you pay for S3)"),
    ("CloudWatch Logs log group", None, "Never expires until you set a retention period"),
]


def how_long_kept():
    w, left, right = 680, 252, 640
    top, bar_h, row_h = 92, 18, 56
    pw = right - left
    dmax = 2557 + 365 // 2
    body = [
        '<text class="title" x="16" y="28">How long each record is kept, unless you change it</text>',
        '<text class="sub" x="16" y="48">Days, from 0 to 7 years. Records with no default limit run off the right edge.</text>',
    ]
    swatch(body, 16, 74, "s1", "A default limit")
    swatch(body, 140, 74, "s2", "No limit by default")
    ph = row_h * len(KEEP)
    for yr in range(0, 8):
        x = left + pw * (yr * 365.25) / dmax
        body.append(f'<line class="{"axis" if yr == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top}" y2="{top + ph}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top + ph + 18}" text-anchor="middle">{"0" if yr == 0 else f"{yr} y"}</text>')
    desc = []
    for i, (label, days, note) in enumerate(KEEP):
        y = top + i * row_h + 8
        body.append(f'<text class="lab" x="{left - 10}" y="{y + 13}" text-anchor="end">{label}</text>')
        if days is None:
            bw = pw + 14
            body.append(f'<path class="s2" d="{right_rounded(left, y, bw - 12, bar_h, 0)}"/>')
            ax = left + bw - 12
            body.append(f'<path class="arrow-s2" d="M{ax:.1f},{y - 4} L{ax + 14:.1f},{y + bar_h / 2} L{ax:.1f},{y + bar_h + 4} Z"/>')
        else:
            bw = pw * days / dmax
            body.append(f'<path class="s1" d="{right_rounded(left, y, bw, bar_h)}"/>')
        body.append(f'<text class="small" x="{left}" y="{y + bar_h + 16}">{note}</text>')
        desc.append(f"{label}: {note}")
    h = top + ph + 30
    body.append(f'<text class="note" x="16" y="{h}">From the CloudTrail, CloudWatch Logs, AWS Config and IAM user guides, checked 2026-10-24.</text>')
    svg("09-01-how-long-kept.svg", w, h + 14,
        "How long CloudTrail, IAM, Config and CloudWatch keep their records by default",
        "Horizontal bars on an axis from 0 to 7 years. " + "; ".join(desc) + ". The last two bars run past the right "
        "edge with an arrow, because they have no default limit.", body, style=STYLE)


if __name__ == "__main__":
    three_questions()
    one_change_three_views()
    how_long_kept()
