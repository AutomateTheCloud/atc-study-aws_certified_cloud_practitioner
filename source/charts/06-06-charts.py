#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the chart for Lab 08 (launch, stop and terminate an instance) as SVG.

Usage: python3 -I source/charts/06-06-charts.py
Writes images/06-06-forgotten-month.svg. Prices are US East (N. Virginia), from the
AWS Price List offer files retrieved 2026-10-24 (research repo,
sources/raw/pricing/compute-networking-us-east-1-summary.tsv). The 8 GiB gp3 volume
is an assumption stated in the lab, matching lesson 06.01. Update the prices and rerun when they change.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, swatch  # noqa: E402

HOURS = 730  # one month, as in lesson 06.01
T3_MICRO = 0.0104  # per hour, Linux, on-demand
IPV4 = 0.005  # per public IPv4 address-hour
GP3 = 0.08  # per GB-month (gp2 is 0.10)
VOLUME_GB = 8

STYLE = make_style(light_extra=" --s3:#1baf7a;", dark_extra=" --s3:#199e70;",
                   rules_extra="\n  .s3 { fill: var(--s3); }")


def forgotten_month():
    inst, ip, vol = HOURS * T3_MICRO, HOURS * IPV4, VOLUME_GB * GP3
    assert (round(inst, 2), round(ip, 2), round(vol, 2)) == (7.59, 3.65, 0.64), "must match the lab text"
    rows = [
        ("Left running", [("s1", inst, "instance hours"), ("s2", ip, "public IPv4"), ("s3", vol, "volume")]),
        ("Stopped, not terminated", [("s3", vol, "volume")]),
        ("Terminated", []),
    ]
    w, left, top, pw, rowh, xmax = 680, 16, 104, 470, 60, 14
    h = top + rowh * len(rows) + 28
    body = [
        '<text class="title" x="16" y="28">One forgotten t3.micro for a month, on a Paid plan</text>',
        '<text class="sub" x="16" y="48">US East (N. Virginia) prices as of 2026-10-24; an 8 GiB gp3 volume and a 730-hour month</text>',
    ]
    swatch(body, 16, 80, "s1", "Instance hours")
    swatch(body, 150, 80, "s2", "Public IPv4 address")
    swatch(body, 320, 80, "s3", "EBS volume")
    sx = lambda v: pw * v / xmax
    for i, (label, segs) in enumerate(rows):
        y = top + i * rowh
        body.append(f'<text class="lab" x="{left}" y="{y + 14}">{label}</text>')
        by, x = y + 22, left
        for j, (cls, v, name) in enumerate(segs):
            wseg = sx(v) - (2 if j < len(segs) - 1 else 0)
            rx = ' rx="2"' if j == len(segs) - 1 else ""
            body.append(f'<rect class="{cls}" x="{x:.1f}" y="{by}" width="{max(wseg, 3):.1f}" height="20"{rx}><title>{label}: {name} ${v:.2f}</title></rect>')
            x += sx(v)
        total = sum(v for _, v, _ in segs)
        if label == "Left running":
            txt = f"${total:.2f}: ${inst:.2f} + ${ip:.2f} + ${vol:.2f}"
        elif segs:
            txt = f"${total:.2f}: the volume is still stored"
        else:
            txt = "$0.00: nothing left to bill"
        body.append(f'<text class="lab" x="{x + 8:.1f}" y="{by + 15}">{txt}</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top + 18}" y2="{top + rowh * len(rows)}"/>')
    svg("06-06-forgotten-month.svg", w, h,
        "What one forgotten t3.micro instance costs in a month: running, stopped or terminated",
        "Horizontal stacked bars, US East (N. Virginia) prices as of 2026-10-24, assuming an 8 GiB gp3 volume and a 730-hour month. "
        f"Left running: ${inst + ip + vol:.2f}, made of ${inst:.2f} of instance hours, ${ip:.2f} for the public IPv4 address "
        f"and ${vol:.2f} for the volume. Stopped but not terminated: ${vol:.2f}, the volume alone. Terminated: $0.00.",
        body, style=STYLE)


if __name__ == "__main__":
    forgotten_month()
