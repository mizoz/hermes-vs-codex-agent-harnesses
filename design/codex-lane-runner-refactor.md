# Codex Lane Runner Refactor

## Goal

Build a Codex-native supervisor that matches Hermes operator-fleet's durable
lane discipline and improves on its liveness, provenance, and cross-machine
scheduling.

## Why

Native Codex has strong execution primitives, but the operator-facing work
ledger is not explicit enough for large parallel operational waves. Hermes
operator-fleet shows the useful shape: queue, profiles, worktrees, bounded
prompts, tmux/process isolation, status, and receipts. The refactor should keep
that shape while adding stronger execution telemetry.

## Non-Goals

- Do not replace Codex.
- Do not replace Hermes Kanban.
- Do not use live record, message, or payment systems in benchmark mode.
- Do not publish private operational data.

## Components

### Queue

`tasks.json` or SQLite table:

- `id`
- `title`
- `lane`
- `profile`
- `repo`
- `workdir`
- `allowed_writes`
- `acceptance`
- `prompt_hash`
- `status`
- `priority`
- `lease_host`
- `lease_pid`
- `lease_expires_at`
- `attempt`
- `created_at`
- `started_at`
- `completed_at`

### Profiles

`profiles.json`:

- `engine`: `codex`, `external-model-sidecar`, `local-model-sidecar`, `noop-fixture`
- `model`
- `reasoning_effort`
- `sandbox`
- `workspace`
- `max_parallel`
- `timeout_seconds`
- `heartbeat_seconds`
- `allowed_tools`
- `role`

Default: read-only unless `allowed_writes` is non-empty.

### Run Directory

```text
runs/<task-id>/
|-- prompt.md
|-- prompt.sha256
|-- codex-events.jsonl
|-- stderr.txt
|-- final.md
|-- receipt.json
|-- heartbeat.json
`-- artifacts/
```

### Receipt

`receipt.json`:

- task id
- runner
- profile
- host
- model
- sandbox
- start/end/elapsed
- command
- return code
- files changed
- commands run
- input hashes
- output hashes
- safety status
- blockers
- next owner

### Liveness

Each worker wrapper updates `heartbeat.json` every 30 seconds:

```json
{
  "task_id": "op_...",
  "pid": 1234,
  "updated_at": "2026-05-10T13:30:00-06:00",
  "phase": "running-codex-exec",
  "last_output_bytes": 4096
}
```

Watcher rule:

- no heartbeat within 2 intervals: `stale_warning`;
- no heartbeat within 4 intervals: mark `blocked_stale`;
- process exited non-zero: `failed`;
- process alive but no output beyond timeout: terminate wrapper and mark
  `timeout`.

### Cross-Machine Scheduling

One approved node remains controller. Other approved nodes can be workers.

Host file:

```json
{
  "node": "worker-class-a",
  "enabled": true,
  "max_parallel": 4,
  "lanes": ["research", "benchmark", "code-review"],
  "forbidden": ["live-record-systems", "live-message-systems", "payments"],
  "workspace": "configured-worker-workspace"
}
```

Task lease is acquired atomically. Results sync back through git or an approved
file-sync path.

## Improvements Over Hermes Operator-Fleet

- Heartbeats instead of silent tmux panes.
- Timeouts by profile.
- JSON Schema final receipts.
- Retained Codex JSONL by default.
- Stale worker detection.
- Node leases for controller/worker scheduling.
- Safer default sandbox.
- Explicit plugin/tool allowlist.
- Benchmark-ready metrics fields.

## Compatibility

The runner should still be able to launch existing Hermes-like tasks and emit
`final.md` so humans can read outputs without special tooling.
