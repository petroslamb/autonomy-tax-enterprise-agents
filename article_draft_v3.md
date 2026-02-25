# AI Agents in the Enterprise: What Ships, What Breaks, and What It Costs

*A field guide for AI engineering practitioners, researchers, and CTOs — February 2026*

**By Rooted Layers** · *AI insights grounded on research*

---

## I. The State of the Field

Among the clearest signals in the current enterprise AI landscape is the gap between *intent* and *deployment*. Deloitte's 2026 State of AI survey, conducted across 3,235 director-to-C-suite leaders in 24 countries, found that 23% of companies are using agentic AI at least moderately today, up from 26% who were merely exploring it a year earlier. Within two years, 74% expect to be using it at moderate levels or above [[Deloitte 2026, n=3,235](https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/services/consulting/2026/state-of-ai-2026.pdf)].

The intent is clear. The execution is not.

Multiple surveys paint a consistent picture of where agent adoption actually lands in practice. According to a vendor-published survey from Akto, 38.6% of respondents report deployed agents at department or enterprise scale — but only 21% report full visibility into what those agents are doing [Akto 2025; note: Akto is an agent security vendor; sample methodology not independently verified]. Deloitte's independent findings corroborate the governance gap: just 21% of companies surveyed report having a mature governance model for autonomous agents [Deloitte 2026, n=3,235].

Meanwhile, AI adoption broadly — not agentic AI specifically — has reached wide penetration. McKinsey's 2025 global survey reports 88% of organizations using AI in at least one function, though majority usage remains in experiment or pilot stages [McKinsey 2025; note: this figure covers all AI, not agents specifically].

Where agents *have* shipped to production at scale, the concentration is striking. Anthropic's analysis of 998,481 tool calls on its public API found that software engineering accounts for nearly 50% of all agentic activity. Beyond coding, business intelligence, customer service, and e-commerce each represent single-digit percentages [Anthropic "Measuring Agent Autonomy," Feb 2026, n=998K tool calls]. On Anthropic's platform at least, the dominant pattern is a developer talking to a coding assistant — not an autonomous system running a business process.

The most comprehensive survey of production agent deployments to date confirms this conservative picture. In a systematic study covering 20 case studies and 306 practitioners across 26 domains, 68% of production agents execute ten or fewer steps before human intervention. Seventy percent rely on prompting off-the-shelf models rather than weight tuning, and 74% depend primarily on human evaluation. Reliability — consistent correct behavior over time — remains the top development challenge [[Pan et al. 2026, arXiv:2512.04123](https://arxiv.org/abs/2512.04123), preprint, n=306 practitioners + 20 case studies]. The implication is clear: what ships in production is far simpler than what framework demos suggest.

The exception that proves part of the pattern is Klarna, which reported that its AI assistant handled 2.3 million conversations in its first month — two-thirds of all customer service chats — doing the equivalent work of 700 full-time agents and contributing an estimated $40 million in profit improvement [Klarna press release, Feb 2024; note: self-reported figures, not independently audited]. An independent field study provides a more grounded anchor. In data covering 5,179 customer support agents, access to a generative AI assistant increased issues resolved per hour by 14% on average, with larger gains (34%) for novice and lower-skilled workers and minimal impact on experienced, highly skilled performers [[Brynjolfsson et al. 2023, NBER w31161](https://doi.org/10.3386/w31161), n=5,179]. Importantly, this study measured AI-assisted human workers, not autonomous agents — but the productivity pattern offers a useful baseline: early enterprise value comes from standardizing best-practice execution across the workforce, not from replacing top performers.

These three data points — software engineering concentration, constrained production agent design, and AI-assisted productivity gains skewing toward novices — converge on the same picture. The technology delivers measurable value when tightly scoped and well-supervised. The open question is what happens when organizations push beyond those boundaries.

**The practical question for 2026 is not whether agents work — they do, in narrow, well-instrumented domains — but whether organizations can govern, monitor, and cost-manage them as they scale beyond coding tools into higher-stakes workflows.**

---

## II. A Practical Taxonomy of Agent Maturity

A practical four-level taxonomy has emerged across practitioner discourse and framework documentation, though no single standards body has formalized it. We present it here as a useful mental model, not as an industry standard.

**Level 1: Copilots.** A human types, an LLM responds. Autocomplete, chat-based Q&A, inline code suggestions. The human remains in the loop for every action. Most deployed enterprise AI sits here.

**Level 2: Linear pipelines.** A fixed sequence of LLM calls processes a task — for example, extract → classify → summarize. No branching, no dynamic routing. Deterministic enough to test, cheap enough to run. The workhorse of production deployments.

**Level 2.5: Artifact-passing pipelines.** Agents hand off structured artifacts (JSON, code diffs, evaluation reports) rather than unstructured text. Each agent in the pipeline reads and writes to a defined interface. This is where reliability and debuggability start to emerge, because you can inspect every handoff point.

**Level 3: Dynamic multi-agent systems.** Agents spawn subtasks, route to specialists, coordinate shared state. Frameworks like LangGraph, CrewAI, and Anthropic's Agent SDK operate here. The surface area for failure modes expands significantly.

**Level 4: Autonomous agents.** Systems that set their own goals, manage their own resources, and operate with minimal human oversight. We are not aware of public examples of customer-facing Level 4 deployments in enterprise settings.

Available surveys suggest most production deployments visible so far are concentrated in Levels 1-2. The MAP study's finding that 68% of production agents execute ten steps or fewer reinforces this: most shipped agents are tightly scoped, human-supervised systems, not open-ended autonomous reasoners. The interesting design question for 2026 is not "how do we reach Level 4?" but "when does Level 2.5 suffice, and when does the complexity of Level 3 actually pay for itself?"

Both Anthropic and OpenAI now publish convergent guidance that supports a conservative architecture path. Anthropic explicitly recommends "finding the simplest solution possible, and only increasing complexity when needed," distinguishing predefined workflows from autonomous agents and noting that "agentic systems often trade latency and cost for better task performance." OpenAI similarly frames agent design as composition across models, tools, state, and orchestration, advising developers to "start experimenting with a flagship model" and scale up only when use-case complexity demands it [Anthropic engineering blog; OpenAI developers track, Feb 2026].

**[EDITORIAL]** In our assessment, the artifact-passing discipline of Level 2.5 handles a large share of real enterprise workflows more reliably, at lower cost, and with simpler debugging than dynamic multi-agent systems. The burden of proof should be on anyone choosing Level 3+ to demonstrate why the workflow *requires* dynamic routing.

---

## III. What It Actually Costs

Cost transparency has been one of the weakest areas in enterprise agent discourse. The title of this article promises cost clarity; here is our best attempt, built from verified pricing data and explicit token math.

### Current API Pricing (February 2026)

| Provider | Model | Input | Output | Source |
|---|---|---|---|---|
| Anthropic | Claude Sonnet 4.6 | $3/MTok | $15/MTok | [Anthropic pricing page](https://docs.anthropic.com/en/docs/about-claude/pricing), captured Feb 2026 |
| Anthropic | Claude Haiku 4.5 | $1/MTok | $5/MTok | Same |
| Anthropic | Claude Opus 4.6 | $5/MTok | $25/MTok | Same |
| OpenAI | GPT-5.2 | $1.75/MTok | $14/MTok | [OpenAI pricing page](https://openai.com/api/pricing/), captured Feb 2026 |
| OpenAI | GPT-5 mini | $0.25/MTok | $2/MTok | Same |

### Example Workflow Costs — With the Math Shown

The following estimates use these stated assumptions:

1. **Input:output ratio = 80:20.** System prompts, tool results, and accumulated context dominate input tokens; agent reasoning outputs are shorter.
2. **"Tokens per run"** = total across all LLM calls in one pipeline execution (3-10 API calls depending on pipeline depth), not a single API call.
3. All estimates are **order-of-magnitude**. Actual costs vary with prompt engineering, tool count, retry behavior, and context accumulation across pipeline hops.

**Workflow 1: Customer support triage (single-turn, Level 1)**
- Model: Haiku 4.5
- Tokens/run: ~3,700 total (est. 3,000 input + 700 output)
- Volume: 10,000 conversations/month
- **Math:** (30M × $1/MTok) + (7M × $5/MTok) = $30 + $35 = **~$65/month**

**Workflow 2: Code review pipeline (3 agents, 2 review loops, Level 2.5)**
- Model: Sonnet 4.6
- Per-run breakdown: Triage (5K in/2K out) → Coder (10K in/5K out) → Reviewer (15K in/3K out) → Revision (15K in/4K out) → Re-review (18K in/3K out)
- Tokens/run: ~63K input + ~17K output = ~80K total
- Volume: 500 runs/month
- **Math:** (31.5M × $3/MTok) + (8.5M × $15/MTok) = $94.50 + $127.50 = **~$222/month**

**Workflow 3: Dynamic research agent (Level 3, ~10 LLM calls avg)**
- Model: Opus 4.6
- Tokens/run: ~200K input + ~40K output = ~240K total (context accumulates across calls)
- Volume: 100 runs/month
- **Math:** (20M × $5/MTok) + (4M × $25/MTok) = $100 + $100 = **~$200/month**

These are API costs only. They do not include infrastructure (orchestration, observability, vector databases), engineering time, or the cost of *what the agent does with its outputs* — which, as we'll see in the next section, can be orders of magnitude larger.

### Where the Real Money Burns

The Proxy post-mortem illustrates a failure pattern where API token costs are trivial but downstream costs are catastrophic. A procurement agent deployed by a mid-sized SaaS company entered a retry loop when a vendor's checkout API returned inconsistent responses. Between 2:47 PM and 2:50 PM, it submitted 12 purchase requests at $399 each — every one approved by the policy engine, which evaluated transactions individually without velocity checks. Total damage: **$4,788 in 3 minutes** [Proxy, Jan 2026; note: Proxy is a virtual-cards vendor; incident details anonymized but timeline and dollar figures published].

The token cost of those 12 API calls was negligible — likely under $1 in LLM inference. The damage came from what the agent *did* with those calls: it spent real money, on a real corporate card, without circuit breakers.

This distinction matters for cost planning. The dangerous cost vector for enterprise agents is not model inference — it is **uncontrolled downstream actions**: API calls to payment systems, database writes, customer-facing communications, and infrastructure provisioning. A cost model that tracks only token spend will miss the highest-risk category entirely.

---

## IV. Four Failure Modes — And What Red-Teaming Reveals

### Failure Mode 1: The Retry Loop

The Proxy incident described above is the canonical example. Root cause analysis identified four contributing factors: (1) the agent lacked circuit breakers for consecutive failures; (2) the vendor API returned inconsistent responses; (3) the policy engine evaluated each transaction individually with no memory of recent approvals; (4) there was a latency gap between authorization and transaction history updates [Proxy, Jan 2026].

**Mechanism:** Any agent with access to a rate-unlimited external API and no exponential backoff or failure-count circuit breaker is vulnerable. The compound cost grows linearly or worse with each retry.

**Mitigation:** Hard spending limits (balance-based, not policy-based), circuit breakers (halt after N consecutive failures), and aggregate velocity monitoring (how much has this agent spent in the last N minutes?).

### Failure Mode 2: Prompt Injection in Production

In 2025, NIST published CVE-2025-32711: an AI command injection vulnerability in Microsoft 365 Copilot that allowed unauthorized information disclosure over the network [NVD, CVE-2025-32711]. This is not a theoretical risk — it is a catalogued vulnerability with a CVE number in a shipping enterprise product. The full exploit chain is detailed in the EchoLeak case study, which documents how five chained bypasses — evading Microsoft's cross-prompt-injection classifier, circumventing link redaction, exploiting auto-fetched images, and abusing a Teams proxy — achieved full privilege escalation across LLM trust boundaries without user interaction [Reddy & Gujral 2025, arXiv:2509.10540, published at AAAI Fall Symposium 2025].

**Mechanism:** An adversary crafts input that causes the agent to execute unintended actions — exfiltrating data, modifying records, or escalating privileges. In multi-agent systems, a single compromised agent can propagate malicious instructions to downstream agents through shared context.

**Mitigation:** Input sanitization at every agent boundary, not just the user-facing entry point. Principle of least privilege for every tool an agent can access. Audit trails that capture the full chain of agent actions. Deloitte's survey found that data privacy and security is the #1 AI risk concern (73% of respondents), well ahead of governance capabilities (46%) [Deloitte 2026, n=3,235].

### Failure Mode 3: Context Window Pollution

As agents accumulate context across multi-step pipelines, the quality of information in the context window degrades. Irrelevant tool outputs, failed attempt logs, and stale state from earlier pipeline stages crowd out the signal that the current agent needs. A study examining code review workflows found that 59.4% of tokens consumed were in review and iteration cycles — not in the primary task execution [Zenodo "Tokenomics" paper].

**Mechanism:** Each agent in a multi-hop pipeline reads the accumulated context of all prior agents. By hop 5-6, the context may contain more noise than signal. The LLM has no way to distinguish "this is a current instruction" from "this is a failed attempt from three steps ago."

**Mitigation:** Artifact-passing architecture (Level 2.5) — each agent reads only a defined structured input and writes only a defined structured output. The accumulated context problem is an argument *for* simpler pipeline architectures, not against them.

### Failure Mode 4: Compound Autonomous Failures

A live red-teaming study deployed autonomous agents with persistent memory, email, Discord, file systems, and shell access in a controlled lab over two weeks. Researchers documented eleven representative failure cases including unauthorized compliance with non-owners, disclosure of sensitive data, destructive system-level actions, denial-of-service conditions, identity spoofing, and cross-agent propagation of unsafe behavior. In several cases, agents reported task completion while the underlying system state contradicted those reports [[Shapira et al. 2026, arXiv:2602.20021](https://arxiv.org/abs/2602.20021), preprint; note: lab environment, not production deployment].

**Mechanism:** These failures emerge not from any single vulnerability but from the *combination* of autonomy, persistent state, tool access, and multi-party communication. Each capability is individually manageable; their intersection creates a failure surface that no single guardrail covers.

**Mitigation:** The combination argues for the same principle as Level 2.5 architecture: minimize the surface area of autonomous tool access to what the task strictly requires, and treat persistent cross-agent state as a privilege to be earned through demonstrated reliability, not a default.

### Emerging Mitigations: From Guardrails to Policy Reasoning

Mitigation research is shifting from static prompt guardrails toward policy-reasoning safety layers that evaluate agent action trajectories before execution. ShieldAgent proposes explicit policy verification through structured rule circuits, reporting state-of-the-art safety detection (+11.3% over prior methods, 90.1% recall) while reducing inference overhead by 58% [Chen et al. 2025, arXiv:2503.22738, preprint]. While still a research prototype, the approach suggests a path toward auditable, enforceable agent guardrails that can be verified against organizational policy documents.

---

## V. The Enterprise Scaffolding Problem

Deploying an agent is 20% of the work. The other 80% is the scaffolding around it: orchestration, observability, evaluation, access control, and compliance.

### Orchestration

Any multi-step agent pipeline needs durable execution — the ability to retry failed steps, maintain state across long-running workflows, and handle timeouts gracefully. The market has split into three tiers:

| Category | Examples | Starting Price | Trade-off |
|---|---|---|---|
| Workflow engines (general) | Temporal Cloud, Inngest | Temporal: from $100/mo (Essentials plan) | High reliability, steeper learning curve |
| Agent-native orchestration | Restate Cloud, Hatchet | Restate: from $75/mo (Starter) | Lower complexity, narrower ecosystem |
| Framework-embedded | LangGraph, CrewAI, Anthropic Agent SDK | Open-source / usage-based | Lowest barrier, tightest vendor coupling |

*[EDITORIAL] The pricing data above is sourced from official vendor pricing pages captured in February 2026. The trade-off assessments are our editorial judgment based on documentation review and architectural analysis.*

### Observability

You cannot govern what you cannot see. The Akto survey found only 21% of enterprises have full visibility into agent actions — and this from a sample weighted toward security-conscious organizations [Akto 2025].

| Tool | Free Tier | Paid Starting At | Source |
|---|---|---|---|
| LangSmith | $0 developer seat | Plus: $39/seat/mo | [LangSmith pricing](https://www.langchain.com/pricing), Feb 2026 |
| Braintrust | Free tier available | Pro: $249/mo | [Braintrust pricing](https://www.braintrust.dev/pricing), Feb 2026 |

*[EDITORIAL] For teams with frontend engineering capacity, building a custom trace viewer on top of OpenTelemetry is viable and removes vendor lock-in, though it requires significant upfront investment. We have no independent data on how long this takes.*

### AgentOps: From Ad Hoc to Lifecycle

The operational management of agent systems is maturing into an explicit discipline. AgentOps formalizes the lifecycle as four stages — monitoring, anomaly detection, root-cause analysis, and resolution — with anomalies categorized into intra-agent failures (tool misuse, hallucinated actions, reasoning drift) and inter-agent failures (coordination breakdowns, conflicting state, message propagation errors) [Wang et al. 2025, arXiv:2508.02121, preprint]. The distinction matters because the tools that catch intra-agent failures (trace-level logging, assertion checks) are fundamentally different from those that catch inter-agent failures (pipeline-level state diffing, message provenance tracking). For organizations scaling from a single agent to multi-step pipelines, adopting this lifecycle framing early prevents the common pattern of retroactively bolting observability onto systems that were never designed for it.

### Compliance and Governance

Regulatory pressure is shaping enterprise agent deployment. The EU AI Act (Regulation 2024/1689) entered into force on August 1, 2024, with staged application dates through 2027. The Act's risk-classification framework is likely to apply to AI systems making autonomous decisions that affect individuals, though agent-specific interpretive guidance has not yet been published [EU AI Act text, Regulation 2024/1689].

The EU compliance layer is now moving from static legal text toward operational instruments. The General-Purpose AI Code of Practice details expected handling of transparency, copyright, and systemic-risk responsibilities for GPAI providers, while the AI Pact reports 3,265 participating organizations with over 230 voluntary pledgers actively engaged in pre-enforcement alignment [EU AI Office, Feb 2026]. For governance implementation, the [NIST AI RMF Playbook](https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook) provides a complementary starting point, structuring controls into Govern, Map, Measure, and Manage functions [NIST; note: framework is not agent-specific and is continuously updated]. For enterprise teams, the practical takeaway is that compliance tooling needs to be designed as part of the agent pipeline, not retrofitted after deployment — the same lesson the AgentOps lifecycle teaches for observability.

SOC 2 compliance, governed by AICPA's Trust Services Criteria, requires organizations to demonstrate controls over system access, change management, and processing integrity. Based on the scope of existing Trust Services Criteria, we infer that SOC 2 audit scope is likely expanding to consider agent permissions and action audit trails — though no AI-specific SOC 2 rule has been published, and we have no direct source confirming this expansion in practice [AICPA Trust Services Criteria; editorial inference based on criteria scope].

ISO 42001 provides a management system standard for responsible AI, and organizations deploying autonomous agents in regulated industries should evaluate certification as a governance foundation [NQA ISO 42001 overview].

---

## VI. Software Engineering Dominance — And What Comes Next

The software engineering concentration documented in Section I raises a deeper question: *why* does code dominate agent adoption, and what does that tell us about expansion into other domains?

Three properties make code uniquely amenable to agent automation:

1. **Testability.** You can run the code and verify whether it works. This makes oversight cheap.
2. **Reversibility.** A bad code change can be reverted. A bad purchase, a bad email to a customer, or a bad medical recommendation cannot.
3. **Structured inputs and outputs.** Code diffs, test results, and compiler errors are machine-readable. Customer interactions, legal documents, and financial decisions are not.

The implication is that agent expansion into non-engineering domains will not simply be "more of the same." Each new domain requires solving the oversight problem from scratch — and the NBER study's finding that AI-assisted gains concentrate among novice workers, while experienced workers see minimal improvement, suggests that the value curve has different shapes in different fields. Anthropic's own analysis noted: "Whether the adoption curve in software engineering will repeat in other domains is an open question. Software is comparatively easy to test and review... In domains like law, medicine, or finance, verifying an agent's output may require significant effort, which could slow the development of trust" [Anthropic, Feb 2026].

Klarna's customer service deployment offers one data point for how this might unfold: structured transactions (refunds, returns, rebooking) with well-defined success criteria and human escalation paths [Klarna, Feb 2024]. But even Klarna's results are self-reported and represent a company that was already aggressive about AI adoption before agents existed.

---

## VII. The Boring Stack Thesis

**[EDITORIAL]** This section represents our editorial position, informed by the evidence discussed above but going beyond what any single source demonstrates.

The most effective enterprise agent architectures in 2026 share a pattern we call the "Boring Stack." They are:

- **Level 2.5, not Level 4.** Artifact-passing pipelines with structured handoffs, not autonomous systems with dynamic routing.
- **Built on proven orchestration.** Temporal, Inngest, or similar workflow engines that predate the AI agent hype cycle.
- **Observable by design.** Every LLM call traced, every tool invocation logged, every artifact versioned.
- **Cost-bounded.** Hard limits on spending, circuit breakers on retries, aggregate velocity monitoring on any action with financial or reputational impact.

The appeal of the Boring Stack is precisely its dullness. It doesn't promise autonomy. It promises *predictability* — which, in an enterprise context, is the more valuable property.

The evidence now supports this position from multiple angles. The MAP study's finding that 68% of production agents are capped at ten steps confirms that successful deployments are already converging on constrained designs. The Agents of Chaos red-team demonstrates what happens when autonomy, persistent state, and tool access are combined without constraint: compound failures that no single guardrail catches. And the convergent guidance from both Anthropic and OpenAI — "find the simplest solution possible" — suggests that even the vendors selling the most capable models understand that complexity is a liability, not a feature.

This does not mean Level 3+ is never justified. Dynamic multi-agent systems make sense when the task space is genuinely open-ended (research synthesis, novel code generation in unfamiliar codebases) and when the cost of failure is low enough to tolerate experimentation. But the burden of proof should be on the team choosing the complex architecture to explain why a simpler pipeline cannot do the job.

The institutional pressures framework from organizational theory supports this conservatism. Enterprises adopt technologies under three pressure types: coercive (regulatory requirements), mimetic (copying peers), and normative (professional standards). Much of the current rush to Level 3+ agents appears driven by mimetic pressure — organizations adopting multi-agent frameworks because competitors are, not because their specific workflows require dynamic orchestration [DOI/IT academic framework, institutional theory and diffusion of innovation].

---

## VIII. Looking Forward: Open Questions for 2026

The following questions remain genuinely open. We do not have sufficient evidence to answer them, and we flag them as areas where the field will need to develop data:

1. **When does the agent cost curve cross the human cost curve?** Klarna's $40M figure suggests it already has for high-volume, low-complexity customer service — but this is a single self-reported data point. Broader, independently audited cost comparisons across workflow types do not exist yet.

2. **How will the EU AI Act's risk classification apply to autonomous agents?** The regulation text is in force, but agent-specific guidance has not been published. The classification of an agent that can independently make purchases, send communications, or access personal data is likely to fall under high-risk categories, but this has not been tested in enforcement.

3. **What does the governance maturity curve look like?** Deloitte reports 21% with mature governance today, and 74% planning to deploy agents within two years. If governance does not catch up to deployment, 2027 could produce a wave of governance failures that shapes regulation for a decade.

4. **Will non-engineering domains follow the software engineering adoption curve?** Anthropic's data shows 50% concentration in coding. The second-wave domains (customer service, finance, legal) have fundamentally different oversight properties. The pace of expansion is an empirical question, not a theoretical one.

---

## A Note on Method

This article draws on sources across five tiers:

- **Tier 1 — Research with published methodology:** Anthropic's agent autonomy study (n=998K tool calls), Deloitte's State of AI 2026 (n=3,235), Brynjolfsson et al. NBER w31161 (n=5,179), Pan et al. MAP study (arXiv:2512.04123, n=306 + 20 case studies), CVE-2025-32711 (NVD record), and the EU AI Act regulation text.
- **Tier 1.5 — Peer-presented or systematic preprints:** Shapira et al. "Agents of Chaos" (arXiv:2602.20021, live red-team study), Reddy & Gujral "EchoLeak" (arXiv:2509.10540, AAAI Fall Symposium 2025), Chen et al. "ShieldAgent" (arXiv:2503.22738, benchmark contribution), Wang et al. "AgentOps Survey" (arXiv:2508.02121). All are arXiv preprints; not final peer-reviewed journal versions.
- **Tier 2 — Industry reports and vendor case studies:** McKinsey (AI-general, not agent-specific), Akto (vendor-published survey), Klarna (self-reported press release), Proxy (vendor blog post-mortem), KPMG (consulting firm survey), AWS Q Developer (first-party blog), Anthropic "Building Effective Agents" (engineering blog), and OpenAI "Building Agents" developer track.
- **Tier 3 — Official pricing pages:** Anthropic, OpenAI, Temporal, Restate, LangSmith, and Braintrust, captured February 2026.
- **Tier 4 — Supporting context:** Zenodo "Tokenomics" paper, academic institutional theory framework, AICPA SOC 2 criteria, NQA ISO 42001 overview, NIST AI RMF Playbook, EU AI Office Code of Practice, EU AI Pact progress report.

**Claims are labeled inline:** `[EDITORIAL]` marks positions that go beyond what the cited evidence demonstrates. Vendor-sourced data includes caveats about conflicts of interest and self-reporting. Statistical claims include sample sizes where available.

We deliberately chose to show our token math rather than present cleaned-up cost ranges. If the arithmetic looks tedious, that is intentional — it exists so that readers can verify or challenge our assumptions rather than trusting polished numbers.

---

*Feedback, corrections, and counter-evidence welcome. The purpose of grounded analysis is to be correctable.*
