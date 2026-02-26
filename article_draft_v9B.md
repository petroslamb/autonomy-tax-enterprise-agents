# The Autonomy Tax Scorecard

*How to Qualify Workflows Before They Qualify You for Incidents*

This companion is designed to answer one operator question with minimal ambiguity: which workflows should run at which autonomy level this quarter, and which ones should be blocked until controls are real. The flagship essay explains why control-layer economics dominate enterprise outcomes. This guide converts that thesis into a repeatable qualification routine that teams can run during planning, rollout, and incident recovery.

The central failure mode this scorecard prevents is narrative override. Organizations often agree on principles, then bypass them under schedule pressure by treating risk scoring as advisory. The scorecard is deliberately strict because autonomy decisions are expensive to reverse once external actions, customer impact, and compliance obligations are already in motion.

## Decision Protocol

The protocol has to run in the same environment where deadlines, political pressure, and incomplete data are normal. It therefore emphasizes sequence and gating over theoretical elegance. Teams score benefit and the three taxes, apply a circuit breaker, compute Net only for non-blocked workflows, then decide autonomy level with explicit threshold rules.

The sequence below should be treated as operating law for deployment decisions. A team can debate score values, but it should not skip steps or reorder them, because reordering is how severe downside gets hidden behind optimistic benefit estimates.

| Step | Action | Required output | Failure mode if skipped |
|---|---|---|---|
| 1 | Score Benefit, Human Bandwidth, Incident, Governance (1-5) | Initial score sheet with rationale | Hidden assumptions remain implicit |
| 2 | Apply circuit breaker (`any tax >= 4`) | Block or proceed decision | High-severity workflows enter pilot |
| 3 | Compute Net for non-blocked workflows | Ranked candidate list | Teams prioritize by narrative, not economics |
| 4 | Assign autonomy level by threshold rules | Level decision with owner | Ambiguous governance and authority scope |
| 5 | Re-score after mitigation or incident | Updated score history | No learning loop, repeated failure classes |

The model formula is `Net = Benefit - Average(HB Tax, Incident Tax, Governance Tax)`. Net is a portfolio-ranking signal, not a license to ignore blocking risk. If a single tax is 4 or 5, the workflow stays blocked regardless of Net until mitigation changes the score.

## Scoring Anchors

Score quality depends on anchor consistency. Without common anchors, teams produce precise-looking numbers that are not comparable across workflows, which defeats portfolio governance. The anchor set below is intentionally practical and should be calibrated with observed incident and review data over time.

Human Bandwidth Tax captures expert review scarcity, Incident Tax captures downside concentration per failure event, and Governance Tax captures the lift required to satisfy policy, audit, and response obligations. Operators should score against expected operating conditions, not against best-case demos.

| Score | Human Bandwidth Tax | Incident Tax | Governance Tax |
|---|---|---|---|
| 1 | Minimal expert review, mostly auto-checkable outputs | Errors are cheap and easily reversible | Existing controls already satisfy audit and policy needs |
| 2 | Light expert sampling | Errors are low-cost with low operational effort to recover | Minor instrumentation or policy updates required |
| 3 | Recurring expert review and exception handling | Errors can cause material cost or service degradation | New approvals, logging, or review workflows required |
| 4 | Expert review is a throughput bottleneck | Errors can cause high financial, legal, or customer harm | Significant compliance, security, or legal lift required |
| 5 | Near-continuous expert supervision | Errors can trigger major regulatory or reputational consequences | No credible governance path with current controls |

The single most common scoring error is underestimating tails. Teams often score based on typical errors when autonomy decisions should be based on plausible high-impact errors. If tail outcomes are heavy and reversibility is weak, Incident and Governance scores should rise accordingly.

## Level Boundary Rules

The level taxonomy exists to bind architecture to risk posture. Level 2.5 uses fixed sequencing with multi-turn tool-using nodes and typed artifact handoffs, while Bounded Level 3 allows dynamic routing only inside non-bypassable policy and escalation constraints.[^taxonomy][^anthropic_build][^openai_build] The taxonomy is not branding; it defines where authority can move and where it cannot.

Promotion criteria should remain explicit. Bounded Level 3 is allowed only when Net is positive and all three taxes are at or below 2. If any tax is 3, the workflow may still be economically attractive but should remain Level 2.5 with explicit review gates. If any tax is 4 or 5, the workflow is blocked until mitigations are implemented and rescoring confirms risk reduction.

| Score condition | Governance action | Typical level |
|---|---|---|
| Any tax >= 4 | Block and mitigate before pilot | Blocked |
| All taxes <= 2 and Net > 0 | Controlled dynamic pilot eligible | Bounded Level 3 |
| At least one tax = 3 and none >= 4 | Run with fixed sequence and explicit gates | Level 2.5 |
| Manual approval required per external action | Keep humans on every actuation boundary | Level 2 |

These boundaries reduce avoidable conflict between leadership and engineering. Leadership still gets prioritization and expected-value ranking, while engineering gets a defensible hard stop when severe risk is present.

## Worked Example: Support Refund Triage

Consider a support operation handling high-volume refund triage under stable policy rules, where typical errors are inexpensive and reversible within a short window. The workflow has clear automation upside and meaningful labor savings, but review burden does not disappear entirely because edge cases and escalation quality still require experienced judgment.

A representative score can be Benefit 4, Human Bandwidth 3, Incident 2, Governance 2. The workflow passes the circuit breaker, Net is positive, and the right decision is Level 2.5 rather than Bounded Level 3 because one tax remains above the dynamic-routing threshold. This avoids premature routing complexity while preserving most of the achievable throughput gain.

| Dimension | Score | Reasoning |
|---|---:|---|
| Benefit | 4 | High volume and repeatable policy decisions |
| Human Bandwidth | 3 | Ongoing expert review of escalations |
| Incident | 2 | Low per-error downside and fast reversibility |
| Governance | 2 | Standard controls with moderate instrumentation |
| Net | +1.67 | `4 - Average(3,2,2)` |
| Decision | Level 2.5 | Positive economics, but not low-enough tax profile for Bounded 3 |

The practical implication is not "automate everything." It is to route reviews to exception points and preserve senior capacity for high-leverage adjudication rather than low-value blanket review.

## Worked Example: Procurement Approval

Now consider procurement approvals where individual errors are expensive, reversibility is slow, and audit obligations are strict. The upside narrative can look compelling because analyst hours are high, but tail risk dominates expected value when one bad approval can erase savings from a large set of correct decisions.

A representative score can be Benefit 5, Human Bandwidth 4, Incident 5, Governance 4. The workflow is blocked immediately, Net is not computed, and the next artifact is a mitigation plan rather than a pilot plan. The right move is to redesign controls first, then rescore.

| Dimension | Score | Reasoning |
|---|---:|---|
| Benefit | 5 | Large potential labor savings |
| Human Bandwidth | 4 | Expert validation remains bottleneck |
| Incident | 5 | High financial and legal downside per failure |
| Governance | 4 | Strong audit and policy-control requirements |
| Circuit breaker | Triggered | Workflow blocked pending mitigation |
| Decision | Blocked | No autonomous pilot until tax profile changes |

Mitigation should target control surfaces directly, including tiered approvals by transaction class, hard spend and velocity controls, hold periods for high-risk categories, and full trace-policy lineage for authorization events. If those controls reduce scores below blocking thresholds, Level 2.5 can be reconsidered with explicit ownership and incident thresholds.

## Reflection, Critique, and Incident Closure

Reflection and critique solve different problems and should not be treated as interchangeable. Reflection improves local output quality within the same role, which is useful for formatting, schema compliance, and consistency. Critique introduces an independent reviewer role with authority to reject transitions where consequences are high.

In high-impact workflows, reflection-only designs are structurally under-controlled because the same reasoning context is grading itself. Independent critique is slower and more expensive, but that cost is often smaller than downstream incident cost in financial, legal, security, or compliance pathways.

Incident closure should follow a structured loop with detection, analysis, mitigation, and requalification. Analysis should classify system factors, context factors, and cognitive factors so fixes target failure mechanism rather than narrative blame.[^incident] Requalification should include rescoring because significant incidents are evidence events that update the tax profile.

## Calibration in the First 30 Days

The scorecard becomes more accurate only if teams treat calibration as part of operations rather than as an annual governance ritual. During the first month, teams should record predicted versus observed values for review effort, escalation frequency, external-action rate, and incident frequency, then adjust anchors where prediction error is persistent.

This process reduces political debate because disagreements become testable over short cycles. Teams can review where they systematically under-scored governance lift, where incident tails were heavier than assumed, and where review capacity saturated earlier than expected.

A practical operating rhythm is to qualify workflows first, instrument top candidates second, run bounded pilots third, and only then expand scope. Promotion should follow measured control performance, not confidence signals.[^casebook][^prodguide]

## Closing

The scorecard is useful because it exposes hidden cost before hidden cost becomes visible loss. It gives leadership a ranking framework, gives engineering a defensible stop mechanism, and gives governance teams a shared language for intervention that is tied to operating evidence rather than abstract caution.

Teams that adopt this rigor are not slower in the long run. They move faster on workflows that are economically suited to autonomy and avoid expensive reversals on workflows where autonomy is currently a risk amplifier.

---

## Notes

[^taxonomy]: Taxonomy synthesis informed by [Anthropic](https://www.anthropic.com/engineering/building-effective-agents), [OpenAI](https://developers.openai.com/tracks/building-agents/), and production-observation literature including [Pan et al. 2026](https://arxiv.org/abs/2512.04123).

[^anthropic_build]: Anthropic Engineering, [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents).

[^openai_build]: OpenAI Developers, [Building Agents](https://developers.openai.com/tracks/building-agents/).

[^incident]: *Incident Analysis for AI Agents* (preprint): [arXiv:2508.14231](https://arxiv.org/abs/2508.14231).

[^casebook]: Casebook materials: [autonomy_tax_casebook.tsv](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/sources/derived/autonomy_tax_casebook.tsv) and [method notes](https://github.com/petroslamb/autonomy-tax-enterprise-agents/blob/main/sources/derived/autonomy_tax_casebook_method.md).

[^prodguide]: *A Practical Guide for Designing, Developing, and Deploying Production-Grade Agentic AI Workflows* (preprint): [arXiv:2512.08769](https://arxiv.org/abs/2512.08769).
