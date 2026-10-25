#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the charts for lesson 11.04 (many accounts, one bill) as SVG.

Usage: python3 -I source/charts/11-04-charts.py
Writes images/11-04-tag-types.svg.

Facts and figures:
- m7g.large, Linux, shared tenancy, US East (N. Virginia), from the AmazonEC2 Price List offer file
  published 2026-10-23 and retrieved 2026-10-24 (research repo,
  sources/raw/pricing/compute-networking-us-east-1-summary.tsv): On-Demand $0.0816 an hour; a
  1-year Standard Reserved Instance, No Upfront, $0.054 an hour effective. 730 hours a month.
- Reserved Instances apply first to the purchasing account, then to matching usage in other
  accounts of the organization when sharing is on; both accounts must have sharing turned on
  ("How Reserved Instance discounts are applied", Amazon EC2 User Guide; "Reserved Instances and
  Savings Plans discount sharing", AWS Billing User Guide; checked 2026-10-24).
- Cost allocation tags: both types must be activated; AWS-generated tags apply to resources created
  after activation; the management account can backfill activation for up to twelve months, and
  backfilled data exists only where the resource carried the tag ("Organizing and tracking costs
  using AWS cost allocation tags", "Using AWS-generated tags", "Using user-defined cost allocation
  tags", "Backfill cost allocation tags", AWS Billing User Guide; checked 2026-10-24).
The accounts, teams and months are made up. Our own design: no AWS logos, icons, trade dress or AWS
diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, right_rounded, svg, swatch, text_lines, wrap  # noqa: E402

OD, RI, HOURS = 0.0816, 0.054, 730
RI_MONTH = round(RI * HOURS, 2)
OD_MONTH = round(OD * HOURS, 2)
assert (RI_MONTH, OD_MONTH) == (39.42, 59.57)

STYLE = make_style(
    light_extra=" --cell:#fcfcfb; --hit:#fbe1d6; --na:#f1f0ec; --on:#d9e8fb;",
    dark_extra=" --cell:#1a1a19; --hit:#4d2716; --na:#252523; --on:#1b3554;",
    rules_extra="""
  .cell { fill: var(--cell); stroke: var(--grid); stroke-width: 1; }
  .na { fill: var(--na); stroke: var(--grid); stroke-width: 1; }
  .on { fill: var(--on); stroke: var(--s1); stroke-width: 1.5; }
  .hit { fill: var(--hit); stroke: var(--ink); stroke-width: 2; }
  .unused { fill: var(--s1-light); }
  .head { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .ct { fill: var(--ink); font-size: 12px; }
  .ctm { fill: var(--muted); font-size: 12px; }
  .ctb { fill: var(--ink); font-size: 12.5px; font-weight: 700; }
  .note { fill: var(--muted); font-size: 11.5px; }""")


def tag_types():
    cols = [("", 168), ("AWS-generated tags", 238), ("User-defined tags", 238)]
    rows = [
        ("Who puts it on", "AWS, on supported resources (some Marketplace sellers add their own)", "You, on your resources (Tag Editor, the console, the API)", False),
        ("Example key", "aws:createdBy: who created the resource", "team, project, cost-center: your choice", False),
        ("In reports", "aws: prefix", "user: prefix", False),
        ("Who activates", "The management account, once, for all member accounts", "The management account (or a standalone account)", False),
        ("Activate before reports show it?", "Yes", "Yes", True),
        ("Which costs carry it", "Only resources created after activation", "Usage from activation on, while the resource carries the tag", False),
    ]
    w, x0, top = 680, 16, 70
    body = ['<text class="title" x="16" y="28">Two kinds of cost allocation tag</text>',
            '<text class="sub" x="16" y="48">The highlighted row is the same for both: nothing shows until you activate it</text>']
    x = x0
    for name, cw in cols:
        if name:
            body.append(f'<text class="head" x="{x + 8}" y="{top + 6}">{name}</text>')
        x += cw
    y = top + 18
    for label, a, b, same in rows:
        la = wrap(a, 34)
        lb = wrap(b, 34)
        ll = wrap(label, 22)
        n = max(len(la), len(lb), len(ll))
        rh = 20 + 15 * n
        x = x0
        for j, (text_l, (_, cw)) in enumerate(zip([ll, la, lb], cols)):
            cls = "hit" if (same and j) else ("na" if j == 0 else "cell")
            body.append(f'<rect class="{cls}" x="{x + 2}" y="{y + 2}" width="{cw - 4}" height="{rh - 4}" rx="4"/>')
            t = "ctb" if j == 0 else "ct"
            text_lines(body, x + 10, y + rh / 2 + 4 - (len(text_l) - 1) * 7.5, text_l, cls=t, dy=15)
            x += cw
        y += rh
    yb = y + 20
    body.append(f'<text class="note" x="16" y="{yb}">Up to 24 hours to appear after activation. From the AWS Billing User Guide, checked 2026-10-24.</text>')
    svg("11-04-tag-types.svg", w, yb + 18,
        "AWS-generated and user-defined cost allocation tags compared on six rows",
        "A grid comparing AWS-generated tags and user-defined tags. Who puts it on: AWS, on supported resources, and "
        "some Marketplace sellers; you, on your resources. Example key: aws:createdBy, who created the resource; team, "
        "project or cost-center, your choice. In reports: aws: prefix; user: prefix. Who activates: the management "
        "account, once, for all member accounts; the management account or a standalone account. Highlighted as the "
        "same for both: they must be activated before reports show them. Which costs carry them: only "
        "resources created after activation; usage from activation on, while the resource carries the tag. A note says "
        "tags take up to 24 hours to appear after activation.",
        body, style=STYLE)


if __name__ == "__main__":
    tag_types()
