#!/usr/bin/env python3
"""Convert case-based semantic golden labels into the retrieval query schema.

Input is `labels/golden_queries.jsonl` (neutral schema written from real
model-selection cases). Output is `labels/semantic_golden_queries.jsonl`, which
`05_validate_retrieval.py --query-file` can run directly. Label fields are kept
under `labels` so `test/evaluate_semantic_golden.py` can score the report.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


HERE = Path(__file__).resolve().parent
SOURCE_PATH = HERE / "labels" / "golden_queries.jsonl"
OUTPUT_PATH = HERE / "labels" / "semantic_golden_queries.jsonl"

ROUTING = {
    "model_comparison": {"primary": "lookup", "dense_bias": "low", "sparse_bias": "high", "metadata_filter": "none", "resolve_reference": True},
    "reference_anchored": {"primary": "hybrid", "dense_bias": "medium", "sparse_bias": "high", "metadata_filter": "hard", "resolve_reference": True},
    "identifier_match": {"primary": "bm25", "dense_bias": "low", "sparse_bias": "high", "metadata_filter": "hard"},
    "benchmark_lookup": {"primary": "bm25", "dense_bias": "medium", "sparse_bias": "high", "metadata_filter": "hard", "benchmark_boost": "required"},
    "constrained_search": {"primary": "hybrid", "dense_bias": "medium", "sparse_bias": "medium", "metadata_filter": "hard"},
    "semantic_capability": {"primary": "dense", "dense_bias": "high", "sparse_bias": "low", "metadata_filter": "hard"},
}


NUMERIC_CONDITIONS = ("max_params_b", "gpu_vram_gb", "ram_gb", "min_context")


def query_signals(conditions: Dict[str, Any]) -> List[str]:
    signals = ["language", "task"]
    if any(conditions.get(key) is not None for key in NUMERIC_CONDITIONS):
        signals.append("numeric_constraint")
    if conditions.get("license_requirement") == "commercial":
        signals.append("license_constraint")
    if conditions.get("runtime") not in (None, "unknown"):
        signals.append("runtime_constraint")
    return signals


def query_type(item: Dict[str, Any]) -> str:
    # Hand-assigned type in the label file wins; the rules below are the fallback.
    if item.get("query_type"):
        return item["query_type"]
    conditions = item["conditions"]
    if item["expected_behavior"] == "warn_on_oversize":
        return "reference_anchored"
    if any(conditions.get(key) is not None for key in NUMERIC_CONDITIONS):
        return "constrained_search"
    if conditions.get("license_requirement") == "commercial":
        return "constrained_search"
    return "semantic_capability"


def convert(item: Dict[str, Any]) -> Dict[str, Any]:
    conditions = item["conditions"]
    kind = query_type(item)
    row = {
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
        "ram_gb": conditions.get("ram_gb"),
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
        "source_case_id": item.get("source_case_id"),
        "source_url": item.get("source_url"),
        "evidence_quote": item.get("evidence_quote"),
        "source_verification": item.get("source_verification"),
    }
    # Judged labels (import_judgments.py) carry extra fields; case-based labels do not.
    if item["label_type"] == "judged":
        row["suite"] = "judged_golden"
        row["labels"]["expected_all"] = item.get("expected_all") or []
        row["reference_models"] = item.get("reference_models") or []
        row["answer_grade"] = item.get("answer_grade")
    return row


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
