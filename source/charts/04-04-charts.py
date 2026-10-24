#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 04.04 (policies and least privilege) as SVG.

Usage: python3 -I source/charts/04-04-charts.py
Writes images/04-04-*.svg. The policy is the lesson's own example for the made-up bakery
bucket; the wording is the lesson's summary of the IAM User Guide (policies, managed vs
inline, least privilege; checked 2026-10-23), not AWS text. Our own design: no AWS logos,
icons or trade dress.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(rules_extra="""
  .card { fill: none; stroke: var(--axis); stroke-width: 1; }
  .card-s1 { fill: none; stroke: var(--s1); stroke-width: 2; }
  .codebg { fill: none; stroke: var(--axis); stroke-width: 1; }
  .code { font-family: ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace; fill: var(--ink); font-size: 12px; }
  .code-dim { font-family: ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace; fill: var(--muted); font-size: 12px; }
  .brace { stroke: var(--s1); stroke-width: 2; fill: none; }
  .name { fill: var(--ink); font-size: 15px; font-weight: 600; }
  .key { fill: var(--muted); font-size: 11px; font-weight: 600; letter-spacing: 0.5px; }
  .small { fill: var(--ink2); font-size: 12px; }
  .box { fill: var(--surface); stroke: var(--muted); stroke-width: 1; }
  .box-s1 { fill: var(--surface); stroke: var(--s1); stroke-width: 2; }
  .attach { stroke: var(--muted); stroke-width: 1.5; fill: none; }""")

POLICY = [
    ('{', 0, None),
    ('"Version": "2012-10-17",', 1, None),
    ('"Statement": [', 1, None),
    ('{', 2, None),
    ('"Sid": "SeeTheBucket",', 3, "sid"),
    ('"Effect": "Allow",', 3, "effect"),
    ('"Action": "s3:ListBucket",', 3, "action"),
    ('"Resource": "arn:aws:s3:::bakery-cake-photos"', 3, "resource"),
    ('},', 2, None),
    ('{', 2, None),
    ('"Sid": "ReadAndAddPhotos",', 3, None),
    ('"Effect": "Allow",', 3, None),
    ('"Action": ["s3:GetObject", "s3:PutObject"],', 3, None),
    ('"Resource": "arn:aws:s3:::bakery-cake-photos/*"', 3, None),
    ('}', 2, None),
    (']', 1, None),
    ('}', 0, None),
]
NOTES = {
    "effect": ("Effect", "Allow or Deny."),
    "action": ("Action", "What may be done, written service:action."),
    "resource": ("Resource", "Which thing, by its ARN; /* means every file in the bucket."),
}


def policy_anatomy():
    w, lh, top = 680, 19, 70
    body = [
        '<text class="title" x="16" y="28">Anatomy of an identity-based policy</text>',
        '<text class="sub" x="16" y="48">Two statements, each saying Allow or Deny, which actions, and on which resources</text>',
    ]
    codew = 424
    ch = lh * len(POLICY) + 20
    body.append(f'<rect class="codebg" x="16" y="{top}" width="{codew}" height="{ch}" rx="6"/>')
    # statement brackets on the left margin of the code box
    y = top + 22
    ys = {}
    for i, (txt, ind, tag) in enumerate(POLICY):
        cls = "code" if ind >= 3 or ind == 2 else "code-dim"
        body.append(f'<text class="{cls}" x="{28 + ind * 14}" y="{y}" xml:space="preserve">{txt}</text>')
        ys[i] = y
        if tag:
            ys[tag] = y
        y += lh
    # notes on the right, each with a lead line to its line in statement 1
    nx = codew + 34
    ny = top + 40
    for tag in ("effect", "action", "resource"):
        title, text = NOTES[tag]
        ly = ys[tag] - 4
        body.append(f'<line class="lead" x1="{codew + 16}" x2="{nx - 6}" y1="{ly}" y2="{ny - 4}"/>')
        body.append(f'<text class="key" x="{nx}" y="{ny}">{title.upper()}</text>')
        ny = text_lines(body, nx, ny + 16, wrap(text, 28), cls="small", dy=15) + 14
    # statement 2 note
    s2y = ys[11] - 4
    body.append(f'<text class="key" x="{nx}" y="{s2y}">STATEMENT 2</text>')
    text_lines(body, nx, s2y + 16, wrap("Same parts again: read and add files inside the bucket.", 28), cls="small", dy=15)
    h = top + ch + 40
    text_lines(body, 16, top + ch + 26, ["No Principal line: an identity-based policy applies to whoever it is attached to."], cls="sub")
    svg("04-04-policy-anatomy.svg", w, h,
        "Anatomy of an identity-based policy for the bakery's photo bucket",
        "A JSON policy with two statements. Statement 1, labeled SeeTheBucket: Effect Allow, Action s3:ListBucket, "
        "Resource arn:aws:s3:::bakery-cake-photos. Statement 2, labeled ReadAndAddPhotos: Effect Allow, Actions "
        "s3:GetObject and s3:PutObject, Resource arn:aws:s3:::bakery-cake-photos/* (the files in the bucket). Notes "
        "explain: Effect is Allow or Deny; Action is what may be done, as service:action; "
        "Resource is which thing, by its ARN, where /* means every file in the bucket. A footnote says there is no Principal line, because an identity-based "
        "policy applies to whoever it is attached to.", body, style=STYLE)


KINDS = [
    ("AWS managed", "AWS", "No", "Many users, groups and roles, in any account",
     "Stays; it belongs to AWS", "AdministratorAccess (primer page 03)", False),
    ("Customer managed", "You", "Yes", "Many users, groups and roles in your account",
     "Stays, ready to reuse", "The bakery's photo-bucket policy", True),
    ("Inline", "You", "Yes", "Exactly one user, group or role",
     "Deleted with it", "A one-off exception for one role", False),
]


def managed_vs_inline():
    w, cw, gap = 680, 210, 9
    top = 66
    body = [
        '<text class="title" x="16" y="28">Three kinds of identity-based policy</text>',
        '<text class="sub" x="16" y="48">Managed policies stand alone and attach to many identities; an inline policy lives inside one</text>',
    ]
    rows = [("WHO WRITES IT", 1), ("CAN YOU EDIT IT?", 2), ("ATTACHES TO", 3),
            ("WHEN THE IDENTITY IS DELETED", 4), ("EXAMPLE", 5)]
    dh = 112  # mini diagram height
    texth = 0
    for k in KINDS:
        t = 0
        for _, idx in rows:
            t += 16 + 15 * len(wrap(k[idx], 28)) + 8
        texth = max(texth, t)
    ch = 40 + dh + texth + 8
    desc = []
    for i, k in enumerate(KINDS):
        x = 16 + i * (cw + gap)
        body.append(f'<rect class="{"card-s1" if k[6] else "card"}" x="{x}" y="{top}" width="{cw}" height="{ch}" rx="8"/>')
        body.append(f'<text class="name" x="{x + 14}" y="{top + 26}">{k[0]}</text>')
        dy0 = top + 40
        cx = x + cw / 2
        if k[0] != "Inline":
            # standalone policy box, lines down to three identities
            body.append(f'<rect class="{"box-s1" if k[6] else "box"}" x="{cx - 50}" y="{dy0}" width="100" height="26" rx="4"/>')
            body.append(f'<text class="small" x="{cx}" y="{dy0 + 17}" text-anchor="middle">Policy</text>')
            for j, lab in enumerate(("User", "Group", "Role")):
                bx = x + 14 + j * 62
                body.append(f'<path class="attach" d="M{cx},{dy0 + 26} L{bx + 28},{dy0 + 64}"/>')
                body.append(f'<rect class="box" x="{bx}" y="{dy0 + 64}" width="56" height="26" rx="4"/>')
                body.append(f'<text class="small" x="{bx + 28}" y="{dy0 + 81}" text-anchor="middle">{lab}</text>')
        else:
            body.append(f'<rect class="box" x="{cx - 70}" y="{dy0}" width="140" height="90" rx="6"/>')
            body.append(f'<text class="small" x="{cx}" y="{dy0 + 18}" text-anchor="middle">One role</text>')
            body.append(f'<rect class="box" x="{cx - 50}" y="{dy0 + 40}" width="100" height="26" rx="4"/>')
            body.append(f'<text class="small" x="{cx}" y="{dy0 + 57}" text-anchor="middle">Policy inside</text>')
        yy = dy0 + dh
        for key, idx in rows:
            body.append(f'<text class="key" x="{x + 14}" y="{yy}">{key}</text>')
            yy = text_lines(body, x + 14, yy + 16, wrap(k[idx], 28), cls="lab", dy=15) + 8
        desc.append(f"{k[0]}: written by {k[1]}; editable: {k[2].lower()}; attaches to {k[3].lower()}; "
                    f"when the identity is deleted: {k[4].lower()}; example: {k[5]}.")
    h = top + ch + 12
    svg("04-04-managed-vs-inline.svg", w, h,
        "AWS managed, customer managed and inline policies compared",
        "Three cards. The AWS managed and customer managed cards each show one standalone policy attached to a user, a "
        "group and a role. The inline card shows a policy drawn inside one role. The customer managed card is "
        "highlighted. " + " ".join(desc), body, style=STYLE)


LEVELS = [
    ("AdministratorAccess", "Every action, on every resource, in the account"),
    ("A storage-wide policy", "Every S3 action, on every bucket in the account"),
    ("The teammate's policy", "List one bucket; read and add the photos in it"),
    ("With a condition", "...and only when signed in with MFA"),
]


def narrowing_scope():
    w, top = 680, 66
    body = [
        '<text class="title" x="16" y="28">Least privilege: each step grants less</text>',
        '<text class="sub" x="16" y="48">Narrow the actions, then the resources, then add conditions. Highlighted: what the photo job needs.</text>',
    ]
    x, y, bw, bh = 16, top, w - 32, 300
    desc = []
    for i, (name, text) in enumerate(LEVELS):
        cls = "card-s1" if i == 2 else "card"
        body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{bw}" height="{bh}" rx="10"/>')
        body.append(f'<text class="name" x="{x + 16}" y="{y + 26}">{name}</text>')
        body.append(f'<text class="small" x="{x + 16}" y="{y + 45}">{text}</text>')
        desc.append(f"{name}: {text}")
        x, y, bw, bh = x + 36, y + 62, bw - 72, bh - 76
    h = top + 300 + 12
    svg("04-04-narrowing-scope.svg", w, h,
        "Least privilege as nested boxes, from all access down to one job",
        "Four nested boxes, each inside the last. " + "; ".join(desc) + ". The third box, the teammate's policy, is "
        "highlighted as what the photo job needs.", body, style=STYLE)


if __name__ == "__main__":
    policy_anatomy()
    managed_vs_inline()
    narrowing_scope()
