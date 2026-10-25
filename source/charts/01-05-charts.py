#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 01.05 (APIs, the command line and JSON) as SVG.

Usage: python3 -I source/charts/01-05-charts.py
Writes images/01-05-*.svg. The command's parts follow "Command structure in the AWS
CLI" (AWS CLI User Guide, checked 2026-10-24); the JSON is the lesson's own made-up
bakery order. Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

MONO = 'font-family: ui-monospace, "SFMono-Regular", Menlo, Consolas, "DejaVu Sans Mono", monospace;'
STYLE = make_style(rules_extra=f"""
  .codebg {{ fill: none; stroke: var(--axis); stroke-width: 1; }}
  .code {{ {MONO} fill: var(--ink); font-size: 15px; }}
  .code-s {{ {MONO} fill: var(--ink); font-size: 13px; }}
  .code-dim {{ {MONO} fill: var(--muted); font-size: 15px; }}
  .key {{ fill: var(--ink); font-size: 12px; font-weight: 600; }}
  .small {{ fill: var(--ink2); font-size: 12px; }}
  .brk {{ stroke: var(--s1); stroke-width: 2; fill: none; }}
  .mark {{ fill: none; stroke: var(--s1); stroke-width: 1.5; }}""")

CH = 9.03  # width of one monospace character at 15px (measured: DejaVu Sans Mono 0.602 em)
CH_S = 7.83  # at 13px


def command_anatomy():
    """`aws s3 mb s3://... --region us-east-1`, each part bracketed and named."""
    w, h = 680, 372
    body = [
        '<text class="title" x="16" y="28">Anatomy of one AWS CLI command</text>',
        '<text class="sub" x="16" y="48">Read it left to right: which program, which service, what to do, to what, and how</text>',
    ]
    parts = [
        ("$ ", None, None),
        ("aws", "PROGRAM", "The AWS CLI itself"),
        (" ", None, None),
        ("s3", "COMMAND", "Which service: Amazon S3"),
        (" ", None, None),
        ("mb", "SUBCOMMAND", "What to do: make a bucket"),
        (" ", None, None),
        ("s3://example-bakery-photos", "ARGUMENT", "What to do it to: the new bucket's name"),
        (" ", None, None),
        ("--region us-east-1", "OPTION", "A setting: a name with two dashes, then its value"),
    ]
    x0, cy = 28, 112
    body.append(f'<rect class="codebg" x="16" y="{cy - 26}" width="{w - 32}" height="40" rx="6"/>')
    x = x0
    spans = []
    for txt, label, note in parts:
        cls = "code-dim" if txt.startswith("$") else "code"
        body.append(f'<text class="{cls}" x="{x:.1f}" y="{cy}" xml:space="preserve">{txt}</text>')
        if label:
            spans.append((x, x + len(txt) * CH, label, note))
        x += len(txt) * CH
    # brackets under each part, labels staggered on three rows so they never collide
    for i, (a, b, label, note) in enumerate(spans):
        by = cy + 24
        body.append(f'<path class="brk" d="M{a + 1:.1f},{by - 6} L{a + 1:.1f},{by} L{b - 1:.1f},{by} L{b - 1:.1f},{by - 6}"/>')
        mid = (a + b) / 2
        row = [0, 1, 2, 0, 1][i]
        ty = by + 26 + row * 64
        body.append(f'<line class="lead" x1="{mid:.1f}" x2="{mid:.1f}" y1="{by}" y2="{ty - 13}"/>')
        anchor = "start" if mid < 200 else "middle"
        tx = mid - 6 if anchor == "start" else mid
        body.append(f'<text class="key" x="{tx:.1f}" y="{ty}" text-anchor="{anchor}">{label}</text>')
        text_lines(body, tx, ty + 16, wrap(note, 24), cls="small", dy=15, anchor=anchor)
    text_lines(body, 16, h - 14, ["$ is the prompt: the shell showing it is ready. You don't type it."], cls="sub")
    svg("01-05-command-anatomy.svg", w, h,
        "The parts of one AWS CLI command",
        "The command aws s3 mb s3://example-bakery-photos --region us-east-1, after a $ prompt, with each part "
        "bracketed and named. aws: the program, the AWS CLI itself. s3: the command, which service, Amazon S3. mb: the "
        "subcommand, what to do, make a bucket. s3://example-bakery-photos: the argument, what to do it to, the new "
        "bucket's name. --region us-east-1: an option, a setting written as a name with two dashes, then its value. "
        "A footnote says the $ is the prompt, the shell showing it is ready, and you don't type it.",
        body, style=STYLE)


ORDER = [
    ('{', None),
    ('  "order_id": "1042",', "pair"),
    ('  "cupcakes": 14,', "number"),
    ('  "paid": true,', "bool"),
    ('  "toppings": ["sprinkles", "lemon icing"],', "array"),
    ('  "customer": {', "object"),
    ('    "name": "Sam",', None),
    ('    "pickup": "Saturday"', None),
    ('  },', None),
    ('  "note": null', "null"),
    ('}', "outer"),
]
NOTES = {
    "pair": ("NAME : VALUE", "A name in double quotes, a colon, then its value. Commas separate the pairs."),
    "number": ("NUMBER", "No quotes. \"14\" in quotes would be text."),
    "bool": ("TRUE OR FALSE", "Written in lowercase, with no quotes."),
    "array": ("ARRAY", "A list in square brackets, in order, separated by commas."),
    "object": ("NESTED OBJECT", "An object inside an object: the customer's two details."),
    "null": ("NULL", "Means \"no value\". Last pair: no comma after it."),
    "outer": ("OBJECT", "Curly braces hold the whole document: one object."),
}


def json_anatomy():
    w, lh, top = 680, 30, 70
    body = [
        '<text class="title" x="16" y="28">Anatomy of a JSON document</text>',
        '<text class="sub" x="16" y="48">A made-up bakery order: names on the left of each colon, values on the right</text>',
    ]
    codew = 372
    ch = lh * len(ORDER) + 18
    body.append(f'<rect class="codebg" x="16" y="{top}" width="{codew}" height="{ch}" rx="6"/>')
    ys = {}
    y = top + 24
    for txt, tag in ORDER:
        body.append(f'<text class="code-s" x="28" y="{y}" xml:space="preserve">{txt}</text>')
        if tag:
            ys[tag] = (y, 28 + len(txt) * CH_S)
        y += lh
    nx = codew + 40
    ny = top + 22
    for tag in ("pair", "number", "bool", "array", "object", "null", "outer"):
        title, text = NOTES[tag]
        ly, lx = ys[tag]
        ny = max(ny, ly)
        edge = codew + 16
        if lx + 6 < edge:
            body.append(f'<line class="lead" stroke-dasharray="2 3" x1="{lx + 6:.1f}" x2="{edge}" y1="{ly - 4}" y2="{ly - 4}"/>')
        body.append(f'<line class="lead" x1="{edge}" x2="{nx - 8}" y1="{ly - 4}" y2="{ny - 4}"/>')
        body.append(f'<text class="key" x="{nx}" y="{ny}">{title}</text>')
        ny = text_lines(body, nx, ny + 15, wrap(text, 36), cls="small", dy=14) + 8
    h = max(top + ch, ny) + 40
    text_lines(body, 16, h - 14, ["Spaces and line breaks between parts don't matter in JSON; they only make it easier to read."], cls="sub")
    svg("01-05-json-anatomy.svg", w, h,
        "The parts of a small JSON document",
        "A JSON document for a made-up bakery order, with notes. The whole document is one object in curly braces. "
        "\"order_id\": \"1042\" is a name and value pair: a name in double quotes, a colon, then its value, with commas "
        "between pairs; here the value is text in quotes. \"cupcakes\": 14 is a number, with no quotes. \"paid\": true is "
        "a true-or-false value, lowercase, no quotes. \"toppings\": [\"sprinkles\", \"lemon icing\"] is an array, a list in "
        "square brackets. \"customer\" holds a nested object with a name, Sam, and a pickup day, Saturday. \"note\": null "
        "means no value, and as the last pair it has no comma after it. A footnote says spaces and line breaks between "
        "parts don't matter in JSON.",
        body, style=STYLE)


if __name__ == "__main__":
    command_anatomy()
    json_anatomy()
