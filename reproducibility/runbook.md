# Reproducibility Runbook

## Local Smoke

```bash
cd <repo-root>
./scripts/validate-data.sh
./scripts/summarize-benchmarks.py data/sample/benchmark-run.example.json
```

## Full Benchmark

1. Generate synthetic fixtures.
2. Hash all fixtures.
3. Freeze task prompts.
4. Run paired tasks through Hermes and Codex-native in randomized order.
5. Store raw outputs under `data/raw/` if sanitized.
6. Convert task receipts to `TaskResult` JSON.
7. Score blind where possible.
8. Run statistical analysis.
9. Update `paper/manuscript.md` findings.

## Release Rule

Do not publish raw operational traces. If a trace comes from private work, reduce
it to a sanitized metric row and remove all identifying content.
