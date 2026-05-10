---
title: Agent Harnesses as Operational Control Systems
subtitle: Why Codex needs a durable lane runner for serious parallel work
author: "Ahmed Mahmoud, ZalaStack, Calgary, Alberta, Canada, GitHub: github.com/mizoz"
date: "Draft: 2026-05-10"
---

## Executive Summary

This paper compares two ways of running agentic work: Hermes operator-fleet and
Codex-native lane running. The comparison is based on a case-study observation,
not a controlled benchmark.

As of 2026-05-10, the case-study finding is clear:

- Hermes was better at multi-lane operational control: task decomposition,
  visible state, acceptance criteria, approval boundaries, receipts, watcher
  synthesis, and operator bookkeeping.
- Codex was better as a direct execution substrate: local code inspection,
  editing, command execution, tool use, subagents, worktrees, and sandboxed
  workspace work.

The practical difference was not mainly model quality. It was harness quality.
Hermes exposed a stronger operational control plane. Codex exposed stronger
first-party execution primitives. The most useful architecture is therefore not
"Hermes instead of Codex" or "Codex instead of Hermes." It is Codex execution
wrapped in a durable lane runner.

The proposed Codex Lane Runner would add the missing control layer: queue state,
leases, workspace allocation, provenance manifests, heartbeats, timeouts,
stale-worker detection, final receipts, and review packets.

The paper separates what was observed, what is inferred, and what still needs a
paired benchmark. Public claims should stay inside that boundary.

## The Problem: Capable Agents Are Not Enough

A single capable agent can be useful in a conversation. Parallel agents create a
different problem.

Once work splits into multiple lanes, the operator needs more than answers. The
operator needs operational state:

- What is running?
- Who owns it?
- What can it touch?
- What evidence did it inspect?
- What did it produce?
- What failed?
- What is waiting for approval?
- What is stale or silent?

A powerful agent without operational state becomes another thing the operator
has to remember.

That is the core systems problem. Parallelism only helps when the work is
bounded, observable, reviewable, and recoverable. Without that control layer,
more agents can increase cognitive load instead of throughput.

An agent harness is the control layer around agent execution. It turns a request
into bounded tasks, assigns workers, constrains permissions, captures evidence,
records state transitions, and produces reviewable artifacts. A good harness
does not make the model smarter. It makes the work safer to delegate.

## Case Study: Hermes vs Codex in Parallel Work

The motivating observation was a private operational wave with several lanes
running in parallel. The wave was not a scientific benchmark. It was a live
operator experience: decompose a messy goal, launch bounded workers, wait for
receipts, synthesize outputs, and decide what to do next.

In that setting, Hermes and Codex felt different.

Hermes externalized coordination. It created named lanes, task records,
profiles, bounded prompts, receipts, watcher status, and terminal states. The
operator could see the shape of the work instead of keeping it all in memory.

Codex was the stronger direct execution surface. It could inspect files, edit
code, run commands, use tools, reason deeply, and delegate to subagents. Codex
also has documented support for CLI execution, non-interactive execution,
sandboxing, subagents, and app worktrees.[^codex-cli][^codex-subagents][^codex-sandbox][^codex-worktrees]

The lesson was not "Hermes is better" or "Codex is worse." The lesson was more
specific:

> Codex had the stronger execution surface. Hermes had the stronger operational
> control surface.

That is the design opportunity.

## Methodology

This paper uses a qualitative case-study method. The goal is not to score model
intelligence. The goal is to compare harness behavior under messy parallel work.

The observation unit was an operational wave: one operator request decomposed
into multiple bounded lanes, each with a worker, prompt boundary, expected
artifact, and terminal state. The comparison asked what each system made visible
to the operator during and after the work.

The evaluation questions were:

1. Could the operator see what work existed?
2. Could the operator see who owned each task?
3. Were task boundaries and approval rules explicit?
4. Did each worker produce a reviewable artifact?
5. Could the operator distinguish running, blocked, failed, stale, and done?
6. Did the harness reduce or increase human bookkeeping?
7. Did the system provide enough evidence to review claims?
8. Could the execution environment inspect, edit, run, and verify code?

The evidence types were task records, lane prompts, acceptance criteria,
terminal receipts, watcher output, generated artifacts, terminal behavior, and
public Codex documentation. Private operational content is not used as benchmark
data and is not published.

The findings are classified in three levels:

- **Observed finding:** directly visible in the case-study run.
- **Interpretation:** a systems conclusion drawn from the observed behavior.
- **Benchmark claim:** a claim that should not be made until paired synthetic
  fixtures are run.

This paper makes observed findings and interpretations. It does not claim a
controlled benchmark winner.

## What Hermes Got Right

Hermes worked well because it behaved like a harness, not because it was a
different kind of intelligence.

The useful flow was simple:

`operator request -> lane decomposition -> bounded workers -> receipts -> watcher -> synthesis`

Each step reduced ambiguity.

| Harness element | Why it mattered |
|---|---|
| Named lanes | The operator could see work streams instead of a single blob of activity. |
| Profiles | Different tasks could use different roles and permissions. |
| Acceptance criteria | Workers knew what "done" meant. |
| Approval boundaries | Workers knew what not to touch. |
| Isolated workspaces | Coding and analysis tasks had bounded surfaces. |
| Queue state | Running, done, blocked, failed, and cancelled states were visible. |
| Receipts | Each lane produced a final artifact the operator could review. |
| Watcher surface | Terminal states could be aggregated into one synthesis. |

This is process control. Hermes turned parallel agent work into something closer
to an operating queue.

The key point is not that every Hermes implementation detail should be copied.
The key point is that agent work needs a durable control plane once the operator
delegates more than one task at a time.

## What Codex Already Has

Codex should not be treated as weak. The opposite is true: Codex already has
many of the primitives needed to build the better system.

The relevant primitives are:

- local CLI execution;
- non-interactive `codex exec`;
- app worktrees;
- subagents;
- sandbox and approval controls;
- MCP, tools, and plugins;
- local shell execution;
- code editing and verification in the workspace.

Those primitives make Codex a strong execution substrate. The missing layer is
not another prompt. It is durable operational semantics around the execution:
queue ownership, state transitions, liveness, evidence, receipts, and review.

Codex can run the worker. The lane runner should make the worker accountable.

## Comparative Findings as of 2026-05-10

The case study supports a narrow public conclusion: Hermes and Codex were better
at different parts of the job.

**Hermes was the better observed fit for operational coordination.** It handled
multi-lane decomposition, visible task state, acceptance criteria, approval
boundaries, receipts, and watcher synthesis better in the observed wave. This is
an observed finding.

**Codex was the better observed fit for direct execution.** It had the stronger
local inspect/edit/run loop and the richer first-party tooling surface:
subagents, worktrees, sandbox controls, tool use, and local verification. This
is an observed finding.

**Neither system fully solved liveness.** Hermes made state more visible, but a
silent-running worker still lacked strong heartbeat semantics. This is an
observed reliability gap.

**Neither system has a public benchmark win yet.** A fair public comparison
needs paired synthetic fixtures, randomized runner order, anonymized review
packets, and raw metrics before composite scores. This is a benchmark boundary.

**The best next architecture is a Codex Lane Runner.** Codex has the execution
substrate. Hermes showed the shape of the control plane. This is an
interpretation, not a benchmark result.

The most important result is therefore not a brand ranking. It is a functional
ranking:

- for **parallel operational coordination**, Hermes was better in the observed
  wave;
- for **direct workspace execution**, Codex was better positioned;
- for **future serious agent operations**, the strongest candidate is a hybrid:
  Codex execution inside a durable Hermes-style lane runner.

## The Real Gap: Durable Operational Control

An operational control system for agent work is the layer that answers four
questions:

1. What work exists?
2. Who owns each unit of work right now?
3. What is each worker allowed to do?
4. What evidence proves what happened?

For serious parallel work, that means the harness needs:

- a queue;
- worker ownership;
- leases and TTLs;
- explicit state transitions;
- allowed write scope;
- approval policy;
- evidence and provenance capture;
- receipt schema;
- retry and failure semantics;
- liveness monitoring;
- review packet generation.

Without this layer, parallelism pushes state into the operator's head. With this
layer, parallelism becomes manageable because every worker has a contract, every
contract has a receipt, and every receipt can be reviewed.

This is also where safety boundaries become practical. "Do not mutate live
systems" is not enough as a sentence in a prompt. It should be represented in
task metadata, worker permissions, validation checks, and final receipts.

## The Liveness Problem

The most concrete reliability lesson from the observed wave was liveness.

One state-audit worker stayed running for several minutes. No terminal receipt
appeared during that period. The terminal surface was blank. The run directory
only showed the initial prompt. The worker eventually completed, but while it
was running the conductor did not have a strong heartbeat signal.

That is not a minor UX issue. It is a process-control failure.

In agent fleets, "still running" is not a sufficient state.

A runner needs to distinguish:

- active worker;
- slow worker;
- silent worker;
- blocked worker;
- failed worker;
- cancelled worker;
- stale-running worker.

The required controls are straightforward:

- heartbeat file updated by the wrapper;
- retained JSON event stream;
- maximum wall-clock timeout;
- no-output timeout;
- stale-running transition;
- automatic blocked-state conversion;
- structured failure reason;
- final receipt required for terminal state.

The state model should be explicit:

| State | Meaning | Required operator signal |
|---|---|---|
| `queued` | Work exists but has no owner. | Priority, lane, and acceptance criteria. |
| `leased` | A worker owns the task for a bounded interval. | Lease owner and expiry. |
| `running` | The worker is active and producing heartbeat updates. | Last heartbeat and current phase. |
| `silent` | The worker is alive but no output has appeared within the no-output window. | Warning with elapsed silence. |
| `blocked` | The worker cannot continue without input, permission, or missing context. | Blocker reason and next owner. |
| `stale_running` | The lease or heartbeat is stale while the task is not terminal. | Escalation and recovery action. |
| `failed` | The wrapper or task exited unsuccessfully. | Return code, stderr summary, and retry policy. |
| `done` | A final receipt exists and passed validation. | Artifacts, evidence, and review packet. |

Monitoring literature makes the same distinction in different language:
operators need signals that support action, not just status labels.[^sre-monitoring]
For agent harnesses, a silent worker with no receipt should become an explicit
blocked event. It should not hold the entire wave hostage while the operator
guesses whether it is thinking, stuck, or gone.

## Proposed Architecture: Codex Lane Runner

The next build should be a Codex-native lane runner.

It should not replace Codex. It should wrap Codex execution in durable process
control.

Core components:

1. SQLite queue or `tasks.json`.
2. Task leases with owner, TTL, and attempt counters.
3. Priority and lane fields.
4. Profile registry for role, sandbox, reasoning effort, timeout, workspace
   type, and allowed tools.
5. Workspace allocator.
6. Worktree allocator for write-capable tasks.
7. Read-only fixture workspace for benchmark tasks.
8. `codex exec` wrapper.
9. `--output-last-message` final receipt capture.
10. JSON event retention.
11. Heartbeat file.
12. Timeout controller.
13. Stale-running detector.
14. Provenance manifest.
15. Watcher and synthesis packet.
16. Controller/worker node model.

The build can be incremental:

1. Start with a local queue and receipt schema.
2. Add leases, attempts, and terminal-state validation.
3. Wrap `codex exec` so every run emits JSON events, heartbeat, and `final.md`.
4. Add stale-running detection and timeout conversion.
5. Add worktree allocation for write-capable tasks.
6. Add a watcher that turns terminal receipts into a synthesis packet.
7. Add controller/worker dispatch only after the single-node runner is reliable.

This order matters. A distributed runner without reliable local receipts only
makes failure harder to understand.

Example task record:

```json
{
  "task_id": "op_20260510_example_ab12cd",
  "lane": "state-audit",
  "profile": "codex-review",
  "status": "leased",
  "allowed_writes": ["reports/state-audit/"],
  "acceptance": [
    "produce final.md",
    "cite inspected files",
    "do not mutate live systems"
  ],
  "lease_owner": "worker-01",
  "lease_expires_at": "2026-05-10T20:30:00Z"
}
```

Example receipt:

```json
{
  "task_id": "op_20260510_example_ab12cd",
  "status": "done",
  "summary": "State audit completed against synthetic fixtures.",
  "artifacts": ["final.md", "provenance.json"],
  "evidence": ["fixtures/tasks.json", "fixtures/logs/run-17.jsonl"],
  "commands": [],
  "returncode": 0,
  "started_at": "2026-05-10T20:00:00Z",
  "ended_at": "2026-05-10T20:08:00Z",
  "review_required": true
}
```

The watcher should not merely print "done." It should produce an operator packet:

- completed lanes;
- blocked lanes;
- stale lanes;
- changed files;
- evidence inspected;
- claims requiring review;
- approval gates;
- next recommended action.

That packet is the difference between parallel work and parallel noise.

## Benchmark Design for the Next Phase

The benchmark should test the harness, not just the model.

This is proposed benchmark design, not completed evidence.

Use paired randomized fixtures. Each fixture runs once through Hermes and once
through Codex Lane Runner. Inputs, time limits, output schemas, and no-go
boundaries should match. Runner order should be randomized.

Benchmark data must be synthetic or sanitized. No live external mutations. No
private records. No message-system actions. No public endpoint changes. No
credentials.

Reviewer packets should be anonymized by stripping runner names, timestamps,
local paths, and formatting cues where feasible.

Suggested sample plan:

- pilot: `N = 40` paired fixtures;
- candidate full run: `N = 160` paired fixtures;
- total candidate executions: `320` runner executions;
- randomized runner order;
- stratified workload classes;
- bootstrap confidence intervals for paired quality differences.

Workload classes should be practical:

1. queue triage from task state;
2. document evidence extraction;
3. record-staging from synthetic CSV/SQLite;
4. no-send message drafting to local files;
5. failure recovery with corrupt inputs;
6. code modification with tests;
7. measurement from run logs;
8. synthesis from multiple receipts.

The primary endpoint should be paired mean quality difference:

`Delta Q = Q_codex_lane_runner - Q_hermes`

Report a stratified 95% bootstrap confidence interval. Treat the pilot as a
pilot. Do not turn it into a victory claim.

## Evaluation Metrics

The metrics should be readable enough for operators and strict enough for
engineers.

Primary components:

- correctness;
- completeness;
- evidence quality;
- decision quality;
- usability;
- safety-boundary adherence;
- auditability;
- reliability;
- latency;
- human review minutes;
- cost.

Quality score:

```text
Q = 0.35 correctness
  + 0.20 completeness
  + 0.15 evidence quality
  + 0.15 decision quality
  + 0.15 usability
```

Auditability score:

```text
A = 0.20 inputs
  + 0.20 steps
  + 0.20 artifacts
  + 0.20 decisions
  + 0.20 replayability
```

Exploratory value density:

```text
VD = (Q * B * R * A) / (latency_minutes * total_cost)
```

`B` is safety-boundary adherence. `R` is reliability. `A` is auditability.

Value density is not a primary endpoint. It mixes scales, so it can be useful
for tradeoff inspection but dangerous as the headline result. Report raw metrics
before composite scores.

The practical throughput lesson is enough: more workers help only when tasks are
independent, human approval does not become the serial bottleneck, and review
burden does not erase the parallelism gain.

## Public Data Boundary

Private operational records are not benchmark data.

Public release should use synthetic fixtures and sanitized evidence-shape
examples. Do not publish private paths, private vendors, model labels, contact
routes, record rows, host details, security posture, credentials, or live-system
counts.

A public paper can say that a private operational wave revealed a liveness gap
and reduced operator bookkeeping. It should not expose operational internals
unless they are separately sanitized and approved.

This boundary matters because the paper's value is the systems lesson, not the
private content of the work that surfaced it.

## Findings

1. **Hermes was better at operational control in the observed case study.**
   It made parallel work easier to supervise because lanes, state, acceptance
   criteria, boundaries, receipts, and watcher synthesis were visible.
2. **Codex was better as a direct execution substrate.** It offered stronger
   local code inspection, editing, command execution, subagent, worktree, and
   tool primitives.
3. **The performance difference was a harness difference.** The observed gap was
   not that one side was simply "smarter." The gap was whether parallel work
   became inspectable process state.
4. **Receipts changed the operator experience.** A final artifact per lane made
   it easier to review, reject, synthesize, and continue.
5. **Liveness was the sharpest reliability lesson.** "Still running" was not
   enough. A serious runner needs heartbeat, no-output timeout, max-runtime
   timeout, stale-running detection, blocked-state conversion, and structured
   failure reasons.
6. **The public benchmark has not been run yet.** Any superiority claim beyond
   the case-study dimensions above requires paired synthetic fixtures and
   blinded review.

## Implications

For operators, the finding is practical: do not evaluate agent systems only by
how smart the worker sounds. Evaluate whether the harness makes work bounded,
observable, reviewable, and recoverable.

For builders, the lesson is architectural: agent fleets need the same basic
control concepts as other operational systems. Queue state, leases, heartbeats,
timeouts, receipts, provenance, and review packets are not extras. They are the
interface that makes parallel delegation usable.

For Codex users, the opportunity is specific. Codex already has the execution
surface. A Codex-native lane runner should wrap that surface with durable task
state and public benchmark fixtures. If that layer is built, Codex can plausibly
match Hermes' observed operational strengths while keeping Codex's direct
execution advantages.

For researchers and reviewers, the next step is measurement. Run the same
fixtures through both harnesses, anonymize reviewer packets, report raw metrics
before composite scores, and separate throughput from review burden.

## Limitations

This paper is grounded in a single observed operational wave and local source
inspection. It is not a controlled benchmark.

Some implementation observations are not independently reproducible until
sanitized manifests are published. The proposed metrics and weights are
judgmental until validated. The benchmark may show that Hermes, Codex Lane
Runner, or some hybrid performs differently across workload classes.

That uncertainty is acceptable. The point of this paper is not to declare a
winner. The point is to identify the missing control plane and make the next
build measurable.

The next serious improvement in agentic work may not come from asking the model
to think harder. It may come from making every worker bounded, observable,
reviewable, and accountable.

## References

[^codex-cli]: OpenAI, "Codex CLI," OpenAI Developers, accessed 2026-05-10, https://developers.openai.com/codex/cli.
[^codex-subagents]: OpenAI, "Subagents," OpenAI Developers, accessed 2026-05-10, https://developers.openai.com/codex/subagents.
[^codex-sandbox]: OpenAI, "Sandbox," OpenAI Developers, accessed 2026-05-10, https://developers.openai.com/codex/concepts/sandboxing.
[^codex-worktrees]: OpenAI, "Worktrees," OpenAI Developers, accessed 2026-05-10, https://developers.openai.com/codex/app/worktrees.
[^sre-monitoring]: Rob Ewaschuk, "Monitoring Distributed Systems," in *Site Reliability Engineering*, Google, https://sre.google/sre-book/monitoring-distributed-systems/.
