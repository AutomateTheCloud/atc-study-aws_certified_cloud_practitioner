#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for Simulation S5 (the lifecycle cost timeline) as SVG.

Usage: python3 -I source/charts/05-09-charts.py
Writes images/05-09-*.svg. The PRICES below are AWS's storage prices for US East
(N. Virginia), USD per GB-month, first tier, from the AWS Price List offer files
(AmazonS3 published 2026-10-15, AmazonS3GlacierDeepArchive published 2026-09-11;
retrieved 2026-10-24; research repo sources/raw/pricing/s3-storage-us-east-1-summary.tsv).
The rules they illustrate are AWS's, from the Amazon S3 User Guide (storage
classes, lifecycle, versioning; checked 2026-10-23): minimum storage durations of 30,
90 and 180 days, and every stored version billed as a whole object. The bakery's data
(volumes and events) is made up. Change the numbers here and in guide/05-storing-data/09-sim-lifecycle-cost-timeline.md
together, then rerun.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import line_key, make_style, svg  # noqa: E402

# AWS storage prices, US East (N. Virginia), USD per GB-month, as of 2026-10-24 (see the docstring).
PRICE = {"STD": 0.023, "IA": 0.0125, "GFR": 0.0036, "GDA": 0.00099}
NAME = {"STD": "S3 Standard", "IA": "Standard-IA", "GFR": "Glacier Flexible Retrieval", "GDA": "Glacier Deep Archive"}
GB = 300  # one month of nightly backups: 30 files of 10 GB
DAYS = 365  # every plan deletes the backups after 365 days
PLANS = [  # (letter, short name, [(class, from day, to day)])
    ("A", "Standard all year", [("STD", 0, 365)]),
    ("B", "Three steps", [("STD", 0, 30), ("IA", 30, 90), ("GFR", 90, 365)]),
    ("C", "Deep Archive from day 0", [("GDA", 0, 365)]),
    ("D", "Standard, then Deep Archive", [("STD", 0, 30), ("GDA", 30, 365)]),
]


def cost_to(plan, day):
    """Storage cost of the 300 GB from day 0 to `day`, with a 30-day month."""
    total = 0.0
    for cls, a, b in plan[2]:
        d = max(0, min(day, b) - a)
        total += GB * PRICE[cls] * d / 30
    return total


TOTALS = {p[0]: round(cost_to(p, DAYS), 2) for p in PLANS}
assert TOTALS == {"A": 83.95, "B": 24.3, "C": 3.61, "D": 10.22}, TOTALS  # must match the page

# Storage classes as an ordinal blue ramp (dataviz reference palette): hottest is darkest
# in light mode; in dark mode the coldest sits nearest the dark surface. Each segment
# also carries its class name in words, so color is never alone.
STYLE = make_style(
    light_extra=(" --c-std:#184f95; --c-ia:#2a78d6; --c-gfr:#6da7ec; --c-gda:#9ec5f4;"
                 " --t-std:#ffffff; --t-ia:#ffffff; --t-gfr:#0b0b0b; --t-gda:#0b0b0b; --s3c:#1baf7a;"),
    dark_extra=(" --c-std:#9ec5f4; --c-ia:#5598e7; --c-gfr:#256abf; --c-gda:#184f95;"
                " --t-std:#0b0b0b; --t-ia:#0b0b0b; --t-gfr:#ffffff; --t-gda:#ffffff; --s3c:#199e70;"),
    rules_extra="""
  .STD { fill: var(--c-std); } .IA { fill: var(--c-ia); } .GFR { fill: var(--c-gfr); } .GDA { fill: var(--c-gda); }
  .tSTD { fill: var(--t-std); font-size: 11.5px; } .tIA { fill: var(--t-ia); font-size: 11.5px; }
  .tGFR { fill: var(--t-gfr); font-size: 11.5px; } .tGDA { fill: var(--t-gda); font-size: 11.5px; }
  .plan { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .plans { fill: var(--ink2); font-size: 11.5px; }
  .exp { stroke: var(--s2); stroke-width: 2.5; }
  .expt { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .fail { fill: var(--muted); font-size: 11.5px; font-style: italic; }
  .line-s2 { stroke: var(--s2); stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .line-s3 { stroke: var(--s3c); stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .dot-s2 { fill: var(--s2); stroke: var(--surface); stroke-width: 2; }
  .dot-s3 { fill: var(--s3c); stroke: var(--surface); stroke-width: 2; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

DAY_TICKS = [0, 30, 90, 180, 365]


def timeline():
    """Each plan as a bar along the backups' age, split into storage classes, ending in deletion."""
    w = 680
    left, right = 190, 640
    sx = lambda d: left + (right - left) * d / DAYS
    body = [
        '<text class="title" x="16" y="28">Four lifecycle plans for one month of nightly backups</text>',
        '<text class="sub" x="16" y="48">Where 300 GB of backups sit as they age, until a rule deletes them on day 365</text>',
    ]
    top, bh, gap = 74, 34, 16
    for i, (letter, short, segs) in enumerate(PLANS):
        y = top + i * (bh + gap)
        body.append(f'<text class="plan" x="16" y="{y + 15}">Plan {letter}</text>')
        body.append(f'<text class="plans" x="16" y="{y + 30}">{short}</text>')
        for cls, a, b in segs:
            x0, x1 = sx(a), sx(b)
            body.append(f'<rect class="{cls}" x="{x0 + 1:.1f}" y="{y}" width="{x1 - x0 - 2:.1f}" height="{bh}" rx="3">'
                        f'<title>Plan {letter}: {NAME[cls]}, day {a} to {b}</title></rect>')
            label = NAME[cls] if x1 - x0 > 7.2 * len(NAME[cls]) else {"STD": "Std", "IA": "IA"}.get(cls, NAME[cls])
            body.append(f'<text class="t{cls}" x="{(x0 + x1) / 2:.1f}" y="{y + 21}" text-anchor="middle">{label}</text>')
    yb = top + len(PLANS) * (bh + gap) - gap
    body.append(f'<line class="exp" x1="{sx(365):.1f}" x2="{sx(365):.1f}" y1="{top - 8}" y2="{yb + 6}"/>')
    body.append(f'<text class="expt" x="{sx(365) - 4:.1f}" y="{top - 12}" text-anchor="end">Deleted on day 365</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{right}" y1="{yb + 6}" y2="{yb + 6}"/>')
    for d in DAY_TICKS:
        body.append(f'<line class="axis" x1="{sx(d):.1f}" x2="{sx(d):.1f}" y1="{yb + 6}" y2="{yb + 11}"/>')
        body.append(f'<text class="tick" x="{sx(d):.1f}" y="{yb + 26}" text-anchor="middle">{d}</text>')
    body.append(f'<text class="tick" x="{left}" y="{yb + 44}">Age of the backups, in days</text>')
    body.append(f'<text class="note" x="16" y="{yb + 70}">Std = S3 Standard; IA = S3 Standard-IA. Colder classes cost less to store but more, and longer, to read back.</text>')
    svg("05-09-lifecycle-timeline.svg", w, yb + 84,
        "Four lifecycle plans for 300 GB of nightly backups, by age in days",
        "Four horizontal bars on a day axis from 0 to 365, each ending at a line marked 'Deleted on day 365'. "
        "Plan A, Standard all year: S3 Standard from day 0 to 365. Plan B, three steps: S3 Standard to day 30, "
        "S3 Standard-IA from day 30 to 90, S3 Glacier Flexible Retrieval from day 90 to 365. Plan C: S3 Glacier "
        "Deep Archive from day 0 to 365. Plan D: S3 Standard to day 30, then S3 Glacier Deep Archive to day 365.",
        body, style=STYLE)


def cost_by_plan():
    """Running storage cost of plans A, B and D (C fails the restore rule, so it is in the table only)."""
    w, h = 680, 400
    left, top, pw, ph, ymax = 56, 96, 400, 250, 90
    sx = lambda d: left + pw * d / DAYS
    sy = lambda v: top + ph - ph * v / ymax
    body = [
        '<text class="title" x="16" y="28">Running storage cost of plans A, B and D</text>',
        '<text class="sub" x="16" y="48">300 GB of backups (made up); S3 prices for US East (N. Virginia) as of 2026-10-24. Plan C fails a rule.</text>',
    ]
    shown = [("A", "line-s1", "dot-s1"), ("B", "line-s2", "dot-s2"), ("D", "line-s3", "dot-s3")]
    for x, (letter, lc, _) in zip((16, 210, 360), shown):
        name = next(p[1] for p in PLANS if p[0] == letter)
        line_key(body, x, 76, lc, f"Plan {letter}: {name}")
    for v in range(0, ymax + 1, 30):
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{sy(v):.1f}" y2="{sy(v):.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{sy(v) + 4:.1f}" text-anchor="end">${v}</text>')
    for d in DAY_TICKS:
        body.append(f'<text class="tick" x="{sx(d):.1f}" y="{top + ph + 18}" text-anchor="middle">{d}</text>')
    body.append(f'<text class="tick" x="{left}" y="{top + ph + 36}">Age of the backups, in days</text>')
    for letter, lc, dc in shown:
        plan = next(p for p in PLANS if p[0] == letter)
        pts = " ".join(f"{sx(d):.1f},{sy(cost_to(plan, d)):.1f}" for d in range(0, DAYS + 1, 5))
        body.append(f'<polyline class="{lc}" points="{pts}"/>')
        end = cost_to(plan, DAYS)
        body.append(f'<circle class="{dc}" cx="{sx(DAYS):.1f}" cy="{sy(end):.1f}" r="5"><title>Plan {letter}: ${end:.2f} over the year</title></circle>')
        body.append(f'<text class="lab" x="{sx(DAYS) + 10:.1f}" y="{sy(end) + 4:.1f}">Plan {letter}: ${end:.2f}</text>')
    svg("05-09-cost-by-plan.svg", w, h,
        "Running storage cost over a year for lifecycle plans A, B and D",
        "Line chart, days 0 to 365, running storage cost in US dollars for 300 GB of backups at S3 prices for "
        "US East (N. Virginia) as of 2026-10-24. All three plans cost the same $6.90 for the first 30 days in S3 "
        "Standard. Plan A, Standard all year, keeps climbing in a straight line to $83.95. Plan B, three steps, "
        "rises to $14.40 by day 90, then flattens, ending at $24.30. Plan D, Standard then Deep Archive, almost "
        "flattens after day 30 and ends at $10.22. Plan C is not drawn because it fails the restore rule.", body, style=STYLE)


def versions_pile_up():
    """Stored GB when one 10 GB file is overwritten nightly in a versioned bucket, with and without a noncurrent rule."""
    w, h = 680, 396
    left, top, pw, ph, ymax, days = 56, 112, 420, 230, 600, 60
    sx = lambda d: left + pw * d / days
    sy = lambda v: top + ph - ph * v / ymax
    no_rule = lambda d: 10 * d
    rule = lambda d: 10 * min(d, 8)  # the current version plus up to 7 days of older ones
    body = [
        '<text class="title" x="16" y="28">One file overwritten every night, versioning on</text>',
        '<text class="sub" x="16" y="48">GB stored for a 10 GB backup file that keeps the same name</text>',
    ]
    line_key(body, 16, 76, "line-s1", "No rule for older versions")
    line_key(body, 236, 76, "line-s2", "Older versions deleted after 7 days")
    for v in range(0, ymax + 1, 100):
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{sy(v):.1f}" y2="{sy(v):.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{sy(v) + 4:.1f}" text-anchor="end">{v}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 10}">GB</text>')
    for d in range(0, days + 1, 10):
        body.append(f'<text class="tick" x="{sx(d):.1f}" y="{top + ph + 18}" text-anchor="middle">{d}</text>')
    body.append(f'<text class="tick" x="{left}" y="{top + ph + 36}">Nights since versioning was turned on</text>')
    for f, lc, dc, lab in ((no_rule, "line-s1", "dot-s1", "600 GB and growing"), (rule, "line-s2", "dot-s2", "80 GB, steady")):
        pts = " ".join(f"{sx(d):.1f},{sy(f(d)):.1f}" for d in range(1, days + 1))
        body.append(f'<polyline class="{lc}" points="{pts}"/>')
        body.append(f'<circle class="{dc}" cx="{sx(days):.1f}" cy="{sy(f(days)):.1f}" r="5"><title>Night {days}: {f(days)} GB</title></circle>')
        body.append(f'<text class="lab" x="{sx(days) + 10:.1f}" y="{sy(f(days)) + 4:.1f}">{lab}</text>')
    svg("05-09-versions-pile-up.svg", w, h,
        "GB stored when a 10 GB file is overwritten every night in a versioned bucket",
        "Line chart over 60 nights. With no rule for older versions, every overwrite keeps the old 10 GB "
        "version, so storage climbs in a straight line to 600 GB on night 60 and keeps growing. With a "
        "lifecycle rule that permanently deletes older versions 7 days after they stop being current, storage "
        "rises to 80 GB by night 8 and stays there.", body, style=STYLE)


if __name__ == "__main__":
    timeline()
    cost_by_plan()
    versions_pile_up()
