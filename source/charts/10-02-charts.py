#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 10.02 (AI and machine learning) as SVG.

Usage: python3 -I source/charts/10-02-charts.py
Writes images/10-02-*.svg. Facts come from AWS pages cited in
guide/10-data-ai-and-more/02-ai-and-ml.md, checked 2026-10-23 and 2026-10-24:
the "What is" pages for Amazon Comprehend, Translate, Polly, Transcribe, Lex V2,
Rekognition, Textract (AnalyzeExpense for invoices and receipts), SageMaker AI
(renamed from Amazon SageMaker on 2024-12-03).
The bakery's receipt is made up for teaching,
and the service outputs shown are illustrations, not real API responses.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# AWS service = slot 1 (blue) tint; inputs and outputs = neutral cards; the one
# highlighted element per graphic = slot 2 (orange) outline. Words always name
# each part, so color never carries meaning alone.
STYLE = make_style(
    light_extra=" --aws-fill:#d9e8fb; --hi-fill:#fbe1d6; --card-fill:#f1f0ec;",
    dark_extra=" --aws-fill:#1b3554; --hi-fill:#4d2716; --card-fill:#252523;",
    rules_extra="""
  .aws { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .card { fill: var(--card-fill); stroke: var(--axis); stroke-width: 1; }
  .hi { fill: var(--hi-fill); stroke: var(--s2); stroke-width: 2.5; }
  .panel { fill: none; stroke: var(--axis); stroke-width: 1; }
  .panelhi { fill: none; stroke: var(--s2); stroke-width: 3; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .grp { fill: var(--ink); font-size: 12px; font-weight: 700; letter-spacing: 0.3px; }
  .colh { fill: var(--muted); font-size: 11.5px; font-weight: 600; letter-spacing: 0.5px; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .mono { fill: var(--ink); font-size: 12px; font-family: ui-monospace, Menlo, Consolas, monospace; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .flow { stroke: var(--ink2); stroke-width: 1.8; fill: none; }
  .head-ink { fill: var(--ink2); }
  .spine { stroke: var(--axis); stroke-width: 2; }
  .ring { fill: var(--surface); stroke: var(--s1); stroke-width: 2; }
  .sq { fill: var(--s2); stroke: var(--surface); stroke-width: 2; }
  .today { stroke: var(--ink); stroke-width: 1.5; }
  .date { fill: var(--ink2); font-size: 12px; font-variant-numeric: tabular-nums; }
  .zone { fill: var(--muted); font-size: 11px; font-weight: 600; letter-spacing: 0.5px; }
  .lab2 { fill: var(--ink); font-size: 13px; }""")


def arrow(body, x1, y1, x2, y2):
    """A straight arrow with a filled head at (x2, y2)."""
    a = math.atan2(y2 - y1, x2 - x1)
    ex, ey = x2 - 8 * math.cos(a), y2 - 8 * math.sin(a)
    body.append(f'<path class="flow" d="M{x1:.1f},{y1:.1f} L{ex:.1f},{ey:.1f}"/>')
    p1 = (x2 - 10 * math.cos(a) + 5 * math.sin(a), y2 - 10 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 10 * math.cos(a) - 5 * math.sin(a), y2 - 10 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="head-ink" d="M{x2:.1f},{y2:.1f} L{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z"/>')


def box(body, cls, x, y, w, h, title=None, lines=(), anchor="start"):
    body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    tx = x + w / 2 if anchor == "middle" else x + 10
    yy = y + 18
    if title:
        body.append(f'<text class="boxt" x="{tx}" y="{yy}" text-anchor="{anchor}">{title}</text>')
        yy += 16
    text_lines(body, tx, yy, list(lines), cls="cells", dy=14, anchor=anchor)


GRID = [
    ("Text in", [
        ("Customer reviews or emails", "Amazon Comprehend", "Sentiment, names, places, key phrases, personal data"),
        ("Text in one language", "Amazon Translate", "The same text in another language"),
        ("Text to be read aloud", "Amazon Polly", "Natural-sounding speech (audio)"),
    ]),
    ("Sound in", [
        ("Recorded or live speech", "Amazon Transcribe", "A written transcript"),
    ]),
    ("A conversation", [
        ("A customer typing or talking", "Amazon Lex", "A bot that works out what they want and replies"),
    ]),
    ("Pictures in", [
        ("Photos or video", "Amazon Rekognition", "Objects, scenes, faces, unsafe content"),
        ("Scans of receipts, forms, PDFs", "Amazon Textract", "Text, form fields, tables, receipt totals"),
    ]),
    ("Nothing ready-made fits", [
        ("Your own data", "Amazon SageMaker AI", "A model you build, train and deploy"),
    ]),
]


def input_output_grid():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Choose an AI service by what goes in and what must come out</text>',
        '<text class="sub" x="16" y="48">Read each row left to right. Same input, different output: a different service.</text>',
    ]
    xin, win = 16, 196
    xs, ws = 248, 172
    xo, wo = 452, 212
    rh, gap = 44, 6
    y = 76
    body.append(f'<text class="colh" x="{xin}" y="{y}">WHAT GOES IN</text>')
    body.append(f'<text class="colh" x="{xs}" y="{y}">AWS SERVICE</text>')
    body.append(f'<text class="colh" x="{xo}" y="{y}">WHAT COMES OUT</text>')
    y += 14
    for group, rows in GRID:
        y += 14
        body.append(f'<text class="grp" x="{xin}" y="{y}">{group}</text>')
        y += 8
        for inp, svc, out in rows:
            box(body, "card", xin, y, win, rh, None, wrap(inp, 28))
            body.append(f'<rect class="aws" x="{xs}" y="{y}" width="{ws}" height="{rh}" rx="6"/>')
            body.append(f'<text class="boxt" x="{xs + 10}" y="{y + rh / 2 + 4.5}">{svc}</text>')
            box(body, "card", xo, y, wo, rh, None, wrap(out, 31))
            arrow(body, xin + win + 4, y + rh / 2, xs - 2, y + rh / 2)
            arrow(body, xs + ws + 4, y + rh / 2, xo - 2, y + rh / 2)
            y += rh + gap
    y += 14
    body.append(f'<text class="small" x="16" y="{y}">The first seven are ready-made: AWS trained the model, and you need no machine learning skills.</text>')
    body.append(f'<text class="note" x="16" y="{y + 18}">Our summary of each service\'s AWS documentation, checked 2026-10-23.</text>')
    svg("10-02-input-output-grid.svg", w, y + 32,
        "Ready-made AI services and SageMaker AI, by what goes in and what comes out",
        "A grid of rows, each reading input, AWS service, output. Text in: customer reviews or emails go to "
        "Amazon Comprehend, which returns sentiment, names, places, key phrases and personal data; text in one "
        "language goes to Amazon Translate, which returns the same text in another language; text to be read "
        "aloud goes to Amazon Polly, which returns natural-sounding speech. Sound in: recorded or live speech "
        "goes to Amazon Transcribe, which returns a written transcript. A conversation: a customer typing or "
        "talking goes to Amazon Lex, a bot that works out what they want and replies. Pictures in: photos or "
        "video go to Amazon Rekognition, which returns objects, scenes, faces and unsafe content; scans of "
        "receipts, forms and PDFs go to Amazon Textract, which returns text, form fields, tables and receipt "
        "totals. Nothing ready-made fits: your own data goes to Amazon SageMaker AI, which gives a model you "
        "build, train and deploy. The first seven are ready-made and need no machine learning skills.",
        body, style=STYLE)


def one_receipt_three_services():
    w = 680
    body = [
        '<text class="title" x="16" y="28">One receipt photo, three services, three different answers</text>',
        '<text class="sub" x="16" y="48">The owner\'s request: "turn our supplier receipts into text". Outputs are illustrations.</text>',
    ]
    # The input, top centre
    rx, ry, rw, rh = 250, 64, 180, 112
    box(body, "card", rx, ry, rw, rh, "Photo of a receipt", [])
    for k, (a, b) in enumerate([("Mill &amp; Co.", "2026-10-02"), ("Flour 25 kg", "$41.00"),
                                ("Butter 10 kg", "$43.20"), ("TOTAL", "$84.20")]):
        yy = ry + 42 + 16 * k
        body.append(f'<text class="mono" x="{rx + 14}" y="{yy}">{a}</text>')
        body.append(f'<text class="mono" x="{rx + rw - 14}" y="{yy}" text-anchor="end">{b}</text>')
    pw, ph, top, gap = 210, 238, 216, 13
    panels = [
        ("Amazon Rekognition", "panel", "card",
         ["Sees a picture:", "• labels such as \"paper\"", "  and \"text\", with a", "  confidence score",
          "• words it spots in the", "  image, as loose lines"],
         "No vendor, total or line items"),
        ("Amazon Textract", "panelhi", "hi",
         ["Reads a document:", "• vendor: Mill &amp; Co.", "• date: 2026-10-02",
          "• total: $84.20", "• line items: flour,", "  butter, with prices"],
         "Fits the request"),
        ("Amazon Comprehend", "panel", "card",
         ["Needs text, not a photo.", "Given Textract's text, it", "finds entities, such as",
          "• an organization", "• a date, a quantity", "• any personal data"],
         "A second step, not the first"),
    ]
    for i, (name, pcls, rcls, lines, verdict) in enumerate(panels):
        px = 16 + i * (pw + gap)
        body.append(f'<rect class="{pcls}" x="{px}" y="{top}" width="{pw}" height="{ph}" rx="8"/>')
        box(body, "aws", px + 12, top + 12, pw - 24, 30, name, [], anchor="middle")
        text_lines(body, px + 16, top + 66, lines, cls="small", dy=18)
        box(body, rcls, px + 12, top + ph - 42, pw - 24, 30, verdict, [], anchor="middle")
        arrow(body, rx + rw / 2, ry + rh + 2, px + pw / 2, top - 2)
    y = top + ph + 22
    body.append(f'<text class="note" x="16" y="{y}">Receipt made up for teaching. Textract\'s AnalyzeExpense reads invoices and receipts (checked 2026-10-24).</text>')
    svg("10-02-one-receipt-three-services.svg", w, y + 14,
        "What Rekognition, Textract and Comprehend each return for the same receipt photo",
        "At the top, a made-up photo of a supplier receipt: Mill and Co., 2026-10-02, flour 25 kg $41.00, butter "
        "10 kg $43.20, total $84.20. Arrows lead to three panels. Amazon Rekognition sees a picture: labels such "
        "as paper and text, with a confidence score, and words it spots in the image as loose lines; verdict: no "
        "vendor, total or line items. Amazon Textract, highlighted, reads a document: vendor Mill and Co., date "
        "2026-10-02, total $84.20, and line items flour and butter with prices; verdict: fits the request. "
        "Amazon Comprehend needs text, not a photo; given Textract's text, it finds entities such as an "
        "organization, a date, a quantity and any personal data; verdict: a second step, not the first. The "
        "outputs are illustrations, not real API responses.",
        body, style=STYLE)


if __name__ == "__main__":
    input_output_grid()
    one_receipt_three_services()
