# Source Inventory

Access date for web sources: 2026-05-10.

## Primary / Official Product Sources

| Source | Type | Claims Supported |
|---|---|---|
| OpenAI Codex CLI, https://developers.openai.com/codex/cli | Official product documentation | Codex CLI runs locally, can inspect/edit/run code, supports non-interactive workflows and CLI features. |
| OpenAI Codex Subagents, https://developers.openai.com/codex/subagents | Official product documentation | Codex can spawn specialized agents in parallel and collect results; subagents require explicit request and consume more tokens. |
| OpenAI Codex Sandboxing, https://developers.openai.com/codex/concepts/sandboxing | Official product documentation | Sandbox boundaries constrain spawned commands and interact with approval policies. |
| OpenAI Codex Worktrees, https://developers.openai.com/codex/app/worktrees | Official product documentation | Worktrees support parallel independent work in Codex app. |
| OpenAI Help: Using Codex with your ChatGPT plan, https://help.openai.com/en/articles/11369540/ | Official help article | Codex product surfaces and plan-related availability. |

## Internal Case-Study Observations

These observations came from local source inspection during the motivating case
study. They are not public web references and should not be treated as
independently reproducible evidence unless sanitized manifests or source excerpts
are intentionally released.

| Internal Observation | Claims Supported | Public Release Treatment |
|---|---|
| Hermes-style operator-fleet wrapper | Profile registry, task queue, worktree creation, tmux launch, provider-neutral agent execution, receipts. | Case-study observation; release sanitized manifests before making reproducibility claims. |
| Codex local configuration inspection | Model, feature, plugin, and MCP surfaces available in the private environment. | Case-study observation; do not publish private config paths or secret-bearing files. |
| Repository instruction policy | No assistant/model/bot attribution requirement. | Safe to express as a publication policy, not as a claim about private files. |

See `references/internal-case-study-summary.md` for the sanitized public summary.

## Standards / Reliability / Provenance

| Source | Type | Claims Supported |
|---|---|---|
| W3C PROV-DM, https://www.w3.org/TR/prov-dm/ | Web standard | Provenance definition and trust role for data/artifact lineage. |
| NIST SP 800-190, https://doi.org/10.6028/NIST.SP.800-190 | Government standard/report | Containerization and isolation security considerations. |
| Google SRE Book: Monitoring Distributed Systems, https://sre.google/sre-book/monitoring-distributed-systems/ | Authoritative practitioner reference | Monitoring distinction, actionable alerts, operational reliability framing. |
| DORA Research Program, https://dora.dev/research/ | Research program | Software delivery performance as sociotechnical system, measurement discipline. |
| DORA 2024 Report, https://dora.dev/research/2024/dora-report/ | Research report | AI/tooling benefits and tradeoffs; importance of stable priorities and robust testing. |

## Academic / Mathematical Sources

| Source | Type | Claims Supported |
|---|---|---|
| Sun et al., "Multi-Agent Coordination across Diverse Applications: A Survey," arXiv:2502.14743 | Academic survey | Coordination questions, scalability, heterogeneity, human-MAS and LLM-based MAS. |
| Rossi et al., "Multi-Agent Algorithms for Collective Behavior," arXiv:2103.11067 | Academic survey | Coordination algorithms, scalability, bandwidth, mathematical structures. |
| Tran et al., "Multi-Agent Collaboration Mechanisms: A Survey of LLMs," arXiv:2501.06322 | Academic survey | LLM-based multi-agent collaboration structures and protocols. |
| Amdahl, "Validity of the Single Processor Approach..." AFIPS 1967 | Foundational parallel computing paper | Serial fraction limits fixed-size parallel speedup. |
| Gustafson, "Reevaluating Amdahl's Law," CACM 1988 | Foundational parallel computing paper | Scaled speedup framing for larger parallel workloads. |
| Erlang C / M/M/c queue references | Queueing theory | Multi-worker utilization and expected wait-time approximation. |
| Little, "A Proof for the Queuing Formula: L = lambda W" | Queueing theory | Relates work-in-progress, throughput, and latency. |
| Wooldridge and Jennings, "Intelligent Agents" | Academic article | Foundational agent concepts. |
| Stone and Veloso, "Multiagent Systems" | Academic survey | Coordination and learning in multi-agent systems. |
| ReAct and AutoGen papers | Academic / applied agent papers | LLM tool-use and multi-agent conversation patterns. |
| Parasuraman/Sheridan/Wickens and Endsley | Human factors research | Human authority, automation levels, and situation awareness. |
| van der Aalst workflow patterns | Workflow research | Splits, joins, cancellation, and state patterns for workflow harnesses. |
| Kraut/Streeter and Cataldo/Herbsleb/Carley | Software engineering research | Coordination overhead and socio-technical dependency alignment. |

## Weak / Not Yet Used

No market-size, productivity-percentage, or superiority claims should be made
until the paired benchmark exists. Vendor claims should remain marked as product
documentation, not independent validation.
