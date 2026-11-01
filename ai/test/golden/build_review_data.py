#!/usr/bin/env python3
"""Assemble the data file for the team review page (no API key).

Three sections, one query list each:
- golden:  the 28 golden queries. Cards are the models already in their labels
           (expected_any / acceptable / must_exclude / needs_review), each with
           its current role, so reviewers can agree or disagree with the label.
- batch1:  judging pool for labels/judging_queries_batch1.jsonl (12 per query)
- batch2:  judging pool for labels/judging_queries_batch2.jsonl (8 per query)
- batch3:  judging pool for labels/judging_queries_batch3.jsonl (identifier, benchmark, constrained)
- batch4:  judging pool for labels/judging_queries_batch4.jsonl (comparison, reference, identifier)

Every query carries its query_type from the label file so the page can show it.
Pool sources are dropped so judges do not see how a candidate was picked.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[2]
GOLDEN_DIR = ROOT / "test" / "golden"
GOLDEN_LABELS = GOLDEN_DIR / "labels" / "golden_queries.jsonl"
POOLS = {
    "batch1": GOLDEN_DIR / "reports" / "judging_pool_batch1.json",
    "batch2": GOLDEN_DIR / "reports" / "judging_pool_batch2.json",
    "batch3": GOLDEN_DIR / "reports" / "judging_pool_batch3.json",
    "batch4": GOLDEN_DIR / "reports" / "judging_pool_batch4.json",
}
SECTION_TITLES = {"batch1": "1차 판정", "batch2": "2차 판정", "batch3": "3차 판정", "batch4": "4차 판정"}
OUTPUT_PATH = GOLDEN_DIR / "reports" / "review_page_data.json"
ROLES = (("expected_any", "정답"), ("acceptable", "허용"), ("must_exclude", "제외"), ("needs_review", "경고 필요"))


def load_module(name: str, path: Path):
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def golden_section(pool_builder, validator) -> List[Dict[str, Any]]:
    rows = {row["model_id"].casefold(): row for row in validator.load_rows()}
    stage2 = {r["model_id"]: r for pool in validator.POOLS for r in read_jsonl(ROOT.parent / "backend" / "data" / f"hf_models_stage2_{pool}.jsonl")}
    stage3 = {r["model_id"]: r for pool in validator.POOLS for r in read_jsonl(ROOT.parent / "backend" / "data" / f"hf_models_stage3_{pool}.jsonl")}
    queries = []
    for label in read_jsonl(GOLDEN_LABELS):
        cards: List[Dict[str, Any]] = []
        seen = set()
        for field, role in ROLES:
            for item in label.get(field) or []:
                model_id = item["model_id"] if isinstance(item, dict) else item
                if model_id.casefold() in seen:
                    continue
                seen.add(model_id.casefold())
                row = rows.get(model_id.casefold())
                if row:
                    card = pool_builder.candidate_facts(row, stage2.get(row["model_id"], {}), stage3.get(row["model_id"], {}))
                    card["in_db"] = True
                else:
                    card = {"model_id": model_id, "url": f"https://huggingface.co/{model_id}", "in_db": False}
                card["label_role"] = role
                if isinstance(item, dict) and item.get("reason"):
                    card["label_reason"] = item["reason"]
                cards.append(card)
        reliability = label.get("reliability") or {}
        verification = label.get("source_verification") or {}
        queries.append(
            {
                "query_id": label["query_id"],
                "query_type": label.get("query_type"),
                "query": label["query"],
                "conditions": label["conditions"],
                "candidates": cards,
                "golden": {
                    "label_type": label["label_type"],
                    "expected_behavior": label["expected_behavior"],
                    "tier": reliability.get("tier"),
                    "case_confidence": reliability.get("case_confidence"),
                    "issues": reliability.get("issues") or [],
                    "source_case_id": label["source_case_id"],
                    "source_url": label["source_url"],
                    "evidence_quote": label.get("evidence_quote"),
                    "verification_note": verification.get("note"),
                    "notes": label.get("notes"),
                    "warn_rule": (label.get("warn_rule") or {}).get("pass_if"),
                },
            }
        )
    return queries


def pool_section(path: Path, query_types: Dict[str, str]) -> List[Dict[str, Any]]:
    pool = json.loads(path.read_text(encoding="utf-8"))
    for query in pool["queries"]:
        query["query_type"] = query_types.get(query["query_id"])
        for card in query["candidates"]:
            card.pop("pool_sources", None)
    return pool["queries"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()

    validator = load_module("model_scout_validator", ROOT / "05_validate_retrieval.py")
    pool_builder = load_module("model_scout_pool", GOLDEN_DIR / "build_judging_pool.py")
    query_types = {
        item["query_id"]: item.get("query_type")
        for name in POOLS
        for item in read_jsonl(GOLDEN_DIR / "labels" / f"judging_queries_{name}.jsonl")
    }
    sections = [{"id": "golden", "title": "골든셋 검토", "queries": golden_section(pool_builder, validator)}]
    sections += [{"id": name, "title": SECTION_TITLES[name], "queries": pool_section(path, query_types)} for name, path in POOLS.items()]
    args.output.write_text(json.dumps({"created": "2026-10-01", "sections": sections}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(json.dumps({s["id"]: [len(s["queries"]), sum(len(q["candidates"]) for q in s["queries"])] for s in sections}, ensure_ascii=False))


if __name__ == "__main__":
    main()
