#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 09.05 (compliance and governance) as SVG.

Usage: python3 -I source/charts/09-05-charts.py
Writes images/09-05-*.svg. Facts come from AWS pages checked 2026-10-24: "What is AWS
Artifact?" (AWS's reports and agreements, free; customers produce their own compliance
documents), the Shared Responsibility Model page (security of vs in the cloud), the AWS
Organizations User Guide (what Organizations is; service control policies: maximum
permissions, never grant, limit a member account's root user, don't affect the management
account; general SCP examples, including the Region deny example that exempts global
services), and the AWS Control Tower User Guide (what Control Tower is; how controls work:
preventive controls from SCPs and RCPs, detective controls from AWS Config rules,
proactive controls from CloudFormation hooks). The bakery and its accounts are made up for
teaching. Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Allowed / highlighted = slot 1 (blue) tint; blocked or denied = slot 2 (orange) tint;
# neutral otherwise. Every cell also says what it means in words.
STYLE = make_style(
    light_extra=" --ok-fill:#d9e8fb; --no-fill:#fbe1d6; --n-fill:#f1f0ec;",
    dark_extra=" --ok-fill:#1b3554; --no-fill:#4d2716; --n-fill:#252523;",
    rules_extra="""
  .ok { fill: var(--ok-fill); stroke: var(--s1); stroke-width: 1.5; }
  .no { fill: var(--no-fill); stroke: var(--s2); stroke-width: 1.5; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .zlab { fill: var(--muted); font-size: 12px; }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .key { fill: var(--muted); font-size: 11px; font-weight: 600; letter-spacing: 0.4px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }""")


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


def arrow(body, x1, y1, x2, y2):
    """A straight line with a small filled head at (x2, y2)."""
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


HALVES = [
    ("AWS's controls", "security of the cloud", "n",
     [("EXAMPLES", "Physical security of data centers, hardware, the global network, each service's own infrastructure"),
      ("EVIDENCE", "AWS's audit reports and certificates, such as SOC 2, ISO 27001 and PCI DSS"),
      ("WHERE FROM", "AWS Artifact, free")]),
    ("The bakery's controls", "security in the cloud", "ok",
     [("EXAMPLES", "Its data and where it lives, who has access, how its services are configured, its staff"),
      ("EVIDENCE", "Its own records: CloudTrail activity, AWS Config history and rules, IAM access reports, written policies, training records"),
      ("WHERE FROM", "The bakery itself")]),
]


def two_halves():
    """Big picture: the auditor's question splits into AWS's half and the bakery's half."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Every audit question has an owner</text>',
        '<text class="sub" x="16" y="48">AWS proves its controls; the customer proves its own</text>',
    ]
    rect(body, "plain", 230, 66, 220, 40)
    body.append('<text class="cellt" x="340" y="91" text-anchor="middle">The auditor\'s question</text>')
    cw, gap, top = 316, 16, 132
    xs = [16, 16 + cw + gap]
    arrow(body, 300, 107, xs[0] + cw / 2, top - 2)
    arrow(body, 380, 107, xs[1] + cw / 2, top - 2)
    heights = []
    blocks = []
    for name, sub, cls, rows in HALVES:
        lines = [(k, wrap(v, 44)) for k, v in rows]
        h = 62 + sum(18 + 16 * len(ls) + 8 for _, ls in lines)
        heights.append(h)
        blocks.append((name, sub, cls, lines))
    h = max(heights)
    for x, (name, sub, cls, lines) in zip(xs, blocks):
        rect(body, cls, x, top, cw, h, 8)
        body.append(f'<text class="cellt" x="{x + 14}" y="{top + 26}">{name}</text>')
        body.append(f'<text class="small" x="{x + 14}" y="{top + 44}">{sub}</text>')
        y = top + 70
        for k, ls in lines:
            body.append(f'<text class="key" x="{x + 14}" y="{y}">{k}</text>')
            y = text_lines(body, x + 14, y + 17, ls, cls="small", dy=16) + 8
    y = top + h + 14
    rect(body, "n", 16, y, w - 32, 36, 6)
    body.append(f'<text class="cellt" x="{w / 2}" y="{y + 23}" text-anchor="middle">Compliant only when both halves are covered</text>')
    y += 60
    body.append(f'<text class="note" x="16" y="{y}">From "What is AWS Artifact?" and the Shared Responsibility Model page, checked 2026-10-24. The bakery is made up</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">for teaching.</text>')
    svg("09-05-two-halves.svg", w, y + 30,
        "An auditor's question splits into AWS's half and the bakery's half",
        "At the top, a box labeled the auditor's question, with arrows to two columns. Left column, AWS's "
        "controls, security of the cloud: examples are physical security of data centers, hardware, the global "
        "network and each service's own infrastructure; evidence is AWS's audit reports and certificates, such as "
        "SOC 2, ISO 27001 and PCI DSS; it comes from AWS Artifact, free. Right column, highlighted, the bakery's "
        "controls, security in the cloud: examples are its data and where it lives, who has access, how its "
        "services are configured, and its staff; evidence is its own records, such as CloudTrail activity, AWS "
        "Config history and rules, IAM access reports, written policies and training records; it comes from the "
        "bakery itself. A band across the bottom says: compliant only when both halves are covered.",
        body, style=STYLE)


SCP_COLS = [("Root SCP", ["denies stopping or", "deleting CloudTrail", "trails"]),
            ("Germany OU SCP", ["denies Regions", "outside Europe", "(global services", "exempt)"]),
            ("IAM policy", ["what the person's", "own policies allow"])]
SCP_ROWS = [
    ("Admin launches a server", "in Europe (Frankfurt)",
     [("n", "Allows"), ("n", "Allows"), ("n", "Allows (admin)")], ("ok", "Allowed")),
    ("Admin launches a server", "in US East (N. Virginia)",
     [("n", "Allows"), ("no", "Blocks"), ("n", "Allows (admin)")], ("no", "Denied: OU SCP")),
    ("Admin stops the", "CloudTrail trail",
     [("no", "Blocks"), ("n", "Allows"), ("n", "Allows (admin)")], ("no", "Denied: root SCP")),
    ("The account's root user", "stops the trail",
     [("no", "Blocks"), ("n", "Allows"), ("n", "Root needs none")], ("no", "Denied: root SCP")),
    ("New user, no policies, reads", "a bucket in Frankfurt",
     [("n", "Allows"), ("n", "Allows"), ("no", "No allow")], ("no", "Denied: default")),
]


def scp_ceiling():
    """Which requests in the German member account pass every SCP and an IAM allow."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">An SCP is a ceiling: every level must allow, and something must grant</text>',
        '<text class="sub" x="16" y="48">Five requests in the bakery\'s German member account</text>',
    ]
    xs = [200, 312, 424]
    cw = 106
    rx, rw = 536, 128
    top = 156
    body.append(f'<text class="zlab" x="16" y="{top - 14}">Request</text>')
    for x, (h, lines) in zip(xs, SCP_COLS):
        body.append(f'<text class="rowl" x="{x}" y="{top - 86}">{h}</text>')
        text_lines(body, x, top - 70, lines, cls="zlab", dy=15)
    body.append(f'<text class="rowl" x="{rx}" y="{top - 14}">Result</text>')
    rh = 48
    for r, (a, b, cells, res) in enumerate(SCP_ROWS):
        y = top + r * (rh + 6)
        body.append(f'<line class="grid" x1="16" x2="664" y1="{y - 3}" y2="{y - 3}"/>')
        text_lines(body, 16, y + 20, [a, b], cls="small", dy=16)
        for x, (cls, txt) in zip(xs, cells):
            rect(body, cls, x, y + 4, cw, rh - 8, 5)
            body.append(f'<text class="cellt" x="{x + cw / 2}" y="{y + 28}" text-anchor="middle">{txt}</text>')
        rect(body, res[0], rx, y + 4, rw, rh - 8, 5)
        body.append(f'<text class="cellt" x="{rx + rw / 2}" y="{y + 28}" text-anchor="middle">{res[1]}</text>')
    y = top + len(SCP_ROWS) * (rh + 6)
    body.append(f'<line class="axis" x1="16" x2="664" y1="{y - 3}" y2="{y - 3}"/>')
    y += 20
    for line in [
        "A request passes only if every SCP above the account allows it AND an IAM policy grants it. An SCP never grants:",
        "in the last row both SCPs allow, and the request is still denied. SCPs limit a member account's root user; they don't",
        "apply to the management account. From the AWS Organizations User Guide (SCPs; SCP examples), checked 2026-10-24.",
        "The bakery's accounts and policies are made up for teaching.",
    ]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg("09-05-scp-ceiling.svg", w, y + 14,
        "Five requests checked against two SCPs and an IAM policy",
        "A grid for the bakery's German member account. Columns: the root SCP, which denies stopping or deleting "
        "CloudTrail trails; the Germany OU SCP, which denies Regions outside Europe with global services exempt; "
        "the person's IAM policy; and the result. Row 1, an admin launches a server in Europe (Frankfurt): root SCP "
        "allows, OU SCP allows, IAM allows; allowed. Row 2, an admin launches a server in US East (N. Virginia): "
        "root SCP allows, OU SCP blocks, IAM allows; denied by the OU SCP. Row 3, an admin stops the CloudTrail "
        "trail: root SCP blocks; denied by the root SCP. Row 4, the account's root user stops the trail: root SCP "
        "blocks, and root needs no IAM policy; denied by the root SCP. Row 5, a new user with no policies reads a "
        "bucket in Frankfurt: both SCPs allow, but no IAM policy allows it; denied by default. A note says a "
        "request passes only if every SCP above the account allows it and an IAM policy grants it.",
        body, style=STYLE)


def compare(name, title, sub, cols, rows, hi_row, note, svg_title, desc):
    """Two comparison columns on labeled rows, with one row highlighted."""
    w = 680
    body = [f'<text class="title" x="16" y="28">{title}</text>', f'<text class="sub" x="16" y="48">{sub}</text>']
    lw, cw, gap = 150, 250, 8
    xs = [16 + lw + i * (cw + gap) for i in range(2)]
    y = 66
    for x, (cname, _) in zip(xs, cols):
        rect(body, "n", x, y, cw, 32)
        body.append(f'<text class="cellt" x="{x + 10}" y="{y + 21}">{cname}</text>')
    y += 40
    for r, row in enumerate(rows):
        hi = r == hi_row
        cells = [wrap(c[1][r], 30 if hi else 34) for c in cols]
        label = wrap(row, 20)
        h = 14 + 15 * max(max(len(c) for c in cells), len(label)) + 6
        if hi:
            for x in xs:
                rect(body, "ok", x - 4, y + 2, cw + 8, h - 4, 5)
        body.append(f'<line class="grid" x1="16" x2="{xs[1] + cw}" y1="{y}" y2="{y}"/>')
        text_lines(body, 16, y + 19, label, cls="rowl", dy=15)
        for x, c in zip(xs, cells):
            text_lines(body, x + 10, y + 19, c, cls="cellt" if hi else "small", dy=15)
        y += h
    body.append(f'<line class="grid" x1="16" x2="{xs[1] + cw}" y1="{y}" y2="{y}"/>')
    y += 22
    for line in note:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg(name, w, y + 14, svg_title, desc, body, style=STYLE)


def scp_vs_iam():
    compare(
        "09-05-scp-vs-iam.svg",
        "SCP or IAM policy: a ceiling or a key",
        "Both use almost the same policy language; read across a row to see how they differ",
        [("Service control policy (SCP)",
          ["In AWS Organizations, from the management account (or an account it delegates to)",
           "Every IAM user and role in the member accounts below where it's attached",
           "Never: it only sets the maximum",
           "Limited by it",
           "Not affected",
           "Organization-wide rules, such as allowed Regions or protecting logs"]),
         ("IAM policy",
          ["Inside one account, in IAM",
           "The one identity or resource it's attached to",
           "Yes: it grants (or denies) permissions",
           "Not limited by IAM policies",
           "Works there as in any account",
           "Giving one person or program the access its job needs"])],
        ["Where it's set", "What it applies to", "Grants permissions?", "A member account's root user",
         "The management account", "Typical use"],
        2,
        ["From the AWS Organizations User Guide (service control policies) and the IAM User Guide, checked 2026-10-24."],
        "Service control policy compared with IAM policy",
        "Two columns, SCP and IAM policy, compared on six rows. Where it's set: in AWS Organizations, from the "
        "management account or an account it delegates to; inside one account, in IAM. What it applies to: every "
        "IAM user and role in the member accounts below where it's attached; the one identity or resource it's "
        "attached to. Grants permissions, highlighted: never, it only sets the maximum; yes, it grants or denies "
        "permissions. A member account's root user: limited by an SCP; not limited by IAM policies. The management "
        "account: not affected by SCPs; IAM policies work there as in any account. Typical use: organization-wide "
        "rules such as allowed Regions or protecting logs; giving one person or program the access its job needs.")


def orgs_vs_control_tower():
    compare(
        "09-05-orgs-vs-control-tower.svg",
        "AWS Organizations or AWS Control Tower: the building or the contractor",
        "Control Tower is built on Organizations; read across a row to see what it adds",
        [("AWS Organizations",
          ["The foundation for grouping and governing accounts",
           "You design the OUs and write the policies",
           "Accounts, OUs, SCPs, RCPs and other policies, one consolidated bill",
           "Enforces its policies; doesn't report on resource settings",
           "You want one bill and your own policies"]),
         ("AWS Control Tower",
          ["A setup and governance layer built on Organizations, Service Catalog and IAM Identity Center",
           "It sets up a best-practice landing zone for you",
           "Preventive, detective and proactive controls; Account Factory; a dashboard",
           "Detective controls find and report resources that break the rules",
           "You want a governed multi-account setup quickly"])],
        ["What it is", "Who designs the structure", "What it provides", "Watching for drift", "Choose it when"],
        0,
        ["From the AWS Organizations User Guide and the AWS Control Tower User Guide (what it is; how controls work),",
         "checked 2026-10-24."],
        "AWS Organizations compared with AWS Control Tower",
        "Two columns, AWS Organizations and AWS Control Tower, compared on five rows. What it is, highlighted: the "
        "foundation for grouping and governing accounts; a setup and governance layer built on Organizations, "
        "Service Catalog and IAM Identity Center. Who designs the structure: you design the OUs and write the "
        "policies; Control Tower sets up a best-practice landing zone for you. What it provides: accounts, OUs, "
        "SCPs, RCPs and other policies, and one consolidated bill; preventive, detective and proactive controls, "
        "Account Factory and a dashboard. Watching for drift: Organizations enforces its policies but doesn't "
        "report on resource settings; Control Tower's detective controls find and report resources that break the "
        "rules. Choose it when: you want one bill and your own policies; you want a governed multi-account setup "
        "quickly.")


if __name__ == "__main__":
    two_halves()
    scp_ceiling()
    scp_vs_iam()
    orgs_vs_control_tower()
