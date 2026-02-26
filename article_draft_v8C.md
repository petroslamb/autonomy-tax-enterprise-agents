# The Agent Control Plane: Five Questions Before You Ship

*Bounded Autonomy in Production*

*Companion to [The Autonomy Tax](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/article_draft_v8A.md) and [The Autonomy Tax Scorecard](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/article_draft_v8B.md).*

---

The main essay argues the thesis: enterprise agent ROI breaks at the control surface before it breaks at model intelligence. The scorecard tells you which workflows qualify and at what autonomy level. This piece answers the question that comes next: *how do you actually build and govern the control plane that makes bounded autonomy work?*

One design principle should govern everything that follows:

**Dynamic routing without hard gates is just stochastic privilege escalation.**

That line is not rhetoric, it is a literal description of what happens when you give an LLM routing authority without deterministic policy constraints. The agent explores a decision space, and somewhere in that space are actions with financial, legal, or reputational consequences. If no gate prevents the agent from reaching those actions, then every inference call is a probabilistic roll against your organization's risk surface. Bounded autonomy means the graph can explore, but it cannot bypass compliance nodes.

Most teams over-focus on model performance and under-specify runtime control behavior. Current evidence is consistent with that failure mode: production deployments remain heavily bounded and human-evaluated,[[^map]] organizations report major visibility and governance gaps,[[^deloitte]][[^akto]] observability studies identify nondeterministic flows as a primary operational challenge,[[^obs]] and incident analyses show multi-factor failures that are rarely solved by prompt edits alone.[[^incident]] After basic model quality is sufficient, failure probability is driven more by control-plane design than by base-model capability.

The rest of this piece is organized around five questions. If your architecture review cannot answer all five with specifics, you do not have bounded autonomy, you have unmanaged variance.

---

## Question 1: What Are the Non-Bypassable Gates?

This is the foundational question. Everything else depends on it.

A bounded system has two zones. The **exploration zone**, planning, decomposition, drafting, reconciliation, is where model-driven routing and tool use happen. The agent reasons, iterates, and produces drafts. The **execution zone**, deterministic validation, policy checks, typed artifact verification, approval enforcement, is where external actions are authorized. Transitions from exploration to execution pass through hard gates that code enforces, not gates that prompts suggest.

This separation solves a common false dichotomy. Teams think they must choose between innovation velocity and control rigor. In practice, dynamic subgraphs give you velocity, and rigid compliance handoffs give you reliability. You don't sacrifice one for the other, you put each in its zone.

The practical implication is a set of control invariants that should remain fixed regardless of how much autonomy you add. Least-privilege tool access per node: no broad, long-lived credentials for routing agents. Input and output policy checks outside model prompts: guardrails that exist only in prompts are advisory, not enforceable controls. Policy-as-code for high-impact actions: approval and compliance conditions must be machine-verifiable predicates, not natural-language instructions. Finite failure budgets: loop counts, retry windows, and spend/action budgets must hard-stop in code. And escalation as a first-class route: human escalation should be a normal state transition, not an exception path.

These requirements align with secure-by-design guidance, security controls must be engineered into the system lifecycle, not bolted on after behavior emerges.[[^ncsc]][[^cisa]][[^nist_adv]]

---

## Question 2: How Is Routing Controlled?

If you allow dynamic routing, and Bounded Level 3 does, you need the **state-gated routing pattern**. This is the safest way to support dynamic behavior without surrendering control.

The principle: routing decisions may be model-driven, but termination and external action privileges are state-gated by deterministic policy checks. Any step can request to proceed, revise, escalate, or finish. But "finish" is blocked unless required gate predicates are true. External actions are blocked unless policy and approval predicates are true. Loop counters and budget counters are hard-limited in code, not in prompt instructions.

The pattern creates bounded exploration: local autonomy is preserved within each node, but destructive paths are structurally unavailable. An agent can take ten reasoning steps to reach a conclusion, but it cannot execute a $5,000 purchase without passing through a deterministic approval gate that checks the current budget state, the vendor's daily velocity, and the human approval status. The model picks the route; the code decides what's allowed at the destination.

This is the architectural distinction between Level 2.5 and Bounded Level 3. In Level 2.5, routing is fixed at design time, the pipeline sequence is hardcoded, and each node operates within typed contracts. In Bounded Level 3, routing is dynamic at runtime, but the gates, budgets, and escalation paths are fixed. Level 2.5 controls complexity at routing time; Bounded Level 3 controls complexity at policy time. Both can be production-grade. Unbounded Level 3 is where most enterprise failures become expensive.

---

## Question 3: Can You Reconstruct Any External Action?

If you can't answer this question in under an hour for any given action your agent took last week, your observability is cosmetic. Most teams add logs and dashboards and think observability is done. For agent systems, the core requirement is **trace continuity across layers**, not visibility into any single component, but the ability to follow a causal chain from an external action back through the policy decision that authorized it, the artifact that informed it, the model calls that produced it, and the orchestration logic that routed it.

That means one correlation key (trace or workflow identifier) must stitch together orchestration spans, model call spans, tool execution spans, policy and gate evaluations, and human approval events. If those records do not join cleanly, the system is observable in fragments, not observable as a control plane. OpenTelemetry semantic conventions for GenAI provide a useful shared structure for spans and events across these layers.[[^otel]]

The practical rule is simple: every external action must be trace-linked to the upstream artifact and policy decision that authorized it. Without that link, incident investigation becomes a manual reconstruction exercise, pulling senior engineers into week-long forensic hunts, and governance cost spikes. This is where the Autonomy Tax compounds: a missing trace turns a $500 incident into a $50,000 investigation.

Trace continuity is the contract between AI engineering and platform operations. If your AI team ships an agent and your platform team can't debug it, you have an organizational failure masquerading as a technical gap.

---

## Question 4: What Happens When Something Fails?

A control plane is incomplete if it cannot absorb and learn from failure. The incident loop has four stages, and most teams only implement the first.

**Detect:** Trigger on policy violations, anomaly thresholds, and severe output defects. Freeze downstream external actions when severity threshold is hit. This is the part most teams have, alerting exists, even if it's crude.

**Analyze:** This is where most teams stop. "The agent hallucinated" is not a root cause. Use a structured framework with three factor classes:[[^incident]] system factors (which policy checks failed or were absent), context factors (what data, environment, or tool conditions triggered the failure), and cognitive factors (whether the agent's decomposition, routing, or self-evaluation increased risk). The three-factor structure prevents the most common failure of AI incident review: concluding that the fix is a better prompt.

**Mitigate:** Implement technical and procedural fixes with owners, deadlines, and explicit success criteria. No incident should close with "updated prompt" or "added instruction to system message" as the sole corrective action. If the failure was in the control layer, and the thesis of this series is that most failures are, the fix must be in the control layer.

**Re-score:** Run the workflow back through the Autonomy Tax Scorecard. If the incident revealed a tax that was underscored, adjust accordingly. Only reopen higher-autonomy mode if the updated score and gate criteria are satisfied after at least one full operating cycle of stability.

This loop is the mechanism that converts individual failures into system-level learning. Without it, the same categories of failure repeat, and each repetition compounds across all three taxes.

---

## Question 5: How Do You Graduate Between Autonomy Levels?

The adoption sequence matters because the failure modes are different at each stage, and teams that skip stages accumulate the wrong kind of risk.

**Start with workflow qualification.** Score your top candidate workflows using the scorecard. Eliminate high-tax candidates from early autonomy experiments, the goal of early adoption is learning, not heroics. If your first agent pilot is also your highest-risk workflow, you are optimizing for maximum drama, not maximum learning.

**Establish a Level 2.5 baseline.** Fixed-sequence pipelines with typed artifacts and explicit human gates. Full trace continuity enabled from day one, not added later, because retrofitting observability into a running agent system is three times harder than building it in. This phase validates that your team can operate a bounded agent pipeline reliably: that reviews happen at gates, traces are complete, and incident response works.

**Run controlled dynamic pilots.** Introduce dynamic routing in a narrow scope with hard state-gated constraints and strict loop budgets. This is where you learn whether your policy gates actually hold under model-driven routing, whether your failure budgets are correctly sized, and whether your escalation paths function under real load. Expect surprises. The purpose of this phase is to find the surprises cheaply.

**Expand Bounded Level 3 only after stability.** Extend dynamic routing only after stability metrics are sustained for at least one full operating cycle. Gate invariants remain non-negotiable controls, the gates don't relax as confidence grows. What changes is the scope of workflows that operate inside those gates.

**Maintain portfolio governance.** Periodic re-scoring by domain, incident trend analysis across workflows, and control debt treated as first-class engineering debt. This is the phase most organizations skip, and it's the phase that prevents the slow accumulation of risk that turns a healthy agent portfolio into a liability. AgentOps lifecycle thinking, monitoring, anomaly detection, root-cause analysis, and iterative correction, is a continuous operational function, not something you do at launch and then forget.[[^agentops]]

---

## Prescriptive vs Context-Dependent

Not everything in this framework should be uniformly applied. Some rules are safety invariants; others should be tuned to your domain. Conflating the two, over-standardizing where context matters, under-standardizing where safety requires invariants, is itself a common failure mode.

**Prescriptive (do not relax):** Circuit breaker semantics for high-tax workflows. Hard gating for external high-impact actions. Trace continuity for all policy-authorized actions. Structured incident loop closure before any autonomy re-expansion.

**Context-dependent (tune by domain):** Exact loop and failure budgets. Approval thresholds by transaction class. The balance between reflection and critique coverage. Escalation timing and on-call model.

The prescriptive rules protect you from catastrophic failure. The context-dependent rules let you ship efficiently. If you apply the prescriptive rules everywhere, you'll never ship. If you treat the prescriptive rules as context-dependent, you'll ship once, and then spend six months recovering.

---

## Closing

The core architecture move for 2026 is not maximal autonomy. It is controlled autonomy, and the difference is entirely in the control plane.

Five questions. If your architecture review can answer all five with specifics, non-bypassable gates, state-gated routing, trace-reconstructible actions, structured incident loops, and evidence-based graduation, you have a production system. If it can't, you have a demo with a deployment date.

Autonomy without control is a demo. Control with measured autonomy is a production system.

---

## Notes

[^map]: Pan et al. (2026), *Measuring Agents in Production* (preprint): [arXiv:2512.04123](https://arxiv.org/abs/2512.04123).

[^deloitte]: Deloitte (2026), *State of AI in the Enterprise*: [PDF](https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/services/consulting/2026/state-of-ai-2026.pdf).

[^akto]: Akto (2025) enterprise visibility survey: [PR Newswire](https://www.prnewswire.com/news-releases/aktos-2025-state-of-agentic-ai-security-report-finds-only-21-of-enterprises-have-visibility-302635105.html).

[^obs]: Kasneci et al. (2025), *Beyond Black-Box Benchmarking*: [arXiv:2503.06745](https://arxiv.org/abs/2503.06745).

[^incident]: *Incident Analysis for AI Agents* (preprint): [arXiv:2508.14231](https://arxiv.org/abs/2508.14231).

[^otel]: OpenTelemetry GenAI semantic conventions: [opentelemetry.io](https://opentelemetry.io/docs/specs/semconv/gen-ai/).

[^anthropic_build]: Anthropic Engineering, [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents).

[^openai_build]: OpenAI Developers, [Building Agents](https://developers.openai.com/tracks/building-agents/).

[^prodguide]: *A Practical Guide for Designing, Developing, and Deploying Production-Grade Agentic AI Workflows* (preprint): [arXiv:2512.08769](https://arxiv.org/abs/2512.08769).

[^ncsc]: NCSC, [Guidelines for Secure AI System Development](https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf).

[^cisa]: CISA et al., [Security-by-Design and -Default principles](https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf).

[^nist_adv]: NIST AI 100-2e2023, [Adversarial ML Taxonomy and Terminology](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf).

[^agentops]: Wang et al. (2025), *A Survey on AgentOps* (preprint): [arXiv:2508.02121](https://arxiv.org/abs/2508.02121).
