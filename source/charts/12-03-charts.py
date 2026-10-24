#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 12.03 (where to find answers) as SVG.

Usage: python3 -I source/charts/12-03-charts.py
Writes images/12-03-*.svg. Facts come from AWS pages checked 2026-10-23 and 2026-10-24: the
AWS re:Post home page and its Knowledge Center page; the AWS Prescriptive Guidance home page
(guides for planners, patterns for builders); "Getting started with AWS Support" and the AWS
Support FAQ (Support Center; Basic accounts open account, billing and quota cases only); the
Compare AWS Support plans page (re:Post with every plan, prioritized responses on paid plans);
the Knowledge Center article "How do I report abuse of AWS resources?" (the abuse form, what
Trust &amp; Safety does, AWS Support can't assist with abuse reports or Trust &amp; Safety notices);
and the AWS Prescriptive Guidance page "Security incident response and resources" (a support
case from the affected account brings in the AWS CIRT at no additional charge on any plan).
The bakery is made up for teaching. Our own design: no AWS logos, icons, trade dress or AWS
diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Highlighted = slot 1 (blue) tint; neutral otherwise. Every cell also says what it means in words.
STYLE = make_style(
    light_extra=" --ok-fill:#d9e8fb; --n-fill:#f1f0ec;",
    dark_extra=" --ok-fill:#1b3554; --n-fill:#252523;",
    rules_extra="""
  .ok { fill: var(--ok-fill); stroke: var(--s1); stroke-width: 1.5; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .key { fill: var(--muted); font-size: 11px; font-weight: 600; letter-spacing: 0.4px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }""")


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


def arrow(body, x1, y1, x2, y2):
    """A straight line with a small filled head at (x2, y2)."""
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def compare(name, title, sub, cols, rows, hi_row, note, svg_title, desc, w=720):
    """Several comparison columns on labeled rows, with one row highlighted."""
    body = [f'<text class="title" x="16" y="28">{title}</text>', f'<text class="sub" x="16" y="48">{sub}</text>']
    n = len(cols)
    lw, gap = 112, 6
    cw = (w - 32 - lw - gap * (n - 1)) / n
    chars = int(cw / 6.9)
    xs = [16 + lw + i * (cw + gap) for i in range(n)]
    y = 66
    head = [wrap(c[0], chars - 2) for c in cols]
    hh = 14 + 16 * max(len(h) for h in head)
    for x, lines in zip(xs, head):
        rect(body, "n", x, y, cw, hh)
        text_lines(body, x + 8, y + 20, lines, cls="cellt", dy=16)
    y += hh + 8
    for r, row in enumerate(rows):
        hi = r == hi_row
        cells = [wrap(c[1][r], chars - (3 if hi else 0)) for c in cols]
        label = wrap(row, 15)
        h = 14 + 15 * max(max(len(c) for c in cells), len(label)) + 6
        if hi:
            for x in xs:
                rect(body, "ok", x - 2, y + 2, cw + 4, h - 4, 5)
        body.append(f'<line class="grid" x1="16" x2="{xs[-1] + cw}" y1="{y}" y2="{y}"/>')
        text_lines(body, 16, y + 19, label, cls="rowl", dy=15)
        for x, c in zip(xs, cells):
            text_lines(body, x + 8, y + 19, c, cls="cellt" if hi else "small", dy=15)
        y += h
    body.append(f'<line class="grid" x1="16" x2="{xs[-1] + cw}" y1="{y}" y2="{y}"/>')
    y += 22
    for line in note:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg(name, w, y + 14, svg_title, desc, body, style=STYLE)


def four_places():
    compare(
        "12-03-four-places.svg",
        "Four places people mix up: who answers, and about what",
        "Read across a row; only one of the four can look inside your account",
        [("re:Post questions",
          ["Anyone: community members, AWS staff, recognized experts",
           "No: a public site, so describe the problem, never your keys or secrets",
           "An unusual problem nobody has written up yet",
           "Free with every plan; paid plans get prioritized responses"]),
         ("Knowledge Center",
          ["AWS, as official articles and videos",
           "No: the same article for every customer",
           "A common problem, fixed step by step",
           "Free, as part of re:Post"]),
         ("Prescriptive Guidance",
          ["AWS experts, as guides and patterns",
           "No: written for many organizations",
           "Planning a change, or building a tested design",
           "Free to read"]),
         ("Support Center",
          ["AWS Support staff, in a case only you and AWS see",
           "Yes: it's opened from your account, about your account",
           "Billing and account questions; technical cases on a paid plan",
           "Account and billing cases with every plan; technical cases need a paid plan"])],
        ["Who answers", "Sees your account?", "Best for", "Cost"],
        1,
        ["From the AWS re:Post and Prescriptive Guidance home pages, the AWS Support FAQ and the Compare AWS Support",
         "plans page, checked 2026-10-24. Plans and their prices are in lesson 12.01."],
        "AWS re:Post, the Knowledge Center, Prescriptive Guidance and Support Center compared",
        "Four columns compared on four rows. Who answers: re:Post questions, anyone, including community members, "
        "AWS staff and recognized experts; Knowledge Center, AWS, as official articles and videos; Prescriptive "
        "Guidance, AWS experts, as guides and patterns; Support Center, AWS Support staff in a case only you and "
        "AWS see. Sees your account, highlighted: re:Post, no, it is a public site, so describe the problem and "
        "never post keys or secrets; Knowledge Center, no, the same article for every customer; Prescriptive "
        "Guidance, no, written for many organizations; Support Center, yes, the case is opened from your account "
        "and is about your account. Best for: re:Post, an unusual problem nobody has written up; Knowledge "
        "Center, a common problem fixed step by step; Prescriptive Guidance, planning a change or building a "
        "tested design; Support Center, billing and account questions, and technical cases on a paid plan. Cost: "
        "re:Post is free with every plan and paid plans get prioritized responses; Knowledge Center is free, as part of re:Post; Prescriptive Guidance is free to read; Support Center account and billing "
        "cases come with every plan, technical cases need a paid plan.")


CASES = [
    ("ok", "1. Traffic from someone else's AWS resource is attacking you",
     "Scans, login floods, spam or stolen content, from an address in AWS's published ranges",
     "AWS Trust &amp; Safety, through the abuse report form",
     "It investigates and deals with the resource's owner; it shares details only with that owner's permission"),
    ("n", "2. AWS tells you that your resource is causing abuse",
     "An abuse report from AWS Trust &amp; Safety about one of your resources",
     "Answer Trust &amp; Safety, and fix the resource",
     "AWS Support can't help with questions about Trust &amp; Safety notifications"),
    ("n", "3. Someone is inside your own account",
     "Unknown users, keys or resources; a GuardDuty finding about your credentials",
     "A support case opened from that account, marked as an urgent security incident",
     "AWS's incident responders (AWS CIRT) can help, at no extra charge, on any Support plan"),
]


def abuse_directions():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Abuse is about whose resource misbehaves</text>',
        '<text class="sub" x="16" y="48">Three security problems, three different doors</text>',
    ]
    y = 66
    lx, rx = 16, 360
    lw, rw = 300, 304
    for cls, head, sign, door, then in CASES:
        hl = wrap(head, 40)
        sl = wrap(sign, 44)
        dl = wrap(door, 40)
        tl = wrap(then, 44)
        lh = 30 + 16 * len(hl) + 16 + 15 * len(sl)
        rh = 30 + 16 * len(dl) + 16 + 15 * len(tl)
        h = max(lh, rh) + 8
        rect(body, cls, lx, y, lw, h, 8)
        body.append(f'<text class="key" x="{lx + 12}" y="{y + 18}">WHAT HAPPENS</text>')
        yy = text_lines(body, lx + 12, y + 36, hl, cls="cellt", dy=16)
        text_lines(body, lx + 12, yy + 4, sl, cls="small", dy=15)
        rect(body, "plain" if cls == "n" else "ok", rx, y, rw, h, 8)
        body.append(f'<text class="key" x="{rx + 12}" y="{y + 18}">WHERE TO GO</text>')
        yy = text_lines(body, rx + 12, y + 36, dl, cls="cellt", dy=16)
        text_lines(body, rx + 12, yy + 4, tl, cls="small", dy=15)
        arrow(body, lx + lw + 4, y + h / 2, rx - 4, y + h / 2)
        y += h + 14
    y += 8
    for line in ["From the Knowledge Center article \"How do I report abuse of AWS resources?\" and the AWS Prescriptive Guidance",
                 "page \"Security incident response and resources\", checked 2026-10-24."]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg("12-03-abuse-directions.svg", w, y + 14,
        "Three security problems and where each one goes",
        "Three rows, each with what happens on the left, an arrow, and where to go on the right. Row 1, "
        "highlighted: traffic from someone else's AWS resource is attacking you, such as scans, login floods, spam "
        "or stolen content from an address in AWS's published ranges. Go to AWS Trust &amp; Safety through the abuse "
        "report form; it investigates and deals with the resource's owner, and shares details only with that "
        "owner's permission. Row 2: AWS tells you that your resource is causing abuse, in an abuse report from "
        "Trust &amp; Safety about one of your resources. Answer Trust &amp; Safety and fix the resource; AWS Support can't help "
        "with questions about Trust &amp; Safety notifications. Row 3: someone is inside your own account, such as unknown "
        "users, keys or resources, or a GuardDuty finding about your credentials. Open a support case from that "
        "account, marked as an urgent security incident; AWS's incident responders, the AWS CIRT, can help at no "
        "extra charge on any Support plan.",
        body, style=STYLE)


if __name__ == "__main__":
    four_places()
    abuse_directions()
