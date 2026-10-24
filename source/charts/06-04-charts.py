#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 06.04 (simpler paths) as SVG.

Usage: python3 -I source/charts/06-04-charts.py
Writes images/06-04-*.svg.
- Four paths: "What is AWS Elastic Beanstalk?" and its FAQ, the Amazon Lightsail
  FAQ and pricing page, "What is AWS Batch?" and its FAQ, "What is AWS Outposts?"
  and the Outposts racks FAQ. All retrieved 2026-10-23.
- Lightsail vs EC2: the Lightsail pricing page, retrieved 2026-10-23 (Linux/Unix
  bundle with a public IPv4 address: $12 a month for 2 GB memory, 2 vCPUs, 60 GB
  SSD and 3 TB transfer). EC2 prices from the AWS Price List offer files for US
  East (N. Virginia), retrieved 2026-10-24 (research repo
  sources/raw/pricing/compute-networking-us-east-1-summary.tsv): t3.small
  on-demand $0.0208 per hour, gp3 storage $0.08 per GB-month, public IPv4
  address $0.005 per hour. 730 hours a month.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --card-fill:#f1f0ec;",
    dark_extra=" --card-fill:#252523;",
    rules_extra="""
  .card { fill: var(--card-fill); stroke: var(--axis); stroke-width: 1; }
  .cellt { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .head { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .ann { fill: var(--ink); font-size: 12px; }
  .vlab { fill: var(--ink); font-size: 12px; font-variant-numeric: tabular-nums; }
  .seg-gap { stroke: var(--surface); stroke-width: 2; }
  .bundle { fill: var(--muted); }""")

CARDS = [
    ("AWS Elastic Beanstalk", [
        ("You bring", "your web application's code"),
        ("AWS sets up", "EC2 instances or an EKS cluster, load balancing, scaling and health monitoring, in your account"),
        ("You pay", "nothing extra; only the resources it creates"),
        ("Pick it when", "you want to deploy code without building the setup by hand"),
    ]),
    ("Amazon Lightsail", [
        ("You bring", "a website or small app, often from a ready-made image such as WordPress"),
        ("AWS sets up", "a virtual server with storage, a static IP and data transfer, as one bundle"),
        ("You pay", "a fixed monthly plan price, charged by the hour up to that maximum"),
        ("Pick it when", "you want something simple with a predictable bill"),
    ]),
    ("AWS Batch", [
        ("You bring", "many jobs, each packaged as a container"),
        ("AWS sets up", "a queue, and compute that grows for the jobs and is removed when they finish"),
        ("You pay", "nothing extra; only the EC2 or Fargate capacity the jobs use"),
        ("Pick it when", "you have lots of jobs to run, often too long for Lambda"),
    ]),
    ("AWS Outposts", [
        ("You bring", "a site with space, power and a network connection to an AWS Region"),
        ("AWS sets up", "racks or servers of AWS hardware that AWS monitors, patches and maintains"),
        ("You pay", "for a term of years, by configuration"),
        ("Pick it when", "work or data must stay in your own building"),
    ]),
]


def four_paths():
    w = 680
    cw, gap = 326, 12
    body = [
        '<text class="title" x="16" y="28">Four simpler paths, and what each one hands to AWS</text>',
        '<text class="sub" x="16" y="48">From each service\'s documentation and FAQ, checked 2026-10-23</text>',
    ]
    # measure card heights per row
    def card_h(rows):
        h = 44
        for _, val in rows:
            h += 16 + 15 * len(wrap(val, 46)) + 6
        return h + 6
    hs = [card_h(r) for _, r in CARDS]
    rowh = [max(hs[0], hs[1]), max(hs[2], hs[3])]
    y0 = 64
    for i, (name, rows) in enumerate(CARDS):
        x = 16 + (i % 2) * (cw + gap)
        y = y0 + (0 if i < 2 else rowh[0] + 12)
        body.append(f'<rect class="card" x="{x}" y="{y}" width="{cw}" height="{rowh[i // 2]}" rx="8"/>')
        body.append(f'<text class="cellt" x="{x + 14}" y="{y + 24}">{name}</text>')
        body.append(f'<line class="axis" x1="{x}" x2="{x + cw}" y1="{y + 36}" y2="{y + 36}"/>')
        yy = y + 56
        for lab, val in rows:
            body.append(f'<text class="head" x="{x + 14}" y="{yy}">{lab}</text>')
            yy = text_lines(body, x + 14, yy + 16, wrap(val, 46), cls="small", dy=15) + 6
    y = y0 + rowh[0] + 12 + rowh[1] + 20
    body.append(f'<text class="note" x="16" y="{y}">Beanstalk, Batch and Lightsail all run on AWS servers that still exist; you just don\'t assemble them yourself.</text>')
    svg("06-04-four-paths.svg", w, y + 14,
        "Four simpler compute paths: Elastic Beanstalk, Lightsail, Batch and Outposts",
        "Four cards in two rows. AWS Elastic Beanstalk: you bring your web application's code; AWS sets up EC2 "
        "instances or an EKS cluster, load balancing, scaling and health monitoring, in your account; you pay nothing "
        "extra, only for the resources it creates; pick it when you want to deploy code without building the setup by "
        "hand. Amazon Lightsail: you bring a website or small app, often from a ready-made image such as WordPress; AWS "
        "sets up a virtual server with storage, a static IP and data transfer as one bundle; you pay a fixed monthly "
        "plan price, charged by the hour up to that maximum; pick it when you want something simple with a predictable "
        "bill. AWS Batch: you bring many jobs, each packaged as a container; AWS sets up a queue and compute that grows "
        "for the jobs and is removed when they finish; you pay nothing extra, only for the EC2 or Fargate capacity the "
        "jobs use; pick it when you have lots of jobs to run, often too long for Lambda. AWS Outposts: you bring a site "
        "with space, power and a network connection to an AWS Region; AWS sets up racks or servers of AWS hardware that "
        "it monitors, patches and maintains; you pay for a term of years, by configuration; pick it when work or data "
        "must stay in your own building. A note says Beanstalk, Batch and Lightsail run on AWS servers that still "
        "exist; you just don't assemble them yourself.", body, style=STYLE)


HOURS = 730
EC2_PARTS = [  # label, monthly dollars, class
    ("t3.small instance, 730 hours", 0.0208 * HOURS, "s1"),
    ("60 GB gp3 disk", 60 * 0.08, "s1l"),
    ("Public IPv4 address", 0.005 * HOURS, "s2"),
]
LIGHTSAIL = 12.0


def lightsail_vs_ec2():
    w = 680
    left, top, pw = 150, 92, 470
    bh, gapb = 40, 34
    xmax = 25
    ec2_total = sum(v for _, v, _ in EC2_PARTS)
    assert abs(ec2_total - 23.63) < 0.01
    body = [
        '<text class="title" x="16" y="28">A small, steady web server for a month: a bundle or the parts</text>',
        '<text class="sub" x="16" y="48">Amazon Lightsail\'s $12 plan against similar pieces on Amazon EC2, US East (N. Virginia)</text>',
    ]

    def X(v):
        return left + pw * v / xmax

    for v in range(0, xmax + 1, 5):
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{top - 6}" y2="{top + 2 * bh + gapb + 6}"/>')
        body.append(f'<text class="tick" x="{X(v):.1f}" y="{top + 2 * bh + gapb + 22}" text-anchor="middle">${v}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2}" y="{top + 2 * bh + gapb + 40}" text-anchor="middle">Dollars per month</text>')
    # Lightsail bar
    y = top
    body.append(f'<text class="lab" x="{left - 10}" y="{y + 17}" text-anchor="end">Lightsail plan</text>')
    body.append(f'<text class="tick" x="{left - 10}" y="{y + 33}" text-anchor="end">2 GB, 2 vCPUs</text>')
    body.append(f'<path class="bundle" d="{right_rounded(X(0), y, X(LIGHTSAIL) - X(0), bh)}"><title>Lightsail plan: $12.00 a month</title></path>')
    body.append(f'<text class="vlab" x="{X(LIGHTSAIL) + 8:.1f}" y="{y + 17}">$12.00, one price that includes the server,</text>')
    body.append(f'<text class="vlab" x="{X(LIGHTSAIL) + 8:.1f}" y="{y + 33}">60 GB SSD, a public IPv4 address and 3 TB transfer</text>')
    # EC2 stacked bar
    y = top + bh + gapb
    body.append(f'<text class="lab" x="{left - 10}" y="{y + 17}" text-anchor="end">EC2, priced by part</text>')
    body.append(f'<text class="tick" x="{left - 10}" y="{y + 33}" text-anchor="end">2 GiB, 2 vCPUs</text>')
    x = X(0)
    for i, (lab, v, cls) in enumerate(EC2_PARTS):
        wv = X(v) - X(0)
        if i == len(EC2_PARTS) - 1:
            body.append(f'<path class="{cls}" d="{right_rounded(x, y, wv, bh)}"><title>{lab}: ${v:.2f}</title></path>')
        else:
            body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{wv:.1f}" height="{bh}"><title>{lab}: ${v:.2f}</title></rect>')
        if i:
            body.append(f'<line class="seg-gap" x1="{x:.1f}" x2="{x:.1f}" y1="{y}" y2="{y + bh}"/>')
        x += wv
    body.append(f'<text class="vlab" x="{x + 8:.1f}" y="{y + 25}">${ec2_total:.2f}</text>')
    # segment labels under the EC2 bar
    ly = y + bh + 56
    x = X(0)
    labs = []
    for lab, v, cls in EC2_PARTS:
        labs.append((x, lab, v, cls))
        x += X(v) - X(0)
    lx = 16
    for x0, lab, v, cls in labs:
        body.append(f'<rect class="{cls}" x="{lx}" y="{ly - 10}" width="12" height="12" rx="2"/>')
        body.append(f'<text class="ann" x="{lx + 18}" y="{ly}">{lab}: ${v:.2f}</text>')
        lx += 18 + 7 * len(f"{lab}: ${v:.2f}") + 26
    y = ly + 28
    for line in (
        "Plus, on EC2 only: data transfer out to the internet beyond the free allowance, $0.09 per GB (price list of 2026-09-16).",
        "Lightsail: pricing page, retrieved 2026-10-23. EC2: AWS Price List offer files, retrieved 2026-10-24; t3.small",
        "$0.0208 an hour, gp3 $0.08 per GB-month, public IPv4 $0.005 an hour, for 730 hours. Prices change.",
        "Not the same machine: EC2 offers far more instance types, pricing options and network control.",
    ):
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 15
    svg("06-04-lightsail-vs-ec2.svg", w, y + 4,
        "Monthly cost of a small web server: a $12 Lightsail plan against EC2 priced by part",
        "A horizontal bar chart in dollars per month, from 0 to 25. The Lightsail plan with 2 GB of memory and 2 vCPUs "
        "is one bar at $12.00, with the server, 60 GB of SSD storage, a public IPv4 address and 3 TB of data transfer "
        f"included. EC2 priced by part, for 2 GiB and 2 vCPUs, is a stacked bar totaling ${ec2_total:.2f}: a t3.small "
        f"instance for 730 hours, ${EC2_PARTS[0][1]:.2f}; a 60 GB gp3 disk, ${EC2_PARTS[1][1]:.2f}; a public IPv4 "
        f"address, ${EC2_PARTS[2][1]:.2f}. EC2 adds data transfer out beyond the free allowance at $0.09 per GB. "
        "Lightsail prices retrieved 2026-10-23; EC2 prices as of 2026-10-24.", body, style=STYLE)


if __name__ == "__main__":
    four_paths()
    lightsail_vs_ec2()
