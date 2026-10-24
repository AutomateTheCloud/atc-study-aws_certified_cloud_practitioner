#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphic for Simulation S12 (input-to-output matcher) as SVG.

Usage: python3 -I source/charts/10-06-charts.py
Writes images/10-06-six-requests.svg: the bakery owner's six requests, each with what
goes in, what must come out, the service that fits and the likeliest wrong pick.
Facts come from the AWS "What is" pages cited in
guide/10-data-ai-and-more/06-sim-input-output-matcher.md, checked 2026-10-23 and 2026-10-24:
Amazon Quick Sight (formerly QuickSight, part of Amazon Quick), Amazon Lex V2 and its
integration with Amazon Connect Customer (formerly Amazon Connect), Amazon Polly, Amazon
Transcribe, Amazon Textract (AnalyzeExpense for receipts), Amazon Rekognition, Amazon
WorkSpaces, Amazon WorkSpaces Applications (formerly AppStream 2.0), AWS IoT Core and
Amazon Kinesis. The requests are made up for teaching.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines  # noqa: E402

STYLE = make_style(
    light_extra=" --card:#eef4fc;",
    dark_extra=" --card:#1f2a37;",
    rules_extra="""
  .card { fill: var(--card); stroke: var(--s1); stroke-width: 1.5; }
  .req { fill: var(--ink); font-size: 13.5px; font-weight: 600; }
  .k { fill: var(--muted); font-size: 12px; }
  .v { fill: var(--ink2); font-size: 12px; }
  .svc { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .not { fill: var(--ink2); font-size: 12px; font-style: italic; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

# (request, input, output, service lines, not-this line)
CARDS = [
    ("1. Sales dashboard", "sales files in S3, queried with Athena", "charts the owner can read",
     ["Amazon Quick Sight"], "Not Athena alone: it answers queries, draws no charts"),
    ("2. Phone bot", "a caller's voice", "a conversation that understands the request",
     ["Amazon Lex, on a phone line from", "Amazon Connect Customer"], "Not Polly alone: it speaks, it doesn't understand"),
    ("3. Spoken product descriptions", "written text", "lifelike speech",
     ["Amazon Polly"], "Not Transcribe: that turns speech into text"),
    ("4. Receipts turned into text", "photos of paper receipts", "text and fields: supplier, date, total",
     ["Amazon Textract"], "Not Rekognition: it finds text in images, not fields"),
    ("5. Desktops for seasonal staff", "staff on their own devices", "a whole desktop, streamed",
     ["Amazon WorkSpaces"], "Not buying PCs; one app only: WorkSpaces Applications"),
    ("6. Freezer sensors", "temperature readings from devices", "readings in AWS, and an alert",
     ["AWS IoT Core"], "Not Kinesis alone: it streams data, manages no devices"),
]


def card(body, x, y, w, h, c):
    req, inp, out, svc, nott = c
    body.append(f'<rect class="card" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/>')
    body.append(f'<text class="req" x="{x + 12}" y="{y + 22}">{req}</text>')
    body.append(f'<text class="k" x="{x + 12}" y="{y + 42}">In:</text>')
    body.append(f'<text class="v" x="{x + 42}" y="{y + 42}">{inp}</text>')
    body.append(f'<text class="k" x="{x + 12}" y="{y + 59}">Out:</text>')
    body.append(f'<text class="v" x="{x + 42}" y="{y + 59}">{out}</text>')
    yy = text_lines(body, x + 12, y + 80, ["→ " + svc[0]] + ["   " + s for s in svc[1:]], cls="svc", dy=16)
    body.append(f'<text class="not" x="{x + 12}" y="{yy + 2}">{nott}</text>')


def six_requests():
    w = 680
    cw, ch, gap = 320, 122, 12
    x0, y0 = 16, 66
    body = [
        '<text class="title" x="16" y="28">The owner\'s six requests, matched by what goes in and what comes out</text>',
        '<text class="sub" x="16" y="48">Each card: the input, the output she wants, the service, and the likeliest wrong pick</text>',
    ]
    for i, c in enumerate(CARDS):
        col, row = i % 2, i // 2
        card(body, x0 + col * (cw + gap), y0 + row * (ch + gap), cw, ch, c)
    y = y0 + 3 * (ch + gap) + 10
    body.append(f'<text class="note" x="16" y="{y}">Made-up requests for teaching. Service names as of 2026-10-24: Quick Sight was QuickSight; Connect Customer</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">was Amazon Connect; WorkSpaces Applications was AppStream 2.0.</text>')
    svg("10-06-six-requests.svg", w, y + 30,
        "The bakery owner's six requests matched to AWS services",
        "Six cards in two columns. 1, sales dashboard: in, sales files in S3 queried with Athena; out, charts the "
        "owner can read; service, Amazon Quick Sight; not Athena alone, which answers queries but draws no charts. "
        "2, phone bot: in, a caller's voice; out, a conversation that understands the request; service, Amazon Lex "
        "on a phone line from Amazon Connect Customer; not Polly alone, which speaks but doesn't understand. "
        "3, spoken product descriptions: in, written text; out, lifelike speech; service, Amazon Polly; not "
        "Transcribe, which turns speech into text. 4, receipts turned into text: in, photos of paper receipts; "
        "out, text and fields such as supplier, date and total; service, Amazon Textract; not Rekognition, which "
        "finds text in images but not document fields. 5, desktops for seasonal staff: in, staff on their own "
        "devices; out, a whole desktop streamed to them; service, Amazon WorkSpaces; not buying PCs, and if staff "
        "need one app only, WorkSpaces Applications. 6, freezer sensors: in, temperature readings from devices; "
        "out, readings in AWS and an alert; service, AWS IoT Core; not Kinesis alone, which streams data but "
        "doesn't connect and manage devices. Names as of 2026-10-24: Quick Sight was QuickSight, Connect "
        "Customer was Amazon Connect, WorkSpaces Applications was AppStream 2.0.",
        body, style=STYLE)


if __name__ == "__main__":
    six_requests()
