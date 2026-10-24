#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphic for Lab 06 (a DynamoDB table) as SVG.

Usage: python3 -I source/charts/05-08-charts.py
Writes images/05-08-cart-table.svg: the lab's three items, grouped by partition key,
with the sort key and the other attributes labeled. The items are the made-up carts
the lab asks you to enter. Key ideas from the Amazon DynamoDB Developer Guide
("Step 1: Create a table in DynamoDB", "What is Amazon DynamoDB?"), checked 2026-10-23.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg  # noqa: E402

STYLE = make_style(
    light_extra=" --grp-fill:#eef4fc; --hl-fill:#d9e8fb;",
    dark_extra=" --grp-fill:#1f2a37; --hl-fill:#1b3554;",
    rules_extra="""
  .grp { fill: var(--grp-fill); stroke: var(--s1); stroke-width: 1.5; }
  .row { fill: var(--surface); stroke: var(--axis); stroke-width: 1; }
  .hl { fill: var(--hl-fill); stroke: var(--s2); stroke-width: 2.5; }
  .colh { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .cell { fill: var(--ink); font-size: 12.5px; font-family: ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace; }
  .cellm { fill: var(--muted); font-size: 12px; font-style: italic; }
  .gl { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .call { fill: var(--ink2); font-size: 12px; }
  .lead { stroke: var(--muted); stroke-width: 1; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

GROUPS = [
    ("cart-1001", [("lemon-tart", "2", "", True), ("rye-loaf", "1", "Happy birthday!", False)]),
    ("cart-1002", [("croissant", "6", "", False)]),
]


def cart_table():
    w = 680
    body = [
        '<text class="title" x="16" y="28">The lab\'s table: items grouped by their partition key</text>',
        '<text class="sub" x="16" y="48">Table clf-lab06-carts. The full key is CartId plus Product; no two items share both.</text>',
    ]
    cx = [40, 156, 270, 350]  # CartId, Product, Quantity, GiftNote
    heads = ["CartId", "Product", "Quantity", "GiftNote"]
    subs = ["partition key", "sort key", "attribute", "attribute"]
    y = 84
    for x, hd, sb in zip(cx, heads, subs):
        body.append(f'<text class="colh" x="{x}" y="{y}">{hd}</text>')
        body.append(f'<text class="call" x="{x}" y="{y + 16}">{sb}</text>')
    y += 30
    rh, gpad = 40, 10
    gx, gw = 26, 498
    for key, items in GROUPS:
        gh = gpad * 2 + len(items) * rh + (len(items) - 1) * 4
        body.append(f'<rect class="grp" x="{gx}" y="{y}" width="{gw}" height="{gh}" rx="6"/>')
        ry = y + gpad
        for prod, qty, note, hl in items:
            cls = "hl" if hl else "row"
            body.append(f'<rect class="{cls}" x="{gx + 8}" y="{ry}" width="{gw - 16}" height="{rh}" rx="4"/>')
            body.append(f'<text class="cell" x="{cx[0]}" y="{ry + 25}">{key}</text>')
            body.append(f'<text class="cell" x="{cx[1]}" y="{ry + 25}">{prod}</text>')
            body.append(f'<text class="cell" x="{cx[2]}" y="{ry + 25}">{qty}</text>')
            if note:
                body.append(f'<text class="cell" x="{cx[3]}" y="{ry + 25}">"{note}"</text>')
            else:
                body.append(f'<text class="cellm" x="{cx[3]}" y="{ry + 25}">(not there)</text>')
            ry += rh + 4
        y += gh + 12
    # Callouts on the right, in reading order, both about the first group (top at y=114).
    rx = gx + gw + 16
    r1, r2 = 114 + gpad + rh / 2, 114 + gpad + rh + 4 + rh / 2  # middles of its two rows
    body.append(f'<line class="lead" x1="{rx - 4}" y1="{r1}" x2="{gx + gw - 8}" y2="{r1}"/>')
    body.append(f'<text class="gl" x="{rx}" y="{r1 + 4}">Get item</text>')
    body.append(f'<text class="call" x="{rx}" y="{r1 + 20}">CartId + Product</text>')
    body.append(f'<text class="call" x="{rx}" y="{r1 + 35}">finds one item</text>')
    body.append(f'<line class="lead" x1="{rx - 4}" y1="{r2 + 6}" x2="{gx + gw}" y2="{r2 + 6}"/>')
    body.append(f'<text class="gl" x="{rx}" y="{r2 + 10}">Query cart-1001</text>')
    body.append(f'<text class="call" x="{rx}" y="{r2 + 26}">finds both items</text>')
    body.append(f'<text class="call" x="{rx}" y="{r2 + 41}">in this group</text>')
    yb = y + 16
    body.append(f'<text class="lab" x="16" y="{yb}">Items in one table don\'t need the same attributes: only rye-loaf has a GiftNote.</text>')
    body.append(f'<text class="note" x="16" y="{yb + 22}">Made-up items for Lab 06. DynamoDB stores key-value and document data without fixed columns</text>')
    body.append(f'<text class="note" x="16" y="{yb + 38}">(Amazon DynamoDB Developer Guide, checked 2026-10-23).</text>')
    svg("05-08-cart-table.svg", w, yb + 52,
        "The Lab 06 table: three cart items grouped by partition key",
        "Table clf-lab06-carts with columns CartId (partition key), Product (sort key), Quantity and GiftNote "
        "(ordinary attributes). Group cart-1001 holds two items: lemon-tart, quantity 2, no gift note, "
        "outlined as the item a Get item finds with CartId and Product together; and rye-loaf, quantity 1, "
        "gift note 'Happy birthday!'. Group cart-1002 holds one item: croissant, quantity 6, no gift note. "
        "Callouts: Get item uses CartId and Product together to find one item; a Query for CartId cart-1001 "
        "alone finds both items in that group. Items don't need the same attributes: only rye-loaf has a GiftNote.",
        body, style=STYLE)


if __name__ == "__main__":
    cart_table()
