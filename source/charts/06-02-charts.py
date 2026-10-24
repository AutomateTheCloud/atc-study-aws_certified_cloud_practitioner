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
from chartkit import MONTHS, make_style, month_axes, svg, swatch, text_lines, top_rounded, wrap  # noqa: E402

# Servers needed in each month's busiest hour, from Module 02 (source/charts/02-02-charts.py)
NEEDED = [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 3, 6]
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


def big_picture():
    """Load balancer in front of an Auto Scaling group that spans two AZs."""
    w, h = 700, 560
    body = [ARROW,
            '<text class="title" x="16" y="28">Auto Scaling decides how many; the load balancer decides which</text>',
            '<text class="sub" x="16" y="48">The bakery\'s order site in two Availability Zones (made-up sizes)</text>']
    body.append('<rect class="box" x="260" y="64" width="180" height="32" rx="6"/>')
    body.append('<text class="cellt" x="350" y="85" text-anchor="middle">Customers\' browsers</text>')
    body.append('<line class="flow" x1="350" y1="96" x2="350" y2="146" marker-end="url(#ab)"/>')
    body.append('<text class="small" x="360" y="124">orders, over HTTPS</text>')
    body.append('<rect class="zone" x="16" y="112" width="668" height="372" rx="10"/>')
    body.append('<text class="small" x="28" y="130">Region: US East (N. Virginia)</text>')
    body.append('<rect class="hi" x="110" y="148" width="480" height="40" rx="6"/>')
    body.append('<text class="cellt" x="350" y="173" text-anchor="middle">Application Load Balancer, in both AZs</text>')
    for x, name in ((96, "Availability Zone a"), (364, "Availability Zone b")):
        body.append(f'<rect class="zone" x="{x}" y="200" width="240" height="196" rx="8"/>')
        body.append(f'<text class="small" x="{x + 12}" y="218">{name}</text>')
    body.append('<rect class="group" x="110" y="230" width="480" height="150" rx="8"/>')
    body.append('<text class="cellt" x="124" y="250">Auto Scaling group: minimum 2, maximum 8</text>')
    spots = [(140, "Instance 1", "box"), (240, "Instance 3", "boxdash"), (408, "Instance 2", "box"), (508, "Instance 4", "boxdash")]
    for x, label, cls in spots:
        instance(body, x, 290, label, cls)
        body.append(f'<line class="flow" x1="{350 + (x + 42 - 350) * 0.55:.1f}" y1="188" x2="{x + 42}" y2="288" marker-end="url(#ab)"/>')
    text_lines(body, 124, 344, ["Solid: the minimum, one per AZ.", "Dashed: added when orders rise,", "removed when they fall."], cls="note", dy=14)
    body.append('<rect class="panel" x="110" y="424" width="480" height="44" rx="6"/>')
    body.append('<text class="cellt" x="350" y="443" text-anchor="middle">Launch template</text>')
    body.append('<text class="small" x="350" y="460" text-anchor="middle">AMI + instance type + security group: the recipe for each new instance</text>')
    body.append('<line class="wire" x1="350" y1="424" x2="350" y2="382" marker-end="url(#ah)"/>')
    body.append('<text class="small" x="358" y="408">launches from</text>')
    y = text_lines(body, 16, 506, ["Load balancer: which healthy instance gets each request.",
                                   "Auto Scaling group: how many instances run, and in which AZs."], cls="lab", dy=19)
    svg("06-02-big-picture.svg", w, h,
        "A load balancer in front of an Auto Scaling group that spans two Availability Zones",
        "Customers' browsers send orders over HTTPS to an Application Load Balancer that sits in both "
        "Availability Zones of the US East (N. Virginia) Region. The load balancer sends requests to four "
        "instances. An Auto Scaling group, minimum 2 and maximum 8, spans both AZs: instance 1 in AZ a and "
        "instance 2 in AZ b are the minimum, one per AZ; instances 3 in AZ a and 4 in AZ b are dashed, added "
        "when orders rise and removed when they fall. Below, a launch template (AMI plus instance type plus "
        "security group) is the recipe the group launches each new instance from. Summary: the load balancer "
        "decides which healthy instance gets each request; the Auto Scaling group decides how many instances "
        "run, and in which AZs.", body, style=STYLE)


def year_with_minimum():
    """Module 02's year: servers needed in each month's busiest hour, and what a group with a minimum of 2 runs."""
    run = [min(MAX, max(MIN, n)) for n in NEEDED]
    w, h, left, top, pw, ph, ymax = 680, 420, 56, 120, 520, 236, 8
    body = [
        '<text class="title" x="16" y="28">The bakery\'s year with Auto Scaling: never fewer than 2</text>',
        '<text class="sub" x="16" y="48">Servers in each month\'s busiest hour (made-up figures from Module 02)</text>',
    ]
    swatch(body, 16, 80, "s1", "Instances the group runs (minimum 2)")
    body.append('<circle cx="292" cy="76" r="5" style="fill:var(--ink);stroke:var(--surface);stroke-width:2"/>')
    body.append('<text x="304" y="80">Servers the orders need</text>')
    body.append('<line class="dash-ink" x1="480" x2="496" y1="76" y2="76"/>')
    body.append('<text x="502" y="80">Fixed fleet of 6</text>')
    band = month_axes(body, left, top, pw, ph, ymax, "Servers", step=2)
    unit = ph / ymax
    bw = 24
    for i, (n, need) in enumerate(zip(run, NEEDED)):
        x = left + band * i + (band - bw) / 2
        body.append(f'<path class="s1" d="{top_rounded(x, top + ph - n * unit, bw, n * unit)}"><title>{MONTHS[i]}: {need} needed, {n} running</title></path>')
        body.append(f'<circle cx="{x + bw / 2:.1f}" cy="{top + ph - need * unit:.1f}" r="5" style="fill:var(--ink);stroke:var(--surface);stroke-width:2"><title>{MONTHS[i]}: {need} needed</title></circle>')
    yf = top + ph - FIXED * unit
    body.append(f'<line class="dash-ink" x1="{left}" x2="{left + pw}" y1="{yf:.1f}" y2="{yf:.1f}"/>')
    body.append(f'<text class="lab" x="{left + pw + 8}" y="{yf + 4:.1f}">6 fixed</text>')
    xj = left + band / 2
    body.append(f'<line class="lead" x1="{xj:.1f}" y1="{top + ph - 2 * unit - 4:.1f}" x2="{xj:.1f}" y2="{top + ph - 3.4 * unit:.1f}"/>')
    body.append(f'<text class="lab" x="{xj - 8:.1f}" y="{top + ph - 3.4 * unit - 6:.1f}">January: 1 needed, 2 run, one per AZ</text>')
    xd = left + band * 11 + (band - bw) / 2
    body.append(f'<text class="lab" x="{xd - 8:.1f}" y="{top + ph - 6 * unit - 10:.1f}" text-anchor="end">December: 6</text>')
    sm = sum(run)
    body.append(f'<text class="sub" x="16" y="{h - 30}">Server-months: {sum(NEEDED)} if capacity only followed demand; {sm} with a minimum of 2; {FIXED * 12} with a fixed fleet of 6.</text>')
    body.append(f'<text class="note" x="16" y="{h - 12}">Busiest hour of each month; inside each day the group also shrinks at night (Simulation S7 works through one day).</text>')
    svg("06-02-year-with-minimum.svg", w, h,
        "Servers the bakery needs each month and the instances an Auto Scaling group with a minimum of 2 runs",
        "Column chart, January to December, from Module 02's made-up figures for each month's busiest hour. "
        "Servers the orders need: " + ", ".join(str(n) for n in NEEDED) + ". Instances an Auto Scaling group with a "
        "minimum of 2 and a maximum of 8 runs: " + ", ".join(str(n) for n in run) + ". A dashed line at 6 shows a fixed "
        f"fleet sized for December. Server-months: {sum(NEEDED)} following demand alone, {sm} with the minimum of 2, "
        f"{FIXED * 12} with the fixed fleet.", body, style=STYLE)


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
    big_picture()
    year_with_minimum()
    health_frames()
