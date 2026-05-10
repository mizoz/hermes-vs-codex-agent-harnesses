# Social Launch Copy

## LinkedIn Post 1

I am releasing a public case-study comparison on agent harnesses: how
operational control systems shape the usefulness of agentic software work.

The paper compares two modes:

Hermes operator-fleet: a queue-backed, profile-based local harness with bounded
lanes, receipts, worktrees, approval boundaries, and status surfaces.

Codex-native lane running: direct use of Codex CLI/app primitives such as local
execution, subagents, worktrees, sandboxing, tools, and non-interactive runs.

As of 2026-05-10, the case-study finding is deliberately narrow:

Hermes was better at multi-lane operational control.
Codex was better as a direct execution substrate.

This is not a controlled benchmark result. It is a public case-study finding:
model quality alone does not explain operator throughput. The harness around
the model matters.

The next step is the paired benchmark: synthetic workloads, randomized ordering,
fixed scoring rubrics, no live record-system or message-system mutation, and
clear provenance records.

The real question is not "which agent is smarter?" It is: "what control plane
turns agent work into something inspectable, bounded, and reviewable?"

https://mizoz.github.io/hermes-vs-codex-agent-harnesses/

## LinkedIn Post 2

A single agent session can be powerful. A fleet of agents can become cognitive
debt unless the harness answers basic operational questions:

What work is running?
Who owns it?
What can it change?
What evidence did it inspect?
What did it produce?
What failed?
What needs human approval?

That is the lens of my paper, "Agent Harnesses as Operational Control
Systems."

The case study compares Hermes operator-fleet and Codex-native lane running.
Hermes made multi-lane work feel more coherent because it externalized
coordination: lanes, task state, receipts, profile boundaries, and watcher
surfaces.

Codex exposes documented first-party primitives: local CLI, subagents,
worktrees, sandboxing, plugins, and non-interactive execution.

As of 2026-05-10, the comparison found Hermes stronger at multi-lane
coordination and Codex stronger as an execution substrate.

The proposed architecture is hybrid: Codex execution wrapped in a more durable
lane runner with heartbeats, timeouts, provenance manifests, stale-worker
detection, and cross-machine scheduling.

This is a case-study finding, not a controlled benchmark win. The benchmark
still has to run.

https://mizoz.github.io/hermes-vs-codex-agent-harnesses/

## LinkedIn Post 3

One lesson from operating agent workflows: parallelism is not free.

Adding workers only helps until coordination, review, retry, and blocked-state
overhead dominate. In agentic work, the harness is where those costs either
become visible or stay hidden.

I wrote a white paper comparing Hermes operator-fleet and Codex-native lane
running as agent harnesses.

The narrow finding: in one observed workflow, Hermes was better at operational
control. Codex was better as a direct execution substrate. The missing layer is
durable multi-worker process control around the execution.

The paper proposes a Codex-native lane runner with leased task queues, profile
registry, worktree allocator, heartbeat files, timeout and stale-running
detection, retained JSON events, provenance manifests, terminal receipts, and
synthetic benchmark fixtures.

This is public case-study evidence. The honest next milestone is controlled
measurement, not victory language.

https://mizoz.github.io/hermes-vs-codex-agent-harnesses/

## LinkedIn Carousel Outline

Title: Agent Harnesses as Operational Control Systems

Slide 1: The Problem
Agent work is moving from one prompt to delegated lanes. Without a harness,
parallel agents become cognitive load.

Slide 2: The Core Question
Not "which model is best?"
"What control plane makes agent work bounded, inspectable, and reviewable?"

Slide 3: Two Modes Compared
Hermes operator-fleet: queue, profiles, lanes, receipts, watcher loops.
Codex-native: CLI, subagents, worktrees, sandboxing, tools, non-interactive
execution.

Slide 4: What Hermes Made Visible
Task ownership, allowed writes, approval boundaries, acceptance criteria,
terminal receipts, and lane status.

Slide 5: What Codex Already Has
Documented first-party primitives: code editing, shell, app worktrees,
sandboxing, subagents, plugins, MCP, and direct verification.

Slide 6: The Gap
Raw capability does not automatically become durable process control.

Slide 7: Current Finding
Hermes was better at multi-lane operational control. Codex was better as a
direct execution substrate.

Slide 8: Liveness Matters
A silent worker is different from a slow worker. Agent harnesses need heartbeat,
timeout, stale-running, and blocked-state semantics.

Slide 9: Benchmark Boundary
No live record-system, message-system, external contact, public endpoint, or
paid SaaS mutation. Use synthetic or sanitized fixtures.

Slide 10: Proposed Architecture
Codex execution plus a Hermes-like lane runner: queue, leases, profiles,
worktrees, receipts, provenance, watcher synthesis.

Slide 11: Current Status
Case-study findings, not controlled benchmark results. Next step: paired
randomized evaluation.

## X Thread 1

1/ I am releasing a public case-study comparison on agent harnesses: how
operational control systems shape agentic software work.

The comparison is Hermes operator-fleet vs Codex-native lane running.

https://mizoz.github.io/hermes-vs-codex-agent-harnesses/

2/ The claim is narrow.

As of 2026-05-10:

Hermes was better at multi-lane operational control.
Codex was better as a direct execution substrate.

This is a case-study finding, not a controlled benchmark result.

3/ Hermes made multi-lane work feel coherent because it exposed lanes, profiles,
task state, worktrees, approval boundaries, receipts, and watcher status.

That matters when work is messy and parallel.

4/ Codex has documented first-party primitives: CLI, local execution, subagents,
worktrees, sandboxing, plugins, tools, and non-interactive runs.

The gap is not raw capability. It is durable multi-worker process control.

5/ The proposed direction: a Codex-native lane runner with leases, heartbeats,
timeouts, stale-worker detection, retained JSON events, output schemas, and
provenance manifests.

6/ The benchmark still needs to run.

The package lays out paired synthetic workloads, randomized ordering, scoring
rubrics, and strict no-live-system mutation boundaries.

7/ The useful question is not "which agent wins overall?"

It is: what harness turns strong execution into work that is bounded,
inspectable, repeatable, and safe to review?

https://github.com/mizoz/hermes-vs-codex-agent-harnesses/releases/download/v0.1.0-draft/whitepaper.pdf

## X Thread 2

1/ Parallel agents can create throughput. They can also create confusion.

A harness is the difference between delegated work and a pile of half-visible
activity.

https://mizoz.github.io/hermes-vs-codex-agent-harnesses/

2/ The draft paper compares Hermes operator-fleet and Codex-native lane running
as operational control systems.

Hermes = queue-backed lanes and receipts.
Codex-native = powerful direct execution primitives.

3/ The observed case-study finding:

Hermes was better at operational control: task state, review artifacts,
boundaries, receipts, watcher surfaces.

Codex was better as the execution substrate.

4/ The weak point found in the Hermes-style setup was liveness.

A worker could be running with no strong heartbeat or structured progress trail.
Slow is not the same as silent.

5/ The proposed fix is boring and important:

heartbeats, wall-clock timeouts, stale-running transitions, blocked-state
conversion, retained event logs, and structured failure reasons.

6/ Agent harnesses should be evaluated like systems, not vibes.

Synthetic fixtures. Paired runs. Blind scoring where possible. No live
record-system, message-system, or external-contact mutations.

7/ The paper now frames the work as comparison, methodology, and architecture.
Controlled superiority claims wait until the benchmark is executed.

https://github.com/mizoz/hermes-vs-codex-agent-harnesses/releases/download/v0.1.0-draft/whitepaper.pdf

## Short X Posts

1. Agent fleets need more than strong models. They need lanes, receipts,
approval boundaries, provenance, and liveness controls. https://mizoz.github.io/hermes-vs-codex-agent-harnesses/

2. The case-study finding is conservative: Hermes was better at multi-lane
operational control; Codex was better as a direct execution substrate. https://mizoz.github.io/hermes-vs-codex-agent-harnesses/

3. A silent agent worker is not just "still running." It is an operational state
that needs heartbeat, timeout, and blocked/failure semantics. https://mizoz.github.io/hermes-vs-codex-agent-harnesses/

4. The useful agent question is shifting from "which model?" to "what harness
makes delegated work inspectable and reviewable?" https://mizoz.github.io/hermes-vs-codex-agent-harnesses/

5. New case-study comparison: agent harnesses as operational control systems.
Hermes won operational control; Codex won direct execution substrate. Benchmark
claims still need paired synthetic runs. https://mizoz.github.io/hermes-vs-codex-agent-harnesses/

## General Announcement Blurbs

Ahmed Mahmoud of ZalaStack has released "Agent Harnesses as Operational Control
Systems," a public case-study comparison of Hermes operator-fleet and
Codex-native lane running. As of 2026-05-10, the finding is that Hermes was
better at multi-lane operational control, while Codex was better as a direct
execution substrate.

New public case-study package from Ahmed Mahmoud / ZalaStack: Hermes showed the
stronger operational control plane; Codex showed the stronger execution
substrate. The paper proposes a Codex-native lane runner with leases, receipts,
heartbeats, timeouts, provenance manifests, and synthetic benchmark fixtures.
