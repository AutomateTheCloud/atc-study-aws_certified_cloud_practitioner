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
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402


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


if __name__ == "__main__":
    families()
