# Install in Codex, Cursor, OpenCode, and other agents

Easywrite is plain Markdown (`SKILL.md` + `references/`), so it works in any harness that supports skill-style
instructions. Point the tool at the skill directory, or paste `SKILL.md` inline.

## Skills CLI (cross-runtime, easiest)
```bash
npx skills add Florent2025/easywrite
```
This detects your runtime and installs into the right directory.

## Manual per tool
```bash
# Codex
git clone https://github.com/Florent2025/easywrite.git ~/.codex/skills/easywrite

# Cursor (project-scoped)
git clone https://github.com/Florent2025/easywrite.git .cursor/skills/easywrite

# OpenCode
git clone https://github.com/Florent2025/easywrite.git ~/.config/opencode/skills/easywrite

# OpenClaw / Gemini CLI / others: clone into that tool's skills directory,
# or add SKILL.md to the project/system prompt.
```

## Paste-in (no automation)
Open [`SKILL.md`](../SKILL.md), paste its contents into the conversation or your system prompt, then give it text
to improve. For full power, also paste the relevant file from `references/` (English/中文 catalog, academic
discipline, or detector science).

## ChatGPT / Claude Projects
Upload `SKILL.md` and the `references/` files into Project Knowledge / Custom Instructions, then ask it to
humanize your draft while keeping every number and citation.
