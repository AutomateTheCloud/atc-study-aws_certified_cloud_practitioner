#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for lesson 11.03 (estimate, watch, analyze) as SVG.

Usage: python3 -I source/charts/11-03-charts.py
Writes images/11-03-january-daily.svg, images/11-03-budget-month.svg,
images/11-03-explorer-horizon.svg and images/11-03-tools-compared.svg.

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


def january_daily():
    days = list(range(1, 32))
    w, h, left, top, pw, ph, ymax = 680, 432, 56, 112, 520, 220, 8
    body = ['<text class="title" x="16" y="28">January in Cost Explorer: daily cost, grouped</text>',
            '<text class="sub" x="16" y="48">The rest of the bill is flat; one new line starts on January 11 (base made up)</text>']
    swatch(body, 16, 76, "base", "Everything else, about $3.61 a day")
    swatch(body, 290, 76, "s2", "EC2 instances: one r7g.large, $2.57 a day")
    for v in range(0, ymax + 1, 2):
        y = top + ph - ph * v / ymax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{y:.1f}" y2="{y:.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{y + 4:.1f}" text-anchor="end">${v}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 14}">US dollars a day</text>')
    band = pw / len(days)
    bw = band - 4
    for d in days:
        x = left + band * (d - 1) + 2
        hb = ph * BASE_DAY / ymax
        yb = top + ph - hb
        if d >= START:
            ht = ph * TEST_DAY / ymax
            body.append(f'<rect class="base" x="{x:.1f}" y="{yb:.1f}" width="{bw:.1f}" height="{hb:.1f}"><title>{d} Jan: everything else ${BASE_DAY:.2f}</title></rect>')
            body.append(f'<path class="s2" d="{top_rounded(x, yb - ht, bw, ht - 2)}"><title>{d} Jan: r7g.large ${TEST_DAY:.2f}</title></path>')
        else:
            body.append(f'<path class="base" d="{top_rounded(x, yb, bw, hb)}"><title>{d} Jan: everything else ${BASE_DAY:.2f}</title></path>')
        if d in (1, 5, 11, 15, 20, 25, 31):
            body.append(f'<text class="tick" x="{x + bw / 2:.1f}" y="{top + ph + 18}" text-anchor="middle">{d}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2:.1f}" y="{top + ph + 36}" text-anchor="middle">Day of January</text>')
    xa = left + band * (ANOMALY - 1) + band / 2
    ya = top + ph - ph * (BASE_DAY + TEST_DAY) / ymax
    body.append(f'<line class="lead" x1="{xa:.1f}" x2="{xa:.1f}" y1="{ya - 6:.1f}" y2="{top + 4}"/>')
    body.append(f'<text class="ctb" x="{xa + 6:.1f}" y="{top + 14}">Anomaly alert, about January 12</text>')
    text_lines(body, 16, top + ph + 62, [
        "The base is about what lesson 11.01 expected for January ($112 for the month), made up for teaching.",
        "r7g.large, Linux, On-Demand, US East (N. Virginia): $0.1071 an hour as of 2026-10-24. The alert day is illustrative."],
        cls="note", dy=15)
    svg("11-03-january-daily.svg", w, h,
        "January's daily cost: a flat base, then a new r7g.large instance from January 11",
        "Stacked column chart of 31 days of January. Every day has about $3.61 of 'everything else', made up to "
        "match the $112 lesson 11.01 expected for the month. From January 11 each column adds $2.57 for one r7g.large "
        "instance, at $0.1071 an hour in US East (N. Virginia) as of 2026-10-24. A marker on about January 12 "
        "(illustrative) shows when Cost Anomaly Detection would alert.",
        body, style=STYLE)


def budget_month():
    budget = 150

    def cum(d):
        return BASE_DAY * d + TEST_DAY * max(0, d - START + 1)

    total = cum(31)
    assert round(total, 2) == 165.98
    w, h, left, top, pw, ph, ymax = 680, 452, 64, 112, 470, 236, 200
    body = ['<text class="title" x="16" y="28">January against a $150 monthly budget</text>',
            '<text class="sub" x="16" y="48">Month-to-date cost, day by day. Each alert is an email; spending carries on</text>']
    line_key(body, 16, 76, "line-s1", "Actual cost, month to date")
    line_key(body, 250, 76, "line-ink", "Budget: $150")
    line_key(body, 410, 76, "line-dash", "85% alert: $127.50")
    for v in range(0, ymax + 1, 50):
        y = top + ph - ph * v / ymax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{y:.1f}" y2="{y:.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{y + 4:.1f}" text-anchor="end">${v}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 14}">US dollars</text>')

    def X(d):
        return left + pw * d / 31

    def Y(v):
        return top + ph - ph * v / ymax

    for d in (1, 5, 10, 15, 20, 25, 31):
        body.append(f'<text class="tick" x="{X(d):.1f}" y="{top + ph + 18}" text-anchor="middle">{d}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2:.1f}" y="{top + ph + 36}" text-anchor="middle">Day of January</text>')
    for v, cls in ((budget, "line-ink"), (0.85 * budget, "line-dash")):
        body.append(f'<line class="{cls}" x1="{left}" x2="{left + pw}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/>')
    pts = " ".join(f"{X(d):.1f},{Y(cum(d)):.1f}" for d in range(0, 32))
    body.append(f'<polyline class="line-s1" points="{pts}"/>')
    d85 = next(d for d in range(1, 32) if cum(d) >= 0.85 * budget)
    d100 = next(d for d in range(1, 32) if cum(d) >= budget)
    assert (d85, d100) == (25, 29)
    events = [
        (13, "A", "forecast passes $150"),
        (d85, "B", "actual passes $127.50 (85%)"),
        (d100, "C", "actual passes $150 (100%)"),
    ]
    for d, tag, label in events:
        v = cum(d)
        body.append(f'<circle class="dot-ink" cx="{X(d):.1f}" cy="{Y(v):.1f}" r="5"><title>Day {d}: {label}, ${v:,.2f} so far</title></circle>')
        body.append(f'<text class="ctb" x="{X(d) - 10:.1f}" y="{Y(v) - 10:.1f}" text-anchor="end">{tag}</text>')
    body.append(f'<circle class="dot-s1" cx="{X(31):.1f}" cy="{Y(total):.1f}" r="5"/>')
    body.append(f'<text class="lab" x="{X(31) + 10:.1f}" y="{Y(total) + 4:.1f}">${total:,.2f}</text>')
    body.append(f'<text class="lab" x="{left + pw + 10}" y="{Y(budget) + 16:.1f}">$150</text>')
    text_lines(body, 16, top + ph + 62, [
        "A: forecast alert, soon after the instance starts (the day is illustrative). B and C: actual-cost alerts at 85% and 100%.",
        "Budgets data updates up to three times a day, so each email arrives hours after the line is crossed.",
        "No alert stops the instance: the line keeps rising to $165.98 until someone terminates it."], cls="note", dy=15)
    svg("11-03-budget-month.svg", w, h,
        "January's month-to-date cost rising past a $150 budget, with three alert points and no stop",
        "Line chart of month-to-date cost for the 31 days of January: about $3.61 a day until January 10, then about "
        "$6.18 a day once a forgotten r7g.large starts on January 11, ending at $165.98. A solid line marks the $150 "
        "budget and a dashed line the 85% alert at $127.50. Point A, about January 13: the forecast passes $150 and a "
        "forecasted-cost alert is sent (the day is illustrative). Point B, January 25: actual cost passes $127.50. "
        "Point C, January 29: actual cost passes $150. The line keeps rising after every alert, because budget alerts "
        "only send email.",
        body, style=STYLE)


def explorer_horizon():
    # months relative to the current month: -38 .. +18
    w, h, left, pw = 680, 340, 24, 632
    lo, hi = -38, 19
    unit = pw / (hi - lo)

    def X(m):
        return left + (m - lo) * unit

    body = ['<text class="title" x="16" y="28">How far Cost Explorer looks back and ahead</text>',
            '<text class="sub" x="16" y="48">By default: 13 months back (blue) and 18 ahead (dashed). Options you switch on: gray</text>']
    rows = [
        (96, -38, -13, "band2", "Up to 38 months with multi-year data (opt-in, monthly)", "Multi-year data, opt-in: up to 38 months, monthly granularity"),
        (140, -13, 0, "band", "13 months back", "Default history: the previous 13 months, daily or monthly"),
        (140, 0, 1, "hit", "", "The current month"),
        (140, 1, 19, "fc", "Forecast: next 18 months", "Forecast: the next 18 months, with an 80% prediction interval"),
        (184, -0.5, 0, "band2", "", "Hourly data for the last 14 days, opt-in and paid"),
    ]
    for y, a, b, cls, label, tip in rows:
        body.append(f'<rect class="{cls}" x="{X(a):.1f}" y="{y}" width="{(b - a) * unit - 2:.1f}" height="30" rx="4"><title>{tip}</title></rect>')
        if label:
            body.append(f'<text class="ct" x="{X(a) + 8:.1f}" y="{y + 20}">{label}</text>')
    body.append(f'<text class="ct" x="{X(0.5):.1f}" y="{136 - 6}" text-anchor="middle">Now</text>')
    body.append(f'<line class="lead" x1="{X(0.5):.1f}" x2="{X(0.5):.1f}" y1="134" y2="140"/>')
    body.append(f'<text class="ct" x="{X(0) - 8:.1f}" y="{204}" text-anchor="end">Hourly, last 14 days (opt-in, paid)</text>')
    # axis
    ya = 236
    body.append(f'<line class="axis" x1="{left}" x2="{left + pw}" y1="{ya}" y2="{ya}"/>')
    for m in (-36, -24, -12, 0, 12, 18):
        body.append(f'<line class="axis" x1="{X(m):.1f}" x2="{X(m):.1f}" y1="{ya}" y2="{ya + 5}"/>')
        lab = "now" if m == 0 else (f"{m}" if m < 0 else f"+{m}")
        body.append(f'<text class="tick" x="{X(m):.1f}" y="{ya + 20}" text-anchor="middle">{lab}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2:.1f}" y="{ya + 38}" text-anchor="middle">Months from the current month</text>')
    text_lines(body, 16, ya + 66, [
        "Older material says 12 months of history and a 12-month forecast. AWS's guide now says 13 and 18.",
        "From the AWS Cost Management User Guide (Cost Explorer pages), checked 2026-10-24."], cls="note", dy=15)
    svg("11-03-explorer-horizon.svg", w, h,
        "Cost Explorer's time range: 13 months back by default, up to 38 with an option, and 18 months of forecast",
        "A horizontal timeline in months around the current month. In blue, the default: the previous 13 months of "
        "history, then the current month, then a dashed forecast band for the next 18 months. In gray, options you "
        "switch on: multi-year data reaching back up to 38 months at monthly granularity, and hourly data for the last "
        "14 days, which is charged. A note says older material gives 12 months of history and a 12-month forecast, "
        "while AWS's guide now says 13 and 18.",
        body, style=STYLE)


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
    january_daily()
    budget_month()
    explorer_horizon()
    tools_compared()
