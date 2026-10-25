#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""End each answer-choice line that is followed by another with a hard break (a trailing backslash).

The site joins consecutive lines into one paragraph, so "A. ..." / "B. ..." lines show as one run-on
line unless each ends with a backslash or the choices are a bulleted list. Idempotent; skips fenced code.

Usage, from the repository root: python3 source/tools/fix_choice_breaks.py guide/*/*.md
"""
import re
import sys
from pathlib import Path
pat=re.compile(r'^((?:> ?)*\s*)([A-F])[.)] \S')
total=0
for f in sys.argv[1:]:
    p=Path(f); lines=p.read_text().split('\n'); n=0; fence=False
    for i,l in enumerate(lines):
        if l.lstrip('> ').startswith('```'): fence=not fence
        if fence or i+1>=len(lines): continue
        if pat.match(l) and pat.match(lines[i+1]) and not l.rstrip().endswith('\\'):
            lines[i]=l.rstrip()+'\\'; n+=1
    if n: p.write_text('\n'.join(lines)); total+=n
print(total)
