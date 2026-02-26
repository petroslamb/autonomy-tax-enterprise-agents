# Publication Plan and Sources (V7 Breakout Operating Spec)

## Primary Objective
Publish a three-piece package where `article_draft_v7A.md` is a true breakout flagship and `v7B`/`v7C` increase trust and execution without diluting narrative force.

## Breakout Contract (V7A is Non-Negotiable)

### What "breakout" means here
- Readers can repeat the thesis in one sentence after one read.
- The post contains at least 3 quotable lines that travel independently on social/email.
- Executives feel urgency; operators feel they got a concrete decision framework.
- It holds up under technical pushback because every key claim is source-backed or explicitly marked as synthesis.

### V7A target score
- Editorial score target: **9.0-9.3**.
- Minimum publish score: **9.0**.
- If below 9.0, do not publish A as final.

### V7A kill conditions
- Hook becomes analytical too early and loses narrative pull.
- Core framework terms are inconsistent or fuzzy.
- Section-level claims cannot be traced to source IDs.
- A drifts into implementation depth that belongs in B/C.

## Stable Reader Personas (Keep)
- VP Engineering / CTO: strategic risk, sequencing, and capital allocation decisions.
- Platform / Staff Engineer: architecture constraints and reliability tradeoffs.
- Applied AI / Agent Engineer: build patterns, failure controls, and instrumentation choices.

## Stable Writing Style (Keep)
- High signal, direct, technical.
- No hype language.
- Claims are precise and caveated where required.
- Readable by executives, usable by operators.

## Locked Editorial Decisions
1. Keep the current cinematic incident hook intact.
2. Keep scaling language after thesis/equation, not inside the cold-open flow.
3. Do not move full framework block above the three-tax explanation.
4. Keep one canonical primary term across pieces for the middle maturity tier.

## Package Role Separation (Hard Boundary)
- A (`v7A`): Why this matters now.
- B (`v7B`): Which workflows qualify and how to score/deploy this week.
- C (`v7C`): How bounded autonomy is built and governed in production.

### Overlap budget
- A with B/C: <= 15% repeated material.
- B with C: <= 20% repeated material.
- Any repeated material must be short and purpose-specific.

## Original Contributions (Defensible)

### Contribution 1: The Autonomy Tax decision model
- `Net = Benefit - Average(HB Tax, Incident Tax, Governance Tax)`.
- Circuit breaker (`any tax >= 4 => blocked`) as a practical governance gate.

### Contribution 2: Level 2 vs 2.5 vs bounded 3 framing
- Level 2.5 explicitly defined as fixed-sequence, multi-turn, tool-using nodes with typed artifact handoffs and predetermined human gates.
- Bounded Level 3 defined as dynamic routing inside mandatory compliance and escalation constraints.

### Contribution 3: Casebook-backed synthesis layer
- The `autonomy_tax_casebook.tsv` normalization of 28 public records into a common schema is original synthesis, auditable via source IDs.

### Contribution 4: Anti-thesis boundary conditions
- Explicit conditions where Level 3 can win economically (low per-error cost, high volume, reversibility).

### Contribution 5: Control-plane operating pattern
- State-gated routing, trace continuity, and incident loop closure framed as control-layer requirements rather than optional enhancements.

### Contribution 6: Reflection vs critique control split
- Reflection as low-cost quality cleanup.
- Critique as independent adversarial control for high-stakes decisions.

## Terminology Lock (Use Exactly)

### Canonical terms
- **Autonomy Tax**: combined hidden costs that rise with autonomy.
- **Level 2.5 - Artifact Pipeline**: fixed pipeline, each node is multi-turn and tool-using, typed artifacts between nodes, human gates at predetermined points.
- **Bounded Level 3**: dynamic routing allowed, but hard constraints/gates cannot be bypassed.
- **Circuit Breaker**: any tax score `>= 4` blocks deployment.
- **Control Layer**: observability, guardrails, durability, governance, and incident response mechanisms.

### Optional descriptors (use sparingly)
- `managed autonomy` (descriptor of Level 2.5; at most once per piece).
- `state-gated autonomy` (descriptor of bounded Level 3; at most once per piece).

### Terms to avoid as primary labels
- `Level 2.5 managed autonomy` as full replacement term.
- `agent swarms` unless discussing explicit Level 4 context.

## Gaps Identified in Latest Materials

### Gap A1: Mechanism density in A still under target
**Importance:** High
**Reason:** Breakout essays need a causal engine, not only evidence snapshots.
**Action:** Add one clean mechanism sentence in Deployment Paradox tying concentration to verification asymmetry.

### Gap A2: Memory-anchor language is present but not yet maximized
**Importance:** High
**Reason:** Shareability depends on repeatable doctrine lines.
**Action:** Keep one compact doctrine line in A and map it explicitly to B/C operating rules.

### Gap A3: Framework boundary can still blur for skimmers
**Importance:** High
**Reason:** If Level 2.5 is misunderstood, the thesis collapses into generic "human-in-loop" advice.
**Action:** Add a one-line contrast near first mention: Level 2 is single-turn nodes; 2.5 is multi-turn tool loops with fixed sequence.

### Gap B1: Operator response loop needs stronger incident mechanics
**Importance:** Medium
**Reason:** B should not stop at scoring; it needs repeatable post-incident procedure.
**Action:** Add compact RCA template using system/context/cognitive factors plus required evidence fields.

### Gap C1: C risks sprawl into tool catalog
**Importance:** High
**Reason:** Tool-listing weakens authority and reduces implementation clarity.
**Action:** Keep C architecture-first, with strict include/exclude boundaries and minimal vendor mention.

### Gap X1: Discussion-derived ideas need source discipline
**Importance:** High
**Reason:** The original discussion is framing input, not empirical evidence.
**Action:** Tag concepts as synthesis unless directly anchored to source corpus.

## Sentence Bank (High-Leverage Draft Lines)

### V7A breakout sentence bank
- "The model did not fail. The control layer did."
- "Enterprise agent ROI breaks at the control surface before it breaks at model intelligence."
- "That was one retry loop. Most enterprises are planning dozens of autonomous workflows."
- "The bottleneck is no longer generation. It is verification."
- "Better models increase what agents can do; they also increase what organizations must govern."
- "Level 2.5 is not a compromise. It is how enterprises buy capability without buying chaos."
- "If one tax is a 4, autonomy is blocked until the control is real, not promised."

### V7B operator sentence bank
- "Score first, deploy second."
- "No workflow graduates to autonomy without passing the circuit breaker."
- "Reflection fixes formatting errors; critique catches decision errors."
- "If you cannot reconstruct the decision path, you do not have production readiness."

### V7C control-plane sentence bank
- "Dynamic routing without hard gates is just stochastic privilege escalation."
- "Bounded autonomy means the graph can explore, but it cannot bypass compliance nodes."
- "Durability keeps execution alive; state persistence keeps agent reasoning inspectable."
- "Trace continuity is the contract between AI engineering and platform operations."

## Piece Blueprints

## Piece A (`article_draft_v7A.md`) - Breakout Flagship
### Purpose
Narrative-first argument that resets how enterprise leaders evaluate agent ROI.

### Required structure
1. Cinematic incident hook.
2. Thesis + equation + scale bridge.
3. Deployment paradox with mechanism sentence.
4. Three taxes with compounding logic.
5. Decision rule boundary (Level 2.5 vs bounded Level 3).
6. Anti-thesis where Level 3 wins.
7. Monday actions.
8. 2027 falsifiable prediction.

### Word target
- 2050-2250.

### Must not include
- Architecture deep dives, tool matrices, framework comparisons.

### Source anchors (minimum)
- `SRC-026`, `SRC-007`, `SRC-009`, `SRC-073`, `SRC-039`, `SRC-050`, `SRC-049`, `SRC-060`, `SRC-012`, `SRC-076`, `SRC-075`, `SRC-021/064/065`, `SRC-079`.

## Piece B (`article_draft_v7B.md`) - Operator Scorecard
### Purpose
Runnable workflow-selection and mitigation guide.

### Required structure
1. Compact taxonomy and decision flow.
2. Circuit breaker + net score usage.
3. Rubric + sensitivity table.
4. Worked examples and mitigation path.
5. Calibration method and known limits.
6. Incident RCA mini-template.
7. Reflection vs critique rule.
8. Optional appendix (explicitly labeled optional reference).

### Word target
- 1800-2050.

### Must not include
- Narrative thesis repetition, architecture debates better suited for C.

### Source anchors (minimum)
- `SRC-071`, `SRC-072`, `SRC-073`, `SRC-077`, `SRC-074`, `SRC-079`, plus casebook assets.

## Piece C (`article_draft_v7C.md`) - Control Plane Companion
### Purpose
Define implementable bounded-autonomy architecture for enterprise operations.

### Required structure
1. Why control-plane failures dominate.
2. Level 2.5 vs bounded Level 3 operating modes.
3. State-gated routing pattern.
4. Dynamic subgraph + rigid compliance handoff.
5. Durability layering (orchestration durability vs agent-state persistence).
6. Observability and trace stitching.
7. Reflection vs critique controls.
8. Incident closure loop (detect -> RCA -> mitigation -> re-score).
9. Build-vs-buy boundary criteria.
10. Adoption ladder and rollout sequencing.

### Word target
- 1800-2200.

### Must not include
- Vendor shopping lists, speculative Level 4 tours, framework flame wars.

### Source anchors (minimum)
- `SRC-074`, `SRC-077`, `SRC-079`, `SRC-038`, `SRC-054`, `SRC-070`, `SRC-056`, `SRC-071`, `SRC-072`, `SRC-078`.

## Claim-to-Source Assignment (Required)

| Core claim | Primary source IDs | Piece |
|---|---|---|
| Deployment intent vs current maturity gap | `SRC-007`, `SRC-008` | A |
| Tool-call concentration in software engineering | `SRC-009` | A |
| Production agents remain bounded/human-evaluated | `SRC-073` | A, B |
| Expert review bottleneck mechanism | `SRC-050`, `SRC-049`, `SRC-060` | A, B |
| Incident combinatorial risk | `SRC-026`, `SRC-012`, `SRC-076`, `SRC-075` | A, B, C |
| Governance visibility and maturity deficit | `SRC-007`, `SRC-010`, `SRC-079` | A, C |
| Secure lifecycle framing | `SRC-054`, `SRC-070`, `SRC-056` | A, C |
| Workflow-first design guidance | `SRC-071`, `SRC-072`, `SRC-074` | B, C |
| Incident analysis template structure | `SRC-077` | B, C |
| Telemetry standards / observability contract | `SRC-038`, `SRC-079` | C |

## Publish Hygiene (Hard Requirements)
- All links must be public URLs.
- No relative repository links in publication copy.
- Replace temporary GitHub links with Substack URLs on publish day.
- Ensure note markers do not stack excessively in one paragraph.

## QA Gates (Pass/Fail)

### Gate 1: Breakout quality (A only)
- [ ] Hook is cinematic and intact.
- [ ] At least 3 high-retention lines from sentence bank survive final edit.
- [ ] Causal mechanism is explicit in at least 3 key sections.

### Gate 2: Role separation
- [ ] A narrative-first, B operator-first, C architecture-first.
- [ ] Overlap budget respected.

### Gate 3: Terminology and math lock
- [ ] Canonical terms unchanged.
- [ ] Formula and thresholds identical across pieces.
- [ ] Level 2.5 definition includes multi-turn + tools + fixed sequence.

### Gate 4: Evidence integrity
- [ ] Every quantitative claim mapped to source IDs.
- [ ] Discussion-derived concepts are marked synthesis unless sourced.
- [ ] Caveats retained at first mention of weaker evidence.

### Gate 5: Usability
- [ ] B executable in one sitting.
- [ ] C implementable by a platform/architecture team without extra context.

## Scoring Framework

| Dimension | Weight | A Target | B Target | C Target |
|---|---:|---:|---:|---:|
| Narrative force and memorability | 25% | 9.3 | 8.3 | 8.2 |
| Conceptual clarity and terminology discipline | 20% | 9.1 | 9.0 | 9.0 |
| Evidence integrity and caveat quality | 20% | 9.0 | 9.0 | 8.9 |
| Operator usefulness | 20% | 8.6 | 9.2 | 9.1 |
| Structural coherence and role separation | 15% | 9.0 | 9.0 | 8.9 |

### Publish threshold
- A must score >= 9.0.
- B and C must each score >= 8.7.
- Package weighted score must be >= 9.0.

## Execution Sequence
1. Finalize v7A for breakout quality first.
2. Finalize v7B to operationalize A without repeating it.
3. Finalize v7C to carry architecture depth and protect A from scope creep.
4. Run full QA gate pass across all three pieces.
5. Final publish hygiene pass and link replacement.

## Core Assets
- `sources/source_manifest.tsv`
- `sources/derived/autonomy_tax_casebook.tsv`
- `sources/derived/autonomy_tax_casebook_method.md`
- `assets/autonomy_tax_scorecard_rubric.md`
- `assets/autonomy_tax_scorecard_template.csv`
- `v7_gem_mining_report.md`
- `original_discussion.md` (framing only, not primary evidence)

## Final Standard
If A is not clearly breakout by the gates above, postpone publication and revise. B and C exist to amplify A, not compete with it.
