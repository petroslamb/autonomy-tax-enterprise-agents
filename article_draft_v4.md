# The Autonomy Tax

*Why Enterprise Agents Fail on Control, Not Intelligence*

---

An AI agent burned through $4,800 in three minutes on a runaway document batch — no hallucination, no jailbreak, just a missing spend cap. That same week, at a different company, a senior engineer spent hours reviewing AI-generated pull requests that a junior developer shipped at several times his usual pace — and found defects in a significant fraction. Meanwhile, a compliance team discovered their agent pipeline was writing customer data into an unencrypted observability trace. Three incidents, three teams, one shared root cause: none of them failed because the model was too stupid. They failed because the control layer wasn't engineered.

*[Note: The first incident is sourced from the [Proxy post-mortem](https://www.useproxy.ai/blog/ai-agent-overspend-postmortem), Jan 2026. The second and third are composite scenarios illustrating patterns documented in [Xu et al. 2025](https://arxiv.org/abs/2510.10165) and [Song et al. 2025](https://arxiv.org/abs/2410.02091); specific organizations are anonymized in both studies.]*

This article argues a simple claim: enterprise agent ROI is constrained less by model capability and more by three hidden costs that compound as autonomy increases. We call them the **Autonomy Tax**:

> **Net Agent Value = Throughput Gain − Human Bandwidth Tax − Incident Tax − Governance Tax**

In practice, we operationalize this as a scorecard heuristic: a circuit breaker first, then a normalized net score for non-blocked workflows.

If that equation holds, then the current industry debate — which model is smartest, which framework is fastest — is asking the wrong question. The right question is: *can your organization absorb the tax?*

**Scope note:** This analysis focuses on enterprises consuming commercial LLM APIs (Anthropic, OpenAI) in US/EU markets. Self-hosted and open-weight deployments carry a different tax structure.

---

## The Deployment Paradox

Enterprise AI intent has never been higher. Deloitte's 2026 survey of 3,235 director-to-C-suite leaders in 24 countries found that 74% expect to be using agentic AI at moderate levels or above within two years — up from 23% using it today [[Deloitte 2026](https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/services/consulting/2026/state-of-ai-2026.pdf), n=3,235]. McKinsey reports 88% of organizations using AI in at least one function, though majority usage remains in pilot stages [[McKinsey 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai); note: this figure covers all AI, not agents specifically]. The appetite is real.

The deployment reality is cautious. On Anthropic's platform, software engineering accounts for nearly 50% of all agentic tool-call activity. Customer service, business intelligence, and e-commerce each register single-digit percentages [[Anthropic, Feb 2026](https://www.anthropic.com/research/measuring-agent-autonomy), n=998K tool calls; note: reflects Anthropic's API usage patterns only]. The most comprehensive field survey to date, covering 306 practitioners and 20 production case studies across 26 domains, found that 68% of deployed agents execute ten or fewer steps before human intervention, 70% rely on prompting rather than weight tuning, and 74% depend primarily on human evaluation [[Pan et al. 2026](https://arxiv.org/abs/2512.04123), preprint, n=306].

Meanwhile, raw capability is accelerating. METR's task-horizon measurements suggest that frontier AI models can now successfully complete tasks that take humans roughly 50 minutes, with the horizon doubling approximately every seven months since 2019 [[Kwa et al. 2025](https://arxiv.org/abs/2503.14499), preprint; caveat: external validity is explicitly uncertain].

So models are getting more capable, but production agents remain tightly constrained. Why? Because the bottleneck isn't intelligence. It's control bandwidth.

---

## The Human Bandwidth Tax

Here is the finding that should make enterprise leaders uncomfortable: AI productivity tools create a hidden tax on your most experienced people.

The mechanism is consistent across domains: AI raises output throughput faster than it raises expert review capacity. When juniors produce more, seniors review more. The net effect on the *team* depends on a ratio that almost nobody measures.

The evidence comes from three independent studies across different contexts:

**Customer support.** In data covering 5,179 agents at a Fortune 500 company, access to a generative AI assistant increased issues resolved per hour by 14% on average — driven by a 34% improvement for novice workers and minimal impact on experienced performers. The AI effectively disseminated senior-level best practices to the entire workforce [[Brynjolfsson et al. 2023, NBER w31161](https://doi.org/10.3386/w31161), n=5,179]. On the surface, this is a clear win. But the asymmetry matters: high-performers gained almost nothing individually while absorbing more quality-assurance load as output volumes increased.

**Collaborative software development (OSS evidence).** A study of open-source projects following GitHub Copilot's introduction found that AI-assisted programming *decreased* experienced developer productivity. Core developers reviewed 6.5% more code after Copilot adoption, while their own original code output dropped by 19%. The productivity gains accrued to peripheral (less-experienced) contributors, while the maintenance and quality-control burden shifted to the expert pool [[Xu et al. 2025](https://arxiv.org/abs/2510.10165), preprint; presented at WITS 2025, CIST 2025, SCECR 2025, INFORMS 2024; note: OSS projects, not enterprise-internal teams].

**Open-source collaboration.** Using GitHub's proprietary Copilot usage data combined with public OSS repository data, a separate study confirmed the pattern: Copilot use increased project-level code contributions by 5.9%, but coordination time for code integration rose by 8%. Peripheral developers showed smaller gains and faced higher coordination overhead than core developers [[Song et al. 2025](https://arxiv.org/abs/2410.02091), preprint].

Three different contexts — call centers, OSS projects, open-source communities — and the same structural pattern: AI amplifies junior output, expert review becomes the bottleneck, and the net effect depends on team composition. If your organization has many novices and few experts, the Human Bandwidth Tax is highest — and that is a common shape in enterprise teams, though we note the evidence is from customer support and OSS, not enterprise-internal dev teams directly.

*[Caveat: All three studies are preprints or working papers. The NBER study examines AI-assisted human workers, not autonomous agents. The Xu and Song studies examine code assistants, not multi-step agent pipelines — all three are Level 1 (copilot) tools in the taxonomy presented later. The bridging inference — that the same expert-bottleneck dynamic applies to agent-generated outputs — is plausible but not directly demonstrated. If anything, the tax likely intensifies at higher autonomy levels: a Level 2.5 agent producing richer, multi-turn outputs generates more material per cycle for seniors to review than a single-turn copilot suggestion.]*

---

## The Incident Tax

The Human Bandwidth Tax drains productivity. The Incident Tax destroys capital.

**The retry loop.** The Proxy post-mortem documents the canonical failure pattern. A procurement agent entered a retry loop when a vendor checkout API returned inconsistent responses. In three minutes, it submitted twelve purchase requests at $399 each — every one approved by a policy engine that evaluated transactions individually without velocity checks. Total damage: $4,788. Token cost of those API calls: under $1. The root cause wasn't the model — it was four missing controls: no circuit breaker for consecutive failures, no aggregate velocity monitoring, no balance-based spending limit, and a latency gap between authorization and transaction history updates [[Proxy, Jan 2026](https://www.useproxy.ai/blog/ai-agent-overspend-postmortem); note: Proxy is a virtual-cards vendor; incident details anonymized but figures published].

**The zero-click exploit.** [CVE-2025-32711](https://nvd.nist.gov/vuln/detail/CVE-2025-32711) documents an AI command injection vulnerability in a shipping enterprise product. The EchoLeak exploit chain achieved full privilege escalation across LLM trust boundaries without user interaction — five chained bypasses evading cross-prompt-injection classifiers, circumventing link redaction, exploiting auto-fetched images, and abusing a proxy service [[Reddy & Gujral 2025](https://arxiv.org/abs/2509.10540), published at AAAI Fall Symposium 2025]. This is a catalogued CVE, not a theoretical risk.

**The compound failure surface.** In a two-week controlled lab study, autonomous agents with persistent memory, email, Discord, file systems, and shell access produced eleven representative failure categories: unauthorized compliance with non-owners, data disclosure, destructive system-level actions, denial-of-service, identity spoofing, and cross-agent propagation of unsafe behavior. In several cases, agents reported successful task completion while the system state contradicted their reports [[Shapira et al. 2026](https://arxiv.org/abs/2602.20021), preprint; lab environment, not production].

The shared pattern across these incidents is that each failure was a *control* failure, not a *capability* failure. The models performed their instructions. The surrounding systems — spending limits, input sanitization, privilege boundaries, state verification — weren't engineered for autonomous operation.

The Incident Tax scales with autonomy level. A Level 2 agent (human reviews every output before external action) has low incident exposure — errors are caught before they reach customers or systems. A Level 3 agent (autonomous within policy bounds) has exposure proportional to its action surface area, because outputs bypass human review. The relationship isn't linear — it's combinatorial, because failures compound across tool access, persistent state, and multi-party communication.

---

## The Governance Tax

This is the tax that's hardest to measure — and that's part of the finding.

Deloitte's survey found that 74% of organizations intend to deploy agentic AI at scale, but only 21% have a mature AI governance model in place [[Deloitte 2026](https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/services/consulting/2026/state-of-ai-2026.pdf)]. A separate security survey found that only 21% of enterprises have full visibility into the actions their AI agents take [[Akto 2025](https://www.prnewswire.com/news-releases/aktos-2025-state-of-agentic-ai-security-report-finds-only-21-of-enterprises-have-visibility-302635105.html); note: survey weighted toward security-conscious organizations]. Even among companies actively deploying agents, the governance infrastructure lags deployment by quarters or years.

The Governance Tax has three components, and the operational one matters most:

**Regulatory compliance** is the most visible. The EU AI Act (Regulation 2024/1689) entered force August 1, 2024, with staged application through 2027. The [General-Purpose AI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/ai-code-practice) details transparency, copyright, and systemic-risk responsibilities for GPAI providers, and the [AI Pact](https://digital-strategy.ec.europa.eu/en/news/ai-pact-marks-one-year-progress-trustworthy-ai-europe) reports 3,265 participating organizations with over 230 voluntary pledgers actively engaged [EU AI Office, Feb 2026]. In the US, the [NIST AI RMF Playbook](https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook) provides a voluntary governance framework structured into Govern, Map, Measure, and Manage functions [NIST; continuously updated].

**Observability infrastructure** is the operational cost that organizations consistently underestimate. An agent pipeline without tracing, token accounting, and action logging is unauditable — and therefore ungovernable. OpenTelemetry's GenAI semantic conventions offer an emerging standard, but adoption is early. Tooling costs are non-trivial: [LangSmith](https://www.langchain.com/pricing-langsmith) starts at $39/seat/month for Plus (with free developer seats available), and [Braintrust](https://www.braintrust.dev/pricing) starts at $249/month for Pro. For a 10-person engineering team running three agent pipelines, observability tooling alone can run $5,000–$15,000/year before accounting for integration engineering time. And that covers only *visibility* — not the analyst or engineer hours to actually review traces, investigate anomalies, and maintain dashboards.

**Expert staffing** — the compliance, legal, and security personnel required to review agent behaviors, audit trails, and incident reports — is the component nobody has published a cost study on. No published study quantifies per-agent governance cost in FTE-hours or dollars. So treat Governance Tax as an immediate measurement problem: track governance-hours per workflow per month across trace review, incident root-cause analysis, compliance documentation, and audit preparation. This converts governance from an abstract concern into a measurable cost line item. **The measurement gap is itself a finding:** organizations are deploying agents faster than they can quantify the governance overhead.

---

## The Decision Rule: Level 2.5 vs Level 3

Not all autonomy levels carry the same tax burden. Before the detailed taxonomy, use this executive decision flow:

1. If any single tax score is 4 or 5, block the workflow until mitigation reduces that tax below 4.
2. For non-blocked workflows, compute `NetScore = Benefit - Average(HB, Incident, Governance)`.
3. Level 3 is allowed only when `NetScore > 0` and both `Incident Tax <= 2` and `Governance Tax <= 2`.

Here is the practical taxonomy, consistent with both [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) and [OpenAI](https://developers.openai.com/tracks/building-agents/) published framework guidance and calibrated against the MAP study's production data:

| Level | Architecture | What AI controls | What's hardcoded / human-owned | Review gate | Tax profile |
|---|---|---|---|---|---|
| **1 — Copilot** | Single LLM call + tools | Response content | Everything else | N/A (human executes) | Minimal |
| **2 — Pipeline** | Linear chain of LLM calls | Each step's reasoning (single-turn) | Pipeline sequence, routing, tool access | Human reviews outputs before external action | Moderate HB Tax; low Incident Tax |
| **2.5 — Artifact pipeline** | Linear chain of multi-turn ReAct agents | Each node's local reasoning, tool use, and iteration across multiple turns | Pipeline sequence, routing; each node's I/O contract | Human review at predetermined decision points | Moderate and predictable across all three taxes |
| **3 — Autonomous** | Dynamic graph or policy engine | Routing between agents, task planning, external actions | Available tools, safety constraints | Policy engine only; outputs reach external systems directly | All three taxes fully active, scaling with action surface |
| **4 — Fully autonomous** | Decentralized / event-driven (actor model) | Agent spawning, inter-agent communication, emergent coordination | Almost nothing | None | Maximum on all axes; no known enterprise production deployment as of early 2026 |

**The Level 2 → 2.5 distinction matters for tax exposure.** In a Level 2 pipeline, each node makes a single LLM call — the blast radius is small and the output is easy to review. In a Level 2.5 pipeline, each node runs a multi-turn ReAct loop with tool access (filesystem, APIs, shell commands), producing richer outputs but with a larger action surface per step. The control comes from two architectural constraints: first, the pipeline sequence itself is fixed and deterministic — no node chooses which node runs next. Second, each node reads a defined structured input and produces a defined structured output (a JSON payload, a markdown document, a typed schema). Only that artifact crosses the node boundary — no conversation history, no context pollution. Human review gates sit at predetermined decision points rather than on every output. The result is a system where seniors review at gates rather than on every action, the blast radius of any single node failure is bounded by its output contract, and the audit trail is a sequence of typed artifacts rather than opaque chat logs.

The architecture decision should be driven by tax exposure:

| Condition | Level 2.5 (pipeline + gates) | Level 3 (autonomous) |
|---|---|---|
| Error cost per incident | > $100 or reputational | < $10 and recoverable |
| Expert review pool | Small / expensive | Large / available |
| Task variance | Low to medium | High |
| Regulatory exposure | Any | Minimal |
| Action reversibility | Low | High (undo available) |

**The decision rule:** Apply circuit breaker first. For non-blocked workflows, use net score for ranking. Promote to Level 3 only when net score is positive and both Incident and Governance tax remain low (<=2). In most enterprise contexts in 2026, that condition is not met.

### The Autonomy Tax Scorecard

Use this to evaluate your top three candidate workflows. **This is a structured decision-making heuristic, not a predictive model.** The value is in forcing explicit estimation of each tax rather than hand-waving about "AI readiness."

#### Scoring Rubric

Use these anchors to calibrate scores consistently across teams:

| Score | Human Bandwidth Tax | Incident Tax | Governance Tax |
|---|---|---|---|
| **1** | No expert review needed; output is internal/low-stakes | Errors are invisible or cost < $1 to fix | No regulatory exposure; internal use only |
| **2** | Light review; seniors spot-check < 10% of outputs | Errors cost $1–$50; easily reversible | Minimal compliance; standard data handling |
| **3** | Moderate review; seniors review 10–50% of outputs | Errors cost $50–$500; partially recoverable | Moderate compliance; PII or financial data involved |
| **4** | Heavy review; seniors review > 50% of outputs | Errors cost $500–$5,000 or reputational damage | Regulated domain; audit trail required |
| **5** | Every output requires expert validation before use | Errors cost > $5,000 or legal/regulatory exposure | Heavily regulated; SOC 2/AI Act obligations apply |

#### Step 1 — Circuit breaker

Before calculating any net score: if any single tax scores ≥ 4, the workflow is **BLOCKED** until you have a documented mitigation plan that would reduce that tax below 4. This is not a footnote — it is the primary safety mechanism.

#### Step 2 — Net score

For workflows that pass the circuit breaker: `Net = Benefit - Average(three taxes)`.

Use `Net` only for ranking non-blocked candidates. A workflow is Level 3-eligible only when `Net > 0` and both Incident and Governance tax are <= 2; otherwise default to Level 2.5 (or Level 2 if manual approval is required at every external action).

| Workflow | Benefit (1–5) | HB Tax (1–5) | Incident Tax (1–5) | Gov Tax (1–5) | Circuit Breaker | Net Score | Level |
|---|---|---|---|---|---|---|---|
| *Support refund triage* | 4 | 3 | 2 | 2 | ✅ Pass | +1.67 | Level 2.5 |
| *Internal log classification* | 3 | 1 | 1 | 1 | ✅ Pass | +2.00 | Level 3 |
| *Procurement approval* | 5 | 4 | 5 | 4 | 🛑 BLOCKED (Incident=5, HB=4, Gov=4) | — | Requires mitigation |
| Your workflow 1 | | | | | | | |
| Your workflow 2 | | | | | | | |
| Your workflow 3 | | | | | | | |

### Tax Sensitivity by Error Cost

Use this table as a quick-reference for how error economics should drive your autonomy-level decision:

| Error cost per incident | Incident Tax weight | Expert review pool | Implied max autonomy | Rationale |
|---|---|---|---|---|
| **Low** (< $10, reversible) | 1–2 | Any | Level 3 viable | Error cost < review cost at volume; automation wins on pure economics |
| **Medium** ($10–$500, partially recoverable) | 3 | Adequate | Level 2.5 with monitoring | Human gates at key decision points keep expected loss bounded |
| **High** (> $500 or reputational/regulatory) | 4–5 | Scarce or expensive | Level 2 or Level 2.5 with gates | Single-incident cost can exceed cumulative throughput savings |

---

## When Level 3 Wins: The Anti-Thesis

This framework has a scope condition, and intellectual honesty demands stating it.

Level 3 autonomy can be economically rational even with immature controls when three conditions hold simultaneously: **(1)** individual error cost is low and bounded (< $10 per incident), **(2)** volume is high enough that human review would cost more than errors do, and **(3)** actions are reversible within a defined time window.

The clearest public example is Klarna's AI assistant, which handled 2.3 million customer service conversations in its first month — two-thirds of all chats — reportedly doing the work of 700 full-time agents and contributing $40 million in estimated profit improvement [[Klarna, Feb 2024](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/); note: self-reported figures, not independently audited].

To illustrate the boundary condition, consider a sensitivity analysis using Klarna-scale parameters. *All inputs below are illustrative — Klarna has not published error rates, remediation costs, or per-review costs. The purpose is to show how the economic logic shifts across assumptions, not to claim any specific threshold as universal.*

Formal boundary condition:

`Level 3 is economically viable when C_review > (p_error * C_error + C_incident_response).`

Where `C_review` is expected human-review cost per unit at your target volume, `p_error` is unreviewed error probability, `C_error` is expected remediation cost per error, and `C_incident_response` is expected incident handling cost per unit.

| Parameter | Low estimate | Mid estimate | High estimate |
|---|---|---|---|
| Daily volume | 50,000 | 75,000 | 100,000 |
| Error rate (unreviewed) | 1% | 2% | 5% |
| Avg error remediation cost | $2 | $5 | $15 |
| Per-conversation human review cost | $0.50 | $0.80 | $1.20 |

| Scenario | Daily review cost | Daily error cost (unreviewed) | Ratio | Level 3 economic case |
|---|---|---|---|---|
| Low vol, low error, low cost | $25,000 | $1,000 | 25:1 | Strong |
| Mid vol, mid error, mid cost | $60,000 | $7,500 | 8:1 | Strong |
| High vol, high error, high cost | $120,000 | $75,000 | 1.6:1 | Marginal |

The pattern: when review cost substantially exceeds expected error cost, Level 3 wins on pure economics even if controls aren't mature. When error rates climb or remediation is expensive, the case collapses. The exact threshold depends on your inputs — run the numbers with your own estimates before deciding. The purpose of this table is not to give a magic ratio, but to show that the decision is *calculable* rather than intuitive.

But notice the conditions: low individual error cost, high reversibility, minimal regulatory exposure. Most enterprise processes that leaders *want* to automate with agents — procurement, compliance review, legal analysis, financial approvals — violate at least two of those conditions. A procurement agent that approves one wrong $5,000 invoice wipes out the savings from 1,000 correct ones. The Klarna case is instructive but not generalizable to the enterprise workflows where the Autonomy Tax bites hardest.

---

## Three Things to Do Monday

These are not aspirational. Each has a concrete deliverable.

**1. Score your top three workflows.** Fill out the Autonomy Tax Scorecard above for your three highest-priority agent candidates. Output: a one-page ranked table with a recommended architecture level for each. Time: one meeting.

**2. Instrument your most expensive LLM workflow.** Add four counters to your most critical agent-facing API integration: retry rate, external-action rate, human-escalation rate, and review-time-per-output. Use OpenTelemetry GenAI semantic conventions if your stack supports them. Output: a baseline dashboard. Time: one sprint.

**3. Measure your expert review burden.** For one sprint, ask your senior engineers to log time spent reviewing, correcting, or reverting AI-generated outputs. Calculate: what percentage of senior engineering time is going to AI output validation? Output: a baseline number. Most teams don't have one and will be surprised by how high it is.

---

## The 2027 Prediction

By December 2027, most failed enterprise agent rollouts will be attributed to control-layer failures — observability gaps, governance deficits, action-guardrail failures, and expert review bottlenecks — rather than to base-model capability gaps.

**What would disprove this:** Any of the following would constitute substantive counter-evidence: (1) an independent post-mortem dataset (e.g., from a consulting firm, insurer, or industry consortium) showing model accuracy as the primary root cause in >50% of enterprise agent failures; (2) a peer-reviewed study demonstrating that improved model capability *reduces* rather than shifts control-layer costs; or (3) widespread enterprise adoption of Level 3+ agents in regulated domains without corresponding investment in observability and governance. If these emerge by December 2027, this thesis is wrong.

We suspect they won't, because the Autonomy Tax scales *with* autonomy. Better models enable more autonomy, which increases the control surface, which raises all three taxes. The taxes don't shrink as models improve — they shift.

---

## Appendix: Method, Sources, and Limitations

### Source Classification

This article draws from 81 collected sources classified into five tiers:

| Tier | Description | Examples used | Confidence |
|---|---|---|---|
| **1** | Peer-reviewed, major institutions, government data | NBER w31161, EU AI Act text, NVD CVE database | High |
| **2** | Major consulting firms, large-sample industry surveys | Deloitte 2026, McKinsey 2025 | Medium-high; note potential respondent bias |
| **3** | Preprints, working papers, conference presentations | MAP study, Xu et al., Song et al., METR, Agents of Chaos | Medium; findings not yet peer-reviewed |
| **4** | Vendor publications, product documentation, self-reported metrics | Anthropic, Klarna, Proxy, pricing pages | Use with explicit caveats; vendor incentive bias |
| **5** | Frameworks, standards, guidelines | NIST AI RMF, OWASP Top 10, OpenTelemetry | Reference material; not evidence claims |

### Key Limitations

- **No original data, one original synthesis.** Every empirical claim in this article cites published research. We have conducted no original surveys, interviews, or experiments. The originality contribution is the framework and a structured synthesis artifact: the [Autonomy Tax Casebook](./sources/derived/autonomy_tax_casebook.tsv), which codes 28 public records (incidents, field studies, regulatory milestones, and tooling baselines) into a normalized schema with source-tier and confidence ratings. Method notes and coding criteria are documented in [autonomy_tax_casebook_method.md](./sources/derived/autonomy_tax_casebook_method.md). (These are internal repository links and should be replaced with public URLs in the Substack publication version.)
- **Domain bridging.** The Human Bandwidth Tax thesis bridges findings from customer support (NBER), enterprise development (Xu et al.), and open-source projects (Song et al.). The common mechanism (AI raises output faster than review capacity) is plausible but not directly demonstrated in a single study.
- **Governance Tax measurement gap.** We explicitly flag that the Governance Tax is the least empirically measured of the three taxes. No published study quantifies per-agent governance cost.
- **Geographic scope.** This analysis reflects US/EU regulatory and market conditions. Self-hosted, open-weight, and non-Western deployments carry different tax structures.
- **Temporal snapshot.** Source data captured in February 2026. Pricing, regulatory status, and capability benchmarks will shift.

### Autonomy Tax Subcomponents (extended)

For teams that want finer-grained analysis, the three taxes decompose further:

| Tax | Subcomponents |
|---|---|
| Human Bandwidth Tax | Expert review time, rework rate, coordination overhead, quality-gate throughput |
| Incident Tax | Direct financial loss, remediation cost, reputational damage, investigation time |
| Governance Tax | Compliance staff, audit tooling, observability infrastructure, regulatory reporting |

### Full Citation List

All sources referenced in this article with URLs, DOIs, and access dates are available in the [source manifest](sources/source_manifest.tsv). Key citations by section are listed below.

**§1 Hook:** Proxy post-mortem (SRC-026); Xu et al. arXiv:2510.10165 (SRC-050); Song et al. arXiv:2410.02091 (SRC-049).

**§2 Deployment Paradox:** Deloitte 2026 (SRC-007); McKinsey 2025 (SRC-008); Anthropic agent autonomy (SRC-009); Pan et al. MAP study arXiv:2512.04123 (SRC-073); Kwa et al. METR arXiv:2503.14499 (SRC-039).

**§3 Human Bandwidth Tax:** Brynjolfsson et al. NBER w31161 (SRC-060); Xu et al. arXiv:2510.10165 (SRC-050); Song et al. arXiv:2410.02091 (SRC-049).

**§4 Incident Tax:** Proxy post-mortem (SRC-026); NVD CVE-2025-32711 (SRC-012); EchoLeak arXiv:2509.10540 (SRC-076); Shapira et al. Agents of Chaos arXiv:2602.20021 (SRC-075).

**§5 Governance Tax:** Deloitte 2026 (SRC-007); Akto 2025 (SRC-010); EU AI Act (SRC-020–022); NIST AI RMF (SRC-032, SRC-066); LangSmith (SRC-018); Braintrust (SRC-019); OpenTelemetry GenAI (SRC-038).

**§6 Decision Rule:** Anthropic building agents (SRC-072); OpenAI building agents (SRC-071); Pan et al. MAP study (SRC-073).

**§7 Anti-Thesis:** Klarna press release (SRC-013).

**§9 Prediction:** Structural argument; no single source.
