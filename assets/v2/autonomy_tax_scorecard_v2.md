# Autonomy Tax Scorecard V2 (Experimental)

This file is the experimental `V2` scoring guide for the Autonomy Tax scorecard.

- `V1` remains the default and public scorecard in this repo.
- `V2` is a layered drill-down, not a reversal of the thesis.
- Read `assets/v2/autonomy_tax_mechanics_v2.md` first if you need the causal model, equations, or evidence basis behind this rubric.
- Use `V2` when a workflow is near the autonomy boundary, when a `Level 2.5` or `Level 3` design has multiple agent handoffs, or when `V1` identifies a tax but does not explain the failure mechanics clearly enough to drive mitigation.

## Positioning

`V1` is still the better public product:

- three top-level taxes
- one circuit-breaker rule
- one deployment decision

`V2` keeps that frame and adds operator detail underneath it. This file is deliberately narrower than the mechanics note. Its job is to help a team score a workflow consistently, not to restate the whole argument for why the decomposition exists.

## Use Order

1. Score all 12 subcomponents from `1` to `5`.
2. Roll each parent tax up from its four subcomponents.
3. Apply the conservative override rules.
4. Apply the existing circuit breaker at the parent-tax level.
5. For non-blocked workflows, compute `Net = Benefit - Average(HB, Incident, Governance)`.
6. Record `governance_leverage` separately and use it for rollout sequencing, not direct score reduction.
7. Name any `4+` subcomponent explicitly in the mitigation plan, even if the rolled-up parent tax stays below `4`.

## V2 Subcomponents

### Human Bandwidth Tax

- `review_load`: how much expert review the workflow demands during normal operation
- `escalation_load`: how often outputs require specialist intervention or exception handling
- `coordination_drag`: how much cross-role handoff and reconciliation work the workflow creates
- `queue_fragility`: how sensitive the workflow is to reviewer scarcity, spikes, or backlog growth

### Incident Tax

- `action_surface`: how much external write power and operational reach the workflow has
- `reversibility_window`: how easy it is to reverse or contain a bad action before harm compounds
- `tail_severity`: how bad the rare but serious failure cases are
- `escape_likelihood`: how likely a bad output is to clear gates and reach production or external systems

### Governance Tax

- `fixed_enablement`: one-time or front-loaded control work needed before safe operation
- `ongoing_assurance`: recurring monitoring, evaluation, review, and policy upkeep
- `auditability_gap`: how hard it is to reconstruct decisions, actions, and approvals after the fact
- `change_burden`: how much ongoing workflow drift forces prompt, tool, policy, and approval updates

## Governance Leverage

Record `governance_leverage` separately as `low`, `medium`, or `high`.

- `low`: controls are mostly workflow-specific
- `medium`: some controls are reusable across adjacent workflows
- `high`: the same controls likely strengthen a broader platform or workflow family

This modifier helps with sequencing. It does not reduce the scored governance burden directly.

## Scoring Anchors

Use the same `1-5` scale as `V1`. Keep the anchors qualitative. The point is consistent operator judgment, not fake precision. Use the closest fit and round up when the workflow sits between two risk levels.

### Human Bandwidth Tax

| Subcomponent | `1` | `2` | `3` | `4` | `5` |
| --- | --- | --- | --- | --- | --- |
| `review_load` | deterministic or auto-checkable | light expert review | regular expert review | heavy review bottleneck | continuous expert supervision |
| `escalation_load` | rare, low-effort escalations | occasional escalations | regular specialist escalations | escalations distort staffing or SLA | specialist intervention is routine |
| `coordination_drag` | minimal handoffs | some clarifications | regular cross-role coordination | handoffs are a throughput bottleneck | active orchestration across experts |
| `queue_fragility` | ample slack, spikes clear | mild queue growth | noticeable backlog at peaks | backlog hard to recover from | unstable with modest volume/staffing shock |

### Incident Tax

| Subcomponent | `1` | `2` | `3` | `4` | `5` |
| --- | --- | --- | --- | --- | --- |
| `action_surface` | no external writes or sandbox only | narrow low-value writes | material but bounded writes | can move money or change important state | high privilege or large-scale effects |
| `reversibility_window` | easy, fast reversal | reversible within same day/cycle | reversal needs real effort | narrow or expensive reversal window | effectively irreversible |
| `tail_severity` | cheap and reversible | moderate, recoverable harm | material cost or service impact | high financial, security, or customer harm | regulatory, legal, or major reputational harm |
| `escape_likelihood` | strong gates catch almost all failures | most failures caught before action | meaningful share can clear gates | gates are weak or inconsistent | no reliable containment before impact |

### Governance Tax

| Subcomponent | `1` | `2` | `3` | `4` | `5` |
| --- | --- | --- | --- | --- | --- |
| `fixed_enablement` | existing controls already fit | minor instrumentation or policy updates | new observability or approval paths | significant compliance, legal, or platform lift | no adequate governance path exists |
| `ongoing_assurance` | minimal recurring review | periodic spot checks | regular monitoring and policy upkeep | dedicated recurring assurance work | continuous named cross-functional staffing |
| `auditability_gap` | full traceability already exists | minor trace gaps | some manual reconstruction needed | major trace gaps slow reconstruction | workflow cannot be reconstructed credibly |
| `change_burden` | workflow is stable | occasional low-cost updates | regular tuning across prompts/tools/rules | frequent drift drives recurring control work | drift outpaces governance capacity |

## Trace Evidence Rules

Use these rules when a workflow has staging or red-team traces that can be mapped to the MAST labels in `sources/derived/mast/mast_autonomy_crosswalk.tsv`.

Definitions:

- `workflow sample`: the most recent `10` staging traces for that workflow, or all available traces if fewer than `10`
- `repeated evidence`: either the same MAST label appears in at least `2` traces in that workflow sample, or at least `2` labels from the same control family appear across that workflow sample
- `floor`: set the subcomponent to at least the stated value before roll-up and override rules are applied

Trigger rules:

| Evidence pattern | Score effect |
| --- | --- |
| repeated `loop_and_termination` evidence | floor `queue_fragility` at `3` |
| repeated `context_continuity` evidence | floor `coordination_drag` at `3` |
| repeated `clarification_and_handoff` evidence | floor `coordination_drag` at `3` |
| repeated `plan_action_verification` evidence | floor `escape_likelihood` at `3` |
| repeated `plan_action_verification` evidence and `action_surface >= 3` | floor `escape_likelihood` at `4` |
| repeated `3.2` or `3.3` evidence | floor `ongoing_assurance` at `3` |
| any `1.2` evidence | floor `fixed_enablement` at `3` |

## Roll-Up and Blocker Rules

### Parent tax roll-up

For each tax:

`parent_tax = round_half_up(average_of_four_subcomponents)`

Use arithmetic mean and round half up. Example: `2.5 -> 3`, `3.5 -> 4`.

### Conservative override

After the average is computed:

- if any subcomponent is `5`, floor the parent tax at `4`
- if any two subcomponents are `4+`, floor the parent tax at `4`

This preserves the `V1` circuit-breaker logic while preventing a severe risk from disappearing inside an average.

### Circuit breaker

The existing `V1` circuit breaker remains unchanged:

- if any parent tax is `4` or `5`, the workflow is blocked until a mitigation plan exists

### Red-flag rule

Any `4+` subcomponent must be named in the mitigation plan even if the rolled-up parent tax does not trigger the circuit breaker.

This is especially important for:

- `queue_fragility`
- `tail_severity`
- `escape_likelihood`
- `auditability_gap`

## Worked Examples

The point of `V2` is to add nuance without breaking the underlying `V1` recommendation.

### Example 1: `support_refund_triage`

This remains a non-blocked `Level 2.5` case under `V2`.

| Subcomponent | Score | Why |
| --- | --- | --- |
| `hb_review_load` | `3` | Regular review is still needed for customer-facing decisions. |
| `hb_escalation_load` | `2` | Only some cases escalate to specialists. |
| `hb_coordination_drag` | `3` | Refund routing and exception handling create real handoffs. |
| `hb_queue_fragility` | `2` | Volume is high, but the queue is manageable under normal staffing. |
| `incident_action_surface` | `2` | Low-value customer service actions with bounded scope. |
| `incident_reversibility_window` | `2` | Most errors can be reversed within a day. |
| `incident_tail_severity` | `2` | Error cost is low and usually recoverable. |
| `incident_escape_likelihood` | `2` | Human gates and business rules catch most bad outputs. |
| `governance_fixed_enablement` | `2` | Minor instrumentation and policy work. |
| `governance_ongoing_assurance` | `2` | Regular but light monitoring and review. |
| `governance_auditability_gap` | `2` | Existing support tooling already captures most decisions. |
| `governance_change_burden` | `2` | Rules change, but not fast enough to destabilize controls. |

Roll-up:

- `Human Bandwidth Tax = round_half_up((3+2+3+2)/4) = 3`
- `Incident Tax = round_half_up((2+2+2+2)/4) = 2`
- `Governance Tax = round_half_up((2+2+2+2)/4) = 2`
- `Governance Leverage = high`
- `Net = 4 - Average(3,2,2) = 1.67`

Decision:

- not blocked
- recommended `Level 2.5`
- `V2` adds useful nuance by showing that the real constraint is review and coordination load, not incident severity

### Example 2: `procurement_approval`

This remains blocked under `V2`.

| Subcomponent | Score | Why |
| --- | --- | --- |
| `hb_review_load` | `4` | Approvals need heavy expert review. |
| `hb_escalation_load` | `4` | Exceptions and vendor edge cases regularly escalate. |
| `hb_coordination_drag` | `3` | Procurement, finance, and policy owners must align. |
| `hb_queue_fragility` | `4` | Reviewer scarcity quickly turns into backlog and delay. |
| `incident_action_surface` | `5` | Actions can move money and alter real external commitments. |
| `incident_reversibility_window` | `4` | Some mistakes are hard to unwind cleanly once approved. |
| `incident_tail_severity` | `5` | Rare bad approvals can create severe loss, compliance, or fraud exposure. |
| `incident_escape_likelihood` | `5` | If gates fail, the downstream impact is direct and expensive. |
| `governance_fixed_enablement` | `4` | Significant approval, traceability, and policy lift is required. |
| `governance_ongoing_assurance` | `4` | Recurring monitoring and review are required. |
| `governance_auditability_gap` | `4` | Manual reconstruction risk is unacceptable for approvals. |
| `governance_change_burden` | `4` | Policy, vendor, and threshold drift require recurring updates. |

Roll-up:

- `Human Bandwidth Tax = round_half_up((4+4+3+4)/4) = 4`
- `Incident Tax = round_half_up((5+4+5+5)/4) = 5`
- `Governance Tax = round_half_up((4+4+4+4)/4) = 4`
- `Governance Leverage = medium`

Decision:

- blocked by parent-tax circuit breaker
- red-flag subcomponents that must be named in mitigation:
  - `hb_review_load`
  - `hb_escalation_load`
  - `hb_queue_fragility`
  - `incident_action_surface`
  - `incident_reversibility_window`
  - `incident_tail_severity`
  - `incident_escape_likelihood`
  - all four governance subcomponents
- `V2` adds useful nuance by showing that the workflow is not just "high incident risk." It is simultaneously a heavy review queue, a tail-risk surface, and a governance-heavy control problem.

## What V2 Does Not Yet Score

See `assets/v2/autonomy_tax_mechanics_v2.md` for the model boundaries and evidence limitations behind those exclusions.

## Default Recommendation

Use `V1` first.

Use `V2` when:

- the workflow is a serious `Level 2.5` or `Level 3` candidate
- `V1` identifies a tax but the mitigation path is unclear
- multiple-agent handoffs or repeated staging failures make execution mechanics the main problem

If `V1` and `V2` disagree materially, treat that as a signal to investigate the workflow further rather than a reason to trust `V2` automatically.
