---
title: Agent Harnesses as Operational Control Systems
subtitle: A Comparative Study of Hermes Operator-Fleet and Codex-Native Lane Running
author: Ahmed
date: "Draft: 2026-05-10"
---

## Executive Summary

The practical difference between Hermes and Codex in the observed operating
environment is not explained by model choice alone. Hermes wraps agent calls in
an operational harness: named lanes, profiles, task state, worktrees, acceptance
criteria, approval boundaries, final receipts, and watcher loops.

That harness gives Hermes a clearer control plane for messy parallel work. A
single interactive Codex session can reason deeply and edit effectively, but it
does not by default create a durable queue of bounded workers with receipts and
status that survive the user's attention moving elsewhere. Codex has the raw
primitives to do this: the CLI can run locally and inspect, edit, and execute
commands; Codex supports subagents for parallel work; Codex sandboxes constrain
command execution; and Codex app worktrees support independent background tasks
without disturbing a local checkout.

The case-study conclusion is a harness conclusion:

> In the observed workflow, Hermes exposed the more explicit local fleet wrapper.
> Codex exposed documented first-party execution primitives. The strongest
> hypothesis to test is a Codex-native lane runner that copies the useful
> Hermes-style control-plane ideas while adding stronger heartbeat, timeout,
> provenance, benchmark, and cross-machine scheduling controls.

## Problem Statement

Agentic software work has shifted from one prompt/one answer toward delegated
workflows: research lanes, implementation lanes, review lanes, safety lanes, and
operator lanes. In that setting, a user does not merely need a capable model.
The user needs a harness that answers:

- What work is running?
- Which worker owns it?
- What model and permissions does it have?
- What is it allowed to change?
- What evidence did it inspect?
- What did it produce?
- What failed?
- What needs human approval?

Without this layer, parallel agents become a source of cognitive load. With this
layer, they become an inspectable production system.

## Related Work

The comparison sits at the intersection of multi-agent systems, workflow
management, human-automation interaction, and software reliability.

Classical agent research defines agents by autonomy, reactivity, proactiveness,
and social ability, while multi-agent systems add coordination and distributed
decision-making concerns.[^wooldridge-jennings][^stone-veloso] Modern LLM-agent
systems revive the same coordination problem with tool use and language-based
delegation; ReAct introduced a practical reasoning/action loop for language
models, and AutoGen framed multi-agent LLM applications as configurable
conversations among agents, tools, and humans.[^react][^autogen]

Workflow research matters because an agent harness is effectively a workflow
engine for uncertain work. The workflow-patterns literature gives a vocabulary
for splits, joins, cancellation, state, and exception handling.[^workflow-patterns]
Human-automation research matters because the human operator still owns approval,
trust calibration, and intervention; levels of automation and situation
awareness research explain why the system must expose state, uncertainty, and
override points instead of hiding work inside a black box.[^parasuraman][^endsley]

Software engineering research also warns that coordination overhead is not
incidental. Coordination in software development and socio-technical congruence
both show that work dependencies and communication structures shape performance,
not merely individual worker skill.[^kraut][^cataldo] Agent fleets face the same
constraint: parallelism helps only when the harness aligns communication, state,
artifacts, and dependencies.

## Systems Compared

### Hermes Operator-Fleet

Hermes operator-fleet is a repo-backed local fallback launcher observed in the
case-study environment. Internal source inspection describes the goal as bounded
work, isolated git worktrees for coding tasks, and fan-out across multiple agent
profiles. Because this internal source is not included as a public artifact,
these details should be treated as case-study observations rather than
independently reproducible public evidence.

The inspected design used task state, profile configuration, run receipts, and a
generated status surface. A public reproduction should include sanitized
equivalent manifests before claiming reproducible implementation details. This
package includes a sanitized evidence appendix with representative task, profile,
receipt, and status records, stripped of private paths, model labels, operational
vendors, host details, and local security posture.

Observed implementation features, stated at the public-safe level:

- stable task ids generated as `op_<timestamp>_<slug>_<digest>`;
- task records containing title, lane, profile, repo/workdir, allowed writes,
  acceptance criteria, prompt, and approval boundary;
- flock-backed mutation of `tasks.json`;
- tmux session launch per worker;
- group slot files for concurrency limits;
- git worktree creation for Codex tasks;
- scratch workspaces for read-only analysis;
- prompt injection of approval boundary, allowed write scope, acceptance
  criteria, and operating rules;
- `codex exec --output-last-message <final.md> --json` for Codex workers;
- provider-neutral sidecar envelopes for proposal-only analysis;
- terminal states `done`, `failed`, `blocked`, and `cancelled`.

### Codex-Native Lane Running

Codex-native lane running means using Codex directly: interactive CLI,
non-interactive `codex exec`, app worktrees, subagents, sandboxing, MCP/tools,
skills, plugins, and local shell execution.

OpenAI's Codex documentation states that the Codex CLI runs locally in the
terminal and can read, change, and run code in a selected directory.[^openai-cli]
The subagent documentation says Codex can spawn specialized agents in parallel
and collect results, while also noting token cost and context tradeoffs.[^openai-subagents]
The sandbox documentation distinguishes sandbox boundaries from approval
policy: the sandbox constrains what spawned commands can do, while approvals
govern when Codex must stop for confirmation.[^openai-sandbox] The Codex app
worktree documentation describes independent worktrees for parallel background
work.[^openai-worktrees]

In the inspected environment, Codex had local CLI execution,
sandbox/approval controls, app integrations, parallel-work primitives, and
native tools for shell, patching, plans, subagents, browser operations, and
tool discovery. Exact model names, plugin inventory, feature flags, worker
counts, host details, and local security posture are intentionally omitted from
public artifacts.

Those are strong primitives. The gap is not capability. The gap is durable
multi-worker process control.

## Why Hermes Felt More Efficient

Hermes made the work feel coherent because it externalized coordination. A rough
operator request became a set of typed lanes:

- conductor map;
- target-review lane;
- document-workflow lane;
- external-resource research;
- data-inventory lane;
- state-audit lane;
- scoring-review lane;
- triage lane;
- approval-review lane;
- synthesis lane.

Each lane received an acceptance criterion and a no-go boundary. Outputs landed
as receipts. Watchers aggregated terminal states. The user did not have to keep
every branch of the investigation in working memory.

From a systems perspective, Hermes converted a conversation into a queueing and
provenance problem. That matters because provenance is the mechanism by which a
reader can decide whether an artifact should be trusted; W3C PROV defines
provenance as records of people, institutions, entities, and activities involved
in producing or influencing data.[^w3c-prov]

## Observed Hermes Liveness Gap

The same observation also exposed a weakness: one state-audit worker
remained running for several minutes with no terminal receipt, a blank terminal
surface, and only the initial prompt in its run directory. It eventually
completed and wrote a receipt, but during execution the conductor had no strong
heartbeat signal. The system had state, but not enough liveness semantics.

This is a classic harness problem:

- no heartbeat file;
- no progress event stream retained by default;
- no maximum wall-clock timeout for Codex workers;
- no stale-running transition;
- no automatic blocked-state conversion after silence;
- no structured failure reason if a child process hangs.

In SRE terms, the system had a status surface, but not enough actionable
monitoring. Google's SRE guidance frames monitoring as the system that informs
humans about conditions that should interrupt them and conditions that should be
handled without paging.[^google-sre-monitoring] Agent harnesses need the same
distinction: a slow worker is not the same as a silent worker; a silent worker
with no receipt should become an actionable blocked event.

## Codex Execution Strengths

Codex exposes documented first-party execution primitives:

- it provides direct coding and command execution primitives;
- it has first-party subagents;
- it has native local tools, app/plugin integrations, and MCP;
- it has explicit sandbox modes and approval policies;
- it can run interactively or non-interactively;
- it can work inside git worktrees;
- it can use web search and official documentation when required;
- it can inspect and edit code directly with local verification.

The architectural issue is not Codex capability. It is that raw capability does
not automatically become durable multi-worker process control. A single Codex
session is an effective execution surface; Hermes operator-fleet is a process
control surface. The architectural recommendation is hybrid: Codex execution
with a durable lane-runner harness.

## Mathematical Model

Let runner \( r \in \{H, C\} \), where \( H \) is Hermes operator-fleet and
\( C \) is Codex-native lane running.

All component scores are normalized to the interval [0, 1] before aggregation.
Task quality is a weighted mean:

`Q = 0.35 correctness + 0.20 completeness + 0.15 evidence + 0.15 decision + 0.15 usability`

Auditability is also a weighted mean:

`A = 0.20 inputs + 0.20 steps + 0.20 artifacts + 0.20 decisions + 0.20 replay`

Safety-boundary adherence, reliability, auditability, latency, and cost should
be reported as raw components first. An exploratory value-density index can then
be reported as:

`VD = (Q * B * R * A) / (latency_minutes * total_cost)`

where `B` is safety-boundary adherence, `R` is reliability, `A` is auditability,
and total cost includes token, compute, tool, and human-review cost. `VD` is an
exploratory composite, not a primary endpoint, because scale choices can change
its magnitude.

For parallel execution, Amdahl's Law bounds fixed-size speedup when a serial
fraction remains.[^amdahl] Gustafson's Law explains why scaled workloads can
still benefit from additional workers when the parallel part grows with system
capacity.[^gustafson] Agent fleets resemble the latter only when tasks are
actually independent. If a human conductor must serialize every decision, the
serial fraction dominates.

Let `c` be available workers, `lambda` be task arrival rate, and `mu` be service
rate per worker. The utilization approximation is `rho = lambda / (c * mu)`.
Stable operation requires `rho < 1`. This queueing approximation assumes
stationary arrivals, independent service times, no shared blocking resource, and
a fixed worker pool; observed agent work violates these assumptions whenever the
human conductor serializes approvals or reviews.

The practical lesson is simple: adding workers improves throughput only until
coordination, review, retry, and blocked-state overhead dominate.

## Evaluation Design

The benchmark should use paired, randomized tasks. Each task is run once through
Hermes and once through Codex-native, using identical fixtures and no live system
mutation.

Minimum pilot: `N = 40` paired fixtures.

Candidate full benchmark: `N = 8 x 10 x 2 = 160` paired fixtures before any
power analysis.

Here `N` means paired fixtures, not total runner executions. Each paired fixture
is executed once by each runner, so the candidate full run has 320 runner
executions. Repetition seeds are clustered within workload class and should not
be treated as fully independent observations. Half should run Hermes first; half
should run Codex first. The scoring packet should be anonymized before review by
stripping runner names, model names, local paths, receipt formatting,
timestamps, and other identifying surface details.

The primary endpoint should be paired mean quality difference, `Delta Q = Q_C -
Q_H`, with a stratified 95% bootstrap confidence interval by workload class and
fixture pair. The initial `N = 40` run should be labeled a pilot unless a
separate power analysis justifies stronger claims. The component score weights
are judgmental and should be pre-registered. Raw correctness, completeness,
evidence, decision quality, usability, auditability, safety-boundary adherence,
review minutes, latency, and reliability should be reported as required
companion endpoints. Weight sensitivity should be reported before using the
composite score for public claims.

Workload classes:

1. public-request discovery simulation from archived public pages;
2. record-staging simulation from synthetic CSV/SQLite;
3. operational graduation decision from mock reply records;
4. no-send message drafting to local text files;
5. queue triage from JSON task state;
6. evidence extraction from local PDFs, HTML, and screenshots;
7. failure recovery with corrupt or ambiguous inputs;
8. measurement/reporting from local run logs.

Safety constraints:

- no live external-system writes;
- no live record-system writes;
- no message-system drafts, sends, labels, or mutation;
- no external contact actions;
- no production workflow-automation execution;
- no public endpoints;
- no paid SaaS calls unless separately approved;
- no destructive filesystem commands.

## Proposed Refactor: Codex Lane Runner

The recommended refactor is to build a Codex-native lane runner with Hermes'
best ideas and stronger reliability controls.

Core components:

1. `tasks.json` or SQLite queue with leases, TTL, attempts, priority, and lane.
2. Profile registry for model, reasoning effort, sandbox, workspace, max
   parallel, timeout, and role prompt.
3. Worktree allocator for write-capable tasks.
4. Read-only fixture workspaces for evaluation tasks.
5. `codex exec` runner with `--output-last-message`, JSON events retained by
   default, and explicit output schema.
6. Heartbeat file updated every 30 seconds by the wrapper.
7. Stale-running detector that converts silent workers to `blocked` or `failed`.
8. Controller/worker dispatch across approved nodes using node leases.
9. Provenance manifest per run:
   `{task, runner, profile, prompt_hash, input_hashes, output_hashes, commands,
   timestamps, returncode, reviewer}`.
10. Watcher that aggregates terminal states and produces a synthesis packet.

This runner should not replace native Codex subagents. It should provide the
durable queue and receipt layer around them.

## Controller + Worker Architecture

One node should remain the controller and review surface. Other approved nodes
can operate as workers for long-running benchmark tasks.

Proposed topology:

- shared git-backed queue repo;
- configured worker workspace;
- sanitized capability class with allowed lanes and concurrency limits;
- task lease acquired by worker node;
- output receipt committed or synced back after completion;
- no direct live-system credentials in benchmark mode.

This lets worker nodes absorb long-running benchmark work while the controller
remains usable for interactive review.

## Findings

Finding 1: The observed workflow favored the Hermes-style harness because it
made task state, lane ownership, and receipts more explicit; this is a
case-study observation, not a controlled benchmark result.

Finding 2: Codex documentation describes primitives needed for a comparable
lane runner: local CLI execution, subagents, sandboxing, worktrees,
non-interactive mode, tools, MCP, and review.

Finding 3: Hermes' receipts and lanes appeared to reduce operator bookkeeping
and review burden in the observed wave, especially when a user was juggling many
operational questions.

Finding 4: Hermes currently needs stronger liveness and timeout controls. A
silent worker can hold a wave open even when all other lanes are done.

Finding 5: The best next architecture is hybrid: Codex execution wrapped in a
Hermes-like durable lane runner, with measured improvements rather than
identity-based preference.

## Recommendations

1. For the current private operational workflow, keep Hermes operator-fleet for
   multi-lane work until Codex-native lane running has equivalent receipts,
   status, and watcher behavior.
2. Add heartbeat, timeout, stale-running, and blocked-state conversion to the
   existing Hermes wrapper immediately.
3. Build the Codex Lane Runner as a separate public/sanitized harness project,
   not inside live operational repositories.
4. Benchmark using synthetic workloads before making claims about superiority.
5. Treat private operational data, records, message systems, and external
   workflow state as out of scope for public release data.

## Public Data Boundary

The observed private operational wave involved non-public records and
message-routing context. That material is useful for internal evaluation, but it
is not public benchmark data. Public release should use synthetic fixtures that
preserve the shape of the work without exposing private entities, contact
routes, record rows, message data, or strategy.

The public paper may say that a private operational wave revealed a liveness gap
and that receipts reduced review burden. It should not publish private
identifiers, private contact routes, or live-system counts unless Ahmed
separately approves a sanitized disclosure.

## Limitations

This draft is based on local source inspection, official documentation, and a
single observed operating wave. It is not yet a controlled benchmark result. The
benchmark design must be executed before publishing quantitative superiority
claims.

## References

[^openai-cli]: OpenAI, "Codex CLI," OpenAI Developers, accessed 2026-05-10, https://developers.openai.com/codex/cli.
[^openai-subagents]: OpenAI, "Subagents," OpenAI Developers, accessed 2026-05-10, https://developers.openai.com/codex/subagents.
[^openai-sandbox]: OpenAI, "Sandbox," OpenAI Developers, accessed 2026-05-10, https://developers.openai.com/codex/concepts/sandboxing.
[^openai-worktrees]: OpenAI, "Worktrees," OpenAI Developers, accessed 2026-05-10, https://developers.openai.com/codex/app/worktrees.
[^w3c-prov]: W3C, "PROV-DM: The PROV Data Model," W3C Recommendation, 2013, https://www.w3.org/TR/prov-dm/.
[^google-sre-monitoring]: Rob Ewaschuk, "Monitoring Distributed Systems," in *Site Reliability Engineering*, Google, https://sre.google/sre-book/monitoring-distributed-systems/.
[^amdahl]: Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities," AFIPS Conference Proceedings, 1967.
[^gustafson]: John L. Gustafson, "Reevaluating Amdahl's Law," *Communications of the ACM*, 31(5), 1988, https://cacm.acm.org/research/reevaluating-amdahls-law/.
[^wooldridge-jennings]: Michael Wooldridge and Nicholas R. Jennings, "Intelligent Agents: Theory and Practice," *The Knowledge Engineering Review*, 10(2), 1995, https://doi.org/10.1017/S0269888900008122.
[^stone-veloso]: Peter Stone and Manuela Veloso, "Multiagent Systems: A Survey from a Machine Learning Perspective," *Autonomous Robots*, 8(3), 2000, https://doi.org/10.1023/A:1008942012299.
[^react]: Shunyu Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models," ICLR, 2023, https://arxiv.org/abs/2210.03629.
[^autogen]: Qingyun Wu et al., "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation," arXiv:2308.08155, 2023, https://arxiv.org/abs/2308.08155.
[^workflow-patterns]: Wil M. P. van der Aalst et al., "Workflow Patterns," *Distributed and Parallel Databases*, 14(1), 2003, https://doi.org/10.1023/A:1022883727209.
[^parasuraman]: Raja Parasuraman, Thomas B. Sheridan, and Christopher D. Wickens, "A Model for Types and Levels of Human Interaction with Automation," *IEEE Transactions on Systems, Man, and Cybernetics - Part A*, 30(3), 2000, https://doi.org/10.1109/3468.844354.
[^endsley]: Mica R. Endsley, "Toward a Theory of Situation Awareness in Dynamic Systems," *Human Factors*, 37(1), 1995, https://doi.org/10.1518/001872095779049543.
[^kraut]: Robert E. Kraut and Lynn A. Streeter, "Coordination in Software Development," *Communications of the ACM*, 38(3), 1995, https://doi.org/10.1145/203330.203345.
[^cataldo]: Marcelo Cataldo, James D. Herbsleb, and Kathleen M. Carley, "Socio-Technical Congruence," ESEM, 2008, https://doi.org/10.1145/1414004.1414008.
