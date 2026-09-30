#!/usr/bin/env python3
"""Convert case-based semantic golden labels into the retrieval query schema.

Input is `golden_retrieval_queries_v2.jsonl` (neutral schema written from real
model-selection cases). Output is `semantic_golden_queries.jsonl`, which
`05_validate_retrieval.py --query-file` can run directly. Label fields are kept
under `labels` so `test/evaluate_semantic_golden.py` can score the report.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


HERE = Path(__file__).resolve().parent
SOURCE_PATH = HERE / "golden_retrieval_queries_v2.jsonl"
OUTPUT_PATH = HERE / "semantic_golden_queries.jsonl"

ROUTING = {
    "semantic_capability": {"primary": "dense", "dense_bias": "high", "sparse_bias": "low", "metadata_filter": "hard"},
    "semantic_constraint": {"primary": "hybrid", "dense_bias": "medium", "sparse_bias": "medium", "metadata_filter": "hard"},
    "structured_constraint": {"primary": "metadata", "dense_bias": "low", "sparse_bias": "medium", "metadata_filter": "hard"},
}


def query_signals(conditions: Dict[str, Any]) -> List[str]:
    signals = ["language", "task"]
    if conditions.get("max_params_b") is not None or conditions.get("gpu_vram_gb") is not None:
        signals.append("numeric_constraint")
    if conditions.get("license_requirement") == "commercial":
        signals.append("license_constraint")
    if conditions.get("runtime") not in (None, "unknown"):
        signals.append("runtime_constraint")
    return signals


def query_type(item: Dict[str, Any]) -> str:
    conditions = item["conditions"]
    if item["expected_behavior"] in ("must_exclude_only", "warn_on_oversize"):
        return "structured_constraint"
    if conditions.get("max_params_b") is not None or conditions.get("gpu_vram_gb") is not None:
        return "semantic_constraint"
    return "semantic_capability"


def convert(item: Dict[str, Any]) -> Dict[str, Any]:
    conditions = item["conditions"]
    kind = query_type(item)
    return {
        "id": f"sg_{item['query_id']}",
        "text": item["query"],
        "tasks": conditions["tasks"],
        "korean_required": conditions.get("language") == "ko",
        "max_parameters_billion": conditions.get("max_params_b"),
        "min_context_length": conditions.get("min_context"),
        "pools": ["core", "low_popularity"],
        "top_k": 5,
        "suite": "semantic_golden",
        "query_schema_version": 2,
        "query_type": kind,
        "query_signals": query_signals(conditions),
        "routing_hint": ROUTING[kind],
        # Conditions 05_validate_retrieval.py does not filter on yet; kept for scoring.
        "license_requirement": conditions.get("license_requirement"),
        "runtime": conditions.get("runtime"),
        "gpu_vram_gb": conditions.get("gpu_vram_gb"),
        "finetune_planned": conditions.get("finetune_planned"),
        "label_type": item["label_type"],
        "evaluable_now": item["evaluable_now"],
        "blocked_by": item.get("blocked_by") or [],
        "known_failure_cause": item.get("known_failure_cause"),
        "labels": {
            "expected_behavior": item["expected_behavior"],
            "expected_any": item["expected_any"],
            "acceptable": item["acceptable"],
            "must_exclude": item["must_exclude"],
            "needs_review": item["needs_review"],
            "warn_rule": item.get("warn_rule"),
        },
        "source_case_id": item["source_case_id"],
        "source_url": item["source_url"],
        "evidence_quote": item.get("evidence_quote"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE_PATH)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()

    items = [json.loads(line) for line in args.source.read_text(encoding="utf-8").splitlines() if line.strip()]
    rows = [convert(item) for item in items]
    args.output.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    print(json.dumps({"queries": len(rows), "evaluable_now": sum(row["evaluable_now"] for row in rows), "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
