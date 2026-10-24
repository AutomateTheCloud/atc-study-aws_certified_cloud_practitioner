#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for Lab 15 (AWS Pricing Calculator) as SVG.

Usage: python3 -I source/charts/11-05-charts.py
Writes images/11-05-*.svg. Prices are US East (N. Virginia), from the AWS Price
List offer files retrieved 2026-10-24 (research repo,
sources/raw/pricing/compute-networking-us-east-1-summary.tsv and
s3-storage-us-east-1-summary.tsv): t3.small on-demand $0.0208 an hour,
Application Load Balancer $0.0225 an hour (capacity units left out), public IPv4
address $0.005 an hour, gp3 storage $0.08 per GB-month, S3 Standard $0.023 per
GB-month. 730 hours a month, as the AWS Pricing Calculator uses.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, swatch  # noqa: E402

HOURS = 730
T3_SMALL, ALB, IPV4, GP3, S3_STD = 0.0208, 0.0225, 0.005, 0.08, 0.023

STYLE = make_style(rules_extra="""
  .vlab { fill: var(--ink); font-size: 12px; font-variant-numeric: tabular-nums; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .seg-gap { stroke: var(--surface); stroke-width: 2; }""")

# label, monthly dollars, kind class
LIVE = [
    ("2 web servers, t3.small, 730 h", round(2 * T3_SMALL * HOURS, 2), "s1"),
    ("Load balancer, 730 h", round(ALB * HOURS, 2), "s1"),
    ("2 public IPv4 addresses, 730 h", 2 * IPV4 * HOURS, "s1"),
    ("2 disks, 20 GB gp3 each", 2 * 20 * GP3, "s1l"),
    ("50 GB of photos in S3 Standard", 50 * S3_STD, "s2"),
]
KINDS = [("s1", "Charged every hour it exists"), ("s1l", "Charged for the size you set"), ("s2", "Charged for what you store")]


def live_estimate():
    total = sum(v for _, v, _ in LIVE)
    hourly = sum(v for _, v, c in LIVE if c == "s1")
    assert abs(total - 58.45) < 0.01 and abs(hourly - 54.10) < 0.01, "must match the model answer"
    w, left, top, pw, bh, gap, xmax = 680, 236, 100, 340, 26, 12, 35
    body = [
        '<text class="title" x="16" y="28">The bakery\'s web tier for a month, line by line</text>',
        '<text class="sub" x="16" y="48">On-Demand, US East (N. Virginia), as of 2026-10-24; capacity units and data transfer left out</text>',
    ]
    x = 16
    for cls, label in KINDS:
        swatch(body, x, 76, cls, label)
        x += 30 + 7.1 * len(label)

    def X(v):
        return left + pw * v / xmax

    bottom = top + len(LIVE) * (bh + gap) - gap
    for v in range(0, xmax + 1, 5):
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{top - 6}" y2="{bottom + 6}"/>')
        body.append(f'<text class="tick" x="{X(v):.1f}" y="{bottom + 22}" text-anchor="middle">${v}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2}" y="{bottom + 40}" text-anchor="middle">Dollars per month</text>')
    for i, (lab, v, cls) in enumerate(LIVE):
        y = top + i * (bh + gap)
        body.append(f'<text class="lab" x="{left - 10}" y="{y + 17}" text-anchor="end">{lab}</text>')
        body.append(f'<path class="{cls}" d="{right_rounded(X(0), y, X(v) - X(0), bh)}"><title>{lab}: ${v:.2f}</title></path>')
        body.append(f'<text class="vlab" x="{X(v) + 8:.1f}" y="{y + 17}">${v:.2f}</text>')
    y = bottom + 66
    for line in (
        f"Total ${total:.2f}. The three hourly lines are ${hourly:.2f}, {100 * hourly / total:.0f}% of it, and they bill the same at 3 a.m. as at noon.",
        "AWS Price List offer files, retrieved 2026-10-24; 730 hours a month. Prices change: check the calculator.",
    ):
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 15
    svg("11-05-live-estimate.svg", w, y + 4,
        "The bakery's web tier priced line by line, with the hourly lines marked",
        f"A horizontal bar chart in dollars per month. Charged every hour the resource exists: two t3.small web "
        f"servers for 730 hours, ${LIVE[0][1]:.2f}; the load balancer's hourly charge, ${LIVE[1][1]:.2f}; two public "
        f"IPv4 addresses, ${LIVE[2][1]:.2f}. Charged for the size you set: two 20 GB gp3 disks, ${LIVE[3][1]:.2f}. "
        f"Charged for what you store: 50 GB of photos in S3 Standard, ${LIVE[4][1]:.2f}. Total ${total:.2f}, of "
        f"which the hourly lines are ${hourly:.2f}, {100 * hourly / total:.0f}%. US East (N. Virginia), On-Demand, "
        "prices as of 2026-10-24, capacity units and data transfer left out.", body, style=STYLE)


TEST_HOURS = HOURS * 40 / 168  # 40 hours a week, in a 730-hour month
DRAFT = [
    ("Servers", round(2 * T3_SMALL * HOURS, 2), "s1"),
    ("Load balancer", round(ALB * HOURS, 2), "s1"),
    ("Public IPv4", 2 * IPV4 * HOURS, "s1"),
    ("Disks", 2 * 20 * GP3, "s1l"),
]
TRIMMED = [
    ("Server", round(T3_SMALL * TEST_HOURS, 2), "s1"),
    ("Disk", 20 * GP3, "s1l"),
]


def test_copy():
    d, t = sum(v for _, v, _ in DRAFT), sum(v for _, v, _ in TRIMMED)
    assert abs(d - 57.30) < 0.01 and abs(t - 5.22) < 0.01, "must match the model answer"
    w, left, top, pw, bh, gap, xmax = 680, 196, 100, 380, 40, 56, 60
    body = [
        '<text class="title" x="16" y="28">The test copy for the new feature, before and after</text>',
        '<text class="sub" x="16" y="48">Monthly cost, On-Demand, US East (N. Virginia), as of 2026-10-24</text>',
    ]
    swatch(body, 16, 76, "s1", "Charged every hour it exists")
    swatch(body, 250, 76, "s1l", "Charged for the size you set")

    def X(v):
        return left + pw * v / xmax

    bottom = top + 2 * bh + gap + 26
    for v in range(0, xmax + 1, 10):
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{top - 6}" y2="{bottom + 6}"/>')
        body.append(f'<text class="tick" x="{X(v):.1f}" y="{bottom + 22}" text-anchor="middle">${v}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2}" y="{bottom + 40}" text-anchor="middle">Dollars per month</text>')
    rows = [("Nephew's draft", "a copy of the live site", DRAFT, d),
            ("Trimmed", "1 server, 40 h a week", TRIMMED, t)]
    for r, (name, sub, parts, tot) in enumerate(rows):
        y = top + r * (bh + gap)
        body.append(f'<text class="lab" x="{left - 10}" y="{y + 17}" text-anchor="end">{name}</text>')
        body.append(f'<text class="tick" x="{left - 10}" y="{y + 33}" text-anchor="end">{sub}</text>')
        x = X(0)
        for i, (lab, v, cls) in enumerate(parts):
            wv = X(v) - X(0)
            if i == len(parts) - 1:
                body.append(f'<path class="{cls}" d="{right_rounded(x, y, wv, bh)}"><title>{lab}: ${v:.2f}</title></path>')
            else:
                body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{wv:.1f}" height="{bh}"><title>{lab}: ${v:.2f}</title></rect>')
            if i:
                body.append(f'<line class="seg-gap" x1="{x:.1f}" x2="{x:.1f}" y1="{y}" y2="{y + bh}"/>')
            x += wv
        body.append(f'<text class="vlab" x="{x + 8:.1f}" y="{y + 25}">${tot:.2f}</text>')
        parts_text = " · ".join(f"{lab} ${v:.2f}" for lab, v, _ in parts)
        body.append(f'<text class="tick" x="{X(0):.1f}" y="{y + bh + 17}">{parts_text}</text>')
    y = bottom + 66
    for line in (
        "Draft: 2 t3.small servers, a load balancer and 2 public IPv4 addresses for 730 hours, 2 disks of 20 GB.",
        "Trimmed: 1 t3.small server for 40 of the week's 168 hours (about 174 hours a month) and its 20 GB disk,",
        "which bills all month even while the server is stopped. AWS Price List, retrieved 2026-10-24.",
    ):
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 15
    svg("11-05-test-copy.svg", w, y + 4,
        "The test copy's monthly cost before and after removing the hourly items it doesn't need",
        f"Two stacked horizontal bars in dollars per month. The nephew's draft, a copy of the live site, totals "
        f"${d:.2f}: servers ${DRAFT[0][1]:.2f}, load balancer ${DRAFT[1][1]:.2f}, public IPv4 ${DRAFT[2][1]:.2f}, all "
        f"charged every hour, plus disks ${DRAFT[3][1]:.2f}. The trimmed copy, one server running 40 hours a week, "
        f"totals ${t:.2f}: server ${TRIMMED[0][1]:.2f} and disk ${TRIMMED[1][1]:.2f}. US East (N. Virginia), "
        "On-Demand, prices as of 2026-10-24.", body, style=STYLE)


if __name__ == "__main__":
    live_estimate()
    test_copy()
