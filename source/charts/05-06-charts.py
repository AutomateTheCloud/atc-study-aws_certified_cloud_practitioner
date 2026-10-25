#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 05.06 (choosing a database) as SVG.

Usage: python3 -I source/charts/05-06-charts.py
Writes images/05-06-*.svg.
- Data shapes: which in-scope AWS database fits which shape of data, from each
  service's "What is" page (RDS, Aurora, DynamoDB, ElastiCache, DocumentDB,
  Neptune, Redshift), checked 2026-10-23. Bakery examples are made up for teaching.
- DynamoDB on-demand: the "On-demand pricing: Simple example" on AWS's DynamoDB
  pricing page (https://aws.amazon.com/dynamodb/pricing/on-demand/, retrieved
  2026-10-23): a new DynamoDB Standard table in US East (N. Virginia); 10,000
  reads and 10,000 writes a day for days 1-10, 2,500,000 of each on day 11,
  50,000 of each a day for days 12-30; $0.625 per million writes, $0.125 per
  million reads; 27 GB average storage with the first 25 GB free and the rest
  at $0.25 per GB-month; $3.16 for the month.
- Transactional vs analytics: RDS and Redshift "What is" pages.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, top_rounded, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --card-fill:#f1f0ec; --tint:#d9e8fb; --tint2:#fbe1d6;",
    dark_extra=" --card-fill:#252523; --tint:#1b3554; --tint2:#4d2716;",
    rules_extra="""
  .card { fill: var(--card-fill); stroke: var(--axis); stroke-width: 1; }
  .pane { fill: var(--tint); stroke: var(--s1); stroke-width: 1.5; }
  .pane2 { fill: var(--tint2); stroke: var(--s2); stroke-width: 1.5; }
  .ico { fill: none; stroke: var(--s1); stroke-width: 1.5; }
  .icof { fill: var(--s1-light); stroke: var(--s1); stroke-width: 1.2; }
  .icot { fill: var(--ink2); font-size: 10.5px; font-family: ui-monospace, Menlo, Consolas, monospace; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .svc { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .ann { fill: var(--ink); font-size: 12px; }""")


def ico_relational(b, x, y):
    for t, (ox, oy) in enumerate(((0, 0), (78, 14))):
        b.append(f'<rect class="ico" x="{x + ox}" y="{y + oy}" width="62" height="40" rx="2"/>')
        b.append(f'<rect class="icof" x="{x + ox}" y="{y + oy}" width="62" height="10" rx="2"/>')
        for r in (20, 30):
            b.append(f'<line class="ico" x1="{x + ox}" x2="{x + ox + 62}" y1="{y + oy + r}" y2="{y + oy + r}"/>')
        b.append(f'<line class="ico" x1="{x + ox + 24}" x2="{x + ox + 24}" y1="{y + oy}" y2="{y + oy + 40}"/>')
    b.append(f'<path class="ico" d="M{x + 62},{y + 25} C{x + 70},{y + 25} {x + 70},{y + 39} {x + 78},{y + 39}"/>')


def ico_keyvalue(b, x, y):
    for i, (k, v) in enumerate((("cart-17", "3 items"), ("cart-18", "1 item"), ("cart-19", "5 items"))):
        yy = y + i * 15
        b.append(f'<rect class="icof" x="{x}" y="{yy}" width="54" height="12" rx="2"/>')
        b.append(f'<text class="icot" x="{x + 4}" y="{yy + 10}">{k}</text>')
        b.append(f'<line class="ico" x1="{x + 58}" x2="{x + 72}" y1="{yy + 6}" y2="{yy + 6}"/>')
        b.append(f'<rect class="ico" x="{x + 76}" y="{yy}" width="60" height="12" rx="2"/>')
        b.append(f'<text class="icot" x="{x + 80}" y="{yy + 10}">{v}</text>')


def ico_document(b, x, y):
    b.append(f'<path class="ico" d="M{x},{y} L{x + 52},{y} L{x + 64},{y + 12} L{x + 64},{y + 46} L{x},{y + 46} Z"/>')
    for i, (ind, wd) in enumerate(((6, 8), (12, 36), (12, 30), (18, 26), (6, 8))):
        b.append(f'<line class="ico" x1="{x + ind}" x2="{x + ind + wd}" y1="{y + 8 + i * 8}" y2="{y + 8 + i * 8}"/>')
    b.append(f'<text class="icot" x="{x + 72}" y="{y + 18}">{{ "name": ...,</text>')
    b.append(f'<text class="icot" x="{x + 78}" y="{y + 32}">"sizes": [...] }}</text>')


def ico_memory(b, x, y):
    # A cylinder (the database) with a small fast box in front of it (the cache).
    cx = x + 98
    b.append(f'<path class="ico" d="M{cx},{y + 8} L{cx},{y + 40} A20,6 0 0 0 {cx + 40},{y + 40} L{cx + 40},{y + 8}"/>')
    b.append(f'<ellipse class="ico" cx="{cx + 20}" cy="{y + 8}" rx="20" ry="6"/>')
    b.append(f'<rect class="icof" x="{x}" y="{y + 10}" width="58" height="28" rx="3"/>')
    b.append(f'<text class="icot" x="{x + 8}" y="{y + 28}">memory</text>')
    b.append(f'<line class="ico" x1="{x + 60}" x2="{cx - 4}" y1="{y + 24}" y2="{y + 24}" stroke-dasharray="3 3"/>')


def ico_graph(b, x, y):
    pts = [(10, 24), (46, 6), (52, 40), (90, 20), (126, 34)]
    for a, c in ((0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (1, 2)):
        b.append(f'<line class="ico" x1="{x + pts[a][0]}" y1="{y + pts[a][1]}" x2="{x + pts[c][0]}" y2="{y + pts[c][1]}"/>')
    for px, py in pts:
        b.append(f'<circle class="icof" cx="{x + px}" cy="{y + py}" r="6"/>')


def ico_warehouse(b, x, y):
    hs = [14, 22, 18, 30, 26, 38, 34, 44]
    for i, h in enumerate(hs):
        b.append(f'<path class="icof" d="{top_rounded(x + i * 16, y + 46 - h, 11, h, 2)}"/>')
    b.append(f'<line class="ico" x1="{x - 2}" x2="{x + 130}" y1="{y + 46}" y2="{y + 46}"/>')


SHAPES = [
    ("Relational", ico_relational, "Tables with rows and columns, linked to each other",
     "orders, customers and order lines", "Amazon RDS, Amazon Aurora"),
    ("Key-value", ico_keyvalue, "Look up one item by its key, fast, at any scale",
     "shopping carts, by cart ID", "Amazon DynamoDB"),
    ("Document", ico_document, "Records stored as JSON documents whose fields can vary",
     "a product catalog where each cake has different options", "Amazon DocumentDB (DynamoDB also stores documents)"),
    ("In-memory", ico_memory, "Copies of hot data held in memory, answered in microseconds",
     "the home page's best sellers; sign-in sessions", "Amazon ElastiCache"),
    ("Graph", ico_graph, "Things and the relationships between them",
     "customers who bought this cake also bought...", "Amazon Neptune"),
    ("Data warehouse", ico_warehouse, "Years of data from many sources, for analysis",
     "sales by month, product and shop over three years", "Amazon Redshift (analytics, not the shop's daily work)"),
]


def data_shapes():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Choose the database by the shape of the data</text>',
        '<text class="sub" x="16" y="48">Six shapes, the AWS database built for each, and a bakery example</text>',
    ]
    cw, gap = 208, 12
    xs = [16 + i * (cw + gap) for i in range(3)]
    ch = 236
    for i, (name, ico, what, ex, svc) in enumerate(SHAPES):
        x, y = xs[i % 3], 66 + (i // 3) * (ch + 12)
        body.append(f'<rect class="card" x="{x}" y="{y}" width="{cw}" height="{ch}" rx="8"/>')
        ico(body, x + 14, y + 14)
        yy = y + 84
        body.append(f'<text class="cellt" x="{x + 12}" y="{yy}">{name}</text>')
        yy = text_lines(body, x + 12, yy + 17, wrap(what, 30), cls="cells", dy=15)
        yy = text_lines(body, x + 12, yy + 4, wrap("Bakery: " + ex, 30), cls="cells", dy=15)
        text_lines(body, x + 12, yy + 6, wrap(svc, 25), cls="svc", dy=15)
    y = 66 + 2 * (ch + 12) + 12
    body.append(f'<text class="note" x="16" y="{y}">From each service\'s documentation, checked 2026-10-23. Bakery examples are made up for teaching.</text>')
    svg("05-06-data-shapes.svg", w, y + 14,
        "Six shapes of data and the AWS database built for each",
        "Six cards in two rows of three, each with a small drawing of the shape. Relational: tables with rows and "
        "columns, linked to each other; bakery example, orders, customers and order lines; Amazon RDS and Amazon "
        "Aurora. Key-value: look up one item by its key, fast, at any scale; shopping carts by cart ID; Amazon "
        "DynamoDB. Document: records stored as JSON documents whose fields can vary; a product catalog where each "
        "cake has different options; Amazon DocumentDB, and DynamoDB also stores documents. In-memory: copies of "
        "hot data held in memory, answered in microseconds; the home page's best sellers and sign-in sessions; "
        "Amazon ElastiCache. Graph: things and the relationships between them; customers who bought this cake "
        "also bought; Amazon Neptune. Data warehouse: years of data from many sources, for analysis; sales by "
        "month, product and shop over three years; Amazon Redshift, for analytics, not the shop's daily work.",
        body, style=STYLE)


PANES = [
    ("Running the shop: transactional", "Amazon RDS or Amazon Aurora", "pane",
     ["\"Save order 1042.\" \"Change this customer's address.\"",
      "A few rows at a time, in milliseconds",
      "Many small reads and writes, all day, from the website",
      "The ordering website's own data, kept up to date"]),
    ("Studying the business: analytics", "Amazon Redshift", "pane2",
     ["\"Total sales by month and product, for three years.\"",
      "Large amounts of data in one query",
      "Fewer, larger queries from analysts and reports",
      "Data copied in from many sources: orders, the till, the website"]),
]
PROWS = ["A typical request", "Each request touches", "The workload", "The data"]


if __name__ == "__main__":
    data_shapes()
