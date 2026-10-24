#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the chart for lesson 08.02 (IaC and automation) as SVG.

Usage: python3 -I source/charts/08-02-charts.py
Writes images/08-02-effort-by-copies.svg. All numbers are made-up teaching
figures from the worked example in
guide/08-building-and-operating/02-iac-and-automation.md: 3 person-hours to
build one copy of the bakery's setup by hand in the console, 8 hours to write
and test the template once, then 15 minutes of a person's time for each copy
built from it. Change them here and in the lesson together, then rerun.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import line_key, make_style, svg, text_lines  # noqa: E402

BY_HAND = 3.0       # person-hours per copy, clicking through the console
TEMPLATE_FIRST = 8.0  # person-hours to write and test the template once
PER_COPY = 0.25     # person-hours per copy built from the template
COPIES = 8

STYLE = make_style(rules_extra="""
  .line-s2 { stroke: var(--s2); stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .dot-s2 { fill: var(--s2); stroke: var(--surface); stroke-width: 2; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")


def hours(v):
    return f"{v:g} h"


def series():
    hand = [BY_HAND * n for n in range(1, COPIES + 1)]
    tmpl = [TEMPLATE_FIRST + PER_COPY * n for n in range(1, COPIES + 1)]
    return hand, tmpl


def effort_by_copies():
    hand, tmpl = series()
    assert (hand[-1], tmpl[-1]) == (24.0, 10.0), "totals must match the lesson"
    cross = next(n for n in range(1, COPIES + 1) if tmpl[n - 1] < hand[n - 1])
    assert cross == 3, "the lesson says the template is cheaper from the third copy"
    w, h, left, top, pw, ph, ymax = 680, 420, 64, 108, 470, 240, 25
    body = [
        '<text class="title" x="16" y="28">By hand, every copy costs the same; a template costs once</text>',
        '<text class="sub" x="16" y="48">Total person-hours to build 1 to 8 copies of the bakery\'s setup (made-up figures)</text>',
    ]
    line_key(body, 16, 76, "line-s2", "By hand in the console")
    line_key(body, 200, 76, "line-s1", "From a template")
    yv = lambda v: top + ph - ph * v / ymax
    xv = lambda n: left + pw * (n - 1) / (COPIES - 1)
    for v in range(0, ymax + 1, 5):
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{yv(v):.1f}" y2="{yv(v):.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{yv(v) + 4:.1f}" text-anchor="end">{hours(v)}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 14}">Person-hours so far</text>')
    for n in range(1, COPIES + 1):
        body.append(f'<text class="tick" x="{xv(n):.1f}" y="{top + ph + 18}" text-anchor="middle">{n}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2:.1f}" y="{top + ph + 38}" text-anchor="middle">Copies built</text>')
    for cls, dot, s in (("line-s2", "dot-s2", hand), ("line-s1", "dot-s1", tmpl)):
        body.append(f'<polyline class="{cls}" points="' + " ".join(f"{xv(n):.1f},{yv(v):.1f}" for n, v in enumerate(s, 1)) + '"/>')
        for n, v in enumerate(s, 1):
            body.append(f'<circle class="{dot}" cx="{xv(n):.1f}" cy="{yv(v):.1f}" r="4"/>')
    # hover targets, one per copy count
    band = pw / (COPIES - 1)
    for n in range(1, COPIES + 1):
        body.append(f'<rect x="{xv(n) - band / 2:.1f}" y="{top}" width="{band:.1f}" height="{ph}" fill="transparent">'
                    f'<title>{n} {"copy" if n == 1 else "copies"}: by hand {hours(hand[n - 1])}; '
                    f'from a template {hours(tmpl[n - 1])}</title></rect>')
    # annotations: the first copy, and where the template becomes cheaper
    x1 = xv(1)
    body.append(f'<line class="lead" x1="{x1:.1f}" y1="{yv(tmpl[0]) - 6:.1f}" x2="{x1:.1f}" y2="{yv(12):.1f}"/>')
    text_lines(body, x1 + 6, yv(14), ["Copy 1: the template costs", "more (8.25 h against 3 h)"], cls="lab")
    xc = xv(cross)
    body.append(f'<line class="lead" x1="{xc:.1f}" y1="{yv(tmpl[cross - 1]) + 6:.1f}" x2="{xc:.1f}" y2="{yv(5.6):.1f}"/>')
    text_lines(body, xc + 6, yv(4.4), [f"From copy {cross}, the template", "is cheaper (8.75 h against 9 h)"], cls="lab")
    # direct end labels
    xe = xv(COPIES) + 10
    for name, v in (("By hand", hand[-1]), ("Template", tmpl[-1])):
        body.append(f'<text class="lab" x="{xe:.1f}" y="{yv(v) - 2:.1f}">{hours(v)}</text>')
        body.append(f'<text class="small" x="{xe:.1f}" y="{yv(v) + 13:.1f}">{name}</text>')
    body.append(f'<text class="note" x="16" y="{h - 14}">Made-up figures: 3 h a copy by hand; 8 h to write the template, then 15 min a copy. Fixing mistakes isn\'t counted.</text>')
    desc = (f"Line chart of total person-hours against the number of copies built, 1 to 8, made-up figures. By hand "
            f"in the console, each copy takes 3 hours, so the total rises in a straight line from 3 hours to "
            f"{hours(hand[-1])}. From a template, the first copy costs 8.25 hours, because writing and testing the "
            f"template takes 8 hours, and each further copy adds 15 minutes, reaching {hours(tmpl[-1])} at 8 copies. "
            f"The template line starts higher but is lower from copy {cross} onwards. Time spent fixing mistakes in "
            f"hand-built copies isn't counted.")
    svg("08-02-effort-by-copies.svg", w, h,
        "Person-hours to build copies of the bakery's setup by hand and from a template", desc, body, style=STYLE)


if __name__ == "__main__":
    effort_by_copies()
