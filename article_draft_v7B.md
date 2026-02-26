# The Autonomy Tax Scorecard: Operator Guide

*How to choose Level 2.5 - Artifact Pipeline vs Bounded Level 3 for a real workflow*

*Companion to [The Autonomy Tax](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/article_draft_v7A.md).* 

---

## Why This Exists

Most teams make autonomy decisions in the wrong order.

They pick a framework, run a demo, then ask governance how to "add controls later."

This guide flips the sequence.

**Score first, deploy second.**

Use this when you need a decision fast:
- Should this workflow stay at Level 2?
- Is it a Level 2.5 - Artifact Pipeline candidate?
- Is it eligible for Bounded Level 3?
- Is it blocked until controls are built?

The method is simple:

> **Net = Benefit - Average(HB Tax, Incident Tax, Governance Tax)**

with one hard gate:

> **Circuit Breaker: if any tax >= 4, deployment is blocked.**

---

## Quick Taxonomy

| Level | Architecture | AI control surface | Non-negotiable control owner |
|---|---|---|---|
| **1 - Copilot** | Single call + optional tools | Content generation | Human executes action |
| **2 - Pipeline** | Fixed sequence, mostly single-turn nodes | Step-local reasoning | Humans and code own routing and external actions |
| **2.5 - Artifact Pipeline** | Fixed sequence, multi-turn tool-using nodes, typed artifact handoffs | Node-local planning/tool usage | Humans own gates; code owns sequence and contracts |
| **Bounded 3** | Dynamic routing allowed within hard policy graph | Routing, decomposition, delegated actions | Hard gates and policy nodes cannot be bypassed |

**Critical distinction:**
- Level 2.5 can be highly capable because each node is multi-turn and tool-using.
- It is still bounded because routing is fixed and artifacts are typed.
- Bounded Level 3 adds dynamic routing, but only inside mandatory compliance and escalation constraints.

This matches the workflow-first guidance from Anthropic and OpenAI: most use cases should start with simpler bounded workflows and earn autonomy with evidence.[^anthropic_build][^openai_build]

---

## Decision Flow (Use in Order)

### Step 1: Score the four dimensions
Assign 1-5 scores for:
- Benefit
- Human Bandwidth Tax
- Incident Tax
- Governance Tax

### Step 2: Apply circuit breaker
If any tax is 4 or 5, workflow is blocked.

Do not compute net score before mitigation.

### Step 3: Compute net for non-blocked workflows

`Net = Benefit - Average(HB Tax, Incident Tax, Governance Tax)`

Use net to rank candidates, not to bypass a high-risk tax.

### Step 4: Select autonomy level
- **Bounded Level 3** only if `Net > 0`, all taxes <= 2, and state-gated routing is enforced.
- **Level 2.5 - Artifact Pipeline** for most positive-net workflows with at least one tax at 3.
- **Level 2** if human approval is required for every external action.

### Step 5: Re-score after mitigation
Every blocked workflow needs explicit mitigation work, then a full re-score.

No workflow graduates by narrative argument.

---

## Scoring Rubric (1-5 Anchors)

| Score | Human Bandwidth Tax | Incident Tax | Governance Tax |
|---|---|---|---|
| **1** | No expert review required; low-stakes internal output | Errors cost <$1 and are trivially reversible | Minimal policy/compliance overhead |
| **2** | Spot-check review (<10%) | Errors cost $1-$50; easily reversible | Standard handling, limited audit burden |
| **3** | Senior review on 10-50% of outputs | Errors cost $50-$500 or partial recoverability | Material control and logging expectations |
| **4** | Senior review on >50% of outputs | Errors cost $500-$5,000, reputational or legal exposure | Regulated domain, auditability is required |
| **5** | Expert validation required for nearly every output | Errors >$5,000 or severe legal/regulatory impact | Heavy compliance obligations and continuous control evidence |

Use this rubric as a structured heuristic, not a statistical model. The purpose is decision discipline, not false precision.

---

## Sensitivity Table (Error Cost Dominates)

| Error cost profile | Typical Incident Tax | Default autonomy ceiling | Why |
|---|---|---|---|
| Low-cost, reversible | 1-2 | Bounded Level 3 possible | Review cost can exceed expected error cost at scale |
| Medium-cost, partly reversible | 3 | Level 2.5 | Human gates keep loss bounded |
| High-cost, low-reversibility, regulated | 4-5 | Level 2 or tightly gated 2.5 | One error can erase cumulative throughput gains |

If indicators conflict, let error cost and reversibility dominate the decision.

---

## Worked Example 1: Support Refund Triage

### Context
- Daily volume: ~10,000
- Typical error cost: $5-$50
- Reversibility: high (24-hour correction window)
- Data class: standard customer operations

### Scoring
| Dimension | Score | Rationale |
|---|---|---|
| Benefit | 4 | High repetitive volume and clear policies |
| HB Tax | 3 | Senior spot-check and escalation review still needed |
| Incident Tax | 2 | Bounded, reversible error economics |
| Governance Tax | 2 | Standard controls sufficient |
| Circuit Breaker | Pass | No tax >= 4 |
| Net | +1.67 | `4 - Average(3,2,2)` |
| Decision | Level 2.5 | Positive net, but HB Tax at 3 blocks Bounded 3 |

### Operator takeaway
Deploy as Level 2.5 - Artifact Pipeline with gates on payout authorization and policy exceptions.

---

## Worked Example 2: Procurement Approval

### Context
- Daily volume: ~500
- Typical error cost: $5,000+
- Reversibility: low (multi-day remediation)
- Data/control class: financial + audit-sensitive

### Scoring
| Dimension | Score | Rationale |
|---|---|---|
| Benefit | 5 | High analyst-hour savings potential |
| HB Tax | 4 | Expert validation needed on most approvals |
| Incident Tax | 5 | Single incorrect action can dominate monthly gains |
| Governance Tax | 4 | Audit trail and control evidence missing |
| Circuit Breaker | BLOCKED | Multiple taxes >= 4 |
| Net | Not computed | Blocked workflows do not proceed to net ranking |
| Decision | Blocked | Mitigation required before any autonomy expansion |

### Minimum mitigation before re-score
1. Add spend velocity detection and aggregate limit checks.
2. Enforce typed approval artifacts and explicit policy reasoning logs.
3. Introduce tiered human approval thresholds by amount/risk class.
4. Add mandatory audit-ready trace continuity for every external action.

---

## Design Defaults (Level 2.5 Execution)

The easiest way to lose control is to over-design before you stabilize behavior. Start with these defaults (aligned with production-grade workflow guidance):[^prodguide]

1. **Deterministic orchestration first.**
Dynamic routing is earned, not default.

2. **Single responsibility per node.**
Each node should produce one typed artifact, not a mixed-output bundle.

3. **Typed handoff contracts.**
No raw chat-history dumps between nodes. Pass bounded artifacts only.

4. **Tool minimization.**
Grant each node the least authority needed for its task.

5. **Pure-function preference where possible.**
Use deterministic validation/transform steps outside the model whenever feasible.

These defaults are why Level 2.5 scales in production.

### Boring Stack Pillars (Operator Mapping)

Use these pillars as a quick self-check before rollout:
- **Level 2.5 first:** default to fixed-sequence artifact pipelines unless data proves you need dynamic routing.
- **Observable by design:** treat trace continuity and policy logs as launch prerequisites, not phase-two tasks.
- **Cost bounded:** enforce loop, retry, and action-budget limits in code, not in prompt text.

---

## Incident RCA Mini-Template (Use After Any Material Failure)

Use this template for any incident above your team's severity threshold.

### A) System factors
- Which policy checks failed, were absent, or were bypassed?
- Which hard constraints should have blocked action?
- Which control node/state transition was missing?

### B) Context factors
- What environment, data quality, or upstream dependency conditions triggered failure?
- Was context stale, incomplete, or contradictory?
- Which external API/tool behavior contributed?

### C) Cognitive factors
- Did the agent's decomposition/routing choice increase risk?
- Did reflection loops mask defects instead of surfacing them?
- Were outputs over-trusted due to confidence language?

### Required evidence fields
- Trace ID and workflow ID
- Input artifact version and schema hash
- Output artifact version and schema hash
- Tool call sequence and timestamps
- Policy evaluation log
- Human intervention points
- Financial and operational impact estimate
- Mitigation owner and deadline

This structure maps directly to current incident-analysis work for AI agents and prevents shallow "prompt-fix" postmortems.[^incident_analysis]

---

## Reflection vs Critique: Operator Decision Rule

These are not interchangeable.

### Use reflection when
- Failure mode is formatting, consistency, or cheap correctness defects
- Stakes are low-to-medium
- Fast iterative cleanup is enough

### Use critique when
- Stakes are high (financial, security, legal, compliance)
- You need adversarial or independent challenge
- You need explicit rejection authority before external action

**Rule:** Reflection improves draft quality. Critique protects decision quality.

If consequences are high, reflection-only pipelines are under-controlled.

---

## Calibration: How to Tune This for Your Domain

Baseline from the casebook:
- 28 coded public records
- 21 records directly supporting the tax model
- Governance as primary tax in 12

This distribution is why governance has circuit-breaker parity with incident risk.[^casebook]

### Domain tuning checklist
1. Adjust Incident Tax boundaries to your real error-loss distribution.
2. Set Governance Tax floor to your regulatory baseline.
3. Adjust HB Tax by actual reviewer-to-producer ratio.
4. Re-score monthly during rollout, not quarterly.
5. Promote levels only with measured improvements, not confidence.

---

## 15-Minute Operating Runbook

1. Pick top three workflows by monthly human-hours.
2. Score all four dimensions for each workflow.
3. Apply circuit breaker.
4. Rank non-blocked candidates by net score.
5. Assign a level recommendation per workflow.
6. For blocked workflows, assign mitigation owner + target re-score date.
7. Schedule instrumentation if missing.
8. Re-run after first sprint of real telemetry.

Complete these eight steps and you have a defensible autonomy decision process.

Why this matters: observability is not cosmetic. In current research, nondeterministic flow behavior is one of the most widely reported operational pain points in agent systems, which is exactly why trace-first operations should be non-negotiable.[^obs79]

---

## Implementation Checklist by Lifecycle Stage

### Design
- [ ] Define workflow objective and explicit failure budget
- [ ] Set autonomy ceiling hypothesis (Level 2 / 2.5 / Bounded 3)
- [ ] Define typed artifact contracts and gate points

### Develop
- [ ] Implement least-privilege tool access per node
- [ ] Add circuit breakers and guardrails as code controls
- [ ] Add reflection/critique roles based on risk class

### Deploy
- [ ] Enable trace continuity and policy decision logs
- [ ] Define escalation paths and human approval thresholds
- [ ] Validate rollback/recovery pathways

### Operate
- [ ] Track HB, incident, and governance metrics continuously
- [ ] Run incident RCA template for severe failures
- [ ] Re-score workflows on observed data and adjust autonomy level

This lifecycle framing keeps security and governance as first-class engineering requirements, not documentation afterthoughts.[^ncsc][^cisa]

---

## Final Rule

No workflow graduates to higher autonomy without passing the circuit breaker, proving positive net on observed data, and sustaining control-layer reliability for at least one full operating cycle.

If you cannot reconstruct the decision path, you do not have production readiness.

---

## Optional Appendix / Reference

---

### Source confidence stack
- Tier 1: institutional/government/peer-reviewed anchors
- Tier 2: large industry surveys
- Tier 3: preprints and working papers
- Tier 4: vendor reports and pricing pages (explicit caveats)
- Tier 5: frameworks and standards (control scaffolding)

### Known limits of this framework
- It is a structured heuristic, not a predictive model.
- Some core evidence is preprint and requires ongoing validation.
- Vendor-reported gains should be treated as directional unless independently audited.
- Governance labor remains under-measured in public datasets.

### Practical artifact links
- Scorecard template: [autonomy_tax_scorecard_template.csv](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/assets/autonomy_tax_scorecard_template.csv)
- Rubric reference: [autonomy_tax_scorecard_rubric.md](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/assets/autonomy_tax_scorecard_rubric.md)
- Casebook dataset: [autonomy_tax_casebook.tsv](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/sources/derived/autonomy_tax_casebook.tsv)
- Casebook method: [autonomy_tax_casebook_method.md](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/sources/derived/autonomy_tax_casebook_method.md)

---

## Notes

[^anthropic_build]: Anthropic Engineering, *Building Effective Agents*: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents).
[^openai_build]: OpenAI Developers, *Building Agents* track: [https://developers.openai.com/tracks/building-agents/](https://developers.openai.com/tracks/building-agents/).
[^prodguide]: *A Practical Guide for Designing, Developing, and Deploying Production-Grade Agentic AI Workflows* (preprint): [arXiv:2512.08769](https://arxiv.org/abs/2512.08769).
[^incident_analysis]: *Incident Analysis for AI Agents* (preprint): [arXiv:2508.14231](https://arxiv.org/abs/2508.14231).
[^casebook]: Casebook synthesis artifact: [autonomy_tax_casebook.tsv](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/sources/derived/autonomy_tax_casebook.tsv).
[^obs79]: Kasneci et al. (2025), *Beyond Black-Box Benchmarking: Observability, Analytics, and Optimization of Agentic Systems*: [arXiv:2503.06745](https://arxiv.org/abs/2503.06745).
[^ncsc]: NCSC, *Guidelines for Secure AI System Development* (PDF): [https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf](https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf).
[^cisa]: CISA et al., *Security-by-Design and -Default* principles (PDF): [https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf](https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf).
