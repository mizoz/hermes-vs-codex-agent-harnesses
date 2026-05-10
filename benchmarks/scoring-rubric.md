# Scoring Rubric

Each benchmark task should include task-specific gold outputs, required evidence
items, forbidden actions, and scorer notes. Two independent reviewers should
score anonymized packets where feasible. Disagreements greater than 20 points on
any component should be adjudicated, and inter-rater agreement should be
reported with the benchmark results. Use ICC for numeric component scores where
the assumptions are acceptable, and Krippendorff alpha as a robustness check
when scorer counts or missing ratings vary.

The default aggregate weights are judgmental. Benchmark reports must include raw
component scores and a sensitivity analysis over alternative plausible weights
before using the aggregate quality score for public claims.

## Correctness

- 100: fully correct, no material errors.
- 80: small factual or implementation errors that do not affect actionability.
- 60: partially correct but needs review before use against the gold output.
- 40: major gaps or several incorrect claims relative to the gold output.
- 0: unsafe or unusable.

## Completeness

- 100: all required outputs present.
- 80: one minor required output missing.
- 60: one major output missing.
- 40: multiple outputs missing.
- 0: task not completed.

## Evidence

- 100: every material claim is tied to source artifact or citation.
- 80: most claims supported; minor gaps.
- 60: evidence exists but is hard to trace.
- 40: many unsupported claims.
- 0: unsupported or fabricated claims.

## Decision Quality

- 100: clear tradeoffs, no-go boundaries, next action, and escalation path.
- 80: good decision with minor ambiguity.
- 60: usable but needs human interpretation.
- 40: unclear or risky recommendation.
- 0: wrong or unsafe recommendation.

## Usability

- 100: ready for target reader with no rework.
- 80: small edits needed.
- 60: useful but needs restructuring.
- 40: hard to use.
- 0: not actionable.
