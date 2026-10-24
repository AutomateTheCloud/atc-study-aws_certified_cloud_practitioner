#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for Simulation S17 (rightsizing the chain's servers) as SVG.

Usage: python3 -I source/charts/13-06-charts.py
Writes images/13-06-peaks.svg (peak CPU and memory for four servers; the utilization data is
made up) and images/13-06-monthly-cost.svg (monthly On-Demand cost before and after rightsizing
and scheduling). Prices: Linux On-Demand, shared tenancy, US East (N. Virginia), from the AWS
Price List offer file for AmazonEC2 retrieved 2026-10-24: m7i.large $0.1008 an hour, t3.medium
$0.0416 an hour. A month is 730 hours; the schedule is 50 hours a week (50 x 52 / 12 hours a month).
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import STYLE, right_rounded, svg, swatch  # noqa: E402

PEAKS = [("web-1", 18, 31), ("test-1", 25, 28), ("stock-1", 97, 88), ("stock-2", 9, None)]

M7I, T3M = 0.1008, 0.0416
HOURS, SCHED = 730, 50 * 52 / 12
COSTS = [
    ("web-1", [("Now, m7i.large", M7I * HOURS, "s1l"), ("t3.medium", T3M * HOURS, "s1")]),
    ("test-1", [("Now, m7i.large", M7I * HOURS, "s1l"), ("Scheduled", M7I * SCHED, "s1"),
                ("Scheduled and t3.medium", T3M * SCHED, "s1")]),
]


def peaks():
    """Grouped horizontal bars: peak CPU (slot 1) and peak memory (slot 2) per server, 0-100%."""
    w, left, pw = 680, 110, 500
    bar, inner, group = 16, 4, 58
    top = 92
    body = ['<text class="title" x="16" y="28">Peak use over three weeks, by server</text>',
            '<text class="sub" x="16" y="48">Percent of the instance\'s CPU and memory at the busiest moment. Made-up data.</text>']
    swatch(body, 16, 74, "s1", "Peak CPU")
    swatch(body, 120, 74, "s2", "Peak memory")
    ph = group * len(PEAKS)
    for v in range(0, 101, 25):
        x = left + pw * v / 100
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 6}" y2="{top + ph}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top + ph + 18}" text-anchor="middle">{v}%</text>')
    for i, (name, cpu, mem) in enumerate(PEAKS):
        y = top + i * group + 6
        body.append(f'<text class="lab" x="{left - 10}" y="{y + bar + 6}" text-anchor="end">{name}</text>')
        for j, (val, cls, label) in enumerate([(cpu, "s1", "CPU"), (mem, "s2", "memory")]):
            by = y + j * (bar + inner)
            if val is None:
                body.append(f'<text class="tick" x="{left + 6}" y="{by + 12}">memory: no data (no CloudWatch agent)</text>')
                continue
            body.append(f'<path class="{cls}" d="{right_rounded(left, by, pw * val / 100, bar)}"/>')
            body.append(f'<text class="tick" x="{left + pw * val / 100 + 6:.1f}" y="{by + 12}">{val}%</text>')
    svg("13-06-peaks.svg", w, top + ph + 34,
        "Peak CPU and peak memory over three weeks for four of the chain's servers",
        "Horizontal bars, two per server, on a scale from 0 to 100 percent. web-1: CPU 18%, memory 31%. "
        "test-1: CPU 25%, memory 28%. stock-1: CPU 97%, memory 88%. stock-2: CPU 9%; memory has no data "
        "because the CloudWatch agent isn't installed.",
        body)


def monthly_cost():
    """Horizontal bars of monthly On-Demand cost: the current type in light slot 1, each change in slot 1."""
    w, left, pw = 680, 190, 380
    bar, gap = 20, 6
    vmax = 80
    top = 92
    body = ['<text class="title" x="16" y="28">Monthly cost before and after rightsizing</text>',
            '<text class="sub" x="16" y="48">On-Demand, Linux, US East (N. Virginia), as of 2026-10-24; 730 hours a month.</text>']
    swatch(body, 16, 74, "s1l", "Today")
    swatch(body, 100, 74, "s1", "After the change")
    rows = sum(len(r) for _, r in COSTS) * (bar + gap) + 30 * len(COSTS)
    for v in range(0, vmax + 1, 20):
        x = left + pw * v / vmax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 6}" y2="{top + rows - 20}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top + rows - 2}" text-anchor="middle">${v}</text>')
    y = top
    for server, items in COSTS:
        body.append(f'<text class="lab" x="16" y="{y + 14}" font-weight="600">{server}</text>')
        for label, cost, cls in items:
            body.append(f'<text class="tick" x="{left - 10}" y="{y + 14}" text-anchor="end">{label}</text>')
            body.append(f'<path class="{cls}" d="{right_rounded(left, y, pw * cost / vmax, bar)}"/>')
            body.append(f'<text class="lab" x="{left + pw * cost / vmax + 6:.1f}" y="{y + 14}">${cost:.2f}</text>')
            y += bar + gap
        y += 30
    svg("13-06-monthly-cost.svg", w, top + rows + 14,
        "Monthly On-Demand cost of two servers before and after rightsizing and scheduling",
        f"Horizontal bars in dollars a month. web-1: today on m7i.large ${M7I * HOURS:.2f}; on t3.medium "
        f"${T3M * HOURS:.2f}. test-1: today on m7i.large ${M7I * HOURS:.2f}; scheduled to run 50 hours a week "
        f"${M7I * SCHED:.2f}; scheduled and on t3.medium ${T3M * SCHED:.2f}.",
        body)


if __name__ == "__main__":
    peaks()
    monthly_cost()
