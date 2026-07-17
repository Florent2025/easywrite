# Changelog

All notable changes to VeriScribe are documented here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/); versions use [SemVer](https://semver.org/).

## [0.1.0] — 2026-07-17

Initial release. First public version of the integrated skill.

### Added
- **Core skill** (`SKILL.md`): IRON RULES (integrity firewall), a 3-axis router
  (language · doc-type · goal), and the 8-step workflow (Diagnose → Protect → Cut →
  Anchor → De-tell → Burstiness → Voice/venue → Score & verify).
- **Reference lanes** (`references/`):
  - `ai-tells-english.md` — 33-pattern English catalog + 2026 vocabulary clusters + false-positive guards.
  - `ai-tells-chinese.md` — 中文 去 AI 味 engine: scene/tier/scope, protected spans, 无源引用三模式.
  - `academic-discipline.md` — over-claim verbs, contribution/citation cliches, venue matching, NSF/NIH/NSFC grant mode, rebuttal mode.
  - `detector-science.md` — perplexity/burstiness/stylometry, cut>rewrite, the four traps, ESL/technical-writer bias, SynthID/C2PA watermark limits.
  - `scoring-rubric.md` — two hard gates (Fidelity, Evidence) + five-dimension rubric + ship gate.
  - `examples.md` — before/after for EN paper, 中文摘要, reviewer response, and grant.
- **Evals** (`evals/benchmark.md`): should-fix and fidelity-guard smoke tests.
- **Packaging**: MIT `LICENSE`, `NOTICE`, `AGENTS.md`, plugin + marketplace manifests, per-tool `install/` notes.
- **Attribution**: full credit to the five source skills (humanizer, academic-humanizer, humanize-prose, stop-slop, shuorenhua).

### Notes
- Synthesized from five MIT-licensed skills; routes between their strengths rather than replacing them.
- Bilingual EN + 中文 is native, not bolted on.
