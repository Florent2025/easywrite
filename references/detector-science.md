# Detector Science

Why clean prose gets flagged, and what actually moves the score. Distilled from `humanize-prose`, whose rules
come from an 8-draft essay graded repeatedly against GPTZero (v1→v8) plus the 2026 detection literature.

## What detectors measure (2026)

GPTZero, Originality.ai, Copyleaks, Winston AI, Turnitin, CrossCheck score three stacked signals:
- **Perplexity** — how predictable each next word is. Low = machine-like.
- **Burstiness** — sentence-to-sentence *variation*. Low (even, mid-length) = machine-like.
- **Stylometry** — the "shape": how ideas flow, how punctuation is deployed, how transitions are managed.

**The enemy is lexical-syntactic smoothness, not length or topic.** The same 1,500-word essay can score 21% AI
and, after "tightening," 66% AI — the content unchanged, only the register smoothed. Three corollaries:

1. **Evidence density is human.** Proper nouns, dated events, quotations with page cites, named scholars,
   verifiable facts — the strongest human-register signals a detector reads. Abstract analytical prose without
   them reads AI even when the argument is original.
2. **Cutting beats rewriting.** Removing words shrinks the surface where AI register shows. Rewriting the same
   content "more tightly" smooths the prose further and *raises* the score.
3. **Asymmetry beats polish.** Long next to short; a hedge next to a flat assertion; uneven paragraph lengths —
   this is the burstiness detectors read as human.

## Who is actually being flagged (say this to the user)

Two populations misfire systematically; a user with a high score is often one of them. **Name it — don't let them
internalize the detector as a verdict on their writing.**
- **Non-native English / ESL / TOEFL writers.** A 2023 Stanford HAI study found ~61% of legitimate TOEFL essays
  flagged as AI; the bias persists through 2026. Cause: simpler, grammatically rigid, more predictable structures —
  the same low-perplexity features the detector reads as machine output.
- **Technical / scientific / medical / legal writers.** Genres that prize clarity, standardized terminology, and
  uniform structure read AI for the same reason: low surface entropy.

Two implications: (1) **the reassurance is real** — a high score means the detector is measuring a proxy that fails
on their population, not that their writing is bad; (2) **ask whether detection is even the right bar** — many 2026
institutions accept *process verification* (draft trails, version history, oral defense) which is more robust than
chasing a number that swings ±10–20 points per run. Suggest it when relevant.

## The moves that work (apply in order — see SKILL.md workflow)

- **Diagnose:** leave evidence-dense paragraphs alone; concentrate on analytical ones.
- **Cut** transitional/restating sentences, metacommentary, "Furthermore/Moreover"-able lines, redundant adjective pairs.
- **Add evidence, not refinement:** to a still-AI paragraph add *one* concrete specific (a dated fact, a named
  source with page, a place/artifact). Caution: adding a specific to an *already dense* paragraph can raise the
  score — evidence works best in abstract paragraphs.
- **Remove AI-tell patterns** (em-dashes, semicolons, cleft "It is X that Y", neat tricolons, causal
  sentence-fusion, crisp metaphor verbs, exhaustive adjective stacks, "illustrates/underscores/demonstrates").
- **Introduce burstiness:** a six-word sentence after a long one; a lone one-idea sentence; a hedge next to a flat
  assertion; one rhetorical question in the whole piece; vary *paragraph* length; permit controlled inconsistency
  (a paragraph ending mid-thought reads less machine-finished than one that closes itself cleanly).

## What NOT to do (the traps)

- **The refinement trap.** "Surgical improvements" — tightening phrasing, sharpening word choice, combining short
  sentences for smoothness, cleaning up parallel structure — are the *exact* operations that push prose toward AI
  register. Copy-editor intuition is often anti-human-register here.
- **The more-effort trap.** Scores don't move monotonically with effort. A reference trajectory ran
  75% → 68% → **21%** → 56% → 66% across successive careful rewrites; the last two thoughtful rounds made it worse.
- **The rewrite-what's-working trap.** Once a paragraph reads human, don't edit it, not even to tighten. In the
  trajectory, the two untouched paragraphs stayed "green"; all four rewritten ones regressed. **Preserve what works.**
- **The chase-the-noise trap.** A single 10-point movement across one run is noise. Act only on consistent
  differences across two+ runs, or deltas > 20 points. If three rewrites land within 15 points of each other, **stop.**

## Ship-readiness scan (before submitting to a detector)

- [ ] Zero em-dashes; zero (or minimal) semicolons.
- [ ] Zero "furthermore / moreover / additionally / thus / indeed / notably / it is important to note".
- [ ] ≤ 1 paragraph with 2+ abstract verbs (delve, leverage, underscore, streamline, foster, harness, facilitate).
- [ ] ≤ 1 paragraph with 2+ inflated adjectives (pivotal, robust, seamless, innovative, cutting-edge, comprehensive, holistic).
- [ ] No tricolons with identical grammatical endings.
- [ ] No two consecutive sentences joined by "because" where "A. B." reads naturally.
- [ ] Paragraph word counts within a factor of 2–3; not one paragraph > 2× the smallest.
- [ ] Each paragraph has ≥ 1 proper noun, date, or direct quote.
- [ ] No two adjacent sentences the same length (±3 words).
- [ ] Body-paragraph openers are not topic-summary restatements.
- [ ] Bibliography ↔ in-text citations match exactly.

(The installed `humanize-prose` skill ships `scripts/ai_tell_scan.py`, which automates most of these counts.)

## Limits & ethics (Watermarks)

- Humanization addresses **stylometric** detection (perplexity/burstiness/stylometry) — **not cryptographic
  provenance.** If a draft was produced by a watermarked model, Google **SynthID** embeds token-level signals that
  survive paraphrasing, and **C2PA** attaches signed creation-history metadata. Surface edits will not change a
  SynthID/C2PA verdict; only replacing machine content with human-written content will. If the target pipeline uses
  those, say so — don't promise a score change it can't deliver.
- These techniques **work only when the content and argument are the user's own.** Evidence density requires the
  writer to actually know the sources; asymmetric prose requires genuine thinking. An AI draft of an unresearched
  topic will still read AI because it lacks retrievable specifics. Easywrite helps a human clear a flawed filter —
  it does not launder machine output, and it is not for evading required AI-use disclosure.
- Detectors are unreliable under ~300 words and on fiction (already human-register). Don't over-fit short text.
