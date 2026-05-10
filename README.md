# Agent Harnesses as Operational Control Systems

This repository contains a public white paper package about agent harnesses as
operational control systems.

- Hermes operator-fleet: a queue-backed, profile-based, multi-worker harness
  that launches bounded agent workers through local task state.
- Codex-native lane running: direct use of Codex CLI/app subagents, tools,
  worktrees, sandboxing, and non-interactive execution without an additional
  queue controller.

The core claim is narrow: model quality alone does not explain operator
throughput. A harness that captures lanes, task state, leases, approval
boundaries, receipts, provenance, liveness, and review packets can reduce
coordination overhead in multi-lane operational work. Quantitative superiority
claims require the paired benchmark described in this repository.

## Public Links

- Project page: https://mizoz.github.io/hermes-vs-codex-agent-harnesses/
- Release page: https://github.com/mizoz/hermes-vs-codex-agent-harnesses/releases/tag/v0.1.0-draft
- PDF: https://github.com/mizoz/hermes-vs-codex-agent-harnesses/releases/download/v0.1.0-draft/whitepaper.pdf

## Current Status

Public draft research package. This is not a benchmark-results paper.
Quantitative claims require executing the paired benchmark described here.

## Author

Ahmed Mahmoud, ZalaStack, Calgary, Alberta, Canada.

GitHub: [@mizoz](https://github.com/mizoz)

## Repository Map

| Path | Purpose |
|---|---|
| `paper/manuscript.md` | Main white paper draft. |
| `paper/abstract.md` | Short abstract. |
| `references/` | Source inventory and BibTeX references. |
| `references/sanitized-evidence-appendix.md` | Public-safe evidence-shape examples. |
| `benchmarks/` | Evaluation design, metrics, workloads, and scoring rubric. |
| `data/schema/` | JSON Schemas for benchmark and provenance records. |
| `data/sample/` | Synthetic sample records only. |
| `reproducibility/` | Runbook and environment notes. |
| `publication/` | Release checklist and editorial QA gates. |
| `scripts/` | Local validation and summarization helpers. |

## Scope

This work studies harnesses, not private business data. Public artifacts should
use synthetic fixtures or sanitized operational traces. No live record-system,
message-system, payment, signature-workflow, DNS, or public
endpoint actions are part of the benchmark.

## Reproducibility

Run:

```bash
./scripts/validate-data.sh
./scripts/summarize-benchmarks.py data/sample/benchmark-run.example.json
./scripts/analyze-paired-benchmark.py data/sample/benchmark-run.example.json
```

The current sample data is illustrative. A valid comparative result requires a
paired benchmark run as described in `benchmarks/harness-plan.md`.

No assistant, model, or bot byline should be added to commits, releases,
metadata, pull requests, or the paper.
