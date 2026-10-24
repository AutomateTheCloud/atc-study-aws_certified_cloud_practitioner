#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 06.03 (containers and serverless) as SVG.

Usage: python3 -I source/charts/06-03-charts.py
Writes images/06-03-*.svg.
- What you manage: "What is Amazon ECS?" (capacity options: with EC2 "you choose
  the instance type, the number of instances, and manage the capacity"; Fargate
  removes server management), the Fargate FAQ and docs (AWS patches the platform),
  "What is AWS Lambda?" and "Lambda runtimes" (AWS manages servers, scaling and
  patching, and updates managed runtimes; you keep code, libraries and runtime
  upgrades), and the Shared Responsibility Model page for EC2. Checked 2026-10-23.
- Lambda vs Fargate: Lambda quotas (15 minutes, 128-10,240 MB), Lambda pricing,
  Fargate FAQ (GPU workloads not supported), Fargate pricing (per second,
  1-minute minimum, from image download to stop). Checked 2026-10-23.
- Pay per use: AWS Price List offer files for US East (N. Virginia), retrieved
  2026-10-24 (research repo sources/raw/pricing/compute-networking-us-east-1-summary.tsv):
  Lambda $0.20 per million requests and $0.0000166667 per GB-second (x86, first
  tier); EC2 t3.micro on-demand $0.0104 per hour. Free allowance (1 million
  requests and 400,000 GB-seconds a month) from the Lambda pricing page. The
  photo workload (512 MB for 2 seconds per photo) is made up for teaching.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap, line_key  # noqa: E402

# AWS = slot 1 (blue), you = slot 2 (orange), as in the 04.01 responsibility grids.
# Cells carry a light tint with ink text, so the words, not the color, say who does it.
STYLE = make_style(
    light_extra=" --aws-fill:#d9e8fb; --you-fill:#fbe1d6; --card-fill:#f1f0ec;",
    dark_extra=" --aws-fill:#1b3554; --you-fill:#4d2716; --card-fill:#252523;",
    rules_extra="""
  .aws { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .you { fill: var(--you-fill); stroke: var(--s2); stroke-width: 1.5; }
  .card { fill: var(--card-fill); stroke: var(--axis); stroke-width: 1; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 11.5px; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .rowl { fill: var(--ink); font-size: 12.5px; }
  .small { fill: var(--ink2); font-size: 12px; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .ann { fill: var(--ink); font-size: 12px; }
  .line-s2 { stroke: var(--s2); stroke-width: 2; fill: none; stroke-linecap: round; }
  .line-s1d { stroke: var(--s1); stroke-width: 2; fill: none; stroke-dasharray: 6 4; stroke-linecap: round; }
  .dot-ink { fill: var(--ink); stroke: var(--surface); stroke-width: 2; }""")


def cell(body, x, y, w, h, who, main, sub=None):
    body.append(f'<rect class="{who}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="5"/>')
    if sub:
        body.append(f'<text class="cellt" x="{x + w / 2:.1f}" y="{y + 18:.1f}" text-anchor="middle">{main}</text>')
        text_lines(body, x + w / 2, y + 33, sub, cls="cells", dy=14, anchor="middle")
    else:
        body.append(f'<text class="cellt" x="{x + w / 2:.1f}" y="{y + h / 2 + 4.5:.1f}" text-anchor="middle">{main}</text>')


COLS = [("Amazon EC2", ""), ("ECS or EKS", "on EC2 instances"), ("ECS or EKS", "on AWS Fargate"), ("AWS Lambda", "")]
ROWS = [
    ("Your code and its libraries, data and permissions", [
        ("you", "You", ["your software"]),
        ("you", "You", ["your containers"]),
        ("you", "You", ["your containers"]),
        ("you", "You", ["your function"]),
    ]),
    ("Language runtime, such as a Python version", [
        ("you", "You", ["installed on", "the server"]),
        ("you", "You", ["inside your", "container image"]),
        ("you", "You", ["inside your", "container image"]),
        ("aws", "AWS", ["updates managed", "runtimes; you leave", "retired ones"]),
    ]),
    ("Starting, stopping and spreading copies of the app", [
        ("you", "You", ["with Auto Scaling", "(lesson 06.02)"]),
        ("aws", "AWS", ["ECS or EKS does it,", "to your settings"]),
        ("aws", "AWS", ["ECS or EKS does it,", "to your settings"]),
        ("aws", "AWS", ["Lambda runs a copy", "per event"]),
    ]),
    ("Choosing servers: type and how many", [
        ("you", "You", ["instance type", "and count"]),
        ("you", "You", ["instance type", "and count"]),
        ("aws", "AWS", ["you only set CPU", "and memory per task"]),
        ("aws", "AWS", ["you only set", "memory"]),
    ]),
    ("Server operating system and its patches", [
        ("you", "You", ["the guest OS"]),
        ("you", "You", ["the instances' OS"]),
        ("aws", "AWS", None),
        ("aws", "AWS", None),
    ]),
    ("Hardware, buildings, power", [("aws", "AWS", None)] * 4),
]


def what_you_manage():
    w = 680
    left, cw, gap, rg = 186, 118, 6, 8
    body = [
        '<text class="title" x="16" y="28">What you manage at each step, from EC2 to Lambda</text>',
        '<text class="sub" x="16" y="48">Each step to the right hands more of the work to AWS (from AWS\'s documentation, checked 2026-10-23)</text>',
    ]
    top = 104
    for i, (a, b) in enumerate(COLS):
        cx = left + i * (cw + gap) + cw / 2
        body.append(f'<text class="head" x="{cx:.1f}" y="{top - (28 if b else 14)}" text-anchor="middle">{a}</text>')
        if b:
            body.append(f'<text class="small" x="{cx:.1f}" y="{top - 12}" text-anchor="middle">{b}</text>')
    y = top
    for name, cells in ROWS:
        nsub = max(len(c[2]) if c[2] else 0 for c in cells)
        lab = wrap(name, 25)
        rh = max(26 + 14 * nsub + (6 if nsub else 8), 15 * len(lab) + 10)
        text_lines(body, left - 12, y + rh / 2 + 4.5 - 7.5 * (len(lab) - 1), lab, cls="rowl", dy=15, anchor="end")
        for i, (who, main, sub) in enumerate(cells):
            cell(body, left + i * (cw + gap), y, cw, rh, who, main, sub)
        y += rh + rg
    y += 8
    counts = [sum(1 for _, cells in ROWS if cells[i][0] == "you") for i in range(4)]
    body.append(f'<text class="small" x="{left - 12}" y="{y + 4}" text-anchor="end">Rows that are yours</text>')
    for i, n in enumerate(counts):
        cx = left + i * (cw + gap) + cw / 2
        body.append(f'<text class="head" x="{cx:.1f}" y="{y + 4}" text-anchor="middle">{n} of {len(ROWS)}</text>')
    y += 30
    body.append(f'<text class="note" x="16" y="{y}">The top row never moves: your code, its libraries, your data and who can reach them stay yours everywhere.</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">Middle options exist too: ECS Managed Instances and EKS Auto Mode let AWS patch and scale the EC2 instances.</text>')
    h = y + 30
    svg("06-03-what-you-manage.svg", w, h,
        "What you manage on Amazon EC2, on ECS or EKS with EC2 instances, on ECS or EKS with AWS Fargate, and on AWS Lambda",
        "A grid of six rows by four compute options, each cell saying who does the work. Your code and its libraries, data "
        "and permissions: you, on all four. Language runtime, such as a Python version: you on EC2 (installed on "
        "the server), you on ECS or EKS with EC2 or Fargate (inside your container image), AWS on Lambda (it updates "
        "managed runtimes; you move off retired ones). Starting, stopping and spreading copies of the app: you on EC2, "
        "with Auto Scaling; AWS on the two container options (ECS or EKS does it, to your settings); AWS on Lambda (a "
        "copy per event). Choosing servers, type and how many: you on EC2 and on ECS or EKS with EC2; AWS on Fargate "
        "(you only set CPU and memory per task) and on Lambda (you only set memory). Server operating system and its "
        "patches: you on EC2 and on ECS or EKS with EC2; AWS on Fargate and Lambda. Hardware, buildings and power: AWS "
        "on all four. Rows that are yours: 5 of 6 on EC2, 4 of 6 on ECS or EKS with EC2, 2 of 6 on Fargate, 1 of 6 on "
        "Lambda. Notes: the top row never moves; ECS Managed Instances and EKS Auto Mode are middle options in which "
        "AWS patches and scales the EC2 instances.", body, style=STYLE)


PANELS = [
    ("AWS Lambda", "Runs a function when an event arrives", [
        ("You hand over", "function code (.zip or a container image)"),
        ("What starts it", "an event: a file upload, a web request, a message, a schedule"),
        ("How long it runs", "up to 15 minutes per invocation"),
        ("What you size", "memory, 128 MB to 10,240 MB; CPU grows with it"),
        ("How it bills", "per request, plus memory x run time (GB-seconds)"),
        ("Not for", "long or always-on work; full control of the OS"),
    ]),
    ("AWS Fargate", "Runs containers for ECS or EKS", [
        ("You hand over", "a container image, through ECS or EKS"),
        ("What starts it", "ECS or EKS starts a task, or keeps a service running"),
        ("How long it runs", "as long as the task runs, minutes or months"),
        ("What you size", "vCPU and memory for each task"),
        ("How it bills", "per second for vCPU, memory and storage, 1-minute minimum"),
        ("Not for", "GPU work (use EC2); events that need no container"),
    ]),
]


def lambda_vs_fargate():
    w = 680
    pw, gap = 318, 12
    body = [
        '<text class="title" x="16" y="28">Lambda and Fargate: both serverless, built for different work</text>',
        '<text class="sub" x="16" y="48">Same: no servers to manage, AWS scales them, you pay for what runs. Differences below.</text>',
    ]
    top = 66
    heights = []
    for p, (name, tag, rows) in enumerate(PANELS):
        x = 16 + p * (pw + gap)
        y = top + 50
        for lab, val in rows:
            y += 16 + 15 * len(wrap(val, 40)) + 8
        heights.append(y - top + 6)
    ph = max(heights)
    for p, (name, tag, rows) in enumerate(PANELS):
        x = 16 + p * (pw + gap)
        body.append(f'<rect class="card" x="{x}" y="{top}" width="{pw}" height="{ph}" rx="8"/>')
        body.append(f'<line class="axis" x1="{x}" x2="{x + pw}" y1="{top + 44}" y2="{top + 44}"/>')
        body.append(f'<text class="cellt" x="{x + 14}" y="{top + 18}">{name}</text>')
        body.append(f'<text class="cells" x="{x + 14}" y="{top + 33}">{tag}</text>')
        y = top + 64
        for lab, val in rows:
            body.append(f'<text class="head" x="{x + 14}" y="{y}">{lab}</text>')
            y = text_lines(body, x + 14, y + 16, wrap(val, 40), cls="small", dy=15) + 8
    y = top + ph + 20
    body.append(f'<text class="note" x="16" y="{y}">From the Lambda quotas and pricing pages and the Fargate FAQ and pricing page, checked 2026-10-23.</text>')
    svg("06-03-lambda-vs-fargate.svg", w, y + 14,
        "AWS Lambda and AWS Fargate compared side by side",
        "Two panels. What is the same: no servers to manage, AWS scales them, you pay for what runs. AWS Lambda runs a "
        "function when an event arrives. You hand over function code, as a .zip file or a container image. An event "
        "starts it: a file upload, a web request, a message or a schedule. It runs up to 15 minutes per invocation. You "
        "size its memory, from 128 MB to 10,240 MB, and CPU grows with it. It bills per request plus memory times run "
        "time, in GB-seconds. It is not for long or always-on work, or when you need full control of the operating "
        "system. AWS Fargate runs containers for ECS or EKS. You hand over a container image through ECS or EKS. ECS "
        "or EKS starts a task or keeps a service running. It runs as long as the task runs, minutes or months. You size "
        "vCPU and memory for each task. It bills per second for vCPU, memory and storage, with a 1-minute minimum. It "
        "is not for GPU work, which needs EC2, or for event-driven code that needs no container.", body, style=STYLE)


# Pay per use vs an always-on server, for the bakery's photo-resize job.
REQ = 0.20 / 1e6            # per request, Lambda, us-east-1, price list 2026-10-24
GBS = 0.0000166667          # per GB-second, x86 first tier
GBS_PER_PHOTO = 0.5 * 2     # 512 MB for 2 seconds (made up for teaching)
T3_MICRO = 0.0104 * 730     # $ per month, on-demand, 730 hours
FREE_REQ, FREE_GBS = 1_000_000, 400_000


def lam(n, free=False):
    if free:
        return max(0, n - FREE_REQ) * REQ + max(0, n * GBS_PER_PHOTO - FREE_GBS) * GBS
    return n * REQ + n * GBS_PER_PHOTO * GBS


def pay_per_use():
    w = 680
    left, top, pw, ph = 64, 92, 580, 250
    xmax, ymax = 1_000_000, 18
    body = [
        '<text class="title" x="16" y="28">Pay per use, or pay for a server that is always on?</text>',
        '<text class="sub" x="16" y="48">Monthly compute cost of resizing photos. US East (N. Virginia), prices as of 2026-10-24.</text>',
    ]
    line_key(body, 16, 74, "line-s1", "Lambda")
    line_key(body, 100, 74, "line-s1d", "Lambda, after the monthly free allowance")
    line_key(body, 400, 74, "line-s2", "One t3.micro instance, on all month")

    def X(n):
        return left + pw * n / xmax

    def Y(v):
        return top + ph - ph * v / ymax

    for v in range(0, ymax + 1, 3):
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{Y(v) + 4:.1f}" text-anchor="end">${v}</text>')
    for n in range(0, xmax + 1, 200_000):
        lab = "0" if n == 0 else f"{n // 1000:,}k"
        body.append(f'<text class="tick" x="{X(n):.1f}" y="{top + ph + 18}" text-anchor="middle">{lab}</text>')
    body.append(f'<text class="tick" x="{left + pw / 2}" y="{top + ph + 36}" text-anchor="middle">Photos resized per month</text>')
    # Lines
    pts = [(n, lam(n)) for n in range(0, xmax + 1, 10_000)]
    body.append('<path class="line-s1" d="M' + " L".join(f"{X(n):.1f},{Y(v):.1f}" for n, v in pts) + '"/>')
    pts = [(n, lam(n, True)) for n in range(0, xmax + 1, 10_000)]
    body.append('<path class="line-s1d" d="M' + " L".join(f"{X(n):.1f},{Y(v):.1f}" for n, v in pts) + '"/>')
    body.append(f'<line class="line-s2" x1="{left}" x2="{left + pw}" y1="{Y(T3_MICRO):.1f}" y2="{Y(T3_MICRO):.1f}"/>')
    # Crossovers
    cross1 = T3_MICRO / lam(1)
    lo, hi = 400_000, 1_000_000
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if lam(mid, True) < T3_MICRO else (lo, mid)
    cross2 = lo
    assert 440_000 < cross1 < 460_000 and 840_000 < cross2 < 870_000
    for n in (cross1, cross2):
        body.append(f'<circle class="dot-ink" cx="{X(n):.1f}" cy="{Y(T3_MICRO):.1f}" r="5"/>')
    body.append(f'<text class="ann" x="{X(cross1) - 8:.1f}" y="{Y(T3_MICRO) - 40:.1f}" text-anchor="end">About {round(cross1, -4) / 1000:.0f}k photos: the server</text>')
    body.append(f'<text class="ann" x="{X(cross1) - 8:.1f}" y="{Y(T3_MICRO) - 24:.1f}" text-anchor="end">becomes the cheaper choice</text>')
    body.append(f'<line class="lead" x1="{X(cross1) - 4:.1f}" x2="{X(cross1):.1f}" y1="{Y(T3_MICRO) - 20:.1f}" y2="{Y(T3_MICRO) - 6:.1f}"/>')
    body.append(f'<text class="ann" x="{X(cross2):.1f}" y="{Y(T3_MICRO) + 24:.1f}" text-anchor="middle">About {round(cross2, -4) / 1000:.0f}k with</text>')
    body.append(f'<text class="ann" x="{X(cross2):.1f}" y="{Y(T3_MICRO) + 40:.1f}" text-anchor="middle">the free allowance</text>')
    body.append(f'<text class="ann" x="{left + 8}" y="{Y(T3_MICRO) + 18:.1f}">${T3_MICRO:.2f} a month, busy or idle</text>')
    bakery = 3_000
    body.append(f'<circle class="dot-s1" cx="{X(bakery):.1f}" cy="{Y(lam(bakery)):.1f}" r="5"/>')
    body.append(f'<text class="ann" x="{X(bakery) + 14:.1f}" y="{Y(16.2):.1f}">The bakery today: about 3,000 photos a month,</text>')
    body.append(f'<text class="ann" x="{X(bakery) + 14:.1f}" y="{Y(16.2) + 16:.1f}">${lam(bakery):.2f} before the free allowance, $0 after it</text>')
    body.append(f'<line class="lead" x1="{X(bakery) + 1:.1f}" x2="{X(bakery) + 8:.1f}" y1="{Y(lam(bakery)) - 7:.1f}" y2="{Y(16.2) - 4:.1f}"/>')
    y = top + ph + 62
    for line in (
        "Assumes each resize needs 512 MB for 2 seconds (1 GB-second), and that one t3.micro could keep up;",
        "made up for teaching. Lambda: $0.20 per million requests and $0.0000166667 per GB-second (x86).",
        "Free allowance: 1 million requests and 400,000 GB-seconds a month. t3.micro: $0.0104 an hour, 730 hours.",
        "Compute only: storage, logs and data transfer are left out. Sources: AWS Price List offer files,",
        "retrieved 2026-10-24; Lambda pricing page, checked 2026-10-23. Prices change.",
    ):
        body.append(f'<text class="note" x="16" y="{y}">{line}</text>')
        y += 15
    svg("06-03-pay-per-use.svg", w, y + 4,
        "Monthly compute cost of resizing photos: AWS Lambda against one always-on t3.micro instance",
        f"A line chart. The horizontal axis is photos resized per month, from 0 to 1 million; the vertical axis is "
        f"dollars per month, from 0 to 18. A flat line for one t3.micro instance running all month sits at "
        f"${T3_MICRO:.2f}, whether busy or idle. A straight Lambda line, before the free allowance, rises from $0 to "
        f"about ${lam(xmax):.2f} at 1 million photos and crosses the server line at about {round(cross1, -4) / 1000:.0f} "
        f"thousand photos. A dashed Lambda line, after the monthly free allowance, stays at $0 until 400 thousand photos, "
        f"then rises and crosses the server line at about {round(cross2, -4) / 1000:.0f} thousand photos. A dot marks "
        f"the bakery today: about 3,000 photos a month, ${lam(bakery):.2f} before the free allowance and $0 after it. "
        "Assumptions: each resize needs 512 MB for 2 seconds; one t3.micro could keep up; compute charges only. "
        "Prices as of 2026-10-24.", body, style=STYLE)


if __name__ == "__main__":
    what_you_manage()
    lambda_vs_fargate()
    pay_per_use()
