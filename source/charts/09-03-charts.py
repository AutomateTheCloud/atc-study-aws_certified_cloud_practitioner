#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 09.03 (finding threats and weaknesses) as SVG.

Usage: python3 -I source/charts/09-03-charts.py
Writes images/09-03-*.svg. Facts come from AWS pages cited in
guide/09-protecting-and-governing/03-finding-threats-and-weaknesses.md, read
2026-10-24:
- What is Amazon GuardDuty? (threat detection; foundational data sources are
  CloudTrail management events, VPC flow logs and DNS logs, used without turning
  anything else on; findings; 30-day free trial);
- What is Amazon Inspector? (vulnerability management; discovers and continually
  scans EC2 instances, container images in Amazon ECR and Lambda functions for
  software vulnerabilities and unintended network exposure; no scheduled
  assessments);
- Introduction to AWS Security Hub CSPM (checks against FSBP, CIS, PCI DSS and
  NIST; security scores; receives findings from GuardDuty, Inspector, Macie and
  partner products; needs AWS Config recording for most controls; 30-day trial);
- Introduction to AWS Security Hub (unified; correlates Security Hub CSPM,
  Inspector, GuardDuty, Macie and IAM Access Analyzer signals into exposure
  findings; attack path graph) and the Security Hub FAQ (Security Hub CSPM was
  previously known as Security Hub; enabling Security Hub enables Security Hub
  CSPM; the unified product does not itself require Config);
- What is Amazon Detective? (investigates findings and root cause; up to a year
  of history; builds a behavior graph from CloudTrail, VPC flow logs and
  GuardDuty findings);
- AWS Trusted Advisor (Basic Support: Service Limits plus selected Security and
  Fault tolerance checks, refreshed by hand; full checks with Business Support+,
  Enterprise or Unified Operations).
The bakery is made up for teaching. Our own design: no AWS logos, icons, trade
dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Slot 1 (blue) tint marks the one highlighted element; everything else is neutral.
STYLE = make_style(
    light_extra=" --hi-fill:#d9e8fb; --n-fill:#f1f0ec; --alt-fill:#fbe1d6;",
    dark_extra=" --hi-fill:#1b3554; --n-fill:#252523; --alt-fill:#4d2716;",
    rules_extra="""
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 2; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .alt { fill: var(--alt-fill); stroke: var(--s2); stroke-width: 1.5; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .panel { fill: none; stroke: var(--axis); stroke-width: 1; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .q { fill: var(--ink); font-size: 12.5px; font-style: italic; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .tag { fill: var(--ink); font-size: 11.5px; font-weight: 600; letter-spacing: 0.4px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }
  .time { stroke: var(--ink); stroke-width: 2; fill: none; }""")

CH = 6.3  # rough width of one 12px character, for wrapping


def arrow(body, x1, y1, x2, y2):
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def card_lines(w, lines, bullets=False):
    """Wrap a card's lines; with bullets, each item starts with a bullet and items get a small gap."""
    out = []
    for ln in lines:
        parts = wrap(ln, int((w - (34 if bullets else 20)) / CH))
        for j, part in enumerate(parts):
            out.append(("\u2022 " if bullets and j == 0 else "") + part if not bullets or j == 0 else part)
        if bullets:
            out.append(None)
    return out


def card(body, cls, x, y, w, title, lines, h=None, bullets=False):
    """A box with a bold title and wrapped lines of text; returns its height."""
    wrapped = card_lines(w, lines, bullets)
    n = sum(1 for ln in wrapped if ln is not None)
    gaps = sum(1 for ln in wrapped if ln is None)
    need = 30 + 15 * n + 5 * gaps + 8
    if h is None:
        h = need
    body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    body.append(f'<text class="boxt" x="{x + 10}" y="{y + 20}">{title}</text>')
    ty = y + 38
    for ln in wrapped:
        if ln is None:
            ty += 5
            continue
        indent = 0 if (not bullets or ln.startswith("\u2022")) else 11
        body.append(f'<text class="cells" x="{x + 10 + indent}" y="{ty:.1f}">{ln}</text>')
        ty += 15
    return h


def before_during_after():
    """Big picture: which service answers which question, before, during and after an attack."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Weaknesses before, threats during, investigation after</text>',
        '<text class="sub" x="16" y="48">Each detection service answers a different question; all of them report, none of them blocks</text>',
    ]
    # Time arrow.
    body.append('<line class="time" x1="16" y1="78" x2="656" y2="78"/>')
    body.append('<path class="arrowhead" d="M664,78 L654,73 L654,83 Z"/>')
    cols = [
        ("BEFORE AN ATTACK", "Is there a hole?", [
            ("Trusted Advisor", ["Best-practice checks on the account; a few security checks free on Basic Support. Its results stay in its own console"]),
            ("Amazon Inspector", ["Known software flaws and unintended network exposure in EC2 instances, Lambda functions and container images"]),
        ]),
        ("DURING", "Is someone at it now?", [
            ("Amazon GuardDuty", ["Suspicious activity found in CloudTrail events, VPC Flow Logs and DNS logs: stolen credentials, crypto mining, calls from known bad addresses"]),
        ]),
        ("AFTER", "How did it happen?", [
            ("Amazon Detective", ["Starts from a finding and investigates it: what happened, what else was touched, using up to a year of history"]),
        ]),
    ]
    cw, gap, x0, top = 196, 26, 16, 96
    bottoms, boxes = [], {}
    for i, (tag, q, items) in enumerate(cols):
        x = x0 + i * (cw + gap)
        body.append(f'<text class="tag" x="{x}" y="{top + 4}">{tag}</text>')
        body.append(f'<text class="q" x="{x}" y="{top + 24}">{q}</text>')
        y = top + 36
        for title, lines in items:
            h = card(body, "n", x, y, cw, title, lines)
            boxes[title] = (x, y, h)
            y += h + 10
        bottoms.append(y)
    yb = max(bottoms) + 30
    # Findings flow from Inspector and GuardDuty down to Security Hub.
    for name in ("Amazon Inspector", "Amazon GuardDuty"):
        bx, by, bh = boxes[name]
        cx = bx + cw / 2
        arrow(body, cx, by + bh + 2, cx, yb - 2)
        body.append(f'<text class="small" x="{cx + 8}" y="{yb - 10}">findings</text>')
    # Detective starts from a GuardDuty finding.
    gx, gy, gh = boxes["Amazon GuardDuty"]
    dx, dy, dh = boxes["Amazon Detective"]
    arrow(body, gx + cw + 2, gy + 30, dx - 2, dy + 30)
    h = 82
    body.append(f'<rect class="hi" x="16" y="{yb}" width="{w - 32}" height="{h}" rx="6"/>')
    body.append(f'<text class="boxt" x="28" y="{yb + 22}">AWS Security Hub: where the findings meet</text>')
    text_lines(body, 28, yb + 40, [
        "Security Hub CSPM (the original Security Hub) runs its own checks of your settings against standards such",
        "as CIS and PCI DSS, collects the other services' findings in one place, and scores you. The newer, unified",
        "Security Hub correlates them into exposures: which problems combine into real risk.",
    ], cls="cells", dy=15)
    y = yb + h + 22
    y = text_lines(body, 16, y, [
        "Amazon Macie (lesson 09.02) also sends its findings here: sensitive data in S3. From the AWS documentation for",
        "each service, checked 2026-10-24. Trusted Advisor's checks depend on your Support plan.",
    ], cls="note", dy=15)
    svg("09-03-before-during-after.svg", w, y + 4,
        "Which AWS detection service answers which question, before, during and after an attack",
        "A time line runs left to right in three columns. Before an attack, the question is: is there a hole? "
        "Trusted Advisor runs best-practice checks on the account, a few security checks free on Basic Support, and "
        "its results stay in its own console. Amazon Inspector finds known software flaws and unintended network "
        "exposure in EC2 instances, Lambda functions and container images. During an attack, the question is: is someone at it now? Amazon GuardDuty finds "
        "suspicious activity in CloudTrail events, VPC Flow Logs and DNS logs, such as stolen credentials, crypto "
        "mining and calls from known bad addresses. After, the question is: how did it happen? Amazon Detective "
        "starts from a finding, shown by an arrow from GuardDuty, and investigates it using up to a year of "
        "history. Arrows labeled findings lead down from Inspector and GuardDuty to a highlighted band: AWS "
        "Security Hub, where the findings meet. Security Hub CSPM, the original Security Hub, runs its own checks "
        "of your settings against standards such as CIS and PCI DSS, collects the other services' findings in one "
        "place and scores you; the newer unified Security Hub correlates them into exposures. Macie's findings about sensitive data in S3 also arrive there.",
        body, style=STYLE)


if __name__ == "__main__":
    before_during_after()
