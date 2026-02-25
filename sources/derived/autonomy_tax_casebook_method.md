# Autonomy Tax Casebook Method (V1)

## Purpose
This file documents how `autonomy_tax_casebook.tsv` was constructed so the dataset can be cited as an original, auditable synthesis artifact in the article.

## Unit of Analysis
- One row is one coded evidence record.
- A record can be a study result, incident, survey finding, regulatory milestone, standards artifact, or pricing baseline.
- Some rows represent control enablers rather than tax events; those are marked with `supports_tax_model=no`.

## Inclusion Rules
- Source must exist in `sources/source_manifest.tsv` with a valid `SRC-*` id.
- Source must provide at least one concrete signal (numeric metric, explicit event, timeline milestone, or documented control pattern).
- Claims coded into rows must be directly traceable to the source text; no invented organization-level details.
- Vendor and self-reported claims are allowed but confidence is downgraded unless independently corroborated.

## Coding Schema
### `primary_tax` values
- `human_bandwidth_tax`: expert review, rework, coordination, or quality-gate bottlenecks.
- `incident_tax`: direct loss, exploitability, security/privacy failure, destructive action risk.
- `governance_tax`: compliance, observability, staffing, reporting, and policy overhead.
- `throughput_gain`: explicit gain cases used for anti-thesis boundaries.
- `control_enabler`: methods/standards that reduce tax exposure but do not measure tax directly.
- `context`: capability context that shapes pressure but is not itself a tax measurement.

### `net_signal` values
- `tax`: predominantly evidence of hidden cost or risk.
- `gain`: predominantly evidence of throughput/productivity benefit.
- `mixed`: simultaneous gain and cost signals.

### `confidence` values
- `high`: government data, peer-reviewed/major institutional source, or direct first-party metric with clear methodology.
- `medium`: preprint or strong but partial evidence.
- `low_to_medium`: vendor/self-reported data or survey with potential sampling bias.

## Reproducibility
- File path: `sources/derived/autonomy_tax_casebook.tsv`
- Delimiter: tab (`.tsv`)
- Source mapping key: `source_id` joins to `sources/source_manifest.tsv`
- Record count query:

```bash
awk 'END{print NR-1}' sources/derived/autonomy_tax_casebook.tsv
```

- Primary tax distribution query:

```bash
awk -F '\t' 'NR>1{count[$8]++} END{for(k in count) print k, count[k]}' sources/derived/autonomy_tax_casebook.tsv
```

## Known Limitations
- No original interviews or private telemetry are included; this is structured synthesis of public sources.
- Mixed evidence quality is intentional; source tier and confidence encode uncertainty explicitly.
- Several entries are framework/guidance artifacts (`control_enabler`) and should not be interpreted as empirical effect sizes.
- Pricing rows are temporal snapshots and will drift over time.

## Intended Use in the Article
- Cite the casebook as the article's original contribution layer: a normalized taxonomy across incidents, studies, and governance artifacts.
- Use row subsets to support each tax section.
- Human Bandwidth Tax: `ATC-007` to `ATC-009`
- Incident Tax: `ATC-010` to `ATC-013`
- Governance Tax: `ATC-014` to `ATC-025`
- Anti-thesis boundary case: `ATC-026`
