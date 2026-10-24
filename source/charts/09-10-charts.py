#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for Simulation S11 (Organizations, SCPs and consolidated billing) as SVG.

Usage: python3 -I source/charts/09-10-charts.py
Writes images/09-10-scp-levels.svg (the model answer to Decision 1: which level decides each
case) and images/09-10-combined-tiers.svg (S3 Standard storage billed for three separate
accounts vs one organization).
Facts: SCP rules from "Service control policies (SCPs)", AWS Organizations User Guide, retrieved
2026-10-24 (every level must allow; the management account and service-linked roles are not
affected; the member root user is). S3 Standard storage in US East (N. Virginia): $0.023 per
GB-month for the first 50 TB (51,200 GB) and $0.022 for the next 450 TB, from the AmazonS3
Price List offer file published 2026-10-15, retrieved 2026-10-24. Volume tiers apply to an
organization's combined usage ("Effective billing date, account activity, and volume
discounts", AWS Billing User Guide). The organization, accounts and storage amounts are made up.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, swatch, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --cell:#fcfcfb; --hit:#fbe1d6; --na:#f1f0ec;",
    dark_extra=" --cell:#1a1a19; --hit:#4d2716; --na:#252523;",
    rules_extra="""
  .cell { fill: var(--cell); stroke: var(--grid); stroke-width: 1; }
  .na { fill: var(--na); stroke: var(--grid); stroke-width: 1; }
  .hit { fill: var(--hit); stroke: var(--ink); stroke-width: 2.5; }
  .head { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .ct { fill: var(--ink); font-size: 11.5px; }
  .ctb { fill: var(--ink); font-size: 12px; font-weight: 700; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

COLS = [("Root SCPs", 128), ("OU SCPs", 128), ("Account SCP", 84), ("IAM policy", 84), ("Result", 84)]
# Each case: label lines, then cells. A cell is (text, kind) with kind cell | hit | na; a "span" cell covers
# the three SCP columns.
CASES = [
    (["a  shop-dev admin:", "EC2 in eu-west-1"],
     [("allows", "cell"), ("Workloads: denies, outside the Regions", "hit"), ("allows", "cell"),
      ("allows", "cell"), ("Denied", "res")]),
    (["b  shop-prod root user:", "stop own trail"],
     [("protect-audit-trail denies", "hit"), ("allows", "cell"), ("allows", "cell"),
      ("allows", "cell"), ("Denied", "res")]),
    (["c  chain-billing admin:", "stop own trail"],
     [("SCPs don't apply to the management account", "span"), ("allows", "cell"), ("Allowed", "res")]),
    (["d  sandbox-anna admin:", "DynamoDB table"],
     [("allows", "cell"), ("Sandbox: allows DynamoDB", "cell"), ("allows", "cell"),
      ("allows", "cell"), ("Allowed", "res")]),
    (["e  sandbox-anna admin:", "EC2 instance"],
     [("allows", "cell"), ("Sandbox: EC2 not on the list", "hit"), ("allows", "cell"),
      ("allows", "cell"), ("Denied", "res")]),
    (["f  GuardDuty service-", "linked role, eu-west-1"],
     [("SCPs don't apply to service-linked roles", "span"), ("its own policy allows", "cell"), ("Allowed", "res")]),
]


def levels():
    w, x0, lw, top, rh = 680, 16, 150, 74, 50
    body = ['<text class="title" x="16" y="28">Which level decides each case</text>',
            '<text class="sub" x="16" y="48">The outlined cell is the one that decides; every level must allow</text>']
    x = x0 + lw
    for name, cw in COLS:
        body.append(f'<text class="head" x="{x + cw / 2:.1f}" y="{top - 8}" text-anchor="middle">{name}</text>')
        x += cw
    for i, (label, cells) in enumerate(CASES):
        y = top + i * rh
        text_lines(body, x0, y + 21, label, cls="ct", dy=15)
        x, ci = x0 + lw, 0
        for text, kind in cells:
            if kind == "span":
                cw = sum(c for _, c in COLS[:3])
                cls, ci = "hit", 3
            else:
                cw = COLS[ci][1]
                cls = {"cell": "cell", "hit": "hit", "res": "na"}[kind]
                ci += 1
            body.append(f'<rect class="{cls}" x="{x + 2}" y="{y + 2}" width="{cw - 4}" height="{rh - 4}" rx="4"/>')
            lines = wrap(text, max(10, int(cw / 6.6)))
            t = "ctb" if kind in ("res", "hit", "span") else "ct"
            yy = y + rh / 2 + 4 - (len(lines) - 1) * 7
            text_lines(body, x + cw / 2, yy, lines, cls=t, dy=14, anchor="middle")
            x += cw
    yb = top + len(CASES) * rh + 22
    body.append(f'<text class="note" x="16" y="{yb}">Everyone here has AdministratorAccess in their own account, so the IAM '
                'column never decides.</text>')
    svg("09-10-scp-levels.svg", w, yb + 18,
        "Six SCP cases against the levels root, OU, account and IAM policy, with the deciding cell outlined",
        "A grid of six cases with columns root SCPs, OU SCPs, account SCP, IAM policy and result. a, a shop-dev admin "
        "launching EC2 in eu-west-1: the Workloads OU denies it as outside the Regions, outlined; denied. b, the "
        "shop-prod root user stopping its own trail: the root's protect-audit-trail denies it, outlined; denied. c, "
        "a chain-billing admin stopping its own trail: one outlined cell across the SCP columns says SCPs don't apply "
        "to the management account; allowed. d, a sandbox-anna admin creating a DynamoDB table: every level allows; "
        "allowed. e, a sandbox-anna admin launching EC2: the Sandbox OU's list doesn't include EC2, outlined; denied. "
        "f, a GuardDuty service-linked role in eu-west-1: one outlined cell says SCPs don't apply to service-linked "
        "roles; allowed. A note says everyone has AdministratorAccess, so the IAM column never decides.",
        body, style=STYLE)


def tiers():
    w, left, pw = 680, 200, 330
    gb_total = 92160
    r1, r2 = 0.023, 0.022
    body = ['<text class="title" x="16" y="28">Three separate accounts or one organization</text>',
            '<text class="sub" x="16" y="48">30 TB each in S3 Standard, US East (N. Virginia), monthly, prices as of 2026-10-24</text>']
    swatch(body, 16, 76, "s1", "Billed at $0.023 per GB-month (first 50 TB)")
    swatch(body, 340, 76, "s2", "Billed at $0.022 (next 450 TB)")
    scale = pw / gb_total
    top, bh = 100, 34
    rows = [
        ("Three separate accounts", [(30720, "s1"), (30720, "s1"), (30720, "s1")], 92160 * r1,
         "each account: 30,720 GB, all at the first-tier rate"),
        ("One organization", [(51200, "s1"), (40960, "s2")], 51200 * r1 + 40960 * r2,
         "combined: 51,200 GB at $0.023, then 40,960 GB at $0.022"),
    ]
    for i, (name, segs, total, sub) in enumerate(rows):
        y = top + i * (bh + 46)
        body.append(f'<text class="lab" x="{left - 10}" y="{y + 22}" text-anchor="end">{name}</text>')
        x = left
        for gb, cls in segs:
            sw = gb * scale
            body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{sw - 2:.1f}" height="{bh}" rx="3"/>')
            x += sw
        body.append(f'<text class="lab" x="{left + pw + 8}" y="{y + 22}">${total:,.2f}</text>')
        body.append(f'<text class="tick" x="{left}" y="{y + bh + 16}">{sub}</text>')
    yn = top + 2 * (bh + 46) + 6
    text_lines(body, 16, yn, [
        f"Difference: ${92160 * r1 - (51200 * r1 + 40960 * r2):,.2f} a month, about 2%. Gaps in the top bar mark the three accounts.",
        "1 TB = 1,024 GB. Storage only: requests and data transfer are left out."], cls="tick", dy=16)
    svg("09-10-combined-tiers.svg", w, yn + 26,
        "S3 Standard storage for three accounts of 30 TB each: $2,119.68 separately, $2,078.72 as one organization",
        "Two horizontal stacked bars of 92,160 GB each. Three separate accounts: three equal segments of 30,720 GB, "
        "all billed at $0.023 per GB-month, total $2,119.68 a month. One organization: 51,200 GB at $0.023 and "
        "40,960 GB at $0.022, total $2,078.72. The difference is $40.96 a month, about 2%. Prices are US East (N. "
        "Virginia) as of 2026-10-24; storage only.",
        body, style=STYLE)


if __name__ == "__main__":
    levels()
    tiers()
