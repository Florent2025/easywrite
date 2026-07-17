# Academic Discipline

The layer a general humanizer misses. Scholarship already has a correct human voice — neutral, precise,
third-person plural, every claim tied to its evidence. The job is to strip AI *tells* **without casualizing**,
and to enforce the discipline: *every claim earns its number, figure, or citation, and no verb is stronger
than its evidence.* Distilled from `academic-humanizer`.

> **Never inject opinion, humor, or first-person "personality" into a manuscript.** For technical writing,
> neutral-and-precise *is* the human voice. The `humanizer` "personality/soul" section does **not** apply here.

## Academic AI tells (remove / fix)

1. **Over-claiming verbs.** Empirical work *shows / provides evidence / is consistent with*; it does not
   *prove / demonstrate / establish / confirm / guarantee* universal truths. "significantly" needs a test or number.
   - ✗ *We prove that our method significantly outperforms all prior approaches.*
   - ✓ *Our method improves held-out accuracy by 4–7 points over the strongest prior approach (Table 3); the gain is significant at p < 0.01 (paired test).*
2. **Significance hype.** paves the way for · a crucial/pivotal step toward · has the potential to revolutionize ·
   opens new avenues · sheds light on · of paramount importance · bridges the gap. → Name the specific failure mode you address.
3. **Empty intensifiers.** extensive/comprehensive/thorough experiments · a wide range of · numerous · various.
   → *We evaluate on three datasets (ImageNet, CIFAR-100, iNaturalist).*
4. **Novelty padding.** "novel" more than once per section · "to the best of our knowledge" · "for the first time".
   → State precisely what prior work does not address.
5. **Formulaic openers.** "In recent years, X has attracted increasing attention" · "With the rapid development
   of…" · "Despite recent advances,…". → Open with the specific limitation or fact.
6. **Connective overuse.** Don't start consecutive sentences with Moreover/Furthermore/Additionally/In particular.
   Let logic carry the order.
7. **Contribution-list clichés.** Each contribution names a *specific result*, not a restatement of the abstract.
   - ✗ *(1) a novel method; (2) extensive experiments; (3) strong results.*
   - ✓ *(1) a metadata-aware encoder reaching 0.91 AUROC vs 0.86 for the strongest baseline; (2) staying within 2 points under 20% label noise where the baseline drops 9; (3) a released benchmark.*
8. **Citation dumping.** Cite the one or two works that matter and say *why*, not "Many methods exist [3,7,9,12,15]."
9. **Hedging-by-vagueness.** somewhat · relatively · fairly · to some extent · quite → quantify or cut.
10. **Boilerplate emphasis.** "It is worth noting that" · "It should be emphasized that" · "Notably," ·
    "Importantly," → if it matters, the sentence shows it.
11. **Overlong clause-stacked sentences** (past ~30 words or 3+ subordinate clauses chained with which/that/while/with)
    → split; one idea per sentence; cut weightless subordinate clauses.

## Claim ↔ evidence discipline (papers)

For every empirical claim: (a) is it backed by a number/figure/table/citation *present in the text*, and
(b) does the verb match that evidence's strength?
- **Unbacked → add the pointer that exists, or soften.** *"Our method is more robust"* → *"Our method's accuracy
  drops 2 points under distribution shift, versus 11 for the baseline (Figure 3)."*
- **Verb > evidence → downgrade.** *"demonstrates universal superiority"* → *"matches or exceeds the strongest
  baseline on these three datasets (Table 2)."*
- **Vague magnitude → number or attributed range.** *"a large improvement"* → *"a 2–6% gain in balanced accuracy
  over the strongest baseline."* Prefer ranges to averaged single values unless the averaging is stated. Lead the
  comparison with the *strongest* competitor, not the trivial baseline.

## Preserve (do NOT over-correct)
- **Evidence-tied hedging is correct and required** — keep "suggests", "is consistent with", "we hypothesize
  that", "may indicate", "appears to" when the claim is genuinely uncertain. Turning "suggests" into "proves" is
  *manufacturing over-claim* — the opposite failure.
- **Passive voice when the actor is irrelevant** ("Samples were normalized to total protein").
- **First-person plural "we"**, formal definitions, named methods/metrics/terms, equations, symbols — verbatim.
- Occasional semicolon or triple in moderation; em-dashes are the exception (remove).
- **Never invent, drop, or alter a number, equation, or citation. Preserve every cite key.**

## Voice & venue
Read the author's sample first (rhythm, connective habits, where they hedge, section openings, notation,
recurring phrasings) and match it. Match the venue register too:
- **ICLR / NeurIPS / ICML / ACL / EMNLP / AAAI / COLM:** terse, direct, results-forward.
- **Nature / Science / PNAS / Cell:** more expository, motivation- and impact-forward, still precise.
- **Systems (OSDI/NSDI/SOSP/ASPLOS):** concrete, mechanism-forward.
- **NSFC / 中文核心期刊:** 按学科规范，摘要-引言-方法-结果-讨论 结构收敛，术语稳定。
Absent a sample → clean, precise, venue-appropriate prose (not a casual/opinionated general-humanizer voice).

## Grant / proposal mode (NSF, NIH, NSFC, foundations)

**A proposal is not a paper.** It is sold on **vision + feasibility**, not finished results, and reviewers score
it. The register shifts: ambition language a paper would trim ("long-term goal", "transformative", "establish a
foundation") is *appropriate here* — **do not flatten the vision.** Enforce a different discipline: **claim ↔ feasibility.**

- **The score lives in the first pages.** NSF: a self-contained one-page Project Summary (**Overview · Intellectual
  Merit · Broader Impacts**), then Description opening *long-term vision → this proposal's goal → the gap → the
  thrusts/aims → the payoff* within pages 1–2. NIH R01: the **Specific Aims page is the whole proposal** — problem +
  gap/critical need → long-term goal + central hypothesis → "The objective of this application is…" → 2–3 Aims
  (goal + approach phrase + expected outcome) → payoff paragraph. Edit these hardest; a reviewer unconvinced by
  page 3 does not recover on page 10.
- **Fix these proposal-specific weak moves:** vague importance ("this is an important problem") → the concrete cost
  of the gap; **method-as-aim** ("Aim 2: apply transfer learning") → a question/outcome aim; **dominoed aims**
  (Aim 2/3 collapse if Aim 1 fails) → parallel, independently valuable aims with stated fallbacks; **ambition
  without feasibility** → attach preliminary data / a prior result / a classical theorem / a collaborator beside
  each bold claim; **boilerplate Broader Impacts** → concrete, enumerated, tied to the research; **hedged central
  hypothesis** → a falsifiable commitment (calibrated hedging belongs in Approach, not the central claim).
- **Preserve & deploy (funded-proposal craft):** a bold long-term goal up front; run-in lead-ins for scannability
  (**Goal:**, **Innovation:**, *Aim N:*); a concrete running example across aims; sharp aim-as-question statements;
  anchoring novel work in named classical results; foregrounding the team's real track record *early* as feasibility
  evidence. **Use only the PI's own real record — never invent funding, results, partners, or letters.**
- **Claim ↔ feasibility:** for every aim, is the ambition matched by a credible means (preliminary data, prior
  method, classical foundation, collaborator, staged de-risking)? If yes, keep the ambitious verb. If no, attach
  the missing evidence or scale the claim. If the support does not exist, **flag the gap for the author** rather
  than papering over it.

## Reviewer-response / rebuttal mode
Match each reviewer point to a specific, verifiable change (new experiment, added citation, revised claim, pointer
to a section/figure). Keep it courteous and terse; no sycophancy ("We thank the reviewer for the insightful…" once
is enough), no over-claiming that a change fully resolves a concern it only partially addresses. Never claim an
experiment was run that was not, or cite a result that does not exist.
