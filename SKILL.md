---
name: veriscribe
description: >
  Make AI-assisted academic and research writing read as human-authored while staying
  evidence-true, in English and 中文. Use for papers, theses, abstracts, related work,
  rebuttals/responses to reviewers, grant proposals (NSF/NIH/NSFC/面上/青年), cover letters,
  and any scholarly prose. Removes AI tells (em-dashes, "delve/underscore/tapestry",
  significance hype, rule-of-three, 综述腔/翻译腔/工程师腔), enforces claim↔evidence
  discipline (no verb stronger than its data), raises burstiness/perplexity so drafts stop
  tripping GPTZero/Turnitin/Originality.ai/CrossCheck, and matches the author's voice and
  the venue's register. Triggers: "去AI味", "说人话", "润色论文", "降AIGC率", "humanize",
  "lower the AI score", "make this less AI", "polish my paper", "reviewer response",
  "润色/改写/审稿 学术文本". NEVER alters a number, result, or citation, and NEVER fabricates
  sources; it is not a tool for evading AI-use disclosure.
license: MIT
compatibility: any-agent (claude-code, codex, cursor, opencode, openclaw, gemini-cli)
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
---

# VeriScribe · 真章

Turn AI-assisted scholarly writing back into *a specific researcher making a precise,
evidence-anchored argument* — not *a model performing "good academic writing."*

VeriScribe unifies five things a single humanizer usually misses: (1) the **claim↔evidence
discipline** scholarship requires, (2) the **detector science** (perplexity / burstiness /
stylometry) that decides whether clean prose gets falsely flagged, (3) a **bilingual EN + 中文**
AI-tell catalog, (4) **voice and venue** matching, and (5) an **integrity firewall** so nothing
becomes less true in the name of sounding human.

> 真章 = "the genuine article / the real substance," a pun on 章 (a piece of writing).
> The name is the whole thesis: writing that is *human in voice* and *true in substance*.

---

## IRON RULES (read first, never break)

These override every stylistic instruction below. If a "humanizing" edit would violate one, don't make it.

1. **Never alter a number, statistic, result, equation, unit, or citation key.** Not to round,
   not to "clean up," not to strengthen. Numbers and cites are load-bearing evidence, copy them verbatim.
2. **Never invent a source, dataset, quotation, institution, date, or preliminary result.** If a
   claim lacks support, you *flag the gap* or *soften the claim*, you do not manufacture a citation
   to cover it.
3. **No verb may be stronger than its evidence.** Empirical work *shows / provides evidence / is
   consistent with*; it does not *prove / demonstrate / guarantee* universal truths (Layer: [academic-discipline](references/academic-discipline.md)).
4. **Preserve every information point.** If the original has five paragraphs, so does the rewrite.
   Nothing that carries a fact, number, judgment, action, or instruction is deleted without a flag.
5. **This is not a disclosure-evasion tool.** VeriScribe helps a *human writer* whose own argument
   and data trip a flawed filter, or whose AI-assisted draft reads mechanically. If a user wants to
   pass off unresearched machine output as their own scholarship, that is out of scope, say so plainly.
   Surface watermark/provenance limits when relevant ([detector-science](references/detector-science.md) §Watermarks).

If the input is not writing to improve (it's code, logs, config, error messages, or a request for
*fact-checking* rather than *style*) — stop and say so. VeriScribe is a prose skill.

---

## Step 0 — Route (30 seconds, before any edit)

Detect three axes; they select which reference lanes you load.

| Axis | Options | How it changes the work |
|------|---------|-------------------------|
| **Language** | English · 中文 · mixed | Load [ai-tells-english](references/ai-tells-english.md) and/or [ai-tells-chinese](references/ai-tells-chinese.md). In mixed text, keep ONE dominant register; English tokens inside a Chinese sentence are judged by that sentence's meaning, not a word list. |
| **Doc type** | paper section · abstract · thesis · **reviewer response/rebuttal** · **grant proposal** · cover letter · general prose | Papers get the strict trim; proposals get *vision + feasibility* register (do NOT flatten ambition) — [academic-discipline](references/academic-discipline.md) §Grant mode. |
| **Goal** | de-slop / humanize · lower a detector score · evidence-audit only · voice-match · diagnose (don't rewrite) | "Diagnose only" ⇒ annotation output, no rewrite. "Detector score" ⇒ prioritize cut + burstiness + evidence density. |

**Ask (one question, only if genuinely ambiguous and it changes the output):** target venue/agency, and
whether the author has a writing sample to match. Otherwise assume clean, venue-neutral scholarly prose
and proceed — don't block on questions.

---

## The workflow (do the steps in order; do not skip Diagnose or Protect)

### 1. Diagnose — mark, don't edit yet
Read the whole draft. Tag each paragraph:
- **Evidence-dense** (proper nouns, dates, quotes with page/figure/table refs, named methods, numbers throughout) → usually already reads human. **Leave it alone.** Editing it *raises* AI score.
- **Analytical** (thesis, framing, transitions, motivation, discussion) → the AI-prone zone. Concentrate here.
- **Mixed** → targeted cuts, not rewrites.

Also note structural balance: if one paragraph is >2× the shortest, flag it — uniform paragraph length is a detector signal.

### 2. Protect — lock the untouchables
Mark **protected spans** that must survive verbatim: numbers, stats, p-values, equations, units, citation
keys, dataset/method/metric names, quoted text, code/CLI/API/field names, error strings, defined terms,
and the *system/actor subject* in technical sentences. In 中文: 术语、系统主语、事故复盘用语、命令、报错 默认保留
(see [ai-tells-chinese](references/ai-tells-chinese.md) §protected-spans). Everything else is editable; these are not.

### 3. Cut — the single strongest move
**Cutting beats rewriting.** Rewriting the same content in "tighter" phrasing *smooths* prose toward AI
register; removing words shrinks the surface where AI-register shows. Delete on sight:
- Throat-clearing openers and meta-commentary: "In recent years, X has attracted increasing attention",
  "It is worth noting that", "In this paper we will argue", "值得注意的是", "众所周知", "随着……的快速发展".
- Transitional sentences that restate the previous paragraph before moving on.
- Sentences that restate the thesis/abstract without adding evidence.
- Any sentence that could open with *Furthermore / Moreover / Additionally / Thus / Indeed*.
- Significance hype: "paves the way for", "sheds light on", "of paramount importance", "开创性地", "具有重要意义".
- Two-adjective pairs meaning the same thing ("careful and thoughtful"); clauses that exist only to keep parallel structure.

If cutting leaves a paragraph stubby, **that's fine** — short paragraphs add the burstiness detectors read as human.

### 4. Anchor — claim ↔ evidence (the scholarship layer)
For every empirical claim, check: (a) is it backed by a number/figure/table/citation present in the text,
and (b) does the verb match that evidence's strength? Then:
- **Unbacked claim** → add the evidence pointer that exists, or soften the claim. *Never* invent one.
- **Verb > evidence** → downgrade ("demonstrates universal superiority" → "matches or exceeds the strongest
  baseline on these three datasets (Table 2)").
- **Vague magnitude** → a number or attributed range ("a large improvement" → "a 2–6% gain in balanced
  accuracy over the strongest baseline"). Lead comparisons with the *strongest* competitor, not the trivial one.
- **Grant mode:** replace claim↔evidence with **claim↔feasibility** — every ambitious aim needs a footing
  (preliminary data, a prior result, a classical theorem, a collaborator). Keep the ambition; attach the footing.

### 5. De-tell — purge the AI fingerprints (subject to §Preserve)
Run the catalog for the detected language ([EN](references/ai-tells-english.md) / [中文](references/ai-tells-chinese.md)).
The universal hard constraints:
- **Zero em-dashes / en-dashes (— –).** The most reliable single tell. Recast with a period, comma, colon,
  or parentheses. Scan the final draft for `—` and `–`; any hit means it isn't done. (中文 破折号 same rule.)
- **No copula avoidance** ("serves as / stands as" → "is"). **No rule-of-three padding.** **No negative
  parallelism** ("not just X, but Y"). **No -ing tails that fake depth** ("..., underscoring its importance").
- **Vocabulary clusters** — the tell is *co-occurrence density*, not any single word. Where 2–3 of
  {delve, leverage, underscore, streamline, foster, harness, seamless, robust, pivotal, tapestry, landscape,
  realm, intricate, showcase} cluster in one paragraph, substitute downward to plain diction. 中文对应：
  {赋能、抓手、闭环、深度、维度、生态、范式、显著、鲁棒、纵观、值得关注} 同段扎堆才处理。
- **Formal connectors → plain ones or none.** "Furthermore/Moreover" signal metronomic restatement; "but/so/and"
  force a pivot that creates variation for free.
- No emoji, no title-case headings, no boldface-per-bullet, no curly-quote-only artifacts, no sycophantic
  chatbot residue ("Great question!", "I hope this helps", "希望这对你有帮助").

### 6. Burstiness — make the rhythm uneven (the detector layer)
Human prose is *unevenly distributed*; AI prose is smooth and mid-length. Introduce contrast:
- After a long sentence, a six-word one. Let a one-idea sentence stand alone.
- Vary **paragraph** length too — drop a one-sentence paragraph between two long analytical ones.
- One well-placed rhetorical question in the whole piece (not a tour) reads as a human thinking in real time.
- Split "A, because B" into "A. B." when both stand. Short-next-to-short is human.
- Keep evidence-tied hedges next to flat assertions ("appears to", "is consistent with", "suggests") — in
  scholarship these are *correct*, not weakness (see §Preserve).

### 7. Voice & venue — match a person and a target
If the author supplies a writing sample, read it first: sentence rhythm, connective habits, where they hedge,
how they open sections, notation, recurring phrasings — then match those, don't impose a generic voice. Match
venue register too: ICLR/NeurIPS/ACL terse and results-forward; Nature/PNAS/Cell more expository; NSFC/中文期刊
按学科规范. No sample ⇒ default to clean, precise, venue-appropriate prose. **Never inject opinion, humor, or
first-person "personality" into a manuscript** — for scholarship, neutral-and-precise *is* the human voice.
(For channeling a specific great science communicator's explanatory style, the adjacent `nuwa-skill`/`huashu-nuwa`
can distill a voice; VeriScribe consumes such a voice sample, it doesn't manufacture personas itself.)

### 8. Score & verify — two passes, then stop
Score the rewrite on the rubric ([scoring-rubric](references/scoring-rubric.md)); anything below the gate goes back to step 3.

**Pass 1 — Fidelity (mandatory):** protected spans intact? every information point traceable? register uniform?
terminology exact? no broken seams from a cut? Bibliography ↔ in-text cites still match?

**Pass 2 — Residual audit (only if fidelity holds):** any opener/summary residue, narrator "this shows that…",
empty value-judgments, or over-uniform sentence length left? Fix lightly — do **not** rewrite what already works.

**Then stop.** Detector scores swing ±10–20 points per run; three rewrites within ~15 points of each other = noise.
"Surgical polish" past this point regresses toward AI register (the **refinement trap**). Ship the best version.

---

## Preserve — do NOT over-correct (scholarship is not slop)
A general humanizer flattens legitimate academic constructs. Keep them:
- **Evidence-tied hedging** ("suggests", "we hypothesize that", "may indicate", "appears to") — required, not a tell.
- **Passive voice when the actor is irrelevant** ("Samples were normalized to total protein").
- **First-person plural "we"**, formal definitions, named methods/metrics/terms, equations, symbols — verbatim.
- **An occasional semicolon or triple** in moderation (em-dashes are the exception — remove those).
- **Domain terminology and the system subject** in technical sentences.
- **Specific, hard-to-fabricate detail** — a real date, a weird quote, an exact address. LLMs round specifics off;
  humans hoard them. This is the strongest human signal there is; protect it.

Judge by **clusters, not isolated hits.** One "however", one curly quote, one semicolon proves nothing. A "vibrant
tapestry" + rule-of-three + a "Challenges and Future Prospects" section + em-dashes is a confession. When in doubt,
leave clean prose alone.

---

## Output contract
Default = deliver the improved draft **plus a short change report**: patterns removed (by type), claims softened
or given evidence pointers, voice/venue notes, and an explicit line confirming *no number, equation, or citation
was altered*. For a "detector score" goal, add which paragraphs were cut vs. left untouched and why.

**Diagnose-only mode** (user says "先别改 / 只标问题 / where does this read AI / just audit"): output the top 1–5
issues, each as {pattern family · trigger location · suggested action · rewrite? yes/no}. No full rewrite.

**中文长文 (≈1000字+):** default to `bounded` scope — clean sentence-internal AI 味 in place, but put whole-sentence
deletions on a "建议删除（待确认）" list with *why removing loses no information*, and let the author decide length.
Use `in-place` (delete nothing, only soften) when the user demands the sentence count be preserved.

---

## Reference navigation
- English AI-tell catalog (33 patterns + 2026 vocab clusters + false-positive guards): [references/ai-tells-english.md](references/ai-tells-english.md)
- 中文 AI 腔 catalog (场景/档位/scope、protected spans、无源引用三模式): [references/ai-tells-chinese.md](references/ai-tells-chinese.md)
- Academic discipline (over-claim verbs, significance hype, contribution/citation cliches, venue, **grant mode**): [references/academic-discipline.md](references/academic-discipline.md)
- Detector science (perplexity/burstiness/stylometry, cut>rewrite, the traps, ESL bias, watermarks): [references/detector-science.md](references/detector-science.md)
- Scoring rubric + ship gate: [references/scoring-rubric.md](references/scoring-rubric.md)
- Before/after examples (EN paper · 中文 摘要 · rebuttal · grant): [references/examples.md](references/examples.md)
- Smoke-test cases: [evals/benchmark.md](evals/benchmark.md)

VeriScribe can run from `SKILL.md` alone as a fallback; full power is `SKILL.md` + `references/` together.
Load a reference lane only when the routed language/doc-type/goal calls for it.

---

*VeriScribe synthesizes and credits five MIT-licensed skills — humanizer, academic-humanizer, humanize-prose,
stop-slop, shuorenhua — plus the adjacent nuwa-skill. See [CREDITS](README.md#credits--attribution). It does not
replace them; it routes between their strengths and adds the bilingual + integrity spine.*
