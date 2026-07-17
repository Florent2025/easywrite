# AGENTS.md

This repository is an **agent skill**. The operative instructions live in [`SKILL.md`](SKILL.md); the detailed
knowledge lives in [`references/`](references/). Any coding agent (Claude Code, Codex, Cursor, OpenCode, OpenClaw,
Gemini CLI, …) should treat `SKILL.md` as the entry point.

## For an agent loading this skill

1. Read [`SKILL.md`](SKILL.md) fully. The **IRON RULES** override every stylistic instruction — never alter a
   number, result, or citation; never fabricate a source; this is not a disclosure-evasion tool.
2. Route on three axes (language · doc-type · goal), then load only the reference lane(s) that apply:
   - English text → [`references/ai-tells-english.md`](references/ai-tells-english.md)
   - 中文 text → [`references/ai-tells-chinese.md`](references/ai-tells-chinese.md)
   - Any scholarly doc → [`references/academic-discipline.md`](references/academic-discipline.md)
   - "Lower the AI score" goal → [`references/detector-science.md`](references/detector-science.md)
   - Before shipping → [`references/scoring-rubric.md`](references/scoring-rubric.md)
3. Follow the 8-step workflow in order. Do not skip Diagnose or Protect. Deliver the improved draft **plus** a
   short change report confirming no number/equation/citation was altered.

## For a human editing this skill

- Every new rule needs a before/after example (add to `references/examples.md` or the relevant lane).
- No rule may weaken an IRON RULE.
- Keep the bilingual coverage balanced: an English pattern should have a 中文 counterpart where one exists.
- Add regression cases to `evals/benchmark.md`.
