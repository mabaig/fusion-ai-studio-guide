#!/usr/bin/env python3
"""Author the twelve non-screenshot figures as original SVG diagrams.

Style is deliberately unlike the captured slide deck: no cream ground, no
terracotta, no hand-drawn script, no oversized display numerals. These use the
blog's own code-panel palette, which the stylesheet already treats as a
first-class element in both light and dark themes.
"""
import html
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ── palette: the blog's code panel, which stays a terminal in both themes ──
BG = "#1A1D24"
RAISE = "#22262F"
SUNK = "#14171D"
INK = "#E4E7EC"
INK2 = "#B9C0CC"
DIM = "#8C94A3"
RULE = "#31363F"
RULE2 = "#454B57"
ACC = "#F0B429"
ACC_D = "#8A6E23"
OK = "#4FBE86"
CRIT = "#E8776B"

SANS = "Helvetica Neue, Helvetica, Arial, sans-serif"
SERIF = "Charter, Bitstream Charter, Sitka Text, Cambria, Georgia, serif"
MONO = "SF Mono, Menlo, Consolas, monospace"


def esc(t):
    return html.escape(str(t), quote=False)


def txt(x, y, t, *, size=14, fill=INK, font=SANS, weight=400, anchor="start",
        ls=None, op=None, style=None):
    a = [f'x="{x}"', f'y="{y}"', f'font-family="{font}"',
         f'font-size="{size}"', f'fill="{fill}"']
    if weight != 400:
        a.append(f'font-weight="{weight}"')
    if anchor != "start":
        a.append(f'text-anchor="{anchor}"')
    if ls:
        a.append(f'letter-spacing="{ls}"')
    if op:
        a.append(f'opacity="{op}"')
    if style:
        a.append(f'font-style="{style}"')
    return f'<text {" ".join(a)}>{esc(t)}</text>'


def rich(x, y, runs, *, size=14, font=SANS, weight=400, ls=None):
    """One line of text made of (string, colour) runs."""
    extra = f' letter-spacing="{ls}"' if ls else ""
    parts = [f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}"'
             f' font-weight="{weight}"{extra}>']
    for s, c in runs:
        parts.append(f'<tspan fill="{c}">{esc(s)}</tspan>')
    parts.append("</text>")
    return "".join(parts)


def rect(x, y, w, h, *, fill="none", stroke=None, r=4, sw=1, dash=None, op=None):
    a = [f'x="{x}"', f'y="{y}"', f'width="{w}"', f'height="{h}"', f'rx="{r}"',
         f'fill="{fill}"']
    if stroke:
        a += [f'stroke="{stroke}"', f'stroke-width="{sw}"']
    if dash:
        a.append(f'stroke-dasharray="{dash}"')
    if op:
        a.append(f'opacity="{op}"')
    return f"<rect {' '.join(a)}/>"


def line(x1, y1, x2, y2, *, stroke=RULE, sw=1, dash=None):
    a = [f'x1="{x1}"', f'y1="{y1}"', f'x2="{x2}"', f'y2="{y2}"',
         f'stroke="{stroke}"', f'stroke-width="{sw}"']
    if dash:
        a.append(f'stroke-dasharray="{dash}"')
    return f"<line {' '.join(a)}/>"


def arrow_down(x, y1, y2, *, stroke=RULE2):
    return (line(x, y1, x, y2 - 7, stroke=stroke, sw=1.5) +
            f'<path d="M{x - 4.5} {y2 - 8} L{x} {y2} L{x + 4.5} {y2 - 8} Z" fill="{stroke}"/>')


def arrow_right(x1, x2, y, *, stroke=RULE2, dash=None):
    return (line(x1, y, x2 - 7, y, stroke=stroke, sw=1.5, dash=dash) +
            f'<path d="M{x2 - 8} {y - 4.5} L{x2} {y} L{x2 - 8} {y + 4.5} Z" fill="{stroke}"/>')


def arrow_left(x1, x2, y, *, stroke=RULE2, dash=None):
    """Arrow from x1 leftwards to x2."""
    return (line(x1, y, x2 + 7, y, stroke=stroke, sw=1.5, dash=dash) +
            f'<path d="M{x2 + 8} {y - 4.5} L{x2} {y} L{x2 + 8} {y + 4.5} Z" fill="{stroke}"/>')


def eyebrow(x, y, t):
    return txt(x, y, t.upper(), size=10.5, fill=ACC, font=MONO, ls="1.6")


def svg(name, w, h, body, *, label):
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
           f'width="{w}" height="{h}" role="img" aria-label="{esc(label)}">'
           f'<rect width="{w}" height="{h}" fill="{BG}"/>'
           f'{body}</svg>')
    with open(os.path.join(OUT, name + ".svg"), "w") as f:
        f.write(doc)
    wrap = ("<!doctype html><meta charset=utf-8>"
            "<style>html,body{margin:0;padding:0;background:%s}svg{display:block}</style>%s"
            % (BG, doc))
    with open(os.path.join(OUT, name + ".html"), "w") as f:
        f.write(wrap)
    print(f"{name:34s} {w}x{h}")
    return (name, w, h)


PAD = 46
JOBS = []

# ════════════════════════════════════════════ 11 — the repo at a glance
W, H = 900, 452
b = []
b.append(eyebrow(PAD, 52, "the repo"))
b.append(txt(PAD, 88, "One public repo. Three folders.", size=26, weight=700, ls="-0.5"))
b.append(txt(PAD, 118, "github.com/oracle/fusion-ai-studio", size=13, fill=ACC, font=MONO))
b.append(line(PAD, 146, W - PAD, 146))
b.append(txt(PAD, 176, "release-26C/", size=13.5, fill=INK, font=MONO, weight=600))
rows = [
    ("├── aiapps/", "167 sample artifacts across 16 Fusion modules",
     "99 .wf  ·  62 .bo  ·  4 .app  ·  2 tools"),
    ("├── aistudio/", "the skill, the CLI and the VS Code extension",
     "SKILL.md  ·  288 CLI commands  ·  30 prompt references"),
    ("└── how-to/", "Oracle's own written guides",
     "install  ·  configure OAuth  ·  uptake updates"),
]
y = 206
for lab, desc, meta in rows:
    b.append(txt(PAD + 8, y + 18, lab, size=13, fill=INK, font=MONO))
    b.append(txt(PAD + 172, y + 15, desc, size=14.5, fill=INK2, font=SERIF))
    b.append(txt(PAD + 172, y + 36, meta, size=11.5, fill=DIM, font=MONO))
    y += 62
    b.append(line(PAD + 8, y - 8, W - PAD, y - 8))
b.append(rect(PAD, 384, W - 2 * PAD, 34, fill=SUNK, stroke=RULE))
b.append(txt(PAD + 16, 406, "nothing in this guide lives outside release-26C",
             size=12, fill=DIM, font=MONO))
JOBS.append(svg("11-repo-at-a-glance", W, H, "".join(b),
                label="Diagram of the oracle/fusion-ai-studio repository: release-26C contains "
                      "aiapps with 167 sample artifacts, aistudio with the skill, the 288-command "
                      "CLI and the VS Code extension, and how-to with Oracle's written guides."))

# ════════════════════════════════════ 01 / 02 — the two sides of the boundary


def side(name, *, eb, title, boundary, boxes, edge, edge_side, label):
    W, H = 900, 516
    b = [eyebrow(PAD, 52, eb), txt(PAD, 88, title, size=26, weight=700, ls="-0.5")]
    bx, bw = (PAD, 600) if edge_side == "right" else (W - PAD - 600, 600)
    by, bh = 124, 348
    b.append(rect(bx, by, bw, bh, fill="none", stroke=RULE2, dash="5 5", r=6))
    b.append(txt(bx + bw / 2, by + 26, boundary.upper(), size=10.5, fill=DIM,
                 font=MONO, ls="1.4", anchor="middle"))
    top, boxh, gap = by + 44, 74, 30
    for i, (head, sub, kind) in enumerate(boxes):
        y = top + i * (boxh + gap)
        fill = SUNK if kind == "files" else RAISE
        stroke = ACC if kind == "accent" else RULE2
        b.append(rect(bx + 34, y, bw - 68, boxh, fill=fill, stroke=stroke,
                      sw=1.5 if kind == "accent" else 1))
        if kind == "files":
            hx = bx + bw / 2
            b.append(txt(hx, y + 33, head, size=17, fill=INK, font=MONO,
                         weight=600, anchor="middle", ls="1.5"))
            b.append(txt(hx, y + 56, sub, size=12.5, fill=DIM, font=SERIF, anchor="middle"))
        else:
            b.append(txt(bx + bw / 2, y + 32, head, size=17,
                         fill=ACC if kind == "accent" else INK,
                         weight=600, anchor="middle"))
            b.append(txt(bx + bw / 2, y + 55, sub, size=13, fill=DIM, font=SERIF,
                         anchor="middle"))
        if i < len(boxes) - 1:
            b.append(arrow_down(bx + bw / 2, y + boxh + 4, y + boxh + gap - 4))
    for ey, lab, sub, dash in edge:
        if edge_side == "right":
            b.append(arrow_right(bx + bw + 10, W - PAD - 4, ey, dash=dash,
                                 stroke=ACC if not dash else RULE2))
            b.append(txt(bx + bw + 14, ey - 12, lab, size=12, fill=ACC if not dash else DIM,
                         font=MONO))
            b.append(txt(bx + bw + 14, ey + 22, sub, size=11, fill=DIM, font=MONO))
        else:
            if dash:
                b.append(arrow_left(bx - 10, PAD + 4, ey, dash=dash, stroke=RULE2))
            else:
                b.append(arrow_right(PAD + 4, bx - 10, ey, stroke=ACC))
            b.append(txt(PAD + 4, ey - 12, lab, size=12, fill=ACC if not dash else DIM,
                         font=MONO))
            b.append(txt(PAD + 4, ey + 22, sub, size=11, fill=DIM, font=MONO))
    return svg(name, W, H, "".join(b), label=label)


JOBS.append(side(
    "01-workspace-side",
    eb="on your machine", title="You produce files. Nothing else.",
    boundary="your workspace",
    boxes=[("Coding agent", "Claude Code, Codex, your editor", "plain"),
           ("aistudio skill + CLI", "Oracle's expertise, written down as files", "accent"),
           (".app   .wf   .bo", "the only files Oracle accepts", "files")],
    edge=[(388, "send it over", "", None)], edge_side="right",
    label="Diagram: inside your workspace a coding agent drives the aistudio skill and CLI, "
          "which write .app, .wf and .bo files — the only files Oracle accepts. Those files are "
          "then sent over to Oracle."))

JOBS.append(side(
    "02-oracle-side",
    eb="then oracle's side", title="Oracle checks, then Oracle builds.",
    boundary="oracle fusion cloud applications",
    boxes=[("Oracle AI Agent Studio", "checks every file before it runs", "accent"),
           ("Oracle builds the screens", "using its own approved parts", "plain"),
           ("End users", "inside Fusion Applications", "plain")],
    edge=[(206, "your files arrive", "rejected if anything is wrong", None),
          (400, "look up what exists", "reading only, never changing", "5 4")],
    edge_side="left",
    label="Diagram: the files arrive at Oracle AI Agent Studio, which checks every one before it "
          "runs and rejects anything wrong. Oracle then builds the screens from its own approved "
          "parts for end users inside Fusion Applications, reading business data but never "
          "changing it."))

# ════════════════════════════════════════════════════ numbered-row figures


def rowfig(name, w, h, eb, title, rows, *, right_head=None, foot=None, label,
           title_size=26, rowh=None, sub=True):
    b = [eyebrow(PAD, 52, eb)]
    ty = 88
    for ln in title if isinstance(title, list) else [title]:
        b.append(txt(PAD, ty, ln, size=title_size, weight=700, ls="-0.5")
                 if isinstance(ln, str)
                 else rich(PAD, ty, ln, size=title_size, weight=700, ls="-0.5"))
        ty += title_size + 8
    top = ty + 18
    if right_head:
        b.append(txt(w - PAD, top - 10, right_head.upper(), size=10, fill=DIM,
                     font=MONO, ls="1.3", anchor="end"))
    b.append(line(PAD, top, w - PAD, top))
    rh = rowh or ((h - (foot and 58 or 24) - top) / len(rows))
    for i, (num, head, right) in enumerate(rows):
        y = top + i * rh
        b.append(txt(PAD, y + (32 if sub else 30), num, size=11.5, fill=ACC, font=MONO))
        b.append(txt(PAD + 44, y + 30, head, size=18, weight=700, ls="-0.3"))
        if right:
            b.append(txt(w - PAD, y + 30, right, size=13.5, fill=DIM, font=SERIF,
                         anchor="end"))
        b.append(line(PAD, y + rh, w - PAD, y + rh))
    if foot:
        b.append(txt(PAD, h - 24, foot, size=12, fill=DIM, font=MONO))
    return svg(name, w, h, "".join(b), label=label)


JOBS.append(rowfig(
    "10-who-this-is-for", 900, 372,
    "before we go further",
    "Let me be straight about who this is for.",
    [("01", "Anyone", "stops at: a validated file"),
     ("02", "Fusion Applications customers", "stops at: live for real users"),
     ("03", "Everyone else", "stops at: the six practices")],
    right_head="how far you get",
    foot="no Fusion environment needed to build and validate",
    label="Three audiences: anyone can clone the repo and build and validate files locally, "
          "Fusion Applications customers can publish to real users, and everyone else can take "
          "the six practices."))

# ═══════════════════════════════════════════════════════ the six practice cards
RULES = [
    ("04-practice-01-contract", "01",
     [("Agree the contract ", INK), ("before any code.", ACC)],
     ["Nothing gets built until the plan is written down and you agree to it:",
      "the screens, the panels, and an explicit list of what it will not build",
      "yet. Arguing with a paragraph is free. A generated build is a rebuild."],
     "the agent hands you a written scope and waits"),
    ("05-practice-02-read-only", "02",
     [("Read-only until a human ", INK), ("opens the gate.", ACC)],
     ["Out of the box the app can look but never change anything. Every action",
      "that touches a real record is named, switched on by hand, and asks",
      "before it fires."],
     "least privilege as a default, not as a policy document"),
    ("06-practice-03-discover", "03",
     [("Discover first, and leave ", INK), ("what you find alone.", ACC)],
     ["The agent searches the workspace first, finds what already exists, and",
      "reuses it. It builds only what is genuinely missing, and never edits or",
      "renames the rest, because other artifacts call those by name."],
     "the most expensive agent rebuilds what already existed"),
    ("07-practice-04-graph-or-loop", "04",
     [("Know which shape ", INK), ("you are in.", ACC)],
     ["A graph is fixed nodes and edges: same input, same path, and when it",
      "breaks you know which node broke. A loop is the model choosing its next",
      "action until it decides it is done: flexible, and prone to wandering."],
     "the mistake is not picking wrong, it is not knowing which you are in"),
    ("08-practice-05-loop-to-graph", "05",
     [("Loop to learn, ", INK), ("graph to ship.", ACC)],
     ["Explore in the loop where a human is watching, then freeze the path it",
      "proved into a graph for production. Where one step stays open-ended, put",
      "a bounded loop inside a single node, with a hard cap on iterations."],
     "the graph owns control flow, the loop owns local judgement"),
    ("09-practice-06-validated", "06",
     [("Validation is the ", INK), ("definition of done.", ACC)],
     ["When the build finishes the agent does not announce that it is done. It",
      "runs the checks first, and if they have not passed it treats the work as",
      "unfinished and fixes it before anything else."],
     "done is a prediction; a check passing is evidence"),
]
for name, num, title, body, foot in RULES:
    W, H = 900, 296
    b = [eyebrow(PAD, 52, "agent engineering practice")]
    b.append(txt(PAD, 132, num, size=64, fill=RULE2, font=MONO, weight=600))
    b.append(rich(PAD + 118, 96, title, size=30, weight=700, ls="-0.6"))
    y = 140
    for ln in body:
        b.append(txt(PAD + 118, y, ln, size=15.5, fill=INK2, font=SERIF))
        y += 27
    b.append(line(PAD + 118, 226, W - PAD, 226))
    b.append(txt(PAD + 118, 252, foot, size=12, fill=DIM, font=MONO))
    JOBS.append(svg(name, W, H, "".join(b),
                    label=f"Practice {num}: " + "".join(s for s, _ in title) + " " + " ".join(body)))

# ════════════════════════════════════════════ 03 — what an agentic app is
W, H = 900, 384
b = [eyebrow(PAD, 52, "so what is an agentic app")]
b.append(rich(PAD, 88, [("It is not a chatbot ", INK), ("bolted onto a dashboard.", ACC)],
              size=26, weight=700, ls="-0.5"))
NY, NH = 130, 150
GAP = 56
NW = [160, 200, 130, 150]
NX = [PAD]
for _w in NW[:-1]:
    NX.append(NX[-1] + _w + GAP)
nodes = [
    (NX[0], NW[0], "Live business data", ["performance, risk,", "pay, plans"], "plain"),
    (NX[1], NW[1], "Agent workspace",
     ["spot what needs attention", "explain why it matters", "suggest what to do"], "accent"),
    (NX[2], NW[2], "A human says yes", ["nothing changes", "without this"], "gate"),
    (NX[3], NW[3], "Record created", ["a real record in", "Fusion Applications"], "record"),
]
for x, w_, head, subs, kind in nodes:
    stroke = ACC if kind == "accent" else (OK if kind == "record" else RULE2)
    fill = RAISE if kind != "record" else SUNK
    b.append(rect(x, NY, w_, NH, fill=fill, stroke=stroke,
                  sw=1.5 if kind in ("accent", "record") else 1,
                  dash="5 4" if kind == "gate" else None))
    cx = x + w_ / 2
    b.append(txt(cx, NY + 40, head, size=15, weight=700, anchor="middle", ls="-0.2",
                 fill=ACC if kind == "accent" else (OK if kind == "record" else INK)))
    sy = NY + 68
    for s in subs:
        b.append(txt(cx, sy, s, size=12, fill=DIM, font=SERIF, anchor="middle"))
        sy += 19
AY = NY + NH / 2
for i, (lab, col) in enumerate([("reads", DIM), ("suggests", DIM), ("approved", OK)]):
    x1 = NX[i] + NW[i] + 8
    x2 = NX[i + 1] - 8
    b.append(arrow_right(x1, x2, AY, stroke=OK if col is OK else RULE2))
    b.append(txt((x1 + x2) / 2, AY - 11, lab, size=10, fill=col, font=MONO, anchor="middle"))
BARW = NX[2] + NW[2] - PAD
b.append(rect(PAD, 296, BARW, 34, fill=SUNK, stroke=RULE))
b.append(txt(PAD + BARW / 2, 318, "nothing on this side can change your data",
             size=12.5, fill=INK2, font=MONO, anchor="middle"))
b.append(txt(NX[3] + NW[3] / 2, 318, "one write", size=12.5, fill=OK, font=MONO,
             anchor="middle"))
JOBS.append(svg("03-what-is-an-agentic-app", W, H, "".join(b),
                label="Diagram: live business data is read by an agent workspace that spots what "
                      "needs attention, explains why it matters and suggests what to do; a human "
                      "says yes; only then is a real record created in Fusion Applications. "
                      "Nothing before the human approval can change your data."))

# ════════════════════════════════════════════════════════════ 34 — closing
W, H = 900, 396
b = [eyebrow(PAD, 52, "take this home")]
b.append(rich(PAD, 96, [("How you ship agents when", INK)], size=31, weight=700, ls="-0.7"))
b.append(rich(PAD, 134, [("a wrong answer is not an option.", ACC)], size=31, weight=700,
              ls="-0.7"))
b.append(line(PAD, 176, W - PAD, 176))
cols = [("01", ["Contract", "first"]), ("02", ["Read-only", "default"]),
        ("03", ["Discover", "first"]), ("04", ["Graph or", "loop"]),
        ("05", ["Loop then", "graph"]), ("06", ["Checks", "pass"])]
cw = (W - 2 * PAD) / 6
for i, (num, words) in enumerate(cols):
    x = PAD + i * cw
    if i:
        b.append(line(x, 176, x, 304))
    b.append(txt(x + cw / 2, 214, num, size=11.5, fill=ACC, font=MONO, anchor="middle"))
    yy = 248
    for wd in words:
        b.append(txt(x + cw / 2, yy, wd, size=17, weight=700, anchor="middle", ls="-0.3"))
        yy += 24
b.append(line(PAD, 304, W - PAD, 304))
b.append(txt(PAD, 340, "Not Oracle-specific.", size=15.5, fill=INK2, font=SERIF))
b.append(txt(PAD + 152, 340, "Use them on whatever you build next.", size=15.5, fill=DIM,
             font=SERIF))
JOBS.append(svg("34-practices-closing", W, H, "".join(b),
                label="Closing summary: how you ship agents when a wrong answer is not an option "
                      "- contract first, read-only default, discover first, graph or loop, loop "
                      "then graph, checks pass. Not Oracle-specific."))

with open(os.path.join(OUT, "manifest.txt"), "w") as f:
    for name, w, h in JOBS:
        f.write(f"{name} {w} {h}\n")
print(f"\n{len(JOBS)} figures written")
