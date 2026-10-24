#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphic for Lab 05 (versions and lifecycle) as SVG.

Usage: python3 -I source/charts/05-07-charts.py
Writes images/05-07-version-stack.svg: what a versioning-enabled S3 bucket keeps for
one object key after each step of the lab. Facts from the Amazon S3 User Guide,
"Retaining multiple versions of objects with S3 Versioning" (checked 2026-10-23):
an overwrite adds a new version, a delete adds a delete marker that becomes the
current version, and every stored version is billed as a whole object.
Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

# Current version = slot 1 (blue) tint with a solid border; older versions = neutral;
# delete marker = slot 2 (orange), dashed. Every box also says in words what it is.
STYLE = make_style(
    light_extra=" --cur-fill:#d9e8fb; --old-fill:#f1f0ec; --dm-fill:#fbe1d6;",
    dark_extra=" --cur-fill:#1b3554; --old-fill:#252523; --dm-fill:#4d2716;",
    rules_extra="""
  .cur { fill: var(--cur-fill); stroke: var(--s1); stroke-width: 2; }
  .old { fill: var(--old-fill); stroke: var(--axis); stroke-width: 1; }
  .dm { fill: var(--dm-fill); stroke: var(--s2); stroke-width: 2; stroke-dasharray: 5 3; }
  .gone { fill: none; stroke: var(--axis); stroke-width: 1; stroke-dasharray: 3 3; }
  .frame { fill: none; stroke: var(--grid); stroke-width: 1; }
  .step { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .stepsub { fill: var(--ink2); font-size: 12px; }
  .vt { fill: var(--ink); font-size: 12.5px; font-weight: 600; }
  .vs { fill: var(--ink2); font-size: 11.5px; }
  .note { fill: var(--muted); font-size: 11.5px; }""")

# Each frame: (step title, what you did, versions from newest to oldest).
# A version is (kind, title, subtitle): kind is cur, old or dm.
FRAMES = [
    ("1. Upload", "order-note.txt, first text",
     [("cur", "Version 1", "current")]),
    ("2. Overwrite", "same name, new text",
     [("cur", "Version 2", "current"), ("old", "Version 1", "older version")]),
    ("3. Delete", "Show versions off",
     [("dm", "Delete marker", "current: the file looks gone"), ("old", "Version 2", "older version"),
      ("old", "Version 1", "older version")]),
    ("4. Undo the delete", "delete the marker",
     [("cur", "Version 2", "current again"), ("old", "Version 1", "older version")]),
    ("5. Bring back the text of version 1", "download it, upload it",
     [("cur", "Version 3", "current: version 1's text"), ("old", "Version 2", "older version"),
      ("old", "Version 1", "older version")]),
    ("6. Delete every version", "Show versions on",
     []),
]


def version_stack():
    w = 680
    body = [
        '<text class="title" x="16" y="28">What the bucket keeps for one file name, step by step</text>',
        '<text class="sub" x="16" y="48">Versioning on. Newest at the top. Every version you see is stored, and billed, as a whole file.</text>',
    ]
    cols, fw, fh, gx, gy = 3, 208, 236, 12, 14
    top = 66
    for i, (title, did, versions) in enumerate(FRAMES):
        fx = 16 + (i % cols) * (fw + gx)
        fy = top + (i // cols) * (fh + gy)
        body.append(f'<rect class="frame" x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="6"/>')
        y = text_lines(body, fx + 10, fy + 20, wrap(title, 30), cls="step", dy=16)
        body.append(f'<text class="stepsub" x="{fx + 10}" y="{y}">{did}</text>')
        by = y + 14
        bh = 42
        if not versions:
            body.append(f'<rect class="gone" x="{fx + 10}" y="{by}" width="{fw - 20}" height="{bh}" rx="5"/>')
            body.append(f'<text class="vt" x="{fx + fw / 2}" y="{by + 18}" text-anchor="middle">Nothing left</text>')
            body.append(f'<text class="vs" x="{fx + fw / 2}" y="{by + 34}" text-anchor="middle">no marker either: gone for good</text>')
        for kind, vt, vs in versions:
            body.append(f'<rect class="{kind}" x="{fx + 10}" y="{by}" width="{fw - 20}" height="{bh}" rx="5"/>')
            body.append(f'<text class="vt" x="{fx + 20}" y="{by + 18}">{vt}</text>')
            body.append(f'<text class="vs" x="{fx + 20}" y="{by + 34}">{vs}</text>')
            by += bh + 6
    y = top + 2 * (fh + gy) + 6
    body.append(f'<text class="note" x="16" y="{y}">Our summary of the Amazon S3 User Guide, S3 Versioning, checked 2026-10-23. Steps match Lab 05, Part C.</text>')
    svg("05-07-version-stack.svg", w, y + 14,
        "What a versioned S3 bucket keeps for one file name after each step of Lab 05",
        "Six frames, newest version at the top of each. 1, Upload: version 1, current. "
        "2, Overwrite with the same name: version 2 is current, version 1 is kept as an older version. "
        "3, Delete with Show versions off: a delete marker becomes the current version, so the file looks "
        "gone, but versions 2 and 1 are still stored. 4, Undo the delete by deleting the marker: version 2 is "
        "current again, version 1 older. 5, Bring back the text of version 1 by downloading it and uploading "
        "it again: version 3, holding version 1's text, is current; versions 2 and 1 are older versions. "
        "6, Delete every version with Show versions on: nothing is left, not even a marker; the file is gone "
        "for good. Every stored version is billed as a whole file.", body, style=STYLE)


if __name__ == "__main__":
    version_stack()
