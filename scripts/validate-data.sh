#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 -m json.tool "$root/data/schema/benchmark-run.schema.json" >/dev/null
python3 -m json.tool "$root/data/schema/task-result.schema.json" >/dev/null
python3 -m json.tool "$root/data/schema/harness-profile.schema.json" >/dev/null
python3 -m json.tool "$root/data/sample/benchmark-run.example.json" >/dev/null
python3 -m json.tool "$root/data/sample/task-result.example.json" >/dev/null

echo "json-ok"
python3 "$root/scripts/validate-package.py"
