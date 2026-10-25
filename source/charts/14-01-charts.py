#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for lesson 14.01 (the capstone review) as SVG.

Usage: python3 -I source/charts/14-01-charts.py
Writes images/14-01-*.svg.

Rates are US East (N. Virginia), On-Demand unless stated, from AWS's Price List offer files
retrieved 2026-10-24 (AmazonEC2 published 2026-10-23; AmazonVPC, AWSELB retrieved 2026-10-24;
AmazonS3 published 2026-10-15; AmazonS3GlacierDeepArchive published 2026-09-11), and from
AWS's DynamoDB pricing page (on-demand requests checked 2026-10-23; point-in-time recovery
$0.20 per GB-month, from the page's US East example, checked 2026-10-24):
  t3.micro $0.0104/h; t4g.micro 1-year Standard RI, No Upfront, $0.0053/h effective;
  public IPv4 address $0.005/h; EBS gp3 $0.08 per GB-month; Application Load Balancer
  $0.0225/h plus $0.008 per LCU-hour; S3 Standard $0.023, Standard-IA $0.0125, Glacier Deep
  Archive $0.00099 per GB-month; S3 GET $0.0004 and PUT $0.005 per 1,000; DynamoDB on-demand
  $0.625 per million writes and $0.125 per million reads.
Quantities (GB stored, requests, LCUs) are made up for teaching. Months are 730 hours.
Cited in the lesson to the EC2, VPC, ELB, S3 and DynamoDB pricing pages.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, swatch, right_rounded  # noqa: E402

H = 730
R = {"t3": 0.0104, "t4g_ri": 0.0053, "ipv4": 0.005, "gp3": 0.08, "alb": 0.0225, "lcu": 0.008,
     "std": 0.023, "ia": 0.0125, "gda": 0.00099, "get": 0.0004 / 1000, "put": 0.005 / 1000,
     "ddb_w": 0.625 / 1e6, "ddb_r": 0.125 / 1e6, "pitr": 0.20}

# Each bill line is rounded to the cent before it is added, as a bill shows it, so the totals
# in the charts and in the lesson's table add up from the parts.
c = lambda v: round(v, 2)
SERVER = c(R["t3"] * H) + c(R["ipv4"] * H) + c(8 * R["gp3"])      # one web server: instance, address, 8 GiB disk
STORAGE = c(50 * R["std"] + 1 * R["std"] + 2 * R["ia"] + 1 * R["gda"]  # photos, exports, archive
            + 200_000 * R["get"] + 2_000 * R["put"]                     # S3 requests
            + 20_000 * R["ddb_w"] + 100_000 * R["ddb_r"])               # cart table requests
LB = c(R["alb"] * H) + c(2 * R["ipv4"] * H) + c(0.2 * R["lcu"] * H)  # hours, two public addresses, 0.2 LCU average
NEW_DATA = c(6 * R["std"]) + c(1 * R["pitr"] + 2 * R["std"])       # trail logs after a year; PITR and old photo versions
SUPPORT = max(29.0, 0.09 * (2 * SERVER + LB + STORAGE + NEW_DATA))
LATER_SAVING = 2 * (c(R["t3"] * H) - c(R["t4g_ri"] * H))          # two t3.micro On-Demand -> two t4g.micro RIs

assert c(SERVER) == 11.88 and c(STORAGE) == 1.31 and c(LB) == 24.90 and c(NEW_DATA) == 0.39
assert c(SERVER + STORAGE) == 13.19
assert c(2 * SERVER + LB + STORAGE + NEW_DATA) == 50.36 and SUPPORT == 29.0
assert c(LATER_SAVING) == 7.44 and c(2 * SERVER - LATER_SAVING) == 16.32

STYLE = make_style(
    light_extra=" --s3:#1baf7a; --sup:#898781;",
    dark_extra=" --s3:#199e70; --sup:#898781;",
    rules_extra="""
  .s3 { fill: var(--s3); } .sup { fill: var(--sup); }
  .gap { stroke: var(--surface); stroke-width: 2; }
  .val { fill: var(--ink); font-size: 13px; font-variant-numeric: tabular-nums; }
  .valb { fill: var(--ink); font-size: 14px; font-weight: 600; font-variant-numeric: tabular-nums; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .pick { fill: none; stroke: var(--ink); stroke-width: 2; }""")


def bars(name, title, sub, rows, legend, xmax, step, note, alt_title, desc, pick=None, label_w=214):
    """Stacked horizontal bars. rows: (label, sublabel, [(cls, name, value)])."""
    w, top, bw, gap = 680, 104, 34, 30
    left, pw = label_w, 680 - label_w - 110
    body = [f'<text class="title" x="16" y="28">{title}</text>', f'<text class="sub" x="16" y="48">{sub}</text>']
    x = 16
    for cls, lab in legend:
        swatch(body, x, 80, cls, lab)
        x += 26 + 7.2 * len(lab)
    xv = lambda v: left + pw * v / xmax
    n = len(rows)
    bottom = top + n * (bw + gap) - gap
    v = 0
    while v <= xmax + 1e-9:
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{xv(v):.1f}" x2="{xv(v):.1f}" y1="{top - 6}" y2="{bottom + 6}"/>')
        body.append(f'<text class="tick" x="{xv(v):.1f}" y="{bottom + 22}" text-anchor="middle">${v:,.0f}</text>')
        v += step
    body.append(f'<text class="tick" x="{left + pw / 2:.1f}" y="{bottom + 40}" text-anchor="middle">USD per month</text>')
    for i, (lab, sublab, segs) in enumerate(rows):
        y = top + i * (bw + gap)
        body.append(f'<text class="lab" x="{left - 10}" y="{y + 14}" text-anchor="end">{lab}</text>')
        body.append(f'<text class="small" x="{left - 10}" y="{y + 30}" text-anchor="end">{sublab}</text>')
        acc = 0.0
        segs = [s for s in segs if s[2] > 0]
        for j, (cls, sname, val) in enumerate(segs):
            x0, x1 = xv(acc), xv(acc + val)
            tip = f"<title>{lab}: {sname} ${val:,.2f}</title>"
            if j == len(segs) - 1:
                body.append(f'<path class="{cls} gap" d="{right_rounded(x0, y, x1 - x0, bw)}">{tip}</path>')
            else:
                body.append(f'<rect class="{cls} gap" x="{x0:.1f}" y="{y}" width="{x1 - x0:.1f}" height="{bw}">{tip}</rect>')
            acc += val
        if pick == i:
            body.append(f'<path class="pick" d="{right_rounded(left - 3, y - 3, xv(acc) - left + 6, bw + 6)}"/>')
        body.append(f'<text class="{"valb" if pick == i else "val"}" x="{xv(acc) + 10:.1f}" y="{y + bw / 2 + 5:.1f}">${acc:,.2f}</text>')
    h = bottom + 74
    for k, line in enumerate(note):
        body.append(f'<text class="note" x="16" y="{h - 22 + 15 * k}">{line}</text>')
    svg(name, w, h + 8, alt_title, desc, body, style=STYLE)


def web_tier_options():
    rows = [
        ("A. Leave it as built", "one server in us-east-1a", [("s1", "web server", SERVER)]),
        ("B. Self-healing single server", "Auto Scaling group of one", [("s1", "web server", SERVER)]),
        ("C. Two servers, two AZs", "behind a load balancer", [("s1", "web servers", 2 * SERVER), ("s2", "load balancer", LB)]),
    ]
    bars("14-01-web-tier-options.svg",
         "The web tier: three ways to answer REL 10, per month",
         "On-Demand, US East (N. Virginia), price lists retrieved 2026-10-24; 730 hours",
         rows, [("s1", "Web servers: instance, public IPv4, 8 GiB disk"), ("s2", "Load balancer: hours, 2 IPv4, LCUs")],
         50, 10,
         ["A: an AZ or server failure takes the site down until someone rebuilds it. B: down for minutes per failure, and the",
          "new server has a new public address. C: the site stays up through either. Capacity units assume 0.2 LCU on average."],
         "Monthly cost of three designs for the bakery's web tier",
         f"Horizontal bars, dollars per month, On-Demand, US East (N. Virginia), price lists retrieved 2026-10-24. "
         f"A, leave it as built, one t3.micro web server in us-east-1a with its public IPv4 address and 8 GiB gp3 disk: ${SERVER:.2f}. "
         f"B, the same server in an Auto Scaling group of one, which costs nothing extra: ${SERVER:.2f}. "
         f"C, outlined as the choice: two such servers in two Availability Zones, ${2 * SERVER:.2f}, behind an Application "
         f"Load Balancer, ${LB:.2f} for its hours, two public IPv4 addresses and an assumed 0.2 capacity units on average, "
         f"${2 * SERVER + LB:.2f} in all. A note says what a failure does to each: A is down until rebuilt by hand, "
         f"B is down for minutes and gets a new public address, C stays up.",
         pick=2)


def bill_before_after():
    after = [("s1", "web servers", 2 * SERVER), ("s2", "load balancer", LB), ("s3", "storage, requests, backups", STORAGE + NEW_DATA)]
    rows = [
        ("As built", "one server, no load balancer", [("s1", "web server", SERVER), ("s3", "storage, requests, backups", STORAGE)]),
        ("With the fixes", "all eight in the write-up", after),
        ("Plus Business Support+", "its $29 monthly minimum", after + [("sup", "Business Support+", SUPPORT)]),
        ("Later: Graviton, 1-year RIs", "after a month of data", [("s1", "web servers", 2 * SERVER - LATER_SAVING)] + after[1:]
         + [("sup", "Business Support+", SUPPORT)]),
    ]
    bars("14-01-bill-before-after.svg",
         "The bakery's monthly bill before and after the review",
         "US East (N. Virginia), price lists retrieved 2026-10-24; usage made up for teaching",
         rows, [("s1", "Web servers"), ("s2", "Load balancer"), ("s3", "Storage, requests, backups"), ("sup", "Support plan")],
         80, 20,
         ["Lambda, CloudWatch, SNS email and data out stay inside their free allowances; VPC parts are free.",
          "Later: two t4g.micro on 1-year Standard RIs, No Upfront, instead of two t3.micro On-Demand."],
         "The bakery's monthly AWS bill as built, with the review's fixes, with Business Support+, and after later savings",
         f"Stacked horizontal bars, dollars per month, US East (N. Virginia), price lists retrieved 2026-10-24, usage made up. "
         f"As built: web server ${SERVER:.2f} plus storage, requests and backups ${STORAGE:.2f}, ${SERVER + STORAGE:.2f}. "
         f"With the fixes: web servers ${2 * SERVER:.2f}, load balancer ${LB:.2f}, storage, requests and backups "
         f"${STORAGE + NEW_DATA:.2f}, ${2 * SERVER + LB + STORAGE + NEW_DATA:.2f}. Plus Business Support+ at its $29 minimum: "
         f"${2 * SERVER + LB + STORAGE + NEW_DATA + SUPPORT:.2f}. Later, with two t4g.micro instances on 1-year Reserved "
         f"Instances: web servers ${2 * SERVER - LATER_SAVING:.2f}, total "
         f"${2 * SERVER + LB + STORAGE + NEW_DATA + SUPPORT - LATER_SAVING:.2f}.")


if __name__ == "__main__":
    web_tier_options()
    bill_before_after()
