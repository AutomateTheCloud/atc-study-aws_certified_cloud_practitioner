#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 06.01 (Amazon EC2) as SVG.

Usage: python3 -I source/charts/06-01-charts.py
Writes images/06-01-*.svg. Facts, checked 2026-10-24 in the research repo:
- what you choose at launch (AMI, instance type, EBS, key pair, security group): EC2 User
  Guide, "What is Amazon EC2?"; EC2 Instance Connect: EC2 User Guide, "Connect to your Linux
  instance using a public IP address and EC2 Instance Connect";
- the six instance families and their example workloads and letters: docs/04-services/compute.md,
  from the EC2 instance types product page and the Instance Types Guide;
- every price: US East (N. Virginia), Linux, shared tenancy, from the AWS Price List offer files
  retrieved 2026-10-24 (research repo sources/raw/pricing/compute-networking-us-east-1-summary.tsv);
- a stopped instance has no instance-hour charge but its EBS storage is charged, and its
  automatic public IPv4 address is released on stop: Amazon EC2 FAQs; Elastic IP addresses are
  charged whether in use or idle: EC2 User Guide, Elastic IP addresses.
The 8 GB gp3 root volume is an example size of ours. Our own design: no AWS logos, icons,
trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, swatch, text_lines, wrap  # noqa: E402

HOURS_MONTH = 730   # hours in an average month, as AWS's price examples use
HOURS_YEAR = 8760
PRICES = {          # USD per hour, On-Demand, and 1-year Standard No Upfront RI (effective)
    "t3.micro": (0.0104, 0.0065),
    "t3.small": (0.0208, 0.013),
    "m7g.large": (0.0816, 0.054),
    "r7g.large": (0.1071, 0.0708),
}
IPV4 = 0.005        # per public IPv4 address per hour, in use or idle
GP3 = 0.08          # per GB-month
ROOT_GB = 8         # example root volume size

STYLE = make_style(
    light_extra=" --panel:#f1f0ec; --hi-fill:#d9e8fb; --s3:#1baf7a;",
    dark_extra=" --panel:#252523; --hi-fill:#1b3554; --s3:#199e70;",
    rules_extra="""
  .panel { fill: var(--panel); stroke: var(--axis); stroke-width: 1; }
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 1.5; }
  .box { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .zone { fill: none; stroke: var(--muted); stroke-width: 1.2; stroke-dasharray: 5 4; }
  .wire { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .head { fill: var(--ink); font-size: 15px; font-weight: 600; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .big { fill: var(--ink); font-size: 56px; font-weight: 600; font-family: ui-monospace, Menlo, Consolas, monospace; }
  .bighi { fill: var(--s1); font-size: 56px; font-weight: 600; font-family: ui-monospace, Menlo, Consolas, monospace; }
  .mono { fill: var(--ink); font-size: 13px; font-family: ui-monospace, Menlo, Consolas, monospace; }
  .brace { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .s3 { fill: var(--s3); }""")


def launch_choices():
    """Big picture: the five choices that make an instance, and where it lives."""
    w, h = 700, 470
    body = [
        '<text class="title" x="16" y="28">Five choices make an EC2 instance</text>',
        '<text class="sub" x="16" y="48">You make them when you launch. This lesson is mostly about the second one.</text>',
    ]
    cards = [
        ("Amazon Machine Image (AMI)", "The template: an operating system and any software that comes with it", False),
        ("Instance type", "How much hardware: vCPUs, memory, storage and network speed", True),
        ("Storage", "An EBS root volume: the disk it starts from, which lives apart from it", False),
        ("Network and security group", "Which Availability Zone it runs in, and who may connect, on which ports", False),
        ("Access", "How you sign in: a key pair, or EC2 Instance Connect with your IAM identity", False),
    ]
    top, ch, gap, cw = 72, 64, 10, 340
    for i, (name, line, hi) in enumerate(cards):
        y = top + i * (ch + gap)
        body.append(f'<rect class="{"hi" if hi else "panel"}" x="16" y="{y}" width="{cw}" height="{ch}" rx="6"/>')
        body.append(f'<text class="cellt" x="30" y="{y + 22}">{i + 1}. {name}</text>')
        text_lines(body, 30, y + 40, wrap(line, 52), cls="small", dy=15)
        body.append(f'<line class="wire" x1="{16 + cw}" y1="{y + ch / 2}" x2="474" y2="{top + 2.5 * ch + 2 * gap}"/>')
    # Region > AZ > instance
    body.append('<rect class="zone" x="404" y="72" width="280" height="356" rx="10"/>')
    body.append('<text class="small" x="418" y="94">Region: US East (N. Virginia)</text>')
    body.append('<rect class="zone" x="424" y="108" width="240" height="300" rx="8"/>')
    body.append('<text class="small" x="438" y="130">One Availability Zone</text>')
    cy = top + 2.5 * ch + 2 * gap
    body.append(f'<rect class="box" x="474" y="{cy - 46}" width="170" height="92" rx="8" style="stroke-width:2"/>')
    body.append(f'<text class="head" x="559" y="{cy - 12}" text-anchor="middle">EC2 instance</text>')
    body.append(f'<text class="small" x="559" y="{cy + 8}" text-anchor="middle">a virtual server,</text>')
    body.append(f'<text class="small" x="559" y="{cy + 24}" text-anchor="middle">billed while it runs</text>')
    body.append(f'<text class="note" x="16" y="{h - 14}">Our summary of the EC2 User Guide, "What is Amazon EC2?", checked 2026-10-24.</text>')
    svg("06-01-launch-choices.svg", w, h,
        "The five choices that make an EC2 instance",
        "Five numbered cards on the left, each joined by a line to one EC2 instance on the right. "
        "1, Amazon Machine Image (AMI): the template, an operating system and any software that comes with it. "
        "2, Instance type, highlighted: how much hardware, vCPUs, memory, storage and network speed. "
        "3, Storage: an EBS root volume, the disk it starts from, which lives apart from it. "
        "4, Network and security group: which Availability Zone it runs in, and who may connect, on which ports. "
        "5, Access: how you sign in, a key pair or EC2 Instance Connect with your IAM identity. "
        "The instance, a virtual server billed while it runs, sits inside one Availability Zone inside the "
        "US East (N. Virginia) Region.", body, style=STYLE)


def families():
    """The six instance families, each with the resource that runs out first."""
    w = 700
    body = [
        '<text class="title" x="16" y="28">Six instance families, sorted by what runs out first</text>',
        '<text class="sub" x="16" y="48">Find the bottleneck, and the family follows. Letters are the first letter of the type name.</text>',
    ]
    fams = [
        ("General purpose", "Nothing in particular: a balance of CPU, memory and network", "M, T (burstable)",
         "Web servers, code repositories, small and medium databases"),
        ("Compute optimized", "CPU: the processors are busy all the time", "C",
         "Batch processing, media transcoding, dedicated game servers"),
        ("Memory optimized", "Memory: the data must fit in RAM", "R, X, U, z1d",
         "In-memory databases, analytics on large data sets in memory"),
        ("Storage optimized", "Fast reads and writes to local disks", "I, D, H",
         "High-throughput databases, processing and streaming large data sets"),
        ("Accelerated computing", "Work that needs GPUs or other special chips", "P, G, Inf, Trn",
         "Machine learning, graphics, floating-point calculations"),
        ("HPC optimized", "Very large, tightly linked computations", "Hpc",
         "Complex simulations, deep learning, visual effects rendering"),
    ]
    cw, chh, gap, top = 216, 222, 10, 66
    for i, (name, neck, letters, uses) in enumerate(fams):
        x = 16 + (i % 3) * (cw + gap)
        y = top + (i // 3) * (chh + gap)
        body.append(f'<rect class="panel" x="{x}" y="{y}" width="{cw}" height="{chh}" rx="8"/>')
        body.append(f'<text class="head" x="{x + 14}" y="{y + 26}">{name}</text>')
        body.append(f'<text class="note" x="{x + 14}" y="{y + 50}">RUNS OUT FIRST</text>')
        yy = text_lines(body, x + 14, y + 68, wrap(neck, 30), cls="cellt", dy=17)
        body.append(f'<text class="note" x="{x + 14}" y="{yy + 6}">LETTERS</text>')
        body.append(f'<text class="mono" x="{x + 14}" y="{yy + 24}">{letters}</text>')
        body.append(f'<text class="note" x="{x + 14}" y="{yy + 46}">AWS EXAMPLES</text>')
        text_lines(body, x + 14, yy + 64, wrap(uses, 32), cls="small", dy=15)
    y = top + 2 * chh + gap + 24
    body.append(f'<text class="note" x="16" y="{y}">Sources: EC2 instance types page and Instance Types Guide, checked 2026-10-23. Not every letter is shown.</text>')
    svg("06-01-families.svg", w, y + 14,
        "The six EC2 instance families and the bottleneck each one is built for",
        "Six cards in two rows. General purpose: nothing in particular runs out, a balance of CPU, memory and "
        "network; letters M and T (burstable); for web servers, code repositories, small and medium databases. "
        "Compute optimized: CPU runs out first; letter C; for batch processing, media transcoding, dedicated game "
        "servers. Memory optimized: memory runs out first, the data must fit in RAM; letters R, X, U, z1d; for "
        "in-memory databases and analytics on large data sets in memory. Storage optimized: fast reads and writes "
        "to local disks; letters I, D, H; for high-throughput databases and processing and streaming large data "
        "sets. Accelerated computing: work that needs GPUs or other special chips; letters P, G, Inf, Trn; for "
        "machine learning, graphics, floating-point calculations. HPC optimized: very large, tightly linked "
        "computations; letters Hpc; for complex simulations, deep learning, visual effects rendering.",
        body, style=STYLE)


def same_size():
    """Three .large types with 2 vCPUs each: memory differs by family."""
    rows = [("c7g.large", "Compute optimized", 4, 0.0725),
            ("m7g.large", "General purpose", 8, 0.0816),
            ("r7g.large", "Memory optimized", 16, 0.1071)]
    w, left, top, pw, rowh, xmax = 680, 200, 92, 300, 52, 16
    h = top + rowh * len(rows) + 56
    body = [
        '<text class="title" x="16" y="28">Same size, same 2 vCPUs, different memory</text>',
        '<text class="sub" x="16" y="48">Memory of three .large instance types, in GiB, with the On-Demand price per hour</text>',
        '<text class="sub" x="16" y="66">Linux, US East (N. Virginia), as of 2026-10-24</text>',
    ]
    for v in range(0, xmax + 1, 4):
        x = left + pw * v / xmax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 6}" y2="{top + rowh * len(rows)}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top + rowh * len(rows) + 18}" text-anchor="middle">{v}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2}" y="{top + rowh * len(rows) + 36}" text-anchor="middle">Memory (GiB)</text>')
    for i, (name, fam, gib, usd) in enumerate(rows):
        y = top + i * rowh + 10
        body.append(f'<text class="mono" x="16" y="{y + 12}">{name}</text>')
        body.append(f'<text class="small" x="16" y="{y + 28}">{fam}</text>')
        body.append(f'<path class="s1" d="{right_rounded(left, y, pw * gib / xmax, 24)}"><title>{name}: 2 vCPU, {gib} GiB, ${usd} an hour</title></path>')
        body.append(f'<text class="lab" x="{left + pw * gib / xmax + 8:.1f}" y="{y + 17}">{gib} GiB · ${usd:.4f} an hour</text>')
    svg("06-01-same-size.svg", w, h,
        "Memory and price of three .large instance types that each have 2 vCPUs",
        "Horizontal bar chart of memory. c7g.large, compute optimized: 4 GiB, $0.0725 an hour. "
        "m7g.large, general purpose: 8 GiB, $0.0816 an hour. r7g.large, memory optimized: 16 GiB, "
        "$0.1071 an hour. All three have 2 vCPUs. Linux On-Demand prices in US East (N. Virginia) as of 2026-10-24.",
        body, style=STYLE)


def name_decoded():
    """m7g.large, part by part."""
    w, h = 680, 300
    body = [
        '<text class="title" x="16" y="28">Reading an instance type name</text>',
        '<text class="sub" x="16" y="48">Before the dot: the family, made of series, generation and options. After the dot: the size.</text>',
    ]
    cw = 34  # width of one monospace character at 56px, approximately
    x0, y0 = 150, 132
    parts = [("m", 0, 1, "Series", "m: general purpose"),
             ("7", 1, 1, "Generation", "7th; a higher number is newer"),
             ("g", 2, 1, "Option", "extra letters; here an AWS Graviton (Arm) processor"),
             ("large", 4, 5, "Size", "how much of the family's hardware")]
    body.append(f'<text class="big" x="{x0 + 3 * cw + cw / 2:.1f}" y="{y0}" text-anchor="middle" style="fill:var(--muted)">.</text>')
    label_x = [40, 180, 330, 500]
    for (txt, start, n, title, line), lx in zip(parts, label_x):
        xa, xb = x0 + start * cw + 3, x0 + (start + n) * cw - 3
        xm = (xa + xb) / 2
        body.append(f'<text class="big" x="{xm:.1f}" y="{y0}" text-anchor="middle" textLength="{n * cw - 4}">{txt}</text>')
        body.append(f'<path class="brace" d="M{xa:.1f},{y0 + 14} L{xa:.1f},{y0 + 22} L{xb:.1f},{y0 + 22} L{xb:.1f},{y0 + 14}"/>')
        body.append(f'<line class="brace" x1="{xm:.1f}" y1="{y0 + 22}" x2="{lx + 60:.1f}" y2="{y0 + 58}"/>')
        body.append(f'<text class="cellt" x="{lx}" y="{y0 + 76}">{title}</text>')
        text_lines(body, lx, y0 + 94, wrap(line, 24), cls="small", dy=15)
    body.append(f'<text class="note" x="16" y="{h - 14}">Source: EC2 Instance Types Guide, naming conventions. Checked 2026-10-24.</text>')
    svg("06-01-name-decoded.svg", w, h,
        "The parts of the instance type name m7g.large",
        "The name m7g.large in large letters, with four labeled parts. m: the series, general purpose. "
        "7: the generation, 7th, where a higher number is newer. g: an option, extra letters, here an AWS "
        "Graviton (Arm) processor. large, after the dot: the size, how much of the family's hardware. "
        "Together, m7g is the family.",
        body, style=STYLE)


def month_by_state():
    """A month of one small instance in each state: what still bills."""
    inst = PRICES["t3.micro"][0] * HOURS_MONTH
    ip = IPV4 * HOURS_MONTH
    ebs = GP3 * ROOT_GB
    rows = [("Running all month", [("s1", inst, "instance hours"), ("s2", ip, "public IPv4"), ("s3", ebs, "EBS volume")]),
            ("Stopped all month", [("s3", ebs, "EBS volume")]),
            ("Stopped, Elastic IP kept", [("s2", ip, "Elastic IP"), ("s3", ebs, "EBS volume")]),
            ("Terminated", [])]
    w, left, top, pw, rowh, xmax = 680, 16, 112, 470, 56, 12
    h = top + rowh * len(rows) + 50
    body = [
        '<text class="title" x="16" y="28">Stopping pauses the instance charge; terminating ends every charge</text>',
        f'<text class="sub" x="16" y="48">One t3.micro with an {ROOT_GB} GB gp3 volume, for a {HOURS_MONTH}-hour month, US East (N. Virginia), as of 2026-10-24</text>',
    ]
    swatch(body, 16, 80, "s1", "Instance hours")
    swatch(body, 150, 80, "s2", "Public IPv4 address")
    swatch(body, 320, 80, "s3", "EBS volume storage")
    sx = lambda v: pw * v / xmax
    for i, (label, segs) in enumerate(rows):
        y = top + i * rowh
        body.append(f'<text class="lab" x="{left}" y="{y + 14}">{label}</text>')
        by, x = y + 22, left
        total = sum(v for _, v, _ in segs)
        for j, (cls, v, what) in enumerate(segs):
            wd = sx(v) - (2 if j < len(segs) - 1 else 0)
            tip = f"{label}: {what} ${v:.2f}"
            if j == len(segs) - 1:
                body.append(f'<path class="{cls}" d="{right_rounded(x, by, max(wd, 3), 20)}"><title>{tip}</title></path>')
            else:
                body.append(f'<rect class="{cls}" x="{x:.1f}" y="{by}" width="{wd:.1f}" height="20"><title>{tip}</title></rect>')
            x += sx(v)
        txt = f"${total:.2f}" if segs else "$0.00: nothing left to bill"
        body.append(f'<text class="lab" x="{x + 8:.1f}" y="{by + 15}">{txt}</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top + 18}" y2="{top + rowh * len(rows)}"/>')
    body.append(f'<text class="note" x="16" y="{h - 26}">Stopping releases the automatic public IPv4 address; an Elastic IP is charged until you release it.</text>')
    body.append(f'<text class="note" x="16" y="{h - 10}">Prices from the AWS Price List, retrieved 2026-10-24. Terminated assumes the volume is set to delete on termination.</text>')
    svg("06-01-month-by-state.svg", w, h,
        "A month's cost of one small instance when running, stopped, stopped with an Elastic IP, and terminated",
        f"Stacked horizontal bar chart for one t3.micro with an {ROOT_GB} GB gp3 volume over {HOURS_MONTH} hours, "
        f"US East (N. Virginia), as of 2026-10-24. Running all month: instance hours ${inst:.2f}, public IPv4 "
        f"${ip:.2f}, EBS volume ${ebs:.2f}, total ${inst + ip + ebs:.2f}. Stopped all month: EBS volume ${ebs:.2f} only. "
        f"Stopped with an Elastic IP kept: Elastic IP ${ip:.2f} plus EBS ${ebs:.2f}, total ${ip + ebs:.2f}. "
        "Terminated: $0.00, nothing left to bill.", body, style=STYLE)


def on_demand_vs_ri():
    """A year of one instance: On-Demand vs a 1-year Standard Reserved Instance, no upfront."""
    names = ["t3.micro", "t3.small", "m7g.large", "r7g.large"]
    w, left, top, pw, grp, xmax = 680, 120, 104, 420, 64, 1000
    h = top + grp * len(names) + 50
    body = [
        '<text class="title" x="16" y="28">The same instance type, two prices</text>',
        '<text class="sub" x="16" y="48">A year (8,760 hours) of one Linux instance, US East (N. Virginia), as of 2026-10-24</text>',
    ]
    swatch(body, 16, 78, "s1", "On-Demand: no commitment")
    swatch(body, 230, 78, "s2", "Reserved Instance: 1 year, Standard, no upfront")
    sx = lambda v: pw * v / xmax
    for v in range(0, xmax + 1, 250):
        x = left + sx(v)
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 4}" y2="{top + grp * len(names)}"/>')
        body.append(f'<text class="tick" x="{x:.1f}" y="{top + grp * len(names) + 18}" text-anchor="middle">${v:,}</text>')
    for i, n in enumerate(names):
        od, ri = (p * HOURS_YEAR for p in PRICES[n])
        y = top + i * grp + 8
        body.append(f'<text class="mono" x="16" y="{y + 26}">{n}</text>')
        body.append(f'<path class="s1" d="{right_rounded(left, y, sx(od), 20)}"><title>{n}: On-Demand ${od:,.2f} a year</title></path>')
        body.append(f'<text class="lab" x="{left + sx(od) + 8:.1f}" y="{y + 15}">${od:,.0f}</text>')
        body.append(f'<path class="s2" d="{right_rounded(left, y + 22, sx(ri), 20)}"><title>{n}: Reserved Instance ${ri:,.2f} a year</title></path>')
        body.append(f'<text class="lab" x="{left + sx(ri) + 8:.1f}" y="{y + 37}">${ri:,.0f} ({(1 - ri / od) * 100:.0f}% less)</text>')
    body.append(f'<text class="note" x="16" y="{h - 12}">AWS Price List offer files, retrieved 2026-10-24. The Reserved Instance is a billing commitment, not a different server.</text>')
    desc = "; ".join(f"{n}: On-Demand ${PRICES[n][0] * HOURS_YEAR:,.2f}, Reserved Instance ${PRICES[n][1] * HOURS_YEAR:,.2f}" for n in names)
    svg("06-01-on-demand-vs-ri.svg", w, h,
        "A year of four instance types at On-Demand and Reserved Instance prices",
        "Grouped horizontal bar chart, yearly cost of one Linux instance in US East (N. Virginia) as of "
        f"2026-10-24, On-Demand compared with a 1-year Standard Reserved Instance with no upfront payment. {desc}. "
        "The Reserved Instance costs about a third less for each type.", body, style=STYLE)


if __name__ == "__main__":
    launch_choices()
    families()
    same_size()
    name_decoded()
    month_by_state()
    on_demand_vs_ri()
