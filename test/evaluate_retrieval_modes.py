#!/usr/bin/env python3
"""Evaluate dense, sparse, and planner-weighted hybrid retrieval by query type.

The golden set currently contains deterministic constraints but no human-judged
relevant model IDs.  This script therefore reports hard-constraint precision,
keyword-hit proxy, evidence completeness, empty rate, and conflict rate.  It
does not label any of those proxies as semantic Recall@5.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import os
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Tuple



ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DEFAULT_QUERY_FILE = ROOT / "test" / "retrieval_queries.jsonl"
DEFAULT_JSON = ROOT / "test" / "retrieval_accuracy_by_type.json"
DEFAULT_MD = ROOT / "test" / "retrieval_accuracy_by_type.md"
POOLS = ("core", "low_popularity")
TOP_K = 5

QUERY_TYPE_DESCRIPTIONS = {
    "semantic_capability": "자연어로 모델의 능력·사용 목적을 설명하며 표현 변형을 이해해야 하는 질의",
    "lexical_exact": "모델명·번역 방향·형식명처럼 정확한 문자열 매칭이 중요한 질의",
    "structured_constraint": "task·파라미터·컨텍스트·인기도·확인된 메타데이터 조건이 중심인 질의",
    "benchmark_lookup": "benchmark·dataset·metric·README 근거를 찾는 질의",
    "semantic_constraint": "한국어·task 같은 의미 조건과 수치·메타데이터 조건을 함께 포함한 질의",
    "abstention": "조건을 만족하는 후보가 없을 때 빈 결과를 유지해야 하는 질의",
}

TOKEN_RE = re.compile(r"[\w가-힣]+", re.UNICODE)
STOPWORDS = {
    "한국어", "모델", "모델을", "모델이", "모델의", "위한", "사용", "사용할",
    "추천", "추천해줘", "찾아줘", "찾는", "있는", "있고", "모두", "확인된",
    "지원", "지원하는", "처리", "처리할", "가능한", "용", "중", "이상", "이하",
    "and", "the", "for", "model", "models", "with", "from", "to",
}


def load_validator():
    path = ROOT / "05_validate_retrieval.py"
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location("model_scout_validator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def query_tokens(text: str) -> List[str]:
    # Use the production language/pair normalizer so evaluation mirrors retrieval.
    return sorted(__import__("retrieval_metadata").normalize_query_terms(text or ""))



def row_tokens(row: Mapping[str, Any]) -> set[str]:
    # Use the same fields users can search in the BM25 shadow index.
    metadata = row.get("filter_metadata") or {}
    task = row.get("task") or {}
    values: List[Any] = [
        row.get("model_id"),
        row.get("embedding_text"),
        task.get("primary"),
        task.get("matched"),
        metadata,
    ]
    output: set[str] = set()
    for value in values:
        if isinstance(value, dict):
            value = json.dumps(value, ensure_ascii=False)
        elif isinstance(value, (list, tuple, set)):
            value = " ".join(str(item) for item in value)
        output.update(token.casefold() for token in TOKEN_RE.findall(str(value or "")))
    return output


def exact_keyword_hit(row: Mapping[str, Any], keywords: Sequence[str]) -> bool:
    return bool(row_tokens(row).intersection(keywords))


def cosine(left: Sequence[float], right: Sequence[float]) -> float:
    if not left or not right or len(left) != len(right):
        return -1.0
    dot = sum(float(a) * float(b) for a, b in zip(left, right))
    left_norm = sum(float(value) ** 2 for value in left) ** 0.5
    right_norm = sum(float(value) ** 2 for value in right) ** 0.5
    if not left_norm or not right_norm:
        return -1.0
    return dot / (left_norm * right_norm)


def type_description(query_type: str) -> str:
    return QUERY_TYPE_DESCRIPTIONS.get(query_type, "분류되지 않은 질의")


def embed_queries(queries: Sequence[Mapping[str, Any]]) -> Dict[int, List[float]]:
    try:
        from dotenv import load_dotenv
        load_dotenv(ROOT / ".env")
    except ImportError:
        pass
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY가 필요합니다. 비용 없는 재사용 모드는 지원하지 않습니다.")
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("openai 패키지가 필요합니다.") from exc
    client = OpenAI(api_key=api_key)
    response = client.embeddings.create(
        model=os.getenv("STAGE4_EMBEDDING_MODEL", "text-embedding-3-small"),
        input=[str(query.get("text") or "") for query in queries],
    )
    return {item.index: item.embedding for item in response.data}


def score_rows(
    validator: Any,
    rows: Sequence[Dict[str, Any]],
    eligible: Sequence[int],
    query: Dict[str, Any],
    query_vector: Sequence[float] | None,
    mode: str,
    sparse_index: Any = None,
) -> List[Dict[str, Any]]:
    benchmark = validator.benchmark_adjustments(rows, query)
    dense_weight, sparse_weight = validator.retrieval_weights(query, has_dense_vector=True)
    if sparse_index is None:
        sparse_index = validator.FieldedBM25(rows)
    scored: List[Dict[str, Any]] = []
    for index in eligible:
        row = dict(rows[index])
        dense_score = max(0.0, cosine(query_vector or [], row.get("embedding") or []))
        sparse_score = float(validator.lexical_relevance(row, query, sparse_index=sparse_index))
        if mode == "dense":
            base = dense_score
        elif mode == "sparse":
            base = sparse_score
        elif mode == "hybrid":
            base = dense_weight * dense_score + sparse_weight * sparse_score
        else:
            raise ValueError(f"unknown mode: {mode}")
        conflict = validator.detect_task_conflict(row)
        benchmark_boost = float((benchmark.get(row.get("model_id", "")) or {}).get("boost", 0.0))
        row["_adjusted_score"] = base - float(conflict.get("ranking_penalty", 0.0)) + benchmark_boost
        row["_dense_score"] = dense_score
        row["_sparse_score"] = sparse_score
        row["_task_conflict"] = bool(conflict.get("conflict"))
        scored.append(row)
    scored.sort(key=lambda item: (-float(item["_adjusted_score"]), str(item.get("model_id", ""))))
    return validator.diversify_results(scored, TOP_K)



def relevance_metrics(top: Sequence[Mapping[str, Any]], query: Mapping[str, Any]) -> Dict[str, Any]:
    """Compute true ranking metrics only when human labels are present."""
    relevant = {str(value) for value in (query.get("relevant_model_ids") or []) if value}
    if not relevant:
        return {"labeled": False, "recall_at_5": None, "mrr": None, "ndcg_at_5": None, "relevant_count": 0}
    ranked = [str(row.get("model_id")) for row in top]
    hits = [index for index, model_id in enumerate(ranked, start=1) if model_id in relevant]
    recall = len(set(ranked[:TOP_K]) & relevant) / len(relevant)
    mrr = 1.0 / hits[0] if hits else 0.0
    dcg = sum(1.0 / math.log2(index + 1.0) for index in hits if index <= TOP_K)
    ideal_hits = min(len(relevant), TOP_K)
    idcg = sum(1.0 / math.log2(index + 1.0) for index in range(1, ideal_hits + 1))
    return {
        "labeled": True,
        "recall_at_5": round(recall, 4),
        "mrr": round(mrr, 4),
        "ndcg_at_5": round(dcg / idcg, 4) if idcg else 0.0,
        "relevant_count": len(relevant),
    }


def evaluate_mode(
    validator: Any,
    rows: Sequence[Dict[str, Any]],
    queries: Sequence[Dict[str, Any]],
    vectors: Mapping[int, Sequence[float] | None],
    mode: str,
    sparse_index: Any = None,
) -> Dict[str, Any]:
    per_query: List[Dict[str, Any]] = []
    type_rows: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for query_index, query in enumerate(queries):
        eligible = [
            index for index, row in enumerate(rows)
            if validator.hard_filter(row, query)[0]
        ]
        started = time.perf_counter()
        results = score_rows(validator, rows, eligible, query, vectors[query_index], mode, sparse_index=sparse_index)
        latency_ms = (time.perf_counter() - started) * 1000.0
        keywords = query_tokens(str(query.get("text") or ""))
        top = results[:TOP_K]
        task_conflicts = sum(1 for row in top if row.get("_task_conflict"))
        hard_pass = sum(1 for row in top if validator.hard_filter(row, query)[0])
        canonical = [
            (validator.filter_metadata(row).get("canonical_model_id") or row.get("model_id"))
            for row in top
        ]
        evidence = Counter(str(row.get("evidence_completeness") or "unknown") for row in top)
        item = {
            "query_id": query.get("id"),
            "query_type": query.get("query_type", "unclassified"),
            "top_k": len(top),
            "candidate_count": len(eligible),
            "empty": not bool(top),
            "hard_constraint_precision_at_5": hard_pass / len(top) if top else 1.0,
            "keyword_hits_at_5": sum(1 for row in top if exact_keyword_hit(row, keywords)),
            "task_conflicts_at_5": task_conflicts,
            "canonical_duplicates_at_5": len(canonical) - len(set(canonical)),
            "evidence_completeness": dict(evidence),
            "latency_ms": round(latency_ms, 3),
            "top_model_ids": [row.get("model_id") for row in top],
            "relevance": relevance_metrics(top, query),
        }
        per_query.append(item)
        type_rows[item["query_type"]].append(item)

    def aggregate(items: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
        total = len(items)
        rows_top = sum(item["top_k"] for item in items)
        evidence = Counter()
        for item in items:
            evidence.update(item["evidence_completeness"])
        return {
            "queries": total,
            "nonempty_queries": sum(not item["empty"] for item in items),
            "empty_queries": sum(item["empty"] for item in items),
            "hard_constraint_precision_at_5": round(
                sum(item["hard_constraint_precision_at_5"] for item in items) / total, 4
            ) if total else 0.0,
            "keyword_hit_rate_at_5": round(
                sum(item["keyword_hits_at_5"] for item in items) / rows_top, 4
            ) if rows_top else 0.0,
            "task_conflict_rate_at_5": round(
                sum(item["task_conflicts_at_5"] for item in items) / rows_top, 4
            ) if rows_top else 0.0,
            "canonical_duplicate_rows_at_5": sum(item["canonical_duplicates_at_5"] for item in items),
            "evidence_completeness": dict(evidence),
            "labeled_queries": sum(1 for item in items if item.get("relevance", {}).get("labeled")),
            "recall_at_5": round(sum(item["relevance"]["recall_at_5"] for item in items if item.get("relevance", {}).get("labeled")) / max(1, sum(1 for item in items if item.get("relevance", {}).get("labeled"))), 4) if any(item.get("relevance", {}).get("labeled") for item in items) else None,
            "mrr": round(sum(item["relevance"]["mrr"] for item in items if item.get("relevance", {}).get("labeled")) / max(1, sum(1 for item in items if item.get("relevance", {}).get("labeled"))), 4) if any(item.get("relevance", {}).get("labeled") for item in items) else None,
            "ndcg_at_5": round(sum(item["relevance"]["ndcg_at_5"] for item in items if item.get("relevance", {}).get("labeled")) / max(1, sum(1 for item in items if item.get("relevance", {}).get("labeled"))), 4) if any(item.get("relevance", {}).get("labeled") for item in items) else None,
            "latency_ms_mean": round(sum(item["latency_ms"] for item in items) / total, 3) if total else 0.0,
        }

    return {
        "overall": aggregate(per_query),
        "by_query_type": {query_type: aggregate(items) for query_type, items in sorted(type_rows.items())},
        "per_query": per_query,
    }


def evaluate_existing_top_ids(
    validator: Any,
    rows: Sequence[Dict[str, Any]],
    queries: Sequence[Dict[str, Any]],
    top_ids_by_query: Mapping[str, Sequence[str]],
) -> Dict[str, Any]:
    """Evaluate a previously saved ranking without pretending to rerun embeddings."""
    row_by_id = {str(row.get("model_id")): row for row in rows}
    per_query: List[Dict[str, Any]] = []
    type_rows: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for query in queries:
        top = [row_by_id[model_id] for model_id in top_ids_by_query.get(str(query.get("id")), []) if model_id in row_by_id]
        keywords = query_tokens(str(query.get("text") or ""))
        hard_pass = sum(1 for row in top if validator.hard_filter(row, query)[0])
        conflicts = sum(1 for row in top if validator.detect_task_conflict(row).get("conflict"))
        canonical = [
            validator.filter_metadata(row).get("canonical_model_id") or row.get("model_id")
            for row in top
        ]
        evidence = Counter(str(row.get("evidence_completeness") or "unknown") for row in top)
        item = {
            "query_id": query.get("id"),
            "query_type": query.get("query_type", "unclassified"),
            "top_k": len(top),
            "candidate_count": None,
            "empty": not bool(top),
            "hard_constraint_precision_at_5": hard_pass / len(top) if top else 1.0,
            "keyword_hits_at_5": sum(1 for row in top if exact_keyword_hit(row, keywords)),
            "task_conflicts_at_5": conflicts,
            "canonical_duplicates_at_5": len(canonical) - len(set(canonical)),
            "evidence_completeness": dict(evidence),
            "latency_ms": None,
            "top_model_ids": [row.get("model_id") for row in top],
            "relevance": relevance_metrics(top, query),
        }
        per_query.append(item)
        type_rows[item["query_type"]].append(item)

    def aggregate(items: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
        total = len(items)
        rows_top = sum(item["top_k"] for item in items)
        evidence = Counter()
        for item in items:
            evidence.update(item["evidence_completeness"])
        return {
            "queries": total,
            "nonempty_queries": sum(not item["empty"] for item in items),
            "empty_queries": sum(item["empty"] for item in items),
            "hard_constraint_precision_at_5": round(sum(item["hard_constraint_precision_at_5"] for item in items) / total, 4) if total else 0.0,
            "keyword_hit_rate_at_5": round(sum(item["keyword_hits_at_5"] for item in items) / rows_top, 4) if rows_top else 0.0,
            "task_conflict_rate_at_5": round(sum(item["task_conflicts_at_5"] for item in items) / rows_top, 4) if rows_top else 0.0,
            "canonical_duplicate_rows_at_5": sum(item["canonical_duplicates_at_5"] for item in items),
            "evidence_completeness": dict(evidence),
            "labeled_queries": sum(1 for item in items if item.get("relevance", {}).get("labeled")),
            "recall_at_5": None,
            "mrr": None,
            "ndcg_at_5": None,
            "latency_ms_mean": None,
        }

    return {
        "overall": aggregate(per_query),
        "by_query_type": {query_type: aggregate(items) for query_type, items in sorted(type_rows.items())},
        "per_query": per_query,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query-file", type=Path, default=DEFAULT_QUERY_FILE)
    parser.add_argument("--report-json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report-md", type=Path, default=DEFAULT_MD)
    parser.add_argument(
        "--reuse-existing",
        action="store_true",
        help="Use the saved dense comparison and current hybrid validation; recompute only sparse locally.",
    )
    parser.add_argument(
        "--dense-snapshot",
        type=Path,
        default=ROOT / "test" / "dense_sparse_comparison_all48.json",
    )
    parser.add_argument(
        "--hybrid-validation",
        type=Path,
        default=ROOT / "test" / "stage4_retrieval_validation.json",
    )
    args = parser.parse_args()

    validator = load_validator()
    rows = validator.load_rows()
    sparse_index = validator.FieldedBM25(rows)
    queries = read_jsonl(args.query_file)
    provenance: Dict[str, Any] = {}
    if args.reuse_existing:
        dense_snapshot = json.loads(args.dense_snapshot.read_text(encoding="utf-8"))
        hybrid_validation = json.loads(args.hybrid_validation.read_text(encoding="utf-8"))
        dense_ids = {
            str(item.get("query_id")): list(item.get("dense_top5") or [])
            for item in dense_snapshot.get("per_query", [])
        }
        hybrid_ids = {
            str(item.get("query_id")): [result.get("model_id") for result in item.get("results", [])[:TOP_K]]
            for item in hybrid_validation.get("reports", [])
        }
        results = {
            "dense": evaluate_existing_top_ids(validator, rows, queries, dense_ids),
            "hybrid": evaluate_existing_top_ids(validator, rows, queries, hybrid_ids),
            "sparse": evaluate_mode(validator, rows, queries, {index: None for index in range(len(queries))}, "sparse", sparse_index=sparse_index),
        }
        provenance = {
            "dense": {"source": str(args.dense_snapshot), "recomputed": False, "note": "기존 저장 ranking을 재평가"},
            "hybrid": {"source": str(args.hybrid_validation), "recomputed": False, "note": "현재 vector/evidence validation ranking을 재평가"},
        "sparse": {"source": "local fielded BM25 scorer", "recomputed": True},
        }
    else:
        vectors = embed_queries(queries)
        results = {
            mode: evaluate_mode(validator, rows, queries, vectors, mode, sparse_index=sparse_index)
            for mode in ("dense", "sparse", "hybrid")
        }
        provenance = {mode: {"source": "fresh query embeddings", "recomputed": True} for mode in ("dense", "sparse", "hybrid")}
    summary = {
        "query_file": str(args.query_file),
        "queries": len(queries),
        "rows": len(rows),
        "embedding_model": os.getenv("STAGE4_EMBEDDING_MODEL", "text-embedding-3-small"),
        "top_k": TOP_K,
        "query_schema_version": 3,
        "query_type_version": 1,
        "relevance_label_version": max((int(query.get("relevance_label_version") or 0) for query in queries), default=0),
        "labeled_query_count": sum(bool(query.get("relevant_model_ids")) for query in queries),
        "metric_note": "사람이 라벨링한 relevant_model_ids가 없어 Recall@5가 아니다. hard constraint precision과 exact keyword hit은 proxy다.",
        "fair_mode_comparison": not args.reuse_existing,
        "query_type_definitions": QUERY_TYPE_DESCRIPTIONS,
        "provenance": provenance,
        "modes": results,
    }
    args.report_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Dense·Sparse·Hybrid 검색 정확도 비교",
        "",
        f"- 골든셋: `{args.query_file}` ({len(queries)}개)",
        f"- 후보 corpus: {len(rows)}개 (Core + Low Popularity)",
        f"- 임베딩: `{summary['embedding_model']}`",
        "- 모든 모드의 평가에는 동일한 hard filter, task-conflict penalty, benchmark boost, canonical/author diversification 규칙을 사용했다.",
        "- 사람이 라벨링한 relevant model ID가 없으므로 아래 결과는 진짜 Recall@5가 아니라 deterministic/proxy 지표다.",
        "- 이번 실행은 네트워크 제한으로 새 query embedding을 호출하지 않고 저장된 dense 비교 결과와 현재 hybrid validation 결과를 재평가했으며, sparse만 현재 corpus에서 다시 계산했다.",
        "- 따라서 이번 `--reuse-existing` 결과는 공통 hard filter를 확인하는 운영 점검이며, 세 모드의 완전한 공정 비교는 `--reuse-existing` 없이 새 query embedding으로 다시 실행해야 한다.",
        "",
        "## 전체 결과",
        "",
        "| 모드 | 질의 | 비어 있음 | hard constraint precision@5 | exact keyword hit@5 | task conflict@5 | canonical 중복 | 평균 rank ms |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for mode in ("dense", "sparse", "hybrid"):
        m = results[mode]["overall"]
        latency = "미측정" if m.get("latency_ms_mean") is None else f"{m['latency_ms_mean']:.2f}"
        lines.append(
            f"| {mode} | {m['queries']} | {m['empty_queries']} | {m['hard_constraint_precision_at_5']:.1%} | "
            f"{m['keyword_hit_rate_at_5']:.1%} | {m['task_conflict_rate_at_5']:.1%} | "
            f"{m['canonical_duplicate_rows_at_5']} | {latency} |"
        )
    lines += ["", "## 유형별 결과", ""]
    types = sorted({q.get("query_type", "unclassified") for q in queries})
    lines += [
        "| 유형 | 질의 | Dense keyword | Sparse keyword | Hybrid keyword | Dense empty | Sparse empty | Hybrid empty |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for query_type in types:
        values = [results[mode]["by_query_type"].get(query_type, {}) for mode in ("dense", "sparse", "hybrid")]
        lines.append(
            f"| `{query_type}` | {values[0].get('queries', 0)} | "
            f"{values[0].get('keyword_hit_rate_at_5', 0):.1%} | {values[1].get('keyword_hit_rate_at_5', 0):.1%} | "
            f"{values[2].get('keyword_hit_rate_at_5', 0):.1%} | {values[0].get('empty_queries', 0)} | "
            f"{values[1].get('empty_queries', 0)} | {values[2].get('empty_queries', 0)} |"
        )
    lines += ["", "## 유형 정의", "", "| 유형 | 설명 |", "|---|---|"]
    for query_type in types:
        lines.append(f"| `{query_type}` | {type_description(query_type)} |")
    lines += [
        "",
        "## 결과 출처",
        "",
        f"- Dense: `{provenance['dense']['source']}`의 저장 top-5 재평가",
        f"- Hybrid: `{provenance['hybrid']['source']}`의 현재 vector/evidence validation 재평가",
        "- Sparse: 현재 Stage 4 corpus의 model_id·translation_pairs·task·metadata·content를 분리한 Fielded BM25 재계산",
        "- 새 query embedding을 포함한 완전한 세 모드 동시 재실행은 네트워크가 허용되는 환경에서 `--reuse-existing` 없이 실행한다.",
    ]
    lines += [
        "",
        "### 해석 주의",
        "",
        "`hard_constraint_precision_at_5`는 필터 오류가 상위 결과에 들어갔는지 보는 지표다. `exact keyword hit@5`는 모델명·메타데이터 문자열이 상위 결과에 포함되는지 보는 lexical proxy라서 의미적 적합도 자체가 아니다.",
        "정식 Recall@5·MRR·nDCG를 산출하려면 각 질의에 사람이 검토한 `relevant_model_ids` 라벨을 추가해야 한다.",
    ]
    args.report_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"report_json": str(args.report_json), "report_md": str(args.report_md), "queries": len(queries)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
