#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 12.04 (partners and paid help) as SVG.

Usage: python3 -I source/charts/12-04-charts.py
Writes images/12-04-*.svg. Facts come from AWS pages checked 2026-10-24: the AWS Support FAQ
(Support doesn't include custom code development, software debugging or system
administration); the AWS Training and Certification Blog post "Maximizing your cloud journey:
Engaging an AWS Solutions Architect" (2024-12-19: a free resource, reached through the
account team or the Contact Us form; they refer hands-on build-outs to Professional Services
or partners); the AWS Professional Services page (design, build, migrate and manage AWS
workloads; offerings in AWS Marketplace); the AWS Partner Network, Partner Paths and "Work
with an AWS Partner" pages (third-party companies; the five paths; AWS Partner Solutions
Finder); the AWS Marketplace Buyer Guide (what Marketplace is; Managing costs; Private
Marketplace; Managing licenses). The bakery is made up for teaching. Our own design: no AWS
logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Highlighted = slot 1 (blue) tint; neutral otherwise. Every cell also says what it means in words.
STYLE = make_style(
    light_extra=" --ok-fill:#d9e8fb; --n-fill:#f1f0ec;",
    dark_extra=" --ok-fill:#1b3554; --n-fill:#252523;",
    rules_extra="""
  .ok { fill: var(--ok-fill); stroke: var(--s1); stroke-width: 1.5; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
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


def compare(name, title, sub, cols, rows, hi_row, note, svg_title, desc, w=720):
    """Several comparison columns on labeled rows, with one row highlighted."""
    body = [f'<text class="title" x="16" y="28">{title}</text>', f'<text class="sub" x="16" y="48">{sub}</text>']
    n = len(cols)
    lw, gap = 112, 6
    cw = (w - 32 - lw - gap * (n - 1)) / n
    chars = int(cw / 6.9)
    xs = [16 + lw + i * (cw + gap) for i in range(n)]
    y = 66
    head = [wrap(c[0], chars - 2) for c in cols]
    hh = 14 + 16 * max(len(h) for h in head)
    for x, lines in zip(xs, head):
        rect(body, "n", x, y, cw, hh)
        text_lines(body, x + 8, y + 20, lines, cls="cellt", dy=16)
    y += hh + 8
    for r, row in enumerate(rows):
        hi = r == hi_row
        cells = [wrap(c[1][r], chars - (3 if hi else 0)) for c in cols]
        label = wrap(row, 15)
        h = 14 + 15 * max(max(len(c) for c in cells), len(label)) + 6
        if hi:
            for x in xs:
                rect(body, "ok", x - 2, y + 2, cw + 4, h - 4, 5)
        body.append(f'<line class="grid" x1="16" x2="{xs[-1] + cw}" y1="{y}" y2="{y}"/>')
        text_lines(body, 16, y + 19, label, cls="rowl", dy=15)
        for x, c in zip(xs, cells):
            text_lines(body, x + 8, y + 19, c, cls="cellt" if hi else "small", dy=15)
        y += h
    body.append(f'<line class="grid" x1="16" x2="{xs[-1] + cw}" y1="{y}" y2="{y}"/>')
    y += 22
    for line in note:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg(name, w, y + 14, svg_title, desc, body, style=STYLE)


def four_kinds():
    compare(
        "12-04-four-kinds-of-help.svg",
        "Four kinds of help from people: who does the work?",
        "Read across a row; the highlighted row is the one exam questions turn on",
        [("AWS Support",
          ["AWS's support engineers",
           "Answer cases about problems with AWS services and your account",
           "No: they guide you; they don't write or debug your code or run your systems",
           "Your Support plan; Basic is free",
           "A case in Support Center"]),
         ("AWS solutions architects",
          ["AWS technical advisers on your account team",
           "Advise on design: architecture and Well-Architected reviews",
           "No: they advise, and point you to people who build",
           "No charge",
           "Your account team, or AWS's contact form"]),
         ("AWS Professional Services",
          ["AWS's own consulting experts",
           "Design, build, migrate and manage workloads as a project",
           "Yes: on a project you hire them for",
           "A paid contract; some offerings sold in AWS Marketplace",
           "AWS's contact form, or AWS Marketplace"]),
         ("AWS Partners",
          ["Other companies in the AWS Partner Network",
           "Services partners deliver projects and run systems; software partners sell products",
           "Yes, for services partners, under your contract with them",
           "The partner's own prices; many sell in AWS Marketplace",
           "AWS Partner Solutions Finder, or AWS Marketplace"])],
        ["Who they are", "What they do", "Do the hands-on work?", "What it costs you", "How you reach them"],
        2,
        ["From the AWS Support FAQ, AWS's post on engaging a solutions architect (2024-12-19), and the AWS Professional",
         "Services and AWS Partner Network pages, checked 2026-10-24. Plans and their prices are in lesson 12.01."],
        "AWS Support, solutions architects, Professional Services and partners compared",
        "Four columns compared on five rows. Who they are: AWS Support, AWS's support engineers; solutions "
        "architects, AWS technical advisers on your account team; Professional Services, AWS's own consulting "
        "experts; partners, other companies in the AWS Partner Network. What they do: Support answers cases about "
        "problems with AWS services and your account; solutions architects advise on design, such as architecture "
        "and Well-Architected reviews; Professional Services designs, builds, migrates and manages workloads as a "
        "project; services partners deliver projects and run systems, and software partners sell products. Do the "
        "hands-on work, highlighted: Support, no, they guide you and don't write or debug your code or run your "
        "systems; solutions architects, no, they advise and point you to people who build; Professional "
        "Services, yes, on a project you hire them for; partners, yes for services partners, under your contract "
        "with them. What it costs you: Support, your Support plan, and Basic is free; solutions architects, no "
        "charge; Professional Services, a paid contract, with some offerings sold in AWS Marketplace; partners, "
        "the partner's own prices, and many sell in AWS Marketplace. How you reach them: a case in Support "
        "Center; your account team or AWS's contact form; AWS's contact form or AWS Marketplace; AWS Partner "
        "Solutions Finder or AWS Marketplace.")


PATHS = [
    (True, "Independent software vendor (ISV)", "Older material: \"Technology Partner\"",
     "Software Path", "Software that runs on or works with AWS. Device makers use the Hardware Path"),
    (True, "System integrator", "Older material: \"Consulting Partner\"",
     "Services Path", "Consulting, professional, managed and resale services"),
    (False, "No exam term", "",
     "Training Path", "Companies that sell or deliver AWS training"),
    (False, "No exam term", "",
     "Distribution Path", "Distributors that recruit and support resellers"),
]


def partner_paths():
    w = 680
    body = [
        '<text class="title" x="16" y="28">The exam\'s partner words, and AWS\'s current Partner Paths</text>',
        '<text class="sub" x="16" y="48">The highlighted rows are the two kinds the exam names</text>',
    ]
    body.append('<text class="key" x="16" y="76">THE EXAM SAYS</text>')
    body.append('<text class="key" x="360" y="76">AWS PARTNER PATH TODAY</text>')
    y = 88
    lx, rx, lw, rw = 16, 360, 290, 304
    for hi, term, old, path, what in PATHS:
        tl = wrap(what, 44)
        h = max(30 + (18 if old else 0), 30 + 15 * len(tl)) + 14
        cls = "ok" if hi else "n"
        rect(body, cls, lx, y, lw, h, 8)
        body.append(f'<text class="cellt" x="{lx + 12}" y="{y + 24}">{term}</text>')
        if old:
            body.append(f'<text class="small" x="{lx + 12}" y="{y + 42}">{old}</text>')
        rect(body, cls if hi else "plain", rx, y, rw, h, 8)
        body.append(f'<text class="cellt" x="{rx + 12}" y="{y + 24}">{path}</text>')
        text_lines(body, rx + 12, y + 42, tl, cls="small", dy=15)
        arrow(body, lx + lw + 4, y + h / 2, rx - 4, y + h / 2)
        y += h + 12
    y += 10
    for line in ["From the AWS Partner Paths page, checked 2026-10-24. AWS publishes no table from the exam's words or the old",
                 "partner types to the paths: this pairing, by what each path covers, is ours. Joining the AWS Partner Network",
                 "is free; on the Free plan, joining upgrades the account to the Paid plan."]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg("12-04-partner-paths.svg", w, y + 14,
        "Exam partner terms mapped to AWS's current Partner Paths",
        "Two columns, the exam's words on the left and today's AWS Partner Paths on the right, joined by arrows. "
        "Row 1, highlighted: independent software vendor, ISV, called Technology Partner in older material, maps "
        "to the Software Path, for software that runs on or works with AWS; device makers use the Hardware Path. "
        "Row 2, highlighted: system integrator, called Consulting Partner in older material, maps to the Services "
        "Path, for consulting, professional, managed and resale services. Row 3: no exam term, the Training Path, "
        "for companies that sell or deliver AWS training. Row 4: no exam term, the Distribution Path, for "
        "distributors that recruit and support resellers. A note says the pairing is ours, by what each path covers, "
        "since AWS publishes no table from the old partner types to the paths; joining the AWS Partner Network is "
        "free, and on the Free plan joining upgrades the account to the Paid plan.",
        body, style=STYLE)


def marketplace_jobs():
    compare(
        "12-04-marketplace-three-jobs.svg",
        "AWS Marketplace's three jobs for a buyer",
        "If the bakery buys software for several accounts in one organization",
        [("Cost management",
          ["What is each team spending on Marketplace products?",
           "The Procurement insights dashboard; cost allocation tags in Cost Explorer",
           "Shows costs and agreements across the organization's accounts; tags split usage by team",
           "Tags appear in Cost Explorer only after you activate them"]),
         ("Governance",
          ["Can staff buy only products we've approved?",
           "Private Marketplace",
           "Approved catalogs per organization, OU or account; users can request more, admins approve",
           "Blocks new subscriptions only; it doesn't control what can be deployed"]),
         ("Entitlement",
          ["Who may use what we bought, and where?",
           "Licenses created at subscription; sharing through AWS License Manager",
           "Shares subscriptions with other accounts in the organization; tracks license use",
           "Sharing covers AMI, container, machine learning and data products"])],
        ["The question", "The feature", "What it does", "Its limit"],
        1,
        ["From the AWS Marketplace Buyer Guide (Managing costs, Private Marketplace, Managing licenses), checked 2026-10-24."],
        "AWS Marketplace's cost management, governance and entitlement features compared",
        "Three columns compared on four rows. Cost management: the question, what is each team spending on "
        "Marketplace products; the feature, highlighted, the Procurement insights dashboard and cost allocation "
        "tags in Cost Explorer; what it does, shows costs and agreements across the organization's accounts, and "
        "tags split usage by team; its limit, tags appear in Cost Explorer only after you activate them. "
        "Governance: can staff buy only products we've approved; the feature, Private Marketplace; what it does, "
        "approved catalogs per organization, OU or account, and users can request more for admins to approve; its "
        "limit, it blocks new subscriptions only and doesn't control what can be deployed. Entitlement: who may "
        "use what we bought, and where; the feature, licenses created at subscription, shared through AWS License "
        "Manager; what it does, shares subscriptions with other accounts in the organization and tracks license "
        "use; its limit, sharing covers AMI, container, machine learning and data products.",
        w=680)


if __name__ == "__main__":
    four_kinds()
    partner_paths()
    marketplace_jobs()
