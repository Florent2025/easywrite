# Install in Claude Code

## As a user-global skill (recommended)
```bash
git clone https://github.com/Florent2025/easywrite.git ~/.claude/skills/easywrite
```
Restart Claude Code (or start a new session). The skill auto-registers under the name `easywrite` and triggers on
research-writing / de-AI / "lower the AI score" requests in English or 中文. Verify with `/help` → skills, or just ask
*"humanize my paper intro, keep every number."*

## As a project skill
```bash
git clone https://github.com/Florent2025/easywrite.git .claude/skills/easywrite
```

## As a plugin (marketplace)
```bash
/plugin marketplace add Florent2025/easywrite
/plugin install easywrite
```

## Manual / single-file
Copy `SKILL.md` into `~/.claude/skills/easywrite/SKILL.md`. It runs standalone; add `references/` for full power.

## Invoke explicitly
Ask naturally (auto-trigger), or force it: `/easywrite` if exposed as a slash command, or "use the easywrite skill to …".
