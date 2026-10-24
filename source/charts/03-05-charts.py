#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphic for Lab 02 (AZ names vs AZ IDs) as SVG.

Usage: python3 -I source/charts/03-05-charts.py
Writes images/03-05-az-names-vs-ids.svg. Facts from AWS's "AWS Availability Zones"
page (read 2026-10-23): an AZ name is the Region code plus a letter; for accounts
created before November 2025, AWS maps names to physical AZs independently for each
account in its oldest Regions; an AZ ID is the same physical location in every
account. The mapping drawn here is a made-up example, not the real one.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg  # noqa: E402

STYLE = make_style(
    light_extra=" --id-fill:#d9e8fb; --name-fill:#f1f0ec;",
    dark_extra=" --id-fill:#1b3554; --name-fill:#252523;",
    rules_extra="""
  .idbox { fill: var(--id-fill); stroke: var(--s1); stroke-width: 1.5; }
  .namebox { fill: var(--name-fill); stroke: var(--axis); stroke-width: 1; }
  .map { stroke: var(--muted); stroke-width: 1.5; fill: none; }
  .maphi { stroke: var(--s2); stroke-width: 3; fill: none; }
  .mono { fill: var(--ink); font-size: 13px; font-family: ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

IDS = ["use1-az1", "use1-az2", "use1-az3"]
ACCOUNT_A = {"us-east-1a": 0, "us-east-1b": 1, "us-east-1c": 2}  # made-up example
ACCOUNT_B = {"us-east-1a": 1, "us-east-1b": 2, "us-east-1c": 0}  # made-up example


def names_vs_ids():
    w = 680
    body = [
        '<text class="title" x="16" y="28">The same AZ name can point to different places</text>',
        '<text class="sub" x="16" y="48">In older accounts, each account\'s names are mapped on their own. AZ IDs never change.</text>',
    ]
    top, rh = 110, 56
    lx, mx, rx = 40, 270, 500
    bw, bh = 140, 34
    body.append(f'<text class="head" x="{lx + bw / 2}" y="{top - 24}" text-anchor="middle">Your account: AZ names</text>')
    body.append(f'<text class="head" x="{mx + bw / 2}" y="{top - 24}" text-anchor="middle">Physical AZs: AZ IDs</text>')
    body.append(f'<text class="head" x="{rx + bw / 2}" y="{top - 24}" text-anchor="middle">A friend\'s account</text>')
    for i, az in enumerate(IDS):
        y = top + i * rh
        body.append(f'<rect class="idbox" x="{mx}" y="{y}" width="{bw}" height="{bh}" rx="5"/>')
        body.append(f'<text class="mono" x="{mx + bw / 2}" y="{y + 22}" text-anchor="middle">{az}</text>')
    for side, mapping, x in (("A", ACCOUNT_A, lx), ("B", ACCOUNT_B, rx)):
        for i, (name, target) in enumerate(mapping.items()):
            y = top + i * rh
            body.append(f'<rect class="namebox" x="{x}" y="{y}" width="{bw}" height="{bh}" rx="5"/>')
            body.append(f'<text class="mono" x="{x + bw / 2}" y="{y + 22}" text-anchor="middle">{name}</text>')
            ty = top + target * rh + bh / 2
            sy = y + bh / 2
            cls = "maphi" if name == "us-east-1a" else "map"
            if side == "A":
                body.append(f'<path class="{cls}" d="M{x + bw},{sy} C{x + bw + 50},{sy} {mx - 50},{ty} {mx},{ty}"/>')
            else:
                body.append(f'<path class="{cls}" d="M{x},{sy} C{x - 50},{sy} {mx + bw + 50},{ty} {mx + bw},{ty}"/>')
    y = top + 3 * rh + 12
    body.append(f'<text class="lab" x="16" y="{y}">Thick lines: <tspan font-family="monospace">us-east-1a</tspan> is a different physical AZ in each of these two accounts.</text>')
    body.append(f'<text class="small" x="16" y="{y + 20}">To agree on a place with another account, compare AZ IDs, not names.</text>')
    body.append(f'<text class="note" x="16" y="{y + 44}">Made-up example mapping. AWS says accounts created from November 2025 get the same mapping;</text>')
    body.append(f'<text class="note" x="16" y="{y + 60}">older accounts in its oldest Regions may differ. Checked 2026-10-23.</text>')
    svg("03-05-az-names-vs-ids.svg", w, y + 74,
        "AZ names mapped to AZ IDs in two accounts",
        "Three columns. In the middle, three physical Availability Zones labeled by AZ ID: use1-az1, use1-az2, "
        "use1-az3. On the left, your account's AZ names: us-east-1a points to use1-az1, us-east-1b to "
        "use1-az2, us-east-1c to use1-az3. On the right, a friend's account: us-east-1a points to use1-az2, "
        "us-east-1b to use1-az3, us-east-1c to use1-az1. The two us-east-1a lines are drawn thick to show "
        "that the same name is a different physical AZ in each account. The mapping is a made-up example. "
        "AWS says accounts created from November 2025 get the same mapping, while older accounts in its "
        "oldest Regions may differ. To agree on a place with another account, compare AZ IDs.",
        body, style=STYLE)


if __name__ == "__main__":
    names_vs_ids()
