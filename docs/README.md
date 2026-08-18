# Oracle AI Agent Studio CLI + Claude Code — step-by-step guide

A complete, screenshot-by-screenshot walkthrough for using the **Oracle Fusion AI Agent Studio CLI**
(released in **26C**) inside **Claude Code** — from cloning Oracle's repo to a validated agentic app.

Oracle's own guide is written for Codex. This one covers Claude Code, including the one extra
setup step Oracle's guide does not mention.

**Oracle's repo:** <https://github.com/oracle/fusion-ai-studio>

---

## Read it

| Format | File | Best for |
| --- | --- | --- |
| **Web page** | [`index.html`](index.html) | The canonical version — GitHub Pages, sharing a link |
| **Markdown** | [`BLOG.md`](BLOG.md) | Reading on GitHub, pasting into Dev.to / Confluence |

`index.html` and `BLOG.md` cover the same 12 sections; the Markdown version carries five extra
figures (the individual rule cards).

### View the web page

Just open `index.html` in a browser — it is a single self-contained file with no build step
and no dependencies. It needs the `images/`, `img/` and `social/` folders next to it.

The page has a scroll-linked ambience layer: a drifting particle field and a rotating Oracle mark
across the hero, a document-wide progress rail, reveal-on-scroll, and a gentle depth effect on the
figures. It is deliberately front-loaded — the field fades out over the first one-and-a-half
viewports and the animation loop then stops drawing entirely, so a long read costs nothing. It
honours `prefers-reduced-motion`, and there is an **Ambience** toggle at the bottom of the sidebar
that persists your choice.

To serve it locally:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

To publish it with **GitHub Pages**: push this folder, then in your repo go to
**Settings → Pages** and set the source to branch `main`, folder `/docs`. (Pages only offers
`/ (root)` or `/docs` — that is why the guide lives in `docs/`.)
`index.html` carries Open Graph and Twitter card tags with a `CANONICAL_URL` placeholder — replace it
before publishing or the link previews will break.

---

## What is in here

```text
.
├── index.html      canonical guide (dark/light aware, copy-to-clipboard code blocks, social tags)
├── BLOG.md         the same guide in markdown
├── README.md       this file
├── images/         34 figures — 12 diagrams, 22 annotated screenshots · WebP, 2.9 MB total
│   └── src/        the diagram SVG sources plus render.py
└── social/         linkedin-card.png (1200×627) and og-card.png (1200×630), plus SVGs
```

Every image is WebP: lossless for the 12 diagrams so the type stays crisp, quality 82 for the
screenshots. The whole folder is 3.1 MB, down from 14.1 MB as PNG.

---

## What the guide covers

| § | Section | What you get |
| --- | --- | --- |
| 01 | What this actually is | The four moving parts, and why the AI/Oracle boundary makes it safe |
| 02 | Who this is for | Three audiences, three stopping points |
| 03 | The five rules | The habits Oracle baked into the skill files — worth stealing |
| 04 | Before you start | Five prerequisites, ten minutes |
| 05 | **Setup, steps 1–10** | Repo, workspace, extension, skills, Claude Code wiring, samples, auth, secrets, CLI check, `CLAUDE.md` |
| 06 | **Your first build, steps 11–16** | One paragraph in → a validated, running agentic app out |
| 07 | Every skill explained | 3 skills, 30 prompt references, 27 node prompts, 14 artifact types |
| 08 | Slash commands | What Oracle ships, plus 8 custom commands to create |
| 09 | The CLI command map | All 288 commands, grouped, with what each verb can touch |
| 10 | Agentic apps explained | Four pillars, seven widgets, `$OraMessageHint`, workflow vs supervisor, the 60-second limit |
| 11 | What goes wrong | 11 real problems and their fixes |
| 12 | Keeping it current | The update routine, and which folders are safe |

---

## The short version

If you just want the commands, here is the whole setup:

```bash
# 1. Oracle's repo
mkdir -p ~/fusion-ai-repo && cd ~/fusion-ai-repo
git clone https://github.com/oracle/fusion-ai-studio.git

# 2. your workspace (a separate folder)
mkdir -p ~/fusion-ai-workspace && cd ~/fusion-ai-workspace
mkdir -p .agents/skills

# 3. install the VS Code extension
#    unzip release-26C/aistudio/bin/aistudio-extension.zip
#    VS Code → Extensions → "..." → Install from VSIX → aistudio-extension.vsix

# 4. install the skills
#    unzip release-26C/aistudio/bin/aistudio-skill.zip
#    unzip release-26C/aistudio/aistudio-apps-skills/aistudio-apps-skills.zip
#    copy all resulting skill folders into .agents/skills/

# 5. let Claude Code see them  ← the step Oracle's guide does not cover
mkdir -p .claude/skills && cd .claude/skills
ln -s ../../.agents/skills/aistudio aistudio
ln -s ../../.agents/skills/aistudio-apps-succession-management \
      aistudio-apps-succession-management
ln -s ../../.agents/skills/aistudio-apps-warehouse-operations-shortages \
      aistudio-apps-warehouse-operations-shortages
cd ~/fusion-ai-workspace

# 6. Oracle's samples, so the agent has something to reuse
cp -R ~/fusion-ai-repo/fusion-ai-studio/release-26C/aiapps .

# 7. connect (VS Code: Cmd/Ctrl+Shift+P → "Fusion AI Studio: Configure Authentication")

# 8. protect your secrets
printf 'env.properties\n.debug/\n' > .gitignore

# 9. check the CLI
node .agents/skills/aistudio/scripts/aistudio.js --help

# 10. then just describe what you want
claude
```

On **Windows**, replace step 5 with a copy — symlinks need Developer Mode:

```powershell
New-Item -ItemType Directory -Force .claude\skills
Copy-Item -Recurse .agents\skills\* .claude\skills\
```

---

## Versions this was tested against

| | |
| --- | --- |
| Oracle release | `release-26C` |
| CLI version | `1.0.1784919021375` |
| CLI commands | 288 |
| Skills | 3 (`aistudio`, `aistudio-apps-succession-management`, `aistudio-apps-warehouse-operations-shortages`) |
| Screenshots | 34 |
| Prompt references | 30, plus 27 workflow node prompts |
| Sample artifacts | 167 across 16 Fusion modules |

Oracle updates this repo. Check the change log at the top of Oracle's
[README](https://github.com/oracle/fusion-ai-studio) before you follow along, and see
§12 of the guide for the update routine.

---

## Note on the screenshots

There are 34 images, in two groups.

**Twelve diagrams** (`01`–`11`, `34`) are drawn for this guide — original SVG, rendered to PNG, in
the same palette and type as the page itself. They replace the captured slides an earlier draft
used, so every figure in this guide is either an original diagram or a screenshot taken here. The
SVG sources live in `images/src/`, with the `render.py` that draws them and rasterises the PNGs.

**Twenty-two walkthrough screenshots** (`12`–`33`) were taken while working through the steps in
this guide on macOS. Before publishing, the following were scrubbed:

- the Fusion instance name in both IDCS scope strings, replaced with `your-env`
- the `env.properties` values on the AI Studio CLI page — client ID, host, token URL, scope and
  tenant are all redacted
- the generated Application ID

The screenshots still show a specific Fusion environment and its sample order data. Nothing in them
is real customer data, but check your own before publishing.

The diagrams are deliberately dark panels, the way the code blocks are, so they read the same in
both the light and dark theme.

---

## Links

- [oracle/fusion-ai-studio](https://github.com/oracle/fusion-ai-studio) — the repo everything comes from
- [Oracle Fusion AI documentation](https://docs.oracle.com/en/cloud/saas/fusion-ai/)
- [Oracle Fusion AI product page](https://www.oracle.com/applications/fusion-ai/)
- [Claude Code](https://claude.com/claude-code)

Oracle's own how-to guides live in the repo under `release-26C/how-to/`:

- `install-and-use-fusion-ai-studio-CLI_vscode-codex.md`
- `how-to-configure-oauth-for-aistudio-cli.md`
- `how-to-uptake-incremental-updates.md`
