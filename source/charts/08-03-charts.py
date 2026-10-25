#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 08.03 (watching workloads) as SVG.

Usage: python3 -I source/charts/08-03-charts.py
Writes images/08-03-*.svg. Facts, checked 2026-10-24: Amazon CloudWatch User
Guide (metrics, logs and alarms); AWS X-Ray Developer Guide (traces, segments,
trace map); AWS CloudTrail User Guide (events, one per action on the account).
The bakery, its numbers and the trace timings are made up for teaching. Our
own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --hi-fill:#d9e8fb; --n-fill:#f1f0ec; --no-fill:#fbe1d6;",
    dark_extra=" --hi-fill:#1b3554; --n-fill:#252523; --no-fill:#4d2716;",
    rules_extra="""
  .panel { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 1.5; }
  .alarm { fill: var(--no-fill); stroke: var(--s2); stroke-width: 1.5; }
  .okband { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 700; }
  .small { fill: var(--ink2); font-size: 12px; }
  .q { fill: var(--ink); font-size: 13px; font-style: italic; }
  .zlab { fill: var(--muted); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .thr { stroke: var(--ink); stroke-width: 1.5; stroke-dasharray: 6 4; fill: none; }
  .bar-n { fill: var(--muted); }
  .bar-hi { fill: var(--s1); }
  .tick-line { stroke: var(--ink2); stroke-width: 1.5; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }""")


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


# ---------------------------------------------------------------- big picture

PANELS = [
    ("Amazon CloudWatch", "How is the workload doing right now, and is anything wrong?",
     ["Metrics: numbers over time, such as errors per 5 minutes",
      "Logs: the lines your code and servers write",
      "Alarms: act when a metric crosses a line"],
     "The order function had 9 errors between 13:20 and 13:25; the alarm emailed the owner."),
    ("AWS X-Ray", "Where did this one request spend its time, and where did it fail?",
     ["Traces: one request's path through every part it touched, with timings",
      "Trace map: the parts that called each other"],
     "Order 1043 took 2.45 seconds; 1.94 of them were waiting for the payment provider."),
    ("AWS CloudTrail", "Who changed what in the account, and when?",
     ["Events: one record per action on your account, by a person, a role or an AWS service",
      "Through the console, the CLI, an SDK or the API"],
     "At 12:58 the nephew's IAM user changed the order function's settings."),
]


def three_questions():
    """Big picture: three services, three questions, one bakery example each."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Three questions, three services</text>',
        '<text class="sub" x="16" y="48">Each one watches the bakery from a different side. Start from the question you need answered.</text>',
    ]
    y = 68
    for name, question, records, example in PANELS:
        rec_lines = []
        for r in records:
            for i, line in enumerate(wrap(r, 44)):
                rec_lines.append(("• " if i == 0 else "  ") + line)
        q_lines = wrap(question, 30)
        ex_lines = wrap("Bakery example: " + example, 44)
        left_h = 30 + 16 * len(q_lines)
        right_h = 16 * len(rec_lines) + 8 + 16 * len(ex_lines)
        h = max(left_h, right_h) + 26
        rect(body, "panel", 16, y, w - 32, h)
        body.append(f'<text class="head" x="30" y="{y + 24}">{name}</text>')
        text_lines(body, 30, y + 46, q_lines, cls="q", dy=16)
        ny = text_lines(body, 290, y + 24, rec_lines, cls="small", dy=16)
        text_lines(body, 290, ny + 8, ex_lines, cls="cellt", dy=16)
        y += h + 10
    y += 12
    body.append(f'<text class="note" x="16" y="{y}">Our summary of the CloudWatch, X-Ray and CloudTrail user guides, checked 2026-10-24.</text>')
    y += 16
    body.append(f'<text class="note" x="16" y="{y}">The bakery, its people and its numbers are made up.</text>')
    desc = ("Three panels, one per service, each with the question it answers, what it records and a bakery example. "
            "Amazon CloudWatch answers: how is the workload doing right now, and is anything wrong? It records metrics, "
            "numbers over time such as errors per 5 minutes; logs, the lines your code and servers write; and alarms, "
            "which act when a metric crosses a line. Example: the order function had 9 errors between 13:20 and 13:25, "
            "and the alarm emailed the owner. AWS X-Ray answers: where did this one request spend its time, and where "
            "did it fail? It records traces, one request's path through every part it touched with timings, and a "
            "trace map of the parts that called each other. Example: order 1043 took 2.45 seconds, 1.94 of them "
            "waiting for the payment provider. AWS CloudTrail answers: who changed what in the account, and when? It "
            "records events, one per action on your account by a person, a role or an AWS service, through the "
            "console, the CLI, an SDK or the API. Example: at 12:58 the nephew's IAM user changed the order "
            "function's settings.")
    svg("08-03-three-questions.svg", w, y + 14, "Three questions, three services: CloudWatch, X-Ray and CloudTrail",
        desc, body, style=STYLE)


# ---------------------------------------------------------------- trace waterfall

TRACE = [  # (part, start ms, end ms, highlighted)
    ("Web server (EC2): POST /order", 0, 2450, False),
    ("Order function (Lambda)", 90, 2400, False),
    ("Read the cake's price (RDS)", 140, 200, False),
    ("Charge the card (payment provider)", 230, 2170, True),
    ("Save the order (RDS)", 2200, 2250, False),
]


def trace_waterfall():
    total = TRACE[0][2]
    pay = [t for t in TRACE if t[3]][0]
    assert total == 2450 and pay[2] - pay[1] == 1940, "must match the lesson text"
    w, lx, left, pw, top, rh = 680, 16, 262, 400, 92, 34
    body = [
        '<text class="title" x="16" y="28">One request, every part it touched</text>',
        '<text class="sub" x="16" y="48">A trace of order 1043 as a timeline: each bar is one part\'s work (made-up timings)</text>',
    ]
    xmax = 2500
    for v in range(0, xmax + 1, 500):
        x = left + pw * v / xmax
        body.append(f'<line class="grid" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 8}" y2="{top + rh * len(TRACE)}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top - 14}" text-anchor="middle">{v / 1000:.1f} s</text>')
    for i, (name, a, b, hi) in enumerate(TRACE):
        y = top + rh * i
        body.append(f'<text class="{"cellt" if hi else "small"}" x="{lx + (12 if i else 0)}" y="{y + 21}">{name}</text>')
        x0, x1 = left + pw * a / xmax, left + pw * b / xmax
        body.append(f'<rect class="{"bar-hi" if hi else "bar-n"}" x="{x0:.1f}" y="{y + 9}" width="{max(x1 - x0, 3):.1f}" height="16" rx="3">'
                    f'<title>{name}: {a} to {b} ms ({b - a} ms)</title></rect>')
        lab = f"{b - a:,} ms"
        if x1 + 8 + 7 * len(lab) < w:
            body.append(f'<text class="tick" x="{x1 + 6:.1f}" y="{y + 21}">{lab}</text>')
        else:
            body.append(f'<text class="tick" x="{x0 + 6:.1f}" y="{y + 5}">{lab}</text>')
    y = top + rh * len(TRACE) + 24
    for line in [
        "Read it like the expert: the whole request took 2.45 s, and 1.94 s of that was the order function waiting",
        "for the payment provider. The database calls took 60 ms and 50 ms. Fix or ask about the slow part, not the",
        "server. Timings are made up; the layout follows what the X-Ray Developer Guide describes (traces, segments).",
    ]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg("08-03-trace-waterfall.svg", w, y + 10, "A trace of one bakery order as a timeline",
        "A timeline of one request, order 1043, from 0 to 2.5 seconds, made-up timings. Web server on EC2 handling "
        "POST /order: 0 to 2,450 ms. Order function in Lambda: 90 to 2,400 ms. Inside it: read the cake's price from "
        "RDS, 140 to 200 ms (60 ms); charge the card at the payment provider, 230 to 2,170 ms (1,940 ms, "
        "highlighted); save the order to RDS, 2,200 to 2,250 ms (50 ms). A note says the whole request took 2.45 "
        "seconds and 1.94 of them were spent waiting for the payment provider, so that is the part to fix or ask "
        "about.", body, style=STYLE)


if __name__ == "__main__":
    three_questions()
    trace_waterfall()
