# Autonomy Tax

Single-publication package for the three-piece *Autonomy Tax* publication line.

This package is a nested git repo that now lives under [`../`](../README.md). Its internal history and evidence pipeline remain package-local, but it is the canonical publication package for the Rooted Layers essay set.

## Package Status

- Archetype: Single-publication package
- Status: Published
- Publication map: *The Autonomy Tax*
- Canonical live publication surface: `v8`
- Canonical workflow docs: [`../../workflows/essay-iteration/README.md`](../../workflows/essay-iteration/README.md), [`../../workflows/article-polish/README.md`](../../workflows/article-polish/README.md), [`../../workflows/substack-publishing/README.md`](../../workflows/substack-publishing/README.md)

## Orientation

- Flagship essay: [`article_draft_v8A.md`](article_draft_v8A.md)
- Operator companion: [`article_draft_v8B.md`](article_draft_v8B.md)
- Control-plane companion: [`article_draft_v8C.md`](article_draft_v8C.md)
- Editorial planning surface: [`publication_plan_and_sources.md`](publication_plan_and_sources.md)
- Discussion and synthesis context: [`original_discussion.md`](original_discussion.md), [`v7_gem_mining_report.md`](v7_gem_mining_report.md)

## Evidence And Asset Surfaces

- The package keeps a stronger established evidence layout under [`sources/`](sources/) rather than the generic `papers/` layout.
- The master source manifest lives in [`sources/source_manifest.tsv`](sources/source_manifest.tsv).
- Raw captures live in [`sources/raw/`](sources/raw/).
- Derived casebook and method notes live in [`sources/derived/`](sources/derived/).
- Scorecard assets and exported publication media live in [`assets/`](assets/).
- NotebookLM notebook mapping lives in [`status.yaml`](status.yaml) and is indexed in [`../notebooklm-notebooks.md`](../notebooklm-notebooks.md).

## Normalization Note

Because this package is a nested repo with its own history, it is treated as a documented exception to the root repo’s generic folder-shape enforcement.

For now:

- `sources/` is the canonical evidence layer
- the `v1` through `v8` draft ladder is the effective local archive history
- `v8A`, `v8B`, and `v8C` remain the final implemented publication package in this repo

## Working Guidance

- Keep claim-level evidence traceable through [`sources/source_manifest.tsv`](sources/source_manifest.tsv) and the derived casebook.
- Preserve terminology lock across the A/B/C publication surface.
- Treat `V1` scorecard assets as canonical for the published package and `V2` assets as experimental drill-down material.
- Use public URLs in publication copy; do not publish local relative repository links.
