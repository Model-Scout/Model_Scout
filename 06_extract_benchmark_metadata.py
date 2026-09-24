#!/usr/bin/env python3
"""Extract safe benchmark metadata from existing Stage 2 README snapshots.

This is an offline sidecar step. It never changes Stage 2/3/4 rows or vectors.
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Dict, List

from benchmark_metadata import extract_benchmarks


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
POOLS = ("core", "low_popularity")


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def write_jsonl_atomic(rows: List[Dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    os.close(fd)
    temporary = Path(name)
    try:
        with temporary.open("w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
                handle.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def read_readme(row: Dict[str, Any]) -> tuple[str, str]:
    readme = ((row.get("source") or {}).get("readme") or {})
    relative = readme.get("path")
    if not relative:
        return "", ""
    path = ROOT / relative
    if not path.exists():
        return "", str(relative)
    return path.read_text(encoding="utf-8", errors="replace"), str(relative)


def process_pool(pool: str) -> Dict[str, Any]:
    source_path = DATA_DIR / f"hf_models_stage2_{pool}.jsonl"
    output_path = DATA_DIR / f"hf_models_benchmark_{pool}.jsonl"
    rows = read_jsonl(source_path)
    output: List[Dict[str, Any]] = []
    stats = {
        "pool": pool,
        "rows": len(rows),
        "readme_available": 0,
        "numeric_results": 0,
        "ranking_eligible": 0,
        "mentions_only": 0,
        "variant_ambiguous": 0,
        "errors": 0,
    }
    for row in rows:
        try:
            text, relative_path = read_readme(row)
            if text:
                stats["readme_available"] += 1
            metadata = extract_benchmarks(row, text, relative_path)
            metadata["model_id"] = row.get("model_id")
            metadata["source_pool"] = pool
            metadata["source_stage1_version"] = (row.get("stage") or {}).get("source_stage1_version")
            metadata["source_stage2_version"] = (row.get("stage") or {}).get("stage2_version")
            output.append(metadata)
            summary = metadata["summary"]
            stats["numeric_results"] += summary["numeric_results"]
            stats["ranking_eligible"] += summary["ranking_eligible"]
            stats["mentions_only"] += summary["mentions_only"]
            stats["variant_ambiguous"] += summary["quantized_ambiguous"]
        except Exception as exc:
            stats["errors"] += 1
            output.append({
                "model_id": row.get("model_id"),
                "source_pool": pool,
                "benchmark_version": 1,
                "readme_available": False,
                "results": [],
                "mentions": [],
                "summary": {"numeric_results": 0, "ranking_eligible": 0, "mentions_only": 0, "quantized_ambiguous": 0},
                "error": {"type": type(exc).__name__, "message": str(exc)},
            })
    write_jsonl_atomic(output, output_path)
    stats["output"] = str(output_path)
    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool", choices=("core", "low_popularity", "all"), default="all")
    args = parser.parse_args()
    pools = POOLS if args.pool == "all" else (args.pool,)
    summaries = [process_pool(pool) for pool in pools]
    print(json.dumps({"benchmark_metadata_version": 1, "summaries": summaries}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

