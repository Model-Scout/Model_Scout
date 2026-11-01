#!/usr/bin/env python3
"""Build candidate pools for human relevance judging (no API key).

For each query in labels/judging_queries_batch1.jsonl:
1. Keep DB rows that pass the retriever's hard filters (task, Korean, size, context).
2. Collapse each canonical family to one representative (original repo first).
3. Interleave the BM25 ranking (query text + English pool_terms) with the
   download ranking until POOL_SIZE candidates are chosen. If fewer families
   are eligible, all of them are judged.
4. Attach the facts a judge needs (license, size, Korean evidence, runtime,
   README-grounded claims) and shuffle the display order with a fixed seed so
   judges are not anchored by pool rank.

pool_terms only steer which candidates are judged; they are never scored.
The pool source of each candidate is kept in the JSON but not shown to judges.

Queries that name models (`reference_models`) are handled by query_type:
- model_comparison: the named models are the whole pool.
- reference_anchored: the named model is shown first as the anchor (even if it
  fails the hard filter), and its family is left out of the regular pool.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[2]
GOLDEN_DIR = ROOT / "test" / "golden"
QUERY_PATH = GOLDEN_DIR / "labels" / "judging_queries_batch1.jsonl"
OUTPUT_PATH = GOLDEN_DIR / "reports" / "judging_pool_batch1.json"
POOL_SIZE = 12
SEED = 20261001
CLAIM_FIELDS = ("use_cases", "documented_strengths", "documented_limitations", "warnings", "license_notes")


def load_module(name: str, path: Path):
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


class CachedBM25:
    """Same fields, boosts and tokenizer as compare_dense_sparse.FieldedBM25, with per-doc counts cached."""

    def __init__(self, rows: List[Dict[str, Any]], sparse) -> None:
        self.fields = ("model_id", "task", "metadata", "content")
        self.boosts = {"model_id": 4.0, "task": 2.0, "metadata": 2.0, "content": 1.0}
        docs = [sparse.field_tokens(row) for row in rows]
        self.counts = [{field: Counter(doc[field]) for field in self.fields} for doc in docs]
        self.lengths = [{field: len(doc[field]) for field in self.fields} for doc in docs]
        n = len(docs)
        self.avg = {field: sum(length[field] for length in self.lengths) / max(n, 1) or 1.0 for field in self.fields}
        df = {field: Counter() for field in self.fields}
        for count in self.counts:
            for field in self.fields:
                df[field].update(count[field].keys())
        self.idf = {
            field: {token: math.log(1.0 + (n - value + 0.5) / (value + 0.5)) for token, value in df[field].items()}
            for field in self.fields
        }

    def score(self, index: int, query_tokens: List[str]) -> float:
        total = 0.0
        for field in self.fields:
            counts = self.counts[index][field]
            length = self.lengths[index][field]
            for token in query_tokens:
                tf = counts.get(token, 0)
                if not tf:
                    continue
                norm = tf + 1.2 * (0.25 + 0.75 * length / self.avg[field])
                total += self.boosts[field] * self.idf[field][token] * (tf * 2.2 / norm)
        return total


def run_query(query: Dict[str, Any]) -> Dict[str, Any]:
    conditions = query["conditions"]
    return {
        "id": query["query_id"],
        "text": query["query"],
        "tasks": conditions["tasks"],
        "korean_required": conditions.get("language") == "ko",
        "max_parameters_billion": conditions.get("max_params_b"),
        "min_context_length": conditions.get("min_context"),
        "pools": ["core", "low_popularity"],
    }


def claims(semantic: Dict[str, Any]) -> Dict[str, List[str]]:
    output = {}
    for field in CLAIM_FIELDS:
        texts = [str(item.get("text") or "").strip() for item in (semantic.get(field) or []) if isinstance(item, dict)]
        texts = [text for text in texts if text][:2]
        if texts:
            output[field] = texts
    return output


def korean_evidence(stage2: Dict[str, Any]) -> List[str]:
    values = ((stage2.get("language") or {}).get("korean") or {}).get("evidence") or []
    return [value if isinstance(value, str) else json.dumps(value, ensure_ascii=False) for value in values][:3]


def candidate_facts(row: Dict[str, Any], stage2: Dict[str, Any], stage3: Dict[str, Any]) -> Dict[str, Any]:
    model = stage2.get("model") or {}
    weights = (stage2.get("hardware") or {}).get("weights_only") or {}
    runtime = stage2.get("runtime_compatibility") or {}
    quant = stage2.get("quantization") or {}
    family = stage2.get("family") or {}
    return {
        "model_id": row["model_id"],
        "url": f"https://huggingface.co/{row['model_id']}",
        "task": (row.get("task") or {}).get("primary"),
        "license": stage2.get("license"),
        "parameters_b": model.get("parameter_count_billion"),
        "context_length": model.get("context_length"),
        "weights_gib": {key: weights.get(key) for key in ("fp16_gib", "int8_gib", "int4_gib") if weights.get(key) is not None},
        "quantization": quant.get("method") if quant.get("enabled") else None,
        "is_variant": bool(family.get("is_variant")),
        "base_model": (family.get("declared_base_models") or [None])[0],
        "downloads": ((stage2.get("popularity") or {}).get("current") or {}).get("downloads"),
        "korean_evidence": korean_evidence(stage2),
        "runtime": {key: (runtime.get(key) or {}).get("status") for key in ("cpu", "cuda", "mps", "llama_cpp", "onnx")},
        "evidence_completeness": (stage3.get("semantic") or {}).get("evidence_completeness"),
        "claims": claims(stage3.get("semantic") or {}),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--queries", type=Path, default=QUERY_PATH)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    parser.add_argument("--pool-size", type=int, default=POOL_SIZE)
    args = parser.parse_args()

    validator = load_module("model_scout_validator", ROOT / "05_validate_retrieval.py")
    sparse = load_module("model_scout_sparse", ROOT / "test" / "compare_dense_sparse.py")
    rows = validator.load_rows()
    stage2 = {r["model_id"]: r for pool in validator.POOLS for r in read_jsonl(ROOT / "data" / f"hf_models_stage2_{pool}.jsonl")}
    stage3 = {r["model_id"]: r for pool in validator.POOLS for r in read_jsonl(ROOT / "data" / f"hf_models_stage3_{pool}.jsonl")}
    bm25 = CachedBM25(rows, sparse)
    rng = random.Random(SEED)

    by_id = {row["model_id"].casefold(): index for index, row in enumerate(rows)}

    def facts_at(index: int) -> Dict[str, Any]:
        return candidate_facts(rows[index], stage2.get(rows[index]["model_id"], {}), stage3.get(rows[index]["model_id"], {}))

    def family(index: int) -> str:
        return (rows[index].get("filter_metadata") or {}).get("canonical_model_id") or rows[index]["model_id"]

    output = []
    for query in read_jsonl(args.queries):
        spec = run_query(query)
        named = []
        for model_id in query.get("reference_models") or []:
            if model_id.casefold() not in by_id:
                raise SystemExit(f"{query['query_id']}: reference model not in DB: {model_id}")
            named.append(by_id[model_id.casefold()])
        role = "비교 대상" if query.get("query_type") == "model_comparison" else "기준 모델"
        anchors = []
        for index in named:
            card = facts_at(index)
            card["label_role"] = role
            card["pool_sources"] = ["reference"]
            anchors.append(card)
        meta = {"query_type": query.get("query_type")} if query.get("query_type") else {}
        if query.get("query_type") == "model_comparison":
            output.append({"query_id": query["query_id"], **meta, "query": query["query"], "conditions": query["conditions"],
                           "eligible_rows": len(named), "eligible_families": len(named), "candidates": anchors})
            continue
        anchor_families = {family(index) for index in named}
        eligible = [index for index, row in enumerate(rows) if validator.hard_filter(row, spec)[0] and family(index) not in anchor_families]

        families: Dict[str, int] = {}
        for index in eligible:
            row = rows[index]
            key = family(index)
            current = families.get(key)
            if current is None:
                families[key] = index
                continue
            def rank(i: int):
                meta = rows[i].get("filter_metadata") or {}
                return (not meta.get("is_variant"), meta.get("downloads") or 0)
            if rank(index) > rank(current):
                families[key] = index
        reps = list(families.values())

        terms = sparse.query_keywords(query["query"] + " " + query.get("pool_terms", ""))
        by_bm25 = sorted(reps, key=lambda i: (-bm25.score(i, terms), rows[i]["model_id"]))
        by_downloads = sorted(reps, key=lambda i: (-((rows[i].get("filter_metadata") or {}).get("downloads") or 0), rows[i]["model_id"]))

        chosen: Dict[int, List[str]] = {}
        for position in range(len(reps)):
            for source, ranking in (("bm25", by_bm25), ("downloads", by_downloads)):
                if len(chosen) >= args.pool_size:
                    break
                if position < len(ranking):
                    chosen.setdefault(ranking[position], []).append(f"{source}#{position + 1}")
            if len(chosen) >= args.pool_size:
                break

        candidates = []
        for index, sources in chosen.items():
            facts = facts_at(index)
            facts["pool_sources"] = sources
            candidates.append(facts)
        rng.shuffle(candidates)
        output.append(
            {
                "query_id": query["query_id"],
                **meta,
                "query": query["query"],
                "conditions": query["conditions"],
                "eligible_rows": len(eligible),
                "eligible_families": len(reps),
                "candidates": anchors + candidates,
            }
        )

    args.output.write_text(json.dumps({"seed": SEED, "pool_size": args.pool_size, "queries": output}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({q["query_id"]: [q["eligible_families"], len(q["candidates"])] for q in output}, ensure_ascii=False))


if __name__ == "__main__":
    main()
