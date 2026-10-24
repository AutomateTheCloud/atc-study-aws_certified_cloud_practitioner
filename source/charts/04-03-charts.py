#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 04.03 (identities) as SVG.

Usage: python3 -I source/charts/04-03-charts.py
Writes images/04-03-*.svg. The wording is the lesson's own summary of the IAM User Guide
(identities, root user, root-only tasks; checked 2026-10-23), not AWS text. Our own design:
no AWS logos, icons or trade dress.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(light_extra=" --on-s1:#ffffff;", dark_extra=" --on-s1:#1a1a19;", rules_extra="""
  .card { fill: none; stroke: var(--axis); stroke-width: 1; }
  .card-s1 { fill: none; stroke: var(--s1); stroke-width: 2; }
  .card-s2 { fill: none; stroke: var(--s2); stroke-width: 2; stroke-dasharray: 6 4; }
  .pill { fill: var(--surface); stroke: var(--muted); stroke-width: 1; }
  .pill-s1 { fill: var(--s1); }
  .pilltext { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .pilltext-on { fill: var(--on-s1); font-size: 12px; font-weight: 600; }
  .name { fill: var(--ink); font-size: 15px; font-weight: 600; }
  .key { fill: var(--muted); font-size: 11px; font-weight: 600; letter-spacing: 0.5px; }
  .small { fill: var(--ink2); font-size: 12px; }
  .tag { fill: var(--ink); font-size: 11px; font-weight: 700; letter-spacing: 0.5px; }""")

# name, what it is, credentials (pill text, temporary?), can sign in, limited by IAM policies, use it for
IDENTITIES = [
    ("Root user", "The account's first identity, created with the sign-up email address.",
     ("Long-term", False), "Yes, with the email address, password and MFA.",
     "No. IAM policies can't be attached to it.",
     "Only the few tasks that need root."),
    ("IAM user", "One named person or program inside the account.",
     ("Long-term", False), "Yes, with a console password and MFA. Programs use access keys.",
     "Yes, by the policies attached to it or its groups.",
     "Our labs' everyday admin; programs that can't use a role."),
    ("IAM user group", "A set of IAM users who share the same policies.",
     ("None", None), "No. A group has no credentials of its own.",
     "It carries policies for its members.",
     "Giving a team the same permissions in one place."),
    ("IAM role", "A set of permissions that anyone allowed to can take on for a while.",
     ("Temporary", True), "Not directly. A person or program assumes it.",
     "Yes, by its permissions policy.",
     "Programs and AWS services, other accounts, people from a central sign-in."),
]


def identity_kinds():
    w, cw, gap, wrap_at = 680, 320, 8, 42
    body = [
        '<text class="title" x="16" y="28">Four kinds of identity in an AWS account</text>',
        '<text class="sub" x="16" y="48">Only the role hands out temporary credentials; a group has no credentials at all</text>',
    ]
    rows = [("WHAT IT IS", 1), ("CAN YOU SIGN IN AS IT?", 3), ("LIMITED BY IAM POLICIES?", 4), ("USE IT FOR", 5)]
    y0 = 68
    desc = []
    for r in range(2):
        cards = IDENTITIES[r * 2:r * 2 + 2]
        # height: the taller of the two cards
        heights = []
        for c in cards:
            hgt = 44
            for _, idx in rows:
                hgt += 16 + 16 * len(wrap(c[idx], wrap_at)) + 6
            heights.append(hgt + 4)
        ch = max(heights)
        for i, c in enumerate(cards):
            x = 16 + i * (cw + gap)
            role = c[2][1] is True
            body.append(f'<rect class="{"card-s1" if role else "card"}" x="{x}" y="{y0}" width="{cw}" height="{ch}" rx="8"/>')
            body.append(f'<text class="name" x="{x + 14}" y="{y0 + 27}">{c[0]}</text>')
            ptxt = f"Credentials: {c[2][0]}"
            pw = len(ptxt) * 6.9 + 18
            px = x + cw - 14 - pw
            body.append(f'<rect class="{"pill-s1" if role else "pill"}" x="{px:.1f}" y="{y0 + 12}" width="{pw:.1f}" height="22" rx="11"/>')
            body.append(f'<text class="{"pilltext-on" if role else "pilltext"}" x="{px + pw / 2:.1f}" y="{y0 + 27}" text-anchor="middle">{ptxt}</text>')
            yy = y0 + 44
            for key, idx in rows:
                yy += 16
                body.append(f'<text class="key" x="{x + 14}" y="{yy}">{key}</text>')
                yy = text_lines(body, x + 14, yy + 17, wrap(c[idx], wrap_at), cls="lab", dy=16) - 16 + 6
            desc.append(f"{c[0]}: credentials {c[2][0].lower()}. What it is: {c[1]} Can you sign in as it? {c[3]} "
                        f"Limited by IAM policies? {c[4]} Use it for: {c[5]}")
        y0 += ch + 10
    h = y0 + 6
    svg("04-03-identity-kinds.svg", w, h,
        "Four kinds of identity in an AWS account, compared",
        "Four cards in two rows. The IAM role card is highlighted, and its credentials label reads Temporary. "
        + " ".join(desc), body, style=STYLE)


ROOT_ONLY = [
    "Change the account's email address, root password or root access keys (standalone account)",
    "Close the account, or reopen it after closing",
    "Restore permissions when the only IAM admin has locked themselves out",
    "Turn on IAM access to the billing pages",
    "View certain tax invoices, and some other billing tasks",
    "Sign up for AWS GovCloud (US)",
    "Register as a seller in the Reserved Instance Marketplace",
    "Recover a KMS key that nobody can manage, through AWS Support",
    "Turn on MFA Delete for an S3 bucket",
    "Fix an S3 bucket policy or SQS queue policy that denies everyone",
]
NOT_ROOT = [
    ("Change the AWS Support plan", True),
    ("Change the account name or contact details", False),
    ("Choose which Regions the account uses", False),
    ("Create IAM users, groups and roles", False),
    ("Create budgets and read bills (once IAM access to billing is on)", False),
]


def root_only_sort():
    w, gap = 680, 8
    lw, rw = 372, w - 32 - 372 - gap
    body = [
        '<text class="title" x="16" y="28">Does this task need the root user?</text>',
        '<text class="sub" x="16" y="48">AWS\'s current list, checked 2026-10-23. An IAM admin can do everything on the right.</text>',
    ]
    top = 66
    # left panel
    ly = top + 52
    lines_left = []
    for t in ROOT_ONLY:
        lines_left.append(wrap(t, 50))
    lh = 52 + sum(16 * len(l) + 8 for l in lines_left) + 8
    rlines = [(wrap(t, 30), trap) for t, trap in NOT_ROOT]
    rh = 52 + sum(16 * len(l) + 8 + (16 if trap else 0) for l, trap in rlines) + 8
    ph = max(lh, rh)
    body.append(f'<rect class="card-s1" x="16" y="{top}" width="{lw}" height="{ph}" rx="8"/>')
    body.append(f'<text class="name" x="30" y="{top + 24}">Only the root user can</text>')
    for l in lines_left:
        body.append(f'<circle cx="34" cy="{ly - 4}" r="3" style="fill:var(--s1)"/>')
        ly = text_lines(body, 44, ly, l, cls="lab", dy=16) + 8
    rx = 16 + lw + gap
    body.append(f'<rect class="card" x="{rx}" y="{top}" width="{rw}" height="{ph}" rx="8"/>')
    body.append(f'<text class="name" x="{rx + 14}" y="{top + 24}">No root needed</text>')
    ry = top + 52
    for l, trap in rlines:
        if trap:
            body.append(f'<rect x="{rx + 8}" y="{ry - 14}" width="4" height="{16 * (len(l) + 1) + 4}" rx="2" style="fill:var(--s2)"/>')
            body.append(f'<text class="tag" x="{rx + 18}" y="{ry}">TRAP: OLDER MATERIAL SAYS ROOT</text>')
            ry += 18
        body.append(f'<circle cx="{rx + 18}" cy="{ry - 4}" r="3" style="fill:var(--muted)"/>')
        ry = text_lines(body, rx + 28, ry, l, cls="lab", dy=16) + 8
    h = top + ph + 12
    svg("04-03-root-only-sort.svg", w, h,
        "Tasks that need the root user, and tasks that don't",
        "Two panels. Left, highlighted, only the root user can: " + "; ".join(ROOT_ONLY) + ". "
        "Right, no root needed: " + "; ".join(t for t, _ in NOT_ROOT) + ". The Support plan item is marked as a trap "
        "because older study material says it needs root.", body, style=STYLE)


if __name__ == "__main__":
    identity_kinds()
    root_only_sort()
