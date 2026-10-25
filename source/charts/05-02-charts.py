#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 05.02 (S3 in practice) as SVG.

Usage: python3 -I source/charts/05-02-charts.py
Writes images/05-02-*.svg. Facts, checked 2026-10-23 and 2026-10-24 in the research repo
(docs/04-services/storage.md, docs/16 lab runs, and their sources):
- Block Public Access on by default for new buckets (ACCT.08, AWS Startup Security
  Baseline: buckets created on or after 2023-04-28); account-level setting found off in a
  new account (docs/16, 2026-10-23);
- S3 default encryption with SSE-S3 for every new object since 2023-01-05 (S3 User Guide,
  "Default encryption FAQ");
- versioning off by default, delete markers, every version billed as a whole object,
  enable-then-only-suspend (S3 User Guide, "Retaining multiple versions of objects with
  S3 Versioning");
- private by default; IAM and bucket policies decide access (S3 User Guide).
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --panel:#f1f0ec; --hi-fill:#d9e8fb; --off-fill:#fbe1d6;",
    dark_extra=" --panel:#252523; --hi-fill:#1b3554; --off-fill:#4d2716;",
    rules_extra="""
  .panel { fill: var(--panel); stroke: var(--axis); stroke-width: 1; }
  .on { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 1.5; }
  .off { fill: var(--off-fill); stroke: var(--s2); stroke-width: 1.5; stroke-dasharray: 6 4; }
  .ver { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .cur { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 2; }
  .marker { fill: var(--off-fill); stroke: var(--s2); stroke-width: 2; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .tag { fill: var(--ink); font-size: 11.5px; font-weight: 600; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .num { fill: var(--surface); font-size: 12px; font-weight: 700; }
  .numc { fill: var(--ink); }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }""")


def protection_layers():
    """Big picture: the layers that protect the photo bucket, and which start on."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Five layers protect the data in a bucket</text>',
        '<text class="sub" x="16" y="48">Three are on when you create a bucket. You choose the other two.</text>',
    ]
    layers = [
        ("Block Public Access", "Someone making the bucket or its objects public by mistake",
         "On: blocks all public access", True),
        ("Policies (IAM and bucket policy)", "The wrong person reading, changing or deleting data",
         "On: private, open only where a policy allows", True),
        ("Encryption at rest", "Someone reading the stored bytes without permission",
         "On: SSE-S3 for every new object", True),
        ("Versioning", "An overwrite or a delete you didn't mean",
         "Off: you turn it on", False),
        ("A copy somewhere else", "Losing the bucket, the Region or the account",
         "Off: replication or backups you set up", False),
    ]
    x0, full = 16, w - 32
    y = 72
    body.append(f'<text class="cellt" x="{x0 + 44}" y="{y}">Layer</text>')
    body.append(f'<text class="cellt" x="{x0 + 262}" y="{y}">Protects against</text>')
    body.append(f'<text class="cellt" x="{x0 + 486}" y="{y}">New bucket</text>')
    y += 10
    for i, (name, against, default, on) in enumerate(layers):
        a = wrap(against, 32)
        d = wrap(default, 25)
        h = 22 + 15 * max(len(a), len(d), 1) + 4
        cls = "on" if on else "off"
        body.append(f'<rect class="{cls}" x="{x0}" y="{y}" width="{full}" height="{h}" rx="6"/>')
        body.append(f'<circle class="numc" cx="{x0 + 20}" cy="{y + h / 2}" r="11"/>')
        body.append(f'<text class="num" x="{x0 + 20}" y="{y + h / 2 + 4}" text-anchor="middle">{i + 1}</text>')
        text_lines(body, x0 + 44, y + 21, wrap(name, 26), cls="cellt", dy=15)
        text_lines(body, x0 + 262, y + 21, a, cls="small", dy=15)
        text_lines(body, x0 + 486, y + 21, d, cls="small", dy=15)
        y += h + 6
    y += 16
    y = text_lines(body, 16, y, wrap("Solid blue boxes start on. Dashed orange boxes start off. Durability, AWS's side of the line, sits under all five.", 88), cls="small")
    y += 4
    body.append(f'<text class="note" x="16" y="{y}">Defaults for a general purpose bucket, from the S3 User Guide and our Lab 01 run, checked 2026-10-24.</text>')
    svg("05-02-protection-layers.svg", w, y + 14,
        "Five layers that protect the data in an S3 bucket, and which are on for a new bucket",
        "Five numbered rows. 1, Block Public Access: protects against someone making the bucket or its "
        "objects public by mistake; on, blocking all public access. 2, policies, IAM and the bucket policy: protect "
        "against the wrong person reading, changing or deleting data; on, the bucket is private and open "
        "only where a policy allows. 3, encryption at rest: protects against someone reading the "
        "stored bytes without permission; on for every new object, with SSE-S3. 4, versioning: protects "
        "against an overwrite or a delete you didn't mean; off, you turn it on. 5, a copy somewhere else: "
        "protects against losing the bucket, the Region or the account; off, replication or backups that "
        "you set up. Rows 1 to 3 are solid blue boxes, on; rows 4 and 5 are dashed orange boxes, off. "
        "Durability, AWS's side of the line, sits under all five.", body, style=STYLE)


if __name__ == "__main__":
    protection_layers()
