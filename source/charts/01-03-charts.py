#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 01.03 (files vs databases) as SVG.

Usage: python3 -I source/charts/01-03-charts.py
Writes images/01-03-*.svg. Facts, checked 2026-10-24: file systems keep files
in a tree of folders (AWS, "What is cloud file storage?"); relational databases
keep records in tables of rows and columns, with a primary key per row and
foreign keys that point to another table's primary key, and are queried in SQL
(AWS, "What is a relational database?"). The bakery's orders, customers and
phone numbers (555-01xx, a range kept for fiction) are made up for teaching.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines  # noqa: E402

STYLE = make_style(
    light_extra=" --hi-fill:#d9e8fb; --n-fill:#f1f0ec;",
    dark_extra=" --hi-fill:#1b3554; --n-fill:#252523;",
    rules_extra="""
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 1.8; }
  .hicell { fill: var(--hi-fill); stroke: none; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .frame { fill: none; stroke: var(--ink); stroke-width: 1.8; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .zlab { fill: var(--muted); font-size: 12px; }
  .mono { fill: var(--ink); font-size: 12px; font-family: ui-monospace, "SFMono-Regular", Menlo, monospace; }
  .monoh { fill: var(--ink); font-size: 12px; font-weight: 700; font-family: ui-monospace, "SFMono-Regular", Menlo, monospace; }
  .arrlab { fill: var(--ink2); font-size: 12px; font-style: italic; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .link { stroke: var(--s1); stroke-width: 1.8; fill: none; }
  .arrowhead { fill: var(--ink2); }
  .linkhead { fill: var(--s1); }""")


def arrow(body, x1, y1, x2, y2, cls="arrow", head="arrowhead"):
    body.append(f'<line class="{cls}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="{head}" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


ORDERS = [("1041", "birthday cake", "2026-12-24", "7"),
          ("1042", "lemon cake", "2026-12-23", "8"),
          ("1043", "fruit cake", "2026-12-24", "7")]


def table(body, x, y, cols, rows, key_col=None, match=None, rh=26):
    """Draw a small table: cols is [(name, width)], rows lists of strings. Returns (bottom, x positions)."""
    total = sum(wd for _, wd in cols)
    rect(body, "plain", x, y, total, rh * (len(rows) + 1), 4)
    xs, cx = [], x
    for c, (name, wd) in enumerate(cols):
        if c == key_col:
            body.append(f'<rect class="hicell" x="{cx + 1:.1f}" y="{y + 1:.1f}" width="{wd - 2:.1f}" height="{rh - 2}"/>')
        body.append(f'<text class="monoh" x="{cx + 8:.1f}" y="{y + 17}">{name}</text>')
        xs.append(cx)
        cx += wd
    body.append(f'<line class="axis" x1="{x}" x2="{x + total}" y1="{y + rh}" y2="{y + rh}"/>')
    for r, row in enumerate(rows):
        ry = y + rh * (r + 1)
        if r:
            body.append(f'<line class="grid" x1="{x + 1}" x2="{x + total - 1}" y1="{ry}" y2="{ry}"/>')
        for c, val in enumerate(row):
            body.append(f'<text class="mono" x="{xs[c] + 8:.1f}" y="{ry + 17}">{val}</text>')
        if match and match(row):
            body.append(f'<text class="cellt" x="{x + total + 8}" y="{ry + 17}">match</text>')
    return y + rh * (len(rows) + 1), xs


def big_picture():
    """The same three orders as files and as a table, answering one question."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">The same orders, kept two ways</text>',
        '<text class="sub" x="16" y="48">Question: which orders are for pickup on December 24?</text>',
    ]
    top, ph = 70, 318
    # Files panel.
    fx, fw = 16, 230
    rect(body, "frame", fx, top, fw, ph, 10)
    body.append(f'<text class="head" x="{fx + 14}" y="{top + 24}">Files</text>')
    # Folder: a tab and a body.
    body.append(f'<path class="n" d="M{fx + 14},{top + 44} L{fx + 70},{top + 44} L{fx + 78},{top + 52} L{fx + fw - 14},{top + 52} '
                f'L{fx + fw - 14},{top + 196} L{fx + 14},{top + 196} Z"/>')
    body.append(f'<text class="cellt" x="{fx + 22}" y="{top + 70}">Folder: orders</text>')
    for i in range(3):
        y = top + 84 + i * 36
        rect(body, "plain", fx + 26, y, fw - 52, 28, 4)
        body.append(f'<text class="mono" x="{fx + 36}" y="{y + 19}">order-104{i + 1}.txt</text>')
        body.append(f'<text class="small" x="{fx + fw - 34}" y="{y + 19}" text-anchor="end">open {i + 1}</text>')
    rect(body, "plain", fx + 26, top + 224, fw - 52, 40)
    body.append(f'<text class="cellt" x="{fx + fw / 2}" y="{top + 249}" text-anchor="middle">Your program</text>')
    arrow(body, fx + fw / 2, top + 223, fx + fw / 2, top + 198)
    text_lines(body, fx + 14, top + 286, ["Opens and reads every file,", "however few of them match"], cls="small", dy=16)
    # Database panel (highlighted).
    dx, dw = 262, 402
    rect(body, "hi", dx, top, dw, ph, 10)
    body.append(f'<text class="head" x="{dx + 14}" y="{top + 24}">Database</text>')
    rect(body, "plain", dx + 14, top + 40, 140, 40)
    body.append(f'<text class="cellt" x="{dx + 84}" y="{top + 65}" text-anchor="middle">Your program</text>')
    rect(body, "n", dx + dw - 168, top + 40, 154, 40)
    body.append(f'<text class="cellt" x="{dx + dw - 91}" y="{top + 65}" text-anchor="middle">Database engine</text>')
    arrow(body, dx + 155, top + 52, dx + dw - 169, top + 52)
    arrow(body, dx + dw - 169, top + 70, dx + 155, top + 70)
    body.append(f'<text class="arrlab" x="{dx + 186}" y="{top + 100}" text-anchor="middle">one query in, two rows back</text>')
    body.append(f'<text class="zlab" x="{dx + 14}" y="{top + 132}">Table: orders</text>')
    cols = [("order_id", 68), ("cake", 102), ("pickup_date", 92), ("cust_id", 66)]
    bottom, _ = table(body, dx + 14, top + 140, cols, ORDERS, match=lambda r: r[2] == "2026-12-24")
    text_lines(body, dx + 14, top + 286, ["The engine finds the matching rows itself;",
                                         "only the answer comes back"], cls="small", dy=16)
    y = top + ph + 24
    body.append(f'<text class="note" x="16" y="{y}">The orders are made up for teaching. cust_id is short for customer_id.</text>')
    svg("01-03-big-picture.svg", w, y + 16,
        "The same orders kept as files and in a database",
        "Two panels under the question 'which orders are for pickup on December 24?'. Files: a folder named orders "
        "holds three files, order-1041.txt, order-1042.txt and order-1043.txt; your program opens and reads every "
        "file, one, two, three, however few match. Database, highlighted: your program sends one query to the "
        "database engine and gets two rows back. The engine holds a table named orders with columns order_id, cake, "
        "pickup_date and customer_id: 1041, birthday cake, 2026-12-24, 7; 1042, lemon cake, 2026-12-23, 8; 1043, "
        "fruit cake, 2026-12-24, 7. Rows 1041 and 1043 are marked as matches.", body, style=STYLE)


def two_tables():
    """An orders table whose customer_id points to rows in a customers table."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Two tables, linked by a key</text>',
        '<text class="sub" x="16" y="48">Each order names its customer by customer_id; the customer\'s details are kept once</text>',
    ]
    top = 96
    ocols = [("order_id", 74), ("cake", 108), ("pickup_date", 100), ("customer_id", 98)]
    body.append(f'<text class="head" x="16" y="{top - 12}">orders</text>')
    obottom, oxs = table(body, 16, top, ocols, ORDERS, key_col=None, rh=32)
    body.append(f'<text class="zlab" x="24" y="{obottom + 18}">primary key: order_id</text>')
    ccols = [("customer_id", 98), ("name", 56), ("phone", 84)]
    cx = 16 + sum(wd for _, wd in ocols) + 46
    body.append(f'<text class="head" x="{cx}" y="{top - 12}">customers</text>')
    customers = [("7", "Ana", "555-0107"), ("8", "Ben", "555-0108")]
    cbottom, cxs = table(body, cx, top, ccols, customers, key_col=0, rh=32)
    body.append(f'<text class="cellt" x="{cx + 8}" y="{cbottom + 18}">primary key: customer_id</text>')
    # Links from orders 1041 and 1043 (customer 7) to Ana's row.
    ox_end = 16 + sum(wd for _, wd in ocols)
    ana_y = top + 32 + 16
    for r in (0, 2):
        y = top + 32 * (r + 1) + 16
        body.append(f'<path class="link" d="M{ox_end - 40},{y} L{ox_end + 18},{y} L{ox_end + 18},{ana_y} L{cx - 9},{ana_y}"/>')
    arrow(body, cx - 12, ana_y, cx - 1, ana_y, cls="link", head="linkhead")
    y = max(obottom, cbottom) + 52
    body.append(f'<text class="small" x="16" y="{y}">Ana\'s phone number is stored once. Change it there, and both of her orders see the new number.</text>')
    y += 26
    body.append(f'<text class="note" x="16" y="{y}">The people, orders and numbers are made up for teaching; 555-01xx numbers are kept for fiction.</text>')
    svg("01-03-two-tables.svg", w, y + 16,
        "An orders table linked to a customers table",
        "Two tables. orders, with primary key order_id, and columns cake, pickup_date and customer_id: 1041, birthday "
        "cake, 2026-12-24, customer 7; 1042, lemon cake, 2026-12-23, customer 8; 1043, fruit cake, 2026-12-24, "
        "customer 7. customers, with primary key customer_id, highlighted, and columns name and phone: 7, Ana, "
        "555-0107; 8, Ben, 555-0108. Lines run from the customer_id of orders 1041 and 1043 to Ana's row. A note "
        "says Ana's phone number is stored once, so a change there reaches both orders.", body, style=STYLE)


if __name__ == "__main__":
    big_picture()
    two_tables()
