# Benchmark Harness Plan

## Question

Which runner produces more verified task value per unit time, cost, and review
burden under controlled no-live-system conditions?

## Runners

- `H`: Hermes operator-fleet.
- `C`: Codex-native lane runner.

## Design

Use a paired randomized design. Every task is run by both systems with the same
inputs, same no-go boundaries, same time limit, and same expected output schema.

Randomize order:

- 50% Hermes first, Codex second.
- 50% Codex first, Hermes second.

Blind scoring where feasible: hide runner identity from the evaluator. Before
scoring, normalize output packets by stripping runner names, model names, local
paths, receipt formatting, timestamps, and other surface cues.

## Sample Size

Unit of analysis:

- `N` means paired fixtures, not total runner executions.
- Each paired fixture is executed once by each runner.
- Repetition seeds should be treated as clustered within workload class.

Minimum pilot:

\[
N = 40
\]

Candidate full run before power analysis:

\[
N = 8 \times 10 \times 2 = 160
\]

## Hypotheses

Primary endpoint:

- paired mean quality difference, `Delta Q = Q_C - Q_H`.

Primary analysis:

- stratified 95% bootstrap confidence interval for `Delta Q`, stratified by
  workload class.

Pilot rule:

- `N = 40` is a pilot unless a separate power analysis justifies stronger
  inferential claims.

Non-inferiority threshold:

- accept non-inferiority only if the lower confidence bound of `Delta Q` is
  greater than `-0.05` on a normalized `[0, 1]` quality scale.

Secondary endpoints:

- safety-boundary adherence;
- auditability;
- review minutes;
- wall-clock latency;
- reliability;
- exploratory value density.

## Data Collection

Each task must capture:

- task id;
- pair id;
- fixture id;
- seed;
- repetition;
- workload class;
- runner id;
- profile/model;
- sandbox/permission mode;
- prompt hash;
- randomization order;
- time limit;
- start/end timestamps;
- input fixture hashes;
- output artifact hashes;
- command/tool summary;
- return code;
- retry count;
- safety violations;
- human review minutes;
- final score.

## No-Go Systems

Do not use live external systems, live record systems, message systems,
signature-workflow systems, production workflow automation, payment systems,
DNS, public endpoints, or real private entity data.

## Terminal States

- `accepted`
- `accepted_with_minor_edits`
- `rejected_quality`
- `rejected_safety`
- `blocked`
- `timeout`
- `runner_failed`
