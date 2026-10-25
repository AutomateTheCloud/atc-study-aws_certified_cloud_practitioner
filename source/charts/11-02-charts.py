#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 11.02 (purchasing options) as SVG.

Usage: python3 -I source/charts/11-02-charts.py
Writes images/11-02-*.svg. Facts, checked 2026-10-24 on AWS pages:
- Savings Plans types and maximum discounts (Compute up to 66%, EC2 Instance up to 72%,
  Database up to 35%, SageMaker AI up to 64%) and what each covers: Savings Plans User Guide,
  "Savings Plans types".
- Reserved Instances: up to 72%; Standard up to 72% with averages of 40% (1 year) and 60%
  (3 years); Convertible up to 66% with averages of 31% and 54%: Amazon EC2 Reserved
  Instances pricing page. Zonal vs Regional, instance size flexibility and normalization
  factors (small 1, medium 2, large 4) and the t2.medium example: EC2 User Guide, "How
  Reserved Instance discounts are applied".
- Spot up to 90%: Amazon EC2 Spot Instances page. Dedicated Host Reservations up to 70%:
  EC2 User Guide, "Amazon EC2 Dedicated Hosts". Capacity Reservations give no billing
  discount: EC2 User Guide, "Reserve compute capacity with EC2 On-Demand Capacity
  Reservations".
- Dedicated Host vs Dedicated Instance rows: EC2 User Guide, "Amazon EC2 Dedicated Hosts"
  comparison table; the $2 per hour per Region fee for Dedicated Instances: Savings Plans
  User Guide, "Savings Plans types".
- Prices, US East (N. Virginia), Linux, shared tenancy: t3.small On-Demand $0.0208/hour and
  1-year Standard No Upfront Reserved Instance $0.013/hour (effective), from the AmazonEC2
  offer file published 2026-10-23, retrieved 2026-10-24 (research repo
  sources/raw/pricing/compute-networking-us-east-1-summary.tsv).
The bakery's server counts are Module 02's made-up teaching figures with Module 06's
Auto Scaling minimum of 2. Yearly figures are our arithmetic (8,760 hours a year, 730 a
month). Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import MONTHS, make_style, month_axes, right_rounded, svg, swatch, text_lines, top_rounded, wrap  # noqa: E402

OD, RI = 0.0208, 0.013            # t3.small, USD per hour
MONTH_H, YEAR_H = 730, 8760
RUN = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 6]   # instances an Auto Scaling group with a minimum of 2 runs
BASE = 2

STYLE = make_style(
    light_extra=" --panel:#f1f0ec; --hi-fill:#d9e8fb; --s3:#1baf7a; --no-fill:#f6f5f2;",
    dark_extra=" --panel:#252523; --hi-fill:#1b3554; --s3:#199e70; --no-fill:#1f1f1e;",
    rules_extra="""
  .panel { fill: var(--panel); stroke: var(--axis); stroke-width: 1; }
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 1.5; }
  .no { fill: var(--no-fill); stroke: var(--grid); stroke-width: 1; }
  .box { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .head { fill: var(--ink); font-size: 15px; font-weight: 600; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .val { fill: var(--ink); font-size: 13px; font-variant-numeric: tabular-nums; }
  .yes { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .avg { fill: var(--ink); stroke: var(--surface); stroke-width: 2; }
  .unit { fill: var(--s1); stroke: var(--surface); stroke-width: 2; }
  .unit-od { fill: var(--s2); stroke: var(--surface); stroke-width: 2; }
  .s3 { fill: var(--s3); }""")


def flexibility():
    """What the discount keeps following when usage changes."""
    cols = ["Compute Savings Plan", "EC2 Instance Savings Plan", "Regional Reserved Instance", "Zonal Reserved Instance"]
    rows = [
        ("Change instance family", ["Yes", "No: one family", "No", "No"]),
        ("Change instance size", ["Yes", "Yes", "Yes*", "No"]),
        ("Change Availability Zone", ["Yes", "Yes", "Yes", "No"]),
        ("Change Region", ["Yes", "No: one Region", "No", "No"]),
        ("Change operating system", ["Yes", "Yes", "No", "No"]),
        ("Change tenancy", ["Yes", "Yes", "No", "No"]),
        ("Covers Fargate and Lambda", ["Yes", "No", "No", "No"]),
        ("Reserves capacity", ["No", "No", "No", "Yes, in one AZ"]),
        ("You commit to", ["$ per hour", "$ per hour", "one configuration", "one configuration"]),
        ("Discount, up to", ["66%", "72%", "72% (Standard)", "72% (Standard)"]),
    ]
    w, left, top, cw, rowh = 720, 196, 74, 130, 32
    h = top + 40 + rowh * len(rows) + 52
    body = [
        '<text class="title" x="16" y="28">When your usage changes, which discounts follow it?</text>',
        '<text class="sub" x="16" y="48">Highlighted cells: the discount keeps applying after that change, with nothing to buy or exchange</text>',
    ]
    for j, c in enumerate(cols):
        x = left + j * cw
        text_lines(body, x + cw / 2, top + 4, wrap(c, 18), cls="cellt", dy=15, anchor="middle")
    for i, (r, vals) in enumerate(rows):
        y = top + 40 + i * rowh
        body.append(f'<text class="lab" x="16" y="{y + 20}">{r}</text>')
        for j, v in enumerate(vals):
            x = left + j * cw
            good = v.startswith("Yes") and r != "Reserves capacity" or (r == "Reserves capacity" and v.startswith("Yes"))
            cls = "hi" if good and i < 8 else ("panel" if i >= 8 else "no")
            body.append(f'<rect class="{cls}" x="{x + 3}" y="{y + 2}" width="{cw - 6}" height="{rowh - 4}" rx="4"/>')
            mark = ("✓ " if good and i < 8 else ("✗ " if i < 8 else "")) + v
            body.append(f'<text class="{"yes" if good else "small"}" x="{x + cw / 2}" y="{y + 20}" text-anchor="middle">{mark}</text>')
    body.append(f'<text class="note" x="16" y="{h - 26}">* Size flexibility: Linux/Unix on default tenancy, within one family; not Windows, RHEL, SUSE,</text>')
    body.append(f'<text class="note" x="16" y="{h - 10}">dedicated tenancy or some GPU families. Sources: AWS Savings Plans and EC2 User Guides, checked 2026-10-24.</text>')
    desc = ". ".join(f"{r}: " + ", ".join(f"{c} {v}" for c, v in zip(cols, vals)) for r, vals in rows)
    svg("11-02-flexibility.svg", w, h,
        "Which usage changes Compute and EC2 Instance Savings Plans and Regional and zonal Reserved Instances keep covering",
        f"A table of ten rows and four columns, as of 2026-10-24. {desc}. Size flexibility for Regional Reserved "
        "Instances applies to Linux/Unix on default tenancy only.", body, style=STYLE)


def host_vs_instance():
    """Dedicated Host vs Dedicated Instance, side by side."""
    w, h = 720, 456
    body = [
        '<text class="title" x="16" y="28">Dedicated Host or Dedicated Instance?</text>',
        '<text class="sub" x="16" y="48">Same: single-tenant hardware, no other customer on it, no difference in performance or security</text>',
    ]
    panels = [
        ("Dedicated Host", "A whole physical server, yours to place instances on", [
            ("You see", "its sockets, cores and host ID"),
            ("You place", "instances on the host you choose, and keep them there"),
            ("Billing", "per host, whatever runs on it"),
            ("Your licenses", "per-socket, per-core or per-VM (BYOL)"),
            ("Capacity Reservations", "not supported"),
            ("Discount", "Host Reservations, up to 70%"),
        ], "Choose it for: software licensed by socket or core"),
        ("Dedicated Instance", "An instance on hardware only your account uses", [
            ("You see", "nothing about the hardware"),
            ("You place", "nothing: AWS places it, and after a stop and start it may move"),
            ("Billing", "per instance, plus a $2 an hour fee per Region while any runs"),
            ("Your licenses", "partial support only"),
            ("Capacity Reservations", "supported"),
            ("Discount", "Reserved Instances with dedicated tenancy"),
        ], "Choose it for: a rule that says no shared hardware"),
    ]
    pw, top = 336, 66
    for k, (name, line, rows, foot) in enumerate(panels):
        x = 16 + k * (pw + 16)
        body.append(f'<rect class="{"hi" if k == 0 else "panel"}" x="{x}" y="{top}" width="{pw}" height="356" rx="8"/>')
        body.append(f'<text class="head" x="{x + 14}" y="{top + 26}">{name}</text>')
        body.append(f'<text class="small" x="{x + 14}" y="{top + 44}">{line}</text>')
        y = top + 72
        for lab, val in rows:
            body.append(f'<text class="cellt" x="{x + 14}" y="{y}">{lab}</text>')
            y = text_lines(body, x + 14, y + 16, wrap(val, 46), cls="small", dy=15) + 6
        body.append(f'<text class="cellt" x="{x + 14}" y="{top + 342}">{foot}</text>')
    body.append(f'<text class="note" x="16" y="{h - 12}">Sources: EC2 User Guide, Dedicated Hosts and Dedicated Instances; Savings Plans types (the $2 fee). Checked 2026-10-24.</text>')
    svg("11-02-host-vs-instance.svg", w, h,
        "Dedicated Host compared with Dedicated Instance",
        "Two panels. What's the same: single-tenant hardware, no other customer on it, and no difference in "
        "performance or security. Dedicated Host, a whole physical server you place instances on: you see its "
        "sockets, cores and host ID; you place instances on the host you choose and keep them there; billed per "
        "host; supports per-socket, per-core or per-VM licenses you bring; no Capacity Reservations; Host "
        "Reservations give up to 70% off. Choose it for software licensed by socket or core. Dedicated Instance, "
        "an instance on hardware only your account uses: you see nothing about the hardware; AWS places it and it "
        "may move after a stop and start; billed per instance plus a $2 an hour fee per Region while any runs; "
        "partial license support; Capacity Reservations supported; Reserved Instances with dedicated tenancy for a "
        "discount. Choose it for a rule that says no shared hardware. As of 2026-10-24.", body, style=STYLE)


if __name__ == "__main__":
    flexibility()
    host_vs_instance()
