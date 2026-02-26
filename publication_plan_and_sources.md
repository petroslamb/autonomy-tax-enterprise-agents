# Publication Plan and Sources (Split Format, V6)

## Mission
- Convert the current single long-form draft (`article_draft_v5.md`) into a two-part publication package:
1. A breakout narrative essay for forwarding and top-of-funnel reach.
2. A practitioner companion guide for implementation and repeat use.
- Preserve one core claim across both pieces: enterprise agent ROI is constrained more by control-layer costs than model intelligence.

## Strategic Decision
- We are splitting by reader intent, not by topic.
- Piece A answers: "What is the Autonomy Tax, and why does it matter now?"
- Piece B answers: "How do I score a workflow and decide Level 2.5 vs Level 3?"
- The two pieces must feel like one system, not two unrelated posts.

## Output Package
| Piece | Working file | Audience | Promise | Target length |
|---|---|---|---|---:|
| A. Breakout Essay | `article_draft_v6_essay.md` | CTOs, VPs, strategy readers, newsletter audience | Reframe how enterprise agent ROI should be evaluated | 3,000-3,300 words |
| B. Practitioner Guide | `autonomy_tax_scorecard_guide_v1.md` | Staff engineers, platform owners, security/compliance leads | Provide a usable scoring workflow with calibration guidance | 2,000-2,500 words |

## Core Thesis Constants (Locked Across A and B)
- Keep the same title and deck language:
  - Title: `The Autonomy Tax`
  - Deck: `Why Enterprise Agents Fail on Control, Not Intelligence`
- Keep the same equation:
  - `Net Agent Value = Throughput Gain - Human Bandwidth Tax - Incident Tax - Governance Tax`
- Keep the same three-tax definitions and decision philosophy.
- Keep circuit breaker logic as first-class rule:
  - Any single tax score `>= 4` blocks deployment until mitigation.

## Section Decomposition Map (From `article_draft_v5.md`)
| Current section in V5 | Piece A action | Piece B action |
|---|---|---|
| Hook + Thesis + Scope | Keep almost intact | 1 short recap paragraph only |
| Deployment Paradox | Keep, trim for pace | Optional short context paragraph |
| Human Bandwidth Tax | Keep, moderate trim | Keep only scoring-relevant mechanism summary |
| Incident Tax | Keep, moderate trim | Keep only controls that drive scoring criteria |
| Governance Tax | Keep core thesis + key evidence, trim policy detail | Keep full operational checklist + measurement guidance |
| What the Three Taxes Mean Together | Keep | Use as 2-3 sentence bridge |
| Decision Rule: Level 2.5 vs Level 3 | Keep only minimum complete rule (decision flow + taxonomy + one worked example) | Keep full section with all tables and caveats |
| Autonomy Tax Scorecard | Keep preview only (template + one worked row) | Keep full rubric and worksheet |
| Tax Sensitivity by Error Cost | Move to B | Keep full table in B |
| Anti-Thesis | Keep in A | Mention briefly in B and link back |
| Three Things to Do Monday | Keep in A with CTA to B | Reframe as implementation checklist in B |
| 2027 Prediction | Keep as ending in A | Omit from B |
| Appendix and citation index | Move to B (or shared public source page) | Keep full appendix and source navigation |

## Piece A: Target Outline and Budget
| Section | Target words | Notes |
|---|---:|---|
| 1. Hook + Thesis + Scope | 280 | Keep one named incident and thesis declaration in first 3 paragraphs |
| 2. Deployment Paradox | 420 | Preserve the capability vs deployment tension |
| 3. Three Taxes (compressed) | 1,050 | Keep strongest evidence only; trim secondary detail |
| 4. What They Mean Together | 220 | Keep casebook stat signal here |
| 5. Decision Rule Preview | 450 | Include decision flow, taxonomy snapshot, one worked example |
| 6. When Level 3 Wins (Anti-thesis) | 420 | Keep honest boundary condition |
| 7. Three Things to Do Monday | 240 | Keep actions concise and link to full guide |
| 8. 2027 Prediction | 180 | End with falsifiable prediction and callback to hook |
| Total | ~3,260 | Acceptable range: 3,000-3,300 |

## Piece B: Target Outline and Budget
| Section | Target words | Notes |
|---|---:|---|
| 1. One-paragraph thesis recap | 120 | Assume reader may not have read Piece A |
| 2. Decision architecture (Level 2 to 4) | 320 | Full taxonomy table and distinctions |
| 3. Circuit breaker + net score workflow | 280 | Step-by-step scoring sequence |
| 4. Full scoring rubric | 350 | Keep all anchors and constraints |
| 5. Sensitivity by error cost | 240 | Keep table and usage instructions |
| 6. Worked examples | 350 | At least 2 examples: one pass, one blocked |
| 7. Calibration note from casebook | 220 | Show why thresholds are heuristics and how to tune |
| 8. Implementation checklist | 180 | Sprint-level execution checklist |
| 9. Appendix, limitations, citations | 250 | Tiering, caveats, source index |
| Total | ~2,310 | Acceptable range: 2,000-2,500 |

## Non-Negotiables for the Split
- Piece A must still be complete without Piece B:
  - Includes equation, three-tax framing, decision rule summary, and one scored example.
- Piece B must be immediately usable:
  - Includes full rubric, full tables, and explicit workflow steps.
- No contradiction between pieces on thresholds, definitions, or caveats.
- Shared claims must use identical wording for critical quantitative statements.

## Writer Execution Plan (Concrete Steps)
1. Create two new drafts from `article_draft_v5.md`:
   - `article_draft_v6_essay.md`
   - `autonomy_tax_scorecard_guide_v1.md`
2. Perform structural cut first, no rewriting yet:
   - Move full scorecard/rubric/sensitivity material to Piece B.
   - Keep only the minimum decision framework in Piece A.
3. Rewrite Piece A for pace:
   - Remove repeated caveats that are already expressed once.
   - Collapse long transition paragraphs.
   - Keep punch lines and evidence-bearing sentences.
4. Rewrite Piece B for usability:
   - Convert explanatory prose into stepwise instructions.
   - Add one additional worked example if space allows.
5. Add calibration note in Piece B:
   - Explain thresholds are order-of-magnitude heuristics.
   - Anchor tuning suggestions to casebook distribution.
6. Add cross-links in both pieces:
   - Piece A CTA: "Full scoring guide and rubric here."
   - Piece B CTA: "Read the full thesis essay here."
7. Run claim-to-source audit on both pieces independently.
8. Final read pass for each piece in the intended reading mode:
   - A: forwardability and narrative momentum.
   - B: operational clarity and task usability.

## Calibration Requirements (Must Add in Piece B)
- Include a short section called `How to Calibrate the Heuristic`.
- Required baseline references from current casebook:
  - 28 coded records total.
  - 15 records with net `tax` signal.
  - Of those 15, `governance_tax` is primary in 10.
- State explicitly:
  - Thresholds are starting points, not fitted model outputs.
  - Teams should tune by incident cost, reversibility, and review capacity.

## Source Strategy
### Tiering Policy (unchanged)
- Tier 1: Peer-reviewed, major institutions, government records.
- Tier 2: Large-sample surveys and major consulting reports.
- Tier 3: Preprints and working papers (always labeled).
- Tier 4: Vendor content and self-reported metrics (always caveated).
- Tier 5: Standards and framework guidance (context, not proof).

### Source Allocation by Piece
| Source block | Piece A | Piece B |
|---|---|---|
| Proxy incident | Primary in hook | Referenced in examples if needed |
| Deloitte/McKinsey/Anthropic/MAP/METR | Primary for paradox framing | Light reuse only |
| NBER/Xu/Song | Primary for Human Bandwidth argument | Reused as mechanism context |
| CVE/EchoLeak/Agents of Chaos | Primary for Incident Tax | Reused for scoring rationale |
| EU AI Act/NIST/Akto/tooling pricing | Keep only highest-signal points | Keep fuller operational detail |
| Casebook + method notes | One high-signal stat only | Full calibration and reference section |

## Citation Integrity Rules (Apply to Both Pieces)
- Every first-use quantitative claim has direct URL/DOI inline.
- Preprints labeled as preprints at first mention.
- Vendor/self-reported claims include incentive-bias note at first mention.
- Composite scenarios are explicitly labeled as composite.
- Illustrative numbers are explicitly labeled as illustrative.

## Risk Register for Split Format
| Risk | Impact | Mitigation |
|---|---|---|
| Piece A feels incomplete | Reader drop after CTA | Keep minimum complete decision rule and one worked example in A |
| Piece B feels dry or detached | Low usage | Open B with one-paragraph thesis recap and direct link to A |
| Inconsistent thresholds between A and B | Credibility loss | Single source of truth: finalize thresholds in B, mirror in A |
| Duplicate maintenance overhead | Drift over revisions | Update B first for tool logic, then sync summary language in A |
| Citation drift across two files | Audit risk | Run claim-source pass on each file separately before publish |

## Packaging and Distribution Plan
- Publish order:
1. Publish Piece A first.
2. Publish Piece B within 24 hours (or same day if workflow allows).
- Cross-link pattern:
  - Top + bottom links in both directions.
  - Shared short URL labels for easy forwarding.
- Suggested headline pair:
  - Piece A: `The Autonomy Tax`
  - Piece B: `The Autonomy Tax Scorecard: A Practitioner's Guide`

## Pre-Publish QA Checklist
### Piece A (Breakout Essay)
- Hook and thesis land in first 3 paragraphs.
- Contains exactly one primary incident in opening.
- Contains minimum complete decision logic.
- Ends with prediction and clear callback.
- Stays within 3,000-3,300 words.

### Piece B (Companion Guide)
- Workflow can be followed without reading Piece A.
- Includes full rubric, sensitivity table, and examples.
- Includes calibration note and casebook stats.
- Includes full source and limitation notes.
- Stays within 2,000-2,500 words.

### Shared
- All critical numbers source-checked.
- Internal links replaced with public URLs before external publication.
- Terminology and thresholds consistent across both pieces.
