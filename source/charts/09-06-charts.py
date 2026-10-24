#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 09.06 (a defense map) as SVG.

Usage: python3 -I source/charts/09-06-charts.py
Writes images/09-06-*.svg. The layers and their controls summarize lessons 04.01, 05.02,
06.02, 07.01 to 07.03 and 09.01 to 09.05. Facts come from AWS pages checked 2026-10-24:
the Well-Architected security design principles ("Apply security at all layers"), the
Shared Responsibility Model page, the AWS WAF developer guide (Shield Standard: automatic,
no additional charge, common network and transport layer attacks; WAF: rules on HTTP(S)
requests, rate-based rules; Firewall Manager needs AWS Organizations), the GuardDuty user
guide (threat detection from CloudTrail, VPC Flow Logs and DNS logs), the Macie user guide
(sensitive data and bucket access in S3) and the AWS Organizations user guide (SCPs; an
organization trail member accounts can't turn off). The bakery is made up for teaching.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Stops = slot 1 (blue) tint; finds = slot 2 (orange) tint; limits = neutral.
# Every cell also starts with the word STOPS, FINDS or LIMITS.
STYLE = make_style(
    light_extra=" --ok-fill:#d9e8fb; --no-fill:#fbe1d6; --n-fill:#f1f0ec;",
    dark_extra=" --ok-fill:#1b3554; --no-fill:#4d2716; --n-fill:#252523;",
    rules_extra="""
  .ok { fill: var(--ok-fill); stroke: var(--s1); stroke-width: 1.5; }
  .no { fill: var(--no-fill); stroke: var(--s2); stroke-width: 1.5; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .watch { fill: var(--no-fill); stroke: var(--s2); stroke-width: 2; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .tiny { fill: var(--ink); font-size: 11px; }
  .zlab { fill: var(--muted); font-size: 12px; }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .key { fill: var(--muted); font-size: 10px; font-weight: 700; letter-spacing: 0.5px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }""")


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


LAYERS = [
    ("1  Edge", "where traffic reaches AWS", "Route 53, CloudFront, Shield Standard and Advanced, AWS WAF"),
    ("2  Network", "the bakery's VPC", "Public and private subnets, route tables, network ACLs, security groups"),
    ("3  Compute", "servers and functions", "Patched images and guest operating systems, Amazon Inspector scans"),
    ("4  Data", "what is stored and sent", "Encryption with KMS keys and ACM certificates, S3 Block Public Access and versioning, Macie, backups"),
    ("5  Identity and account", "who can do what", "IAM least privilege, MFA, roles instead of access keys, root user protection"),
    ("6  Organization", "rules over every account", "Separate accounts, SCPs, Control Tower controls, Firewall Manager"),
]
WATCH = ["CloudTrail", "AWS Config", "CloudWatch", "GuardDuty", "Security Hub"]


def defense_map():
    """Big picture: six nested layers, with a 'watch and prove' band across all of them."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">A defense map: six layers, and a watch across all of them</text>',
        '<text class="sub" x="16" y="48">From the internet (top) to the organization (bottom), with the controls at each layer</text>',
    ]
    top = 92
    body.append('<text class="zlab" x="16" y="78">The internet: customers, bots and attackers</text>')
    lx, lw = 16, 500
    bh, gap = 66, 8
    for i, (name, sub, ctrl) in enumerate(LAYERS):
        y = top + i * (bh + gap)
        inset = i * 6
        rect(body, "n", lx + inset, y, lw - 2 * inset, bh, 6)
        body.append(f'<text class="cellt" x="{lx + inset + 12}" y="{y + 22}">{name}</text>')
        body.append(f'<text class="zlab" x="{lx + inset + 12}" y="{y + 40}">{sub}</text>')
        text_lines(body, lx + 206, y + 22, wrap(ctrl, 40), cls="small", dy=15)
    h = len(LAYERS) * (bh + gap) - gap
    wx, ww = 530, 134
    rect(body, "watch", wx, top, ww, h, 8)
    body.append(f'<text class="cellt" x="{wx + ww / 2}" y="{top + 26}" text-anchor="middle">Watch and prove</text>')
    body.append(f'<text class="zlab" x="{wx + ww / 2}" y="{top + 44}" text-anchor="middle">across every layer</text>')
    y = top + 84
    for s in WATCH:
        body.append(f'<text class="cellt" x="{wx + ww / 2}" y="{y}" text-anchor="middle">{s}</text>')
        y += 30
    text_lines(body, wx + ww / 2, y + 10, ["records, findings", "and alarms that", "show what got", "through"], cls="zlab", dy=15, anchor="middle")
    y = top + h + 26
    for line in [
        "Each layer is drawn inside the one above it. Lessons: 07.01 to 07.03 and 09.04 (edge and network),",
        "Module 06 and 09.03 (compute), 05.02 and 09.02 (data), Module 04 and 09.01 (identity and account),",
        "09.05 (organization). The bakery is made up for teaching.",
    ]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg("09-06-defense-map.svg", w, y + 14,
        "Six security layers from the edge to the organization, with a watch across all of them",
        "Six bands, each drawn slightly inside the one above, from the internet at the top to the organization at "
        "the bottom. 1, Edge, where traffic first reaches AWS: Route 53, CloudFront, Shield Standard and Advanced, "
        "AWS WAF. 2, Network, the bakery's VPC: public and private subnets, route tables, network ACLs, security "
        "groups. 3, Compute, servers and functions: patched images and guest operating systems, Amazon Inspector "
        "scans. 4, Data, what is stored and sent: encryption with KMS keys and ACM certificates, S3 Block Public "
        "Access and versioning, Macie, backups. 5, Identity and account, who can do what: IAM least privilege, MFA, "
        "roles instead of access keys, root user protection. 6, Organization, rules over every account: separate "
        "accounts, SCPs, Control Tower controls, Firewall Manager. A highlighted vertical band on the right, "
        "labeled watch and prove across every layer, lists CloudTrail, AWS Config, CloudWatch, GuardDuty and "
        "Security Hub: records, findings and alarms that show what got through.",
        body, style=STYLE)


COLS = ["Edge", "Network", "Compute", "Data", "Identity, account", "Organization", "Finds it"]
# Each threat: {column index: (kind, text)}; kind is stop, limit or find.
THREATS = [
    ("Network flood", {0: ("stop", "Shield Standard"), 1: ("limit", "Only needed ports open"),
                       6: ("find", "CloudWatch metrics")}),
    ("HTTP request flood", {0: ("stop", "WAF rate-based rule"), 2: ("limit", "Auto Scaling absorbs load"),
                            6: ("find", "CloudWatch alarm")}),
    ("SQL injection on the order form", {0: ("stop", "WAF managed rules"), 2: ("stop", "Own code checks input"),
                                         6: ("find", "WAF logs")}),
    ("Stolen access key", {4: ("stop", "MFA, no long-term keys"), 5: ("limit", "SCP caps what it can do"),
                           6: ("find", "GuardDuty, CloudTrail")}),
    ("Unpatched web server", {1: ("limit", "Few ports reachable"), 2: ("stop", "Regular patching"),
                              6: ("find", "Inspector")}),
    ("Bucket made public by mistake", {3: ("stop", "Block Public Access"), 5: ("stop", "Org-wide Block Public Access"),
                                       6: ("find", "Macie, Config rule")}),
    ("Trail switched off to hide activity", {5: ("stop", "SCP, organization trail"),
                                             6: ("find", "CloudTrail records the attempt")}),
]
KIND = {"stop": ("ok", "STOPS"), "limit": ("n", "LIMITS"), "find": ("no", "FINDS")}


def threat_grid():
    """Seven threats against six layers plus detection: where each is stopped, limited and found."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Cover every threat twice: a layer that stops it, a control that finds it</text>',
        '<text class="sub" x="16" y="48">Seven threats to the bakery, against the six layers and the watch</text>',
    ]
    lw = 104
    cw, gap = 74, 4
    xs = [16 + lw + i * (cw + gap) for i in range(len(COLS))]
    top = 92
    for x, c in zip(xs, COLS):
        text_lines(body, x + cw / 2, top - 22, wrap(c, 10), cls="rowl", dy=14, anchor="middle")
    rh = 76
    for r, (threat, cells) in enumerate(THREATS):
        y = top + r * (rh + 4)
        body.append(f'<line class="grid" x1="16" x2="664" y1="{y - 2}" y2="{y - 2}"/>')
        text_lines(body, 16, y + 22, wrap(threat, 14), cls="small", dy=15)
        for i, (kind, text) in cells.items():
            cls, label = KIND[kind]
            x = xs[i]
            rect(body, cls, x, y + 2, cw, rh - 4, 5)
            body.append(f'<text class="key" x="{x + 6}" y="{y + 16}">{label}</text>')
            text_lines(body, x + 6, y + 30, wrap(text, 10), cls="tiny", dy=13)
    y = top + len(THREATS) * (rh + 4) + 4
    body.append(f'<line class="axis" x1="16" x2="664" y1="{y - 2}" y2="{y - 2}"/>')
    y += 18
    for line in [
        "STOPS: a preventive control blocks it. LIMITS: a control shrinks the damage or the exposure. FINDS: a detective",
        "control reports it. Lessons 07.02, 09.01 to 09.05. The bakery is made up for teaching.",
    ]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg("09-06-threat-grid.svg", w, y + 14,
        "Seven threats, the layers that stop or limit them, and the controls that find them",
        "A grid. Rows are seven threats; columns are the six layers (edge, network, compute, data, identity and "
        "account, organization) and a last column, finds it. Each filled cell starts with STOPS, LIMITS or FINDS. "
        "Network flood: edge stops it with Shield Standard; network limits it, only needed ports open; found by "
        "CloudWatch metrics. HTTP request flood: edge stops it with a WAF rate-based rule; compute limits it, Auto "
        "Scaling absorbs load; found by a CloudWatch alarm. SQL injection on the order form: edge stops it with WAF "
        "managed rules; compute stops it, the bakery's own code checks input; found in WAF logs. Stolen access key: "
        "identity and account stops it with MFA and no long-term keys; organization limits it, an SCP caps what it "
        "can do; found by GuardDuty and CloudTrail. Unpatched web server: network limits it, few ports reachable; "
        "compute stops it with regular patching; found by Inspector. Bucket made public by mistake: data stops it "
        "with Block Public Access; organization stops it with organization-wide Block Public Access; found by Macie "
        "and a Config rule. Trail switched off to hide activity: organization stops it with an SCP and an "
        "organization trail; CloudTrail records the attempt.",
        body, style=STYLE)


SPLIT = [
    ("Edge", "Runs the edge network; applies Shield Standard to everyone automatically",
     "Puts CloudFront and Route 53 in front; writes WAF rules; decides on Shield Advanced", False),
    ("Network", "Runs the physical network; keeps each VPC isolated",
     "Designs subnets and routes; writes security group and network ACL rules", False),
    ("Compute", "Runs hardware and virtualization; for Lambda, also the operating system",
     "Patches EC2 guest operating systems; owns its code and the code's dependencies", False),
    ("Data", "Provides encryption features and key storage",
     "Classifies data; turns on and manages encryption; decides who can read it", True),
    ("Identity and account", "Provides IAM, MFA and the detection services",
     "Decides who gets access; protects the root user; turns detection on", True),
    ("Organization", "Provides Organizations and Control Tower",
     "Designs the accounts; writes SCPs and chooses controls", False),
]


def who_does_what():
    """Shared responsibility recap, layer by layer, with the always-yours cells highlighted."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Who does what at each layer</text>',
        '<text class="sub" x="16" y="48">AWS provides and runs the tools; you choose and configure them</text>',
    ]
    lw, cw, gap = 150, 250, 8
    xs = [16 + lw + i * (cw + gap) for i in range(2)]
    y = 66
    for x, name in zip(xs, ["AWS does (security of the cloud)", "You do (security in the cloud)"]):
        rect(body, "n", x, y, cw, 32)
        body.append(f'<text class="cellt" x="{x + 10}" y="{y + 21}">{name}</text>')
    y += 40
    for layer, aws, you, hi in SPLIT:
        cells = [wrap(aws, 34), wrap(you, 30 if hi else 34)]
        label = wrap(layer, 20)
        h = 14 + 15 * max(len(cells[0]), len(cells[1]), len(label)) + 6
        if hi:
            rect(body, "ok", xs[1] - 4, y + 2, cw + 8, h - 4, 5)
        body.append(f'<line class="grid" x1="16" x2="{xs[1] + cw}" y1="{y}" y2="{y}"/>')
        text_lines(body, 16, y + 19, label, cls="rowl", dy=15)
        text_lines(body, xs[0] + 10, y + 19, cells[0], cls="small", dy=15)
        text_lines(body, xs[1] + 10, y + 19, cells[1], cls="cellt" if hi else "small", dy=15)
        y += h
    body.append(f'<line class="grid" x1="16" x2="{xs[1] + cw}" y1="{y}" y2="{y}"/>')
    y += 22
    for line in [
        "Highlighted: your data and who can reach it are yours on every service. Compliance evidence splits",
        "the same way: AWS's reports in AWS Artifact, your own records for your side. From the Shared",
        "Responsibility Model page, checked 2026-10-24.",
    ]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg("09-06-who-does-what.svg", w, y + 14,
        "What AWS does and what you do at each of the six layers",
        "Six rows, one per layer, and two columns: AWS does, security of the cloud; you do, security in the cloud. "
        "Edge: AWS runs the edge network and applies Shield Standard to everyone automatically; you put CloudFront "
        "and Route 53 in front, write WAF rules and decide on Shield Advanced. Network: AWS runs the physical "
        "network and keeps each VPC isolated; you design subnets and routes and write security group and network "
        "ACL rules. Compute: AWS runs hardware and virtualization, and for Lambda also the operating system; you "
        "patch EC2 guest operating systems and own your code and its dependencies. Data, your cell highlighted: AWS "
        "provides encryption features and key storage; you classify data, turn on and manage encryption, and decide "
        "who can read it. Identity and account, your cell highlighted: AWS provides IAM, MFA and the detection "
        "services; you decide who gets access, protect the root user and turn detection on. Organization: AWS "
        "provides Organizations and Control Tower; you design the accounts, write SCPs and choose controls.",
        body, style=STYLE)


if __name__ == "__main__":
    defense_map()
    threat_grid()
    who_does_what()
