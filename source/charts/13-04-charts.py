#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for lesson 13.04 (the business case) as SVG.

Usage: python3 -I source/charts/13-04-charts.py
Writes images/13-04-*.svg.

- 13-04-big-picture.svg: made-up three-year figures for teaching, as in the lesson's table.
- 13-04-license-share.svg: On-Demand prices for US East
  (N. Virginia) from AWS's EC2 Price List offer file (AmazonEC2, published
  2026-10-23T22:13:55Z, retrieved 2026-10-24), compute and licenses only, no storage:
  m7i.xlarge Linux $0.2016/h; Windows license-included $0.3856/h; Windows with SQL Server
  Standard $0.8656/h; Windows with SQL Server Enterprise $1.8856/h; m7i.2xlarge Windows with
  SQL Server Enterprise $3.7712/h; m7i Dedicated Host $10.644/h (96 physical cores).
  Months are 730 hours. Cited in the lesson to https://aws.amazon.com/ec2/pricing/on-demand/
  and https://aws.amazon.com/ec2/dedicated-hosts/pricing/.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, swatch, right_rounded  # noqa: E402

HOURS = 730
P = {  # USD per hour, price list of 2026-10-23
    "xl_linux": 0.2016, "xl_win": 0.3856, "xl_std": 0.8656, "xl_ent": 1.8856,
}

# Owned infrastructure in neutrals (dark to light), licenses in slot 2 (orange), AWS usage in
# slot 1 (blue), one-time migration costs in slot 3 (aqua). Every segment is also named in text.
STYLE = make_style(
    light_extra=" --hw:#52514e; --fac:#898781; --staff:#c3c2b7; --s3:#1baf7a; --win:#898781;",
    dark_extra=" --hw:#c3c2b7; --fac:#898781; --staff:#52514e; --s3:#199e70; --win:#898781;",
    rules_extra="""
  .hw { fill: var(--hw); } .fac { fill: var(--fac); } .staff { fill: var(--staff); }
  .s3 { fill: var(--s3); } .win { fill: var(--win); }
  .gap { stroke: var(--surface); stroke-width: 2; }
  .val { fill: var(--ink); font-size: 13px; font-variant-numeric: tabular-nums; }
  .valb { fill: var(--ink); font-size: 14px; font-weight: 600; font-variant-numeric: tabular-nums; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .na { fill: none; stroke: var(--muted); stroke-width: 1.5; stroke-dasharray: 5 4; }
  .hiring { fill: none; stroke: var(--s2); stroke-width: 2.5; }""")


def k(v):
    return f"${v // 1000:,}k"


def big_picture():
    cols = [
        ("Stay on-premises", [("hw", "Hardware and refresh", 240000), ("fac", "Facilities", 180000),
                              ("staff", "Staff", 300000), ("s2", "Licenses", 210000)]),
        ("Move as it is", [("s1", "AWS usage", 450000), ("s2", "Licenses", 260000),
                           ("staff", "Staff", 210000), ("s3", "One-time migration", 150000)]),
        ("Move, rightsized and relicensed", [("s1", "AWS usage", 250000), ("s2", "Licenses", 140000),
                                             ("staff", "Staff", 210000), ("s3", "One-time migration", 150000)]),
    ]
    totals = [sum(v for _, _, v in segs) for _, segs in cols]
    assert totals == [930000, 1070000, 750000], "totals must match the lesson"
    w, top, ph, ymax, bw = 680, 118, 300, 1100000, 64
    xs = [64, 274, 484]
    body = [
        '<text class="title" x="16" y="28">Three ways to spend the next three years</text>',
        '<text class="sub" x="16" y="48">Three-year costs by category. Made-up figures for teaching.</text>',
    ]
    legend = [("hw", "Hardware and refresh"), ("fac", "Facilities"), ("staff", "Staff"),
              ("s2", "Licenses"), ("s1", "AWS usage"), ("s3", "One-time migration")]
    for (cls, lab), x in zip(legend, [16, 182, 276, 342, 426, 520]):
        swatch(body, x, 76, cls, lab)
    yv = lambda v: top + ph - ph * v / ymax
    for v in range(0, ymax + 1, 250000):
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="56" x2="{w - 16}" y1="{yv(v):.1f}" y2="{yv(v):.1f}"/>')
        body.append(f'<text class="tick" x="50" y="{yv(v) + 4:.1f}" text-anchor="end">{k(v) if v else "$0"}</text>')
    for (name, segs), x, tot in zip(cols, xs, totals):
        acc = 0
        for cls, lab, v in segs:
            y1, y0 = yv(acc + v), yv(acc)
            body.append(f'<rect class="{cls} gap" x="{x}" y="{y1:.1f}" width="{bw}" height="{y0 - y1:.1f}">'
                        f'<title>{name}: {lab} {k(v)}</title></rect>')
            body.append(f'<text class="small" x="{x + bw + 8}" y="{(y0 + y1) / 2 - 3:.1f}">{lab}</text>')
            body.append(f'<text class="small" x="{x + bw + 8}" y="{(y0 + y1) / 2 + 12:.1f}">{k(v)}</text>')
            acc += v
        body.append(f'<text class="valb" x="{x + bw / 2}" y="{yv(tot) - 8:.1f}" text-anchor="middle">{k(tot)}</text>')
        words = name.split(", ")
        for i, line in enumerate(words):
            body.append(f'<text class="lab" x="{x + bw / 2}" y="{top + ph + 20 + i * 16}" text-anchor="middle">{line + ("," if i < len(words) - 1 else "")}</text>')
    svg("13-04-big-picture.svg", w, top + ph + 52,
        "Three-year costs of staying on-premises, moving as it is, and moving rightsized and relicensed",
        "Stacked column chart, made-up figures for teaching. Stay on-premises, $930k: hardware and refresh $240k, "
        "facilities $180k, staff $300k, licenses $210k. Move as it is, $1,070k: AWS usage $450k, licenses $260k, "
        "staff $210k, one-time migration $150k. Move, rightsized and relicensed, $750k: AWS usage $250k, licenses "
        "$140k, staff $210k, one-time migration $150k.", body, style=STYLE)


def license_share():
    rows = [
        ("Linux", [("s1", P["xl_linux"])]),
        ("Windows Server", [("s1", P["xl_linux"]), ("win", P["xl_win"] - P["xl_linux"])]),
        ("Windows + SQL Standard", [("s1", P["xl_linux"]), ("win", P["xl_win"] - P["xl_linux"]),
                                    ("s2", P["xl_std"] - P["xl_win"])]),
        ("Windows + SQL Enterprise", [("s1", P["xl_linux"]), ("win", P["xl_win"] - P["xl_linux"]),
                                      ("s2", P["xl_ent"] - P["xl_win"])]),
    ]
    assert round(P["xl_win"] - P["xl_linux"], 4) == 0.1840 and round(P["xl_ent"] - P["xl_win"], 4) == 1.5
    w, left, top, bw, gap, pw, xmax = 680, 186, 104, 32, 18, 400, 2.0
    body = [
        '<text class="title" x="16" y="28">What an hour of the same instance pays for</text>',
        '<text class="sub" x="16" y="48">m7i.xlarge (4 vCPUs, 16 GiB), On-Demand, US East (N. Virginia), price list of 2026-10-23</text>',
    ]
    swatch(body, 16, 80, "s1", "The instance (its Linux price)")
    swatch(body, 236, 80, "win", "Windows Server license")
    swatch(body, 420, 80, "s2", "SQL Server license")
    xv = lambda v: left + pw * v / xmax
    n = len(rows)
    for v in (0, 0.5, 1.0, 1.5, 2.0):
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{xv(v):.1f}" x2="{xv(v):.1f}" y1="{top - 6}" y2="{top + n * (bw + gap) - gap + 6}"/>')
        body.append(f'<text class="tick" x="{xv(v):.1f}" y="{top + n * (bw + gap) + 12}" text-anchor="middle">${v:.2f}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2:.1f}" y="{top + n * (bw + gap) + 30}" text-anchor="middle">USD per hour</text>')
    for i, (lab, segs) in enumerate(rows):
        y = top + i * (bw + gap)
        body.append(f'<text class="lab" x="{left - 10}" y="{y + bw / 2 + 5:.1f}" text-anchor="end">{lab}</text>')
        acc = 0
        for j, (cls, v) in enumerate(segs):
            x0, x1 = xv(acc), xv(acc + v)
            if j == len(segs) - 1:
                body.append(f'<path class="{cls} gap" d="{right_rounded(x0, y, x1 - x0, bw)}"><title>{lab}: ${v:.4f}</title></path>')
            else:
                body.append(f'<rect class="{cls} gap" x="{x0:.1f}" y="{y}" width="{x1 - x0:.1f}" height="{bw}"><title>{lab}: ${v:.4f}</title></rect>')
            acc += v
        body.append(f'<text class="val" x="{xv(acc) + 8:.1f}" y="{y + bw / 2 + 5:.1f}">${acc:.4f}</text>')
    h = top + n * (bw + gap) + 52
    body.append(f'<text class="note" x="16" y="{h - 8}">License parts = each price minus the Linux price. Compute and licenses only; no storage.</text>')
    svg("13-04-license-share.svg", w, h,
        "What an hour of an m7i.xlarge instance pays for, by operating system and SQL Server edition",
        "Stacked horizontal bars, On-Demand, US East (N. Virginia), price list of 2026-10-23. Every bar starts with the "
        "instance at $0.2016, its Linux price. Linux: $0.2016. Windows Server license-included: plus $0.1840 for "
        "Windows, $0.3856. Windows with SQL Server Standard: plus $0.1840 Windows and $0.4800 SQL Server, $0.8656. "
        "Windows with SQL Server Enterprise: plus $0.1840 Windows and $1.5000 SQL Server, $1.8856.", body, style=STYLE)


if __name__ == "__main__":
    big_picture()
    license_share()
