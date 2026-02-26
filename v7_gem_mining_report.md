# V7 Gem Mining Report (All Drafts + Source Corpus)

## Scope Completed
- Reviewed draft evolution: `article_draft_v1.md` through `article_draft_v6B.md`.
- Reviewed source inventory: `sources/source_manifest.tsv` (82 sources), `sources/derived/autonomy_tax_casebook.tsv` (28 coded records).
- Reviewed original seed dialogue: `original_discussion.md` (1,771 lines) and extracted architecture-level insights.
- Deep-read high-signal unused or underused sources, including:
  - `SRC-074` (production-grade workflow best practices)
  - `SRC-077` (incident analysis framework for agents)
  - `SRC-079` (observability and non-deterministic flow findings)
  - `SRC-081` (guardrail architecture + benchmark)
  - `SRC-054`, `SRC-070`, `SRC-056` (security/governance frameworks)
  - `SRC-031`, `SRC-067`, `SRC-059`, `SRC-040`, `SRC-041`, `SRC-057` (macro/capability context)

## Brutal Summary
- `v6A` and `v6B` are strong, but they still leave breakout upside on the table.
- The missing upside is not more stats. It is sharper mechanism language + stronger operator specificity.
- Biggest gap: `v6A` proves *that* control costs matter, but not always *why those costs are structurally inevitable*.
- Biggest gap in `v6B`: practical execution is good, but incident response and design defaults are still lighter than they should be for an operator guide.

## Addendum: Gems from `original_discussion.md`

### Important handling note
- The discussion is useful as architecture framing and operator language, but it is not itself a primary evidence source.
- Any quantitative or market claim from that discussion must still be backed by the source corpus before publication.

### Net-new strategic gems

1. **Bounded Level 3 is the practical target.**
- High-value framing from the thread: mature Level 3 is not unconstrained routing; it is supervisor autonomy inside mandatory graph gates.
- Editorial use: sharpen the Level 2.5 vs Level 3 boundary in `v7A` and `v7B` by explicitly naming "bounded autonomy."

2. **State-gated routing is the cleanest anti-chaos pattern.**
- The strongest architecture concept in the thread: allow dynamic exploration, but hard-override `FINISH` until required checks (test/audit) pass.
- Operator use: add this as a canonical pattern in `v7B` (one short pattern block).

3. **Sub-graph separation (dynamic dev + rigid compliance) is a premium implementation pattern.**
- This gives a credible answer to "how do we keep flexibility without skipping governance."
- Operator use: include as an advanced option in `v7B` without overloading the main flow.

4. **Temporal vs Checkpointer framing is highly clarifying for enterprise readers.**
- Best concise distinction from the thread: infrastructure durability vs agent-state replay/debug.
- Editorial use: one sentence in `v7A` governance/control-layer language; one implementation note in `v7B`.

5. **Reflection vs Critique needs explicit role split.**
- Thread articulates this cleanly: same-agent polish vs separate-agent adversarial review.
- Operator use: add explicit decision rule in `v7B` so teams do not misuse reflection as governance.

6. **Trace stitching is the hidden requirement in hybrid stacks.**
- Practical insight: dropping LangGraph inside durable orchestration creates black-box gaps unless trace context is stitched.
- Operator use: add a "trace continuity" checklist line in `v7B`.

7. **SaaS sprawl and build/buy discipline should be named directly.**
- Strong product reality from thread: too many point tools increase latency, risk, and coupling.
- Editorial use: keep this compact (1-2 lines) as execution realism, not as anti-vendor rant.

## Gem Bank (A-Tier: Must Use)

### A1. Restore the causal mechanism for deployment concentration
- Gem: "software engineering dominates because code is self-verifying" (from `v1`).
- Why it matters: this explains the deployment paradox with mechanism, not just percentages.
- Where to use:
  - `v7A` Deployment Paradox section, immediately after Anthropic/MAP stats.
- Source roots:
  - Draft gem: `article_draft_v1.md` Section I.
  - Supporting context: `SRC-009`, `SRC-073`.
- Expected impact: +0.2 to +0.3 score on clarity/memorability.

### A2. Keep the hook cinematic, then escalate with portfolio risk language
- Gem: scale sentence from prior reviews, but placed after thesis (not in cold-open narrative sentence flow).
- Why it matters: preserves emotional hook while broadening stakes to enterprise-level exposure.
- Where to use:
  - `v7A` paragraph after equation.
- Source roots:
  - Existing `v6A` already partly does this; keep and sharpen.
- Expected impact: +0.2 on shareability.

### A3. Bring back "Boring Stack" as the sticky operating doctrine
- Gem: named doctrine from `v1-v3` (Level 2.5, observable-by-design, cost-bounded).
- Why it matters: breakout essays need a compact, repeatable label readers can quote.
- Where to use:
  - `v7A`: one short doctrine block near end of Decision Rule or Monday section.
  - `v7B`: map checklist items explicitly to Boring Stack pillars.
- Source roots:
  - Draft gem: `v1`, `v2`, `v3` "Boring Stack Thesis" sections.
- Expected impact: +0.2 to +0.4 on memorability.

### A4. Use the 79% nondeterminism signal to harden observability argument
- Gem: user study result: non-deterministic flow as major challenge (79% agreement; broader pain points include root-cause difficulty).
- Why it matters: turns observability from "best practice" to "measured pain in current operations".
- Where to use:
  - `v7A` Governance Tax (1 sentence + note).
  - `v7B` Instrumentation checklist (justify trace-first requirement).
- Source roots:
  - `SRC-079`.
- Expected impact: +0.15 to +0.25 on evidence density in Governance Tax.

### A5. Upgrade governance section with secure lifecycle language from multi-agency guidance
- Gem: secure design, secure development, secure deployment, secure operation/maintenance; security must be core requirement throughout lifecycle.
- Why it matters: reframes governance as engineering lifecycle, not policy overhead.
- Where to use:
  - `v7A` Governance Tax component paragraph.
  - `v7B` Implementation checklist as a lifecycle scaffold.
- Source roots:
  - `SRC-054`, `SRC-070`, `SRC-056`.
- Expected impact: +0.2 on executive credibility.

### A6. Add incident postmortem template (system/context/cognitive factors)
- Gem: incident analysis framework with three cause classes and required evidence artifacts.
- Why it matters: turns Incident Tax from warning into repeatable response mechanism.
- Where to use:
  - `v7B` under mitigation path or add mini "post-incident template" box.
- Source roots:
  - `SRC-077`.
- Expected impact: +0.25 on operator usefulness.

### A7. Pull in production-grade design defaults for Level 2.5 implementation
- Gem: practical defaults: deterministic orchestration, tool-first over ambiguous MCP wrappers, single-tool/single-responsibility agents, pure-function invocation where possible, KISS.
- Why it matters: this is exactly the bridge from theory to build decisions.
- Where to use:
  - `v7B` checklist and calibration notes.
  - Optional one-line reinforcement in `v7A` Decision Rule section.
- Source roots:
  - `SRC-074`.
- Expected impact: +0.25 on practitioner forwarding.

### A8. Keep the Level 2 vs 2.5 distinction explicit everywhere autonomy is discussed
- Gem: Level 2.5 is multi-turn + tools per node, with fixed pipeline order and typed artifacts.
- Why it matters: this is the framework's non-obvious core; if fuzzy, the whole thesis weakens.
- Where to use:
  - `v7A` Decision Rule and one earlier teaser sentence.
  - `v7B` quick reference table and examples.
- Source roots:
  - Strongest wording from `v5` and current `v6B`.
- Expected impact: +0.2 on framework coherence.

### A9. Explicitly define "bounded autonomy" as the enterprise-safe form of Level 3
- Gem: dynamic supervisor routing constrained by mandatory compliance gates.
- Why it matters: resolves the "Level 3 is too stochastic" objection without collapsing back to rigid chains.
- Where to use:
  - `v7A` Decision Rule section (short boundary paragraph).
  - `v7B` Decision Flow or advanced pattern note.
- Source roots:
  - `original_discussion.md` conceptual pattern, aligned to `SRC-074` and `SRC-077` control framing.
- Expected impact: +0.2 on conceptual robustness and reader trust.

### A10. Add a concise operator rule for reflection vs critique
- Gem: reflection for cheap formatting/consistency defects; critique for high-stakes adversarial validation.
- Why it matters: teams frequently overtrust reflection and under-invest in independent review.
- Where to use:
  - `v7B` Worked Examples or checklist section.
- Source roots:
  - `original_discussion.md`, reinforced by incident-analysis and guardrail literature (`SRC-077`, `SRC-081`).
- Expected impact: +0.15 to +0.25 on practical execution quality.

## Gem Bank (B-Tier: Useful if word budget allows)

### B1. Add a short "Known Unknowns" block
- Gem: from `v1` "What We Don't Know Yet".
- Why it matters: raises trust and intellectual seriousness.
- Where: endnotes-adjacent in `v7A` or appendix lead-in in `v7B`.

### B2. Add a compact "why benchmark wins do not equal production reliability" line
- Gem: GAIA/SWE-bench/RE-Bench style capability-performance context.
- Why it matters: protects against capability-counterargument in comments.
- Where: Deployment Paradox, one sentence only.
- Sources: `SRC-040`, `SRC-041`, `SRC-057`.

### B3. Add one sentence on governance cost as delayed failure tax
- Gem: secure-by-design guidance explicitly acknowledges up-front cost and later redesign avoidance.
- Why it matters: improves CFO/CTO framing.
- Where: Governance Tax paragraph.
- Sources: `SRC-054`, `SRC-070`.

## Not Gems (Do Not Spend Word Budget Here)
- `SRC-028` Anthropic Economic Index raw HTML capture is noisy and not extraction-friendly in current corpus state.
- `SRC-027` KPMG pulse data is usable as directional context but weak relative to stronger anchors already present.
- `SRC-035` OECD incident monitor entries include AI-generated summaries; weak for precise claim-level support.
- `SRC-059` PwC Jobs Barometer is marketing-heavy for this thesis and may dilute rigor.
- Broad labor displacement macro (BLS/PwC) is interesting but off-axis for this piece's control-layer argument.

## Missed Gems in Current v6 (Concrete)
1. Missing mechanism sentence in Deployment Paradox (why engineering dominates beyond concentration data).
2. Governance Tax still under-leverages formal secure lifecycle framing from multi-agency guidance.
3. v6B does not yet include a concrete incident RCA template despite discussing mitigation.
4. v6 package underuses named doctrine memory effect ("Boring Stack") that earlier drafts had.
5. v6B operational guidance can be tighter by encoding production design defaults from `SRC-074`.

## Section-by-Section Insertion Map for v7

### v7A (Essay)
- Deployment Paradox:
  - Add 1 mechanism sentence (self-verifying feedback loop in engineering vs ambiguous feedback in legal/ops).
- Governance Tax:
  - Add 1 sentence with 79% nondeterministic-flow pain signal.
  - Add 1 sentence framing governance as secure lifecycle (design -> dev -> deploy -> operate).
- Decision Rule:
  - Preserve current Level 2.5 definition and add one short contrast with Level 2.
- Near ending / Monday lead:
  - Add compact "Boring Stack" doctrine line (3 pillars max).

### v7B (Companion)
- Decision Flow or Checklist:
  - Add "Design Defaults" sub-block with 4 defaults from `SRC-074`.
- Worked Examples / Mitigation:
  - Add "Incident RCA mini-template" (system/context/cognitive + required logs).
- Implementation Checklist:
  - Align checklist stages to secure lifecycle terms (design/dev/deploy/operate).

## Evidence Quality Guardrails for V7
- Keep all numeric claims tethered to existing notes style.
- If using preprints, keep one concise caveat at first mention only.
- Prefer adding mechanism sentences over adding new numbers.
- Preserve readability priority: each new addition must either sharpen mechanism or improve operator execution.

## Net Assessment: Have We Found the Real Remaining Upside?
Yes. The remaining upside is now clearly bounded:
- Add 5-8 high-leverage lines (not 500 more words).
- Strengthen operational specificity in `v7B`.
- Reintroduce one sticky doctrine label for recall.

If these A-tier gems are integrated cleanly, v7 has a credible path into 9-territory quality while staying tight.
