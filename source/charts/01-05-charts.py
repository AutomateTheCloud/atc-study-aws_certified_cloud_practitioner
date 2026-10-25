#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 01.05 (APIs, the command line and JSON) as SVG.

Usage: python3 -I source/charts/01-05-charts.py
Writes images/01-05-*.svg. The JSON is the lesson's own made-up bakery order;
its parts follow RFC 8259. Our own design: no AWS logos, icons, trade dress or AWS diagrams.
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
    json_anatomy()
