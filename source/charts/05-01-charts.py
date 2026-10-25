#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 05.01 (block, file and object storage) as SVG.

Usage: python3 -I source/charts/05-01-charts.py
Writes images/05-01-*.svg. Facts, checked 2026-10-23 and 2026-10-24 in the research repo
(docs/04-services/storage.md and its sources):
- the three storage types and their AWS examples: EFS FAQ, "When should I use Amazon EFS
  vs. Amazon EBS vs. Amazon S3?";
- what happens to instance store data on reboot, stop, hibernate and terminate: EC2 User
  Guide, "Data persistence for Amazon EC2 instance store volumes";
- EBS data persisting independently of the instance, and the root volume's "Delete on
  termination" flag: Amazon EBS FAQs;
- where copies live: EBS volumes are replicated within one AZ (What is Amazon EBS?); EFS
  Regional stores data across multiple AZs and EFS One Zone in one (What is Amazon EFS?);
  S3 Standard stores data across at least three AZs and S3 One Zone-IA in one (S3 User
  Guide, storage classes).
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Panels use a neutral fill; the one thing each panel highlights (the disk, the shared
# folder tree, the bucket) uses categorical slot 1 (blue). Kept/lost cells use the fixed
# status colors, always with an icon and a word, so color never carries meaning alone.
STYLE = make_style(
    light_extra=" --panel:#f1f0ec; --hi-fill:#d9e8fb; --good:#0ca30c; --crit:#d03b3b;"
                " --good-fill:#e3f4e3; --crit-fill:#fae3e3;",
    dark_extra=" --panel:#252523; --hi-fill:#1b3554; --good:#0ca30c; --crit:#d03b3b;"
               " --good-fill:#16301a; --crit-fill:#3d1d1d;",
    rules_extra="""
  .panel { fill: var(--panel); stroke: var(--axis); stroke-width: 1; }
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 1.5; }
  .box { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .blk { fill: var(--s1); }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .head { fill: var(--ink); font-size: 15px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .mono { fill: var(--ink); font-size: 11.5px; font-family: ui-monospace, Menlo, Consolas, monospace; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .ex { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .wire { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .good { fill: var(--good-fill); stroke: var(--good); stroke-width: 1.5; }
  .crit { fill: var(--crit-fill); stroke: var(--crit); stroke-width: 1.5; }
  .gi { stroke: var(--good); stroke-width: 2.5; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .ci { stroke: var(--crit); stroke-width: 2.5; fill: none; stroke-linecap: round; }
  .az { fill: none; stroke: var(--axis); stroke-width: 1.2; stroke-dasharray: 5 4; }
  .span { fill: var(--s1); }
  .span-light { fill: var(--s1-light); }""")


def server(body, x, y, label="Server"):
    """A small server box with a label inside."""
    body.append(f'<rect class="box" x="{x}" y="{y}" width="58" height="26" rx="4"/>')
    body.append(f'<text class="small" x="{x + 29}" y="{y + 17}" text-anchor="middle">{label}</text>')


def three_kinds():
    """Big picture: block, file and object storage side by side."""
    w, pw, gap = 700, 216, 10
    top = 64
    ph = 380
    body = [
        '<text class="title" x="16" y="28">Three ways to store data: block, file and object</text>',
        '<text class="sub" x="16" y="48">What differs is how a computer reaches the data, and how many computers can reach it at once.</text>',
    ]
    xs = [16 + i * (pw + gap) for i in range(3)]
    for x in xs:
        body.append(f'<rect class="panel" x="{x}" y="{top}" width="{pw}" height="{ph}" rx="8"/>')

    # Block: one server, one disk made of numbered blocks.
    x = xs[0]
    body.append(f'<text class="head" x="{x + 14}" y="{top + 26}">Block</text>')
    body.append(f'<text class="small" x="{x + 14}" y="{top + 44}">A disk for one server</text>')
    server(body, x + 79, top + 62)
    body.append(f'<line class="wire" x1="{x + 108}" y1="{top + 88}" x2="{x + 108}" y2="{top + 112}"/>')
    body.append(f'<rect class="hi" x="{x + 38}" y="{top + 112}" width="140" height="92" rx="6"/>')
    for r in range(3):
        for c in range(6):
            body.append(f'<rect class="blk" x="{x + 50 + c * 20}" y="{top + 124 + r * 22}" width="16" height="16" rx="2"/>')
    body.append(f'<text class="small" x="{x + 108}" y="{top + 222}" text-anchor="middle">Numbered blocks, no names</text>')
    y = text_lines(body, x + 14, top + 252, wrap("The server's operating system formats the disk and keeps its own files on it, as on a laptop's drive.", 30), cls="small", dy=16)
    body.append(f'<text class="ex" x="{x + 14}" y="{top + ph - 44}">Amazon EBS</text>')
    body.append(f'<text class="ex" x="{x + 14}" y="{top + ph - 24}">EC2 instance store</text>')

    # File: a shared folder tree, three servers connected.
    x = xs[1]
    body.append(f'<text class="head" x="{x + 14}" y="{top + 26}">File</text>')
    body.append(f'<text class="small" x="{x + 14}" y="{top + 44}">A shared folder tree</text>')
    for i in range(3):
        sx = x + 14 + i * 66
        server(body, sx, top + 62)
        body.append(f'<line class="wire" x1="{sx + 29}" y1="{top + 88}" x2="{x + 108}" y2="{top + 112}"/>')
    body.append(f'<rect class="hi" x="{x + 28}" y="{top + 112}" width="160" height="92" rx="6"/>')
    tree = ["/shared", "  photos/", "    birthday-cake.jpg", "  menus/"]
    for i, t in enumerate(tree):
        body.append(f'<text class="mono" x="{x + 40}" y="{top + 134 + i * 19}" xml:space="preserve">{t}</text>')
    body.append(f'<text class="small" x="{x + 108}" y="{top + 222}" text-anchor="middle">Folders and file names</text>')
    text_lines(body, x + 14, top + 252, wrap("Many servers connect over the network at the same time and see the same files.", 30), cls="small", dy=16)
    body.append(f'<text class="ex" x="{x + 14}" y="{top + ph - 44}">Amazon EFS</text>')
    body.append(f'<text class="ex" x="{x + 14}" y="{top + ph - 24}">Amazon FSx</text>')

    # Object: a bucket of whole objects, reached by an API call over HTTPS.
    x = xs[2]
    body.append(f'<text class="head" x="{x + 14}" y="{top + 26}">Object</text>')
    body.append(f'<text class="small" x="{x + 14}" y="{top + 44}">Whole objects in a bucket</text>')
    server(body, x + 22, top + 62, "App")
    server(body, x + 136, top + 62, "Phone")
    body.append(f'<line class="wire" x1="{x + 51}" y1="{top + 88}" x2="{x + 90}" y2="{top + 112}"/>')
    body.append(f'<line class="wire" x1="{x + 165}" y1="{top + 88}" x2="{x + 126}" y2="{top + 112}"/>')
    body.append(f'<text class="note" x="{x + 108}" y="{top + 104}" text-anchor="middle">HTTPS</text>')
    body.append(f'<rect class="hi" x="{x + 18}" y="{top + 112}" width="180" height="92" rx="6"/>')
    body.append(f'<text class="mono" x="{x + 28}" y="{top + 132}">key: cakes/birthday.jpg</text>')
    body.append(f'<text class="mono" x="{x + 28}" y="{top + 150}">data: the whole photo</text>')
    body.append(f'<text class="mono" x="{x + 28}" y="{top + 168}">metadata: type, date</text>')
    body.append(f'<text class="mono" x="{x + 28}" y="{top + 192}">key: menus/may.pdf ...</text>')
    body.append(f'<text class="small" x="{x + 108}" y="{top + 222}" text-anchor="middle">Each object has a key</text>')
    text_lines(body, x + 14, top + 252, wrap("Programs put and get whole objects through an API, from anywhere they are allowed to.", 30), cls="small", dy=16)
    body.append(f'<text class="ex" x="{x + 14}" y="{top + ph - 44}">Amazon S3</text>')
    body.append(f'<text class="ex" x="{x + 14}" y="{top + ph - 24}">(all its storage classes)</text>')

    y = top + ph + 22
    body.append(f'<text class="note" x="16" y="{y}">Our summary of the Amazon EFS FAQ ("EFS vs. EBS vs. S3"), checked 2026-10-24. File and key names are made up.</text>')
    svg("05-01-three-kinds.svg", w, y + 14,
        "Block, file and object storage side by side",
        "Three panels. Block: a disk for one server. One server connects to a disk drawn as numbered "
        "blocks with no names; the server's operating system formats the disk and keeps its own files on "
        "it, as on a laptop's drive. Examples: Amazon EBS and EC2 instance store. File: a shared folder "
        "tree. Three servers connect to one folder tree with folders and file names; many servers connect "
        "over the network at the same time and see the same files. Examples: Amazon EFS and Amazon FSx. "
        "Object: whole objects in a bucket. An app and a phone reach the bucket over HTTPS; each object has "
        "a key, such as cakes/birthday.jpg, the whole data, and metadata; programs put and get whole "
        "objects through an API. Example: Amazon S3, with all its storage classes.", body, style=STYLE)


def what_survives():
    """EBS vs instance store: what happens to the data on each instance event."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">What happens to the data when the server changes state</text>',
        '<text class="sub" x="16" y="48">An EBS volume lives apart from the server. Instance store lives and dies with it.</text>',
    ]
    rows = [
        ("Reboot", "The server restarts", ("good", "Kept", ""), ("good", "Kept", "")),
        ("Stop", "The server is turned off", ("good", "Kept", ""), ("crit", "Lost", "every block erased")),
        ("Hibernate", "Memory saved, then off", ("good", "Kept", ""), ("crit", "Lost", "every block erased")),
        ("Terminate", "The server is deleted", ("good", "Kept", "only if its Delete on termination setting is No"),
         ("crit", "Lost", "every block erased")),
    ]
    c0, c1, c2 = 16, 220, 460
    cw = 204
    y = 78
    body.append(f'<text class="cellt" x="{c0}" y="{y}">Server event</text>')
    body.append(f'<text class="cellt" x="{c1}" y="{y}">Data on an EBS volume</text>')
    body.append(f'<text class="cellt" x="{c2}" y="{y}">Data on instance store</text>')
    y += 12

    def cell(x, y, h, kind, word, note):
        body.append(f'<rect class="{kind}" x="{x}" y="{y}" width="{cw}" height="{h}" rx="6"/>')
        ix, iy = x + 18, y + h / 2  # icon and word centered in taller cells
        if kind == "good":
            body.append(f'<path class="gi" d="M{ix - 6},{iy} L{ix - 1},{iy + 5} L{ix + 7},{iy - 6}"/>')
        else:
            body.append(f'<path class="ci" d="M{ix - 5},{iy - 5} L{ix + 5},{iy + 5} M{ix + 5},{iy - 5} L{ix - 5},{iy + 5}"/>')
        body.append(f'<text class="cellt" x="{x + 36}" y="{y + h / 2 + 5}">{word}</text>')
        if note:
            lines = wrap(note, 18)
            text_lines(body, x + 82, y + h / 2 + 4 - 7 * (len(lines) - 1), lines, cls="small", dy=14)

    for ev, sub, ebs, inst in rows:
        h = 64 if ebs[2] else 44
        body.append(f'<text class="cellt" x="{c0}" y="{y + 20}">{ev}</text>')
        body.append(f'<text class="small" x="{c0}" y="{y + 36}">{sub}</text>')
        cell(c1, y, h, *ebs)
        cell(c2, y, h, *inst)
        y += h + 8
    y += 14
    y = text_lines(body, 16, y, wrap("A reboot is the one event instance store survives. Copy anything you need to keep to EBS, S3 or EFS.", 84), cls="small")
    y += 6
    body.append(f'<text class="note" x="16" y="{y}">Sources: EC2 User Guide, "Data persistence for instance store volumes"; Amazon EBS FAQs. Checked 2026-10-24.</text>')
    svg("05-01-what-survives.svg", w, y + 14,
        "What happens to data on an EBS volume and on instance store when the server changes state",
        "A grid of four server events by two kinds of block storage. Reboot, the server restarts: EBS kept; "
        "instance store kept. Stop, the server is turned off: EBS kept; instance store lost, every block "
        "erased. Hibernate, memory saved, then off: EBS kept; instance store lost. Terminate, the server is "
        "deleted: EBS kept only if the volume's Delete on termination setting is No; instance store lost. "
        "Below: a reboot is the one event instance store survives; copy anything you need to keep to EBS, "
        "S3 or EFS.", body, style=STYLE)


if __name__ == "__main__":
    three_kinds()
    what_survives()
