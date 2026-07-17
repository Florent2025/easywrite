# Easywrite Smoke-Test Benchmark

Small, hand-checkable cases to sanity-check a change to the skill. Each case = input + what a correct pass must do
(should-fix) and must NOT do (false-positive / fidelity guard). Not a detector score suite — those swing ±10–20 pts.

## Should-fix (the rewrite must address these)

| # | Input | Must fix |
|---|-------|----------|
| S1 | "In recent years, X has attracted increasing attention." | Remove formulaic opener; replace with a specific limitation/fact. |
| S2 | "We prove our method significantly outperforms all prior work." | Downgrade "prove/significantly" to match evidence; keep any number. |
| S3 | "The method serves as a testament to its pivotal role — underscoring its importance." | Kill copula avoidance, em-dash, vocab cluster, significance hype. |
| S4 | "Experts argue this is crucial." (no cite) | Flag missing source or soften; do NOT invent a citation. |
| S5 | 中文 "随着……的快速发展，本文创新性地提出全新框架，大量实验充分证明其显著优越性。" | 去套话开场 + 拔高词；换成具体问题/数据。 |
| S6 | Three consecutive 18-word sentences. | Break rhythm; introduce a short sentence (burstiness). |
| S7 | A paragraph with delve + leverage + seamless + robust together. | Substitute ≥2 downward to plain diction. |
| S8 | "We thank the reviewer for the insightful comment; we fully addressed it." | Cut sycophancy + unverifiable "fully addressed"; tie to a specific change. |

## Fidelity / false-positive guards (the rewrite must NOT do these)

| # | Input | Must preserve / must NOT do |
|---|-------|-----------------------------|
| F1 | "accuracy improved by 4.2 points (p < 0.01, Table 3)." | Keep 4.2, p<0.01, Table 3 verbatim. No rounding, no dropping. |
| F2 | "The results suggest X may indicate Y." | Keep the evidence-tied hedge; do NOT turn "suggest" into "prove". |
| F3 | "Samples were normalized to total protein." | Keep the actor-irrelevant passive. |
| F4 | "We use the AdamW optimizer with cite key [smith2021]." | Keep method name and [smith2021] exactly. |
| F5 | A single em-dash inside a quoted sentence being discussed. | Do NOT edit inside the quotation. |
| F6 | Grant: "Our long-term goal is to establish a foundation for…" | Do NOT flatten the vision (proposal register); check feasibility footing instead. |
| F7 | An already evidence-dense paragraph (dates, named scholars, page cites). | Leave it alone; editing raises AI score. |
| F8 | Text < 300 words asking for a "detector score" fix. | Note detector unreliability at this length; don't over-fit. |

## How to run
There is no automated grader here (LLM-judged rewrites vary). Run the cases through the skill and eyeball each
against its column. For AI-tell density counts on English text, the installed `humanize-prose` skill ships
`scripts/ai_tell_scan.py`. A regression = any F-guard violated or any S-case left unaddressed.
