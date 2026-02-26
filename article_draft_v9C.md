# The Agent Control Plane

*How Bounded Autonomy Works in Production*

The thesis of this series is that enterprise agent programs usually fail at the control surface before they fail at model intelligence. The flagship essay establishes the economics, and the scorecard provides workflow qualification rules. This companion describes the control-plane architecture that allows dynamic behavior without allowing unauthorized action.

The core principle is straightforward: dynamic routing without hard gates is stochastic privilege escalation. That statement is not rhetorical shorthand. If model-directed planning can reach external actuation states without deterministic policy enforcement, then every reasoning path includes a nontrivial chance of executing an action that the organization cannot justify, reconstruct, or contain under incident conditions.

Once baseline model quality is adequate, production failure probability is driven primarily by authority design, state integrity, trace continuity, and incident-closure discipline rather than by isolated prompt defects.[^map][^deloitte][^obs] Teams that optimize only model behavior can produce impressive demonstrations while still shipping brittle systems.

## Authority Boundaries and Non-Bypassable Gates

A production system needs a hard boundary between exploration and execution. Exploration includes planning, decomposition, retrieval, drafting, and local revision loops. Execution includes actions that mutate external state, move money, trigger customer-visible effects, or alter regulated records. Crossing that boundary should require deterministic gate evaluation implemented outside model text.

This boundary allows organizations to keep innovation velocity without giving away authority. Models can explore broad strategy space inside bounded zones, but execution privileges remain constrained by policy checks, approval state, and explicit budget conditions. The practical result is that a system can reason flexibly while still failing safely when policy predicates are unsatisfied.

Secure-by-design guidance from public-sector sources reinforces this design choice. Controls that protect high-impact actions are lifecycle requirements, not post-incident patches.[^ncsc][^cisa][^nist_adv] Organizations that postpone authority-boundary engineering are not buying speed; they are borrowing risk.

## State-Gated Routing for Bounded Level 3

Bounded Level 3 depends on state-gated routing. In this pattern, model components can propose route transitions, but deterministic gate predicates decide which transitions are legal for the current state. A node may request continuation, revision, escalation, or completion, yet external action remains blocked until policy and approval predicates evaluate true.

This design preserves useful autonomy while constraining high-cost failure paths. A node can take many reasoning turns and call tools to improve local decision quality, but confidence language cannot directly authorize action. Authorization must be earned through state checks that reference budget, policy, approval, and compliance context.

The distinction from Level 2.5 is architectural, not cosmetic. Level 2.5 controls complexity through fixed sequence and typed handoffs. Bounded Level 3 permits dynamic sequence but fixes policy authority and escalation invariants. Both can work in production, but each requires its own control discipline.

## Durability and Agent-State Persistence

Teams frequently treat durability and state persistence as one requirement and then discover incident scenarios where neither guarantee is complete. Orchestration durability means workflow execution survives process failure, retries safely, and preserves authoritative execution order. Agent-state persistence means reasoning artifacts, intermediate decisions, and memory context remain inspectable and versioned across steps.

A durable orchestrator without inspectable agent state can recover execution while obscuring why decisions were made. Persistent agent state without durable orchestration can preserve rationale fragments while losing idempotency and action-order guarantees. Either gap can turn a contained event into prolonged forensic reconstruction.

The control-plane contract should therefore separate ownership cleanly. Orchestration owns action semantics, retry policy, and compensation behavior. Agent-state systems own memory boundaries, artifact lineage, and auditability of reasoning-to-action transitions. Clear ownership reduces ambiguity during incident response and prevents cross-team accountability collapse.

## Trace Continuity as an Operations Contract

Agent observability is not defined by the number of dashboards; it is defined by reconstructability under time pressure. For any external action, operators should be able to recover a connected path linking workflow identity, model outputs, tool calls, policy evaluations, approval events, and resulting state changes. If that chain cannot be reconstructed quickly, governance overhead rises immediately.

Trace continuity requires shared identifiers and consistent event semantics across orchestration, model, tool, and policy layers. OpenTelemetry GenAI semantic conventions are useful because they reduce schema drift and make cross-layer joins feasible during live incidents rather than only during retrospective analysis.[^otel]

In multi-team organizations, this is also an interface contract. AI teams must emit interpretable state transitions and artifact identifiers, while platform teams must preserve and query those records under production load. Without that division of responsibility, incident reviews devolve into component-level blame rather than system-level correction.

## Incident Closure and Requalification

Detection is only the beginning of incident handling. A complete closure loop requires analysis, mitigation, and requalification before autonomy scope is restored. Analysis should classify system factors, context factors, and cognitive factors so corrective work targets control mechanisms rather than superficial narrative labels.[^incident]

Mitigation should be proportional to failure mechanism. If failure involved policy bypass, privilege drift, or missing lineage, corrective action must change gate logic, authority boundaries, or trace guarantees, not only prompt wording. Closure should include accountable owners, measurable criteria, and recurrence-focused acceptance conditions.

Requalification connects incident learning back to governance. Workflows should be rescored after significant incidents, and autonomy should expand only after an operating cycle demonstrates stable behavior under revised controls. Without requalification, organizations institutionalize the same failure class under different labels.

## Prescriptive Controls Versus Tunable Controls

A practical control plane needs clarity on which rules are invariant and which can vary by domain. Invariant controls should not be negotiated per team because they protect catastrophic boundaries. Tunable controls should be adapted by domain economics and operational context because over-standardization can block useful deployment.

Circuit-breaker semantics, non-bypassable gates for high-impact actions, trace continuity, and incident-loop closure before re-expansion should be treated as prescriptive invariants. Loop budgets, approval thresholds by transaction class, critique coverage depth, and escalation timing can be tuned to domain-specific risk tolerance and staffing models.

| Control category | Typical examples | Governance stance |
|---|---|---|
| Prescriptive invariants | Circuit breaker, hard action gates, trace continuity, requalification after incidents | Do not relax without executive and risk-owner sign-off |
| Tunable parameters | Retry budgets, threshold amounts, escalation windows, critique sampling depth | Calibrate with observed data and domain risk profile |

This split prevents two opposite failure modes: rigid standardization that kills adoption, and ad hoc flexibility that destroys safety. Mature teams separate the two explicitly and review each with different cadence and ownership.

## Build-Versus-Buy Through the Lens of Control Ownership

Build-versus-buy decisions are often made on feature breadth and short-term delivery speed, but production outcomes depend more on control ownership boundaries. Buying orchestration, observability, or policy tooling can accelerate implementation, yet accountability for authority models, gate semantics, and incident response still remains internal.

The right question is not whether a vendor offers a feature. The right question is which control obligations must remain first-party to satisfy legal, security, and audit responsibilities. In many enterprises, policy logic, approval workflows, and retention guarantees are core governance assets that cannot be fully delegated without contractual and technical safeguards.

Integration cost should be priced at control-plane depth. A lower procurement price can become expensive when identity, policy, and incident workflows are forced into incompatible abstractions. Coherence of control architecture is a stronger long-term decision criterion than maximal feature count.

## Graduating Autonomy Across a Portfolio

Autonomy maturity should be managed as a portfolio lifecycle, not as a one-time architecture milestone. The reliable sequence starts with workflow qualification, moves through Level 2.5 stabilization with complete trace continuity, introduces narrow dynamic pilots under strict gates, and expands Bounded Level 3 scope only after measured stability.[^agentops][^prodguide]

This sequence is disciplined because failure modes shift by stage. Early-stage risk is usually governance immaturity and measurement blindness, while later-stage risk is control drift and policy debt accumulation across teams. Portfolio governance should therefore include periodic rescoring, incident trend review by failure class, and explicit tracking of control debt.

The objective of graduation is not to maximize autonomy labels. The objective is to increase authorized capability while preserving the ability to explain, constrain, and recover from behavior under adverse conditions.

## Closing

Bounded autonomy is not defined by how complex a routing graph can become. It is defined by whether the system can preserve authority boundaries, maintain durable and inspectable state, reconstruct decisions under pressure, and close incidents into stronger controls. Organizations that internalize this distinction can scale capability without normalizing hidden risk.

The practical test is immediate. If your team cannot explain why a specific external action was authorized, what state and policy conditions enabled it, and what changed after the last comparable incident, the system is not production-grade yet. It is partially automated variance with a deferred governance bill.

---

## Notes

[^map]: Pan et al. (2026), *Measuring Agents in Production* (preprint): [arXiv:2512.04123](https://arxiv.org/abs/2512.04123).

[^deloitte]: Deloitte (2026), *State of AI in the Enterprise*: [report](https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/services/consulting/2026/state-of-ai-2026.pdf).

[^obs]: Kasneci et al. (2025), *Beyond Black-Box Benchmarking*: [arXiv:2503.06745](https://arxiv.org/abs/2503.06745).

[^ncsc]: NCSC, [Guidelines for Secure AI System Development](https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf).

[^cisa]: CISA and partners, [Principles and Approaches for Security-by-Design and -Default](https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf).

[^nist_adv]: NIST AI 100-2e2023, [Adversarial ML Taxonomy and Terminology](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf).

[^otel]: OpenTelemetry GenAI semantic conventions: [documentation](https://opentelemetry.io/docs/specs/semconv/gen-ai/).

[^incident]: *Incident Analysis for AI Agents* (preprint): [arXiv:2508.14231](https://arxiv.org/abs/2508.14231).

[^agentops]: Wang et al. (2025), *A Survey on AgentOps* (preprint): [arXiv:2508.02121](https://arxiv.org/abs/2508.02121).

[^prodguide]: *A Practical Guide for Designing, Developing, and Deploying Production-Grade Agentic AI Workflows* (preprint): [arXiv:2512.08769](https://arxiv.org/abs/2512.08769).
