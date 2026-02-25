# Autonomy Tax Scorecard Rubric (V1)

## Use Order
1. Score each tax from 1 to 5 using anchors below.
2. Apply circuit breaker first.
3. If any tax is 4 or 5, mark workflow as blocked until mitigation plan exists.
4. For non-blocked workflows, compute `Net = Benefit - Average(HB, Incident, Governance)`.
5. Rank only non-blocked workflows for pilot priority.

## Circuit Breaker Rule
- Trigger: any single tax score `>= 4`
- Effect: workflow cannot move to autonomous pilot until documented mitigation is approved.

## Scoring Anchors

### Human Bandwidth Tax
- 1: Minimal expert review; outputs are deterministic and auto-checkable.
- 2: Light expert review; spot checks only.
- 3: Regular expert review needed for quality or correctness.
- 4: Heavy expert review; experts become throughput bottleneck.
- 5: Continuous expert supervision required; review load displaces core work.

### Incident Tax
- 1: Errors are cheap (<$10) and easily reversible.
- 2: Errors are moderate but recoverable with low operational effort.
- 3: Errors can create material cost or service impact.
- 4: Errors can cause high financial, security, or customer harm.
- 5: Errors can cause regulatory, legal, or major reputational damage.

### Governance Tax
- 1: Existing controls and logs already satisfy policy and audit needs.
- 2: Minor instrumentation and policy updates required.
- 3: New observability, review workflows, or approvals required.
- 4: Significant compliance/infosec/legal lift before safe operation.
- 5: No adequate governance path currently in place for this workflow.

## Level Guidance
- Level 1: Copilot — single LLM call, human executes.
- Level 2: Pipeline — linear chain of single-turn LLM calls, human reviews before external action.
- Level 2.5: Artifact pipeline — linear chain of multi-turn ReAct agents with tools, structured I/O contracts between nodes, human gates at decision points.
- Level 3: Autonomous — dynamic routing or policy engine, outputs reach external systems without per-action human review.
- Level 4: Fully autonomous — decentralized actor model, no human in loop.
