#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 08.04 (connecting parts, shipping software) as SVG.

Usage: python3 -I source/charts/08-04-charts.py
Writes images/08-04-*.svg. Facts, checked 2026-10-24: Amazon SQS Developer
Guide and FAQ (producers send, consumers poll and delete; retention 4 days by
default, 1 minute to 14 days); Amazon SNS Developer Guide and FAQ (publish to a
topic, pushed to every subscriber; email subscriptions must be confirmed; email
body can't be customized and is meant for internal system alerts, not
marketing; sent from an SNS no-reply address with a display name set per
topic); Amazon EventBridge User Guide (the default event bus receives AWS
service events; rules match event patterns and send to up to five targets);
AWS Step Functions Developer Guide (state machines, retries, choices, human
approval steps); Amazon SES Developer Guide (send from your own verified
addresses and domains; sandbox: verified recipients only, 200 messages per 24
hours, 1 per second, per Region, until production access); AWS CodeBuild and
AWS CodePipeline user guides (CodeBuild compiles, tests and packages; a
pipeline runs source, build, test, approval and deploy stages; CloudFormation
deploy actions; manual approval can notify an SNS topic). The bakery is made up
for teaching. Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --hi-fill:#d9e8fb; --n-fill:#f1f0ec; --o-fill:#fbe1d6;",
    dark_extra=" --hi-fill:#1b3554; --n-fill:#252523; --o-fill:#4d2716;",
    rules_extra="""
  .panel { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .box { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .svc { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 1.5; }
  .orng { fill: var(--o-fill); stroke: var(--s2); stroke-width: 1.5; }
  .slot { fill: var(--s1); }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 700; }
  .mini { fill: var(--ink); font-size: 11.5px; }
  .small { fill: var(--ink2); font-size: 12px; }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .arrlab { fill: var(--ink2); font-size: 11px; font-style: italic; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.4; fill: none; }
  .arrowhead { fill: var(--ink2); }
  .brace { stroke: var(--s1); stroke-width: 2; fill: none; }""")


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


def arrow(body, x1, y1, x2, y2):
    """A straight line with a small head at (x2, y2), horizontal or sloped."""
    import math
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 7 * math.cos(a) + 4 * math.sin(a), y2 - 7 * math.sin(a) - 4 * math.cos(a))
    p2 = (x2 - 7 * math.cos(a) - 4 * math.sin(a), y2 - 7 * math.sin(a) + 4 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def node(body, cls, x, y, w, h, lines):
    rect(body, cls, x, y, w, h, 5)
    yy = y + h / 2 - 7 * (len(lines) - 1) + 4
    text_lines(body, x + w / 2, yy, lines, cls="mini", dy=14, anchor="middle")


# ---------------------------------------------------------------- big picture: five shapes

def shape_queue(body, x, y):
    node(body, "box", x, y + 22, 74, 36, ["Web server"])
    rect(body, "svc", x + 100, y + 22, 92, 36, 5)
    for i in range(4):
        body.append(f'<rect class="slot" x="{x + 110 + i * 19}" y="{y + 31}" width="13" height="18" rx="2"/>')
    body.append(f'<text class="mini" x="{x + 146}" y="{y + 72}" text-anchor="middle">SQS queue</text>')
    node(body, "box", x + 222, y + 22, 74, 36, ["Packing", "worker"])
    arrow(body, x + 75, y + 40, x + 99, y + 40)
    arrow(body, x + 221, y + 40, x + 193, y + 40)
    body.append(f'<text class="arrlab" x="{x + 207}" y="{y + 16}" text-anchor="middle">pulls</text>')
    body.append(f'<text class="arrlab" x="{x + 87}" y="{y + 16}" text-anchor="middle">sends</text>')


def shape_topic(body, x, y):
    node(body, "box", x, y + 26, 74, 36, ["Order", "function"])
    node(body, "svc", x + 100, y + 26, 80, 36, ["SNS topic"])
    subs = ["Owner's email", "Kitchen queue", "Invoice function"]
    for i, s in enumerate(subs):
        sy = y + 2 + i * 30
        node(body, "box", x + 206, sy, 92, 24, [s])
        arrow(body, x + 181, y + 44, x + 205, sy + 12)
    arrow(body, x + 75, y + 44, x + 99, y + 44)
    body.append(f'<text class="arrlab" x="{x + 87}" y="{y + 20}" text-anchor="middle">publishes</text>')


def shape_bus(body, x, y):
    srcs = ["AWS services", "Your apps", "SaaS partners"]
    for i, s in enumerate(srcs):
        sy = y + 2 + i * 30
        node(body, "box", x, sy, 84, 24, [s])
        arrow(body, x + 85, sy + 12, x + 107, y + 44)
    node(body, "svc", x + 108, y + 22, 90, 44, ["Event bus", "+ rules"])
    node(body, "box", x + 222, y + 8, 76, 24, ["Target A"])
    node(body, "box", x + 222, y + 56, 76, 24, ["Target B"])
    arrow(body, x + 199, y + 40, x + 221, y + 20)
    arrow(body, x + 199, y + 48, x + 221, y + 68)


def shape_workflow(body, x, y):
    steps = ["Take", "deposit"], ["Check", "baker"], ["Owner", "approves"], ["Book", "the bake"]
    for i, s in enumerate(steps):
        sx = x + i * 77
        node(body, "svc" if i == 2 else "box", sx, y + 24, 66, 38, list(s))
        if i:
            arrow(body, sx - 10, y + 43, sx - 1, y + 43)
    body.append(f'<text class="arrlab" x="{x + 150}" y="{y + 82}" text-anchor="middle">a state machine: steps in order, with retries and waits</text>')


def shape_email(body, x, y):
    node(body, "box", x, y + 26, 74, 36, ["Order", "website"])
    node(body, "svc", x + 100, y + 26, 80, 36, ["Amazon SES"])
    node(body, "box", x + 206, y + 26, 92, 36, ["Customers'", "inboxes"])
    arrow(body, x + 75, y + 44, x + 99, y + 44)
    arrow(body, x + 181, y + 44, x + 205, y + 44)
    body.append(f'<text class="arrlab" x="{x + 193}" y="{y + 20}" text-anchor="middle">from the bakery\'s domain</text>')


SHAPES = [
    ("Amazon SQS", "A queue", shape_queue, "Work waits until a worker pulls it.",
     "Orders wait for the packing worker, even if it's down for an hour."),
    ("Amazon SNS", "A topic", shape_topic, "One message, pushed to every subscriber.",
     "“Order failed” reaches the owner, the kitchen and invoicing at once."),
    ("Amazon EventBridge", "An event bus", shape_bus, "Events routed by rules on what they say.",
     "“When an EC2 instance stops, tell the owner”; a sales report at 23:00."),
    ("AWS Step Functions", "A workflow", shape_workflow, "Several steps in order, tracked to the end.",
     "A custom cake: deposit, baker, the owner's approval, then the booking."),
    ("Amazon SES", "Email out", shape_email, "Email from your own domain to customers.",
     "The order confirmation each customer receives."),
]


def message_shapes():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Five shapes of message, five services</text>',
        '<text class="sub" x="16" y="48">Look at who sends, who receives and who waits, then pick the service</text>',
    ]
    y = 64
    for name, shape, draw, rule, example in SHAPES:
        h = 108
        rect(body, "panel", 16, y, w - 32, h)
        body.append(f'<text class="head" x="28" y="{y + 22}">{name}</text>')
        body.append(f'<text class="small" x="28" y="{y + 40}">{shape}</text>')
        text_lines(body, 28, y + 62, wrap(rule, 20), cls="cellt", dy=15)
        draw(body, 190, y + 8)
        text_lines(body, 500, y + 30, wrap(example, 24), cls="small", dy=15)
        y += h + 8
    y += 10
    body.append(f'<text class="note" x="16" y="{y}">Our summary of the SQS, SNS, EventBridge, Step Functions and SES developer guides, checked 2026-10-24.</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">The bakery is made up.</text>')
    svg("08-04-message-shapes.svg", w, y + 30, "Five shapes of message: SQS, SNS, EventBridge, Step Functions and SES",
        "Five panels, each with a service, the shape of message it handles, a small diagram and a bakery example. "
        "Amazon SQS, a queue: work waits until a worker pulls it. The web server sends orders into an SQS queue, "
        "and a packing worker pulls them; example: orders wait for the packing worker even if it is down for an "
        "hour. Amazon SNS, a topic: one message pushed to every subscriber. The order function publishes to an SNS "
        "topic, which pushes to the owner's email, a kitchen queue and an invoice function; example: order failed "
        "reaches the owner, the kitchen and invoicing at once. Amazon EventBridge, an event bus: events routed by "
        "rules on what they say. AWS services, your apps and SaaS partners send events to an event bus with rules, "
        "which sends matching events to targets; example: when an EC2 instance stops, tell the owner, and a sales "
        "report at 23:00. AWS Step Functions, a workflow: several steps in order, tracked to the end. Four steps: "
        "take deposit, check baker, owner approves (highlighted), book the bake; a state machine with retries and "
        "waits. Amazon SES, email out: email from your own domain to customers. The order website sends through "
        "Amazon SES to customers' inboxes, from the bakery's own domain; example: the order "
        "confirmation each customer receives.", body, style=STYLE)


# ---------------------------------------------------------------- SNS email vs SES

ROWS = ["Who receives it", "Who it's from", "What it looks like", "Before the first send", "Meant for", "At the bakery"]
COLS = [
    ("Amazon SNS email subscription",
     ["Addresses subscribed to a topic; each owner clicks a confirmation link first",
      "An SNS no-reply address; you set only a display name per topic",
      "Plain text of the message; you can't customize the email body",
      "Create a topic, subscribe the address, wait for the confirmation",
      "Internal alerts to people who asked for them, not marketing",
      "“Orders are failing” to the owner"]),
    ("Amazon SES",
     ["Any recipient once the account leaves the sandbox; before that, only verified addresses",
      "Your own verified address or domain",
      "Whatever you design, such as an HTML receipt with the bakery's logo",
      "Verify your domain; ask for production access (new accounts start in the sandbox, per Region)",
      "Transactional and marketing email to customers",
      "“Your order 1043 is confirmed” to each customer"]),
]


def sns_vs_ses():
    w = 680
    body = [
        '<text class="title" x="16" y="28">An email from SNS is an alert; an email from SES is your mail</text>',
        '<text class="sub" x="16" y="48">Both can put a message in someone\'s inbox. Read across a row to see how they differ.</text>',
    ]
    lw, cw, gap = 140, 254, 8
    xs = [16 + lw + i * (cw + gap) for i in range(2)]
    y = 66
    for i, (x, (name, _)) in enumerate(zip(xs, COLS)):
        rect(body, "svc" if i == 0 else "orng", x, y, cw, 32)
        body.append(f'<text class="cellt" x="{x + 10}" y="{y + 21}">{name}</text>')
    y += 40
    for r, row in enumerate(ROWS):
        cells = [wrap(c[1][r], 36) for c in COLS]
        h = 14 + 15 * max(len(c) for c in cells) + 4
        body.append(f'<line class="grid" x1="16" x2="{xs[1] + cw}" y1="{y}" y2="{y}"/>')
        text_lines(body, 16, y + 19, wrap(row, 18), cls="rowl", dy=15)
        for x, c in zip(xs, cells):
            text_lines(body, x + 10, y + 19, c, cls="small", dy=15)
        y += h
    body.append(f'<line class="grid" x1="16" x2="{xs[1] + cw}" y1="{y}" y2="{y}"/>')
    y += 22
    for line in [
        "SES sandbox, as of 2026-10-24: verified recipients only, at most 200 messages in 24 hours and 1 a second.",
        "From the Amazon SNS and Amazon SES developer guides and the SNS FAQ, checked 2026-10-24.",
    ]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg("08-04-sns-vs-ses.svg", w, y + 14, "An SNS email subscription compared with Amazon SES",
        "Two columns compared on six rows. Who receives it: SNS, addresses subscribed to a topic, each owner clicks "
        "a confirmation link first; SES, any recipient once the account leaves the sandbox, and before that only "
        "verified addresses. Who it's from: SNS, an SNS no-reply address, with only a display name set per topic; "
        "SES, your own verified address or domain. What it looks like: SNS, plain text of the message, the email "
        "body can't be customized; SES, whatever you design, such as an HTML receipt with the bakery's logo. "
        "Before the first send: SNS, create a topic, subscribe the address and wait for the confirmation; SES, "
        "verify your domain and ask for production access, because new accounts start in the sandbox, per Region. "
        "Meant for: SNS, internal alerts to people who asked for them, not marketing; SES, transactional and "
        "marketing email to customers. At the bakery: SNS sends orders are failing to the owner; SES sends your "
        "order 1043 is confirmed to each customer. A note gives the SES sandbox limits as of 2026-10-24: verified "
        "recipients only, at most 200 messages in 24 hours and 1 a second.", body, style=STYLE)


# ---------------------------------------------------------------- the release pipeline

STAGES = [
    ("Source", ["A code change", "is pushed to", "the repository"], "box"),
    ("Build", ["CodeBuild", "compiles, runs", "unit tests, packages"], "svc"),
    ("Test", ["CodeBuild runs", "more tests on", "the package"], "svc"),
    ("Approve", ["The owner", "approves (SNS", "emails her)"], "box"),
    ("Deploy", ["CloudFormation", "updates both", "Regions"], "box"),
]


def pipeline():
    w = 680
    body = [
        '<text class="title" x="16" y="28">CodePipeline runs the release; CodeBuild does the building</text>',
        '<text class="sub" x="16" y="48">The bakery\'s release pipeline: each change goes through every stage in order</text>',
    ]
    bw, gap, x0, y0 = 116, 17, 16, 108
    # The brace for CodePipeline over all stages.
    bx1, bx2 = x0, x0 + 5 * bw + 4 * gap
    body.append(f'<path class="brace" d="M{bx1},{y0 - 12} L{bx1},{y0 - 22} L{bx2},{y0 - 22} L{bx2},{y0 - 12}"/>')
    body.append(f'<text class="cellt" x="{(bx1 + bx2) / 2}" y="{y0 - 30}" text-anchor="middle">AWS CodePipeline: runs the stages in order and stops the release if one fails</text>')
    for i, (name, lines, cls) in enumerate(STAGES):
        x = x0 + i * (bw + gap)
        rect(body, cls, x, y0, bw, 96, 6)
        body.append(f'<text class="head" x="{x + bw / 2}" y="{y0 + 24}" text-anchor="middle">{name}</text>')
        text_lines(body, x + bw / 2, y0 + 46, lines, cls="small", dy=15, anchor="middle")
        if i:
            arrow(body, x - gap + 1, y0 + 48, x - 1, y0 + 48)
    y = y0 + 96 + 30
    for line in [
        "Highlighted: the stages CodeBuild runs. A failed test stops the release before anything reaches customers.",
        "CodeDeploy can also be a deploy step; it exists, but the exam guide lists it as out of scope.",
        "From the AWS CodePipeline and AWS CodeBuild user guides, checked 2026-10-24. The bakery is made up.",
    ]:
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 16
    svg("08-04-pipeline.svg", w, y + 10, "A release pipeline: CodePipeline runs the stages, CodeBuild builds and tests",
        "Five stages in a row, left to right, joined by arrows, under a bracket labeled AWS CodePipeline: runs the "
        "stages in order and stops the release if one fails. Source: a code change is pushed to the repository. "
        "Build, highlighted: CodeBuild compiles, runs unit tests and packages. Test, highlighted: CodeBuild runs "
        "more tests on the package. Approve: the owner approves, and SNS emails her that a release is waiting. "
        "Deploy: CloudFormation updates both Regions. Notes: the highlighted stages are the ones CodeBuild runs; a "
        "failed test stops the release before anything reaches customers; CodeDeploy can also be a deploy step, "
        "but the exam guide lists it as out of scope.", body, style=STYLE)


if __name__ == "__main__":
    message_shapes()
    sns_vs_ses()
    pipeline()
