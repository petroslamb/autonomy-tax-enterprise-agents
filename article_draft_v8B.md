# The Autonomy Tax Scorecard: A Practitioner's Guide

*The decision framework and scoring workflow for enterprise agent autonomy levels*

*This is a companion to [The Autonomy Tax](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/article_draft_v8A.md). You can follow this guide independently, but the essay provides the full thesis, evidence, and anti-thesis behind the framework.*

*Open-source materials for this guide (casebook, rubric, templates, and sources) are available in the [GitHub repository](https://github.com/petroslamb/autonomy-tax-enterprise-agents).*

---

## Why This Exists

Your team is about to deploy an agent workflow. Before you do, run it through this framework, it takes 15 minutes and will tell you whether you need human gates, a circuit breaker, or a full mitigation plan. The scoring system below is based on three hidden costs, the **Autonomy Tax**, that compound as autonomy increases:

> **Net = Benefit − Average(HB Tax, Incident Tax, Governance Tax)**

Score first, deploy second. If any single tax scores ≥ 4, deployment is **blocked** until mitigation is documented and the workflow re-scored. This is the primary safety mechanism, not a footnote.

---

## Autonomy Levels: Quick Reference

This taxonomy synthesizes Anthropic and OpenAI published guidance, cross-checked against production deployment data.[[^taxonomy]]

| Level | Architecture | What AI controls | What's hardcoded / human-owned | Review gate |
|---|---|---|---|---|
| **1 Copilot** | Single LLM call + tools | Response content | Everything else | N/A (human executes) |
| **2 Pipeline** | Linear chain of single-turn LLM calls | Each step's reasoning | Pipeline sequence, routing, tool access | Human reviews outputs before external action |
| **2.5 Artifact Pipeline** | Linear chain of multi-turn ReAct agents | Each node's reasoning, tool use, and iteration | Pipeline sequence; each node's I/O contract | Human review at predetermined decision points |
| **Bounded 3** | Dynamic graph or policy engine | Routing, task planning, external actions | Hard gates, policy nodes, escalation constraints | Policy engine + mandatory compliance gates |
| **4 Fully autonomous** | Decentralized actor model | Agent spawning, coordination | Almost nothing | None |

**The Level 2 → 2.5 distinction matters.** In a Level 2 pipeline, each node makes a single LLM call, small blast radius, easy to review. In Level 2.5, each node runs a multi-turn ReAct loop with tool access, but the pipeline sequence is fixed and each node's inputs/outputs are typed contracts. Human review gates sit at predetermined decision points rather than on every output. Level 2.5 is not a compromise, it is how enterprises buy capability without buying chaos. Bounded Level 3 adds dynamic routing, but only inside mandatory compliance and escalation constraints that cannot be bypassed.

This layering matches the workflow-first guidance from Anthropic and OpenAI: most use cases should start with simpler bounded workflows and earn autonomy with evidence.[[^anthropic_build]][[^openai_build]]

---

## The Decision Flow

Follow these steps in order. Do not skip the circuit breaker.

**Step 1 Score each tax.** Use the scoring rubric below. Score Benefit and each of the three taxes on a 1–5 scale.

**Step 2 Circuit breaker.** If any single tax scores ≥ 4, the workflow is BLOCKED. It cannot move to autonomous operation until you have a documented mitigation plan that reduces that tax below 4.

**Step 3 Net score.** For non-blocked workflows only: `Net = Benefit − Average(HB Tax, Incident Tax, Governance Tax)`. Use Net for ranking candidate workflows, higher Net means higher priority for pilot.

**Step 4 Level decision.** Bounded Level 3 is allowed only when `Net > 0` **and** all three taxes `≤ 2`. Otherwise, default to Level 2.5 with human gates at decision points. If manual approval is required at every external action, use Level 2.

**Step 5 Re-score after mitigation.** Every blocked workflow needs explicit mitigation work, then a full re-score. No workflow graduates by narrative argument.

---

## Scoring Rubric

Use these anchors to calibrate scores consistently across teams. This is a structured decision-making heuristic, not a predictive model, the value is in forcing explicit estimation of each tax rather than hand-waving about "AI readiness."

| Score | Human Bandwidth Tax | Incident Tax | Governance Tax |
|---|---|---|---|
| **1** | No expert review needed; output is internal/low-stakes | Errors are invisible or cost < $1 to fix | No regulatory exposure; internal use only |
| **2** | Light review; seniors spot-check < 10% of outputs | Errors cost $1–$50; easily reversible | Minimal compliance; standard data handling |
| **3** | Moderate review; seniors review 10–50% of outputs | Errors cost $50–$500; partially recoverable | Moderate compliance; PII or financial data involved |
| **4** | Heavy review; seniors review > 50% of outputs | Errors cost $500–$5,000 or reputational damage | Regulated domain; audit trail required |
| **5** | Every output requires expert validation before use | Errors cost > $5,000 or legal/regulatory exposure | Heavily regulated; SOC 2/AI Act obligations apply |

The full scoring anchors are also available as a standalone reference: [Autonomy Tax Scorecard Rubric](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/assets/autonomy_tax_scorecard_rubric.md).

---

## Tax Sensitivity by Error Cost

When conditions conflict, error cost should dominate. This table shows how error economics drive the autonomy-level decision:

| Error cost per incident | Incident Tax weight | Implied max autonomy | Rationale |
|---|---|---|---|
| **Low** (< $10, reversible) | 1–2 | Bounded Level 3 viable | Error cost < review cost at volume; automation wins on pure economics |
| **Medium** ($10–$500, partially recoverable) | 3 | Level 2.5 with monitoring | Human gates at key decision points keep expected loss bounded |
| **High** (> $500 or reputational/regulatory) | 4–5 | Level 2 or Level 2.5 with gates | Single-incident cost can exceed cumulative throughput savings |

A workflow with high task variance but high error cost is a Level 2.5 problem, not a Bounded Level 3 opportunity.

---

## Worked Examples

### Example 1: Support Refund Triage (Pass → Level 2.5)

A customer ops team processes ~10,000 support refund requests daily. Each follows clear policy rules. Errors typically cost $5–$50 and are reversible within 24 hours. The team has adequate senior staff for spot-checking.

| Dimension | Score | Rationale |
|---|---|---|
| Benefit | 4 | High volume, repetitive, clear rules |
| HB Tax | 3 | Moderate review, seniors spot-check escalations and edge cases |
| Incident Tax | 2 | Errors cost $1–$50; easily reversible within 24 hours |
| Governance Tax | 2 | Standard data handling; no regulated domain exposure |
| **Circuit Breaker** | ✅ Pass | No tax ≥ 4 |
| **Net Score** | +1.67 | 4 − Average(3, 2, 2) = 4 − 2.33 |
| **Level Decision** | Level 2.5 | Net positive, but HB Tax = 3 (> 2), so Bounded Level 3 gate not met |

**Implication:** Deploy as an Artifact Pipeline with human gates at escalation decision points. Seniors review flagged cases, not every output.

### Example 2: Procurement Approval (Blocked → Requires Mitigation)

A finance ops team wants to automate vendor invoice approval. Volume is ~500/day, but error cost per incident is high ($5,000+) and recovery windows are long (7+ days). The domain is regulated, audit trails are required, and existing logging doesn't capture agent reasoning.

| Dimension | Score | Rationale |
|---|---|---|
| Benefit | 5 | Massive time savings if accurate; high analyst hours currently |
| HB Tax | 4 | Every approval needs expert validation before release |
| Incident Tax | 5 | A single wrong $5,000 approval wipes out savings from 1,000 correct ones |
| Governance Tax | 4 | Regulated domain; SOC 2 compliance; no agent audit trail exists |
| **Circuit Breaker** | 🛑 BLOCKED | HB Tax = 4, Incident Tax = 5, Governance Tax = 4 |
| **Net Score** |, | Not calculated; workflow is blocked |
| **Level Decision** | Blocked | Requires mitigation plan for all three taxes before any autonomous pilot |

**Mitigation path before re-scoring:** First, reduce the HB Tax by implementing tiered review, auto-approve invoices < $100 matching existing vendor contracts, flag everything else for human review (target HB Tax: 2–3). Second, reduce the Incident Tax by adding per-vendor daily spend limits, real-time velocity detection, and mandatory 24-hour holds on new vendor approvals (target: 3). Third, reduce the Governance Tax by instrumenting the pipeline with full trace logging, token accounting, and audit-ready decision logs for each approval (target: 3). After mitigation, re-run the scorecard. If all taxes < 4 and Net > 0, the workflow can proceed at Level 2.5 with heavy gating.

Use the [scorecard template CSV](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/assets/autonomy_tax_scorecard_template.csv) to score your own workflows.

---

## Reflection vs Critique: Know the Difference

These are not interchangeable controls and conflating them is a common design error.

**Reflection** is a same-node (or same-role) self-review loop. It is fast, cheap, and effective for formatting, schema compliance, and consistency defects. Use it when the failure mode is quality of expression, wrong format, missed field, inconsistent output, and stakes are low-to-medium. Reflection fixes formatting errors.

**Critique** is an independent reviewer role that challenges output before a risky transition. It is slower, more expensive, and required for high-impact decisions where you need adversarial challenge and explicit rejection authority. Use it when consequences are high, financial, legal, security, or compliance decisions, and you need a genuine second opinion, not a cosmetic pass. Critique catches decision errors.

The operator rule: if consequences are high, reflection-only pipelines are under-controlled. If you wouldn't ship a financial report without a second pair of eyes, don't ship a financial agent output without a critique node.

---

## Incident RCA Template

When an agent incident crosses your severity threshold, don't accept "we updated the prompt" as a corrective action. Use this three-factor structure to force a proper root-cause analysis.[[^incident]]

**System factors:** Which policy checks failed, were absent, or were bypassed? Which hard constraints should have blocked the action? Which control node or state transition was missing?

**Context factors:** What environment, data quality, or upstream dependency conditions triggered the failure? Was context stale, incomplete, or contradictory? Which external API or tool behavior contributed?

**Cognitive factors:** Did the agent's decomposition or routing choice increase risk? Did reflection loops mask defects instead of surfacing them? Were outputs over-trusted due to confidence language?

Every incident record should include: trace ID and workflow ID, input and output artifact versions, tool call sequence and timestamps, policy evaluation log, human intervention points, financial and operational impact estimate, and mitigation owner with a deadline. This structure prevents shallow postmortems and maps directly to current incident-analysis work for AI agents.[[^incident]]

---

## How to Calibrate the Heuristic

The thresholds in this scorecard are order-of-magnitude starting points, not empirically fitted cutoffs. Here's how they were set and how to tune them.

**Baseline from the casebook.** We coded [28 public records](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/sources/derived/autonomy_tax_casebook.tsv), incidents, field studies, regulatory milestones, and tooling baselines, into a normalized schema with source-tier and confidence ratings. Of those, 21 directly support the tax model. The distribution: governance is the primary tax in 12 (57%), human bandwidth in 4 (19%), incident in 4 (19%). Governance is the dominant tax in the coded evidence, which is why a high governance score should block deployment even when the other taxes look manageable.[[^casebook]]

**How to tune for your domain:** Adjust Incident Tax breakpoints by your actual error cost distribution, if your median error cost is $200, the 3→4 boundary at $500 may be too generous. Adjust Governance Tax by your regulatory exposure, in healthcare or financial services, a score of 3 may already represent significant audit risk. Adjust HB Tax by your review pool depth, if you have 2 seniors reviewing for 20 juniors, a score of 3 may already be throttling your experts. Re-score monthly during rollout, not quarterly. Promote levels only with measured improvements, not confidence.

Coding criteria and method notes are documented in [autonomy_tax_casebook_method.md](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/sources/derived/autonomy_tax_casebook_method.md).

---

## Implementation Checklist

These are sprint-level execution steps, not aspirational goals.

**Sprint 1: Measure.** Identify your top three candidate workflows, start with workflows where you're already considering or piloting AI assistance and rank by monthly human-hours spent. Score each workflow using the rubric above. Apply the circuit breaker and flag any workflow with a tax score ≥ 4. Calculate Net Score for non-blocked workflows and rank candidates.

**Sprint 2: Instrument.** Add four counters to your most critical agent-facing API: retry rate, external-action rate, human-escalation rate, and review-time-per-output. Set up observability (OpenTelemetry GenAI semantic conventions if your stack supports them). Establish a baseline dashboard for the top-ranked workflow.

**Sprint 3: Validate.** Ask senior engineers to log time spent reviewing, correcting, or reverting AI outputs for one sprint. Calculate what percentage of senior engineering time goes to AI output validation. Re-score your top workflow with observed data instead of estimates. Compare estimated vs. observed scores and calibrate your rubric accordingly.

---

## Design Defaults for Level 2.5

The easiest way to lose control is to over-design before you stabilize behavior. These defaults align with production-grade workflow guidance[[^prodguide]] and represent the simplest architecture that supports real autonomy:

**Deterministic orchestration first.** Dynamic routing is earned, not default. Start with fixed-sequence pipelines. **Single responsibility per node.** Each node should produce one typed artifact, not a mixed-output bundle. **Typed handoff contracts.** No raw chat-history dumps between nodes, pass bounded artifacts only. **Tool minimization.** Grant each node the least authority needed for its task. **Pure-function preference.** Use deterministic validation and transform steps outside the model whenever feasible.

These defaults are why Level 2.5 scales in production. They also map directly to the Boring Stack Doctrine from the main essay: constrain routing, type the artifacts, gate external action.

---

## Optional Reference: Sources and Limitations

### Source classification

This framework draws from sources classified into five tiers: Tier 1 (peer-reviewed, major institutions, government data, e.g., NBER w31161, EU AI Act, NVD), Tier 2 (major consulting firms and large-sample surveys, e.g., Deloitte 2026), Tier 3 (preprints and working papers, e.g., MAP study, Xu et al., METR), Tier 4 (vendor publications and self-reported metrics, used with explicit caveats), and Tier 5 (frameworks and standards, reference material, not evidence claims).

### Key limitations

This is a structured heuristic, not a predictive model. Some core evidence is preprint and requires ongoing validation. Vendor-reported gains should be treated as directional unless independently audited. Governance labor remains under-measured in public datasets. The domain-bridging inference, that the expert-bottleneck dynamic from copilot studies intensifies at higher autonomy, is plausible but not directly demonstrated. Geographic scope is US/EU; self-hosted and open-weight deployments carry different structures.

All sources with URLs, DOIs, and access dates are available in the [source manifest](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/sources/source_manifest.tsv).

---

## Notes

[^taxonomy]: Synthesized from [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) and [OpenAI](https://developers.openai.com/tracks/building-agents/) published guidance, cross-checked against [Pan et al. 2026](https://arxiv.org/abs/2512.04123) (MAP study, n=306), and triangulated with [Wang et al. 2025](https://arxiv.org/abs/2508.02121) (AgentOps survey) and [Kasirzadeh & Gabriel 2025](https://arxiv.org/abs/2504.21848) (governance-oriented agent characterization).

[^anthropic_build]: Anthropic Engineering, [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents).

[^openai_build]: OpenAI Developers, [Building Agents](https://developers.openai.com/tracks/building-agents/).

[^prodguide]: *A Practical Guide for Designing, Developing, and Deploying Production-Grade Agentic AI Workflows* (preprint): [arXiv:2512.08769](https://arxiv.org/abs/2512.08769).

[^incident]: *Incident Analysis for AI Agents* (preprint): [arXiv:2508.14231](https://arxiv.org/abs/2508.14231).

[^casebook]: The [Autonomy Tax Casebook](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/sources/derived/autonomy_tax_casebook.tsv) codes 28 public records. Method notes: [autonomy_tax_casebook_method.md](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/sources/derived/autonomy_tax_casebook_method.md).
