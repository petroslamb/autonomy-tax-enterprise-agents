# The Autonomy Tax Scorecard: A Practitioner's Guide

*The decision framework and scoring workflow for enterprise agent autonomy levels*

*This is a companion to [The Autonomy Tax](./article_draft_v6A.md). You can follow this guide independently, but the essay provides the full thesis, evidence, and anti-thesis behind the framework.*

---

## Why This Exists

Enterprise agent ROI is constrained less by model capability and more by three hidden costs — the **Autonomy Tax**:

> **Net Agent Value = Throughput Gain − Human Bandwidth Tax − Incident Tax − Governance Tax**

The **Human Bandwidth Tax** is the expert review burden that grows as AI amplifies junior output. The **Incident Tax** is the financial and reputational damage from uncontrolled agent actions. The **Governance Tax** is the compliance, observability, and audit overhead that almost nobody measures — and that emerges as the dominant tax in [the coded evidence](./sources/derived/autonomy_tax_casebook.tsv).

These taxes compound as autonomy increases. This guide helps you **score specific workflows against all three taxes, decide the right autonomy level, and calibrate the heuristic to your domain.**

---

## Autonomy Levels: The Full Taxonomy

This taxonomy is consistent with both [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) and [OpenAI](https://developers.openai.com/tracks/building-agents/) published framework guidance and calibrated against the MAP study's production data [[Pan et al. 2026](https://arxiv.org/abs/2512.04123), preprint, n=306].

| Level | Architecture | What AI controls | What's hardcoded / human-owned | Review gate | Tax profile |
|---|---|---|---|---|---|
| **1 — Copilot** | Single LLM call + tools | Response content | Everything else | N/A (human executes) | Minimal |
| **2 — Pipeline** | Linear chain of single-turn LLM calls | Each step's reasoning | Pipeline sequence, routing, tool access | Human reviews outputs before external action | Moderate HB Tax; low Incident Tax |
| **2.5 — Artifact pipeline** | Linear chain of multi-turn ReAct agents | Each node's reasoning, tool use, and iteration across multiple turns | Pipeline sequence, routing; each node's I/O contract | Human review at predetermined decision points | Moderate and predictable across all three taxes |
| **3 — Autonomous** | Dynamic graph or policy engine | Routing between agents, task planning, external actions | Available tools, safety constraints | Policy engine only; outputs reach external systems directly | All three taxes fully active, scaling with action surface |
| **4 — Fully autonomous** | Decentralized / event-driven (actor model) | Agent spawning, inter-agent communication, emergent coordination | Almost nothing | None | Maximum on all axes; no known enterprise production deployment as of early 2026 |

**The Level 2 → 2.5 distinction matters for tax exposure.** In a Level 2 pipeline, each node makes a single LLM call — the blast radius is small and the output is easy to review. In a Level 2.5 pipeline, each node runs a multi-turn ReAct loop with tool access, producing richer outputs with a larger action surface per step. The control comes from two architectural constraints: the pipeline sequence is fixed and deterministic, and each node reads a defined structured input and produces a defined structured output. Human review gates sit at predetermined decision points rather than on every output.

---

## The Decision Flow

Follow these steps in order. Do not skip the circuit breaker.

### Step 1 — Score each tax

Use the scoring rubric below. Score Benefit and each of the three taxes on a 1–5 scale.

### Step 2 — Circuit breaker

**If any single tax scores ≥ 4, the workflow is BLOCKED.** It cannot move to autonomous operation until you have a documented mitigation plan that reduces that tax below 4. This is the primary safety mechanism, not a footnote.

### Step 3 — Net score

For non-blocked workflows only:

```
Net = Benefit − Average(HB Tax, Incident Tax, Governance Tax)
```

Use `Net` for ranking candidate workflows. A higher Net means higher priority for pilot.

### Step 4 — Level decision

- **Level 3** is allowed only when `Net > 0` **and** both `Incident Tax ≤ 2` **and** `Governance Tax ≤ 2`.
- Otherwise, default to **Level 2.5** (pipeline with human gates at decision points).
- If manual approval is required at every external action, use **Level 2**.

---

## Scoring Rubric

Use these anchors to calibrate scores consistently across teams. This is a structured decision-making heuristic, not a predictive model — the value is in forcing explicit estimation of each tax rather than hand-waving about "AI readiness."

| Score | Human Bandwidth Tax | Incident Tax | Governance Tax |
|---|---|---|---|
| **1** | No expert review needed; output is internal/low-stakes | Errors are invisible or cost < $1 to fix | No regulatory exposure; internal use only |
| **2** | Light review; seniors spot-check < 10% of outputs | Errors cost $1–$50; easily reversible | Minimal compliance; standard data handling |
| **3** | Moderate review; seniors review 10–50% of outputs | Errors cost $50–$500; partially recoverable | Moderate compliance; PII or financial data involved |
| **4** | Heavy review; seniors review > 50% of outputs | Errors cost $500–$5,000 or reputational damage | Regulated domain; audit trail required |
| **5** | Every output requires expert validation before use | Errors cost > $5,000 or legal/regulatory exposure | Heavily regulated; SOC 2/AI Act obligations apply |

The full scoring anchors are also available as a standalone reference: [Autonomy Tax Scorecard Rubric](./assets/autonomy_tax_scorecard_rubric.md).

---

## Tax Sensitivity by Error Cost

Use this table as a quick-reference for how error economics should drive your autonomy-level decision:

| Error cost per incident | Incident Tax weight | Expert review pool | Implied max autonomy | Rationale |
|---|---|---|---|---|
| **Low** (< $10, reversible) | 1–2 | Any | Level 3 viable | Error cost < review cost at volume; automation wins on pure economics |
| **Medium** ($10–$500, partially recoverable) | 3 | Adequate | Level 2.5 with monitoring | Human gates at key decision points keep expected loss bounded |
| **High** (> $500 or reputational/regulatory) | 4–5 | Scarce or expensive | Level 2 or Level 2.5 with gates | Single-incident cost can exceed cumulative throughput savings |

**When conditions conflict, error cost should dominate.** A workflow with high task variance but high error cost is a Level 2.5 problem, not a Level 3 opportunity.

---

## Worked Examples

### Example 1: Support Refund Triage (Pass → Level 2.5)

A customer ops team processes ~10,000 support refund requests daily. Each follows clear policy rules. Errors typically cost $5–$50 and are reversible within 24 hours. The team has adequate senior staff for spot-checking.

| Dimension | Score | Rationale |
|---|---|---|
| Benefit | 4 | High volume, repetitive, clear rules |
| HB Tax | 3 | Moderate review — seniors spot-check escalations and edge cases |
| Incident Tax | 2 | Errors cost $1–$50; easily reversible within 24 hours |
| Governance Tax | 2 | Standard data handling; no regulated domain exposure |
| **Circuit Breaker** | ✅ Pass | No tax ≥ 4 |
| **Net Score** | +1.67 | 4 − Average(3, 2, 2) = 4 − 2.33 |
| **Level Decision** | Level 2.5 | Net positive, but HB Tax = 3 (> 2), so Level 3 gate not met |

**Implication:** Deploy as an artifact pipeline with human gates at escalation decision points. Seniors review flagged cases, not every output.

### Example 2: Procurement Approval (Blocked → Requires Mitigation)

A finance ops team wants to automate vendor invoice approval. Volume is ~500/day, but error cost per incident is high ($5,000+) and recovery windows are long (7+ days). The domain is regulated, audit trails are required, and existing logging doesn't capture agent reasoning.

| Dimension | Score | Rationale |
|---|---|---|
| Benefit | 5 | Massive time savings if accurate; high analyst hours currently |
| HB Tax | 4 | Every approval needs expert validation before release |
| Incident Tax | 5 | A single wrong $5,000 approval wipes out savings from 1,000 correct ones |
| Governance Tax | 4 | Regulated domain; SOC 2 compliance; no agent audit trail exists |
| **Circuit Breaker** | 🛑 BLOCKED | HB Tax = 4, Incident Tax = 5, Governance Tax = 4 |
| **Net Score** | — | Not calculated; workflow is blocked |
| **Level Decision** | Blocked | Requires mitigation plan for all three taxes before any autonomous pilot |

**Mitigation path before re-scoring:**
1. **HB Tax:** Implement tiered review — auto-approve invoices < $100 matching existing vendor contracts, flag everything else for human review. Re-score HB Tax: target 2–3.
2. **Incident Tax:** Add per-vendor daily spend limits, real-time velocity detection, and mandatory 24-hour hold on new vendor approvals. Re-score Incident Tax: target 3.
3. **Governance Tax:** Instrument the pipeline with full trace logging and token accounting. Create audit-ready decision logs for each approval. Re-score Governance Tax: target 3.

After mitigation, re-run the scorecard. If all taxes < 4 and Net > 0, the workflow can proceed at Level 2.5 with heavy gating.

Use the [scorecard template CSV](./assets/autonomy_tax_scorecard_template.csv) to score your own workflows.

---

## How to Calibrate the Heuristic

The thresholds in this scorecard are order-of-magnitude starting points, not empirically fitted cutoffs. Here's how they were set and how to tune them.

**Baseline from the casebook.** We coded [28 public records](./sources/derived/autonomy_tax_casebook.tsv) — incidents, field studies, regulatory milestones, and tooling baselines — into a normalized schema with source-tier and confidence ratings. Of those, 21 directly support the tax model. The distribution of primary tax across those records:

| Primary tax | Count | Share |
|---|---|---|
| Governance Tax | 12 | 57% |
| Human Bandwidth Tax | 4 | 19% |
| Incident Tax | 4 | 19% |
| Throughput Gain (positive signal) | 1 | 5% |

Governance is the dominant tax in the coded evidence. This informs the circuit breaker design: governance failures are the most common and least visible, so a high governance score should block deployment even when the other taxes look manageable.

**How to tune for your domain:**
- **Adjust Incident Tax breakpoints by your error cost distribution.** If your median error cost is $200, the 3→4 boundary at $500 may be too generous. Lower it.
- **Adjust Governance Tax by your regulatory exposure.** In healthcare or financial services, a score of 3 (moderate compliance) may already represent significant audit risk. Treat your industry's baseline as the scoring floor.
- **Adjust HB Tax by your review pool depth.** If you have 2 seniors reviewing for 20 juniors, a score of 3 (10–50% review) may already be throttling your experts. If you have 10 seniors for 20 juniors, the same review rate is sustainable.

Coding criteria and method notes are documented in [autonomy_tax_casebook_method.md](./sources/derived/autonomy_tax_casebook_method.md).

---

## Implementation Checklist

These are sprint-level execution steps, not aspirational goals.

**Sprint 1: Measure**
- [ ] Identify your top three candidate workflows for agent autonomy
- [ ] Score each workflow using the rubric above
- [ ] Apply circuit breaker — flag any workflow with a tax score ≥ 4
- [ ] Calculate Net Score for non-blocked workflows
- [ ] Rank candidates by Net Score

**Sprint 2: Instrument**
- [ ] Add four counters to your most critical agent-facing API: retry rate, external-action rate, human-escalation rate, review-time-per-output
- [ ] Set up observability: OpenTelemetry GenAI semantic conventions if your stack supports them
- [ ] Establish a baseline dashboard for the top-ranked workflow

**Sprint 3: Validate**
- [ ] Ask senior engineers to log time spent reviewing/correcting/reverting AI outputs for one sprint
- [ ] Calculate: what percentage of senior engineering time is going to AI output validation?
- [ ] Re-score your top workflow with observed data instead of estimates
- [ ] Compare estimated vs. observed scores — calibrate your rubric accordingly

---

## Appendix: Method, Sources, and Limitations

### Source Classification

This framework draws from 81 collected sources classified into five tiers:

| Tier | Description | Examples used | Confidence |
|---|---|---|---|
| **1** | Peer-reviewed, major institutions, government data | NBER w31161, EU AI Act text, NVD CVE database | High |
| **2** | Major consulting firms, large-sample industry surveys | Deloitte 2026, McKinsey 2025 | Medium-high; note potential respondent bias |
| **3** | Preprints, working papers, conference presentations | MAP study, Xu et al., Song et al., METR, Agents of Chaos | Medium; findings not yet peer-reviewed |
| **4** | Vendor publications, product documentation, self-reported metrics | Anthropic, Klarna, Proxy, pricing pages | Use with explicit caveats; vendor incentive bias |
| **5** | Frameworks, standards, guidelines | NIST AI RMF, OWASP Top 10, OpenTelemetry | Reference material; not evidence claims |

### Key Limitations

- **No original data, one original synthesis.** Every empirical claim cites published research. The originality contribution is the framework and the [Autonomy Tax Casebook](./sources/derived/autonomy_tax_casebook.tsv), which codes 28 public records into a normalized schema. Method notes: [autonomy_tax_casebook_method.md](./sources/derived/autonomy_tax_casebook_method.md).
- **Domain bridging.** The Human Bandwidth Tax thesis bridges findings from customer support (NBER), enterprise development (Xu et al.), and open-source projects (Song et al.). The common mechanism is plausible but not directly demonstrated in a single study.
- **Governance Tax measurement gap.** No published study quantifies per-agent governance cost. Track governance-hours per workflow per month to convert this into a measurable cost line item.
- **Geographic scope.** US/EU regulatory and market conditions. Self-hosted and open-weight deployments carry different tax structures.
- **Temporal snapshot.** Source data captured February 2026. Pricing, regulatory status, and capability benchmarks will shift.

### Tax Subcomponents (Extended)

For teams that want finer-grained analysis:

| Tax | Subcomponents |
|---|---|
| Human Bandwidth Tax | Expert review time, rework rate, coordination overhead, quality-gate throughput |
| Incident Tax | Direct financial loss, remediation cost, reputational damage, investigation time |
| Governance Tax | Compliance staff, audit tooling, observability infrastructure, regulatory reporting |

All sources with URLs, DOIs, and access dates are available in the [source manifest](./sources/source_manifest.tsv).
