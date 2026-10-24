#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the chart for lesson 02.03 (downtime a year at each availability level) as SVG.

Usage: python3 -I source/charts/02-03-charts.py
Writes images/02-03-downtime-by-nines.svg. The values are arithmetic:
(1 - availability) x 8,760 hours in a year.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import OUT, right_rounded as bar  # noqa: E402

HOURS_A_YEAR = 8760
LEVELS = [("99.9%", "three nines", 0.999), ("99.99%", "four nines", 0.9999), ("99.999%", "five nines", 0.99999)]

# Reference palette (dataviz skill, references/palette.md); validated light and dark.
STYLE = """
<style>
  svg { --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e; --axis:#c3c2b7; --s1:#2a78d6; }
  @media (prefers-color-scheme: dark) {
    svg { --surface:#1a1a19; --ink:#f0efec; --ink2:#c3c2b7; --axis:#383835; --s1:#3987e5; }
  }
  text { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; fill: var(--ink2); font-size: 13px; }
  .title { fill: var(--ink); font-size: 16px; font-weight: 600; }
  .lab { fill: var(--ink); font-size: 13px; }
  .axis { stroke: var(--axis); stroke-width: 1; }
  .s1 { fill: var(--s1); }
</style>"""


def label(minutes):
    if minutes >= 120:
        return f"about {minutes / 60:.1f} hours"
    return f"about {minutes:.0f} minutes"


def downtime_by_nines():
    w, left, top, pw, rowh = 680, 150, 76, 380, 50
    h = top + rowh * len(LEVELS) + 24
    xmax = (1 - LEVELS[0][2]) * HOURS_A_YEAR * 60
    body = [
        '<text class="title" x="16" y="28">Each extra nine cuts yearly downtime to a tenth</text>',
        '<text x="16" y="50">Downtime a year allowed at each availability level</text>',
    ]
    for i, (pct, name, a) in enumerate(LEVELS):
        minutes = (1 - a) * HOURS_A_YEAR * 60
        y = top + i * rowh
        body.append(f'<text class="lab" x="16" y="{y + 15}">{pct}</text>')
        body.append(f'<text x="16" y="{y + 31}">{name}</text>')
        bw = max(pw * minutes / xmax, 2)
        body.append(f'<path class="s1" d="{bar(left, y + 4, bw, 22)}"><title>{pct}: {label(minutes)} of downtime a year</title></path>')
        body.append(f'<text class="lab" x="{left + bw + 8:.1f}" y="{y + 20}">{label(minutes)}</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top}" y2="{top + rowh * len(LEVELS) - 16}"/>')
    doc = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">\n'
        '<title id="t">Downtime a year at three availability levels</title>\n'
        '<desc id="d">Horizontal bar chart. 99.9% availability allows about 8.8 hours of downtime a year; '
        '99.99% about 53 minutes; 99.999% about 5 minutes.</desc>\n'
        f'{STYLE}\n<rect width="{w}" height="{h}" style="fill:var(--surface)"/>\n' + "\n".join(body) + "\n</svg>\n"
    )
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "02-03-downtime-by-nines.svg"), "w") as f:
        f.write(doc)


if __name__ == "__main__":
    downtime_by_nines()
