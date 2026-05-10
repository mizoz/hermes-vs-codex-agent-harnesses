# Internal Case-Study Summary

This file records non-public evidence categories used to motivate the paper.
It intentionally avoids local absolute paths, private hostnames, private entity
data, and credential-bearing files.

## Observed Harness Properties

- Queue-backed task records with stable task ids.
- Profile registry for Codex and provider-neutral sidecar roles.
- Read-only default behavior when no write scope is approved.
- Isolated workspaces for worker execution.
- Per-run prompts and final receipts.
- Status/event surface for task transitions.
- Human approval boundary embedded in worker prompts.

## Observed Weaknesses

- Worker liveness was hard to assess while a long-running task produced no
  visible receipt.
- Status snapshots could lag the true worker state.
- Runtime events were not always retained by default.
- Public reproducibility requires sanitized manifests because the motivating
  implementation lives in private operational repos.

## Public Use

These observations support the paper's case-study framing. They do not support
quantitative superiority claims.
