#!/usr/bin/env python3
"""Embed compact deterministic benchmark metadata into Stage 4 rows.

The original benchmark sidecars contain long supporting quotes and parser
audit details. Stage 4 only needs comparable result fields for ranking. This
script keeps the provenance path/hash and evidence reference, removes the
large quote payload from the index, and preserves all existing Stage 4 fields.
Run without --apply to validate counts and report the projected output size.
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
POOLS = ("core", "low_popularity")


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number}: expected JSON object")
            rows.append(value)
    return rows


def write_jsonl_atomic(rows: Sequence[Dict[str, Any]], path: Path) -> None:
    fd, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent)
    )
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with temporary.open("w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def compact_result(result: Dict[str, Any]) -> Dict[str, Any]:
    fields = (
        "benchmark",
        "dataset",
        "metric",
        "score",
        "higher_is_better",
        "split",
        "config",
        "evidence_ref",
        "model_name",
        "variant_kind",
        "variant_safe",
        "comparability",
        "self_reported",
        "ranking_eligible",
    )
    return {field: result.get(field) for field in fields if field in result}


def compact_mention(mention: Dict[str, Any]) -> Dict[str, Any]:
    fields = (
        "benchmark",
        "dataset",
        "metric",
        "model_name",
        "evidence_ref",
        "comparability",
        "reason",
        "self_reported",
    )
    return {field: mention.get(field) for field in fields if field in mention}


def compact_sidecar(sidecar: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "benchmark_version": sidecar.get("benchmark_version"),
        "readme_available": bool(sidecar.get("readme_available")),
        "readme_path": sidecar.get("readme_path"),
        "readme_sha256": sidecar.get("readme_sha256"),
        "summary": sidecar.get("summary") or {},
        "results": [
            compact_result(result)
            for result in sidecar.get("results", [])
            if result.get("ranking_eligible") is True
        ],
        "mentions": [
            compact_mention(mention)
            for mention in sidecar.get("mentions", [])
            if isinstance(mention, dict)
        ],
    }


def process_pool(pool: str, apply: bool) -> Dict[str, Any]:
    stage4_path = DATA_DIR / f"hf_models_stage4_{pool}.jsonl"
    sidecar_path = DATA_DIR / f"hf_models_benchmark_{pool}.jsonl"
    rows = read_jsonl(stage4_path)
    sidecars = {row.get("model_id"): row for row in read_jsonl(sidecar_path)}
    if len(rows) != len(sidecars):
        raise ValueError(f"[{pool}] row count mismatch: stage4={len(rows)} sidecar={len(sidecars)}")

    stage4_ids = {row.get("model_id") for row in rows}
    sidecar_ids = set(sidecars)
    if stage4_ids != sidecar_ids:
        missing = sorted(stage4_ids - sidecar_ids)[:5]
        extra = sorted(sidecar_ids - stage4_ids)[:5]
        raise ValueError(f"[{pool}] model_id mismatch: missing={missing} extra={extra}")

    merged: List[Dict[str, Any]] = []
    for row in rows:
        updated = dict(row)
        updated["benchmark_metadata"] = compact_sidecar(sidecars[row["model_id"]])
        merged.append(updated)

    if apply:
        write_jsonl_atomic(merged, stage4_path)

    eligible = sum(len(row["benchmark_metadata"]["results"]) for row in merged)
    mentions = sum(len(row["benchmark_metadata"]["mentions"]) for row in merged)
    return {
        "pool": pool,
        "rows": len(rows),
        "ranking_eligible_results": eligible,
        "mentions": mentions,
        "apply": apply,
        "output": str(stage4_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool", choices=[*POOLS, "all"], default="all")
    parser.add_argument("--apply", action="store_true", help="atomically replace Stage 4 files")
    args = parser.parse_args()

    pools = POOLS if args.pool == "all" else (args.pool,)
    summaries = [process_pool(pool, args.apply) for pool in pools]
    print(json.dumps({"summaries": summaries}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
