<div align="center">

# VeriScribe · 真章

**The academic-writing skill that makes AI-assisted papers read *human* while staying *evidence-true* — in English and 中文.**

*让 AI 辅助的论文既有人味、又守得住真章：去 AI 味 + 守证据 + 降 AIGC 检出率，中英双语。*

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/type-agent%20skill-6e56cf.svg)](SKILL.md)
[![EN + 中文](https://img.shields.io/badge/lang-EN%20%2B%20%E4%B8%AD%E6%96%87-c0392b.svg)](#)
[![Works with](https://img.shields.io/badge/works%20with-Claude%20Code%20·%20Codex%20·%20Cursor%20·%20OpenCode-333.svg)](#install)

</div>

---

## Why this exists

A general "humanizer" strips AI tells but has no idea that *your p-value is load-bearing*. An academic polisher
fixes structure but doesn't know why clean prose still trips GPTZero. And neither one handles 中文 AI 腔. Research
writing needs all three at once, plus a hard rule that **nothing gets less true in the name of sounding human**.

VeriScribe is that skill. It routes between five strengths and adds a bilingual + integrity spine:

- 🧬 **Claim ↔ evidence discipline** — no verb stronger than its data; every claim earns its number, figure, or citation. Papers, rebuttals, and grants each get the right register (grants keep their vision; papers get the strict trim).
- 🔬 **Detector science, done right** — perplexity / burstiness / stylometry. It *cuts* instead of "polishing" (polishing raises the AI score), and it tells ESL and technical writers the truth: a high score is often the detector's bias, not their writing.
- 🈶 **Bilingual** — a full English AI-tell catalog *and* a 中文 去 AI 味 engine (场景 / 档位 / scope、protected spans、无源引用三模式).
- 🎯 **Voice & venue matching** — matches your own writing sample and the target venue (NeurIPS terse vs. Nature expository vs. NSFC 规范).
- 🔒 **Integrity firewall** — never alters a number, result, or citation; never fabricates a source; not a tool for evading AI-use disclosure.

> **真章** means "the genuine article / the real substance," punning on 章 (a piece of writing). That's the whole thesis: *human in voice, true in substance.*

## What it does (at a glance)

```
Route (language · doc-type · goal)
  └─ Diagnose  → tag paragraphs (evidence-dense = leave alone; analytical = fix here)
  └─ Protect   → lock numbers, results, cite keys, terms, system subjects
  └─ Cut       → the strongest move; remove filler, restatement, hype
  └─ Anchor    → claim ↔ evidence (papers) / claim ↔ feasibility (grants)
  └─ De-tell   → em-dashes, vocab clusters, rule-of-three, 综述腔/翻译腔
  └─ Burstiness→ uneven sentence & paragraph rhythm
  └─ Voice     → match author sample + venue register
  └─ Score     → 2 hard gates (Fidelity, Evidence) + 5-dim rubric, then STOP
```

## Use it

Once installed, just ask in natural language — the skill auto-triggers:

- *"Humanize the introduction of my paper, keep every number."*
- *"降一下这段摘要的 AIGC 检出率，别动数据和引用。"*
- *"My rebuttal reads too AI and too grovelly — tighten it and tie each reply to a change."*
- *"Polish Aim 1 of my NSF proposal but keep the vision."*
- *"这段哪里像 AI？先别改，先标问题。"* (diagnose-only mode)

## Install

<a id="install"></a>

**Option A — Skills CLI (any agent):**
```bash
npx skills add <your-github-username>/veriscribe
```

**Option B — Claude Code plugin marketplace:**
```bash
/plugin marketplace add <your-github-username>/veriscribe
/plugin install veriscribe
```

**Option C — Manual (Claude Code / Codex / Cursor / OpenCode):**
```bash
# Claude Code (user-global):
git clone https://github.com/<your-github-username>/veriscribe.git ~/.claude/skills/veriscribe
# Codex:  ~/.codex/skills/veriscribe    Cursor: .cursor/skills/veriscribe    OpenCode: ~/.config/opencode/skills/veriscribe
```

**Option D — No automation:** paste [`SKILL.md`](SKILL.md) into the conversation. It runs standalone; full power is `SKILL.md` + `references/`.

See [`install/`](install/) for per-tool notes.

## Repository layout

```
veriscribe/
├── SKILL.md                        # core router + 8-step workflow + IRON RULES
├── references/
│   ├── ai-tells-english.md         # 33 patterns + 2026 vocab clusters + false-positive guards
│   ├── ai-tells-chinese.md         # 场景/档位/scope · protected spans · 无源引用三模式
│   ├── academic-discipline.md      # over-claim verbs · venue · grant (NSF/NIH/NSFC) mode
│   ├── detector-science.md         # perplexity/burstiness/stylometry · the traps · ESL bias · watermarks
│   ├── scoring-rubric.md           # 2 hard gates + 5-dim rubric + ship gate
│   └── examples.md                 # before/after: EN paper · 中文摘要 · rebuttal · grant
├── evals/benchmark.md              # should-fix + fidelity-guard smoke tests
├── install/                        # per-tool install notes
└── .claude-plugin/                 # plugin + marketplace manifests
```

## Design principles

1. **Fidelity is a gate, not a dimension.** A stylistically perfect draft that altered a number is a failure.
2. **Cutting beats rewriting.** "Polishing" smooths prose toward AI register. Remove, don't re-smooth.
3. **Preserve what works.** Evidence-dense paragraphs and evidence-tied hedges are *human* — leave them.
4. **Clusters, not isolated hits.** One em-dash proves nothing; four tells together is a confession.
5. **Honesty about limits.** It clears a flawed *stylometric* filter for a real author; it does not beat SynthID/C2PA watermarks and is not for disclosure evasion.

## Credits & attribution

VeriScribe stands on the shoulders of five excellent MIT-licensed skills. It does not replace them — it routes
between their strengths and adds the bilingual + integrity spine. Please star the originals:

| Source | Author | What VeriScribe took |
|--------|--------|----------------------|
| [humanizer](https://github.com/blader/humanizer) | [@blader](https://github.com/blader) | The 33-pattern English AI-tell catalog, voice calibration, false-positive guards |
| [academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) | AIScientists-Dev | Claim↔evidence discipline, over-claim verbs, venue & NSF/NIH grant modes |
| [humanize-prose](https://github.com/celestialdust/humanize-prose) | [@celestialdust](https://github.com/celestialdust) | Detector science (perplexity/burstiness/stylometry), cut>rewrite, the traps, ESL bias, watermark limits |
| [stop-slop](https://github.com/hardikpandya/stop-slop) | [Hardik Pandya](https://hvpandya.com) | Tight core rules + the multi-dimension scoring rubric |
| [shuorenhua 说人话](https://github.com/MrGeDiao/shuorenhua) | [@MrGeDiao](https://github.com/MrGeDiao) | The entire 中文 去 AI 味 engine: scene/tier/scope, protected spans, 无源引用三模式 |

Adjacent and complementary: [nuwa-skill 女娲](https://github.com/alchaincyf/nuwa-skill) (distills a thinker's voice
you can then feed to VeriScribe's voice-match step) and [taste-skill](https://github.com/leonxlnx/taste-skill)
(frontend/UI, not prose).

## License

[MIT](LICENSE). If you build on VeriScribe, keep the attribution chain intact — credit the five sources above, as this repo does.

## Contributing

Issues and PRs welcome: new AI-tell patterns (with a before/after), venue register notes, additional languages,
and benchmark cases. Every rule should come with an example, and no rule may weaken an IRON RULE in `SKILL.md`.
