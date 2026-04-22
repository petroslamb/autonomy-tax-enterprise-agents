# Package Blueprint: The Autonomy Tax

This file is the governing brief for the published `v8` Autonomy Tax package.

It exists for two reasons:

1. to give the package a resolvable `config.blueprint_path` under the current workflow rules
2. to preserve the actual governing frame of the published package without pointing lifecycle routing at the unimplemented `v9` breakout plan

This is an archival governing brief for the live `v8` surface, not an instruction to reopen the package around the abandoned `v9` breakout spec.

Live draft: `the-autonomy-tax.md`
Published package surface: `v8A`, `v8B`, `v8C`

## Promise

The active package thesis is that enterprise agent ROI breaks first at the control surface rather than at model intelligence. The flagship essay must explain that the hidden cost of autonomy is not one thing but three compounding taxes: expert review burden, incident exposure, and governance overhead. The package survives pressure because each companion has a distinct job. The flagship names the causal engine and decision rule. The scorecard turns the thesis into a workflow qualification tool. The control-plane companion explains how bounded autonomy is actually implemented in production.

## Spine

The package-level argumentative spine is fixed:

1. **Flagship object**: `the-autonomy-tax.md` / `article_draft_v8A.md`
   Prove that the main deployment bottleneck is the control layer and introduce the three-tax frame.
2. **Decision surface**: `article_draft_v8B.md`
   Convert the thesis into a practical scoring and level-selection framework.
3. **Architecture surface**: `article_draft_v8C.md`
   Explain how non-bypassable gates, routing constraints, trace continuity, and incident loops make bounded autonomy operable.

## Paragraph Burden

### Flagship

The flagship must do five things:

- establish a concrete incident-style opening that makes control-layer failure legible
- define the three taxes as compounding constraints rather than as isolated risks
- explain why capability growth does not remove the verification and governance bottleneck
- draw the boundary between Level 2.5 and Bounded Level 3
- end on a decision question for leaders, not on generic future-of-AI prose

The flagship must not become a scorecard manual or a control-plane implementation guide.

### Scorecard

The scorecard must:

- qualify workflows before deployment
- make the circuit breaker impossible to miss
- preserve the autonomy taxonomy and level-decision logic from the flagship
- keep examples operational and bounded

It must not restate the flagship at essay length or drift into system architecture detail that belongs in the control-plane companion.

### Control Plane

The control-plane companion must:

- define non-bypassable gates
- explain state-gated routing and bounded exploration
- require trace continuity for external actions
- describe the structured incident loop
- explain how systems graduate between autonomy levels

It must not become a second flagship essay or a generic observability memo.

## Evidence Burden

The package's evidence home remains `sources/`, with `sources/source_manifest.tsv` as the canonical source index.

The flagship is licensed to make these load-bearing claims:

- deployment caution persists despite model capability gains
- expert review becomes the scarce resource as AI output scales
- incident exposure scales with autonomy and poor control design
- governance overhead is real even when it is weakly measured
- most enterprise autonomy should remain bounded until controls are explicit

The scorecard is licensed to operationalize the thesis into:

- the autonomy-level taxonomy
- the circuit-breaker rule
- workflow scoring heuristics
- worked examples and mitigation paths

The control-plane companion is licensed to govern:

- gating and policy invariants
- routing constraints
- traceability requirements
- incident handling and graduation logic

Use `publication_plan_and_sources.md` only as archival planning context. It is not the governing brief for the published package because it is explicitly a `v9` breakout operating spec for an unimplemented revision.

## Cut Order

If the package is ever revised again, cut in this order before changing the core object:

1. duplicated explanation across `v8A`, `v8B`, and `v8C`
2. implementation detail in the flagship that belongs in the companions
3. speculative `v9` breakout ambitions not supported by the published `v8` object
4. ornament, meta-commentary, or repeated throat-clearing before any load-bearing claim

Do not cut the three-tax causal engine, the Level 2.5 versus Bounded Level 3 boundary, or the role separation across the three pieces.

## Failure Triggers

This governing brief is void for routing purposes if any of the following happens:

- `status.yaml` points back to the archival `v9` plan instead of this file
- the package starts treating `publication_plan_and_sources.md` as the active governing brief without first rewriting it into a true package-level blueprint
- the flagship collapses into scorecard mechanics or control-plane implementation detail
- the companions stop being independently useful and revert to essay overflow dumps
- a future rewrite tries to govern the published `v8` package from speculative `v9` goals instead of first deciding that a new package object actually exists

## Opening Lab

Not active.

## Object Decision

The package's current object is the published `v8` three-piece line, not the unimplemented `v9` breakout successor. Any future escalation should first decide whether a genuine new package object exists before changing this governing brief.

## Body / Support / Footnote Ledger

- **Body work**: the three-tax thesis, deployment paradox, autonomy boundary, circuit breaker, bounded control-plane doctrine
- **Support work**: worked examples, mitigation sequences, taxonomy explanation, observability and incident-loop mechanics
- **Footnote or appendix work**: extended caveats, lower-priority source qualification, asset-specific implementation notes, and speculative next-step planning

## Second-Pass Bet

If the package is reopened, the strongest next move is not to chase a louder hook first. It is to preserve the current package split, decide whether a real successor object exists beyond `v8`, and only then write a new governing brief for that successor rather than retrofitting `v9` planning notes into the published package's lifecycle metadata.
