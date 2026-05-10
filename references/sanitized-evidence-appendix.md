# Sanitized Evidence Appendix

This appendix shows the evidence shape used in the case study without exposing
private paths, hostnames, model labels, plugin inventories, local security
posture, private records, message data, private-entity identifiers, or live
system state.

## Representative Task Record

```json
{
  "id": "op_YYYYMMDD-HHMMSS_lane_slug_digest",
  "title": "Bounded lane task",
  "lane": "research-or-review",
  "profile": "planner",
  "repo": "sanitized-workspace",
  "allowed_write": ["reports/example-output.md"],
  "acceptance": "Return a concise report with evidence paths and approval gates.",
  "approval_boundary": "Read-only unless an explicit allowed output path is provided.",
  "status": "running"
}
```

## Representative Profile Record

```json
{
  "name": "planner",
  "runner": "codex-native",
  "engine": "provider-neutral-coding-model",
  "workspace": "worktree",
  "sandbox": "read-only",
  "max_parallel": 2,
  "timeout_seconds": 1800,
  "role": "planning and synthesis"
}
```

## Representative Run Receipt

```json
{
  "task_id": "op_YYYYMMDD-HHMMSS_lane_slug_digest",
  "started_at": "2026-05-10T13:00:00-06:00",
  "ended_at": "2026-05-10T13:08:00-06:00",
  "terminal_state": "done",
  "artifacts": ["reports/example-output.md"],
  "evidence": ["docs/example-source.md"],
  "no_go_actions": ["no sends", "no live-system writes", "no public endpoint changes"],
  "summary": "Completed bounded review and produced a terminal receipt."
}
```

## Representative Status Snapshot

```json
{
  "queued": 1,
  "running": 3,
  "done": 8,
  "blocked": 1,
  "failed": 0,
  "cancelled": 0,
  "stale_running": 1
}
```

These records are illustrative. They document the shape of the harness evidence,
not the private implementation or live operating data.
