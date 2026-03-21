# MAST Failure Motifs For Enterprise Autonomy

This note summarizes what the local ignored MAST bundle contributes to the Autonomy Tax repo.

Use it as a diagnostic supplement for `V2`, not as enterprise threshold calibration.

## Dataset Shape

The local dataset used here is `sources/raw/mast/datasets/MAD_full_dataset.json`.

- `1242` total traces
- `956` traces with at least one active MAST label
- `3.21` average active labels among failing traces

Version caveat:

- the local full JSON contains `1242` traces, while the paper narrative references `1642`
- the local human-labeled JSON contains `19` records, while the paper narrative references `21`

Because of that mismatch, this repo uses MAST for failure mechanics and control-family design, not for enterprise threshold calibration.

## Top Label Patterns

Most common labels in the local full dataset:

- `2.6 Action-Reasoning Mismatch`: `495` traces, `39.9%` of all traces, `51.8%` of failing traces
- `1.3 Step Repetition`: `451` traces, `36.3%` of all traces, `47.2%` of failing traces
- `1.1 Disobey Task Specification`: `367` traces, `29.6%` of all traces, `38.4%` of failing traces
- `1.5 Unaware of Termination Conditions`: `346` traces, `27.9%` of all traces, `36.2%` of failing traces
- `2.2 Fail to Ask for Clarification`: `303` traces, `24.4%` of all traces, `31.7%` of failing traces
- `3.3 No or Incorrect Verification`: `283` traces, `22.8%` of all traces, `29.6%` of failing traces

The pattern is clear: MAST is strongest on workflow-control failures, not on pure intelligence shortfalls.

## Top Co-Occurrence Patterns

Most common observed label pairs:

- `1.3 + 1.5`: `299` traces, `31.3%` of failing traces
- `1.3 + 2.6`: `236` traces, `24.7%` of failing traces
- `1.1 + 2.6`: `234` traces, `24.5%` of failing traces
- `1.5 + 2.6`: `213` traces, `22.3%` of failing traces
- `2.2 + 2.6`: `206` traces, `21.5%` of failing traces
- `2.6 + 3.3`: `164` traces, `17.2%` of failing traces

This is the most useful macro-signal for the Autonomy Tax framework: failures compound across control layers instead of appearing as isolated misses.

## Control Families

The repo collapses the 14 MAST labels into five control families in `mast_autonomy_crosswalk.tsv`.

### `loop_and_termination`

Labels: `1.3`, `1.5`

- local trace coverage: `498` traces
- enterprise translation: stuck runs, retry storms, reviewer babysitting

### `context_continuity`

Labels: `1.4`, `2.1`

- local trace coverage: `73` traces
- enterprise translation: lost state, repeated handoff recovery, reconciliation work

### `clarification_and_handoff`

Labels: `2.2`, `2.4`, `2.5`

- local trace coverage: `305` traces
- enterprise translation: missing-info exceptions, unshared context, queue churn

### `plan_action_verification`

Labels: `1.1`, `2.3`, `2.6`, `3.1`, `3.2`, `3.3`

- local trace coverage: `866` traces
- enterprise translation: wrong external actions, failed checks, escaped bad writes

### `role_and_authority`

Labels: `1.2`

- local trace coverage: `10` traces
- enterprise translation: unclear final decision rights, privilege confusion

## Benchmark Relevance Weighting

Not all MAST benchmarks are equally relevant to enterprise autonomy decisions.

- `ProgramDev`: highest enterprise relevance in this dataset because it resembles orchestrated software workflows with real coordination, staging, and verification burden.
- `SWE-Bench-Lite`: high enterprise relevance because it is small but strongly tied to verifiable code-change tasks.
- `GAIA`: medium relevance because parts of it resemble bounded tool-using workflows, but it is broader than enterprise operations.
- `Test-C`: medium relevance because it is a small tool-use sample with useful verification signals.
- `GSM`, `MMLU`, `Olympiad`: low relevance for enterprise economics; still useful for coordination and compounding-failure claims.

In other words: MAST can strengthen the repo's control thesis broadly, but only part of the dataset should influence operator guidance for enterprise workflows.

## How This Fits The Autonomy Tax

MAST is most useful in this repo when it is translated into `V2` trigger rules rather than into more casebook rows.

- `loop_and_termination` raises `queue_fragility`
- `context_continuity` and `clarification_and_handoff` raise `coordination_drag`
- `plan_action_verification` raises `escape_likelihood`
- repeated verification failures raise `ongoing_assurance`
- role confusion raises `fixed_enablement`

That use is narrow, but it is defensible. It improves the scorecard's internal mechanics without pretending that MAST tells us enterprise governance cost, compliance burden, or incident dollar-loss distributions.
