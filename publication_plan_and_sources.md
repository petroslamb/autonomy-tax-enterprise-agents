# Publication Plan and Sources (V9 Breakout Operating Spec)

## Primary Objective
Ship a three-piece package where `article_draft_v9A.md` is a breakout flagship and `v9B`/`v9C` deepen trust and execution without stealing narrative oxygen from A.

## Baseline From V8 (Starting Point)
- `v8A` has strong thesis and evidence discipline, but reads closer to a high-end analyst brief than a breakout essay.
- `v8B` is operationally useful but over-extended; it needs tighter runbook ergonomics.
- `v8C` is structurally strong, but still missing explicit durability and build-vs-buy treatment from the blueprint.
- Package overlap is currently acceptable, but A still includes decision mechanics that belong in B.

## Breakout Contract (A Is Non-Negotiable)

### What "breakout" means
- A reader can restate the thesis in one sentence after one read.
- The piece contains at least three independent, quotable lines with high recall.
- Executives feel urgency, operators trust the logic, skeptics cannot dismiss evidence discipline.
- The argument has one dominant causal engine: control-layer economics, not model intelligence, sets enterprise ROI ceilings.

### V9A publish threshold
- Target score: `9.0-9.3`.
- Minimum publish score: `9.0`.
- If `< 9.0`, do not publish A.

### Kill conditions
- Hook loses cinematic momentum inside first 200 words.
- Framework appears before stakes are established.
- A drifts into implementation depth or workbook detail better suited for B/C.
- Evidence caveats are absent at first mention of weaker sources.

## Canonical Package Roles (Hard Boundary)
- A (`v9A`): Why enterprise agent ROI breaks and what decision doctrine follows.
- B (`v9B`): How to score workflows, mitigate blocked cases, and run the operating loop.
- C (`v9C`): How to design and govern the control plane in production.

### Overlap budget
- A with B/C: `<= 12%`.
- B with C: `<= 18%`.
- Repeated lines must be doctrine anchors only.

## Terminology Lock (Use Exactly)
- **Autonomy Tax**: combined hidden costs that rise with autonomy.
- **Level 2.5 - Artifact Pipeline**: fixed pipeline, multi-turn tool-using nodes, typed artifacts, predetermined human gates.
- **Bounded Level 3**: dynamic routing allowed, non-bypassable policy/compliance/escalation constraints.
- **Circuit Breaker**: any tax score `>= 4` blocks deployment.
- **Control Layer**: observability, guardrails, durability, governance, incident response.

## V9 Improvement Plan (By Piece)

## Piece A (`article_draft_v9A.md`) - Breakout Flagship

### Objective
Convert A from "excellent analysis" into "must-share thesis" while preserving technical credibility.

### Target shape
- Narrative body: `1900-2150` words.
- Notes/endnotes: concise, non-redundant, avoid stacked markers.
- Reading mode: one clean argument arc, eight sections max before notes.

### Required structure and word budget
| Section | Target words | Keep / change |
|---|---:|---|
| Cinematic incident hook + thesis bridge | 230-280 | Keep hook; tighten to one failure chain and one consequence line |
| Deployment paradox | 180-220 | Keep strongest stats, add one explicit mechanism sentence |
| Three taxes | 430-520 | Keep all three taxes, remove duplicate examples |
| Compounding logic | 170-220 | Keep one concrete cascade example, delete redundancy |
| Decision boundary (2.5 vs Bounded 3) | 170-220 | Keep rule, move worked mechanics to B |
| Anti-thesis (when Bounded 3 wins) | 140-180 | Keep inequality and one exception case |
| Monday actions | 120-160 | Keep 3 actions, tighten outputs/timeboxes |
| 2027 falsifiable prediction + close | 180-240 | Keep falsifiers, shorten meta-commentary |

### Exact breakout edits (surgical)
1. Keep the cold open exactly as narrative first; remove any formula-like framing until after the three-tax setup.
2. Introduce the formula only at the Decision Boundary section, not in opening argument.
3. Cut implementation-heavy passages from A and move them to B:
   - Detailed scoring workflow mechanics.
   - Multi-step mitigation details better suited to scorecard operations.
4. Compress "Known Unknowns" into a short "limits" close (60-100 words) or absorb into caveat lines inside relevant sections.
5. Keep only one doctrine block in A: `Constrain routing, type the artifacts, gate external action.`
6. Force three memory anchors to survive final cut:
   - "The model did not fail. The control layer did."
   - "The bottleneck is no longer generation. It is verification."
   - "If one tax is a 4, autonomy is blocked until the control is real, not promised."
7. Reduce parenthetical caveats in-flow; move lower-priority caveats to notes so prose velocity stays high.
8. End with one sharp decision question for leaders, not a broad summary paragraph.

### A rewrite workflow (exact pass order)
1. **Pass 1: Structural cut**
   - Remove or move 250-400 words of operator detail to B.
   - Ensure formula/circuit breaker first appears at decision section.
2. **Pass 2: Causal tightening**
   - Add one mechanism line in deployment paradox.
   - Add one compounding line connecting all three taxes in one incident chain.
3. **Pass 3: Quote hardening**
   - Keep exactly 3-5 travel lines.
   - Delete lines that are true but not repeatable.
4. **Pass 4: Evidence and caveat pass**
   - Confirm every number has a source.
   - Mark synthesis where evidence is bridged.
5. **Pass 5: Breakout gate test**
   - One-sentence recall test.
   - 30-second skim test: thesis and rule visible without reading full piece.

### A QA gate (must pass all)
- Hook stays cinematic for first 180+ words.
- One-sentence thesis appears once and is unmistakable.
- Three taxes are causal, not just descriptive.
- Decision boundary between Level 2.5 and Bounded Level 3 is explicit and short.
- At least three quotable lines remain.
- Final score `>= 9.0`.

## Piece B (`article_draft_v9B.md`) - Operator Scorecard

### Objective
Turn B into the operational workbook teams can run in one week.

### Improvement actions
1. Trim to `2000-2200` words total by reducing narrative restatement of A.
2. Keep taxonomy and decision flow, but compress explanatory prose around obvious concepts.
3. Keep worked examples and mitigation path; make each example decision in one line at the end.
4. Preserve incident RCA template and reflection-vs-critique split.
5. Keep calibration section, but move deep source-method detail to optional appendix.
6. Add one "first 7 days" execution box with strict deliverables.

### B QA gate
- Runnable without reading A.
- Circuit breaker impossible to miss.
- Net-score mechanics consistent with A and rubric assets.
- No architecture sprawl that belongs in C.

## Piece C (`article_draft_v9C.md`) - Control Plane Companion

### Objective
Make C the architecture/governance playbook for bounded autonomy in production.

### Improvement actions
1. Add explicit durability section:
   - orchestration durability (workflow retries/state),
   - agent-state persistence (memory/reasoning artifacts),
   - failure semantics across both.
2. Add explicit build-vs-buy boundary section with criteria:
   - control requirements,
   - integration complexity,
   - incident/compliance ownership model.
3. Keep five-question framing, but tighten repetitive rhetoric.
4. Preserve state-gated routing, trace continuity, and incident closure loop as non-bypassable controls.
5. Keep vendor references minimal and principle-first.

### C QA gate
- Architecture-first throughout.
- Durability and build-vs-buy explicitly covered.
- Observability described as end-to-end trace continuity, not dashboard count.

## Breakout Scoring Rubric (V9 Editorial)
| Dimension | Weight | Pass threshold |
|---|---:|---:|
| Hook and narrative pull | 15% | >= 9 |
| Thesis clarity and recall | 15% | >= 9 |
| Causal mechanism quality | 15% | >= 9 |
| Evidence integrity and caveating | 15% | >= 8.5 |
| Quotability / shareability | 10% | >= 9 |
| Structure and pacing | 10% | >= 8.5 |
| Role separation discipline | 10% | >= 9 |
| Operator utility without overload | 10% | >= 8.5 |

## Claim-to-Source Assignment (Required)
| Core claim | Primary source IDs | Piece |
|---|---|---|
| Deployment intent vs maturity gap | `SRC-007`, `SRC-008` | A |
| Tool-call concentration in software engineering | `SRC-009` | A |
| Production agents remain bounded/human-evaluated | `SRC-073` | A, B |
| Expert review bottleneck mechanism | `SRC-050`, `SRC-049`, `SRC-060` | A, B |
| Incident combinatorial risk | `SRC-026`, `SRC-012`, `SRC-076`, `SRC-075` | A, B, C |
| Governance maturity and visibility deficit | `SRC-007`, `SRC-010`, `SRC-079` | A, C |
| Secure lifecycle framing | `SRC-054`, `SRC-070`, `SRC-056` | A, C |
| Workflow-first design guidance | `SRC-071`, `SRC-072`, `SRC-074` | B, C |
| Incident analysis structure | `SRC-077` | B, C |
| Observability/telemetry contract | `SRC-038`, `SRC-079` | C |

## Delivery Sequence (V9)
1. Rewrite A first and lock breakout score.
2. Refactor B to absorb A overflow and tighten operator flow.
3. Refactor C to add durability + build-vs-buy sections.
4. Run cross-piece consistency QA on terminology, thresholds, and overlap.
5. Final source integrity audit and publication formatting pass.

## Publish Hygiene (Hard Requirements)
- All links must be public URLs.
- No relative repository links in publication copy.
- Replace temporary GitHub links with Substack URLs on publish day.
- Keep citation density readable; avoid marker clusters.

## Final Pass/Fail Checklist
- [ ] A scores `>= 9.0` on V9 rubric.
- [ ] B and C each score `>= 8.5`.
- [ ] Role separation and overlap budgets are respected.
- [ ] Canonical terms and thresholds are consistent across all pieces.
- [ ] Every quantitative claim maps to a source ID.
