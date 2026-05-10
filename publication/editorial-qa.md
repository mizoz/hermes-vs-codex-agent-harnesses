# Editorial QA

## Strong Claims Currently Supported

- Hermes operator-fleet has a durable task queue, profiles, worktree/scratch
  isolation, tmux sessions, and `final.md` receipts. Supported by local source
  inspection.
- Codex has native execution primitives including CLI, subagents, sandboxing,
  and worktrees. Supported by official OpenAI documentation.
- Provenance and audit trails are central to trust in generated artifacts.
  Supported by W3C PROV.
- Parallel worker speedup is constrained by serial coordination and review.
  Supported by Amdahl/Gustafson framing and queueing theory.

## Claims Not Yet Supported

- "Codex-native is faster than Hermes."
- "Hermes is more accurate than Codex-native."
- "A specific percentage productivity gain exists."
- "Public benchmark results prove superiority."

These require executing the paired benchmark.

## Risky Wording To Avoid

- "proves"
- "guarantees"
- "fully autonomous"
- "production-safe"
- "scientifically validated" before benchmark execution
- "compliant" unless tied to an actual compliance review

## Current Release Assessment

Public-safe as a draft methodology repo after final approval. Not ready as a
results paper until benchmark data is generated and scored.

## Latest QA Notes

- Local path leaks were scrubbed from public text and generated HTML.
- Strong "winner" language was changed to case-study and hypothesis language.
- Internal implementation evidence is labeled as non-public case-study evidence.
- Package validation now checks placeholders, local paths, attribution strings,
  and sample shape.
