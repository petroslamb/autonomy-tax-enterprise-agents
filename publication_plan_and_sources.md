# Publication Plan and Sources (V4 Breakout)

## Mission
- Transform `article_draft_v4.md` from a strong synthesis into a breakout thesis essay.
- Core claim: enterprise agent ROI is constrained by control-layer costs more than model intelligence.
- Ownable framework: **Autonomy Tax** with three terms: Human Bandwidth Tax, Incident Tax, and Governance Tax.

## Working Package
- Primary title: **The Autonomy Tax**
- Deck: **Why Enterprise Agents Fail on Control, Not Intelligence**
- Publication: Rooted Layers (Substack)
- Draft in progress: `article_draft_v4.md`
- Current word count: 3,171 total (2,652 body + 519 appendix)
- Target word count: 4,200 body (acceptable ceiling 4,400)

## Breakout Bar
- The thesis is declared in first 3 paragraphs.
- Reader gets one "rethink" moment supported by triangulated evidence, not one stat.
- Reader gets a usable Monday artifact, not only analysis.
- Anti-thesis is steelmanned honestly.
- Claims are auditable with direct citations in body text.
- Framework is framed as a heuristic, not a validated model.

## Non-Negotiables (Locked)
- Composite cold open that previews all three taxes.
- Composite scenarios explicitly labeled as illustrative when not a named incident.
- Scorecard uses a first-class circuit breaker: any single tax >= 4 means blocked until mitigation.
- Net score is computed only after passing the circuit breaker.
- Human Bandwidth bridging mechanism explicitly stated: AI output throughput can scale faster than expert review throughput.
- Governance Tax presented as least-measured tax, with measurement gap called out as a finding.
- Anti-thesis includes high-volume, low-error-cost case where Level 3 can win.
- Prediction includes practical disproof criteria.

## Structure and Word Budget (Target)
| Section | Target words | Purpose |
|---|---:|---|
| 1. Hook + Thesis + Scope | 250 | Composite incident beat, equation, scope boundary |
| 2. Deployment Paradox | 550 | Capability growth vs constrained deployments |
| 3. Human Bandwidth Tax | 700 | Triangulated paradox, mechanism, caveats |
| 4. Incident Tax | 600 | Control failures, blast-radius logic |
| 5. Governance Tax | 500 | Regulatory + observability + staffing costs |
| 6. Decision Rule + Scorecard | 500 | Level 2.5 vs 3 rule, circuit breaker workflow |
| 7. When Level 3 Wins (Anti-thesis) | 450 | Honest counter-case with sensitivity logic |
| 8. Three Things to Do Monday | 300 | Specific actions with concrete outputs |
| 9. 2027 Prediction | 150 | Falsifiable forecast and disproof triggers |
| Appendix | 600-900 | Source tiers, limitations, rubric, citations |

## Voice and Rhythm Map
- Section 1: Op-ed energy, short sentences, high stakes.
- Section 2: Data-dense analytical voice, restrained claims.
- Section 3: Surprise and mechanism, "this changes your staffing math."
- Section 4: Incident post-mortem voice, concrete controls.
- Section 5: Operational governance voice, implementation drag.
- Section 6: Field guide voice, table-first and scannable.
- Section 7: Adversarial honesty, strongest counterargument first.
- Section 8: Operator checklist voice, assignment-ready language.
- Section 9: Clear forecast voice with explicit falsifiers.

## Breakout Artifact Package
- Derived dataset: `sources/derived/autonomy_tax_casebook.tsv` as original synthesis moat.
- Method notes: `sources/derived/autonomy_tax_casebook_method.md` for coding transparency.
- In-body scorecard table with circuit-breaker column.
- One fully worked example (at least one blocked workflow and one pass workflow).
- One sensitivity table for error-cost regimes (low, medium, high).
- Optional downloadable asset for distribution: `assets/autonomy_tax_scorecard_template.csv`.
- Scoring rubric companion: `assets/autonomy_tax_scorecard_rubric.md`.

## Source Strategy
### Tiering Policy
- Tier 1: Peer-reviewed, major institutional, or government records.
- Tier 2: Large-sample surveys and reputable consulting reports.
- Tier 3: Preprints and working papers (always labeled as preprint).
- Tier 4: Vendor content and press releases (always caveated).
- Tier 5: Frameworks and standards (guidance context, not empirical proof).

### Required Core Sources by Section
| Section | Required sources |
|---|---|
| 1 | Proxy (SRC-026), Xu (SRC-050), Song (SRC-049) |
| 2 | Deloitte (SRC-007), McKinsey (SRC-008), Anthropic (SRC-009), MAP (SRC-073), METR (SRC-039) |
| 3 | NBER w31161 (SRC-060), Xu (SRC-050), Song (SRC-049) |
| 4 | Proxy (SRC-026), NVD CVE-2025-32711 (SRC-012), EchoLeak (SRC-076), Agents of Chaos (SRC-075) |
| 5 | Deloitte (SRC-007), Akto (SRC-010), EU AI Act package (SRC-020-022), NIST RMF (SRC-032/SRC-066), LangSmith (SRC-018), Braintrust (SRC-019), OpenTelemetry (SRC-038) |
| 6 | Anthropic building agents (SRC-072), OpenAI building agents (SRC-071), MAP (SRC-073) |
| 7 | Klarna press release (SRC-013), explicit assumption label for scenario math |
| 8 | Reuse sections 3-6 operationally |
| 9 | Structural argument; no single source dependency |

## Citation Integrity Policy (Hard Rules)
- Every first-use quantitative claim in body text must include a direct URL or DOI inline.
- No label-only citations for key claims (for example "McKinsey 2025" without link).
- Every preprint must carry a preprint caveat at first mention.
- Vendor/self-reported claims must include incentive-bias caveat at first mention.
- Composite scenarios must be labeled as composites in-line or immediate note.
- If a number is illustrative, label it explicitly as illustrative and not observed.

## Known Risks and Mitigations
| Risk | Impact | Mitigation |
|---|---|---|
| Scorecard feels pseudo-precise | Credibility loss | Keep heuristic framing and circuit breaker first |
| Anti-thesis math seen as invented | Trust loss | Use sensitivity ranges and explicit assumptions |
| Human Bandwidth triangulation challenged | Thesis weakens | State domain-bridging mechanism and caveat clearly |
| Governance Tax evidence thin | Section feels assertive | Frame measurement gap as finding, avoid false precision |
| Word count pressure drops caveats | Integrity drops | Keep caveats in body; move long methods to appendix |

## Editing Checklist Before Publish
- Thesis appears in first 3 paragraphs.
- Composite opening clearly labeled.
- Scorecard includes circuit-breaker status per workflow.
- At least one blocked workflow and one approved workflow shown.
- Human Bandwidth section includes explicit bridging sentence.
- Governance section states "least-measured tax" and why it matters.
- Anti-thesis includes a real low-error-cost/high-volume economic case.
- Every critical number has inline direct citation.
- No unsupported or anecdotal quantitative claim remains.
- Body word count is 4,000+ with no integrity regressions.

## Final Release Validation
- Read aloud pass for pacing and sentence rhythm.
- Numerical verification pass against `sources/source_manifest.tsv`.
- Link check pass for all URLs in body and appendix.
- Claim-to-source audit pass by section owner.
- Final editorial decision: publish only if all non-negotiables pass.
