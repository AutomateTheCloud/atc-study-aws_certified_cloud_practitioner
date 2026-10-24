#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphic for Lab 14 (Amazon Polly text to speech) as SVG.

Usage: python3 -I source/charts/10-05-charts.py
Writes images/10-05-price-by-engine.svg: Amazon Polly's pay-as-you-go price per million
characters for each voice engine, and what the lab's 211-character product description
costs to synthesize once with each. Prices from the Amazon Polly pricing page
(aws.amazon.com/polly/pricing/), checked 2026-10-24: Standard $4.00, Neural $16.00,
Generative $30, Long-Form $100.00 per 1 million characters. The per-description figures
are our arithmetic, before any free allowance.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, text_lines  # noqa: E402

STYLE = make_style(rules_extra="""
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

CHARS = 211
# (engine, USD per 1 million characters, used in the lab)
ENGINES = [
    ("Standard", 4.00, True),
    ("Neural", 16.00, True),
    ("Generative", 30.00, True),
    ("Long Form", 100.00, False),
]


def price_by_engine():
    w = 680
    left, top, pw, rowh = 110, 92, 330, 44
    xmax = 100
    body = [
        '<text class="title" x="16" y="28">Amazon Polly charges by the character, and the engine sets the rate</text>',
        '<text class="sub" x="16" y="48">US dollars per 1 million characters, pay-as-you-go, before any free allowance</text>',
    ]
    nrows = len(ENGINES)
    bottom = top + nrows * rowh - 10
    for v in range(0, xmax + 1, 25):
        x = left + pw * v / xmax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 6}" y2="{bottom}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{bottom + 18}" text-anchor="middle">${v}</text>')
    for i, (name, price, used) in enumerate(ENGINES):
        y = top + i * rowh
        bw = pw * price / xmax
        once = CHARS * price / 1_000_000
        body.append(f'<text class="lab" x="{left - 12}" y="{y + 19}" text-anchor="end">{name}</text>')
        tip = f"{name}: ${price:.2f} per million characters; the lab's {CHARS} characters once: about ${once:.4f}"
        body.append(f'<path class="s1" d="{right_rounded(left, y + 4, bw, 22)}"><title>{tip}</title></path>')
        tail = "" if used else " (not used in this lab)"
        body.append(f'<text class="lab" x="{left + bw + 8:.1f}" y="{y + 15}">${price:.0f}{tail}</text>')
        body.append(f'<text class="small" x="{left + bw + 8:.1f}" y="{y + 31}">this description once: about ${once:.4f}</text>')
    y = bottom + 46
    y = text_lines(body, 16, y, [
        f"The lab's lemon tart description is {CHARS} characters. You pay each time Polly turns text into speech,",
        "so a shop that plays the same description to every visitor should synthesize it once and keep the",
        "audio file: AWS allows you to store and replay Polly's output at no extra charge.",
    ], cls="small", dy=17)
    body.append(f'<text class="note" x="16" y="{y + 6}">Amazon Polly pricing, checked 2026-10-24. Per-description figures are our arithmetic.</text>')
    h = y + 20
    svg("10-05-price-by-engine.svg", w, h,
        "Amazon Polly's price per million characters, by voice engine",
        "Horizontal bar chart of Amazon Polly's pay-as-you-go price per 1 million characters, before any free "
        "allowance, checked 2026-10-24. Standard: $4, so the lab's 211-character description costs about "
        "$0.0008 to synthesize once. Neural: $16, about $0.0034 once. Generative: $30, about $0.0063 once. "
        "Long Form: $100, about $0.0211 once; the lab doesn't use it. You pay each time Polly synthesizes, so "
        "speech you will reuse is best synthesized once and kept as a file, which AWS allows at no extra charge.",
        body, style=STYLE)


if __name__ == "__main__":
    price_by_engine()
