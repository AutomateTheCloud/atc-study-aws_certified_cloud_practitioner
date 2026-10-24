#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for Simulation S10 (an AWS Config timeline) as SVG.

Usage: python3 -I source/charts/09-09-charts.py
Writes images/09-09-config-timeline.svg (a week of CloudTrail events, Config configuration
items and restricted-ssh compliance for one security group; the week, people and times are
made up) and images/09-09-evidence-windows.svg (how far back three evidence sources reach).
Facts retrieved 2026-10-24: CloudTrail Event history keeps 90 days of management events
("Working with CloudTrail event history"); IAM last accessed information tracks services for
at least 400 days ("Refine permissions in AWS using last accessed information"); AWS Config
keeps configuration items for 7 years (2,557 days) by default ("Deleting AWS Config Data");
restricted-ssh is noncompliant when SSH is open to 0.0.0.0/0 or ::/0 ("restricted-ssh").
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, text_lines  # noqa: E402

# Noncompliant is carried by a thick outline, a hatch and the word, never color alone.
STYLE = make_style(
    light_extra=" --ok-fill:#f1f0ec; --bad-fill:#fbe1d6; --item:#d9e8fb;",
    dark_extra=" --ok-fill:#252523; --bad-fill:#4d2716; --item:#1b3554;",
    rules_extra="""
  .okb { fill: var(--ok-fill); stroke: var(--muted); stroke-width: 1; }
  .badb { fill: url(#hatch); stroke: var(--ink); stroke-width: 2.5; }
  .item { fill: var(--item); stroke: var(--s1); stroke-width: 1.2; }
  .lane { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .lab2 { fill: var(--ink); font-size: 12px; }
  .lab2b { fill: var(--ink); font-size: 12px; font-weight: 700; }
  .small { fill: var(--ink2); font-size: 11.5px; }
  .mark { fill: var(--ink); }
  .note { fill: var(--muted); font-size: 11.5px; }
  .hatchbg { fill: var(--bad-fill); }
  .hatchln { stroke: var(--s2); stroke-width: 1.5; }""")

DEFS = ('<defs><pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        '<rect class="hatchbg" width="8" height="8"/><line class="hatchln" x1="0" y1="0" x2="0" y2="8"/></pattern></defs>')

DAYS = ["Mon 12", "Tue 13", "Wed 14", "Thu 15", "Fri 16", "Sat 17", "Sun 18"]


def timeline():
    w, left, pw = 680, 150, 510
    day = pw / 7

    def x(d, hh=0.0):
        return left + day * (d + hh / 24)

    body = [DEFS,
            '<text class="title" x="16" y="28">A week in the life of web-sg</text>',
            '<text class="sub" x="16" y="48">Times in UTC. The week, the people and the times are made up.</text>']
    top, bottom = 70, 330
    for i, d in enumerate(DAYS):
        xx = x(i)
        body.append(f'<line class="grid" x1="{xx:.1f}" x2="{xx:.1f}" y1="{top}" y2="{bottom}"/>')
        body.append(f'<text class="tick" x="{xx + day / 2:.1f}" y="{bottom + 18}" text-anchor="middle">{d}</text>')
    body.append(f'<line class="grid" x1="{x(7):.1f}" x2="{x(7):.1f}" y1="{top}" y2="{bottom}"/>')
    body.append(f'<line class="axis" x1="{left}" x2="{x(7):.1f}" y1="{bottom}" y2="{bottom}"/>')

    # Lane 1: CloudTrail events
    ly = 110
    text_lines(body, 16, ly - 6, ["CloudTrail:", "requests"], cls="lane", dy=16)
    for d, hh, name, who, anchor, dx in [(2, 14 + 5 / 60, "AuthorizeSecurityGroupIngress", "sam-dev", "end", 8),
                                         (4, 10 + 40 / 60, "RevokeSecurityGroupIngress", "lee-ops", "start", -8)]:
        xx = x(d, hh)
        body.append(f'<path class="mark" d="M{xx:.1f},{ly - 7} L{xx + 7:.1f},{ly} L{xx:.1f},{ly + 7} L{xx - 7:.1f},{ly} Z"/>')
        body.append(f'<text class="lab2b" x="{xx:.1f}" y="{ly - 14}" text-anchor="{anchor}">{who}</text>')
        body.append(f'<text class="small" x="{xx + dx:.1f}" y="{ly + 22}" text-anchor="{anchor}">{name}</text>')

    # Lane 2: configuration items
    ly = 190
    text_lines(body, 16, ly - 6, ["Config:", "configuration items"], cls="lane", dy=16)
    t1, t2 = x(2, 14 + 6 / 60), x(4, 10 + 41 / 60)
    for xa, xb, label in [(left, t1, "Item 1: port 443"), (t1, t2, "Item 2: 443 and 22"), (t2, x(7), "Item 3: port 443")]:
        body.append(f'<rect class="item" x="{xa + 1:.1f}" y="{ly - 14}" width="{xb - xa - 2:.1f}" height="28" rx="4"/>')
        body.append(f'<text class="lab2" x="{(xa + xb) / 2:.1f}" y="{ly + 4}" text-anchor="middle">{label}</text>')

    # Lane 3: compliance
    ly = 270
    text_lines(body, 16, ly - 6, ["Config rule:", "restricted-ssh"], cls="lane", dy=16)
    c1, c2 = x(2, 14 + 7 / 60), x(4, 10 + 42 / 60)
    body.append(f'<rect class="okb" x="{left + 1}" y="{ly - 14}" width="{c1 - left - 2:.1f}" height="28" rx="4"/>')
    body.append(f'<text class="lab2" x="{(left + c1) / 2:.1f}" y="{ly + 4}" text-anchor="middle">COMPLIANT</text>')
    body.append(f'<rect class="badb" x="{c1 + 1:.1f}" y="{ly - 14}" width="{c2 - c1 - 2:.1f}" height="28" rx="4"/>')
    body.append(f'<rect class="okb" x="{c2 + 1:.1f}" y="{ly - 14}" width="{x(7) - c2 - 2:.1f}" height="28" rx="4"/>')
    body.append(f'<text class="lab2" x="{(c2 + x(7)) / 2:.1f}" y="{ly + 4}" text-anchor="middle">COMPLIANT</text>')
    body.append(f'<text class="lab2b" x="{(c1 + c2) / 2:.1f}" y="{ly + 32}" text-anchor="middle">NONCOMPLIANT for about 44.5 hours</text>')
    ps = x(5, 3)
    body.append(f'<line class="lead" x1="{ps:.1f}" x2="{ps:.1f}" y1="{ly - 22}" y2="{ly + 14}"/>')
    body.append(f'<text class="small" x="{ps + 4:.1f}" y="{ly - 24}">periodic check</text>')

    body.append(f'<text class="note" x="16" y="{bottom + 44}">Each CloudTrail request comes one minute before the configuration item '
                'it caused, and the rule ran one minute after that.</text>')
    svg("09-09-config-timeline.svg", w, bottom + 62,
        "A week of web-sg's history: CloudTrail requests, Config configuration items and restricted-ssh compliance",
        "A timeline from Monday 12 to Sunday 18 October with three lanes. CloudTrail lane: on Wednesday at 14:05, "
        "sam-dev, AuthorizeSecurityGroupIngress; on Friday at 10:40, lee-ops, RevokeSecurityGroupIngress. Config "
        "lane: item 1, port 443, until Wednesday 14:06; item 2, ports 443 and 22, until Friday 10:41; item 3, port "
        "443, after that. Rule lane, restricted-ssh: compliant until Wednesday 14:07, then a hatched, thickly "
        "outlined stretch labeled noncompliant for about 44.5 hours until Friday 10:42, then compliant, with a "
        "periodic check marked on Saturday at 03:00. A note says each request comes one minute before the "
        "configuration item it caused, and the rule ran one minute after that.",
        body, style=STYLE)


def windows():
    w, left, pw = 680, 210, 320
    vmax = 2600
    body = ['<text class="title" x="16" y="28">How far back each evidence source reaches</text>',
            '<text class="sub" x="16" y="48">Days of history, by default (checked 2026-10-24)</text>']
    top, bh, gap = 76, 26, 22
    rows = [("CloudTrail Event history", 90, "90 days"),
            ("IAM last accessed information", 400, "400 days (at least)"),
            ("AWS Config", 2557, "2,557 days (7 years)")]
    ph = len(rows) * (bh + gap)
    for v in range(0, 2501, 500):
        xx = left + pw * v / vmax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{xx:.1f}" x2="{xx:.1f}" y1="{top - 8}" y2="{top + ph - gap + 8}"/>')
        body.append(f'<text class="tick" x="{xx:.1f}" y="{top + ph - gap + 26}" text-anchor="middle">{v:,}</text>')
    for i, (name, v, label) in enumerate(rows):
        y = top + i * (bh + gap)
        bw = pw * v / vmax
        body.append(f'<text class="lab" x="{left - 10}" y="{y + 18}" text-anchor="end">{name}</text>')
        body.append(f'<path class="s1" d="{right_rounded(left, y, bw, bh)}"/>')
        body.append(f'<text class="lab" x="{left + bw + 8:.1f}" y="{y + 18}">{label}</text>')
    yn = top + ph - gap + 52
    text_lines(body, 16, yn, [
        "Config counts only from the day recording started; you can set 30 days to 7 years. Last accessed covers services;",
        "action detail started later. A CloudTrail trail keeps events for as long as you keep its files in S3."], cls="tick", dy=16)
    svg("09-09-evidence-windows.svg", w, yn + 26,
        "How far back three evidence sources reach: Event history 90 days, IAM last accessed 400 days, AWS Config 2,557 days",
        "A horizontal bar chart of days of history, from 0 to 2,500. CloudTrail Event history: 90 days. IAM last "
        "accessed information: at least 400 days. AWS Config: 2,557 days, or 7 years, by default. A note says "
        "Config counts only from the day recording started and can be set from 30 days to 7 years, last accessed "
        "covers services with action detail starting later, and a CloudTrail trail keeps events as long as you keep "
        "its files in S3.",
        body)


if __name__ == "__main__":
    timeline()
    windows()
