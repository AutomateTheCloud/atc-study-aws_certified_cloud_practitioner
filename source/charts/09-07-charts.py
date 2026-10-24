#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphic for Lab 12 (answer the auditor) as SVG.

Usage: python3 -I source/charts/09-07-charts.py
Writes images/09-07-event-record.svg: a simplified CloudTrail event record for DeleteVpc with
labels for what each field tells an auditor. Field names (userIdentity, userName, eventTime,
eventSource, eventName, awsRegion, sourceIPAddress, requestParameters) are CloudTrail's, from
the AWS CloudTrail User Guide ("CloudTrail record contents", sign-in event examples), retrieved
2026-10-24. The values are made up; 198.51.100.0/24 is a range reserved for documentation.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg  # noqa: E402

STYLE = make_style(
    light_extra=" --card:#f4f3ef; --tag:#d9e8fb;",
    dark_extra=" --card:#232322; --tag:#1b3554;",
    rules_extra="""
  .card { fill: var(--card); stroke: var(--axis); stroke-width: 1; }
  .code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; fill: var(--ink); font-size: 12.5px; }
  .tag { fill: var(--tag); stroke: var(--s1); stroke-width: 1.2; }
  .tagt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .note { fill: var(--muted); font-size: 11.5px; }""")


def event_record():
    w, h = 680, 456
    body = [
        '<text class="title" x="16" y="28">What one CloudTrail event record tells an auditor</text>',
        '<text class="sub" x="16" y="48">A shortened DeleteVpc record. Real records hold more fields; these values are made up.</text>',
        '<rect class="card" x="16" y="66" width="430" height="338" rx="8"/>',
    ]
    lines = [
        ("{", None),
        ('  "userIdentity": {', None),
        ('    "type": "IAMUser",', None),
        ('    "userName": "lab-admin"', "Who did it"),
        ("  },", None),
        ('  "eventTime": "2026-10-17T14:32:08Z",', "When (UTC)"),
        ('  "eventSource": "ec2.amazonaws.com",', "Which service"),
        ('  "eventName": "DeleteVpc",', "What they did"),
        ('  "awsRegion": "us-east-1",', "In which Region"),
        ('  "sourceIPAddress": "198.51.100.7",', "From where"),
        ('  "requestParameters": {', None),
        ('    "vpcId": "vpc-0abc1234example"', "To which resource"),
        ("  }", None),
        ("}", None),
    ]
    y = 88
    for text, label in lines:
        body.append(f'<text class="code" x="30" y="{y:.1f}" xml:space="preserve">{text}</text>')
        if label:
            body.append(f'<line class="lead" x1="440" y1="{y - 4:.1f}" x2="470" y2="{y - 4:.1f}"/>')
            body.append(f'<rect class="tag" x="470" y="{y - 15:.1f}" width="190" height="21" rx="4"/>')
            body.append(f'<text class="tagt" x="480" y="{y:.1f}">{label}</text>')
        y += 23.5
    body.append('<text class="note" x="16" y="428">Your own record shows your user name, your VPC ID and your IP address. '
                'Keep the IP address out of anything you share.</text>')
    svg("09-07-event-record.svg", w, h,
        "A simplified CloudTrail event record for DeleteVpc, with labels for who, when, which service, what, which Region, from where and which resource",
        "A shortened JSON event record. userIdentity with type IAMUser and userName lab-admin is labeled 'Who did it'. "
        "eventTime 2026-10-17T14:32:08Z is labeled 'When (UTC)'. eventSource ec2.amazonaws.com is labeled 'Which "
        "service'. eventName DeleteVpc is labeled 'What they did'. awsRegion us-east-1 is labeled 'In which Region'. "
        "sourceIPAddress 198.51.100.7 is labeled 'From where'. requestParameters with vpcId vpc-0abc1234example is "
        "labeled 'To which resource'. A note says your own record shows your user name, VPC ID and IP address, and "
        "to keep the IP address out of anything you share.",
        body, style=STYLE)


if __name__ == "__main__":
    event_record()
