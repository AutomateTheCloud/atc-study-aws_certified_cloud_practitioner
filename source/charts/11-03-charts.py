#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for lesson 11.03 (estimate, watch, analyze) as SVG.

Usage: python3 -I source/charts/11-03-charts.py
Writes images/11-03-tools-compared.svg.

Facts and figures:
- The bakery's January bill is made up for teaching: $112 for the month, about what lesson 11.01
  expects once December's customers leave. The forgotten instance uses a US East (N. Virginia)
  price from the AWS Price List offer file retrieved 2026-10-24 (research repo,
  sources/raw/pricing/compute-networking-us-east-1-summary.tsv): one r7g.large, Linux, On-Demand,
  $0.1071 an hour, from January 11 (21 days, $53.98). January total $165.98.
- Budgets: alerts on actual and forecasted cost; data updated up to three times a day, typically
  8-12 hours apart ("Managing your costs with AWS Budgets", AWS Cost Management User Guide, checked
  2026-10-24). The day the forecast alert fires is illustrative.
- Cost Explorer: the current month and up to 13 previous months by default; up to 38 months of
  multi-year data at monthly granularity if enabled; hourly data for the previous 14 days if
  enabled (paid); forecasts for the next 18 months ("Analyzing your costs with AWS Cost Explorer",
  "Exploring more data for advanced cost analysis", "Multi-year data at monthly granularity",
  checked 2026-10-24).
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import line_key, make_style, svg, swatch, text_lines, top_rounded, wrap  # noqa: E402

BASE_DAY = 112 / 31  # made up: about what lesson 11.01 expects January to cost
TEST_DAY = 24 * 0.1071  # one r7g.large, Linux, On-Demand
START, ANOMALY = 11, 12  # the instance starts on January 11; the anomaly alert day is illustrative

STYLE = make_style(
    light_extra=" --base:#a8a69d; --cell:#fcfcfb; --hit:#fbe1d6; --band:#d9e8fb; --band2:#eeeeea;",
    dark_extra=" --base:#6b6a65; --cell:#1a1a19; --hit:#4d2716; --band:#1b3554; --band2:#2c2c2a;",
    rules_extra="""
  .base { fill: var(--base); }
  .line-dash { stroke: var(--ink2); stroke-width: 1.5; fill: none; stroke-dasharray: 5 4; }
  .line-s2 { stroke: var(--s2); stroke-width: 2; fill: none; stroke-dasharray: 6 4; }
  .dot-s2 { fill: var(--s2); stroke: var(--surface); stroke-width: 2; }
  .dot-ink { fill: var(--ink); stroke: var(--surface); stroke-width: 2; }
  .cell { fill: var(--cell); stroke: var(--grid); stroke-width: 1; }
  .hit { fill: var(--hit); stroke: var(--ink); stroke-width: 2; }
  .band { fill: var(--band); stroke: var(--s1); stroke-width: 1.5; }
  .band2 { fill: var(--band2); stroke: var(--axis); stroke-width: 1; stroke-dasharray: 4 3; }
  .fc { fill: none; stroke: var(--s2); stroke-width: 2; stroke-dasharray: 6 4; }
  .head { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .ct { fill: var(--ink); font-size: 12px; }
  .ctb { fill: var(--ink); font-size: 12.5px; font-weight: 700; }
  .note { fill: var(--muted); font-size: 11.5px; }""")


def tools_compared():
    cols = [("Tool", 150), ("Stage", 92), ("The question it answers", 236), ("Acts on its own?", 166)]
    rows = [
        ("AWS Pricing Calculator", "Before you build", "What will this design cost a month?", "No: an estimate only"),
        ("AWS Budgets", "While it runs", "Are we heading past our limit? Tell me.", "Emails only, unless you add a budget action"),
        ("AWS Cost Anomaly Detection", "While it runs", "Is spending unusual for us? Tell me.", "No: alerts only"),
        ("AWS Cost Explorer", "After the fact", "Where did the money go, and where is it heading?", "No: charts, forecasts, recommendations"),
        ("Cost and Usage Report (CUR 2.0) in Data Exports", "Raw detail", "Every line item, to query my own way", "No: files in your S3 bucket"),
    ]
    w, x0, top, rh = 680, 16, 82, 56
    body = ['<text class="title" x="16" y="28">Five cost tools, five questions</text>',
            '<text class="sub" x="16" y="48">The highlighted cell: only Budgets can act, and only if you set an action</text>']
    x = x0
    for name, cw in cols:
        body.append(f'<text class="head" x="{x + 6}" y="{top - 10}">{name}</text>')
        x += cw
    for i, row in enumerate(rows):
        y = top + i * rh
        x = x0
        for j, (text, (_, cw)) in enumerate(zip(row, cols)):
            cls = "hit" if (j == 3 and i == 1) else "cell"
            body.append(f'<rect class="{cls}" x="{x + 2}" y="{y + 2}" width="{cw - 4}" height="{rh - 4}" rx="4"/>')
            lines = wrap(text, max(12, int((cw - 12) / 6.4)))
            t = "ctb" if j == 0 else "ct"
            yy = y + rh / 2 + 4 - (len(lines) - 1) * 7.5
            text_lines(body, x + 8, yy, lines, cls=t, dy=15)
            x += cw
    yb = top + len(rows) * rh + 22
    body.append(f'<text class="note" x="16" y="{yb}">An action can apply an IAM policy or an SCP, or stop chosen EC2 or RDS instances. Checked 2026-10-24.</text>')
    svg("11-03-tools-compared.svg", w, yb + 18,
        "Five cost tools compared: the stage each serves, the question it answers, and whether it acts",
        "A grid with five rows. AWS Pricing Calculator: before you build; what will this design cost a month; no, an "
        "estimate only. AWS Budgets: while it runs; are we heading past our limit, tell me; emails only, unless you add "
        "a budget action, highlighted. AWS Cost Anomaly Detection: while it runs; is spending unusual for us, tell me; "
        "no, alerts only. AWS Cost Explorer: after the fact; where did the money go and where is it heading; no, charts, "
        "forecasts and recommendations. Cost and Usage Report (CUR 2.0) in Data Exports: raw detail; every line item, to "
        "query my own way; no, files in your S3 bucket. A note says an action can apply an IAM policy or an SCP, or stop "
        "chosen EC2 or RDS instances.",
        body, style=STYLE)


if __name__ == "__main__":
    tools_compared()
