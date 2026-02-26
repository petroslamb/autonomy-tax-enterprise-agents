# The Agent Control Plane

*Bounded Autonomy in Production*

*Companion to [The Autonomy Tax](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/article_draft_v7A.md) and [The Autonomy Tax Scorecard](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/article_draft_v7B.md).* 

---

## What This Piece Does

`v7A` argues the thesis. `v7B` gives a scoring decision tool. This piece defines the architecture needed to run bounded autonomy without control collapse.

Core claim:

**Dynamic routing without hard gates is just stochastic privilege escalation.**

If you remember one design principle from this document, make it this:

**Bounded autonomy means the graph can explore, but it cannot bypass compliance nodes.**

---

## 1) Why Control-Plane Failures Dominate Rollout Failures

Most teams over-focus on model performance and under-specify runtime control behavior.

Current evidence is consistent with that failure mode:
- production deployments remain heavily bounded and human-evaluated[^map]
- organizations report major visibility and governance gaps[^deloitte][^akto]
- observability studies identify nondeterministic flows as a primary operational challenge[^obs]
- incident analyses show multi-factor failures that are rarely solved by prompt edits alone[^incident]

The operational implication is straightforward: after basic model quality is sufficient, failure probability is driven more by control-plane design than by base-model IQ.

Control plane, in this context, is the system that governs what an agent may do, how it is monitored, how it is interrupted, and how failures are reconstructed.

---

## 2) Operating Modes: Level 2.5 - Artifact Pipeline vs Bounded Level 3

### Level 2.5 - Artifact Pipeline
A fixed sequence of multi-turn, tool-using nodes with typed artifact contracts and predetermined human gates.

### Bounded Level 3
Dynamic routing and decomposition are allowed, but only inside hard constraints:
- mandatory policy gates
- escalation gates
- approval gates for high-risk action classes
- finite loop/failure budgets

### Why this distinction matters
Level 2.5 controls complexity at routing time. Bounded Level 3 controls complexity at policy time.

Both can be production-grade. Unbounded Level 3 is where most enterprise failures become expensive.

This layering is consistent with current engineering guidance: start with the simplest workflow that works, then add autonomy only where the task and controls justify it.[^anthropic_build][^openai_build][^prodguide]

---

## 3) State-Gated Routing Pattern (Canonical)

State-gated routing is the safest way to support dynamic behavior without surrendering control.

### Pattern definition
Routing decisions may be model-driven, but **termination and external action privileges are state-gated by deterministic policy checks**.

### Minimal rule set
- Any step can request `PROCEED`, `REVISE`, `ESCALATE`, or `FINISH`.
- `FINISH` is blocked unless required gate predicates are true.
- External actions are blocked unless policy and approval predicates are true.
- Loop counters and budget counters are hard-limited in code.

### Pseudocode shape
```text
if state.tax_score_max >= 4:
  route = ESCALATE
elif state.requires_approval and not state.approval_received:
  route = WAIT_HUMAN
elif state.required_checks_passed and state.output_contract_valid:
  route = FINISH
else:
  route = CONTINUE_OR_REVISE
```

This pattern creates bounded exploration: local autonomy is preserved, but destructive paths are structurally unavailable.

---

## 4) Dynamic Subgraph + Rigid Compliance Handoff

A practical enterprise architecture is to split the workflow into two zones:

1. **Dynamic subgraph (exploration zone)**
- planning, decomposition, drafting, reconciliation
- model-driven routing allowed
- tool access is scoped and auditable

2. **Rigid compliance handoff (execution zone)**
- deterministic validation and policy checks
- typed artifact verification
- approval/authorization enforcement
- external action execution only after gates pass

This separation solves a common false dichotomy: teams think they must choose either innovation velocity or control rigor. In practice, dynamic subgraphs give you velocity, and rigid handoffs give you reliability.

## 4.5) Control Invariants for Bounded Level 3

If you adopt dynamic routing, these invariants should remain fixed:

1. **Least-privilege tool access per node.** No broad long-lived credentials for routing agents.
2. **Input and output policy checks outside model prompts.** Guardrails that exist only in prompts are advisory, not enforceable controls.
3. **Policy-as-code for high-impact actions.** Approval and compliance conditions must be machine-verifiable predicates.
4. **Finite failure budgets.** Loop counts, retry windows, and spend/action budgets must hard-stop in code.
5. **Escalation as a first-class route.** Human escalation should be a normal state transition, not an exception path.

These requirements align with secure-by-design guidance and adversarial-ML risk framing: security controls must be engineered into the system lifecycle, not bolted on after behavior emerges.[^ncsc][^cisa][^nist_adv]

---

## 5) Durability Layering: Execution Durability vs Agent-State Persistence

Durability is not one feature. It is two separate requirements that teams often conflate.

### A) Orchestration durability
Purpose: survive worker restarts, retries, long waits, and async events.

### B) Agent-state persistence
Purpose: preserve step-level state, artifact lineage, and replay/debug context.

You need both for high-confidence operations:
- orchestration durability prevents workflow loss
- state persistence preserves explainability and forensic reconstruction

**Durability keeps execution alive; state persistence keeps reasoning inspectable.**

If you only implement A, you can resume jobs but may lose diagnostic clarity.
If you only implement B, you can inspect state but may fail under runtime disruption.

---

## 6) Observability Architecture: Trace Continuity, Not Dashboard Count

Most teams add logs and think observability is done. It is not.

For agent systems, the core requirement is **trace continuity across layers**:
- orchestrator events
- node-level model calls
- tool invocations
- policy decisions
- human approval events

OpenTelemetry semantic conventions for GenAI are useful because they provide a shared structure for spans and events across components.[^otel]

Practical rule:
- Every external action must be trace-linked to the upstream artifact and policy decision that authorized it.

Without this link, incident investigation becomes a manual reconstruction exercise, and governance cost spikes.

**Trace continuity is the contract between AI engineering and platform operations.**

### Trace-stitching pattern

Use one correlation key (trace/workflow identifier) across:
- orchestration spans
- model call spans
- tool execution spans
- policy/gate evaluations
- human approval events

If those records do not join cleanly, the system is observable in fragments, not observable as a control plane.

---

## 7) Reflection vs Critique as Separate Controls

Reflection and critique are different controls with different assurance levels.

### Reflection control
- same node (or same-role node) inspects and revises output
- fast and cheap
- good for schema/format/consistency defects

### Critique control
- independent reviewer role challenges output before risky transition
- slower and more expensive
- required for high-impact decisions

Control-plane rule:
- low-risk path: reflection may be sufficient
- high-risk path: critique is mandatory before policy gate advancement

Treating reflection as a substitute for critique is a category error in high-stakes pipelines.

---

## 8) Incident Loop Closure: Detect -> Analyze -> Mitigate -> Re-Score

A control plane is incomplete if it cannot absorb and learn from failure.

### Stage 1: Detect
- trigger on policy violations, anomaly thresholds, and severe output defects
- freeze downstream external actions when severity threshold is hit

### Stage 2: Analyze
Use a structured incident framework with three factor classes:[^incident]
- **System factors:** control/gate implementation failures
- **Context factors:** data/environment/tooling conditions
- **Cognitive factors:** decomposition/routing/reasoning misjudgments

### Stage 3: Mitigate
- implement technical and procedural fixes
- assign owners and deadlines
- define success criteria for each fix

### Stage 4: Re-score
- re-run workflow through autonomy scorecard
- only reopen higher-autonomy mode if score and gate criteria are satisfied

No incident should close with "updated prompt" as the only corrective action.

---

## 9) Build-vs-Buy Boundaries (Decision Criteria)

Avoid vendor-catalog thinking. Use capability criteria.

### Build in-house when
- requirement is core policy logic or risk posture differentiation
- data or control path sensitivity prohibits external dependency
- internal platform team can sustain ownership lifecycle

### Buy or adopt platform when
- capability is commodity but implementation cost is high (for example, robust trace UI, mature integration maintenance)
- speed-to-control matters more than bespoke optimization
- lock-in risk is acceptable relative to control gap risk

### Always retain internal ownership of
- policy definitions and gate criteria
- escalation logic and approval authority model
- incident severity taxonomy and closure standards

You can outsource tooling. You cannot outsource accountability.

---

## 10) Adoption Ladder (Pilot to Bounded Scale)

### Phase 0: Workflow qualification
- score top workflows
- eliminate high-tax candidates from early autonomy experiments

### Phase 1: Level 2.5 baseline
- fixed sequence, typed artifacts, explicit gates
- full trace continuity enabled

### Phase 2: Controlled dynamic pilots
- introduce bounded dynamic routing in a narrow scope
- enforce hard state-gated constraints and strict loop budgets

### Phase 3: Bounded Level 3 expansion
- extend only after stability metrics are sustained
- maintain gate invariants as non-negotiable controls

### Phase 4: Portfolio governance
- periodic re-scoring by domain
- incident trend analysis across workflows
- control debt backlog treated as first-class engineering debt

This ladder is intentionally conservative. The point is compounding reliability, not headline autonomy.

It also aligns with AgentOps lifecycle thinking: monitoring, anomaly detection, root-cause analysis, and iterative correction are continuous operational functions, not launch-phase tasks.[^agentops]

---

## Prescriptive vs Context-Dependent Rules

### Prescriptive (do not relax)
- Circuit breaker semantics for high-tax workflows
- Hard gating for external high-impact actions
- Trace continuity for all policy-authorized actions
- Structured incident loop closure before autonomy re-expansion

### Context-dependent (tune by domain)
- Exact loop budgets
- Approval thresholds by transaction class
- Reflection vs critique coverage ratios
- Escalation timing and on-call model

This split prevents one common failure mode: teams over-standardize where context matters and under-standardize where safety requires invariants.

---

## What This Means for Enterprise Architecture Reviews

When reviewing an agent system, stop asking first: "Which model?"

Ask first:
1. What are the non-bypassable gates?
2. How is state-gated routing enforced?
3. Can we reconstruct any external action from trace and artifact lineage?
4. What is our incident loop closure mechanism?
5. Which autonomy transitions are blocked by score until mitigation?

If these questions do not have clear answers, you do not have bounded autonomy. You have unmanaged variance.

---

## Closing

The core architecture move for 2026 is not maximal autonomy. It is controlled autonomy.

Level 2.5 - Artifact Pipeline remains the default for most high-value enterprise workflows. Bounded Level 3 is the right next step only when controls are mature enough to constrain dynamic behavior in real time.

Autonomy without control is a demo.

Control with measured autonomy is a production system.

---

## Notes

[^map]: Pan et al. (2026), *Measuring Agents in Production* (preprint): [arXiv:2512.04123](https://arxiv.org/abs/2512.04123).
[^deloitte]: Deloitte (2026), *State of AI in the Enterprise*: [PDF](https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/services/consulting/2026/state-of-ai-2026.pdf).
[^akto]: Akto (2025) enterprise visibility survey release: [PR Newswire](https://www.prnewswire.com/news-releases/aktos-2025-state-of-agentic-ai-security-report-finds-only-21-of-enterprises-have-visibility-302635105.html).
[^obs]: Kasneci et al. (2025), *Beyond Black-Box Benchmarking: Observability, Analytics, and Optimization of Agentic Systems*: [arXiv:2503.06745](https://arxiv.org/abs/2503.06745).
[^incident]: *Incident Analysis for AI Agents* (preprint): [arXiv:2508.14231](https://arxiv.org/abs/2508.14231).
[^otel]: OpenTelemetry GenAI semantic conventions: [https://opentelemetry.io/docs/specs/semconv/gen-ai/](https://opentelemetry.io/docs/specs/semconv/gen-ai/).
[^anthropic_build]: Anthropic Engineering, *Building Effective Agents*: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents).
[^openai_build]: OpenAI Developers, *Building Agents* track: [https://developers.openai.com/tracks/building-agents/](https://developers.openai.com/tracks/building-agents/).
[^prodguide]: *A Practical Guide for Designing, Developing, and Deploying Production-Grade Agentic AI Workflows* (preprint): [arXiv:2512.08769](https://arxiv.org/abs/2512.08769).
[^ncsc]: NCSC, *Guidelines for Secure AI System Development* (PDF): [https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf](https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf).
[^cisa]: CISA et al., *Security-by-Design and -Default* principles (PDF): [https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf](https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf).
[^nist_adv]: NIST AI 100-2e2023, *Adversarial ML Taxonomy and Terminology* (PDF): [https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf).
[^agentops]: Wang et al. (2025), *A Survey on AgentOps* (preprint): [arXiv:2508.02121](https://arxiv.org/abs/2508.02121).
