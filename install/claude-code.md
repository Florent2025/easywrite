# Install in Claude Code

## As a user-global skill (recommended)
```bash
git clone https://github.com/YOUR_GH_USERNAME/veriscribe.git ~/.claude/skills/veriscribe
```
Restart Claude Code (or start a new session). The skill auto-registers under the name `veriscribe` and triggers on
research-writing / de-AI / "lower the AI score" requests in English or 中文. Verify with `/help` → skills, or just ask
*"humanize my paper intro, keep every number."*

## As a project skill
```bash
git clone https://github.com/YOUR_GH_USERNAME/veriscribe.git .claude/skills/veriscribe
```

## As a plugin (marketplace)
```bash
/plugin marketplace add YOUR_GH_USERNAME/veriscribe
/plugin install veriscribe
```

## Manual / single-file
Copy `SKILL.md` into `~/.claude/skills/veriscribe/SKILL.md`. It runs standalone; add `references/` for full power.

## Invoke explicitly
Ask naturally (auto-trigger), or force it: `/veriscribe` if exposed as a slash command, or "use the veriscribe skill to …".
