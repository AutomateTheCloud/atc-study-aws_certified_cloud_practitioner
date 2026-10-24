#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the case board for Simulation S4 (the policy playground) as SVG.

Usage: python3 -I source/charts/04-09-charts.py
Writes images/04-09-case-board.svg. The eight cases and their outcomes are the model
answers in guide/04-shared-responsibility-and-access/09-sim-policy-playground.md, worked
from AWS's policy evaluation rules (IAM User Guide, "Policies and permissions in IAM").
Change the cases there and here together.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

COLUMNS = ["SCP", "Permissions boundary", "Identity policies", "Resource policy"]

# (case label, cells for the four policy types, decisive column index, result, reason)
# "—" means the policy type isn't present in that case.
CASES = [
    ("1 Teammate, group with no policies, downloads a photo", ["—", "—", "No allow", "—"], 2, "Denied", "default deny"),
    ("2 Teammate, group allows photo files, downloads a photo", ["—", "—", "Allows", "—"], 2, "Allowed", "an allow, no deny"),
    ("3 Teammate with Lab 04's broken guardrail, uploads", ["—", "—", "Allows and denies", "—"], 2, "Denied", "explicit deny wins"),
    ("4 Photographer, no identity policy; bucket policy names her", ["—", "—", "No allow", "Allows"], 3, "Allowed", "same-account resource policy"),
    ("5 Print shop user in another account downloads a photo", ["—", "—", "No allow", "Allows"], 2, "Denied", "cross-account needs both"),
    ("6 Chain shop admin with AdministratorAccess creates a user", ["Doesn't allow", "—", "Allows", "—"], 0, "Denied", "outside the SCP"),
    ("7 Chain shop user with no policies downloads a photo", ["Allows", "—", "No allow", "—"], 2, "Denied", "an SCP grants nothing"),
    ("8 Helper, admin within an S3-only boundary, creates a user", ["—", "Doesn't allow", "Allows", "—"], 1, "Denied", "outside the boundary"),
]

STYLE = make_style(
    rules_extra="""
  .cell { fill: var(--surface); stroke: var(--grid); stroke-width: 1; }
  .absent { fill: var(--surface); stroke: var(--grid); stroke-width: 1; stroke-dasharray: 3 3; }
  .decides { fill: none; stroke: var(--ink); stroke-width: 2.5; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .celltext { fill: var(--ink); font-size: 13px; }
  .celltext-key { fill: var(--ink); font-size: 13px; font-weight: 700; }
  .muted { fill: var(--muted); font-size: 13px; }
  .result { fill: var(--ink); font-size: 14px; font-weight: 700; }
  .small { fill: var(--ink2); font-size: 12px; }""",
)


def case_board():
    w = 820
    left, top, labw, colw, resw, rowh = 16, 112, 236, 92, 140, 52
    gx = left + labw
    rx = gx + colw * len(COLUMNS)
    body = [
        '<text class="title" x="16" y="28">Eight requests, and the policy that decided each one</text>',
        '<text class="sub" x="16" y="48">The heavy outline marks the deciding cell; a dashed cell means that policy type isn\'t present</text>',
    ]
    for j, col in enumerate(COLUMNS):
        lines = wrap(col, 12)
        text_lines(body, gx + colw * j + colw / 2, top - 12 - 15 * (len(lines) - 1), lines, cls="head", dy=15, anchor="middle")
    body.append(f'<text class="head" x="{rx + 12}" y="{top - 12}">Result and why</text>')
    for i, (label, cells, key, result, reason) in enumerate(CASES):
        y = top + rowh * i
        lines = wrap(label, 34)
        text_lines(body, left, y + rowh / 2 - 8 * (len(lines) - 1) + 4, lines, cls="lab", dy=16)
        tip = f"Case {label}: " + "; ".join(f"{c}: {v}" for c, v in zip(COLUMNS, cells)) + f". Result: {result}, {reason}."
        body.append(f"<g><title>{tip}</title>")
        for j, val in enumerate(cells):
            x = gx + colw * j
            if val == "—":
                body.append(f'<rect class="absent" x="{x + 2}" y="{y + 2}" width="{colw - 4}" height="{rowh - 4}" rx="4"/>')
                body.append(f'<text class="muted" x="{x + colw / 2:.1f}" y="{y + rowh / 2 + 4:.1f}" text-anchor="middle">none</text>')
                continue
            body.append(f'<rect class="cell" x="{x + 2}" y="{y + 2}" width="{colw - 4}" height="{rowh - 4}" rx="4"/>')
            tl = wrap(val, 11)
            cls = "celltext-key" if j == key else "celltext"
            text_lines(body, x + colw / 2, y + rowh / 2 - 7 * (len(tl) - 1) + 4, tl, cls=cls, dy=14, anchor="middle")
            if j == key:
                body.append(f'<rect class="decides" x="{x + 3}" y="{y + 3}" width="{colw - 6}" height="{rowh - 6}" rx="4"/>')
        mark = "✓" if result == "Allowed" else "✗"
        body.append(f'<text class="result" x="{rx + 12}" y="{y + rowh / 2 - 2:.1f}">{mark} {result}</text>')
        body.append(f'<text class="small" x="{rx + 12}" y="{y + rowh / 2 + 14:.1f}">{reason}</text>')
        body.append("</g>")
        body.append(f'<line class="grid" x1="{left}" x2="{w - 16}" y1="{y + rowh:.1f}" y2="{y + rowh:.1f}"/>')
    h = top + rowh * len(CASES) + 40
    body.append(f'<text class="sub" x="16" y="{h - 14}">Only cases 2 and 4 are allowed. The six denials come from four different rules.</text>')
    desc = "A table of eight cases. " + " ".join(
        f"Case {label}. " + ", ".join(f"{c}: {v if v != '—' else 'none'}" for c, v in zip(COLUMNS, cells))
        + f". Deciding: {COLUMNS[key]}. Result: {result}, because of {reason}."
        for label, cells, key, result, reason in CASES)
    svg("04-09-case-board.svg", w, h, "Eight policy evaluation cases: which policies were present, which one decided, and the result",
        desc, body, style=STYLE)


if __name__ == "__main__":
    case_board()
