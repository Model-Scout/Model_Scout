#!/usr/bin/env python3
"""Run the semantic golden queries with the local BM25 retriever (no API key).

Reuses the hard filters and canonical dedup of 05_validate_retrieval.py and the
FieldedBM25 scorer of test/compare_dense_sparse.py, and writes a report in the
same shape as 05_validate_retrieval.py so test/evaluate_semantic_golden.py can
score it. Dense (vector) retrieval still needs OPENAI_API_KEY; this is the
sparse baseline.

Each report also records where the first expected model ranks among *all*
eligible candidates, which separates filter failures (answer never eligible)
from ranking failures (eligible but below top-k).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


ROOT = Path(__file__).resolve().parents[2]
GOLDEN_DIR = ROOT / "test" / "golden"
QUERY_PATH = GOLDEN_DIR / "labels" / "semantic_golden_queries.jsonl"
REPORT_PATH = GOLDEN_DIR / "reports" / "semantic_golden_retrieval_bm25.json"


def load_module(name: str, path: Path):
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def first_position(model_ids: List[str], targets: List[str]) -> Optional[int]:
    wanted = {target.casefold() for target in targets}
    for position, model_id in enumerate(model_ids, start=1):
        if model_id.casefold() in wanted:
            return position
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--queries", type=Path, default=QUERY_PATH)
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    args = parser.parse_args()

    validator = load_module("model_scout_validator", ROOT / "05_validate_retrieval.py")
    sparse = load_module("model_scout_sparse", ROOT / "test" / "compare_dense_sparse.py")
    queries = [json.loads(line) for line in args.queries.read_text(encoding="utf-8").splitlines() if line.strip()]
    rows = validator.load_rows()
    bm25 = sparse.FieldedBM25(rows)

    reports: List[Dict[str, Any]] = []
    for query in queries:
        candidates = [index for index, row in enumerate(rows) if validator.hard_filter(row, query)[0]]
        boosts = validator.benchmark_adjustments([rows[index] for index in candidates], query)
        ranked = sparse.dedupe_indices(rows, bm25.rank(candidates, query, len(candidates), validator, boosts))
        top = ranked[: int(query.get("top_k", 5))]
        ranked_ids = [rows[index].get("model_id", "") for index in ranked]
        eligible_ids = {rows[index].get("model_id", "").casefold() for index in candidates}
        expected = (query.get("labels") or {}).get("expected_any") or []
        reports.append(
            {
                "query_id": query["id"],
                "text": query["text"],
                "mode": "bm25_offline",
                "candidate_count": len(candidates),
                "top_k": len(top),
                "diagnostics": {
                    "expected_eligible": sorted(model_id for model_id in expected if model_id.casefold() in eligible_ids),
                    # Position after canonical dedup; a dedup-collapsed answer shows as None here.
                    "expected_rank_all_candidates": first_position(ranked_ids, expected),
                    # Position of the row that took the answer's canonical slot, if any.
                    "expected_family_rank_all_candidates": first_position(
                        [str((rows[index].get("filter_metadata") or {}).get("canonical_model_id") or "") for index in ranked],
                        expected,
                    ),
                    "dedup_removed_expected": bool(
                        first_position(ranked_ids, expected) is None
                        and any(model_id.casefold() in eligible_ids for model_id in expected)
                    ),
                },
                "results": [
                    {
                        "model_id": rows[index].get("model_id"),
                        "canonical_model_id": (rows[index].get("filter_metadata") or {}).get("canonical_model_id"),
                        "source_pool": rows[index].get("source_pool"),
                        "task": (rows[index].get("task") or {}).get("primary"),
                        "parameter_count": (rows[index].get("filter_metadata") or {}).get("parameter_count"),
                    }
                    for index in top
                ],
            }
        )

    args.report.write_text(
        json.dumps({"mode": "bm25_offline", "query_count": len(queries), "reports": reports}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"mode": "bm25_offline", "queries": len(queries), "report": str(args.report)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
