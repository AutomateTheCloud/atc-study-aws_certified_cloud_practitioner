# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Shared pieces for the guide's chart scripts: palette, SVG writer and mark helpers.

The chart scripts run as `python3 -I source/charts/MM-PP-charts.py`. Isolated mode
leaves the script's own folder off sys.path, so each script adds it before
`import chartkit`.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "images")

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def make_style(light_extra="", dark_extra="", rules_extra=""):
    """The house <style> block. With no arguments it is exactly the block the 02.02 charts use.

    Colors are the reference palette of the dataviz skill (references/palette.md),
    validated in light and dark mode. Extra custom properties and rules are appended
    for charts that need them.
    """
    return f"""
<style>
  svg {{ --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
        --grid:#e1e0d9; --axis:#c3c2b7; --s1:#2a78d6; --s1-light:#9ec5f4; --s2:#eb6834;{light_extra} }}
  @media (prefers-color-scheme: dark) {{
    svg {{ --surface:#1a1a19; --ink:#f0efec; --ink2:#c3c2b7; --muted:#898781;
          --grid:#2c2c2a; --axis:#383835; --s1:#3987e5; --s1-light:#1c5cab; --s2:#d95926;{dark_extra} }}
  }}
  text {{ font-family: system-ui, -apple-system, "Segoe UI", sans-serif; fill: var(--ink2); font-size: 13px; }}
  .title {{ fill: var(--ink); font-size: 16px; font-weight: 600; }}
  .sub {{ fill: var(--ink2); font-size: 13px; }}
  .tick {{ fill: var(--muted); font-size: 12px; font-variant-numeric: tabular-nums; }}
  .lab {{ fill: var(--ink); font-size: 13px; }}
  .grid {{ stroke: var(--grid); stroke-width: 1; }}
  .axis {{ stroke: var(--axis); stroke-width: 1; }}
  .s1 {{ fill: var(--s1); }} .s1l {{ fill: var(--s1-light); }} .s2 {{ fill: var(--s2); }}
  .line-ink {{ stroke: var(--ink); stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }}
  .line-s1 {{ stroke: var(--s1); stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }}
  .dot-s1 {{ fill: var(--s1); stroke: var(--surface); stroke-width: 2; }}
  .lead {{ stroke: var(--muted); stroke-width: 1; }}{rules_extra}
</style>"""


STYLE = make_style()


def svg(name, w, h, title, desc, body, style=STYLE):
    """Write images/<name>: a titled, described SVG with the house style and a surface fill."""
    doc = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-labelledby="t d">\n<title id="t">{title}</title>\n<desc id="d">{desc}</desc>\n'
        f"{style}\n"
        f'<rect width="{w}" height="{h}" fill="var(--surface)" style="fill:var(--surface)"/>\n'
        + "\n".join(body)
        + "\n</svg>\n"
    )
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w") as f:
        f.write(doc)


def top_rounded(x, y, w, h, r=4):
    """A bar rising from the baseline with a 4px rounded top and a square base."""
    r = min(r, h, w / 2)
    return (f"M{x:.1f},{y + h:.1f} L{x:.1f},{y + r:.1f} Q{x:.1f},{y:.1f} {x + r:.1f},{y:.1f} "
            f"L{x + w - r:.1f},{y:.1f} Q{x + w:.1f},{y:.1f} {x + w:.1f},{y + r:.1f} L{x + w:.1f},{y + h:.1f} Z")


def right_rounded(x, y, w, h, r=4):
    """A horizontal bar growing from the left with a 4px rounded right end."""
    r = min(r, w, h / 2)
    return (f"M{x:.1f},{y:.1f} L{x + w - r:.1f},{y:.1f} Q{x + w:.1f},{y:.1f} {x + w:.1f},{y + r:.1f} "
            f"L{x + w:.1f},{y + h - r:.1f} Q{x + w:.1f},{y + h:.1f} {x + w - r:.1f},{y + h:.1f} L{x:.1f},{y + h:.1f} Z")


def month_axes(body, left, top, pw, ph, ymax, ylabel, fmt=str, step=1):
    """Horizontal gridlines with y ticks, a y-axis label, and Jan-Dec under 12 equal bands."""
    for v in range(0, ymax + 1, step):
        y = top + ph - ph * v / ymax
        body.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{left}" x2="{left + pw}" y1="{y:.1f}" y2="{y:.1f}"/>')
        body.append(f'<text class="tick" x="{left - 8}" y="{y + 4:.1f}" text-anchor="end">{fmt(v)}</text>')
    body.append(f'<text class="tick" x="16" y="{top - 14}">{ylabel}</text>')
    band = pw / len(MONTHS)
    for i, m in enumerate(MONTHS):
        body.append(f'<text class="tick" x="{left + band * i + band / 2:.1f}" y="{top + ph + 18}" text-anchor="middle">{m}</text>')
    return band


def swatch(body, x, y, cls, label):
    """A legend entry: a 12px rounded square in a fill class, then its label."""
    body.append(f'<rect class="{cls}" x="{x}" y="{y - 10}" width="12" height="12" rx="2"/>')
    body.append(f'<text x="{x + 18}" y="{y}">{label}</text>')


def line_key(body, x, y, cls, label):
    """A legend entry: a short line in a stroke class, then its label."""
    body.append(f'<line class="{cls}" x1="{x}" x2="{x + 16}" y1="{y - 4}" y2="{y - 4}"/>')
    body.append(f'<text x="{x + 22}" y="{y}">{label}</text>')


def wrap(text, width):
    """Split text into lines of at most `width` characters, breaking at spaces."""
    lines, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > width:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}" if line else word
    if line:
        lines.append(line)
    return lines


def text_lines(body, x, y, lines, cls=None, dy=17, anchor=None):
    """Write lines of text, one under another, starting at baseline y. Returns the next baseline."""
    c = f' class="{cls}"' if cls else ""
    a = f' text-anchor="{anchor}"' if anchor else ""
    for line in lines:
        body.append(f'<text{c} x="{x}" y="{y:.1f}"{a}>{line}</text>')
        y += dy
    return y
