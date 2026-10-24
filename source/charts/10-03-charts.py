#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 10.03 (people, apps and devices) as SVG.

Usage: python3 -I source/charts/10-03-charts.py
Writes images/10-03-*.svg. Facts come from AWS pages cited in
guide/10-data-ai-and-more/03-people-apps-and-devices.md, checked 2026-10-23 and
2026-10-24: the "What is" pages for Amazon WorkSpaces, Amazon WorkSpaces
Applications (formerly AppStream 2.0), Amazon WorkSpaces Secure Browser (and its
availability-change page: closed to new customers from 2026-10-29), Amazon Connect
Customer (formerly Amazon Connect), Amazon SES, AWS Amplify Hosting and AWS IoT
Core; the WorkSpaces FAQ for hourly and monthly billing (hourly = a low monthly
fee plus an hourly usage fee; monthly = a fixed fee for unlimited use). The billing
chart shows the shape only: its numbers are made up and are not AWS prices.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap, line_key  # noqa: E402

# AWS service = slot 1 (blue) tint; people, devices and screens = neutral cards; the
# one highlighted element = slot 2 (orange) outline. Words name every part.
STYLE = make_style(
    light_extra=" --aws-fill:#d9e8fb; --hi-fill:#fbe1d6; --card-fill:#f1f0ec; --scr:#ffffff;",
    dark_extra=" --aws-fill:#1b3554; --hi-fill:#4d2716; --card-fill:#252523; --scr:#2c2c2a;",
    rules_extra="""
  .aws { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .card { fill: var(--card-fill); stroke: var(--axis); stroke-width: 1; }
  .hi { fill: var(--hi-fill); stroke: var(--s2); stroke-width: 2.5; }
  .panel { fill: none; stroke: var(--axis); stroke-width: 1; }
  .scr { fill: var(--scr); stroke: var(--ink2); stroke-width: 1.5; }
  .win { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.2; }
  .winhi { fill: var(--hi-fill); stroke: var(--s2); stroke-width: 1.5; }
  .bar { fill: var(--grid); }
  .boxt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .colh { fill: var(--muted); font-size: 11.5px; font-weight: 600; letter-spacing: 0.5px; }
  .head { fill: var(--ink); font-size: 14px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .tiny { fill: var(--ink2); font-size: 10.5px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .flow { stroke: var(--ink2); stroke-width: 1.8; fill: none; }
  .flowd { stroke: var(--ink2); stroke-width: 1.8; fill: none; stroke-dasharray: 5 4; }
  .head-ink { fill: var(--ink2); }
  .line-s2 { stroke: var(--s2); stroke-width: 2; fill: none; stroke-linecap: round; }
  .ann { fill: var(--ink); font-size: 12px; }
  .band { fill: var(--grid); opacity: 0.6; }""")


def arrow(body, x1, y1, x2, y2, dashed=False):
    a = math.atan2(y2 - y1, x2 - x1)
    ex, ey = x2 - 8 * math.cos(a), y2 - 8 * math.sin(a)
    body.append(f'<path class="{"flowd" if dashed else "flow"}" d="M{x1:.1f},{y1:.1f} L{ex:.1f},{ey:.1f}"/>')
    p1 = (x2 - 10 * math.cos(a) + 5 * math.sin(a), y2 - 10 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 10 * math.cos(a) - 5 * math.sin(a), y2 - 10 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="head-ink" d="M{x2:.1f},{y2:.1f} L{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z"/>')


def box(body, cls, x, y, w, h, title=None, lines=(), anchor="start"):
    body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    tx = x + w / 2 if anchor == "middle" else x + 10
    yy = y + 18
    if title:
        body.append(f'<text class="boxt" x="{tx}" y="{yy}" text-anchor="{anchor}">{title}</text>')
        yy += 16
    text_lines(body, tx, yy, list(lines), cls="cells", dy=14, anchor=anchor)


LANES = [
    ("Staff at a screen", "Seasonal staff, an accountant", [
        ("Amazon WorkSpaces", "a whole desktop"),
        ("WorkSpaces Applications", "one application (AppStream 2.0)"),
        ("WorkSpaces Secure Browser", "one web browser"),
    ]),
    ("Customers", "On the phone, in chat, by email", [
        ("Amazon Connect Customer", "a contact center (Amazon Connect)"),
        ("Amazon SES", "email at scale"),
    ]),
    ("App users", "Website and phone app", [
        ("AWS Amplify", "builds and hosts the front end"),
    ]),
    ("Devices", "Freezer sensors", [
        ("AWS IoT Core", "connects devices; routes messages"),
    ]),
]


def big_picture():
    w = 680
    body = [
        '<text class="title" x="16" y="28">Who is on the other end? Four kinds of user, seven services</text>',
        '<text class="sub" x="16" y="48">Start from who the service is for; then pick the service by what they need.</text>',
    ]
    xw, ww = 16, 196
    xs, ws = 250, 414
    y = 74
    body.append(f'<text class="colh" x="{xw}" y="{y}">WHO</text>')
    body.append(f'<text class="colh" x="{xs}" y="{y}">AWS SERVICE AND WHAT IT GIVES THEM</text>')
    y += 10
    for who, eg, svcs in LANES:
        n = len(svcs)
        lh = n * 40 + (n - 1) * 6
        box(body, "card", xw, y, ww, lh, who, [eg])
        for k, (svc, what) in enumerate(svcs):
            sy = y + k * 46
            body.append(f'<rect class="aws" x="{xs}" y="{sy}" width="{ws}" height="40" rx="6"/>')
            body.append(f'<text class="boxt" x="{xs + 10}" y="{sy + 25}">{svc}</text>')
            body.append(f'<text class="cells" x="{xs + 206}" y="{sy + 25}">{what}</text>')
            arrow(body, xw + ww + 4, y + lh / 2, xs - 2, sy + 20)
        y += lh + 16
    y += 4
    body.append(f'<text class="note" x="16" y="{y}">Exam names in parentheses. Secure Browser closes to new customers on 2026-10-29. Checked 2026-10-24.</text>')
    svg("10-03-big-picture.svg", w, y + 14,
        "Seven services grouped by who is on the other end",
        "Four groups. Staff at a screen, such as seasonal staff or an accountant: Amazon WorkSpaces gives a whole "
        "desktop; WorkSpaces Applications, the exam's AppStream 2.0, gives one application; WorkSpaces Secure "
        "Browser gives one browser and is closed to new customers from 2026-10-29. Customers on the phone, in chat "
        "or by email: Amazon Connect Customer, the exam's Amazon Connect, is a contact center; Amazon SES is email "
        "at scale. App users of the bakery's web and phone app: AWS Amplify builds and hosts the front end. "
        "Devices such as freezer sensors: AWS IoT Core connects devices and routes their messages.",
        body, style=STYLE)


def screen(body, x, y, w, h):
    body.append(f'<rect class="scr" x="{x}" y="{y}" width="{w}" height="{h}" rx="4"/>')


def what_user_sees():
    w = 680
    body = [
        '<text class="title" x="16" y="28">What does the user see? The question that tells the three apart</text>',
        '<text class="sub" x="16" y="48">All three run in AWS and stream only pictures of the screen to the user\'s device.</text>',
    ]
    pw, top, ph, gap = 210, 64, 330, 13
    panels = [
        ("Amazon WorkSpaces", "A whole desktop", ["Their own Windows or", "Linux desktop; any app", "they need, files kept"]),
        ("WorkSpaces Applications", "One application", ["Exam name: AppStream 2.0", "Chosen apps in a window", "or browser tab"]),
        ("WorkSpaces Secure Browser", "One web browser", ["Internal websites and", "web apps only; closed to", "new customers 2026-10-29"]),
    ]
    for i, (name, sees, lines) in enumerate(panels):
        px = 16 + i * (pw + gap)
        body.append(f'<rect class="panel" x="{px}" y="{top}" width="{pw}" height="{ph}" rx="8"/>')
        box(body, "aws", px + 12, top + 12, pw - 24, 44, name, ["runs in AWS"], anchor="middle")
        arrow(body, px + pw / 2, top + 60, px + pw / 2, top + 96)
        body.append(f'<text class="tiny" x="{px + pw / 2 + 8}" y="{top + 82}">pixels only</text>')
        sx, sy, sw, sh = px + 20, top + 100, pw - 40, 112
        screen(body, sx, sy, sw, sh)
        if i == 0:
            body.append(f'<rect class="bar" x="{sx + 2}" y="{sy + sh - 14}" width="{sw - 4}" height="12" rx="2"/>')
            body.append(f'<rect class="win" x="{sx + 10}" y="{sy + 10}" width="90" height="56" rx="3"/>')
            body.append(f'<rect class="win" x="{sx + 60}" y="{sy + 34}" width="96" height="58" rx="3"/>')
            for k in range(3):
                body.append(f'<rect class="bar" x="{sx + 10 + 14 * k}" y="{sy + 74}" width="10" height="10" rx="2"/>')
        elif i == 1:
            body.append(f'<rect class="winhi" x="{sx + 26}" y="{sy + 18}" width="{sw - 52}" height="76" rx="3"/>')
            body.append(f'<text class="tiny" x="{sx + sw / 2}" y="{sy + 60}" text-anchor="middle">stock app</text>')
        else:
            body.append(f'<rect class="win" x="{sx + 12}" y="{sy + 12}" width="{sw - 24}" height="88" rx="3"/>')
            body.append(f'<rect class="bar" x="{sx + 18}" y="{sy + 18}" width="{sw - 36}" height="12" rx="2"/>')
            body.append(f'<text class="tiny" x="{sx + 24}" y="{sy + 28}">https://orders.internal</text>')
        body.append(f'<text class="head" x="{px + pw / 2}" y="{sy + sh + 26}" text-anchor="middle">{sees}</text>')
        text_lines(body, px + pw / 2, sy + sh + 48, lines, cls="small", dy=16, anchor="middle")
    y = top + ph + 22
    body.append(f'<text class="note" x="16" y="{y}">Our summary of the three services\' AWS documentation, checked 2026-10-23 and 2026-10-24.</text>')
    svg("10-03-what-the-user-sees.svg", w, y + 14,
        "What a user sees with WorkSpaces, WorkSpaces Applications and WorkSpaces Secure Browser",
        "Three panels. In each, the service runs in AWS and only pixels, pictures of the screen, stream to the "
        "user's device. Amazon WorkSpaces: the screen shows a whole desktop with a taskbar and several windows; the "
        "user gets their own Windows or Linux desktop with any app they need and files kept. WorkSpaces "
        "Applications, the exam's AppStream 2.0: the screen shows one application, a stock app, in a window; "
        "chosen apps in a window or browser tab. WorkSpaces Secure Browser: the screen shows one web browser open "
        "at an internal web address; internal websites and web apps only; closed to new customers from "
        "2026-10-29.",
        body, style=STYLE)


def billing_shape():
    """Hourly vs monthly WorkSpaces billing: the shape of the trade-off, with made-up numbers."""
    w, h = 680, 380
    left, top, pw, ph = 70, 76, 560, 220
    hmax = 200
    base, rate, flat = 10.0, 0.30, 34.0  # made up, for shape only; not AWS prices
    ymax = 70.0

    def X(v):
        return left + pw * v / hmax

    def Y(v):
        return top + ph - ph * v / ymax

    body = [
        '<text class="title" x="16" y="28">Hourly or monthly WorkSpaces billing: it depends on hours used</text>',
        '<text class="sub" x="16" y="48">The shape of the trade-off only. The numbers are made up; check real prices in the calculator.</text>',
    ]
    cross = (flat - base) / rate
    body.append(f'<rect class="band" x="{X(0):.1f}" y="{top}" width="{X(60) - X(0):.1f}" height="{ph}"/>')
    body.append(f'<text class="ann" x="{X(4):.1f}" y="{top + 16}">Part-time,</text>')
    body.append(f'<text class="ann" x="{X(4):.1f}" y="{top + 32}">seasonal staff</text>')
    body.append(f'<text class="ann" x="{X(196):.1f}" y="{top + ph - 10}" text-anchor="end">Full-time staff →</text>')
    for v in (0, 50, 100, 150, 200):
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{top}" y2="{top + ph}"/>')
        body.append(f'<text class="tick" x="{X(v):.1f}" y="{top + ph + 18}" text-anchor="middle">{v}</text>')
    body.append(f'<line class="axis" x1="{left}" x2="{left + pw}" y1="{top + ph}" y2="{top + ph}"/>')
    body.append(f'<text class="tick" x="{left + pw / 2}" y="{top + ph + 38}" text-anchor="middle">Hours the WorkSpace runs in a month</text>')
    body.append(f'<text class="tick" x="16" y="{top - 10}">Cost in a month (no scale: shape only)</text>')
    body.append(f'<path class="line-s1" d="M{X(0):.1f},{Y(flat):.1f} L{X(hmax):.1f},{Y(flat):.1f}"/>')
    end = min(hmax, (ymax - base) / rate)
    body.append(f'<path class="line-s2" d="M{X(0):.1f},{Y(base):.1f} L{X(end):.1f},{Y(base + rate * end):.1f}"/>')
    body.append(f'<circle class="dot-s1" cx="{X(cross):.1f}" cy="{Y(flat):.1f}" r="5"/>')
    body.append(f'<line class="lead" x1="{X(cross):.1f}" x2="{X(cross):.1f}" y1="{Y(flat) + 6:.1f}" y2="{top + ph}"/>')
    body.append(f'<text class="ann" x="{X(cross) - 8:.1f}" y="{Y(flat) - 30:.1f}" text-anchor="end">Break-even: beyond it,</text>')
    body.append(f'<text class="ann" x="{X(cross) - 8:.1f}" y="{Y(flat) - 14:.1f}" text-anchor="end">monthly is cheaper</text>')
    body.append(f'<text class="ann" x="{X(196):.1f}" y="{Y(flat) + 18:.1f}" text-anchor="end">Monthly: one fixed fee, unlimited use</text>')
    body.append(f'<text class="ann" x="{X(150):.1f}" y="{Y(65):.1f}" text-anchor="end">Hourly: a low monthly fee</text>')
    body.append(f'<text class="ann" x="{X(150):.1f}" y="{Y(65) + 16:.1f}" text-anchor="end">plus a charge per hour it runs</text>')
    y = top + ph + 64
    line_key(body, 16, y, "line-s2", "Hourly billing")
    line_key(body, 150, y, "line-s1", "Monthly billing")
    body.append(f'<text class="note" x="16" y="{y + 22}">Billing models from the Amazon WorkSpaces FAQ, checked 2026-10-24. AutoStop stops hourly WorkSpaces when idle.</text>')
    svg("10-03-billing-shape.svg", w, y + 36,
        "The shape of hourly versus monthly WorkSpaces billing",
        "A line chart of cost in a month against hours the WorkSpace runs in a month, from 0 to 200 hours, with no "
        "cost scale because the numbers are made up and only the shape matters. Monthly billing is a flat line: "
        "one fixed fee for unlimited use. Hourly billing starts lower, at a low monthly fee, and rises steadily with "
        "each hour the WorkSpace runs. The lines cross at a break-even point; above it, monthly is cheaper. A shaded "
        "band at low hours is labeled part-time, seasonal staff, where hourly is cheaper; the high-hours end is "
        "labeled full-time staff, where monthly is cheaper.",
        body, style=STYLE)


if __name__ == "__main__":
    big_picture()
    what_user_sees()
    billing_shape()
