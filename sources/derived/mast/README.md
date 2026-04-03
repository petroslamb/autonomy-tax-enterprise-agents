# MAST Distillation Package

Tracked MAST artifacts for the Autonomy Tax repo live here.

- Raw `sources/raw/mast/` remains local and ignored.
- The retained raw inputs are intentionally minimal:
  - `sources/raw/mast/datasets/MAD_full_dataset.json`
  - `sources/raw/mast/datasets/MAD_human_labelled_dataset.json`
  - `sources/raw/mast/repo_files/definitions.txt`
  - `sources/raw/mast/repo_files/examples.txt`
  - `sources/raw/mast/repo_files/traces_README.md`
- This folder is the repo-usable distillation of that local bundle.
- Use these files to reason about failure mechanics, control families, and `V2` scorecard triggers.
- Do not treat MAST as enterprise cost calibration or threshold truth.
- Redundant local snapshots such as `MAST_repo/`, `MAST_repo_clone/`, and `MAST_repo_tar/` are not required for regeneration and should not be retained.

## Files

- `mast_autonomy_crosswalk.tsv`: hand-authored mapping from the 14 MAST labels into Autonomy Tax control families, taxes, `V2` subcomponents, and operator responses.
- `mast_label_stats.tsv`: per-label trace prevalence from the local `MAD_full_dataset.json`.
- `mast_pair_stats.tsv`: observed label co-occurrences and their enterprise interpretations.
- `mast_benchmark_stats.tsv`: benchmark-level failure rates, average label density, and enterprise relevance.
- `mast_system_stats.tsv`: system-level failure rates and dominant label profiles.
- `mast_failure_motifs.md`: human-readable synthesis for operators.

## Method

Generate the stats TSVs with:

```bash
python tools/derive_mast_artifacts.py \
  --dataset sources/raw/mast/datasets/MAD_full_dataset.json \
  --definitions sources/raw/mast/repo_files/definitions.txt \
  --crosswalk sources/derived/mast/mast_autonomy_crosswalk.tsv \
  --output-dir sources/derived/mast
```

The script only writes the generated TSVs. It does not overwrite:

- `mast_autonomy_crosswalk.tsv`
- `mast_failure_motifs.md`

Those two files are curated because they translate MAST into this repo's enterprise-autonomy framing.
