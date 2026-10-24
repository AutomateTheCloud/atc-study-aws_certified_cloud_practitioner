#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 07.03 (names and the edge) as SVG.

Usage: python3 -I source/charts/07-03-charts.py
Writes images/07-03-*.svg. Facts come from AWS pages cited in
guide/07-connecting-it/03-names-and-the-edge.md, all read 2026-10-23: What is
Amazon Route 53? and Choosing a routing policy (DNS, routing policies, health
checks); What is Amazon CloudFront? and the CloudFront FAQ (edge caching, origins);
What is AWS Global Accelerator? (two static anycast IPv4 addresses, AWS global
network, Regional endpoints, no caching); What is Amazon API Gateway? (API front end
for Lambda and other backends). The bakery's setup is made up for teaching. Our own
design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# In a Region = categorical slot 1 (blue) tint; at the edge = slot 2 (orange) tint;
# people and outside systems = neutral. Every box also says in words where it runs,
# so color is never alone. The highlighted path is solid ink; others are dashed gray.
STYLE = make_style(
    light_extra=" --aws-fill:#d9e8fb; --edge-fill:#fbe1d6; --prem-fill:#f1f0ec;",
    dark_extra=" --aws-fill:#1b3554; --edge-fill:#4d2716; --prem-fill:#252523;",
    rules_extra="""
  .aws { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .edgeb { fill: var(--edge-fill); stroke: var(--s2); stroke-width: 1.5; }
  .prem { fill: var(--prem-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .zone { fill: none; stroke: var(--axis); stroke-width: 1.5; stroke-dasharray: 6 4; }
  .panel { fill: none; stroke: var(--axis); stroke-width: 1; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .q { fill: var(--ink2); font-size: 12px; font-style: italic; }
  .small { fill: var(--ink2); font-size: 12px; }
  .arrlab { fill: var(--ink); font-size: 11.5px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .num { fill: var(--ink); font-size: 11px; font-weight: 700; }
  .numc { fill: var(--surface); stroke: var(--ink); stroke-width: 1.5; }
  .flow { stroke: var(--ink); stroke-width: 2; fill: none; }
  .flowx { stroke: var(--muted); stroke-width: 1.8; fill: none; stroke-dasharray: 6 4; }
  .head-ink { fill: var(--ink); }
  .head-mut { fill: var(--muted); }""")


def arrow(body, pts, dashed=False):
    """A polyline through pts with a filled head at the last point."""
    cls, hcls = ("flowx", "head-mut") if dashed else ("flow", "head-ink")
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    a = math.atan2(y2 - y1, x2 - x1)
    ex, ey = x2 - 8 * math.cos(a), y2 - 8 * math.sin(a)
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts[:-1]) + f" L{ex:.1f},{ey:.1f}"
    body.append(f'<path class="{cls}" d="{d}"/>')
    p1 = (x2 - 10 * math.cos(a) + 5 * math.sin(a), y2 - 10 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 10 * math.cos(a) - 5 * math.sin(a), y2 - 10 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="{hcls}" d="M{x2:.1f},{y2:.1f} L{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z"/>')


def box(body, cls, x, y, w, h, title, lines=(), anchor="middle"):
    body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    tx = x + w / 2 if anchor == "middle" else x + 10
    body.append(f'<text class="boxt" x="{tx}" y="{y + 18}" text-anchor="{anchor}">{title}</text>')
    text_lines(body, tx, y + 34, list(lines), cls="cells", dy=14, anchor=anchor)


def num(body, x, y, n):
    """A numbered callout that matches a numbered step in the lesson text."""
    body.append(f'<circle class="numc" cx="{x}" cy="{y}" r="9"/>')
    body.append(f'<text class="num" x="{x}" y="{y + 4}" text-anchor="middle">{n}</text>')


def request_path():
    """Big picture: a customer's request from a name to an answer, through the edge."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">From a name to an answer: the bakery\'s requests at the edge</text>',
        '<text class="sub" x="16" y="48">Numbers match the steps in the text. Solid: every request. Dashed: only when needed.</text>',
    ]
    # Zones
    body.append('<rect class="zone" x="200" y="66" width="200" height="252" rx="10"/>')
    body.append('<text class="small" x="300" y="84" text-anchor="middle">At edge locations</text>')
    body.append('<rect class="zone" x="430" y="66" width="234" height="352" rx="10"/>')
    body.append('<text class="small" x="547" y="84" text-anchor="middle">In the Region: US East (N. Virginia)</text>')
    # People and outside systems
    box(body, "prem", 16, 150, 150, 58, "Customer", ["browser or phone"])
    box(body, "prem", 16, 338, 150, 58, "Delivery partner", ["its own app"])
    # Edge services
    box(body, "edgeb", 214, 96, 172, 66, "Amazon Route 53", ["DNS: answers", "\"where is it?\""])
    box(body, "edgeb", 214, 220, 172, 84, "Amazon CloudFront", ["edge location near", "the customer; keeps", "copies of content"])
    # Regional services
    box(body, "aws", 444, 96, 206, 52, "S3 photo bucket", ["origin for cake photos"])
    box(body, "aws", 444, 176, 206, 52, "Web server on EC2", ["origin for order pages"])
    box(body, "aws", 444, 268, 206, 52, "Amazon API Gateway", ["the API's front door"])
    box(body, "aws", 444, 350, 206, 52, "Lambda order functions", ["look up the order"])
    # 1 and 2: DNS question and answer
    arrow(body, [(166, 160), (214, 122)])
    num(body, 178, 124, 1)
    arrow(body, [(214, 146), (166, 180)])
    num(body, 204, 180, 2)
    # 3: request to the edge
    arrow(body, [(166, 196), (214, 248)])
    num(body, 174, 236, 3)
    # 4: edge to origins, only when needed
    arrow(body, [(386, 236), (414, 236), (414, 122), (444, 122)], dashed=True)
    arrow(body, [(386, 262), (424, 262), (424, 202), (444, 202)], dashed=True)
    num(body, 404, 250, 4)
    # 5: partner calls the API
    arrow(body, [(166, 367), (418, 367), (418, 294), (444, 294)])
    num(body, 300, 367, 5)
    arrow(body, [(547, 320), (547, 350)])
    y = 440
    y = text_lines(body, 16, y, [
        "1 Where is bakery.example?   2 An address at CloudFront.   3 The request goes to a nearby edge location.",
        "4 The edge fetches from an origin only when it has no fresh copy.   5 A partner's app calls the bakery's API.",
    ], cls="small", dy=17)
    body.append(f'<text class="note" x="16" y="{y + 6}">Orange boxes run at edge locations; blue boxes run in a Region. The bakery\'s setup is made up for teaching.</text>')
    svg("07-03-request-path.svg", w, y + 20,
        "How the bakery's requests flow through Route 53, CloudFront and API Gateway",
        "Three areas from left to right: people and outside systems, edge locations, and the US East (N. Virginia) "
        "Region. Step 1: the customer's browser asks Amazon Route 53, at the edge, where bakery.example is. Step 2: "
        "Route 53 answers with an address at CloudFront. Step 3: the browser sends the page or photo request to "
        "Amazon CloudFront at an edge location near the customer, which keeps copies of content. Step 4, dashed: "
        "only when it has no fresh copy, CloudFront fetches from an origin in the Region, either the S3 photo "
        "bucket or the web server on EC2. Step 5: a delivery partner's app calls Amazon API Gateway in the Region, "
        "which runs the Lambda order functions to look up the order. Orange boxes run at edge locations; blue boxes "
        "run in a Region.", body, style=STYLE)


def mini_user(body, x, y, label):
    body.append(f'<circle class="prem" cx="{x}" cy="{y}" r="9"/>')
    text_lines(body, x, y + 24, label, cls="small", dy=14, anchor="middle")


def routing_policies():
    """Four Route 53 routing policies as small multiples, one question each."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Four Route 53 routing policies, four different questions</text>',
        '<text class="sub" x="16" y="48">Solid arrow: the answer Route 53 gives. Dashed arrow: an answer it doesn\'t give that user.</text>',
    ]
    pw, ph, gap, top = 318, 196, 12, 64
    panels = [
        ("Latency", "Which Region answers this user fastest?"),
        ("Geolocation", "Where is this user? Send them by the rule"),
        ("Failover", "Is the main site healthy? If not, the standby"),
        ("Weighted", "What share goes where? You set the split"),
    ]
    for i, (name, q) in enumerate(panels):
        px = 16 + (i % 2) * (pw + gap)
        py = top + (i // 2) * (ph + gap)
        body.append(f'<rect class="panel" x="{px}" y="{py}" width="{pw}" height="{ph}" rx="8"/>')
        body.append(f'<text class="head" x="{px + 12}" y="{py + 22}">{name}</text>')
        body.append(f'<text class="q" x="{px + 12}" y="{py + 40}">{q}</text>')
        rx, rw, rh = px + 186, 120, 46
        ra, rb = py + 58, py + 128
        if name == "Latency":
            box(body, "aws", rx, ra, rw, rh, "N. Virginia", ["far from this user"])
            box(body, "aws", rx, rb, rw, rh, "Frankfurt", ["lowest delay here"])
            mini_user(body, px + 50, py + 112, ["Customer", "in Munich"])
            arrow(body, [(px + 62, py + 106), (rx, ra + 23)], dashed=True)
            arrow(body, [(px + 62, py + 118), (rx, rb + 23)])
        elif name == "Geolocation":
            box(body, "aws", rx, ra, rw, rh, "N. Virginia", ["everyone else"])
            box(body, "aws", rx, rb, rw, rh, "Frankfurt", ["users in Germany"])
            mini_user(body, px + 50, py + 76, ["Users in the US"])
            mini_user(body, px + 50, py + 136, ["Users in Germany"])
            arrow(body, [(px + 62, py + 76), (rx, ra + 23)])
            arrow(body, [(px + 62, py + 136), (rx, rb + 23)])
            body.append(f'<text class="small" x="{px + 12}" y="{py + 186}">The rule follows the user\'s location.</text>')
        elif name == "Failover":
            box(body, "aws", rx, ra, rw, rh, "Primary", ["fails health check"])
            box(body, "aws", rx, rb, rw, rh, "Standby", ["takes the traffic"])
            mini_user(body, px + 50, py + 112, ["Customer"])
            arrow(body, [(px + 62, py + 106), (rx, ra + 23)], dashed=True)
            arrow(body, [(px + 62, py + 118), (rx, rb + 23)])
            body.append(f'<text class="small" x="{px + 12}" y="{py + 186}">Health checks decide; no person has to act.</text>')
        else:
            box(body, "aws", rx, ra, rw, rh, "Current site", ["90 in 100 users"])
            box(body, "aws", rx, rb, rw, rh, "New version", ["10 in 100 users"])
            mini_user(body, px + 50, py + 112, ["Customers"])
            arrow(body, [(px + 62, py + 106), (rx, ra + 23)])
            arrow(body, [(px + 62, py + 118), (rx, rb + 23)])
            body.append(f'<text class="small" x="{px + 12}" y="{py + 186}">Both answers are used, in proportion.</text>')
    y = top + 2 * ph + gap + 24
    y = text_lines(body, 16, y, [
        "Route 53 only answers with an address; the customer's browser then connects there. Four more policies",
        "(simple, geoproximity, IP-based, multivalue answer) are in the table in the lesson.",
    ], cls="small", dy=17)
    body.append(f'<text class="note" x="16" y="{y + 4}">Our summary of AWS\'s "Choosing a routing policy" page, checked 2026-10-23. Regions are the bakery\'s.</text>')
    svg("07-03-routing-policies.svg", w, y + 18,
        "Four Route 53 routing policies compared as small diagrams",
        "Four panels. Latency: which Region answers this user fastest? A customer in Munich gets Frankfurt, which "
        "has the lowest delay for them, not N. Virginia, which is far away. Geolocation: where is this user? Users "
        "in the US go to N. Virginia and users in Germany go to Frankfurt; the rule follows the user's location. "
        "Failover: is the main site healthy? The primary fails its health check, so the customer is sent to the "
        "standby; health checks decide and no person has to act. Weighted: what share goes where? 90 in 100 "
        "customers go to the current site and 10 in 100 to a new version; both answers are used, in proportion. "
        "A note says Route 53 only answers with an address, and that four more policies, simple, geoproximity, "
        "IP-based and multivalue answer, are in the table in the lesson.", body, style=STYLE)


def cloudfront_vs_ga():
    """Two panels: CloudFront keeps copies at the edge; Global Accelerator carries traffic to a Region."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">CloudFront and Global Accelerator both start at the edge, then differ</text>',
        '<text class="sub" x="16" y="48">The difference to notice: where the answer comes from</text>',
    ]
    pw, top, ph = 318, 64, 384
    for i, name in enumerate(["Amazon CloudFront", "AWS Global Accelerator"]):
        px = 16 + i * (pw + 12)
        body.append(f'<rect class="panel" x="{px}" y="{top}" width="{pw}" height="{ph}" rx="8"/>')
        body.append(f'<text class="head" x="{px + 14}" y="{top + 24}">{name}</text>')
        cx = px + pw / 2
        box(body, "prem", cx - 90, top + 46, 180, 30, "User", [])
        if i == 0:
            box(body, "edgeb", cx - 120, top + 118, 240, 70, "Nearest edge location",
                ["keeps a copy of popular content", "and answers from it when it can"])
            arrow(body, [(cx, top + 76), (cx, top + 118)])
            box(body, "aws", cx - 120, top + 236, 240, 54, "Origin in a Region",
                ["S3 bucket, web server, or API"])
            arrow(body, [(cx - 30, top + 188), (cx - 30, top + 236)], dashed=True)
            body.append(f'<text class="arrlab" x="{cx - 20}" y="{top + 216}">only when no fresh copy</text>')
            lines = ["Web content over HTTP and HTTPS", "Many requests never reach the origin",
                     "A content delivery network (CDN)"]
        else:
            box(body, "edgeb", cx - 120, top + 118, 240, 70, "Nearest edge location",
                ["two fixed IP addresses, announced", "from AWS's edge; no copies kept"])
            arrow(body, [(cx, top + 76), (cx, top + 118)])
            box(body, "aws", px + 14, top + 236, 140, 54, "Region A", ["healthy endpoint"])
            box(body, "aws", px + pw - 154, top + 236, 140, 54, "Region B", ["used if A fails"])
            arrow(body, [(cx - 40, top + 188), (px + 84, top + 236)])
            arrow(body, [(cx + 40, top + 188), (px + pw - 84, top + 236)], dashed=True)
            body.append(f'<text class="arrlab" x="{cx}" y="{top + 224}" text-anchor="middle">AWS network</text>')
            lines = ["Any TCP or UDP traffic: games, voice, IoT", "Every request reaches your application",
                     "Switches Regions without waiting on DNS"]
        yy = top + 320
        for ln in lines:
            body.append(f'<text class="cells" x="{px + 14}" y="{yy}">• {ln}</text>')
            yy += 20
    y = top + ph + 24
    body.append(f'<text class="note" x="16" y="{y}">Our summary of AWS\'s CloudFront and Global Accelerator documentation, checked 2026-10-23.</text>')
    svg("07-03-cloudfront-vs-ga.svg", w, y + 14,
        "Amazon CloudFront compared with AWS Global Accelerator",
        "Two panels. Amazon CloudFront: a user connects to the nearest edge location, which keeps a copy of "
        "popular content and answers from it when it can; a dashed arrow goes to the origin in a Region, an S3 "
        "bucket, web server or API, only when there is no fresh copy. Bullets: web content over HTTP and HTTPS; "
        "many requests never reach the origin; a content delivery network. AWS Global Accelerator: a user connects "
        "to the nearest edge location through two fixed IP addresses announced from AWS's edge, with no copies "
        "kept; traffic travels over the AWS network to a healthy endpoint in Region A, with a dashed arrow to "
        "Region B, used if A fails. Bullets: any TCP or UDP traffic such as games, voice and IoT; every request "
        "reaches your application; switches Regions without waiting on DNS.", body, style=STYLE)


if __name__ == "__main__":
    request_path()
    routing_policies()
    cloudfront_vs_ga()
