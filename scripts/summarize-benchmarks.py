#!/usr/bin/env python3
"""Summarize synthetic benchmark run JSON."""

from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path


def quality(scores: dict[str, float]) -> float:
    return (
        0.35 * scores["correctness"]
        + 0.20 * scores["completeness"]
        + 0.15 * scores["evidence"]
        + 0.15 * scores["decision"]
        + 0.15 * scores["usability"]
    )


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: summarize-benchmarks.py <benchmark-run.json>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    tasks = data.get("tasks", [])
    if not tasks:
        print("tasks=0")
        return 0

    qualities = [quality(task["scores"]) for task in tasks]
    critical = sum(task["safety"]["critical"] for task in tasks)
    major = sum(task["safety"]["major"] for task in tasks)
    minor = sum(task["safety"]["minor"] for task in tasks)

    print(f"run_id={data.get('run_id')}")
    print(f"runner={data.get('runner')}")
    print(f"tasks={len(tasks)}")
    print(f"quality_mean={statistics.mean(qualities):.2f}")
    print(f"quality_min={min(qualities):.2f}")
    print(f"quality_max={max(qualities):.2f}")
    print(f"safety_critical={critical}")
    print(f"safety_major={major}")
    print(f"safety_minor={minor}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
