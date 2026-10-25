#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 05.04 (hybrid storage and backup) as SVG.

Usage: python3 -I source/charts/05-04-charts.py
Writes images/05-04-*.svg. Facts come from AWS pages cited in
guide/05-storing-data/04-hybrid-storage-and-backup.md, all checked 2026-10-23/24:
the AWS Storage Gateway FAQ and per-gateway "What is" pages (protocols, local
cache, cached vs stored volumes, tapes archived to the S3 Glacier classes), the
AWS Backup docs and FAQ (plans, vaults, cross-Region copies), the AWS Elastic
Disaster Recovery docs, product page and FAQ (continuous replication to a
staging area, launch in minutes, RPO of seconds and RTO of minutes), and the
Amazon EBS and Amazon RDS docs (snapshots, automated backups). The bakery's
setup is made up for teaching. Our own design: no AWS logos, icons, trade dress
or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# On premises = neutral fill; in AWS = categorical slot 1 (blue) tint; the service
# that connects them = slot 2 (orange) tint. Every box also says in words where it
# runs, so color is never alone.
STYLE = make_style(
    light_extra=" --aws-fill:#d9e8fb; --link-fill:#fbe1d6; --prem-fill:#f1f0ec;",
    dark_extra=" --aws-fill:#1b3554; --link-fill:#4d2716; --prem-fill:#252523;",
    rules_extra="""
  .aws { fill: var(--aws-fill); stroke: var(--s1); stroke-width: 1.5; }
  .link { fill: var(--link-fill); stroke: var(--s2); stroke-width: 1.5; }
  .prem { fill: var(--prem-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .zone { fill: none; stroke: var(--axis); stroke-width: 1.5; stroke-dasharray: 6 4; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .cells { fill: var(--ink2); font-size: 12px; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .arrlab { fill: var(--ink2); font-size: 11.5px; font-style: italic; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }""")


def arrow(body, x1, y1, x2, y2):
    """A straight line with a small filled head at (x2, y2); horizontal or vertical."""
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    if abs(x1 - x2) < 0.1:
        d = 1 if y2 > y1 else -1
        body.append(f'<path class="arrowhead" d="M{x2 - 5:.1f},{y2 - 8 * d:.1f} L{x2 + 5:.1f},{y2 - 8 * d:.1f} L{x2:.1f},{y2:.1f} Z"/>')
    else:
        d = 1 if x2 > x1 else -1
        body.append(f'<path class="arrowhead" d="M{x2 - 8 * d:.1f},{y2 - 5:.1f} L{x2 - 8 * d:.1f},{y2 + 5:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def box(body, cls, x, y, w, h, title, lines, width_chars):
    """A rounded box with a bold title and wrapped lines under it."""
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="6"/>')
    yy = text_lines(body, x + 10, y + 19, wrap(title, width_chars), cls="cellt", dy=16)
    text_lines(body, x + 10, yy + 1, [ln for t in lines for ln in wrap(t, width_chars + 3)], cls="cells", dy=15)


def box_height(title, lines, width_chars):
    n = len(wrap(title, width_chars)) * 16 + sum(len(wrap(t, width_chars + 3)) for t in lines) * 15
    return n + 18


LANES = [  # (on premises, connector, in AWS, label on the left arrow, label on the right arrow)
    (("Back-office computers", ["Staff save invoices in a shared folder"]),
     ("S3 File Gateway", ["A virtual machine in the shop; keeps recent files in a local cache"]),
     ("Amazon S3 bucket", ["Each file becomes an object"]),
     "files over SMB or NFS", "stored as objects"),
    (("Backup software", ["Writes the accounts' weekly backups to tape"]),
     ("Tape Gateway", ["Looks like a tape library to the backup software"]),
     ("Virtual tapes in S3", ["Archived to the S3 Glacier classes"]),
     "virtual tapes", "stored and archived"),
    (("The till server", ["The shop's cash-register system"]),
     ("Elastic Disaster Recovery", ["An agent copies every change to the server's disks"]),
     ("Staging area", ["Cheap storage; recovery servers launch in minutes"]),
     "every change, continuously", "kept ready"),
]


GATEWAYS = [  # (name, app, protocol label, kept locally, lands in AWS, typical need)
    ("S3 File Gateway", "File-sharing apps and users", "files: NFS or SMB",
     "recently used files, in a local cache",
     "Objects in an S3 bucket, readable with normal S3 tools",
     "Keep a shared folder, store the files in S3"),
    ("Volume Gateway", "Servers that need disks", "disk blocks: iSCSI",
     "cached mode, frequently used data; stored mode, the whole dataset",
     "Cached mode: the data itself, in S3. Stored mode: point-in-time copies, as EBS snapshots",
     "Cloud-backed disks, or off-site copies of local disks"),
    ("Tape Gateway", "Existing backup software", "tapes: iSCSI",
     "recently used tapes, in a local cache",
     "Virtual tapes in S3, archived to S3 Glacier Flexible Retrieval or Deep Archive",
     "Replace physical tapes without changing the backup jobs"),
]


def gateway_types():
    """Three side-by-side flows: the app, the gateway and its cache, where the data lands."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Three kinds of Storage Gateway, one idea: local access, data in AWS</text>',
        '<text class="sub" x="16" y="48">The app keeps the protocol it already speaks; the gateway turns it into AWS storage</text>',
    ]
    cw, gap = 208, 12
    xs = [16 + i * (cw + gap) for i in range(3)]
    top = 70
    h2m = max(max(box_height("The gateway (on premises)", ["Keeps: " + g[3]], 27), 78) for g in GATEWAYS)
    h3m = max(max(box_height("In AWS", [g[4]], 27), 78) for g in GATEWAYS)
    for x, (name, app, proto, local, lands, need) in zip(xs, GATEWAYS):
        body.append(f'<text class="cellt" x="{x + cw / 2:.1f}" y="{top + 4}" text-anchor="middle">{name}</text>')
        y = top + 16
        h1 = 46
        box(body, "prem", x, y, cw, h1, "In the shop", [app], 27)
        arrow(body, x + cw / 2, y + h1 + 2, x + cw / 2, y + h1 + 34)
        body.append(f'<text class="arrlab" x="{x + cw / 2 + 8:.1f}" y="{y + h1 + 22:.1f}">{proto}</text>')
        y += h1 + 36
        h2 = h2m
        box(body, "link", x, y, cw, h2, "The gateway (on premises)", ["Keeps: " + local], 27)
        arrow(body, x + cw / 2, y + h2 + 2, x + cw / 2, y + h2 + 34)
        body.append(f'<text class="arrlab" x="{x + cw / 2 + 8:.1f}" y="{y + h2 + 22:.1f}">over the network</text>')
        y += h2 + 36
        h3 = h3m
        box(body, "aws", x, y, cw, h3, "In AWS", [lands], 27)
        y += h3 + 22
        body.append(f'<text class="rowl" x="{x}" y="{y}">Typical need</text>')
        text_lines(body, x, y + 16, wrap(need, 30), cls="small", dy=15)
    yb = top + 16 + 46 + 36 + h2m + 36 + h3m + 22 + 60
    body.append(f'<text class="note" x="16" y="{yb}">A fourth type, Amazon FSx File Gateway, has been closed to new customers since 2024-10-28.</text>')
    body.append(f'<text class="note" x="16" y="{yb + 16}">From the AWS Storage Gateway FAQ and documentation, checked 2026-10-23.</text>')
    svg("05-04-gateway-types.svg", w, yb + 30,
        "Three kinds of AWS Storage Gateway: what stays on premises and where the data lands",
        "Three columns, each a flow from top to bottom. S3 File Gateway: file-sharing apps and users in the shop "
        "send files over NFS or SMB to the gateway on premises, which keeps recently used files in a local cache "
        "and stores them over the network as objects in an S3 bucket, readable with normal S3 tools; typical need: "
        "keep a shared folder and store the files in S3. Volume Gateway: servers that need disks send block "
        "volumes over iSCSI; in cached mode the gateway keeps frequently used data and the data itself lives in S3; "
        "in stored mode the gateway keeps the whole dataset and AWS holds point-in-time copies as EBS snapshots; typical need: cloud-backed disks or "
        "off-site copies of local disks. Tape Gateway: existing backup software sends virtual tapes over iSCSI; "
        "the gateway caches recently used tapes; tapes are stored in S3 and archived to S3 Glacier Flexible "
        "Retrieval or Deep Archive; typical need: replace physical tapes without changing the backup jobs. "
        "A note says Amazon FSx File Gateway has been closed to new customers since 2024-10-28.", body, style=STYLE)


COMPARE_ROWS = ["Copies", "How often", "What you get back", "How fast"]
COMPARE = [
    ("A snapshot", "Go back to how one disk or database was",
     ["One EBS volume or one RDS database",
      "When you take one, or on a schedule",
      "A new volume or database, as it was at that moment",
      "As long as a restore takes"]),
    ("AWS Backup", "Run backups for many services by one set of rules",
     ["Many resources across services and accounts, chosen by tag",
      "On the plan's schedule; kept for the plan's retention",
      "Recovery points of your data, also copied to other Regions or accounts",
      "As long as a restore takes; servers still need relaunching"]),
    ("Elastic Disaster Recovery", "Get whole servers running again, fast",
     ["Whole servers: disks, operating system, applications",
      "Continuously, change by change",
      "Running recovery servers in AWS, from the latest state or an earlier point",
      "AWS says: seconds of data lost, running again in minutes"]),
]


def backup_dr_snapshot():
    """Comparison panels: snapshot vs AWS Backup vs Elastic Disaster Recovery."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">A snapshot, AWS Backup and Elastic Disaster Recovery side by side</text>',
        '<text class="sub" x="16" y="48">All three keep copies; they differ in scope and in what you get back</text>',
    ]
    lw = 118
    cw, gap = 174, 6
    xs = [16 + lw + i * (cw + gap) for i in range(3)]
    y = 72
    hh = 0
    for x, (name, q, _) in zip(xs, COMPARE):
        ql = wrap(q, 24)
        h = 26 + 15 * len(ql) + 8
        hh = max(hh, h)
    for i, (x, (name, q, _)) in enumerate(zip(xs, COMPARE)):
        cls = "aws"
        body.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{cw}" height="{hh}" rx="6"/>')
        body.append(f'<text class="cellt" x="{x + 10}" y="{y + 19}">{name}</text>')
        text_lines(body, x + 10, y + 36, wrap(q, 26), cls="cells", dy=15)
    body.append(f'<text class="rowl" x="16" y="{y + 19}">The job</text>')
    y += hh + 8
    for r, row in enumerate(COMPARE_ROWS):
        cells = [wrap(c[2][r], 26) for c in COMPARE]
        h = 12 + 15 * max(len(c) for c in cells) + 6
        body.append(f'<line class="grid" x1="16" x2="{xs[2] + cw}" y1="{y}" y2="{y}"/>')
        body.append(f'<text class="rowl" x="16" y="{y + 19}">{row}</text>')
        for x, c in zip(xs, cells):
            text_lines(body, x + 10, y + 19, c, cls="small", dy=15)
        y += h
    body.append(f'<line class="grid" x1="16" x2="{xs[2] + cw}" y1="{y}" y2="{y}"/>')
    y += 22
    body.append(f'<text class="note" x="16" y="{y}">Only Elastic Disaster Recovery brings back running servers; the other two bring back data.</text>')
    body.append(f'<text class="note" x="16" y="{y + 16}">From AWS documentation for Amazon EBS, Amazon RDS, AWS Backup and AWS DRS, checked 2026-10-23.</text>')
    svg("05-04-backup-dr-snapshot.svg", w, y + 30,
        "A snapshot, AWS Backup and AWS Elastic Disaster Recovery compared",
        "Three columns compared on five rows. The job: a snapshot goes back to how one disk or database was; "
        "AWS Backup runs backups for many services by one set of rules; Elastic Disaster Recovery gets whole "
        "servers running again, fast. Copies: one EBS volume or one RDS database; many resources across "
        "services and accounts, chosen by tag; whole servers with disks, operating system and applications. How "
        "often: when you take one or on a schedule; on the plan's schedule, kept for the plan's retention; "
        "continuously, change by change. What you get back: a new volume or database as it was at that moment; "
        "recovery points of your data, also copied to other Regions or accounts; running recovery servers in AWS "
        "from the latest state or an earlier point. How fast: as long as a restore takes; as long as a restore "
        "takes, and servers still need relaunching; AWS says seconds of data lost and running again in minutes. A note: only Elastic Disaster Recovery brings back running servers; the other two bring back data.",
        body, style=STYLE)


if __name__ == "__main__":
    gateway_types()
    backup_dr_snapshot()
