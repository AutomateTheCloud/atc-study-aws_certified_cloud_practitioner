#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 09.02 (encryption) as SVG.

Usage: python3 -I source/charts/09-02-charts.py
Writes images/09-02-*.svg. Facts come from the AWS KMS Developer Guide ("AWS KMS keys":
customer managed, AWS managed and AWS owned keys, who controls each key policy, CloudTrail
logging, rotation, fees; "Rotate AWS KMS keys"), the AWS KMS pricing page ($1 per customer
managed key per month, prorated hourly; the first and second rotations each add $1 per month,
and later rotations add nothing; 20,000 requests a month free across Regions; $0.03 per
10,000 symmetric requests, from the page's example; no fee for AWS managed or AWS owned keys
to exist), the AWS CloudHSM User Guide (single-tenant HSMs you control, user management
outside IAM, not visible to AWS; an hourly fee per HSM, with no rate on the pricing page),
the ACM User Guide and pricing page (public certificates at no cost with integrated services
such as Elastic Load Balancing and CloudFront), the Amazon S3 User Guide (SSE-S3 default
encryption) and the Amazon RDS User Guide (encryption at rest with a KMS key, chosen when the
database is created). All checked 2026-10-24. The bakery is made up for teaching. Our own
design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --rest-fill:#d9e8fb; --n-fill:#f1f0ec;",
    dark_extra=" --rest-fill:#1b3554; --n-fill:#252523;",
    rules_extra="""
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .rest { fill: var(--rest-fill); stroke: var(--s1); stroke-width: 1.5; }
  .zone { fill: none; stroke: var(--axis); stroke-width: 1.2; stroke-dasharray: 6 4; }
  .card { fill: none; stroke: var(--axis); stroke-width: 1; }
  .hl { fill: none; stroke: var(--s1); stroke-width: 2.2; }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .keyl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .key { fill: var(--muted); font-size: 10.5px; font-weight: 600; letter-spacing: 0.5px; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrlab { fill: var(--ink2); font-size: 11.5px; font-style: italic; }
  .flow { stroke: var(--ink2); stroke-width: 2; fill: none; }
  .head-ink { fill: var(--ink2); }
  .spec { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .val { fill: var(--ink); font-size: 13px; font-variant-numeric: tabular-nums; }""")


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


def arrow(body, pts, label=None, lx=None, ly=None, anchor="middle"):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    body.append(f'<path class="flow" d="{d}"/>')
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 9 * math.cos(a) + 5 * math.sin(a), y2 - 9 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 9 * math.cos(a) - 5 * math.sin(a), y2 - 9 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="head-ink" d="M{x2:.1f},{y2:.1f} L{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z"/>')
    if label:
        for i, line in enumerate(label):
            body.append(f'<text class="arrlab" x="{lx}" y="{ly + 14 * i}" text-anchor="{anchor}">{line}</text>')


def big_picture():
    """The bakery's data in transit (arrows) and at rest (shaded stores), with who holds each key."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">The bakery\'s data, moving and stored</text>',
        '<text class="sub" x="16" y="48">Arrows carry data in transit; shaded boxes hold data at rest, each with the key that protects it</text>',
    ]
    # customer
    rect(body, "plain", 16, 150, 92, 64)
    text_lines(body, 62, 176, ["Customer's", "browser"], cls="boxt", dy=16, anchor="middle")
    # AWS zone
    rect(body, "zone", 130, 66, 534, 334, 10)
    body.append('<text class="note" x="142" y="84">The bakery on AWS, US East (N. Virginia)</text>')
    # load balancer
    rect(body, "plain", 150, 140, 112, 84)
    text_lines(body, 206, 162, ["Load balancer"], cls="boxt", anchor="middle")
    text_lines(body, 206, 182, ["TLS certificate", "from ACM"], cls="cells", dy=15, anchor="middle")
    # web server
    rect(body, "plain", 306, 140, 118, 84)
    text_lines(body, 365, 166, ["Web servers", "(EC2)"], cls="boxt", dy=16, anchor="middle")
    # EBS volume under web server
    rect(body, "rest", 306, 276, 118, 92)
    text_lines(body, 365, 298, ["Server disks", "(EBS)"], cls="boxt", dy=16, anchor="middle")
    text_lines(body, 365, 334, ["key: aws/ebs,", "AWS managed"], cls="cells", dy=15, anchor="middle")
    # stores on the right
    stores = [
        (96, "Order database (RDS)", "key: chosen at creation"),
        (196, "Photo bucket (S3)", "SSE-S3: S3's own keys"),
        (296, "Tax archive (S3)", "SSE-KMS: the bakery's own key"),
    ]
    for y, title, key in stores:
        rect(body, "rest", 474, y, 178, 76)
        text_lines(body, 563, y + 24, [title], cls="boxt", anchor="middle")
        text_lines(body, 563, y + 46, wrap(key, 26), cls="cells", dy=15, anchor="middle")
    # arrows in transit
    arrow(body, [(108, 182), (150, 182)], ["HTTPS"], 129, 172)
    arrow(body, [(262, 182), (306, 182)], ["HTTP or", "HTTPS"], 284, 154)
    arrow(body, [(365, 224), (365, 276)])
    arrow(body, [(424, 160), (448, 160), (448, 134), (474, 134)], ["TLS, if you", "require it"], 442, 112, "end")
    arrow(body, [(424, 182), (474, 234)])
    arrow(body, [(424, 204), (448, 204), (448, 334), (474, 334)])
    body.append('<text class="arrlab" x="442" y="262" text-anchor="end">HTTPS</text>')
    y = 424
    y = text_lines(body, 16, y, [
        "In transit: TLS, the protection behind HTTPS, scrambles data on the wire. AWS also encrypts all traffic between",
        "Availability Zones and between Regions on its own network. At rest: every shaded store is encrypted; what",
        "differs is who holds the key and who can see it being used.",
    ], cls="small", dy=17)
    body.append(f'<text class="note" x="16" y="{y + 4}">The bakery is made up for teaching. From the S3, RDS, KMS and ACM user guides, checked 2026-10-24.</text>')
    svg("09-02-big-picture.svg", w, y + 18,
        "The bakery's data in transit and at rest, with the key protecting each store",
        "Left: the customer's browser. An arrow labeled HTTPS runs to a load balancer that holds a TLS certificate "
        "from ACM. An arrow labeled HTTP or HTTPS runs from the load balancer to the web servers on EC2. From the "
        "web servers, arrows run down to the server disks on EBS, encrypted at rest with the AWS managed key aws/ebs; "
        "to the order database on RDS, labeled TLS if you require it, encrypted at rest with a key chosen when the "
        "database is created; to the photo bucket in S3, labeled HTTPS, encrypted with SSE-S3, S3's own keys; and to "
        "the tax archive bucket in S3, encrypted with SSE-KMS and the bakery's own key. The four stores are shaded "
        "as data at rest. A note says that AWS also encrypts all traffic between Availability Zones and between "
        "Regions on its own network.", body, style=STYLE)


if __name__ == "__main__":
    big_picture()
