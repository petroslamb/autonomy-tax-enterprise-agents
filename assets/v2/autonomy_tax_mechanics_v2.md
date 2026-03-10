# Autonomy Tax Mechanics V2 (Experimental)

This note explains the causal model behind the experimental `V2` scorecard.

- `V1` remains the default and public scorecard in this repo.
- `V2` is a drill-down for operators when `V1` is directionally right but too coarse to show where the workflow is actually breaking.
- The `V2` rubric in `assets/v2/autonomy_tax_scorecard_v2.md` is derived from this note.

## Why This Exists

The original three-tax model is still the right public frame:

- Human Bandwidth Tax
- Incident Tax
- Governance Tax

What `V2` adds is not a new thesis. It adds a more precise account of what sits inside each tax so teams can diagnose whether a workflow is failing because it overloads expert queues, expands the action surface, or requires too much control-plane work to be tolerable.

`V2` is not a predictive model. It is a structured operator heuristic.

## First-Principles Model

### Human Bandwidth Tax

Scarce expert capacity consumed or destabilized by agent behavior.

This is fundamentally a queue problem. Review cost is not just how much expert time a workflow uses in the steady state. The real issue is whether review, escalation, and coordination work arrives faster than scarce experts can clear it. Once utilization gets high, delay and supervision cost stop being linear.

### Incident Tax

Downside exposure from wrong autonomous actions escaping into real systems.

This is fundamentally a tail-risk problem. Median misses matter, but the real autonomy question is whether rare but serious failures can slip past gates and create high-cost external effects before they are caught or reversed.

### Governance Tax

Control-plane burden required to make autonomy tolerable.

This includes instrumentation, approvals, policy upkeep, assurance work, auditability, and change management. Governance is not only a burden. Some of it becomes reusable platform capability. But the workflow still has to bear the current burden required to operate safely.

### Governance Leverage

`governance_leverage` is a non-scored modifier.

- `low`: controls are mostly workflow-specific
- `medium`: some controls are reusable across adjacent workflows
- `high`: the same controls likely strengthen a broader platform or workflow family

This modifier affects rollout sequencing and platform priority. It does not reduce the current workflow score directly.

## Tax Mechanics

These equations are the mental model behind `V2`.

They are not fitted formulas and they are not used to compute the final score mechanically. They are compact guides for how to reason about the scored subcomponents.

### Human Bandwidth mechanics

```text
human_bandwidth_burden
  ≈ review_load
  + escalation_load
  + coordination_drag
  + nonlinear(queue_fragility)
```

Interpretation:

- `review_load` is the steady-state expert work.
- `escalation_load` is the exception path that pulls in specialists.
- `coordination_drag` is the handoff and reconciliation overhead.
- `queue_fragility` is the nonlinear term. Queue pain stays manageable until reviewer utilization gets high, then latency and supervision cost jump.

### Incident mechanics

```text
incident_burden
  ≈ action_surface × escape_likelihood × tail_severity
  + irreversibility_pressure
```

Where:

```text
irreversibility_pressure ≈ reversibility_window
```

Interpretation:

- `action_surface` is how much real-world write power the workflow has.
- `escape_likelihood` is the chance that a bad output clears gates and reaches the real system.
- `tail_severity` captures the fact that rare, ugly failures matter more than the median miss.
- `reversibility_window` increases burden when detection and rollback are slow, partial, or operationally expensive.

### Governance mechanics

```text
governance_burden
  ≈ fixed_enablement
  + ongoing_assurance
  + auditability_gap
  + change_burden
```

Interpretation:

- `fixed_enablement` is the front-loaded lift to build the control path.
- `ongoing_assurance` is the recurring monitoring, evaluation, and policy upkeep.
- `auditability_gap` is the penalty for weak trace reconstruction.
- `change_burden` is the recurring tax from workflow drift.

### Governance leverage mechanics

```text
governance_leverage
  ≈ reusable_control_value / workflow_specific_control_work
```

Interpretation:

- High leverage means the same instrumentation, approval logic, evaluation path, or audit trail can support many workflows.
- Low leverage means the workflow requires mostly bespoke controls.

Do not subtract leverage from governance burden inside the score. Reusable controls are still real work to build.

## Interaction Rule

The three taxes do not stay independent in practice.

```text
incidents -> more review + more governance work
review overload -> higher escape likelihood
better governance -> lower escape likelihood and lower queue fragility
```

This interaction is why `V2` still rolls up the three top-level taxes separately instead of pretending the workflow can be summarized by one clean blended formula.

## What V2 Scores

The rubric converts the model above into 12 scored subcomponents:

- Human Bandwidth Tax:
  - `review_load`
  - `escalation_load`
  - `coordination_drag`
  - `queue_fragility`
- Incident Tax:
  - `action_surface`
  - `reversibility_window`
  - `tail_severity`
  - `escape_likelihood`
- Governance Tax:
  - `fixed_enablement`
  - `ongoing_assurance`
  - `auditability_gap`
  - `change_burden`

The scoring logic is intentionally qualitative. The current evidence base supports the existence of these mechanisms more strongly than it supports precise weights.

## What V2 Does Not Score

These ideas may matter, but the repo does not yet support scoring them cleanly:

- `trust_cost`
- lagged interaction effects between incidents, review overload, and governance response
- direct amortization formulas for setup cost across many workflows
- dynamic subcomponent weighting by domain

These remain future work so the rubric does not pretend to more precision than the evidence can support.

## Evidence Basis

`V2` rests on two evidence layers.

### 1. Calibration base: the existing casebook

The calibration base remains:

- `sources/derived/autonomy_tax_casebook.tsv`
- `sources/derived/autonomy_tax_casebook_method.md`

This is still the right base for enterprise governance economics because it spans:

- enterprise incidents
- regulation and compliance
- observability standards
- tooling and platform cost floors
- production deployment guidance

This is also why `V2` does not replace `V1`. The repo has stronger evidence for the top-level tax model than for exact subcomponent weighting.

### 2. Diagnostic supplement: MAST

Use MAST as diagnostic evidence for execution-failure mechanics and interaction patterns, not as threshold-calibration truth.

Canonical local references:

- `sources/raw/mast/datasets/MAD_full_dataset.json`
- `sources/raw/mast/datasets/MAD_human_labelled_dataset.json`
- `sources/raw/mast/repo_files/definitions.txt`
- `sources/raw/mast/repo_files/examples.txt`

Local inspection of `MAD_full_dataset.json` in this repo found:

- `1242` records
- `956` traces with at least one failure label
- `3.21` average active labels among failing traces

The most common labeled modes in the local file are:

- `2.6` action-reasoning mismatch
- `1.3` step repetition
- `1.1` disobey task specification
- `1.5` unaware of termination conditions
- `2.2` fail to ask for clarification
- `3.3` no or incorrect verification
- `2.3` task derailment
- `3.2` weak verification

These support the `V2` decomposition:

- loops and clarification gaps strengthen `queue_fragility` and `coordination_drag`
- action-reasoning mismatch and verification failures strengthen `escape_likelihood`
- verification fixes strengthen `fixed_enablement` and `ongoing_assurance`

The casebook rows that bridge MAST into this repo are:

- `ATC-029`
- `ATC-030`

## Limitations

- MAST is benchmark-heavy and execution-focused. It is strong on failure mechanics but weak on enterprise compliance, audit, and platform economics.
- The local downloaded MAD files do not perfectly match the headline counts described in the paper and repo narrative. The local full JSON has `1242` records rather than the paper's `1642`, and the local human-labeled JSON has `19` records rather than the narrative `21`.
- Because of that mismatch, MAST should be treated as diagnostic evidence, not calibration truth.
- `V2` is not a fitted quantitative model. It is a structured heuristic intended to improve diagnosis, not to claim mathematically precise expected-value estimates.

## How To Use This Note

Read this note first if you need to understand the model or defend the decomposition.

Use `assets/v2/autonomy_tax_scorecard_v2.md` when you need to score a workflow, discuss mitigations, or compare autonomy candidates.
