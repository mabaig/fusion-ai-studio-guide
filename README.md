# Oracle AI Agent Studio CLI + Claude Code — a step-by-step guide

A complete, figure-by-figure walkthrough of the **Oracle Fusion AI Agent Studio CLI** (released in
**26C**) driven from **Claude Code** — from cloning Oracle's repo to a validated, running agentic app.

**📖 Read it here: <https://mabaig.github.io/fusion-ai-studio-guide/>**

> **This is not Oracle's repository.** It is an independent guide *about* Oracle's public
> [`oracle/fusion-ai-studio`](https://github.com/oracle/fusion-ai-studio) repo. Nothing here is
> affiliated with or endorsed by Oracle. For the toolkit itself, go to Oracle's repo.

Oracle's own how-to is written for Codex. This one covers Claude Code, including the one extra wiring
step Oracle's guide does not mention — Claude Code reads skills from `.claude/skills/`, not
`.agents/skills/`.

---

## What the guide covers

| § | Section |
| --- | --- |
| 01–04 | What this actually is, who it is for, the five rules, prerequisites |
| 05 | **Setup, steps 1–10** — repo, workspace, VS Code extension, skills, Claude Code wiring, samples, auth (basic *and* IDCS OAuth), secrets, CLI check, `CLAUDE.md` |
| 06 | **Your first build, steps 11–16** — one paragraph in, a validated and published agentic app out |
| 07–10 | Every skill explained, slash commands, the full 288-command CLI map, agentic apps explained |
| 11–12 | What goes wrong and the fix, and keeping it current |

34 figures: 12 diagrams drawn for the guide, 22 screenshots taken while working through the steps.

---

## What is in here

```text
docs/                GitHub Pages serves this folder
├── index.html       the guide — canonical, dark/light aware, copy-to-clipboard code blocks
├── BLOG.md          the same guide in markdown
├── images/          34 figures in WebP · 2.9 MB total
│   └── src/         the 12 diagram SVGs + render.py that draws them
└── social/          Open Graph and LinkedIn cards
```

The diagrams are original SVG, not screenshots — edit `docs/images/src/render.py` and re-run it to
restyle or translate them.

---

## Tested against

| | |
| --- | --- |
| Oracle release | `release-26C` |
| CLI version | `1.0.1784919021375` |
| CLI commands | 288 |
| Skills | 3 (`aistudio`, `aistudio-apps-succession-management`, `aistudio-apps-warehouse-operations-shortages`) |
| Prompt references | 30, plus 27 workflow node prompts |
| Sample artifacts | 167 across 16 Fusion modules |

Oracle updates its repo. Check the change log at the top of
[Oracle's README](https://github.com/oracle/fusion-ai-studio) before following along, and see §12 of
the guide for the update routine.

---

## Links

- [oracle/fusion-ai-studio](https://github.com/oracle/fusion-ai-studio) — the repo everything comes from
- [Oracle Fusion AI documentation](https://docs.oracle.com/en/cloud/saas/fusion-ai/)
- [Claude Code](https://claude.com/claude-code)
