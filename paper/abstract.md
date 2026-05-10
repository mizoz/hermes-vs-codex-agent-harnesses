# Abstract

This paper argues that the practical performance of agentic software work is
not determined by model capability alone. In an observed private operational
wave, Hermes operator-fleet felt more effective for messy parallel work because
it exposed a clearer operational control plane: lanes, task state, acceptance
criteria, approval boundaries, receipts, watcher loops, and terminal status.

Codex already provides documented first-party execution primitives including
CLI execution, non-interactive execution, sandbox and approval controls,
subagents, worktrees, tools, and code editing. The missing layer is durable
multi-worker process control around those primitives.

The proposed next architecture is a Codex-native lane runner: Codex execution
wrapped in queue state, task leases, workspace allocation, provenance manifests,
heartbeats, timeouts, stale-worker detection, final receipts, and operator
review packets. The paper separates case-study observation from proposed
benchmark design and defines public-data boundaries for evaluating the harness
using synthetic or sanitized fixtures.
