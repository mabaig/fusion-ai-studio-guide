#!/usr/bin/env python3
"""Draw the share cards. Same palette and type as the guide's diagrams.

Writes:
  docs/social/og-card.svg      1200x630  — Open Graph / Twitter preview (public)
  publishing/linkedin-card.svg 1200x627  — LinkedIn native post image (kept local)

Rasterise with:
  chrome --headless=new --force-device-scale-factor=2 --window-size=W,H \
         --screenshot=out.png file://.../<name>.html
then downscale by 2 for a crisp 1x PNG.
"""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
OG_DIR = os.path.join(ROOT, "docs", "social")
LI_DIR = os.path.join(ROOT, "publishing")

BG = "#1A1D24"; SUNK = "#14171D"
INK = "#E4E7EC"; INK2 = "#B9C0CC"; DIM = "#8C94A3"
RULE = "#31363F"; RULE2 = "#454B57"; ACC = "#F0B429"

SANS = "Helvetica Neue, Helvetica, Arial, sans-serif"
SERIF = "Charter, Bitstream Charter, Sitka Text, Cambria, Georgia, serif"
MONO = "SF Mono, Menlo, Consolas, monospace"

HEAD_A = "Oracle let the AI write the files."
HEAD_B = "It kept the checks for itself."
DEK = ["Inside Fusion 26C's AI Agent Studio CLI - the boundary",
       "that makes agentic apps safe on real ERP data."]
RULES = [("01", "Contract first"), ("02", "Read-only"), ("03", "Discover first"),
         ("04", "Graph or loop"), ("05", "Loop then graph"), ("06", "Checks pass")]
AUTHOR = "Baig Mohammed"
HANDLE = "linkedin.com/in/mbaig162"


def t(x, y, s, size=14, fill=INK, font=SANS, w=400, anchor="start", ls=None):
    a = f'x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{fill}"'
    if w != 400:
        a += f' font-weight="{w}"'
    if anchor != "start":
        a += f' text-anchor="{anchor}"'
    if ls:
        a += f' letter-spacing="{ls}"'
    return f"<text {a}>{s}</text>"


def line(x1, y1, x2, y2, stroke=RULE, sw=1):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{stroke}" stroke-width="{sw}"/>')


def card(name, out_dir, W, H):
    P = 64
    b = [f'<rect width="{W}" height="{H}" fill="{BG}"/>',
         f'<rect x="0" y="0" width="{W}" height="6" fill="{ACC}"/>']
    b.append(t(P, P + 40, "ORACLE FUSION 26C  ·  AI AGENT STUDIO CLI",
               size=15, fill=ACC, font=MONO, ls="2"))
    b.append(t(P, P + 116, HEAD_A, size=52, w=700, ls="-1.3"))
    b.append(t(P, P + 180, HEAD_B, size=52, fill=ACC, w=700, ls="-1.3"))
    b.append(line(P, P + 224, W - P, P + 224, RULE2))
    y = P + 266
    for ln in DEK:
        b.append(t(P, y, ln, size=23, fill=INK2, font=SERIF))
        y += 33

    # five-rule strip
    sy = H - 168
    b.append(line(P, sy, W - P, sy, RULE))
    cw = (W - 2 * P) / len(RULES)
    for i, (n, lab) in enumerate(RULES):
        x = P + i * cw
        if i:
            b.append(line(x, sy, x, sy + 92, RULE))
        b.append(t(x + cw / 2, sy + 36, n, size=15, fill=ACC, font=MONO, anchor="middle"))
        b.append(t(x + cw / 2, sy + 70, lab, size=20, w=700, anchor="middle", ls="-0.3"))
    b.append(line(P, sy + 92, W - P, sy + 92, RULE))

    # byline
    b.append(t(P, H - 30, AUTHOR, size=17, w=700, ls="-0.2"))
    b.append(t(W - P, H - 30, HANDLE, size=13, fill=DIM, font=MONO, anchor="end"))

    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
           f'width="{W}" height="{H}">' + "".join(b) + "</svg>")
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, name + ".svg"), "w").write(doc)
    open(os.path.join(out_dir, name + ".html"), "w").write(
        "<!doctype html><meta charset=utf-8>"
        "<style>html,body{margin:0;background:%s}svg{display:block}</style>%s" % (BG, doc))
    print(f"{name:16s} {W}x{H}  -> {out_dir}")


card("og-card", OG_DIR, 1200, 630)
card("linkedin-card", LI_DIR, 1200, 627)
