#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 05.03 (storage classes and lifecycle) as SVG.

Usage: python3 -I source/charts/05-03-charts.py
Writes images/05-03-*.svg. Facts, checked 2026-10-23 in the research repo
(docs/04-services/storage.md and its sources):
- minimum storage durations, Availability Zone counts, retrieval fees and first-byte or
  retrieval times per class: S3 User Guide, "Understanding and managing Amazon S3 storage
  classes" (comparison table), and the S3 and S3 Glacier storage classes product pages;
- early deletion billed for the rest of the minimum duration: the same User Guide page;
- lifecycle transition and expiration actions: S3 User Guide, "Managing the lifecycle of
  objects";
- Intelligent-Tiering's 30-day and 90-day automatic moves: S3 storage classes product page.
No prices: the research holds no dated per-GB S3 storage prices, so the charts show days,
times and fees by kind only. The bakery's records and rules are made up for teaching.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, swatch, text_lines, wrap  # noqa: E402

# The lifecycle timeline uses one hue (blue) from light to dark for hot to cold: an
# ordinal ramp (dataviz palette, steps 250 / 400 / 600 in light; mirrored for dark).
# Every segment is also labeled with its class name, so color is never alone.
STYLE = make_style(
    light_extra=" --hot:#86b6ef; --warm:#3987e5; --cold:#184f95; --panel:#f1f0ec; --it:#d9e8fb;",
    dark_extra=" --hot:#184f95; --warm:#2a78d6; --cold:#86b6ef; --panel:#252523; --it:#1b3554;",
    rules_extra="""
  .hot { fill: var(--hot); } .warm { fill: var(--warm); } .cold { fill: var(--cold); }
  .it { fill: var(--it); stroke: var(--s1); stroke-width: 1.5; stroke-dasharray: 6 4; }
  .panel { fill: var(--panel); }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .head { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .val { fill: var(--ink); font-size: 12px; font-variant-numeric: tabular-nums; }
  .ev { fill: var(--ink); stroke: var(--surface); stroke-width: 2; }
  .evline { stroke: var(--ink2); stroke-width: 1; stroke-dasharray: 3 3; }
  .brk { stroke: var(--surface); stroke-width: 4; }
  .brk2 { stroke: var(--ink2); stroke-width: 1.2; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }""")

CLASSES = [  # name, minimum storage duration (days), first byte, retrieval fee, AZs
    ("S3 Standard", 0, ["Milliseconds"], ["None"], "3 or more"),
    ("S3 Intelligent-Tiering", 0, ["Milliseconds (optional", "archive tiers: longer)"], ["None; small monitoring", "fee per object"], "3 or more"),
    ("S3 Standard-IA", 30, ["Milliseconds"], ["Per GB read"], "3 or more"),
    ("S3 One Zone-IA", 30, ["Milliseconds"], ["Per GB read"], "1"),
    ("S3 Glacier Instant Retrieval", 90, ["Milliseconds"], ["Per GB read"], "3 or more"),
    ("S3 Glacier Flexible Retrieval", 90, ["Minutes to 12 hours,", "after a restore"], ["Per GB read;", "bulk restores free"], "3 or more"),
    ("S3 Glacier Deep Archive", 180, ["12 to 48 hours,", "after a restore"], ["Per GB read"], "3 or more"),
]


def hot_to_cold():
    """Big picture: the classes from hot to cold, with minimum durations as bars."""
    w = 820
    body = [
        '<text class="title" x="16" y="28">S3 storage classes from hot to cold</text>',
        '<text class="sub" x="16" y="48">In general, the lower the row, the less storage costs per GB, and the more it costs to read data or delete it early.</text>',
    ]
    name_x, bar_x, bar_w = 34, 236, 120
    fb_x, fee_x, az_x = 430, 600, 750
    top = 84
    body.append(f'<text class="head" x="{name_x}" y="{top}">Storage class</text>')
    body.append(f'<text class="head" x="{bar_x}" y="{top}">Minimum billed stay</text>')
    body.append(f'<text class="head" x="{fb_x}" y="{top}">First byte</text>')
    body.append(f'<text class="head" x="{fee_x}" y="{top}">Retrieval fee</text>')
    body.append(f'<text class="head" x="{az_x}" y="{top}">AZs</text>')
    y = top + 14
    rh = 46
    first_y = y
    for name, days, fb, fee, az in CLASSES:
        body.append(f'<rect class="panel" x="16" y="{y}" width="{w - 32}" height="{rh - 6}" rx="5"/>')
        cy = y + (rh - 6) / 2
        body.append(f'<text class="cellt" x="{name_x}" y="{cy + 5}">{name}</text>')
        if days:
            bw = bar_w * days / 180
            body.append(f'<path class="s1" d="{right_rounded(bar_x, cy - 8, bw, 16)}"/>')
            body.append(f'<text class="val" x="{bar_x + bw + 6:.1f}" y="{cy + 4}">{days} days</text>')
        else:
            body.append(f'<text class="val" x="{bar_x}" y="{cy + 4}">None</text>')
        text_lines(body, fb_x, cy + 4 - 7.5 * (len(fb) - 1), fb, cls="small", dy=15)
        text_lines(body, fee_x, cy + 4 - 7.5 * (len(fee) - 1), fee, cls="small", dy=15)
        body.append(f'<text class="small" x="{az_x}" y="{cy + 4}">{az}</text>')
        y += rh
    # A hot-to-cold arrow down the left edge.
    body.append(f'<line class="arrow" x1="24" y1="{first_y + 4}" x2="24" y2="{y - 14}"/>')
    body.append(f'<path class="arrowhead" d="M19,{y - 20} L29,{y - 20} L24,{y - 10} Z"/>')
    y += 14
    y = text_lines(body, 16, y, wrap("Delete, overwrite or move an object out early, and you are billed for the rest of the minimum stay. Standard-IA, One Zone-IA and Glacier Instant Retrieval also bill any object under 128 KB as 128 KB.", 118), cls="small")
    y += 4
    body.append(f'<text class="note" x="16" y="{y}">S3 User Guide storage class table and S3 storage classes pages, checked 2026-10-23. S3 Express One Zone is left out.</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">No prices are shown: they vary by Region and change. Check the Amazon S3 pricing page.</text>')
    y += 16
    svg("05-03-hot-to-cold.svg", w, y + 14,
        "S3 storage classes from hot to cold, with minimum billed stay, first-byte time, retrieval fee and AZ count",
        "Seven rows from hot at the top to cold at the bottom; in general, the lower the row, the less storage "
        "costs per GB, and the more it costs to read data or delete it early. S3 Standard: no minimum stay; "
        "milliseconds; no retrieval fee; 3 or more AZs. S3 Intelligent-Tiering: no minimum stay; "
        "milliseconds, with optional archive tiers that take longer; no retrieval fee, but a small "
        "monitoring fee per object; 3 or more AZs. S3 Standard-IA: 30 days; milliseconds; per GB read; 3 or "
        "more AZs. S3 One Zone-IA: 30 days; milliseconds; per GB read; 1 AZ. S3 Glacier Instant Retrieval: "
        "90 days; milliseconds; per GB read; 3 or more AZs. S3 Glacier Flexible Retrieval: 90 days; minutes "
        "to 12 hours after a restore; per GB read, bulk restores free; 3 or more AZs. S3 Glacier Deep "
        "Archive: 180 days; 12 to 48 hours after a restore; per GB read; 3 or more AZs. The minimum stays "
        "are drawn as bars of 0, 0, 30, 30, 90, 90 and 180 days. Below: deleting, overwriting or moving an "
        "object out early is billed for the rest of the minimum stay, and Standard-IA, One Zone-IA and "
        "Glacier Instant Retrieval bill any object under 128 KB as 128 KB.", body, style=STYLE)


if __name__ == "__main__":
    hot_to_cold()
