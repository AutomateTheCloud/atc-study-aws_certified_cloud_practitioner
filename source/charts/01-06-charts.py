#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 01.06 (everyday security) as SVG.

Usage: python3 -I source/charts/01-06-charts.py
Writes images/01-06-*.svg. The numbers are arithmetic, not measurements: a random
password of length n drawn from k possible characters has k**n possibilities.
k = 26 for lowercase letters only; k = 94 for the printable keyboard characters
(26 + 26 letters, 10 digits, 32 symbols; space not counted). Our own design.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, line_key  # noqa: E402

STYLE = make_style(rules_extra="""
  .line-s2 { stroke: var(--s2); stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: 7 4; }
  .dot-s2 { fill: var(--s2); stroke: var(--surface); stroke-width: 2; }
  .ring { fill: none; stroke: var(--ink); stroke-width: 1.5; }
  .small { fill: var(--ink2); font-size: 12px; }""")

LENGTHS = list(range(8, 21))
SETS = [("All four character types (94 characters)", 94, "line-s1", "dot-s1"),
        ("Lowercase letters only (26 characters)", 26, "line-s2", "dot-s2")]


def sup(v):
    """A power of ten's exponent as a raised tspan."""
    return f'<tspan dy="-6" font-size="10">{v}</tspan><tspan dy="6"> </tspan>'


def table_rows():
    """Rows for the lesson's data table: length, lowercase-only and all-types as powers of ten."""
    return [(n, n * math.log10(26), n * math.log10(94)) for n in (8, 10, 12, 16, 20)]


def combinations():
    w, h = 680, 440
    left, top, pw, ph = 70, 86, 560, 250
    ymin, ymax = 10, 40
    body = [
        '<text class="title" x="16" y="28">Each extra character multiplies the guesses needed</text>',
        '<text class="sub" x="16" y="48">Possible random passwords, by length; each gridline is 100,000 times the one below</text>',
    ]
    for v in range(ymin, ymax + 1, 5):
        y = top + ph - ph * (v - ymin) / (ymax - ymin)
        body.append(f'<line class="{"axis" if v == ymin else "grid"}" x1="{left}" x2="{left + pw}" y1="{y:.1f}" y2="{y:.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{y + 4:.1f}" text-anchor="end">10{sup(v)}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 14}">Possible passwords (log scale)</text>')

    def px(n):
        return left + pw * (n - LENGTHS[0]) / (LENGTHS[-1] - LENGTHS[0])

    def py(e):
        return top + ph - ph * (e - ymin) / (ymax - ymin)

    for n in LENGTHS:
        if n % 2 == 0:
            body.append(f'<text class="tick" x="{px(n):.1f}" y="{top + ph + 18}" text-anchor="middle">{n}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2}" y="{top + ph + 36}" text-anchor="middle">Length in characters</text>')
    for label, k, lcls, dcls in SETS:
        pts = " ".join(f"{px(n):.1f},{py(n * math.log10(k)):.1f}" for n in LENGTHS)
        body.append(f'<polyline class="{lcls}" points="{pts}"/>')
    # the comparison the lesson makes: 10 characters of all types vs 16 lowercase letters
    a = (10, 10 * math.log10(94), "dot-s1", f"10 characters, all types: about 10{sup(19.7)}")
    b = (16, 16 * math.log10(26), "dot-s2", f"16 lowercase letters: about 10{sup(22.6)}")
    for n, e, dcls, txt in (a, b):
        body.append(f'<circle class="{dcls}" cx="{px(n):.1f}" cy="{py(e):.1f}" r="5"/>')
    body.append(f'<text class="lab" x="{left + 16}" y="{top + 54}">{a[3]}</text>')
    body.append(f'<line class="lead" x1="{px(10):.1f}" x2="{px(10):.1f}" y1="{top + 62}" y2="{py(a[1]) - 8:.1f}"/>')
    body.append(f'<text class="lab" x="{px(16):.1f}" y="{py(b[1]) + 44:.1f}" text-anchor="middle">{b[3]}</text>')
    body.append(f'<line class="lead" x1="{px(16):.1f}" x2="{px(16):.1f}" y1="{py(b[1]) + 8:.1f}" y2="{py(b[1]) + 31:.1f}"/>')
    line_key(body, 16, h - 40, "line-s1", SETS[0][0])
    line_key(body, 360, h - 40, "line-s2", SETS[1][0] + ", dashed")
    text_lines(body, 16, h - 14, ["Counts for passwords picked at random, as a password manager does. Human-chosen ones are far easier to guess."], cls="small")
    svg("01-06-password-combinations.svg", w, h,
        "How many random passwords are possible, by length",
        "A line chart with a log scale from 10 to the 10th up to 10 to the 40th possible passwords, against length from "
        "8 to 20 characters. Two straight lines rise with length. All four character types (94 characters): from about "
        "10 to the 15.8th at 8 characters to about 10 to the 39.5th at 20. Lowercase letters only (26 characters, dashed): "
        "from about 10 to the 11.3th at 8 characters to about 10 to the 28.3th at 20. Two points are marked: 10 characters "
        "of all types, about 10 to the 19.7th, and 16 lowercase letters, about 10 to the 22.6th, which is higher. A note "
        "says the counts are for passwords picked at random, as a password manager does; human-chosen ones are far easier "
        "to guess.", body, style=STYLE)


if __name__ == "__main__":
    combinations()
    for row in table_rows():
        print("%2d  lowercase 10^%.1f  all types 10^%.1f" % row)
