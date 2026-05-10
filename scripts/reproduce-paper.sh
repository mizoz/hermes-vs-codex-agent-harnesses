#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"$root/scripts/validate-data.sh"
"$root/scripts/summarize-benchmarks.py" "$root/data/sample/benchmark-run.example.json"
"$root/scripts/analyze-paired-benchmark.py" "$root/data/sample/benchmark-run.example.json"

echo "reproducibility-smoke-ok"
