#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 11.01 (how AWS charges) as SVG.

Usage: python3 -I source/charts/11-01-charts.py
Writes images/11-01-*.svg. Facts, checked 2026-10-24:
- prices, US East (N. Virginia), USD, from the AWS Price List offer files summarized in the
  research repo (sources/raw/pricing/): t3.small $0.0208/hour, Application Load Balancer
  $0.0225/hour, NAT gateway $0.045/hour and $0.045/GB processed, EBS gp3 $0.08/GB-month
  (AmazonEC2 and AWSELB, published 2026-10-23, retrieved 2026-10-24); S3 Standard
  $0.023/GB-month for the first 50 TB, GET $0.0004 per 1,000 (AmazonS3, published
  2026-10-15); data transfer out to the internet $0.09/GB for the first 10 TB after
  100 GB free each month, across Availability Zones $0.01/GB in each direction, to US East
  (Ohio) $0.01/GB and to most other Regions $0.02/GB (AWSDataTransfer, published
  2026-09-16). Lambda's monthly free allowance (1 million requests, 400,000 GB-seconds):
  AWS Lambda pricing page, checked 2026-10-23.
- free transfers (in from the internet; same AZ over private addresses; EC2 to S3 in the
  same Region; S3 to CloudFront): EC2 On-Demand and S3 pricing pages, checked 2026-10-23.
- Free Tier: AWS Free Tier page and Billing User Guide "Explore AWS services with AWS Free
  Tier" and "Choosing a plan" (checked 2026-10-24): $100 in credits plus up to $100 more;
  the Free plan ends after 6 months or when the credits are used, then the account closes
  and AWS keeps content for 90 days; Always Free on both plans; short-term trials only on
  the Paid plan; "up to $200 over 6 months" on the Free plan (AWS Free Tier page). Expiry of
  leftover credits after an upgrade is disputed: two Free Tier FAQ answers say 6 months, two FAQ
  answers and the Free Tier terms say 12; the Credits page of our own Free plan account
  (2026-10-23) showed 12.
  Accounts created before 2025-07-15 stay on the legacy Free Tier: AWS tutorial "Control
  your AWS costs".
The bakery's quantities are made up for teaching; the order database is left out because
its charge doesn't change between the two months. Monthly figures are our arithmetic for a
730-hour month. Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, swatch, text_lines, wrap  # noqa: E402

HOURS = 730
T3_SMALL, ALB, NAT_H, NAT_GB, GP3 = 0.0208, 0.0225, 0.045, 0.045, 0.08
S3_STD, S3_GET = 0.023, 0.0004 / 1000
OUT, XAZ = 0.09, 0.02          # XAZ: $0.01 charged on each side

STYLE = make_style(
    light_extra=" --panel:#f1f0ec; --hi-fill:#d9e8fb; --s3:#1baf7a; --s4:#eda100; --warm-fill:#fbe1d6;",
    dark_extra=" --panel:#252523; --hi-fill:#1b3554; --s3:#199e70; --s4:#c98500; --warm-fill:#4d2716;",
    rules_extra="""
  .panel { fill: var(--panel); stroke: var(--axis); stroke-width: 1; }
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 1.5; }
  .warm { fill: var(--warm-fill); stroke: var(--s2); stroke-width: 1.5; }
  .zone { fill: none; stroke: var(--muted); stroke-width: 1.2; stroke-dasharray: 5 4; }
  .box { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .head { fill: var(--ink); font-size: 15px; font-weight: 600; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .val { fill: var(--ink); font-size: 13px; font-variant-numeric: tabular-nums; }
  .arrlab { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .free { stroke: var(--s3); stroke-width: 2.5; fill: none; }
  .paid { stroke: var(--s2); stroke-width: 2.5; fill: none; }
  .ahead-free { fill: var(--s3); }
  .ahead-paid { fill: var(--s2); }
  .s3 { fill: var(--s3); } .s4 { fill: var(--s4); }
  .conn { stroke: var(--muted); stroke-width: 1; stroke-dasharray: 3 3; }
  .dashext { fill: none; stroke: var(--s3); stroke-width: 1.5; stroke-dasharray: 5 4; }""")


def bill():
    """The bakery's two months, line by line. Returns (rows, nov_total, dec_total)."""
    rows = [
        # (line item, meter, November, December)
        ("Web servers (t3.small hours)", "Time", 2 * HOURS * T3_SMALL, 4 * HOURS * T3_SMALL),
        ("Load balancer hours", "Time", HOURS * ALB, HOURS * ALB),
        ("NAT gateway hours (new in December)", "Time", 0.0, HOURS * NAT_H),
        ("Server disks (EBS gp3, 8 GB each)", "Storage", 2 * 8 * GP3, 4 * 8 * GP3),
        ("Photo bucket (S3 Standard)", "Storage", 200 * S3_STD, 260 * S3_STD),
        ("Photo downloads (S3 GET requests)", "Requests", 2_000_000 * S3_GET, 6_000_000 * S3_GET),
        ("Photo resizing (Lambda)", "Requests", 0.0, 0.0),
        ("Data out to the internet", "Data transfer", (300 - 100) * OUT, (900 - 100) * OUT),
        ("Web server to database, across AZs", "Data transfer", 100 * XAZ, 300 * XAZ),
        ("Data processed by the NAT gateway", "Data transfer", 0.0, 150 * NAT_GB),
    ]
    rows = [(a, b, round(c, 2), round(d, 2)) for a, b, c, d in rows]
    return rows, round(sum(r[2] for r in rows), 2), round(sum(r[3] for r in rows), 2)


def four_meters():
    """Big picture: every line on a bill is a quantity on one of four meters, times a rate."""
    w, h = 720, 430
    body = [
        '<text class="title" x="16" y="28">Every line on a bill is a quantity times a rate</text>',
        '<text class="sub" x="16" y="48">Most charges run on one of four meters. The bakery\'s resources, sorted by meter:</text>',
    ]
    cols = [
        ("Time", "hours or seconds a resource exists or runs", "s1",
         ["EC2 web servers", "Load balancer", "NAT gateway", "RDS database", "Public IPv4 addresses"],
         "Bills while it exists, busy or idle"),
        ("Storage", "GB kept, per month", "s3",
         ["S3 photo bucket", "EBS disks (size you set)", "RDS storage, backups", "Snapshots"],
         "Bills for what you keep, until deleted"),
        ("Requests", "calls and runs, by the count", "s4",
         ["S3 GET and PUT", "Lambda invocations", "Lambda GB-seconds", "Athena data scanned"],
         "Bills only when someone uses it"),
        ("Data transfer", "GB moved, by direction", "s2",
         ["Out to the internet", "Across AZs", "To another Region", "In from internet: $0"],
         "Bills for where data goes"),
    ]
    cw, gap, top = 166, 10, 70
    for i, (name, unit, cls, items, foot) in enumerate(cols):
        x = 16 + i * (cw + gap)
        body.append(f'<rect class="panel" x="{x}" y="{top}" width="{cw}" height="300" rx="8"/>')
        body.append(f'<rect class="{cls}" x="{x}" y="{top}" width="{cw}" height="6" rx="2"/>')
        body.append(f'<text class="head" x="{x + 12}" y="{top + 32}">{name}</text>')
        text_lines(body, x + 12, top + 52, wrap(unit, 24), cls="small", dy=15)
        y = top + 100
        for it in items:
            body.append(f'<rect class="box" x="{x + 10}" y="{y - 16}" width="{cw - 20}" height="26" rx="4"/>')
            body.append(f'<text class="lab" x="{x + 18}" y="{y + 2}" style="font-size:12px">{it}</text>')
            y += 34
        text_lines(body, x + 12, top + 268, wrap(foot, 20), cls="cellt", dy=15)
    body.append(f'<text class="note" x="16" y="{h - 34}">Bar colors only group the columns; each column is named.</text>')
    body.append(f'<text class="note" x="16" y="{h - 16}">Our summary of the EC2, S3, Lambda and data transfer pricing pages, checked 2026-10-24.</text>')
    svg("11-01-four-meters.svg", w, h,
        "The four meters behind most AWS charges, with the bakery's resources on each",
        "Four columns. Time, the hours or seconds a resource exists or runs: EC2 web servers, the load balancer, "
        "a NAT gateway, the RDS database, public IPv4 addresses; it bills while the resource exists, busy or idle. "
        "Storage, GB kept per month: the S3 photo bucket, EBS disks billed by the size you set, RDS storage and "
        "backups, snapshots; it bills for what you keep until you delete it. Requests, calls and runs by the count: "
        "S3 GET and PUT requests, Lambda invocations and GB-seconds, Athena data scanned; it bills only when someone "
        "uses it. Data transfer, GB moved by direction: out to the internet, across Availability Zones, to another "
        "Region, while data in from the internet is free; it bills for where data goes.", body, style=STYLE)


def waterfall():
    """From November's bill to December's: which lines grew."""
    rows, nov, dec = bill()
    d = {r[0]: (r[2], r[3]) for r in rows}
    nat = d["NAT gateway hours (new in December)"][1] + d["Data processed by the NAT gateway"][1]
    out = d["Data out to the internet"][1] - d["Data out to the internet"][0]
    srv = d["Web servers (t3.small hours)"][1] - d["Web servers (t3.small hours)"][0]
    xaz = d["Web server to database, across AZs"][1] - d["Web server to database, across AZs"][0]
    other = round(dec - nov - nat - out - srv - xaz, 2)
    steps = [("November total", nov, "total"),
             ("+ NAT gateway (new): hours and data", nat, "up-new"),
             ("+ Data out to the internet", out, "up"),
             ("+ More web server hours", srv, "up"),
             ("+ Web server to database across AZs", xaz, "up"),
             ("+ Disks, photo storage, requests", other, "up"),
             ("December total", dec, "total")]
    w, left, top, pw, rowh, xmax = 720, 270, 92, 400, 40, 220
    h = top + rowh * len(steps) + 64
    sx = lambda v: pw * v / xmax
    body = [
        '<text class="title" x="16" y="28">The bill nearly tripled. Which lines grew?</text>',
        '<text class="sub" x="16" y="48">The bakery\'s November and December, without the database, US East (N. Virginia) prices as of 2026-10-24</text>',
    ]
    swatch(body, 16, 76, "s1", "Month total")
    swatch(body, 130, 76, "s4", "Grew with customers")
    swatch(body, 300, 76, "s2", "New resource, not customers")
    for v in range(0, xmax + 1, 50):
        x = left + sx(v)
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 4}" y2="{top + rowh * len(steps)}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top + rowh * len(steps) + 18}" text-anchor="middle">${v}</text>')
    run = 0.0
    for i, (label, v, kind) in enumerate(steps):
        y = top + i * rowh + 9
        body.append(f'<text class="lab" x="16" y="{y + 15}">{label}</text>')
        if kind == "total":
            body.append(f'<path class="s1" d="{right_rounded(left, y, sx(v), 22)}"><title>{label}: ${v:,.2f}</title></path>')
            body.append(f'<text class="val" x="{left + sx(v) + 8:.1f}" y="{y + 16}">${v:,.2f}</text>')
            run = v
        else:
            cls = "s2" if kind == "up-new" else "s4"
            body.append(f'<rect class="{cls}" x="{left + sx(run):.1f}" y="{y}" width="{max(sx(v), 2):.1f}" height="22" rx="3"><title>{label}: +${v:,.2f}</title></rect>')
            body.append(f'<line class="conn" x1="{left + sx(run):.1f}" x2="{left + sx(run):.1f}" y1="{y - 18}" y2="{y}"/>')
            body.append(f'<text class="val" x="{left + sx(run + v) + 8:.1f}" y="{y + 16}">+${v:,.2f}</text>')
            run += v
    body.append(f'<text class="note" x="16" y="{h - 26}">Quantities are made up for teaching. Prices from AWS\'s published price lists (data transfer published 2026-09-16).</text>')
    body.append(f'<text class="note" x="16" y="{h - 10}">Lambda stayed inside its monthly free allowance in both months, so it adds $0.00.</text>')
    desc = "; ".join(f"{lab} {'$' if k == 'total' else 'plus $'}{v:,.2f}" for lab, v, k in steps)
    svg("11-01-bill-waterfall.svg", w, h,
        "How the bakery's bill grew from November to December, line by line",
        "Waterfall chart, in US dollars, without the order database. " + desc.replace("+ ", "") +
        ". The NAT gateway is a new resource, not caused by customers; the other increases grew with customers.",
        body, style=STYLE)
    return steps


def arrow(body, x1, y1, x2, y2, cls):
    """A straight arrow with a triangular head at (x2, y2)."""
    import math
    body.append(f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 10 * math.cos(a - 0.4), y2 - 10 * math.sin(a - 0.4))
    p2 = (x2 - 10 * math.cos(a + 0.4), y2 - 10 * math.sin(a + 0.4))
    head = "ahead-free" if cls == "free" else "ahead-paid"
    body.append(f'<path class="{head}" d="M{x2},{y2} L{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z"/>')


def transfer_map():
    """Where the bakery's data moves, each arrow labeled free or with its rate."""
    w, h = 720, 520
    body = [
        '<text class="title" x="16" y="28">Data transfer is priced by where the data goes</text>',
        '<text class="sub" x="16" y="48">Rates from US East (N. Virginia), per GB, from AWS\'s price list published 2026-09-16</text>',
    ]
    line_y = 72
    body.append(f'<line class="free" x1="16" y1="{line_y}" x2="40" y2="{line_y}"/>')
    body.append(f'<text x="46" y="{line_y + 4}">Free: solid green, labeled "free"</text>')
    body.append(f'<line class="paid" x1="300" y1="{line_y}" x2="324" y2="{line_y}"/>')
    body.append(f'<text x="330" y="{line_y + 4}">Charged: dashed orange, labeled with the rate</text>')
    # Internet
    body.append('<rect class="box" x="16" y="210" width="130" height="80" rx="40"/>')
    body.append('<text class="head" x="81" y="245" text-anchor="middle">Internet</text>')
    body.append('<text class="small" x="81" y="263" text-anchor="middle">customers</text>')
    # Region N. Virginia
    body.append('<rect class="zone" x="230" y="100" width="300" height="340" rx="10"/>')
    body.append('<text class="cellt" x="244" y="122">Region: US East (N. Virginia)</text>')
    body.append('<rect class="panel" x="246" y="140" width="130" height="150" rx="8"/>')
    body.append('<text class="small" x="258" y="160">Availability Zone a</text>')
    body.append('<rect class="hi" x="262" y="172" width="98" height="40" rx="6"/>')
    body.append('<text class="cellt" x="311" y="197" text-anchor="middle">Web server</text>')
    body.append('<rect class="hi" x="262" y="232" width="98" height="40" rx="6"/>')
    body.append('<text class="cellt" x="311" y="250" text-anchor="middle">Another</text>')
    body.append('<text class="cellt" x="311" y="265" text-anchor="middle">instance</text>')
    body.append('<rect class="panel" x="390" y="140" width="126" height="150" rx="8"/>')
    body.append('<text class="small" x="402" y="160">Availability Zone b</text>')
    body.append('<rect class="hi" x="404" y="172" width="98" height="40" rx="6"/>')
    body.append('<text class="cellt" x="453" y="197" text-anchor="middle">Database</text>')
    body.append('<rect class="hi" x="300" y="360" width="160" height="44" rx="6"/>')
    body.append('<text class="cellt" x="380" y="381" text-anchor="middle">S3 photo bucket</text>')
    body.append('<text class="small" x="380" y="397" text-anchor="middle">a Regional service</text>')
    # Ohio and CloudFront
    body.append('<rect class="zone" x="590" y="140" width="114" height="90" rx="10"/>')
    body.append('<text class="cellt" x="647" y="174" text-anchor="middle">Another</text>')
    body.append('<text class="cellt" x="647" y="190" text-anchor="middle">Region</text>')
    body.append('<text class="small" x="647" y="208" text-anchor="middle">backup copies</text>')
    body.append('<rect class="box" x="590" y="330" width="114" height="70" rx="8"/>')
    body.append('<text class="cellt" x="647" y="360" text-anchor="middle">CloudFront</text>')
    body.append('<text class="small" x="647" y="378" text-anchor="middle">edge locations</text>')
    # Arrows
    arrow(body, 146, 228, 258, 190, "free")
    body.append('<text class="arrlab" x="150" y="196">1. In: free</text>')
    arrow(body, 258, 200, 150, 266, "paid")
    body.append('<text class="arrlab" x="60" y="316">2. Out: $0.09</text>')
    body.append('<text class="small" x="60" y="332">after 100 GB free a month</text>')
    arrow(body, 311, 214, 311, 230, "free")
    body.append('<text class="arrlab" x="250" y="306">3. Same AZ: free</text>')
    arrow(body, 362, 186, 402, 186, "paid")
    body.append('<text class="arrlab" x="402" y="312">4. Across AZs: $0.01</text>')
    body.append('<text class="small" x="402" y="328">charged in each direction</text>')
    arrow(body, 355, 274, 420, 358, "free")
    body.append('<text class="arrlab" x="244" y="346">5. EC2 to S3: free</text>')
    arrow(body, 504, 190, 588, 186, "paid")
    body.append('<text class="arrlab" x="540" y="250">6. To another Region:</text>')
    body.append('<text class="small" x="540" y="266">$0.02 most; $0.01 to Ohio</text>')
    arrow(body, 460, 382, 588, 366, "free")
    body.append('<text class="arrlab" x="474" y="420">7. S3 to CloudFront: free</text>')
    # mark charged arrows dashed
    body[:] = [b.replace('class="paid"', 'class="paid" style="stroke-dasharray:7 4"') if b.startswith("<line") else b for b in body]
    body.append(f'<text class="note" x="16" y="{h - 30}">Services in the path add their own fees, such as a NAT gateway\'s $0.045 per GB processed.</text>')
    body.append(f'<text class="note" x="16" y="{h - 14}">Rates differ by Region; outbound rates fall as volume grows. Sources: AWS price list; EC2 and S3 pricing pages.</text>')
    svg("11-01-transfer-map.svg", w, h,
        "Where the bakery's data moves, and which moves are free",
        "A map of the bakery's setup with seven numbered arrows. 1, data in from the internet to the web server: "
        "free. 2, data out from the web server to the internet: $0.09 per GB after 100 GB free a month. 3, between "
        "the web server and another instance in the same Availability Zone, over private addresses: free. 4, from the web "
        "server in Availability Zone a to the database in Availability Zone b: $0.01 per GB, charged in each "
        "direction. 5, from EC2 to the S3 photo bucket in the same Region: free. 6, from US East (N. Virginia) to "
        "another Region for backup copies: $0.02 per GB to most Regions, $0.01 to US East (Ohio). 7, from S3 to "
        "CloudFront edge locations: free. Free arrows are solid green; charged ones dashed orange. Rates from "
        "AWS's price list published 2026-09-16.", body, style=STYLE)


def two_clocks():
    """The Free plan's two clocks (calendar and credits), the Paid plan and Always Free."""
    w, h = 720, 470
    left, right, top = 200, 690, 92
    pw = right - left
    sx = lambda m: left + pw * m / 12
    body = [
        '<text class="title" x="16" y="28">The Free Tier now: two plans, and the Free plan\'s two clocks</text>',
        '<text class="sub" x="16" y="48">A new account, months after sign-up. Terms as of 2026-10-24; check the AWS Free Tier page.</text>',
    ]
    for m in range(0, 13, 1):
        x = sx(m)
        body.append(f'<line class="{"axis" if m in (0, 12) else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 6}" y2="{top + 250}"/>')
        if m % 3 == 0:
            body.append(f'<text class="tick" x="{x:.1f}" y="{top + 268}" text-anchor="middle">{m}</text>')
    body.append(f'<text class="tick" x="{sx(6):.1f}" y="{top + 286}" text-anchor="middle">months after sign-up</text>')
    rows = [
        ("Free plan", 0, 6, "s1", "Calendar clock: 6 months, or less if the credits run out; then it closes"),
        ("Credits: $100,", 0, 6, "s3", "Balance clock: up to $200 over 6 months (AWS Free Tier page)"),
        ("Paid plan", 0, 12, "s2", "Never closes for lack of credits; usage beyond credits is billed"),
        ("Always Free", 0, 12, "s4", "Monthly allowances on both plans, with no end date"),
    ]
    sub = {"Credits: $100,": "plus up to $100 more"}
    for i, (name, a, b, cls, note) in enumerate(rows):
        y = top + 8 + i * 60
        body.append(f'<text class="cellt" x="16" y="{y + 15}">{name}</text>')
        if name in sub:
            body.append(f'<text class="small" x="16" y="{y + 31}">{sub[name]}</text>')
        body.append(f'<path class="{cls}" d="{right_rounded(sx(a), y, sx(b) - sx(a), 20)}"><title>{name}: {note}</title></path>')
        if name in sub:
            # leftover credits after an upgrade: expiry disputed, so drawn dashed and unfilled
            body.append(f'<rect class="dashext" x="{sx(6) + 2:.1f}" y="{y + 1}" width="{sx(12) - sx(6) - 3:.1f}" height="18" rx="3">'
                        '<title>After an upgrade, leftover credits apply to later bills until they expire: '
                        'AWS pages say 6 or 12 months after sign-up</title></rect>')
            body.append(f'<text class="small" x="{sx(9):.1f}" y="{y + 14}" text-anchor="middle">after an upgrade: 6 or 12?</text>')
        text_lines(body, sx(a), y + 38, [note], cls="small")
    body.append(f'<text class="note" x="16" y="{h - 62}">After the Free plan closes the account, AWS keeps your content for 90 days; upgrading within that time restores access,</text>')
    body.append(f'<text class="note" x="16" y="{h - 46}">and leftover credits apply to later bills. When they expire, AWS pages disagree: two FAQ answers say 6 months, two FAQ</text>')
    body.append(f'<text class="note" x="16" y="{h - 30}">answers and the Free Tier terms say 12; our own account\'s Credits page showed 12. Check your own Credits page.</text>')
    body.append(f'<text class="note" x="16" y="{h - 14}">Sources: AWS Free Tier page, FAQ and terms; Billing User Guide, "Choosing a plan"; our own Free plan account, 2026-10-23.</text>')
    svg("11-01-two-clocks.svg", w, h,
        "The Free plan's two clocks, the calendar and the credits, beside the Paid plan and Always Free offers",
        "Timeline from 0 to 12 months after sign-up, as of 2026-10-24. Free plan: a bar from 0 to 6 months; it "
        "ends at 6 months or sooner if the credits run out, and then the account closes. Credits, $100 plus up to "
        "$100 more: a solid bar from 0 to 6 months, up to $200 over 6 months on the Free plan, as AWS's Free Tier page "
        "says; then a dashed, unfilled bar from 6 to 12 months for leftover credits after an upgrade, whose expiry AWS "
        "pages give as 6 or 12 months after sign-up. Paid plan: a bar across all 12 months and beyond; it never closes "
        "for lack of credits, and usage beyond credits is billed. Always Free: monthly allowances on both plans with no "
        "end date. After the Free plan closes the account, AWS keeps content for 90 days; upgrading in that time "
        "restores access and leftover credits apply to later bills.",
        body, style=STYLE)


if __name__ == "__main__":
    four_meters()
    steps = waterfall()
    transfer_map()
    two_clocks()
    rows, nov, dec = bill()
    for r in rows:
        print(f"{r[0]:<42} {r[1]:<14} {r[2]:>8.2f} {r[3]:>8.2f}")
    print("totals", nov, dec)
    for s in steps:
        print(s)
