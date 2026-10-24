#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the chart for Simulation S14 (guardrail timeline) as SVG.

Usage: python3 -I source/charts/11-08-charts.py
Writes images/11-08-runaway.svg. The runaway and the refresh times are made-up
teaching figures from guide/11-paying-for-aws/08-sim-guardrail-timeline.md.
Prices are US East (N. Virginia), from the AWS Price List offer files retrieved
2026-10-24 (research repo, sources/raw/pricing/compute-networking-us-east-1-summary.tsv):
m7i.large On-Demand $0.1008 an hour, NAT gateway $0.045 an hour, gp3 $0.08 per
GB-month (730 hours a month). NAT gateway data processing is left out.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import line_key, make_style, svg  # noqa: E402

M7I, NAT, GP3 = 0.1008, 0.045, 0.08
RATE = 4 * M7I + NAT + 4 * 8 * GP3 / 730  # four instances, a NAT gateway, four 8 GB disks
END = 62  # Friday 18:00 + 62 h = Monday 08:00
ACT = 14  # you read the first email at Saturday 08:00 and delete everything
REFRESH = [12, 24, 36, 48, 60]
LABELS = {0: "Fri 18:00", 6: "Sat 00:00", 12: "Sat 06:00", 18: "Sat 12:00", 24: "Sat 18:00", 30: "Sun 00:00",
          36: "Sun 06:00", 42: "Sun 12:00", 48: "Sun 18:00", 54: "Mon 00:00", 60: "Mon 06:00"}

STYLE = make_style(rules_extra="""
  .line-s2 { stroke: var(--s2); stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .refresh { stroke: var(--muted); stroke-width: 1; stroke-dasharray: 3 4; }
  .dot-ink { fill: var(--ink); stroke: var(--surface); stroke-width: 2; }
  .ann { fill: var(--ink); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")


def spend(t, stop=None):
    return RATE * (t if stop is None else min(t, stop))


def runaway():
    assert round(spend(END), 2) == 28.01 and round(spend(END, ACT), 2) == 6.32
    assert round(spend(4), 2) == 1.81 and round(spend(16), 2) == 7.23
    w, left, top, pw, ph, ymax = 680, 56, 112, 560, 250, 30
    body = [
        '<text class="title" x="16" y="28">A forgotten weekend: what the money did while the alerts caught up</text>',
        '<text class="sub" x="16" y="48">Cumulative cost of 4 m7i.large instances and a NAT gateway, Friday 18:00 to Monday 08:00</text>',
    ]
    line_key(body, 16, 80, "line-s2", "Nobody acts until Monday 08:00")
    line_key(body, 290, 80, "line-s1", "You act on the first email, Saturday 08:00")

    def X(t):
        return left + pw * t / END

    def Y(v):
        return top + ph - ph * v / ymax

    for v in range(0, ymax + 1, 5):
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{Y(v) + 4:.1f}" text-anchor="end">${v}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 14}">Dollars spent</text>')
    for t, lab in LABELS.items():
        if t % 12 == 0:
            body.append(f'<text class="tick" x="{X(t):.1f}" y="{top + ph + 18}" text-anchor="middle">{lab}</text>')
    for t in REFRESH:
        body.append(f'<line class="refresh" x1="{X(t):.1f}" x2="{X(t):.1f}" y1="{top}" y2="{top + ph}"/>')
    pts = " ".join(f"{X(t):.1f},{Y(spend(t)):.1f}" for t in range(0, END + 1))
    body.append(f'<polyline class="line-s2" points="{pts}"><title>Nobody acts: ${spend(END):.2f} by Monday 08:00</title></polyline>')
    pts = " ".join(f"{X(t):.1f},{Y(spend(t, ACT)):.1f}" for t in range(0, END + 1))
    body.append(f'<polyline class="line-s1" points="{pts}"><title>You act Saturday 08:00: ${spend(END, ACT):.2f}</title></polyline>')
    # events
    for t, txt, dy in ((12, "Sat 06:00: zero-spend budget and billing alarm email (data to Fri 22:00, $1.81)", -10),
                       (24, "Sat 18:00: $5 budget's 85% and 100% alerts (data to Sat 10:00, $7.23)", -10)):
        body.append(f'<circle class="dot-ink" cx="{X(t):.1f}" cy="{Y(spend(t)):.1f}" r="5"><title>{txt}</title></circle>')
    body.append(f'<text class="ann" x="{X(12) + 8:.1f}" y="{Y(spend(12)) + 18:.1f}">1. Sat 06:00: first emails</text>')
    body.append(f'<text class="ann" x="{X(24) + 8:.1f}" y="{Y(spend(24)) + 18:.1f}">2. Sat 18:00: $5 budget alerts</text>')
    body.append(f'<text class="ann" x="{X(END) - 4:.1f}" y="{Y(spend(END)) - 10:.1f}" text-anchor="end">${spend(END):.2f}</text>')
    body.append(f'<text class="ann" x="{X(END) - 4:.1f}" y="{Y(spend(END, ACT)) - 10:.1f}" text-anchor="end">${spend(END, ACT):.2f}</text>')
    y = top + ph + 46
    for line in (
        "Dotted lines: billing data refreshes. Neither line flattens by itself: alerts send email; only deleting stops the meter.",
        "Made-up timings within AWS's documented ranges. Prices: m7i.large $0.1008 an hour, NAT gateway $0.045 an hour,",
        "gp3 $0.08 per GB-month, US East (N. Virginia), AWS Price List retrieved 2026-10-24; NAT data processing left out.",
    ):
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 15
    svg("11-08-runaway.svg", w, y + 4,
        "Cumulative cost of a forgotten weekend, with and without someone acting on the first alert",
        f"A line chart of dollars spent from Friday 18:00 to Monday 08:00. Four m7i.large instances, their disks and a "
        f"NAT gateway cost about ${RATE:.2f} an hour. Dotted vertical lines mark billing data refreshes at 06:00 and "
        f"18:00 each day. The orange line, nobody acts, rises steadily to ${spend(END):.2f}. The blue line, you read "
        f"the first email at Saturday 08:00 and delete everything, stops rising at ${spend(END, ACT):.2f}. Marked "
        "points: at Saturday 06:00 the zero-spend budget and the billing alarm email, based on data up to Friday 22:00, "
        "$1.81; at Saturday 18:00 the $5 budget sends its 85% and 100% alerts, based on data up to Saturday 10:00, "
        "$7.23. Made-up timings within AWS's documented ranges.", body, style=STYLE)


if __name__ == "__main__":
    runaway()
