# English AI-Tell Catalog

Scannable catalog of the patterns that mark English prose as AI-generated, with fixes. Synthesized from
Wikipedia's *Signs of AI writing* (via `humanizer`), `stop-slop`, and `humanize-prose`. **Judge by clusters,
not isolated hits** — the false-positive guards at the bottom matter as much as the patterns.

## A. Content tells

1. **Significance / legacy inflation** — "marks a pivotal moment", "stands as a testament to", "reflects a
   broader shift", "setting the stage for", "left an indelible mark". → State the plain fact. *"was established
   in 1989 to publish regional statistics."*
2. **Notability padding** — listing outlets/follower counts to prove importance. → Cite the one thing that
   actually matters, with context.
3. **Superficial "-ing" tails** — "..., highlighting its importance", "..., reflecting the community's deep
   connection". Fake depth bolted onto a sentence. → Cut the tail or make it a real, sourced clause.
4. **Promotional / figurative language** — "vibrant", "rich cultural heritage", "nestled in the heart of",
   "breathtaking", "groundbreaking" (figurative), "renowned". → Neutral description.
5. **Vague attribution / weasel words** — "experts argue", "studies show", "observers have cited",
   "industry reports" with no actual source. → Name the source or drop the claim. Never invent one.
6. **Formulaic "Challenges and Future Prospects" sections** — "Despite these challenges, X continues to
   thrive." → Replace with the specific facts.

## B. Language & grammar tells

7. **AI vocabulary words** — actually, additionally, align with, crucial, delve, emphasize, enduring, enhance,
   foster, garner, highlight (v.), interplay, intricate/intricacies, key (adj.), landscape (abstract),
   leverage (filler), pivotal, realm, seamless, showcase, streamline, tapestry, testament, underscore,
   valuable, vibrant. **Tell = 2–3 in one paragraph**, not one in isolation. → Plain substitutes: use, look at,
   show, build, help, do; important, solid, smooth, new — or cut the adjective.
8. **Copula avoidance** — "serves as / stands as / represents / boasts / features". → "is / has".
9. **Negative parallelism** — "not only… but…", "it's not just X, it's Y", plus clipped tailing negations
   ("no guessing", "no wasted motion"). → State Y directly, as a real clause.
10. **Rule of three** — forcing ideas into triples to sound comprehensive ("innovation, inspiration, and
    insights"). → Two items, or vary the count.
11. **Elegant variation** — cycling synonyms for one referent (protagonist → main character → central figure →
    hero). → Pick one and repeat it.
12. **False ranges** — "from the Big Bang to dark matter, from X to Y" where X/Y aren't on one scale. → List them plainly.
13. **Passive / subjectless fragments** — "No configuration needed.", "The results are preserved automatically."
    → Name the actor when it clarifies. (But keep passive when the actor is genuinely irrelevant — see guards.)

## C. Style tells (mostly hard constraints)

14. **Em-dashes & en-dashes (— –)** — the most reliable single tell. **Zero in the final draft.** Recast with
    period / comma / colon / parentheses. Also catch spaced `—`, `--`. Scan the output for `—` and `–` before shipping.
15. **Semicolons** — a softer tell; in detector-sensitive work, split into two sentences (in scholarship an
    occasional one is fine — judge by context).
16. **Boldface abuse** — mechanically bolding phrases or every list item's lead-in. → Prose or plain lists.
17. **Inline-header vertical lists** — "- **Performance:** Performance has been enhanced…". → Fold into a sentence.
18. **Title Case Headings** → sentence case.
19. **Emojis** decorating headings/bullets → remove.
20. **Curly quotes only** — weak tell (editors auto-curl); count only when clustered with others.

## D. Communication / register tells

21. **Chatbot artifacts** — "Here is an overview…", "I hope this helps", "Would you like me to expand?",
    "Certainly!", "You're absolutely right!". → Delete; start with the content.
22. **Knowledge-cutoff disclaimers & speculative gap-fill** — "as of my last update", "while specific details
    are limited…", then invented filler ("likely grew up…", "maintains a low profile"). → Say what isn't known, or cut.
23. **Sycophantic / servile tone** — "Great question!", "That's an excellent point." → Cut.

## E. Filler, hedging, rhetoric

24. **Filler phrases** — "in order to" → "to"; "due to the fact that" → "because"; "at this point in time" →
    "now"; "has the ability to" → "can"; "it is important to note that the data shows" → "the data shows".
25. **Excessive hedging** — "could potentially possibly be argued that it might have some effect". → "may affect".
    (Distinct from *evidence-tied* hedging, which is required — see guards.)
26. **Generic positive conclusions** — "the future looks bright", "exciting times lie ahead". → A concrete next fact.
27. **Hyphenated-pair overuse in predicate position** — "the report is high-quality/data-driven". → Keep the
    hyphen attributively ("a high-quality report"), drop it after the noun ("the report is high quality").
28. **Persuasive-authority tropes** — "the real question is", "at its core", "what really matters",
    "fundamentally", "the heart of the matter". → Say the ordinary point without the ceremony.
29. **Signposting** — "Let's dive in", "here's what you need to know", "without further ado". → Just do the thing.
30. **Fragmented header** — a heading, then a one-line paragraph restating the heading. → Delete the restatement.
31. **Diff-anchored writing** — describing a thing by what changed ("this function was added to replace…").
    → Describe it as it is (except in changelogs/migration guides).
32. **Manufactured punchlines / staccato drama** — a run of short declaratives to fake momentum ("It had no
    preference. No aesthetic prior. No nostalgia."). → One emphatic sentence is fine; a stack is engineered.
33. **Aphorism formulas & fake-candid openers** — "X is the Y of Z", "not a tool but a mirror"; "Honestly?",
    "Here's the thing", "Look,". → The concrete claim, said plainly.

## The 2026 vocabulary clusters (density check, not a purge)

| Cluster | Members | Plain replacement |
|---|---|---|
| Abstract verbs | delve, leverage, underscore, streamline, unleash, foster, harness, facilitate | use, look at, show, build, push, help, do |
| Inflated adjectives | pivotal, robust, seamless, innovative, cutting-edge, multifaceted, comprehensive, holistic | important, solid, smooth, new, detailed — or cut |
| Flowery metaphors | tapestry, landscape, realm, symphony, beacon, journey, ecosystem, fabric | a concrete noun; keep at most one load-bearing metaphor per essay |
| Formal transitions | furthermore, moreover, additionally, notably, in conclusion | also, but, so, and — or none |

Rule: scan for **clusters**. Two or three in the same paragraph → substitute downward. One "pivotal" in 1,500 words is fine.

## False-positive guards (do NOT flag these alone)

Clean human writers hit these without any AI. Flag only in **clusters**:
- Perfect grammar / consistent style (professionals get edited).
- Mixed casual+formal register (often a technical or ESL writer, not a bot).
- "Bland/robotic" prose without specific tells — that's just dry writing.
- Formal/academic vocabulary in general — AI overuses *specific* fancy words (§7), not all of them. Don't flatten "ostensibly".
- A single em-dash, one "however", curly quotes alone, one short emphatic sentence, one letter-style sign-off.
- Unsourced claims (most of the web is unsourced — lack of a cite isn't proof).
- **Evidence-tied hedging** ("suggests", "appears to") — required in scholarship.
- **Passive voice when the actor is irrelevant** ("samples were normalized").
- Secondhand text: never rewrite a watched phrase that sits inside a quotation, title, or example being *discussed*.

Signs of genuine human authorship (preserve, don't touch): specific hard-to-fabricate detail; mixed feelings /
unresolved tension; dated era-bound references; defensible first-person editorial choices; real variety in
sentence length; genuine self-corrections and parentheticals.
