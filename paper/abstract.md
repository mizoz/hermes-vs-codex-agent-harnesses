# Abstract

This paper compares Hermes operator-fleet and Codex-native lane running as
agent harnesses for parallel work. As of 2026-05-10, the case-study finding is
that Hermes was better at multi-lane operational control: decomposition,
visible task state, acceptance criteria, approval boundaries, receipts, watcher
synthesis, and operator bookkeeping.

Codex was better as a direct execution substrate: local code inspection,
editing, command execution, tool use, subagents, worktrees, and sandboxed
workspace work. The difference was therefore not mainly model quality. It was
harness quality.

The proposed next architecture is a Codex-native lane runner: Codex execution
wrapped in queue state, task leases, workspace allocation, provenance manifests,
heartbeats, timeouts, stale-worker detection, final receipts, and operator
review packets. The paper separates observed findings, interpretation, and
future benchmark claims, and defines public-data boundaries for evaluating the
harness using synthetic or sanitized fixtures.
