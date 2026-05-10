# Abstract

This paper compares two practical harness patterns for agentic software work:
Hermes operator-fleet, a queue-backed multi-worker launcher, and Codex-native
lane running, which uses Codex CLI/app capabilities directly. The case study
suggests that the decisive performance variable is not simply model capability.
For multi-lane operational work, the paper argues that the control surface around
the model matters:
task contracts, explicit approval boundaries, worktree isolation, model-role
profiles, durable receipts, queue state, watcher processes, and failure
classification.

In the motivating case study, Hermes operator-fleet exposed more explicit
operational scaffolding for parallel, auditable work. Codex provides documented
first-party execution primitives: CLI, subagents, sandbox controls, worktrees,
local tools, and non-interactive execution. The highest-leverage path
is therefore not to choose one as a universal winner, but to test a Codex-native
lane runner that adopts Hermes-style queue discipline while adding stronger
heartbeat, timeout, provenance, benchmark, and cross-machine scheduling controls.

The paper proposes a paired benchmark framework using synthetic workloads,
queueing-theoretic throughput metrics, reliability and auditability scores, and
human-review cost. It also defines public-release boundaries so private
operational systems are not exposed in the evaluation.
