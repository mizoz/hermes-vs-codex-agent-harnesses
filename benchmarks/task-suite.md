# Synthetic Task Suite

Use local fixtures only.

## Workload Classes

1. Public-request discovery simulation
   - Inputs: archived HTML, saved PDFs, synthetic search result pages.
   - Output: opportunity table, evidence links, reject/hold reasons.

2. Record-staging simulation
   - Inputs: synthetic CSV/SQLite records with duplicate and malformed rows.
   - Output: clean import packet, dedupe report, missing-field report.

3. Operational graduation decision
   - Inputs: mock reply records, meeting notes, opportunity stages.
   - Output: promote/hold/reject with rationale.

4. No-send message drafting
   - Inputs: local `.eml` or markdown thread fixtures.
   - Output: text-only draft packet and approval flags.

5. Queue triage
   - Inputs: task JSON with priorities, lanes, blockers, deadlines.
   - Output: ordered execution plan and blocked list.

6. Evidence extraction
   - Inputs: local PDFs, HTML, screenshots, DOCX fixtures.
   - Output: structured facts with source references.

7. Failure recovery
   - Inputs: corrupt files, missing fields, ambiguous instructions.
   - Output: graceful escalation with no invented facts.

8. Measurement/reporting
   - Inputs: local run logs.
   - Output: metrics summary, confidence intervals, anomaly notes.

## Fixture Rules

- No private entity data.
- No credential values.
- No live service calls.
- Each fixture gets a SHA256 hash.
- Expected outputs must be specified before running the task.
