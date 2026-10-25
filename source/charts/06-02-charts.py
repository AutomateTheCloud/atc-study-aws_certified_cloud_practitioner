#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 06.02 (Auto Scaling and load balancers) as SVG.

Usage: python3 -I source/charts/06-02-charts.py
Writes images/06-02-*.svg. Facts, checked 2026-10-24 in the research repo:
- an Auto Scaling group keeps its size between a minimum and a maximum, launches from a launch
  template, balances instances across the AZs you choose, and replaces unhealthy instances:
  EC2 Auto Scaling User Guide, "What is Amazon EC2 Auto Scaling?";
- Elastic Load Balancing spreads traffic across targets in one or more AZs, sends it only to
  healthy targets, and registers and deregisters instances that Auto Scaling launches and
  terminates: ELB User Guide, "What is Elastic Load Balancing?".
The servers needed each month are Module 02's made-up teaching figures
(guide/02-why-the-cloud/00-brief.md and source/charts/02-02-charts.py). Our own design: no AWS logos, icons, trade dress or
AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

MIN, MAX, FIXED = 2, 8, 6


STYLE = make_style(
    light_extra=" --panel:#f1f0ec; --hi-fill:#d9e8fb; --crit:#d03b3b; --crit-fill:#fae3e3;",
    dark_extra=" --panel:#252523; --hi-fill:#1b3554; --crit:#d03b3b; --crit-fill:#3d1d1d;",
    rules_extra="""
  .panel { fill: var(--panel); stroke: var(--axis); stroke-width: 1; }
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 1.5; }
  .box { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .boxdash { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; stroke-dasharray: 4 3; }
  .zone { fill: none; stroke: var(--muted); stroke-width: 1.2; stroke-dasharray: 5 4; }
  .group { fill: none; stroke: var(--ink); stroke-width: 1.8; stroke-dasharray: 9 4; }
  .wire { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .flow { stroke: var(--s1); stroke-width: 2; fill: none; }
  .crit { fill: var(--crit-fill); stroke: var(--crit); stroke-width: 1.5; }
  .ci { stroke: var(--crit); stroke-width: 2.5; fill: none; stroke-linecap: round; }
  .head { fill: var(--ink); font-size: 15px; font-weight: 600; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .num { fill: var(--surface); font-size: 13px; font-weight: 700; }
  .numc { fill: var(--ink); }
  .dash-ink { stroke: var(--ink); stroke-width: 2; stroke-dasharray: 6 4; fill: none; }
  .dash-muted { stroke: var(--muted); stroke-width: 1.5; stroke-dasharray: 3 3; fill: none; }""")

ARROW = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
         'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--ink2)"/></marker>'
         '<marker id="ab" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
         'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--s1)"/></marker></defs>')


def instance(body, x, y, label, cls="box", w=84):
    body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="34" rx="5"/>')
    body.append(f'<text class="small" x="{x + w / 2}" y="{y + 21}" text-anchor="middle">{label}</text>')


def health_frames():
    """Three numbered frames: healthy, one instance fails, Auto Scaling replaces it."""
    w, pw, gap, top, ph = 700, 216, 10, 64, 300
    body = [ARROW,
            '<text class="title" x="16" y="28">When an instance fails, both services act</text>',
            '<text class="sub" x="16" y="48">Three moments in one Auto Scaling group behind a load balancer, minimum 2, one per AZ</text>']
    frames = [
        ("Both instances healthy", [("Instance 1", "box", True), ("Instance 2", "box", True)],
         "The load balancer splits requests between the two AZs."),
        ("Instance 1 fails its health check", [("Instance 1", "crit", False), ("Instance 2", "box", True)],
         "The load balancer stops sending it requests. Instance 2 carries the site."),
        ("Auto Scaling replaces it", [("Instance 3", "hi", True), ("Instance 2", "box", True)],
         "The new instance registers with the load balancer and takes requests again."),
    ]
    for i, (head, insts, line) in enumerate(frames):
        x = 16 + i * (pw + gap)
        body.append(f'<rect class="panel" x="{x}" y="{top}" width="{pw}" height="{ph}" rx="8"/>')
        body.append(f'<circle cx="{x + 22}" cy="{top + 22}" r="11" style="fill:var(--ink)"/>')
        body.append(f'<text class="num" x="{x + 22}" y="{top + 27}" text-anchor="middle">{i + 1}</text>')
        text_lines(body, x + 40, top + 27, wrap(head, 24), cls="cellt", dy=16)
        body.append(f'<rect class="box" x="{x + 18}" y="{top + 64}" width="{pw - 36}" height="30" rx="5"/>')
        body.append(f'<text class="small" x="{x + pw / 2}" y="{top + 83}" text-anchor="middle">Load balancer</text>')
        for j, (label, cls, gets) in enumerate(insts):
            ax = x + 14 + j * 100
            body.append(f'<rect class="zone" x="{ax}" y="{top + 116}" width="90" height="84" rx="6"/>')
            body.append(f'<text class="note" x="{ax + 45}" y="{top + 194}" text-anchor="middle">AZ {"ab"[j]}</text>')
            instance(body, ax + 6, top + 140, label, cls, w=78)
            if cls == "crit":
                cx, cy = ax + 76, top + 146
                body.append(f'<path class="ci" d="M{cx - 5},{cy - 5} L{cx + 5},{cy + 5} M{cx + 5},{cy - 5} L{cx - 5},{cy + 5}"/>')
            if gets:
                body.append(f'<line class="flow" x1="{ax + 45}" y1="{top + 94}" x2="{ax + 45}" y2="{top + 138}" marker-end="url(#ab)"/>')
            else:
                body.append(f'<text class="small" x="{ax + 45}" y="{top + 112}" text-anchor="middle">no requests</text>')
        text_lines(body, x + 14, top + 226, wrap(line, 30), cls="small", dy=16)
    body.append(f'<text class="note" x="16" y="{top + ph + 22}">Blue arrows: requests. Our summary of the EC2 Auto Scaling and Elastic Load Balancing user guides, checked 2026-10-24.</text>')
    svg("06-02-health-frames.svg", w, top + ph + 36,
        "Three frames: a failed instance is skipped by the load balancer and replaced by Auto Scaling",
        "Three numbered frames, each with a load balancer above two Availability Zones, a and b. "
        "Frame 1, both instances healthy: requests go to instance 1 in AZ a and instance 2 in AZ b; the load balancer "
        "splits requests between the two AZs. Frame 2, instance 1 fails its health check, marked with a cross: it gets "
        "no requests, and instance 2 carries the site. Frame 3, Auto Scaling replaces it: a new instance 3, highlighted, "
        "runs in AZ a, registers with the load balancer and takes requests again, alongside instance 2.",
        body, style=STYLE)


if __name__ == "__main__":
    health_frames()
