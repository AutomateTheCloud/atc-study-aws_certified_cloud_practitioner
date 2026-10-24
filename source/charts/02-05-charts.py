#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 02.05 (the Well-Architected Framework) as SVG.

Usage: python3 -I source/charts/02-05-charts.py
Writes images/02-05-*.svg. The wording comes from
guide/02-why-the-cloud/05-the-well-architected-framework.md: the pillar questions
are the lesson's own summaries, not AWS text. Our own design: no AWS logos, icons
or trade dress.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(rules_extra="""
  .card { fill: none; stroke: var(--axis); stroke-width: 1; }
  .panel { fill: none; stroke: var(--axis); stroke-width: 1; }
  .pill { fill: var(--surface); stroke: var(--muted); stroke-width: 1; }
  .pill-s1 { fill: var(--surface); stroke: var(--s1); stroke-width: 2; }
  .tag { fill: var(--ink2); font-size: 11px; font-weight: 600; letter-spacing: 0.5px; }
  .name { fill: var(--ink); font-size: 15px; font-weight: 600; }
  .rowlab { fill: var(--ink2); font-size: 12px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .track { stroke: var(--axis); stroke-width: 2; stroke-linecap: round; }
  .knob { fill: var(--s1); stroke: var(--surface); stroke-width: 2; }""")

ROWS = [
    ("Generally not traded away against the other pillars", [
        ("OPS", "Operational excellence",
         "Can we run this well day to day, see what it is doing, and keep improving how we work?"),
        ("SEC", "Security", "Are the data, systems and accounts protected?"),
    ]),
    ("Sound alike: both care about capacity", [
        ("REL", "Reliability",
         "Does it do its job correctly whenever it is needed, and recover when something fails?"),
        ("PERF", "Performance efficiency",
         "Are we using the right kind and amount of resources to meet our needs, as demand and technology change?"),
    ]),
    ("Usually point the same way: waste costs money and energy at once", [
        ("COST", "Cost optimization", "Does it deliver its value at the lowest cost?"),
        ("SUS", "Sustainability", "Are we using as few resources, and as little energy, as we can?"),
    ]),
]


def six_pillars():
    w, cw, gap, wrap_at = 680, 320, 8, 47
    body = [
        '<text class="title" x="16" y="28">Six pillars, six questions</text>',
        '<text class="sub" x="16" y="48">"Is our system built well?" split into the six questions of the Well-Architected Framework</text>',
    ]
    y = 76
    longdesc = []
    for label, cards in ROWS:
        body.append(f'<text class="rowlab" x="16" y="{y + 12}">{label}</text>')
        y += 22
        nlines = max(len(wrap(q, wrap_at)) for _, _, q in cards)
        ch = 50 + 17 * nlines
        for i, (tag, name, q) in enumerate(cards):
            x = 16 + i * (cw + gap)
            body.append(f'<rect class="card" x="{x}" y="{y}" width="{cw}" height="{ch}" rx="8"/>')
            tw = 9 + 8 * len(tag)
            body.append(f'<rect class="pill" x="{x + 14}" y="{y + 13}" width="{tw}" height="20" rx="10"/>')
            body.append(f'<text class="tag" x="{x + 14 + tw / 2:.1f}" y="{y + 27}" text-anchor="middle">{tag}</text>')
            body.append(f'<text class="name" x="{x + 22 + tw}" y="{y + 28}">{name}</text>')
            text_lines(body, x + 14, y + 54, wrap(q, wrap_at), cls="lab")
            longdesc.append(f"{name} ({tag}): {q}")
        y += ch + 18
    h = y + 4
    svg("02-05-six-pillars.svg", w, h,
        "The six pillars of the Well-Architected Framework, each as one question",
        "Six cards in three rows of two, each with a pillar's ID prefix, name and question. "
        "Row 1, generally not traded away against the other pillars: " + " ".join(longdesc[0:2]) + " "
        "Row 2, sound alike because both care about capacity: " + " ".join(longdesc[2:4]) + " "
        "Row 3, usually point the same way because waste costs money and energy at once: " + " ".join(longdesc[4:6]),
        body, style=STYLE)


def trade_offs():
    w, h, pw = 680, 432, 320
    body = [
        '<text class="title" x="16" y="28">Which pillars bend: the bakery\'s two copies of its site</text>',
        '<text class="sub" x="16" y="48">Reliability can be traded against cost. Security and operational excellence stay on both.</text>',
    ]
    panels = [
        ("Test copy", "the owner's nephew waits until tomorrow.", 0.82, "Bends toward cost",
         "One small server, no standby copy, switched off at night."),
        ("Live ordering site", "the bakery loses orders at a holiday peak.", 0.18, "Leans toward reliability",
         "Pays more for reliability during the peak months."),
    ]
    top, ph = 68, 214
    for i, (name, stake, pos, verdict, detail) in enumerate(panels):
        x = 16 + i * (pw + 8)
        body.append(f'<rect class="panel" x="{x}" y="{top}" width="{pw}" height="{ph}" rx="8"/>')
        body.append(f'<text class="name" x="{x + 16}" y="{top + 28}">{name}</text>')
        text_lines(body, x + 16, top + 52, wrap("If it fails, " + stake, 44), cls="small")
        ty = top + 120
        x0, x1 = x + 24, x + pw - 24
        kx = x0 + (x1 - x0) * pos
        anchor, vx = ("end", kx + 12) if pos > 0.5 else ("start", kx - 12)
        body.append(f'<text class="lab" x="{vx:.1f}" y="{ty - 18}" text-anchor="{anchor}" style="font-weight:600">{verdict}</text>')
        body.append(f'<line class="track" x1="{x0}" x2="{x1}" y1="{ty}" y2="{ty}"/>')
        for xe in (x0, x1):
            body.append(f'<line class="track" x1="{xe}" x2="{xe}" y1="{ty - 6}" y2="{ty + 6}"/>')
        body.append(f'<circle class="knob" cx="{kx:.1f}" cy="{ty}" r="8"/>')
        body.append(f'<text class="small" x="{x0}" y="{ty + 24}">Reliability</text>')
        body.append(f'<text class="small" x="{x1}" y="{ty + 24}" text-anchor="end">Cost optimization</text>')
        text_lines(body, x + 16, ty + 58, wrap(detail, 44), cls="lab")
    by = top + ph + 14
    body.append(f'<rect class="panel" x="16" y="{by}" width="{w - 32}" height="96" rx="8"/>')
    body.append(f'<text class="name" x="32" y="{by + 30}">Held on both copies</text>')
    px = 200
    for label in ("Security", "Operational excellence"):
        pwid = len(label) * 7.6 + 24
        body.append(f'<rect class="pill-s1" x="{px}" y="{by + 13}" width="{pwid:.1f}" height="26" rx="13"/>')
        body.append(f'<text class="lab" x="{px + pwid / 2:.1f}" y="{by + 31}" text-anchor="middle">{label}</text>')
        px += pwid + 10
    text_lines(body, 32, by + 62, ["The test copy still needs a strong password with MFA, because a break-in",
                                   "there can reach the rest of the account."], cls="small")
    body.append(f'<text class="sub" x="16" y="{h - 14}">Then write the decision down, so the next person knows the test copy is unreliable on purpose.</text>')
    svg("02-05-trade-offs.svg", w, h,
        "Trade-offs for the bakery's test copy and live ordering site",
        "Two panels, each with a slider between Reliability and Cost optimization. Test copy: if it fails, the owner's "
        "nephew waits until tomorrow; the slider sits near Cost optimization, labeled bends toward cost: one small "
        "server, no standby copy, switched off at night. Live ordering site: if it fails, the bakery loses orders at a "
        "holiday peak; the slider sits near Reliability, labeled leans toward reliability: it pays more for reliability during the peak months. A band "
        "across both panels reads held on both copies: Security and Operational excellence; the test copy still needs a "
        "strong password with MFA. A final line says to write the decision down.", body, style=STYLE)


if __name__ == "__main__":
    six_pillars()
    trade_offs()
