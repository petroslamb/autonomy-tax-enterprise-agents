# AI Agents in the Enterprise: What Ships, What Breaks, and What It Costs

*A field guide for AI engineering practitioners, researchers, and CTOs — February 2026*

**By Rooted Layers** · *AI insights grounded on research*

---

## I. The State of the Field

Among the clearest signals in the current enterprise AI landscape is the gap between *intent* and *deployment*. Deloitte's 2026 State of AI survey, conducted across 3,235 director-to-C-suite leaders in 24 countries, found that 23% of companies are using agentic AI at least moderately today, up from 26% who were merely exploring it a year earlier. Within two years, 74% expect to be using it at moderate levels or above [Deloitte 2026, n=3,235].

The intent is clear. The execution is not.

Multiple surveys paint a consistent picture of where agent adoption actually lands in practice. According to a vendor-published survey from Akto, 38.6% of respondents report deployed agents at department or enterprise scale — but only 21% report full visibility into what those agents are doing [Akto 2025; note: Akto is an agent security vendor; sample methodology not independently verified]. Deloitte's independent findings corroborate the governance gap: just 21% of companies surveyed report having a mature governance model for autonomous agents [Deloitte 2026, n=3,235].

Meanwhile, AI adoption broadly — not agentic AI specifically — has reached wide penetration. McKinsey's 2025 global survey reports 88% of organizations using AI in at least one function, though majority usage remains in experiment or pilot stages [McKinsey 2025; note: this figure covers all AI, not agents specifically].

Where agents *have* shipped to production at scale, the concentration is striking. Anthropic's analysis of 998,481 tool calls on its public API found that software engineering accounts for nearly 50% of all agentic activity. Beyond coding, business intelligence, customer service, and e-commerce each represent single-digit percentages [Anthropic "Measuring Agent Autonomy," Feb 2026, n=998K tool calls]. Most agentic AI in production today is a developer talking to a coding assistant — not an autonomous system running a business process.

The most prominent exception is Klarna, which reported that its AI assistant handled 2.3 million conversations in its first month — two-thirds of all customer service chats — doing the equivalent work of 700 full-time agents and contributing an estimated $40 million in profit improvement [Klarna press release, Feb 2024; note: self-reported figures, not independently audited]. This remains one of the few publicly quantified examples of non-engineering agentic deployment at enterprise scale.

**The practical question for 2026 is not whether agents work — they do, in narrow, well-instrumented domains — but whether organizations can govern, monitor, and cost-manage them as they scale beyond coding tools into higher-stakes workflows.**

---

## II. A Practical Taxonomy of Agent Maturity

A practical four-level taxonomy has emerged across practitioner discourse and framework documentation, though no single standards body has formalized it. We present it here as a useful mental model, not as an industry standard.

**Level 1: Copilots.** A human types, an LLM responds. Autocomplete, chat-based Q&A, inline code suggestions. The human remains in the loop for every action. Most deployed enterprise AI sits here.

**Level 2: Linear pipelines.** A fixed sequence of LLM calls processes a task — for example, extract → classify → summarize. No branching, no dynamic routing. Deterministic enough to test, cheap enough to run. The workhorse of production deployments.

**Level 2.5: Artifact-passing pipelines.** Agents hand off structured artifacts (JSON, code diffs, evaluation reports) rather than unstructured text. Each agent in the pipeline reads and writes to a defined interface. This is where reliability and debuggability start to emerge, because you can inspect every handoff point.

**Level 3: Dynamic multi-agent systems.** Agents spawn subtasks, route to specialists, coordinate shared state. Frameworks like LangGraph, CrewAI, and Anthropic's Agent SDK operate here. The surface area for failure modes expands significantly.

**Level 4: Autonomous agents.** Systems that set their own goals, manage their own resources, and operate with minimal human oversight. We are not aware of public examples of customer-facing Level 4 deployments in enterprise settings.

Available surveys suggest most production deployments visible so far are concentrated in Levels 1-2. The interesting design question for 2026 is not "how do we reach Level 4?" but "when does Level 2.5 suffice, and when does the complexity of Level 3 actually pay for itself?"

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

## IV. Three Failure Modes from Production Deployments

### Failure Mode 1: The Retry Loop

The Proxy incident described above is the canonical example. Root cause analysis identified four contributing factors: (1) the agent lacked circuit breakers for consecutive failures; (2) the vendor API returned inconsistent responses; (3) the policy engine evaluated each transaction individually with no memory of recent approvals; (4) there was a latency gap between authorization and transaction history updates [Proxy, Jan 2026].

**Mechanism:** Any agent with access to a rate-unlimited external API and no exponential backoff or failure-count circuit breaker is vulnerable. The compound cost grows linearly or worse with each retry.

**Mitigation:** Hard spending limits (balance-based, not policy-based), circuit breakers (halt after N consecutive failures), and aggregate velocity monitoring (how much has this agent spent in the last N minutes?).

### Failure Mode 2: Prompt Injection in Production

In 2025, NIST published CVE-2025-32711: an AI command injection vulnerability in Microsoft 365 Copilot that allowed unauthorized information disclosure over the network [NVD, CVE-2025-32711]. This is not a theoretical risk — it is a catalogued vulnerability with a CVE number in a shipping enterprise product.

**Mechanism:** An adversary crafts input that causes the agent to execute unintended actions — exfiltrating data, modifying records, or escalating privileges. In multi-agent systems, a single compromised agent can propagate malicious instructions to downstream agents through shared context.

**Mitigation:** Input sanitization at every agent boundary, not just the user-facing entry point. Principle of least privilege for every tool an agent can access. Audit trails that capture the full chain of agent actions. Deloitte's survey found that data privacy and security is the #1 AI risk concern (73% of respondents), well ahead of governance capabilities (46%) [Deloitte 2026, n=3,235].

### Failure Mode 3: Context Window Pollution

As agents accumulate context across multi-step pipelines, the quality of information in the context window degrades. Irrelevant tool outputs, failed attempt logs, and stale state from earlier pipeline stages crowd out the signal that the current agent needs. A study examining code review workflows found that 59.4% of tokens consumed were in review and iteration cycles — not in the primary task execution [Zenodo "Tokenomics" paper].

**Mechanism:** Each agent in a multi-hop pipeline reads the accumulated context of all prior agents. By hop 5-6, the context may contain more noise than signal. The LLM has no way to distinguish "this is a current instruction" from "this is a failed attempt from three steps ago."

**Mitigation:** Artifact-passing architecture (Level 2.5) — each agent reads only a defined structured input and writes only a defined structured output. The accumulated context problem is an argument *for* simpler pipeline architectures, not against them.

---

## V. The Enterprise Scaffolding Problem

Deploying an agent is 20% of the work. The other 80% is the scaffolding around it: orchestration, observability, evaluation, access control, and compliance.

### Orchestration

Any multi-step agent pipeline needs durable execution — the ability to retry failed steps, maintain state across long-running workflows, and handle timeouts gracefully. The market has split into three tiers:

| Category | Examples | Starting Price | Trade-off |
|---|---|---|---|
| Workflow engines (general) | Temporal Cloud, Inngest | Temporal: from $200/mo (Growth plan) | High reliability, steeper learning curve |
| Agent-native orchestration | Restate Cloud, Hatchet | Restate: from $99/mo (Pro) | Lower complexity, narrower ecosystem |
| Framework-embedded | LangGraph, CrewAI, Anthropic Agent SDK | Open-source / usage-based | Lowest barrier, tightest vendor coupling |

*[EDITORIAL] The pricing data above is sourced from official vendor pricing pages captured in February 2026. The trade-off assessments are our editorial judgment based on documentation review and architectural analysis.*

### Observability

You cannot govern what you cannot see. The Akto survey found only 21% of enterprises have full visibility into agent actions — and this from a sample weighted toward security-conscious organizations [Akto 2025].

| Tool | Free Tier | Paid Starting At | Source |
|---|---|---|---|
| LangSmith | $0 developer seat | Plus: $39/seat/mo | [LangSmith pricing](https://www.langchain.com/pricing), Feb 2026 |
| Braintrust | Free tier available | Pro: $249/mo | [Braintrust pricing](https://www.braintrust.dev/pricing), Feb 2026 |

*[EDITORIAL] For teams with frontend engineering capacity, building a custom trace viewer on top of OpenTelemetry is viable and removes vendor lock-in, though it requires significant upfront investment. We have no independent data on how long this takes.*

### Compliance and Governance

Regulatory pressure is shaping enterprise agent deployment. The EU AI Act (Regulation 2024/1689) entered into force on August 1, 2024, with staged application dates through 2027. The Act's risk-classification framework is likely to apply to AI systems making autonomous decisions that affect individuals, though agent-specific interpretive guidance has not yet been published [EU AI Act text, Regulation 2024/1689].

SOC 2 compliance, governed by AICPA's Trust Services Criteria, requires organizations to demonstrate controls over system access, change management, and processing integrity. Compliance teams report that SOC 2 audit scope is expanding to consider agent permissions and action audit trails, though formalized standards for agentic AI are still developing [AICPA Trust Services Criteria; inference based on criteria scope, not a published AI-specific SOC 2 rule].

ISO 42001 provides a management system standard for responsible AI, and organizations deploying autonomous agents in regulated industries should evaluate certification as a governance foundation [NQA ISO 42001 overview].

---

## VI. Software Engineering Dominance — And What Comes Next

Anthropic's data makes the concentration stark: software engineering accounts for nearly 50% of all agentic tool calls on their public API. Beyond coding, business intelligence, customer service, sales, finance, and e-commerce each represent single-digit percentages of traffic [Anthropic, Feb 2026, n=998K tool calls].

Why software engineering first? Several properties make code uniquely amenable to agent automation:

1. **Testability.** You can run the code and verify whether it works. This makes oversight cheap.
2. **Reversibility.** A bad code change can be reverted. A bad purchase, a bad email to a customer, or a bad medical recommendation cannot.
3. **Structured inputs and outputs.** Code diffs, test results, and compiler errors are machine-readable. Customer interactions, legal documents, and financial decisions are not.

The implication is that agent expansion into non-engineering domains will not simply be "more of the same." Each new domain requires solving the oversight problem from scratch. Anthropic's own analysis noted: "Whether the adoption curve in software engineering will repeat in other domains is an open question. Software is comparatively easy to test and review... In domains like law, medicine, or finance, verifying an agent's output may require significant effort, which could slow the development of trust" [Anthropic, Feb 2026].

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

This article draws on sources across four tiers:

- **Tier 1 — Research with published methodology:** Anthropic's agent autonomy study (n=998K tool calls), Deloitte's State of AI 2026 (n=3,235), CVE-2025-32711 (NVD record), and the EU AI Act regulation text.
- **Tier 2 — Industry reports and vendor case studies:** McKinsey (AI-general, not agent-specific), Akto (vendor-published survey), Klarna (self-reported press release), Proxy (vendor blog post-mortem), KPMG (consulting firm survey), and AWS Q Developer (first-party blog).
- **Tier 3 — Official pricing pages:** Anthropic, OpenAI, Temporal, Restate, LangSmith, and Braintrust, captured February 2026.
- **Tier 4 — Supporting context:** Zenodo "Tokenomics" paper, academic institutional theory framework, AICPA SOC 2 criteria, NQA ISO 42001 overview.

**Claims are labeled inline:** `[EDITORIAL]` marks positions that go beyond what the cited evidence demonstrates. Vendor-sourced data includes caveats about conflicts of interest and self-reporting. Statistical claims include sample sizes where available.

We deliberately chose to show our token math rather than present cleaned-up cost ranges. If the arithmetic looks tedious, that is intentional — it exists so that readers can verify or challenge our assumptions rather than trusting polished numbers.

---

*Feedback, corrections, and counter-evidence welcome. The purpose of grounded analysis is to be correctable.*
