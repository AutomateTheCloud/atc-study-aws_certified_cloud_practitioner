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


def ceilings():
    """'Up to' figures are ceilings: AWS's stated maximums, with averages where AWS gives them."""
    rows = [("Spot Instances", 90, None),
            ("Standard Reserved Instances", 72, (40, 60)),
            ("EC2 Instance Savings Plans", 72, None),
            ("Dedicated Host Reservations", 70, None),
            ("Convertible Reserved Instances", 66, (31, 54)),
            ("Compute Savings Plans", 66, None),
            ("SageMaker AI Savings Plans", 64, None),
            ("Database Savings Plans", 35, None),
            ("Capacity Reservations", 0, None),
            ("On-Demand (the baseline)", 0, None)]
    w, left, top, pw, rowh = 720, 230, 104, 420, 34
    h = top + rowh * len(rows) + 70
    sx = lambda v: pw * v / 100
    body = [
        '<text class="title" x="16" y="28">"Up to" is a ceiling, not the discount you get</text>',
        '<text class="sub" x="16" y="48">Largest discount off On-Demand that AWS states for each option, as of 2026-10-24</text>',
    ]
    swatch(body, 16, 80, "s1l", "Stated maximum (\"up to\")")
    body.append('<circle class="avg" cx="230" cy="75" r="6"/>')
    body.append('<text x="242" y="80">Stated average: 1-year term, then 3-year term</text>')
    for v in range(0, 101, 25):
        x = left + sx(v)
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 4}" y2="{top + rowh * len(rows)}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top + rowh * len(rows) + 18}" text-anchor="middle">{v}%</text>')
    for i, (name, mx, avg) in enumerate(rows):
        y = top + i * rowh + 7
        body.append(f'<text class="lab" x="16" y="{y + 15}">{name}</text>')
        if mx:
            body.append(f'<path class="s1l" d="{right_rounded(left, y, sx(mx), 20)}"><title>{name}: up to {mx}%</title></path>')
            body.append(f'<text class="val" x="{left + sx(mx) + 8:.1f}" y="{y + 15}">up to {mx}%</text>')
        else:
            body.append(f'<text class="val" x="{left + 8}" y="{y + 15}">no discount</text>')
        if avg:
            for a in avg:
                body.append(f'<circle class="avg" cx="{left + sx(a):.1f}" cy="{y + 10}" r="6"><title>{name}: average {a}%</title></circle>')
            body.append(f'<text class="small" x="{left + sx(avg[0]) - 10:.1f}" y="{y + 15}" text-anchor="end">avg {avg[0]}%, {avg[1]}%</text>')
    body.append(f'<text class="note" x="16" y="{h - 42}">Maximums need the longest term, the most paid upfront and the configurations with the biggest gaps. Older material says</text>')
    body.append(f'<text class="note" x="16" y="{h - 26}">"up to 75%"; the figures moved, and will again. Sources: AWS pages for Savings Plans types, Reserved Instances pricing,</text>')
    body.append(f'<text class="note" x="16" y="{h - 10}">Spot Instances, Dedicated Hosts and Capacity Reservations, checked 2026-10-24.</text>')
    desc = "; ".join(f"{n}: " + (f"up to {m}%" if m else "no discount") + (f", averages {a[0]}% for 1 year and {a[1]}% for 3 years" if a else "") for n, m, a in rows)
    svg("11-02-up-to-vs-average.svg", w, h,
        "The maximum discount AWS states for each purchasing option, with averages where AWS gives them",
        f"Horizontal bar chart, percent off On-Demand, as of 2026-10-24. {desc}. Maximums need the longest term "
        "and most upfront payment; older material says up to 75%.", body, style=STYLE)


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


def size_flex():
    """A Regional Reserved Instance counts in normalized units across sizes."""
    w, h = 720, 330
    body = [
        '<text class="title" x="16" y="28">A Regional Reserved Instance covers units, not one exact size</text>',
        '<text class="sub" x="16" y="48">One t3.medium Regional Reserved Instance (Linux) is worth 2 units an hour. Each square is one unit.</text>',
    ]
    unit, gap = 30, 4
    cases = [
        ("Two t3.small (1 unit each)", [1, 1], 2, "Fully covered"),
        ("One t3.medium (2 units)", [2], 2, "Fully covered"),
        ("One t3.large (4 units)", [4], 2, "Half covered; the rest at On-Demand"),
    ]
    y = 84
    for name, inst, covered, verdict in cases:
        body.append(f'<text class="cellt" x="16" y="{y + 20}">{name}</text>')
        x = 250
        used = 0
        for n in inst:
            bx = x
            for k in range(n):
                cls = "unit" if used < covered else "unit-od"
                body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{unit}" height="{unit}" rx="4"/>')
                used += 1
                x += unit + gap
            body.append(f'<rect fill="none" style="stroke:var(--ink2);stroke-width:1.2" x="{bx - 3}" y="{y - 3}" width="{x - bx - gap + 6}" height="{unit + 6}" rx="6"/>')
            x += 14
        body.append(f'<text class="lab" x="{x + 6}" y="{y + 20}">{verdict}</text>')
        y += 64
    swatch(body, 16, y + 10, "s1", "Covered by the Reserved Instance")
    swatch(body, 280, y + 10, "s2", "Paid at On-Demand rates")
    body.append(f'<text class="note" x="16" y="{y + 38}">Units per size: small 1, medium 2, large 4, xlarge 8. A zonal Reserved Instance has no size flexibility: it covers only its exact type.</text>')
    body.append(f'<text class="note" x="16" y="{y + 54}">Source: EC2 User Guide, "How Reserved Instance discounts are applied", checked 2026-10-24.</text>')
    svg("11-02-size-flex.svg", w, y + 66,
        "How one t3.medium Regional Reserved Instance covers different sizes in its family",
        "One t3.medium Regional Reserved Instance for Linux is worth 2 normalized units an hour. Case 1: two "
        "t3.small instances, 1 unit each, are fully covered. Case 2: one t3.medium, 2 units, is fully covered. "
        "Case 3: one t3.large, 4 units, is half covered, and the other 2 units are paid at On-Demand rates. Units "
        "per size: small 1, medium 2, large 4, xlarge 8. A zonal Reserved Instance has no size flexibility.",
        body, style=STYLE)


def bakery_year():
    """The bakery's year: a steady base all year, a peak in November and December."""
    w, left, top, pw, ph, ymax = 720, 64, 120, 620, 220, 6
    h = top + ph + 74
    body = [
        '<text class="title" x="16" y="28">A steady base all year, a peak at the end</text>',
        '<text class="sub" x="16" y="48">Web servers the bakery\'s Auto Scaling group runs at each month\'s busiest hour (minimum of 2)</text>',
    ]
    swatch(body, 16, 80, "s1", "Base: 2 servers every hour of the year")
    swatch(body, 330, 80, "s2", "Peak: extra servers, only when needed")
    band = month_axes(body, left, top, pw, ph, ymax, "Servers", step=1)
    unit = ph / ymax
    bw = band * 0.6
    for i, n in enumerate(RUN):
        x = left + band * i + (band - bw) / 2
        base_h = BASE * unit
        body.append(f'<rect class="s1" x="{x:.1f}" y="{top + ph - base_h:.1f}" width="{bw:.1f}" height="{base_h:.1f}"><title>{MONTHS[i]}: 2 base servers</title></rect>')
        if n > BASE:
            ex = (n - BASE) * unit
            body.append(f'<path class="s2" d="{top_rounded(x, top + ph - base_h - ex, bw, ex - 2)}"><title>{MONTHS[i]}: {n - BASE} extra</title></path>')
            body.append(f'<text class="val" x="{x + bw / 2:.1f}" y="{top + ph - n * unit - 6:.1f}" text-anchor="middle">+{n - BASE}</text>')
    body.append(f'<text class="note" x="16" y="{h - 26}">Made-up teaching figures from Modules 02 and 06. Inside each day the group also shrinks at night;</text>')
    body.append(f'<text class="note" x="16" y="{h - 10}">this chart counts each month at its busiest hour, as Module 06 did.</text>')
    svg("11-02-bakery-year.svg", w, h,
        "The bakery's web servers each month: a steady base of 2 and a peak in November and December",
        "Stacked column chart, January to December. Every month has a base of 2 servers. November adds 1 extra "
        "server and December adds 4, for 3 and 6 in total. Made-up teaching figures from Modules 02 and 06.",
        body, style=STYLE)


def strategies():
    """A year of web servers paid three ways."""
    ondemand = sum(RUN) * MONTH_H * OD
    base_ri = BASE * YEAR_H * RI
    peak_od = sum(n - BASE for n in RUN) * MONTH_H * OD
    peak_ri = max(RUN) * YEAR_H * RI
    rows = [("All On-Demand", [("s2", ondemand, "On-Demand")], "pay for what runs"),
            ("Commit to the base, peak On-Demand", [("s1", base_ri, "Reserved base"), ("s2", peak_od, "On-Demand peak")], "the usual answer"),
            ("Commit to the peak (6 all year)", [("s1", peak_ri, "Reserved, mostly unused")], "pays for idle commitments")]
    w, left, top, pw, rowh, xmax = 720, 270, 104, 360, 58, 700
    h = top + rowh * len(rows) + 64
    sx = lambda v: pw * v / xmax
    body = [
        '<text class="title" x="16" y="28">A year of the bakery\'s web servers, paid three ways</text>',
        '<text class="sub" x="16" y="48">t3.small, Linux, US East (N. Virginia), as of 2026-10-24</text>',
    ]
    swatch(body, 16, 80, "s2", "On-Demand, $0.0208 an hour")
    swatch(body, 240, 80, "s1", "1-year Standard Reserved Instance, no upfront, $0.013 an hour")
    for v in range(0, xmax + 1, 100):
        x = left + sx(v)
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 4}" y2="{top + rowh * len(rows)}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top + rowh * len(rows) + 18}" text-anchor="middle">${v}</text>')
    totals = []
    for i, (label, segs, sub) in enumerate(rows):
        y = top + i * rowh + 10
        body.append(f'<text class="lab" x="16" y="{y + 12}">{label}</text>')
        body.append(f'<text class="small" x="16" y="{y + 28}">{sub}</text>')
        x = left
        for j, (cls, v, what) in enumerate(segs):
            wd = sx(v) - (2 if j < len(segs) - 1 else 0)
            if j == len(segs) - 1:
                body.append(f'<path class="{cls}" d="{right_rounded(x, y, wd, 24)}"><title>{label}: {what} ${v:,.2f}</title></path>')
            else:
                body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{wd:.1f}" height="24"><title>{label}: {what} ${v:,.2f}</title></rect>')
            x += sx(v)
        tot = sum(v for _, v, _ in segs)
        totals.append((label, tot, segs))
        body.append(f'<text class="val" x="{x + 8:.1f}" y="{y + 17}">${tot:,.2f}</text>')
    body.append(f'<text class="note" x="16" y="{h - 26}">29 server-months in all. A Savings Plan for the base works the same way at its own rate. Our arithmetic from</text>')
    body.append(f'<text class="note" x="16" y="{h - 10}">AWS\'s EC2 price list (published 2026-10-23); 8,760 hours a year, 730 a month.</text>')
    desc = "; ".join(f"{l}: " + " plus ".join(f"{w} ${v:,.2f}" for _, v, w in s) + f", total ${t:,.2f}" for l, t, s in totals)
    svg("11-02-three-strategies.svg", w, h,
        "A year of the bakery's web servers paid three ways",
        f"Horizontal bar chart, US dollars for a year of t3.small Linux servers in US East (N. Virginia) as of "
        f"2026-10-24. {desc}. Committing to the base is cheapest; committing to the peak costs more than On-Demand.",
        body, style=STYLE)
    return totals


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
    ceilings()
    flexibility()
    size_flex()
    bakery_year()
    for t in strategies():
        print(t[0], round(t[1], 2), [(w, round(v, 2)) for _, v, w in t[2]])
    host_vs_instance()
