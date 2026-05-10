#!/usr/bin/env python3
"""Validate public-package hygiene without external dependencies."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_PATTERNS = [
    re.compile(r"/" + r"home/[A-Za-z0-9_.-]+"),
    re.compile("REPLACE" + "-ME"),
    re.compile("Co-" + r"Authored-By:\s*(Codex|AI|Assistant)", re.I),
    re.compile("Generated " + r"with (Codex|AI|ChatGPT)", re.I),
    re.compile("Generated " + r"by (Codex|AI|ChatGPT)", re.I),
    re.compile(r"AI[- ]assisted", re.I),
    re.compile("Created " + r"by (Codex|AI|ChatGPT|Assistant)", re.I),
    re.compile("Built " + r"with (Codex|AI|ChatGPT|Assistant)", re.I),
    re.compile("Reviewed " + r"by (Codex|AI|ChatGPT|Assistant)", re.I),
    re.compile(r"\b(CRM|ERPNext|Maton|DocuSeal|Gmail|Stripe|Supabase|Vercel)\b", re.I),
    re.compile(r"danger-full-access", re.I),
    re.compile(r"\b(ollama|anthropic|gemini|sonnet|opus)\b", re.I),
    re.compile(r"\bgpt-[0-9]", re.I),
    re.compile(r"business-record|mailbox|outreach|prospect|customer", re.I),
    re.compile(r"commercial strategy", re.I),
    re.compile(r"operator-worktrees|available models|network policy", re.I),
    re.compile(r"Public launch|real workflow|non- interactive|recordreview", re.I),
]

TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".json", ".cff", ".bib", ".css", ".mmd", ".sh", ".py", ".txt", ".html"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_json(path: str) -> object:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def validate_json() -> None:
    for path in [
        "data/schema/benchmark-run.schema.json",
        "data/schema/task-result.schema.json",
        "data/schema/harness-profile.schema.json",
        "data/sample/benchmark-run.example.json",
        "data/sample/task-result.example.json",
    ]:
        read_json(path)


def validate_task_result(task: dict[str, object]) -> None:
    required = {
        "task_id",
        "pair_id",
        "fixture_id",
        "seed",
        "repetition",
        "workload_class",
        "runner",
        "profile",
        "model",
        "sandbox",
        "prompt_hash",
        "fixture_hashes",
        "randomization_order",
        "runner_order",
        "time_limit_seconds",
        "started_at",
        "ended_at",
        "terminal_state",
        "input_hashes",
        "output_hashes",
        "commands_or_tools",
        "return_code",
        "retry_count",
        "human_review_minutes",
        "scores",
        "safety",
        "scorer",
    }
    missing = required - set(task)
    if missing:
        fail(f"task result missing keys {sorted(missing)}")
    scores = task.get("scores")
    if not isinstance(scores, dict):
        fail("task result scores must be an object")
    for key in ["correctness", "completeness", "evidence", "decision", "usability"]:
        value = scores.get(key)
        if not isinstance(value, (int, float)) or not 0 <= value <= 100:
            fail(f"task score {key} must be 0..100")
    safety = task.get("safety")
    if not isinstance(safety, dict):
        fail("task result safety must be an object")
    for key in ["critical", "major", "minor"]:
        value = safety.get(key)
        if not isinstance(value, int) or value < 0:
            fail(f"safety {key} must be a non-negative integer")
    scorer = task.get("scorer")
    if not isinstance(scorer, dict):
        fail("task result scorer must be an object")
    for key in ["scorer_id", "blinded", "rubric_version"]:
        if key not in scorer:
            fail(f"task result scorer missing {key}")


def validate_samples() -> None:
    run = read_json("data/sample/benchmark-run.example.json")
    if not isinstance(run, dict):
        fail("benchmark sample must be an object")
    for key in ["run_id", "created_at", "design", "tasks"]:
        if key not in run:
            fail(f"benchmark sample missing {key}")
    tasks = run.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        fail("benchmark sample needs non-empty tasks")
    for task in tasks:
        if not isinstance(task, dict):
            fail("benchmark task must be an object")
        validate_task_result(task)

    single = read_json("data/sample/task-result.example.json")
    if not isinstance(single, dict):
        fail("task sample must be an object")
    validate_task_result(single)


def validate_text_hygiene() -> None:
    for path in ROOT.rglob("*"):
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            fail(f"{path.relative_to(ROOT)}: remove local bytecode/cache files before release packaging")
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        if path.relative_to(ROOT).as_posix() == "scripts/validate-package.py":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(ROOT)
        for pattern in FORBIDDEN_PATTERNS:
            match = pattern.search(text)
            if match:
                fail(f"{rel}: forbidden public-release text matched {pattern.pattern!r}: {match.group(0)!r}")


def validate_pdf_text() -> None:
    pdf = ROOT / "dist" / "whitepaper.pdf"
    if not pdf.exists() or shutil.which("pdftotext") is None:
        return
    text = subprocess.check_output(["pdftotext", str(pdf), "-"], text=True, errors="ignore")
    for pattern in FORBIDDEN_PATTERNS:
        match = pattern.search(text)
        if match:
            fail(f"dist/whitepaper.pdf: forbidden public-release text matched {pattern.pattern!r}: {match.group(0)!r}")
    if "$$" in text or "\\frac" in text:
        fail("dist/whitepaper.pdf: raw TeX appears in extracted text")


def main() -> int:
    validate_json()
    validate_samples()
    validate_text_hygiene()
    validate_pdf_text()
    print("package-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
