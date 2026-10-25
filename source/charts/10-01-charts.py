#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 10.01 (analytics in five verbs) as SVG.

Usage: python3 -I source/charts/10-01-charts.py
Writes images/10-01-*.svg. Facts come from AWS pages cited in
guide/10-data-ai-and-more/01-analytics-in-five-verbs.md, checked 2026-10-24:
What is Amazon Kinesis Data Streams? (several applications read the same
stream); Change the data retention period (24 hours by default, up to 8,760
hours, 365 days); What is Amazon Data Firehose? (delivers streaming data to S3,
Redshift, OpenSearch Service and other destinations; no applications to write;
buffers by size or time); the Firehose FAQ (buffer interval 0 to 900 seconds
for S3 and OpenSearch destinations); the Amazon SQS FAQ (retention 1 minute to
14 days, default 4 days; the consumer deletes a message once processed); the
Kinesis Data Streams FAQ (ordering and replay for several applications; SQS
deletes acknowledged messages); What is AWS Glue? (serverless; Data Catalog used
by Athena, EMR and Redshift Spectrum; crawlers; ETL); What is Amazon Athena? and
When should I use Athena? (serverless SQL on data in S3; Redshift for complex
reports over data from many sources; EMR for custom code with full control of
clusters); What is Amazon EMR?; What is Amazon OpenSearch Service?; What is
Amazon Quick? (Quick Sight is its dashboards and BI feature). Pricing models from
the Athena FAQ, the EMR, Glue and Redshift pricing pages, read 2026-10-23 and
2026-10-24. The bakery is made up for teaching. Our own design: no AWS logos,
icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --hi-fill:#d9e8fb; --n-fill:#f1f0ec; --st-fill:#ecebe6;",
    dark_extra=" --hi-fill:#1b3554; --n-fill:#252523; --st-fill:#262624;",
    rules_extra="""
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 1.5; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .store { fill: var(--st-fill); stroke: var(--axis); stroke-width: 1.2; stroke-dasharray: 6 4; }
  .band { fill: none; stroke: var(--axis); stroke-width: 1; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .verb { fill: var(--ink); font-size: 14px; font-weight: 700; }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .arrlab { fill: var(--ink2); font-size: 11.5px; font-style: italic; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }
  .num { fill: var(--surface); font-size: 13px; font-weight: 700; }
  .numc { fill: var(--s1); stroke: var(--s1); stroke-width: 1.5; }
  .range { fill: var(--s1); }
  .dflt { fill: var(--ink); stroke: var(--surface); stroke-width: 2; }""")


def arrow(body, x1, y1, x2, y2):
    """A straight line with a small filled head at (x2, y2)."""
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


def marker(body, x, y, n):
    body.append(f'<circle class="numc" cx="{x}" cy="{y}" r="11"/>')
    body.append(f'<text class="num" x="{x}" y="{y + 4.5}" text-anchor="middle">{n}</text>')


def chip(body, x, y, w, h, name, desc, cls="n", width=None):
    """A service box: its name in bold, then a short wrapped description."""
    rect(body, cls, x, y, w, h, 6)
    body.append(f'<text class="cellt" x="{x + 10}" y="{y + 20}">{name}</text>')
    text_lines(body, x + 10, y + 37, wrap(desc, width or int(w / 6.6)), cls="small", dy=15)


def pipeline():
    """Big picture: the five verbs, with the services that do each one."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">An analytics pipeline in five verbs</text>',
        '<text class="sub" x="16" y="48">Each AWS analytics service does one job; data flows down the page</text>',
    ]
    lx, mx, mw = 16, 132, 340          # verb column, main column
    sx, sw = 492, 172                  # side column for search
    rows = {}
    y = 72

    def verb(n, name, yy, hh):
        if n:
            marker(body, lx + 11, yy + hh / 2 - 4, n)
            body.append(f'<text class="verb" x="{lx + 28}" y="{yy + hh / 2}">{name}</text>')
        else:
            body.append(f'<text class="rowl" x="{lx + 28}" y="{yy + hh / 2}">{name}</text>')

    # 1 Ingest
    h = 78
    verb(1, "Ingest", y, h)
    chip(body, mx, y, 164, h, "Kinesis Data Streams", "holds a stream of records for your own programs", width=23)
    chip(body, mx + 176, y, 164, h, "Amazon Data Firehose", "delivers a stream to a store, no code", width=24)
    rows["ingest"] = (y, h)
    y += h + 34
    arrow(body, mx + mw / 2, y - 34, mx + mw / 2, y - 2)
    body.append(f'<text class="arrlab" x="{mx + mw / 2 + 8}" y="{y - 14}">records, seconds after they happen</text>')
    # Store
    h = 52
    verb(None, "Lands in", y, h)
    rect(body, "store", mx, y, mw, h, 6)
    body.append(f'<text class="cellt" x="{mx + 10}" y="{y + 21}">Amazon S3: the data lake</text>')
    body.append(f'<text class="small" x="{mx + 10}" y="{y + 39}">files kept as they arrive: CSV, JSON, Parquet</text>')
    rows["store"] = (y, h)
    y += h + 34
    arrow(body, mx + mw / 2, y - 34, mx + mw / 2, y - 2)
    body.append(f'<text class="arrlab" x="{mx + mw / 2 + 8}" y="{y - 14}">files to describe and tidy</text>')
    # 2 Catalog
    h = 78
    verb(2, "Catalog", y, h)
    chip(body, mx, y, mw, h, "AWS Glue",
         "Data Catalog: a table definition for each set of files; crawlers to find them; ETL jobs to clean them",
         cls="hi", width=50)
    rows["catalog"] = (y, h)
    y += h + 34
    arrow(body, mx + mw / 2, y - 34, mx + mw / 2, y - 2)
    body.append(f'<text class="arrlab" x="{mx + mw / 2 + 8}" y="{y - 14}">tables to query</text>')
    # 3 Query
    h = 86
    verb(3, "Query", y, h)
    cw = (mw - 16) / 3
    chip(body, mx, y, cw, h, "Athena", "SQL on files in S3; no servers", width=15)
    chip(body, mx + cw + 8, y, cw, h, "Redshift", "data warehouse for big reports", width=15)
    chip(body, mx + 2 * (cw + 8), y, cw, h, "EMR", "Spark and Hadoop clusters", width=15)
    rows["query"] = (y, h)
    y += h + 34
    arrow(body, mx + mw / 2, y - 34, mx + mw / 2, y - 2)
    body.append(f'<text class="arrlab" x="{mx + mw / 2 + 8}" y="{y - 14}">query results</text>')
    # 5 Visualize
    h = 56
    verb(5, "Visualize", y, h)
    chip(body, mx, y, mw, h, "Amazon Quick Sight", "dashboards and charts for people in the business", width=50)
    rows["vis"] = (y, h)
    y += h
    # 4 Search, the side branch, level with Query.
    qy, qh = rows["query"]
    iy, ih = rows["ingest"]
    marker(body, sx + 11, qy - 40, 4)
    body.append(f'<text class="verb" x="{sx + 28}" y="{qy - 36}">Search</text>')
    chip(body, sx, qy, sw, qh, "OpenSearch Service", "finds words and patterns in text and logs; its own dashboards", width=25)
    # Branch arrow: from Firehose, right then down to Search.
    fx = mx + 340
    body.append(f'<path class="arrow" d="M{fx:.1f},{iy + ih / 2:.1f} L{sx + sw / 2:.1f},{iy + ih / 2:.1f} L{sx + sw / 2:.1f},{qy - 58:.1f}"/>')
    arrow(body, sx + sw / 2, qy - 66, sx + sw / 2, qy - 56)
    text_lines(body, sx + sw / 2 + 8, iy + ih / 2 + 22, ["log records,", "for searching"], cls="arrlab", dy=14)
    y += 26
    body.append(f'<text class="note" x="16" y="{y}">Simplified: real pipelines skip or repeat steps. Redshift can also load data itself, and Quick Sight can</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">read from Redshift or OpenSearch Service. From AWS documentation, checked 2026-10-24.</text>')
    svg("10-01-pipeline.svg", w, y + 30,
        "An analytics pipeline in five verbs, with the AWS services for each",
        "Top to bottom. Step 1, ingest: Amazon Kinesis Data Streams, which holds a stream of records for your own "
        "programs, and Amazon Data Firehose, which delivers a stream to a store with no code. Records flow down, "
        "seconds after they happen, and land in Amazon S3, the data lake, as files such as CSV, JSON or Parquet. "
        "Files flow down to step 2, catalog, highlighted: AWS Glue, whose Data Catalog holds a table definition for "
        "each set of files, with crawlers to find them and ETL jobs to clean them. Tables flow down to step 3, "
        "query: Amazon Athena, SQL on files in S3 with no servers; Amazon Redshift, a data warehouse for big "
        "reports; Amazon EMR, Spark and Hadoop clusters. Query results flow down to step 5, visualize: Amazon "
        "Quick Sight, dashboards and charts for people in the business. A side branch runs from Firehose to step 4, "
        "search: Amazon OpenSearch Service, which finds words and patterns in text and logs and has its own "
        "dashboards; the arrow is labeled log records, for searching. A note says real pipelines skip or repeat "
        "steps, Redshift can load data itself, and Quick Sight can read from Redshift or OpenSearch Service.",
        body, style=STYLE)


def panels(name, title, sub, cols, rows, hi_row, label_w, wrap_w, note, desc):
    """Comparison panels: one column per service, one row per question, one row highlighted."""
    w = 680
    body = [f'<text class="title" x="16" y="28">{title}</text>', f'<text class="sub" x="16" y="48">{sub}</text>']
    n = len(cols)
    gap = 8
    cw = (w - 16 - label_w - gap * (n - 1) - 16) / n
    xs = [16 + label_w + i * (cw + gap) for i in range(n)]
    y = 66
    for x, (cname, _) in zip(xs, cols):
        rect(body, "n", x, y, cw, 32)
        body.append(f'<text class="cellt" x="{x + 8}" y="{y + 21}">{cname}</text>')
    y += 40
    for r, row in enumerate(rows):
        cells = [wrap(c[1][r], wrap_w) for c in cols]
        h = 14 + 15 * max(len(c) for c in cells) + 4
        hi = row == hi_row
        if hi:
            for x in xs:
                rect(body, "hi", x - 3, y + 2, cw + 6, h - 4, 5)
        body.append(f'<line class="grid" x1="16" x2="{w - 16}" y1="{y}" y2="{y}"/>')
        text_lines(body, 16, y + 19, wrap(row, int(label_w / 7)), cls="rowl", dy=15)
        for x, c in zip(xs, cells):
            text_lines(body, x + 8, y + 19, c, cls="cellt" if hi else "small", dy=15)
        y += h
    body.append(f'<line class="grid" x1="16" x2="{w - 16}" y1="{y}" y2="{y}"/>')
    y += 22
    for line in note:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg(name, w, y + 14, title, desc, body, style=STYLE)


QUERY_ROWS = ["Main job", "Where the data is", "Choose it when"]
QUERY_COLS = [
    ("Amazon Athena",
     ["Runs SQL on files where they sit",
      "In S3, left unchanged",
      "Ad hoc questions about files in S3"]),
    ("Amazon Redshift",
     ["Data warehouse: stores data for analysis and runs SQL on it",
      "Loaded into Redshift",
      "Regular, complex reports over years of data from many sources"]),
    ("Amazon EMR",
     ["Runs Spark, Hadoop and similar frameworks",
      "Usually S3, read by your code",
      "Custom big-data code with full control"]),
    ("AWS Glue",
     ["Catalogs and prepares data (ETL); not for asking questions",
      "Wherever it connects; the catalog describes it",
      "Make data findable and clean before others query it"]),
]


def query_compared():
    panels("10-01-query-compared.svg",
           "Athena, Redshift, EMR or Glue: who does what",
           "Three of them answer questions about data; Glue gets the data ready",
           QUERY_COLS, QUERY_ROWS, "Main job", 92, 17,
           ["From the Athena, Redshift, EMR and Glue documentation, checked 2026-10-24."],
           "Four columns compared on three rows. Main job, highlighted: Amazon Athena runs SQL on files where they "
           "sit; Amazon Redshift is a data warehouse that stores data for analysis and runs SQL on it; Amazon EMR "
           "runs Spark, Hadoop and similar frameworks; AWS Glue catalogs and prepares data (ETL) and is not for "
           "asking questions. Where the data is: Athena, in S3, left unchanged; Redshift, loaded into Redshift; "
           "EMR, usually S3, read by your code; Glue, wherever it connects, and its catalog describes it. Choose it "
           "when: Athena, ad hoc questions about files in S3; Redshift, regular complex reports over years of data "
           "from many sources; EMR, custom big-data code with full control; Glue, to make data findable and clean "
           "before others query it.")


if __name__ == "__main__":
    pipeline()
    query_compared()
