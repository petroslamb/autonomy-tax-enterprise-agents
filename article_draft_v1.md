# AI Agents in the Enterprise: What Ships, What Breaks, and What Costs

*A field guide for AI engineering practitioners, researchers, and CTOs — February 2026*

**By Rooted Layers** · *AI insights grounded on research*

---

Every enterprise board deck in 2025 promised autonomous AI agents would transform operations by mid-2026. The pitch was compelling: fleets of specialized AI workers routing tasks, calling APIs, writing code, and making decisions at machine speed.

The reality, as of February 2026, is more interesting than the pitch — and less comfortable. The agents are here. Some of them work extraordinarily well. Most of them don't work the way the vendor slides suggested. And nearly all of them have exposed architectural problems that the industry is still figuring out how to solve.

This guide is a ground-level report. It's written for the three people who most need the honest picture: the AI engineer choosing an architecture, the researcher studying where theory meets production constraints, and the CTO deciding what to fund. We'll show where agents are genuinely shipping value, where they break, what they actually cost, and what nobody has figured out yet.

---

## I. The Deployment Reality: Software Engineering Eats Everything

### The Evidence

The single most important fact about enterprise AI agents in February 2026 is this: **software engineering dominates**.

Amazon's Q Developer agent provides the clearest public case study. According to AWS, the code transformation agent — which autonomously upgrades legacy Java applications by analyzing dependencies, rewriting deprecated functions, and running test suites — has generated **$260 million in annualized efficiency gains**, saving an estimated **4,500 developer-years** of work. Customers report 25% faster initial development and up to a 40% increase in developer productivity.¹

Outside of software engineering — in finance, sales, HR, and operations — agent adoption remains in its early, heavily supervised days. While industry surveys suggest a majority of enterprises are running agent pilots, comprehensive public data on non-engineering adoption rates remains scarce. We don't have a definitive number. That absence is itself informative.

### The Mechanism

Why does software engineering run so far ahead? Because code has a property that almost no other enterprise domain shares: **it is self-verifying**.

An agent can write a function, execute the test suite, and receive an unambiguous signal — pass or fail — in milliseconds. This tight feedback loop is precisely what makes the ReAct pattern (Reason → Act → Observe) work reliably. The "Observe" step produces a deterministic outcome.

In sales, success is ambiguous. In HR, the feedback loop is months. In legal review, "correct" is a matter of interpretation. These domains lack the crisp, machine-readable reward signal that makes autonomous agent loops converge rather than hallucinate.

### The Implication

**For the CTO:** If you're evaluating agent adoption outside of engineering, your ROI timeline is 3–5× longer than the vendor pitch suggests. Budget for a 6-month supervised pilot with hard human-in-the-loop gates before any autonomous operation. The "we'll deploy agents across the org by Q3" timeline is almost certainly wrong.

**For the engineer:** The engineering-first reality means the tooling, frameworks, and best practices you'll encounter are overwhelmingly optimized for code generation workflows. If you're building agents for non-engineering use cases, expect to solve problems the frameworks haven't solved for you.

> ¹ AWS DevOps Blog, ["Amazon Q Developer just reached a $260 million dollar milestone"](https://aws.amazon.com/blogs/devops/amazon-q-developer-just-reached-a-260-million-dollar-milestone/)

---

## II. The Maturity Model — And Why You're Probably at Level 2

### The Technical Ladder

The industry has converged on a rough four-level taxonomy for agentic systems. Here's what each level actually looks like in production, stripped of marketing language:

| Level | Architecture | What the AI Controls | What's Hardcoded |
|---|---|---|---|
| **1 — Task Copilots** | Single LLM call + tools | The response content | Everything else |
| **2 — Orchestrated Pipelines** | Linear chain, artifact passing | Each agent's local reasoning | The pipeline sequence, routing logic |
| **3 — Supervised Autonomy** | Dynamic graph with LLM router | Routing between agents, task planning | The set of available agents, safety constraints |
| **4 — Decentralized Swarms** | Actor model, event bus | Agent spawning, inter-agent communication | Almost nothing |

**Where most of the world actually sits: Level 1–2.** The overwhelming majority of production enterprise deployments are copilots (Level 1) or linear pipelines (Level 2). This is not a failure. This is engineering maturity.

### The "Level 2.5" Sweet Spot

The most interesting finding from practitioners building production systems is what we call **Level 2.5** — linear pipelines where each agent node exhibits *local* autonomy through multi-turn ReAct loops, but the overall workflow follows a deterministic sequence.

In this architecture:
- Agent A receives a task, takes multiple turns using tools (filesystem, bash, APIs), and produces a **clean artifact** (a JSON payload, a markdown document, a code file).
- Agent A's artifact — and *only* that artifact — is passed to Agent B. No conversation history dumps. No context pollution.
- Agent B works autonomously within its scope, produces its own artifact, passes it forward.

This design has high **engineering maturity** even at a moderate **autonomy level**. It is an assembly line where each station is highly capable, but the line itself follows a fixed route.

**Why this matters:** Many teams assume they need Level 3's dynamic routing to handle complex problems. In practice, the artifact-passing discipline of Level 2.5 handles 80% of real enterprise workflows more reliably, at lower cost, and with dramatically simpler debugging.

### Why the Maturity Model Itself Is Incomplete

The four-level model tells you *what* to build. It says nothing about *whether your organization can actually adopt it*.

Research on technology adoption in organizations — drawing on Institutional Theory and Diffusion of Innovation frameworks — identifies three forces that determine where companies actually end up, independent of their engineering capability:²

- **Coercive pressure:** Regulatory mandates force adoption (or prohibit autonomy). An EU-regulated bank faces constraints that an unregulated startup doesn't.
- **Mimetic pressure:** Companies copy what competitors do. When a market leader announces an agent deployment, followers imitate the architecture — regardless of whether it fits their context.
- **Normative pressure:** Industry benchmarks and professional standards set expectations. If "every modern engineering team uses agents for code review," teams adopt agents to avoid looking outdated.

The maturity level a company reaches is the intersection of its technical capability and its institutional environment. A bank with a brilliant AI team may still operate at Level 1 because coercive regulatory pressure prohibits autonomous decision-making.

### The Team Shape Table

What each maturity level actually requires in headcount:

| Level | AI Engineers | Backend / Platform | DevOps / SRE | Estimated Annual Infra Cost |
|---|---|---|---|---|
| **1 — Copilots** | 0–1 (uses vendor tools) | Existing team | Existing team | $1K–$10K (API costs) |
| **2 — Pipelines** | 1–2 | 1 (integration) | Existing team | $10K–$50K |
| **2.5 — Artifact Pipelines** | 2–3 | 1–2 (infra, state mgmt) | 0–1 | $30K–$100K |
| **3 — Supervised Autonomy** | 3–5 | 2–3 (Temporal/Restate, checkpointing) | 1–2 (observability, alerting) | $100K–$500K |
| **4 — Swarms** | 5+ (research-grade) | 3+ (distributed systems) | 2+ (dedicated) | $500K+ |

> ⚠️ *These are editorial estimates based on the architectural requirements at each level, not survey data. No public source provides validated team-size benchmarks for agentic deployments as of Feb 2026.*

> ² Institutional Theory and Diffusion of Innovation: A Theoretical Approach on AI. [DOI: 10.1590/1807-7692bar2025250060](https://doi.org/10.1590/1807-7692bar2025250060)

---

## III. Where Agents Break: Three Failure Modes That Cost Real Money

Before we discuss architecture choices, we need to understand the failure modes. These aren't hypothetical — they are documented patterns from production deployments in the 2024–2025 cycle.³

### Failure Mode 1: The "Loop of Doom" — Cost Blowout

**What happens:** An agent encounters a tool execution error — a syntax mistake in a generated SQL query, a malformed API call, or a missing dependency. The framework prompts the agent to retry. Without a hard exit condition, the agent enters an infinite retry loop, spending thousands of tokens apologizing for its failure and attempting the same broken action.

**Documented impact:** Users of framework-based multi-agent systems have reported costs of **$7 per run for simple tasks** — tasks that should cost fractions of a cent — because agents burned tokens in apologetic retry loops without a circuit breaker.

**The mechanism:** This failure is architectural, not model-related. It occurs when orchestration frameworks manage retries implicitly (inside a black box) rather than through explicit state-based counters that the developer controls. The fix is unglamorous: a `recursion_limit` parameter, a `max_retries` counter in the state, and a hard escalation to a human when the counter is exceeded.

**For the CTO:** Ask your team: "What is the maximum dollar amount a single agent run can spend before it's automatically killed?" If they can't answer immediately, you have this failure mode in production.

### Failure Mode 2: The Latency & Coordination Trap

**What happens:** An agent system that works perfectly on a developer's laptop falls apart in cloud production. The cause is network latency. Local inter-agent communication is near-instant; in production, API calls introduce 200–500ms delays per hop.

**The cascade:** Agents that rely on implicit timing for coordination — expecting responses within milliseconds — begin to timeout. When they timeout, they either hallucinate an answer (proceeding without the data they were waiting for) or duplicate work (starting the same task a second time because they assumed the first attempt failed).

**The mechanism:** This is the "Valley of Death" in agent development — the gap between the prototype that works magically in a Jupyter notebook and the production system that must survive network jitter, API rate limits, and concurrent users. Frameworks that hide their coordination logic inside opaque abstractions make this failure especially hard to debug, because the developer cannot adjust timeout thresholds or see where the implicit handoff broke.

**For the engineer:** Build your agent system to be latency-tolerant from day one. Use explicit artifact passing (file-based or database-backed) rather than in-memory message passing. Test with simulated network delays *before* deploying to cloud.

### Failure Mode 3: Context Window Pollution — Information Degradation

**What happens:** As agents collaborate through conversation-style coordination, the context window fills with operational chatter: "Here is the data." "Thank you, I will now analyze it." "Please confirm." The original task instructions — the actual goal — get pushed out of the context window by this noise.

**The cascade:** By the time Agent C receives the task from Agent B, the signal-to-noise ratio has degraded. Agent C gets a watered-down version of the instructions, producing lower-quality outputs. In multi-step pipelines, each hop compounds the loss.

**The mechanism:** This is why the artifact-passing discipline of Level 2.5 matters so much. When Agent A distills its work into a discrete artifact (a structured JSON object, a markdown document) and only that artifact is passed to Agent B, the context is clean at every stage. The chatter is discarded. The signal is preserved.

**The cost dimension:** A recent academic study quantifying token usage in agentic software engineering found that **59.4% of all tokens are consumed by automated code review cycles** — the back-and-forth between generating, testing, and revising code.⁴ This means the majority of your API bill goes to the iterative loops, not the initial generation. Reducing unnecessary context in those loops directly reduces cost.

> ³ Xcelore, ["LangGraph vs CrewAI: Comparison Guide for Production Agents in 2025"](https://xcelore.com/blog/langgraph-vs-crewai/) — documents the Valley of Death, Loop of Doom, and context pollution patterns from production post-mortems.

> ⁴ "Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering." [Zenodo, DOI: 10.5281/zenodo.17430187](https://zenodo.org/records/17430187)

---

## IV. The Architecture Wars: Frameworks vs. Primitives

The most contentious debate in AI engineering in 2026 is not about which model to use. It's about how much abstraction to accept in your orchestration layer.

The industry has fractured into three camps:

### Camp A: The Framework Approach (LangGraph)

**Philosophy:** "Multi-agent routing is complex. Don't reinvent the wheel."

LangGraph models your workflow as a compiled state machine (a directed graph). You define typed state schemas, agent nodes, and routing edges. The framework handles the ReAct loop, error recovery, and state persistence via a Postgres-backed checkpointer.

**What you get for free:**
- Context eviction logic (automatic summarization when the window fills)
- Three-tier error handling (transient retries, LLM-recoverable errors, human escalation)
- Sub-graph composition (nesting a dynamic "dev team" inside a rigid "compliance pipeline")
- Time-travel debugging (rewind to any step and modify state)

**What you give up:**
- **Ecosystem gravity toward proprietary SaaS.** LangGraph itself is MIT-licensed. But running it in production — background workers, WebSocket streaming, concurrent user isolation — is painful without LangGraph Platform (proprietary). Debugging is painful without LangSmith (proprietary). The open-source library is free; the production scaffolding has a price.
- **Abstraction opacity.** When a LangGraph agent fails, the stack trace traverses framework internals. Debugging requires understanding the framework's reducer logic, channel merging, and compilation model — not just your business logic.

### Camp B: The Primitives Approach (Raw SDK + Temporal)

**Philosophy:** "An LLM call is just an API request that returns a string. Just use code."

You write a standard Python `while` loop. You call the Claude or OpenAI API directly. You parse the tool-use response. You execute the tool. You append the result. You loop. The state is a Python list. The routing is an `if` statement.

**What you get:**
- Total transparency. Every line of code is yours. If it breaks, the stack trace points to your code, not a framework's internals.
- Infrastructure-agnostic durability. Wrap the `while` loop in a Temporal workflow, and you get crash recovery, long-running execution, and human-in-the-loop signals without any AI-specific framework.

**What you give up:**
- Every production concern — context eviction, tool-output truncation, error classification, concurrent state isolation — becomes your engineering team's responsibility to build from scratch.
- At 50+ tools and complex multi-agent routing, the `while` loop becomes thousands of lines of fragile boilerplate.

### Camp C: The Hybrid ("Belt and Suspenders")

**Philosophy:** "Use LangGraph for the routing logic. Use Temporal/Restate for the infrastructure."

LangGraph handles graph compilation, state management, and AI-specific concerns (context eviction, checkpointing). Temporal or Restate handles infrastructure concerns (durable execution, crash recovery, async queuing, multi-tenancy).

This is the architecture behind the most ambitious enterprise deployments in 2026. It's also the most complex, requiring three different engineering skill sets: AI engineers for the graph nodes, distributed systems engineers for the Temporal/Restate cluster, and platform engineers for the glue (trace stitching, Redis pub/sub for streaming).

### The Infrastructure Contenders

The orchestration layer has its own ecosystem war:

| Engine | Complexity | Strength | Best For |
|---|---|---|---|
| **Temporal** | 🔴 High | Indestructible. Event-sourced replay. Battle-tested at Uber/Netflix scale. | High-stakes systems where a crash means losing millions. |
| **Restate** | 🟡 Medium | Single Rust binary. Sub-100ms latency. Native actor model. Serverless-friendly. | Modern cloud-native deployments. New projects without Temporal baggage. |
| **Hatchet** | 🟢 Low | Python-native. Standard decorators. No deterministic replay constraints. | Teams that want Temporal's durability without Temporal's learning curve. |

**The honest trade-off:** Temporal's strict deterministic replay (`datetime.now()` will crash your workflow — you must use `workflow.now()`) is the price of its indestructible guarantees. Hatchet's freedom from those constraints comes at the cost of replay-based time travel and in-flight state querying. Restate sits in the middle — event-sourced durability without the full complexity of Temporal's worker model.

### The Observability Problem

Wherever you land architecturally, you need to see inside the agent. The tooling landscape for this is fragmented and frankly, a mess:

| Tool | Open Source? | Strength | The Catch |
|---|---|---|---|
| **LangSmith** | ❌ No | Best-in-class LangGraph trace visualization | Proprietary SaaS. Your prompts live on their servers. |
| **Langfuse** | ✅ Yes | Self-hostable LangSmith alternative | You maintain the Docker containers and Postgres. |
| **Arize Phoenix** | ✅ Yes | Eval-first. Native OpenTelemetry. | Strongest in RAG evaluation, less polished for multi-agent traces. |
| **Braintrust** | ❌ No | Tight eval + trace coupling. Regression testing. | Enterprise SaaS pricing. |
| **Traceloop (OpenLLMetry)** | ✅ Yes | Pure OTel standardization for existing APM tools | You lose AI-specific visualization; Datadog sees JSON blobs. |

**The real-world pattern:** Most enterprises operating at Level 3 run a dual-pane strategy — Datadog (or equivalent) for infrastructure health and alerting, plus an AI-native tool (Langfuse or LangSmith) for prompt-level debugging. The two are linked by a shared OpenTelemetry trace ID, so a DevOps engineer seeing a timeout in Datadog can click through to the exact hallucinated prompt in Langfuse.

---

## V. The Enterprise Scaffolding Nobody Talks About

Beyond the orchestration engine and the observability dashboard, production agent systems require infrastructure that rarely appears in framework tutorials.

### Security: Guardrails Are Code, Not Prompts

Enterprise security for agents means one thing: **never rely on a system prompt for safety.** The instruction "do not reveal confidential information" in a system prompt is trivially bypassed by prompt injection.

Production guardrails are implemented as **code proxies** external to the agent:
- **Input gateways** (NeMo Guardrails, Llama Guard) scan user prompts for injection attacks *before* the agent sees them
- **Output gateways** scan agent responses for PII, toxic content, or policy violations *before* the user sees them
- **Zero-trust tooling** grants agents short-lived, scoped tokens (not static API keys) through OAuth propagation or MCP (Model Context Protocol)

The principle is Least Privilege applied to AI: an agent that writes code should have *no memory address* pointing to the production database password, regardless of how cleverly a user phrases their prompt.

### Agentic IAM: Whose Credentials Does the Agent Use?

When your agent has a "Jira Tool," whose Jira account does it authenticate with? If it uses a global service account, a low-level employee could prompt-inject the agent into reading the CEO's private tickets.

The emerging standard is **user-delegated OAuth**: the agent assumes the IAM identity of the user who triggered it, inheriting that user's permissions exactly. Tools like Composio and Nango provide managed integration endpoints for this pattern.

### The Regulatory Pressure

As of February 2026, no clear regulatory playbook exists specifically for autonomous enterprise agents. But the pressure is building:

- The **EU AI Act** is in force, and its risk-classification framework applies to AI systems making autonomous decisions. The compliance requirements — audit trails, human oversight provisions, transparency obligations — map directly onto the observability and human-in-the-loop patterns discussed above.
- **ISO 42001** (AI Management Systems) is emerging as the standard for demonstrating responsible AI governance to auditors and enterprise clients.⁵
- **SOC2 audits** increasingly ask: "What happens when your AI agent accesses customer data? What's the audit trail? Who approved the action?"

The regulatory landscape is fragmented and evolving. This uncertainty is itself a constraint: it's one more reason why enterprises default to Level 2 (fully auditable, human-approved) rather than Level 3 (dynamic routing that's harder to explain to a regulator).

> ⁵ CompliancERT provides a practical framework for navigating GDPR, Swiss FINMA regulations, and ISO 42001 certification for AI-powered systems. [compliancert.com](https://compliancert.com/)

---

## VI. Level 4: The Bleeding Edge and Why You Shouldn't Be There (Yet)

Everything discussed so far — Levels 1 through 3 — operates within a **state machine** paradigm. There is a central state, a graph, a supervisor. Control is centralized, even when the routing is dynamic.

Level 4 abandons this entirely. It uses the **Actor Model**: every agent is an independent process with its own private memory, communicating asynchronously via an event bus (publish/subscribe). There is no central graph. There is no supervisor dictating the flow.

### How It Works

A "Manager" agent receives a massive objective ("Analyze the 2025 EV market and write a 50-page report"). Instead of routing this through a predefined graph, the Manager:
1. Drafts a plan (JSON array of required specialists)
2. **Dynamically spawns** new agents at runtime — a Tesla_Expert, a Ford_Expert, an Editor
3. Assigns each agent to listen on specific pub/sub topics
4. Publishes the initial task and **goes to sleep**

The spawned agents work independently, publishing findings to shared topics. The Editor listens for all research to arrive and synthesizes the final output. The path emerges from the agents' interactions — it was never pre-defined in code.

### The Frameworks

- **Microsoft AutoGen v0.4:** The leading Level 4 framework. Rebuilt around asynchronous message passing and pub/sub event buses.
- **OpenAI Swarm:** Experimental. Uses stateless "handoffs" rather than an event bus. Simple and token-efficient but explicitly not production-ready.
- **Letta (MemGPT):** Treats agents as OS processes with RAM (working memory) and disk (archival memory). Strongest for agents that must run continuously for months.
- **Ray Actors:** Not an AI framework at all — it's a distributed computing engine. The biggest tech companies building Level 4 systems often skip AI frameworks entirely and deploy standard Python classes as Ray remote actors with LLM calls inside.

### Why CISOs Are Terrified

Level 4 has three unsolved problems:

1. **Infinite argument loops.** Without a central router enforcing `max_revisions`, two agents can disagree and debate indefinitely, burning API credits. There are reports of agents spending thousands of tokens reasoning about why the other agent is wrong.

2. **The deadlock problem.** If Agent A is waiting for a message from Agent B, and Agent B formatted its message slightly wrong so Agent A doesn't recognize it, the system silently halts. No error is thrown. Both agents sit idle, consuming infrastructure resources.

3. **The garbage collection problem.** If a Manager spawns 15 agents for 3 concurrent users, that's 45 agents sitting in RAM listening to the event bus. A stray message on the wrong topic can wake up dozens of agents simultaneously, triggering a cascade of hallucinated responses and cost blowouts.

**The honest assessment:** Level 4 is currently used in enterprise settings only for internal R&D, autonomous red-teaming, and deep research tasks where it's acceptable for agents to run for hours and argue. No one is putting an AutoGen event bus in front of a real customer. The industry hasn't figured out how to make decentralized agent communication safe enough for customer-facing production.

---

## VII. The "Boring Stack" Thesis

After surveying the full landscape — the frameworks, the infrastructure engines, the observability tools, the security layers, the compliance platforms — the most striking pattern is this:

**The most robust production agents run on remarkably boring foundations.**

The SaaS sprawl problem is real. If you buy a dedicated startup product for memory, prompt management, model routing, tool authentication, observability, and evals, you end up with 6+ third-party services in your critical path. Each adds a network hop (latency), a security surface (data exposure), and a business dependency (startup mortality risk — half of these companies may not exist in 18 months).

### What to Build In-House

- **Memory:** Enable the `pgvector` extension on your existing PostgreSQL database. Write a short script to embed conversation history. It's free, has zero external latency, and stays behind your firewall.
- **Prompt management:** Prompts are text. Store them in `.json` files in your Git repo. Version them with standard CI/CD. No "Prompt CMS" SaaS needed.
- **Model routing:** Run a free LiteLLM proxy container inside your Kubernetes cluster to standardize API calls across providers and track token spend in your own logs.

### What to Actually Buy

There are only two areas where the build cost genuinely exceeds the buy cost:

1. **Observability & Evals** (Langfuse or Braintrust): Building a custom UI to render nested, interactive LLM trace trees and run LLM-as-a-Judge evaluations against golden datasets will take your frontend team 6 months. Pay the SaaS fee or self-host Langfuse.

2. **Agentic IAM & Integrations** (Composio, Nango): Managing OAuth2 refresh tokens, rate limits, and credential rotation for 50 different enterprise APIs is a full-time job. Offload it.

### The Stack That Ships

If you're building an enterprise agent system tomorrow and want to minimize external dependencies while maximizing reliability:

| Layer | Choice | Why |
|---|---|---|
| **Agent logic** | Claude SDK or OpenAI SDK | Direct API control. No abstraction tax for simple pipelines. |
| **Orchestration** | LangGraph (for complex routing) or raw SDK (for linear pipelines) | Match the tool to the problem complexity. |
| **Durability** | Temporal (battle-tested) or Restate (modern, lighter) | Depends on your team's distributed systems experience. |
| **State & Memory** | PostgreSQL + pgvector | Free. Private. Already in your stack. |
| **Observability** | Langfuse (self-hosted) + Datadog (infrastructure) | Dual-pane: AI traces + system health. |
| **Security** | NeMo Guardrails + OAuth delegation | Prompts are not security. Code proxies are security. |

---

## VIII. What We Don't Know Yet

The honest Rooted Layers way to end this guide is to name what's missing — the problems the industry hasn't solved and the data that doesn't exist yet.

**Deterministic testing of stochastic systems.** We don't have good tools for writing unit tests for agents whose outputs change on every run. LLM-as-a-Judge evaluations are the current best practice, but they're expensive, noisy, and hard to use as regression gates in CI/CD. This is an open research problem.

**Long-horizon episodic memory.** Current agent memory is session-scoped (what happened during this task) or semantic (vector embeddings of past facts). Neither is good at learning from experience over weeks and months. The agent that crashed spectacularly on a task yesterday will try the same approach tomorrow unless you manually update its prompt.

**Multi-tenant agent isolation.** When 1,000 users share the same agent system, ensuring that User A's context never leaks into User B's response is a solved problem for traditional web applications but an unsolved problem for stateful, multi-turn agent sessions that share model context.

**Reliable cost prediction.** Because agent execution is inherently variable — an easy task might take 3 LLM calls, a hard one might take 30 — enterprises cannot reliably budget for agent API costs. The Tokenomics research showing that 59.4% of tokens go to review cycles gives us the first quantitative anchor, but per-task cost variance remains high and unpredictable.

**The regulatory endgame.** No one knows yet how regulators will classify autonomous enterprise agents under the EU AI Act's risk framework. Until that classification is settled, enterprises face a compliance uncertainty premium that pushes them toward more conservative (lower-autonomy) architectures.

---

## A Note on Method

This guide synthesizes architectural patterns from the current AI engineering ecosystem with published case studies and practitioner reports. Where we cite specific numbers, the sources are linked. Where we make editorial estimates (particularly the team-size table), we say so explicitly.

We deliberately chose not to include unsourced statistics, even widely repeated ones. Several commonly cited numbers about agent adoption rates — "70% of enterprises are piloting," "only 20% have visibility" — appear throughout the industry press without traceable primary sources. We excluded them. An article that claims to be grounded cannot repeat numbers it can't verify.

If you're a practitioner with production deployment data, failure post-mortems, or cost benchmarks you'd be willing to share (even anonymously), we'd like to hear from you. The field moves fast, and the best evidence comes from the people doing the work.

---

*Petros Lambrakopoulos writes Rooted Layers on Substack — AI insights grounded on research. Follow for grounded analysis of AI engineering, systems architecture, and the messy reality of putting intelligence into production.*
