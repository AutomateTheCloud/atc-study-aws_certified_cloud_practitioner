#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 08.03 (watching workloads) as SVG.

Usage: python3 -I source/charts/08-03-charts.py
Writes images/08-03-*.svg. Facts, checked 2026-10-24: Amazon CloudWatch User
Guide (metrics concepts: metrics are Regional and kept 15 months, 1-minute data
15 days, 5-minute data 63 days, 1-hour data 455 days; alarms: states OK, ALARM
and INSUFFICIENT_DATA, actions run on a state change; alarm history kept 30
days); CloudWatch Logs User Guide (log data kept indefinitely by default);
AWS X-Ray Developer Guide (traces, segments, trace map; trace data kept 30
days); AWS CloudTrail User Guide (Event history: 90 days of management events
per Region, no charge to view). The bakery, its numbers, the error counts and
the trace timings are made up for teaching. Our own design: no AWS logos,
icons, trade dress or AWS diagrams.
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


# ---------------------------------------------------------------- alarm timeline

# Errors (Sum) for the order function, per 5-minute period from 12:00 to 15:00. Made up.
ERRORS = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,   # 12:00-12:55
          0, 0, 4, 7, 9, 6, 2, 0, 0, 1, 0, 0,   # 13:00-13:55
          0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]   # 14:00-14:55
THRESHOLD = 3  # ALARM when one 5-minute period has 3 or more errors


def label(i):
    m = i * 5
    return f"{12 + m // 60}:{m % 60:02d}"


def states():
    return ["ALARM" if e >= THRESHOLD else "OK" for e in ERRORS]


def alarm_timeline():
    st = states()
    first = st.index("ALARM")
    last = len(st) - 1 - st[::-1].index("ALARM")
    assert (label(first), label(last + 1)) == ("13:10", "13:30"), "must match the lesson text"
    assert max(ERRORS) == 9 and label(ERRORS.index(9)) == "13:20"
    w, left, top, pw, ph, ymax = 680, 56, 104, 600, 200, 10
    body = [
        '<text class="title" x="16" y="28">An alarm acts when its state changes, not on every bad period</text>',
        '<text class="sub" x="16" y="48">Errors in the bakery\'s order function per 5 minutes, one afternoon (made-up figures)</text>',
        f'<rect class="bar-hi" x="16" y="64" width="12" height="12" rx="2"/><text x="34" y="74">Period at or above the threshold</text>',
        f'<rect class="bar-n" x="262" y="64" width="12" height="12" rx="2"/><text x="280" y="74">Below it</text>',
        f'<line class="thr" x1="360" x2="384" y1="70" y2="70"/><text x="390" y="74">Threshold: {THRESHOLD} errors</text>',
    ]
    for v in range(0, ymax + 1, 2):
        y = top + ph - ph * v / ymax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{y:.1f}" y2="{y:.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{y + 4:.1f}" text-anchor="end">{v}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 10}">Errors</text>')
    band = pw / len(ERRORS)
    for i, e in enumerate(ERRORS):
        x = left + band * i + 2
        if e:
            hgt = ph * e / ymax
            cls = "bar-hi" if e >= THRESHOLD else "bar-n"
            r = min(4, hgt)
            y0 = top + ph - hgt
            body.append(f'<path class="{cls}" d="M{x:.1f},{top + ph:.1f} L{x:.1f},{y0 + r:.1f} Q{x:.1f},{y0:.1f} {x + r:.1f},{y0:.1f} '
                        f'L{x + band - 4 - r:.1f},{y0:.1f} Q{x + band - 4:.1f},{y0:.1f} {x + band - 4:.1f},{y0 + r:.1f} L{x + band - 4:.1f},{top + ph:.1f} Z">'
                        f'<title>{label(i)} to {label(i + 1)}: {e} error{"s" if e != 1 else ""}</title></path>')
    for i in range(0, len(ERRORS) + 1, 6):
        body.append(f'<text class="tick" x="{left + band * i:.1f}" y="{top + ph + 18}" text-anchor="middle">{label(i)}</text>')
    ty = top + ph - ph * THRESHOLD / ymax
    body.append(f'<line class="thr" x1="{left}" x2="{left + pw}" y1="{ty:.1f}" y2="{ty:.1f}"/>')
    peak = ERRORS.index(9)
    body.append(f'<text class="lab" x="{left + band * peak + band / 2 + 14:.1f}" y="{top + ph - ph * 9 / ymax + 4:.1f}">9 errors, 13:20 to 13:25</text>')
    # State band.
    sy = top + ph + 36
    body.append(f'<text class="rowl" x="16" y="{sy + 17}">State</text>')
    runs, start = [], 0
    for i in range(1, len(st) + 1):
        if i == len(st) or st[i] != st[start]:
            runs.append((st[start], start, i))
            start = i
    for s, a, b in runs:
        rect(body, "alarm" if s == "ALARM" else "okband", left + band * a, sy, band * (b - a) - 2, 26, 4)
        body.append(f'<text class="cellt" x="{left + band * (a + b) / 2:.1f}" y="{sy + 17}" text-anchor="middle">{s}</text>')
    # The two actions.
    ay = sy + 46
    xa, xb = left + band * first, left + band * (last + 1)
    for x in (xa, xb):
        body.append(f'<line class="tick-line" x1="{x:.1f}" x2="{x:.1f}" y1="{sy + 28}" y2="{ay - 12}"/>')
    text_lines(body, xa - 4, ay, ["13:10 OK → ALARM:", "email to the owner"], cls="small", dy=15, anchor="end")
    text_lines(body, xb + 4, ay, ["13:30 ALARM → OK:", "an “all clear” email, if you asked for one"], cls="small", dy=15)
    y = ay + 46
    for line in [
        "Four bad periods, one email: actions run when the state changes. Drawn by period; in practice each change",
        "comes shortly after the period ends. From the CloudWatch User Guide (alarms), checked 2026-10-24.",
    ]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    rows = ", ".join(f"{label(i)} {e}" for i, e in enumerate(ERRORS) if e)
    svg("08-03-alarm-timeline.svg", w, y + 10,
        "Errors per 5 minutes against an alarm threshold, with the alarm's state",
        "Bar chart, made-up figures: errors in the bakery's order function per 5-minute period from 12:00 to 15:00, "
        f"with a dashed threshold line at {THRESHOLD} errors. Periods with errors: {rows}; all other periods have 0. "
        "The four periods from 13:10 to 13:30 are at or above the threshold and are highlighted; the peak is 9 "
        "errors between 13:20 and 13:25. Below the bars, the alarm's state: OK until 13:10, ALARM from 13:10 to "
        "13:30, OK after. Two marks show the actions: at 13:10 the change from OK to ALARM sends an email to the "
        "owner; at 13:30 the change from ALARM to OK can send an all-clear email if one was configured. A note says "
        "four bad periods produce one email, because actions run when the state changes.",
        body, style=STYLE)


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


# ---------------------------------------------------------------- how long records last

KEEP = [  # (record, days or None for no end, note)
    ("AWS X-Ray traces", 30, "30 days"),
    ("CloudWatch alarm history", 30, "30 days"),
    ("CloudTrail Event history", 90, "90 days, management events, per Region"),
    ("CloudWatch metrics", 455, "15 months; detail coarsens after 15 and 63 days"),
    ("CloudWatch Logs", None, "kept until you set retention (the default never expires)"),
]


def retention():
    w, left, pw, top, rh, xmax = 680, 196, 360, 96, 50, 500
    body = [
        '<text class="title" x="16" y="28">How long each record lasts by default</text>',
        '<text class="sub" x="16" y="48">Days AWS keeps each kind of record unless you send it somewhere else or change a setting</text>',
    ]
    for v in range(0, xmax + 1, 100):
        x = left + pw * v / xmax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 8}" y2="{top + rh * len(KEEP)}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top - 14}" text-anchor="middle">{v}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 14}">Days</text>')
    for i, (name, days, note) in enumerate(KEEP):
        y = top + rh * i
        body.append(f'<text class="cellt" x="16" y="{y + 22}">{name}</text>')
        below = days is None or days > 300
        if days is None:
            x1 = left + pw + 14
            body.append(f'<path class="bar-hi" d="M{left},{y + 10} L{x1 - 10},{y + 10} L{x1},{y + 18} L{x1 - 10},{y + 26} L{left},{y + 26} Z">'
                        f'<title>{name}: {note}</title></path>')
            body.append(f'<text class="small" x="{left + 6}" y="{y + 42}">{note}</text>')
        else:
            x1 = left + pw * days / xmax
            r = 4
            body.append(f'<path class="bar-n" d="M{left},{y + 10} L{x1 - r:.1f},{y + 10} Q{x1:.1f},{y + 10} {x1:.1f},{y + 10 + r} '
                        f'L{x1:.1f},{y + 26 - r} Q{x1:.1f},{y + 26} {x1 - r:.1f},{y + 26} L{left},{y + 26} Z"><title>{name}: {note}</title></path>')
            if below:
                body.append(f'<text class="small" x="{left + 6}" y="{y + 42}">{note}</text>')
            else:
                body.append(f'<text class="small" x="{x1 + 8:.1f}" y="{y + 22}">{note}</text>')
    y = top + rh * len(KEEP) + 22
    for line in [
        "To keep account activity longer than 90 days, create a CloudTrail trail: it delivers events to an S3 bucket",
        "you keep. Logs grow until you set retention (Lab 07). From the CloudWatch, CloudWatch Logs, X-Ray and",
        "CloudTrail user guides, checked 2026-10-24.",
    ]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg("08-03-retention.svg", w, y + 10, "How long CloudWatch, X-Ray and CloudTrail keep records by default",
        "Horizontal bars, in days. AWS X-Ray traces: 30 days. CloudWatch alarm history: 30 days. CloudTrail Event "
        "history: 90 days of management events, per Region. CloudWatch metrics: 455 days, about 15 months, with "
        "detail coarsening after 15 and 63 days. CloudWatch Logs, highlighted, with an arrow running off the chart: "
        "kept until you set retention, because the default never expires. A note says that to keep account activity "
        "longer than 90 days, you create a CloudTrail trail, which delivers events to an S3 bucket you keep.", body, style=STYLE)


if __name__ == "__main__":
    three_questions()
    alarm_timeline()
    trace_waterfall()
    retention()
