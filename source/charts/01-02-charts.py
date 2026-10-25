#!/usr/bin/env python3
# Copyright 2026 Automate the Cloud Inc.
# SPDX-License-Identifier: Apache-2.0
"""Draw the graphics for lesson 01.02 (networks, IP addresses, DNS and HTTPS) as SVG.

Usage: python3 -I source/charts/01-02-charts.py
Writes images/01-02-*.svg. Facts, checked 2026-10-24: DNS turns names into IP
addresses (AWS, "What is DNS?"); routers pass packets between networks (AWS,
"What is routing?"); an IPv4 address is 32 bits written as four numbers from 0
to 255, an IPv6 address 128 bits written as eight groups of hexadecimal digits,
with :: for consecutive zero groups (Amazon VPC User Guide, "IP addressing for
your VPCs and subnets"); IPv4 has about 4.3 billion (2^32) addresses, all
already allocated (AWS, "What is IPv4?"); HTTP sends plaintext, HTTPS adds TLS
encryption and a certificate that proves the server's identity, default ports 80
and 443 (AWS, "HTTP vs HTTPS"). Addresses and the .example name come from ranges
reserved for documentation. Port 22 for SSH is from the Amazon EC2 User Guide's
security group rules reference. The bakery and its customer are made up for
teaching. Our own design: no AWS logos, icons, trade dress or AWS diagrams.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chartkit import make_style, svg, text_lines, wrap  # noqa: E402

STYLE = make_style(
    light_extra=" --hi-fill:#d9e8fb; --n-fill:#f1f0ec;",
    dark_extra=" --hi-fill:#1b3554; --n-fill:#252523;",
    rules_extra="""
  .hi { fill: var(--hi-fill); stroke: var(--s1); stroke-width: 1.8; }
  .hiband { fill: var(--hi-fill); stroke: none; }
  .n { fill: var(--n-fill); stroke: var(--ink2); stroke-width: 1.2; }
  .plain { fill: var(--surface); stroke: var(--ink2); stroke-width: 1.2; }
  .frame { fill: none; stroke: var(--ink); stroke-width: 1.8; }
  .tunnel { fill: none; stroke: var(--s1); stroke-width: 2.2; }
  .cellt { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .small { fill: var(--ink2); font-size: 12px; }
  .head { fill: var(--ink); font-size: 13px; font-weight: 600; }
  .zlab { fill: var(--muted); font-size: 12px; }
  .mono { fill: var(--ink); font-size: 13px; font-family: ui-monospace, "SFMono-Regular", Menlo, monospace; }
  .bigmono { fill: var(--ink); font-size: 22px; font-weight: 600; font-family: ui-monospace, "SFMono-Regular", Menlo, monospace; }
  .arrlab { fill: var(--ink2); font-size: 12px; font-style: italic; }
  .note { fill: var(--muted); font-size: 11.5px; }
  .arrow { stroke: var(--ink2); stroke-width: 1.5; fill: none; }
  .arrowhead { fill: var(--ink2); }
  .rowl { fill: var(--ink); font-size: 12px; font-weight: 600; }
  .num { fill: var(--ink); font-size: 13px; font-weight: 700; }
  .numc { fill: var(--surface); stroke: var(--ink); stroke-width: 1.5; }
  .numh { fill: var(--s1); stroke: var(--s1); stroke-width: 1.5; }
  .numhl { fill: var(--surface); font-size: 13px; font-weight: 700; }""")


def arrow(body, x1, y1, x2, y2):
    body.append(f'<line class="arrow" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 8 * math.cos(a) + 5 * math.sin(a), y2 - 8 * math.sin(a) - 5 * math.cos(a))
    p2 = (x2 - 8 * math.cos(a) - 5 * math.sin(a), y2 - 8 * math.sin(a) + 5 * math.cos(a))
    body.append(f'<path class="arrowhead" d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{x2:.1f},{y2:.1f} Z"/>')


def rect(body, cls, x, y, w, h, r=6):
    body.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}"/>')


def marker(body, x, y, n, hi=False):
    body.append(f'<circle class="{"numh" if hi else "numc"}" cx="{x}" cy="{y}" r="11"/>')
    body.append(f'<text class="{"numhl" if hi else "num"}" x="{x}" y="{y + 4.5}" text-anchor="middle">{n}</text>')


def padlock(body, x, y):
    """A small padlock drawn from shapes, top-left at (x, y)."""
    body.append(f'<path class="arrow" d="M{x + 3},{y + 8} L{x + 3},{y + 5} A5,5 0 0 1 {x + 13},{y + 5} L{x + 13},{y + 8}"/>')
    body.append(f'<rect x="{x}" y="{y + 8}" width="16" height="11" rx="2" style="fill:var(--ink2)"/>')


def big_picture():
    """Four steps from a customer's phone to the bakery's web server."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">Four steps to one web page</text>',
        '<text class="sub" x="16" y="48">What happens when a customer opens bakery.example on their phone</text>',
    ]
    top, rh, gap = 70, 92, 8
    px, pw = 16, 92          # phone column
    sx, sw = 572, 92         # server column
    mid_l, mid_r = px + pw, sx
    steps = ["Look up the name", "Travel to the address", "Secure the line", "Ask and answer"]
    total = 4 * rh + 3 * gap
    # Highlight band for step 3, behind everything.
    y3 = top + 2 * (rh + gap)
    rect(body, "hiband", mid_l + 4, y3, mid_r - mid_l - 8, rh, 6)
    rect(body, "plain", px, top, pw, total, 8)
    text_lines(body, px + pw / 2, top + total / 2 - 8, ["Customer's", "phone"], cls="cellt", dy=16, anchor="middle")
    rect(body, "plain", sx, top, sw, total, 8)
    text_lines(body, sx + sw / 2, top + total / 2 - 16, ["Bakery's", "web server", "192.0.2.10"], cls="cellt", dy=16, anchor="middle")
    for i, name in enumerate(steps):
        y = top + i * (rh + gap)
        marker(body, mid_l + 24, y + 18, i + 1, hi=(i == 2))
        body.append(f'<text class="rowl" x="{mid_l + 42}" y="{y + 22}">{name}</text>')
        if i == 0:
            dx, dw = 340, 150
            rect(body, "n", dx, y + 34, dw, 46)
            text_lines(body, dx + dw / 2, y + 54, ["DNS", "(the address book)"], cls="small", dy=15, anchor="middle")
            arrow(body, mid_l + 1, y + 46, dx - 1, y + 46)
            arrow(body, dx - 1, y + 70, mid_l + 1, y + 70)
            body.append(f'<text class="arrlab" x="{mid_l + 14}" y="{y + 42}">"Where is bakery.example?"</text>')
            body.append(f'<text class="arrlab" x="{mid_l + 14}" y="{y + 86}">"192.0.2.10"</text>')
        elif i == 1:
            hops = ["home network", "ISP", "internet", "routers"]
            hx = mid_l + 20
            hw = 104
            for j, h in enumerate(hops[:3]):
                rect(body, "n", hx + j * (hw + 12), y + 36, hw, 26, 4)
                body.append(f'<text class="small" x="{hx + j * (hw + 12) + hw / 2}" y="{y + 53}" text-anchor="middle">{h}</text>')
            arrow(body, mid_l + 1, y + 76, sx - 1, y + 76)
            body.append(f'<text class="arrlab" x="{hx + 3 * (hw + 12) + 2}" y="{y + 53}">via routers</text>')
            body.append(f'<text class="arrlab" x="{(mid_l + sx) / 2}" y="{y + 90}" text-anchor="middle">packets to 192.0.2.10, port 443</text>')
        elif i == 2:
            arrow(body, sx - 1, y + 46, mid_l + 1, y + 46)
            arrow(body, mid_l + 1, y + 72, sx - 1, y + 72)
            body.append(f'<text class="arrlab" x="{(mid_l + sx) / 2}" y="{y + 40}" text-anchor="middle">certificate: "I hold the name bakery.example"</text>')
            body.append(f'<text class="arrlab" x="{(mid_l + sx) / 2}" y="{y + 88}" text-anchor="middle">both sides agree how to encrypt</text>')
        else:
            rect(body, "tunnel", mid_l + 8, y + 32, mid_r - mid_l - 16, 54, 14)
            padlock(body, mid_l + 18, y + 49)
            arrow(body, mid_l + 44, y + 50, sx - 14, y + 50)
            arrow(body, sx - 14, y + 72, mid_l + 44, y + 72)
            body.append(f'<text class="arrlab" x="{mid_l + 200}" y="{y + 45}">request: "send me the order page"</text>')
            body.append(f'<text class="arrlab" x="{mid_l + 200}" y="{y + 84}">response: the page</text>')
    y = top + total + 24
    body.append(f'<text class="note" x="16" y="{y}">Step 4 travels inside the encrypted connection that step 3 set up. Names and addresses are reserved for examples.</text>')
    svg("01-02-big-picture.svg", w, y + 16,
        "Four steps from a phone to a web page",
        "A customer's phone on the left and the bakery's web server, 192.0.2.10, on the right, with four numbered "
        "steps between them. 1, look up the name: the phone asks DNS where bakery.example is, and DNS answers "
        "192.0.2.10. 2, travel to the address: packets cross the home network, the ISP and the internet, via "
        "routers, to 192.0.2.10 port 443. 3, highlighted, secure the line: the server sends its certificate, saying "
        "it holds the name bakery.example, and both sides agree how to encrypt. 4, ask and answer: inside an "
        "encrypted connection marked with a padlock, the request 'send me the order page' goes to the server and "
        "the page comes back.", body, style=STYLE)


def addresses_and_ports():
    """IPv4 and IPv6 addresses, then one address leading to programs on ports."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">An address finds the computer; a port finds the program</text>',
        '<text class="sub" x="16" y="48">Two kinds of IP address, and the ports on the bakery\'s web server</text>',
    ]
    top = 70
    # IPv4 panel.
    rect(body, "frame", 16, top, 316, 156, 10)
    body.append(f'<text class="head" x="30" y="{top + 24}">IPv4</text>')
    parts = ["192", "0", "2", "10"]
    x = 30
    for i, p in enumerate(parts):
        rect(body, "n", x, top + 38, 56, 40, 5)
        body.append(f'<text class="bigmono" x="{x + 28}" y="{top + 66}" text-anchor="middle">{p}</text>')
        body.append(f'<text class="zlab" x="{x + 28}" y="{top + 94}" text-anchor="middle">0 to 255</text>')
        if i < 3:
            body.append(f'<text class="bigmono" x="{x + 64}" y="{top + 66}" text-anchor="middle">.</text>')
        x += 72
    text_lines(body, 30, top + 118, ["32 bits; about 4.3 billion addresses,",
                                     "all already allocated"], cls="small", dy=16)
    # IPv6 panel.
    rect(body, "frame", 348, top, 316, 156, 10)
    body.append(f'<text class="head" x="362" y="{top + 24}">IPv6</text>')
    rect(body, "n", 362, top + 38, 288, 40, 5)
    body.append(f'<text class="mono" x="506" y="{top + 63}" text-anchor="middle">2001:db8:85a3::8a2e:370:7334</text>')
    body.append(f'<text class="zlab" x="506" y="{top + 94}" text-anchor="middle">eight groups of up to four hex digits</text>')
    text_lines(body, 362, top + 118, ["128 bits; :: stands for groups of zeros;",
                                      "vastly more addresses than IPv4"], cls="small", dy=16)
    # Address to ports.
    y = top + 186
    rect(body, "plain", 16, y + 40, 128, 60)
    text_lines(body, 80, y + 64, ["Packets to", "192.0.2.10"], cls="cellt", dy=16, anchor="middle")
    rect(body, "frame", 196, y, 468, 160, 10)
    body.append(f'<text class="head" x="210" y="{y + 22}">The bakery\'s web server, 192.0.2.10</text>')
    arrow(body, 145, y + 70, 195, y + 70)
    ports = [("443", "HTTPS", "the website, encrypted", True),
             ("80", "HTTP", "plain web, not encrypted", False),
             ("22", "SSH", "staff signing in remotely", False)]
    for i, (num, proto, what, hi) in enumerate(ports):
        py = y + 36 + i * 40
        rect(body, "hi" if hi else "n", 210, py, 440, 32, 5)
        body.append(f'<text class="rowl" x="224" y="{py + 21}">Port {num}</text>')
        body.append(f'<text class="cellt" x="300" y="{py + 21}">{proto}</text>')
        body.append(f'<text class="small" x="360" y="{py + 21}">{what}</text>')
    y += 186
    body.append(f'<text class="note" x="16" y="{y}">Addresses come from ranges reserved for examples. Other ports appear later, such as 5432 for PostgreSQL.</text>')
    svg("01-02-addresses-and-ports.svg", w, y + 16,
        "IPv4 and IPv6 addresses, and ports on one server",
        "Top left, IPv4: the address 192.0.2.10 as four numbers, each from 0 to 255, separated by dots; 32 bits; "
        "about 4.3 billion addresses, all already allocated. Top right, IPv6: the address "
        "2001:db8:85a3::8a2e:370:7334, eight groups of up to four hexadecimal digits; 128 bits; :: stands for "
        "groups of zeros; vastly more addresses than IPv4. Bottom: packets to 192.0.2.10 arrive at the bakery's web "
        "server, where three ports lead to programs: port 443, HTTPS, the website, encrypted, highlighted; port 80, "
        "HTTP, plain web, not encrypted; port 22, SSH, staff signing in remotely.", body, style=STYLE)


def http_vs_https():
    """What someone watching the path sees with HTTP and with HTTPS."""
    w = 680
    body = [
        '<text class="title" x="16" y="28">HTTPS hides the conversation from anyone on the path</text>',
        '<text class="sub" x="16" y="48">What someone watching a network between the customer and the bakery sees</text>',
    ]
    top, pw, ph = 70, 316, 300
    panels = [
        ("Plain HTTP, port 80", False,
         ["Name: Ana", "Address: 12 Mill Lane", "Order: one birthday cake"],
         ["Readable, and could be changed", "No proof the server is the real bakery", "Browser warns: not secure"]),
        ("HTTPS, port 443", True,
         ["x7#Qp!2vL0r@9sK", "mE4+tZ1q%Wb8Yc", "J5^nH3d*Fu6aR"],
         ["Scrambled: no use to the watcher", "Certificate proves the name bakery.example", "Browser marks it secure"]),
    ]
    for i, (head, hi, seen, notes) in enumerate(panels):
        x = 16 + i * (pw + 16)
        rect(body, "hi" if hi else "frame", x, top, pw, ph, 10)
        body.append(f'<text class="head" x="{x + 14}" y="{top + 24}">{head}</text>')
        # Phone, watcher, server in a row.
        ry = top + 44
        rect(body, "plain", x + 14, ry, 64, 40)
        body.append(f'<text class="small" x="{x + 46}" y="{ry + 25}" text-anchor="middle">Phone</text>')
        rect(body, "plain", x + pw - 78, ry, 64, 40)
        body.append(f'<text class="small" x="{x + pw - 46}" y="{ry + 25}" text-anchor="middle">Server</text>')
        arrow(body, x + 79, ry + 20, x + pw - 79, ry + 20)
        if hi:
            padlock(body, x + pw / 2 - 8, ry - 2)
        # What the watcher sees.
        wy = ry + 64
        body.append(f'<text class="zlab" x="{x + 14}" y="{wy}">The watcher on the path sees:</text>')
        rect(body, "n", x + 14, wy + 8, pw - 28, 80, 5)
        text_lines(body, x + 26, wy + 32, seen, cls="mono", dy=22)
        ny = wy + 116
        for j, note in enumerate(notes):
            body.append(f'<text class="small" x="{x + 14}" y="{ny + j * 22}">{"✗" if not hi else "✓"}  {note}</text>')
    y = top + ph + 24
    body.append(f'<text class="note" x="16" y="{y}">In both, the watcher can still see which two addresses are talking. The customer and order are made up.</text>')
    svg("01-02-http-vs-https.svg", w, y + 16,
        "What a watcher on the network sees with HTTP and with HTTPS",
        "Two panels, each with a phone, a server and an arrow between them. Plain HTTP, port 80: the watcher on the "
        "path reads 'Name: Ana. Address: 12 Mill Lane. Order: one birthday cake'; it is readable and could be "
        "changed, nothing proves the server is the real bakery, and the browser warns that it is not secure. HTTPS, port 443, "
        "highlighted, with a padlock on the arrow: the watcher sees scrambled characters only; the certificate proves "
        "the name bakery.example; the browser marks the connection as secure. A note says that in both, the watcher can still see "
        "which two addresses are talking.", body, style=STYLE)


if __name__ == "__main__":
    big_picture()
    addresses_and_ports()
    http_vs_https()
