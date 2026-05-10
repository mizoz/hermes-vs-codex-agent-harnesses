#!/usr/bin/env python3
"""Analyze paired Hermes/Codex benchmark JSON with a stratified bootstrap."""

from __future__ import annotations

import json
import random
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


def quality(scores: dict[str, float]) -> float:
    return (
        0.35 * scores["correctness"]
        + 0.20 * scores["completeness"]
        + 0.15 * scores["evidence"]
        + 0.15 * scores["decision"]
        + 0.15 * scores["usability"]
    ) / 100.0


def percentile(values: list[float], pct: float) -> float:
    if not values:
        raise ValueError("no values")
    ordered = sorted(values)
    idx = (len(ordered) - 1) * pct
    lo = int(idx)
    hi = min(lo + 1, len(ordered) - 1)
    frac = idx - lo
    return ordered[lo] * (1 - frac) + ordered[hi] * frac


def paired_deltas(tasks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_pair: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for task in tasks:
        by_pair[task["pair_id"]][task["runner"]] = task

    deltas: list[dict[str, Any]] = []
    for pair_id, runs in sorted(by_pair.items()):
        if "hermes" not in runs or "codex-native" not in runs:
            continue
        hermes = quality(runs["hermes"]["scores"])
        codex = quality(runs["codex-native"]["scores"])
        deltas.append(
            {
                "pair_id": pair_id,
                "workload_class": runs["hermes"]["workload_class"],
                "delta_q": codex - hermes,
            }
        )
    return deltas


def stratified_bootstrap(deltas: list[dict[str, Any]], iterations: int = 1000) -> tuple[float, float]:
    rng = random.Random(20260510)
    strata: dict[str, list[float]] = defaultdict(list)
    for row in deltas:
        strata[row["workload_class"]].append(row["delta_q"])

    boot: list[float] = []
    for _ in range(iterations):
        sample: list[float] = []
        for values in strata.values():
            sample.extend(rng.choice(values) for _ in values)
        boot.append(statistics.mean(sample))
    return percentile(boot, 0.025), percentile(boot, 0.975)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: analyze-paired-benchmark.py <benchmark-run.json>", file=sys.stderr)
        return 2

    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    deltas = paired_deltas(data.get("tasks", []))
    if not deltas:
        print("paired_fixtures=0")
        return 1

    mean_delta = statistics.mean(row["delta_q"] for row in deltas)
    ci_lower, ci_upper = stratified_bootstrap(deltas)
    print(f"run_id={data.get('run_id')}")
    print(f"paired_fixtures={len(deltas)}")
    print(f"mean_delta_q={mean_delta:.4f}")
    print(f"bootstrap_ci_95_lower={ci_lower:.4f}")
    print(f"bootstrap_ci_95_upper={ci_upper:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
