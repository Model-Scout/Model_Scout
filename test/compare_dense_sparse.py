#!/usr/bin/env python3
"""Compare the existing dense golden-set results with an OpenSearch-style BM25 shadow.

This is intentionally a local comparison.  It does not require an OpenSearch
server and does not write to Supabase.  The sparse side uses the same candidate
filters as ``05_validate_retrieval.py`` and a field-weighted BM25 scorer over
Stage 4 metadata/semantic text.  The dense top-5 is read from the last validated
vector run so this script does not spend on new query embeddings.

The report calls dense/sparse overlap a *dense-agreement proxy*, not true
semantic Recall@5: the current golden set contains constraints but no
human-judged relevant model IDs.  True Recall@5 requires a judged relevance set.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import re
import statistics
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Tuple



ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
GOLDEN_QUERY_PATH = ROOT / "test" / "retrieval_queries.jsonl"
DENSE_REPORT_PATH = ROOT / "test" / "stage4_retrieval_validation.json"
REPORT_JSON = ROOT / "test" / "dense_sparse_comparison.json"
REPORT_MD = ROOT / "test" / "dense_sparse_comparison.md"

# 27 standard queries (including the three benchmark queries) plus three
# representative difficult queries.  The selection is fixed for reproducibility
# and covers every collected task, both pools, benchmark terms and hard numeric
# constraints without expanding the paid dense embedding run.
SELECTED_QUERY_IDS = (
    "q01_ko_classification_cpu",
    "q02_ko_sentence_embedding",
    "q03_ko_document_embedding",
    "q04_ko_asr",
    "q05_ko_translation",
    "q06_ko_summarization",
    "q07_ko_qa",
    "q08_ko_generation_long_context",
    "q09_ko_multimodal",
    "q10_ko_small_low_popularity",
    "q11_ko_known_hardware",
    "q13_small_cpu_classifier",
    "q14_semantic_search_embedding",
    "q15_long_context_embedding",
    "q16_realtime_asr_small",
    "q18_long_document_summarization",
    "q19_small_question_answering",
    "q20_long_context_generation",
    "q21_vision_language_ocr",
    "q22_low_popularity_generation",
    "q23_known_embedding_metadata",
    "q24_small_sentence_similarity",
    "q26_on_device_asr",
    "q27_very_long_context_generation",
    "q31_mteb_arguana_ndcg",
    "q32_mteb_embedding_evidence",
    "q33_asr_wer_evidence",
    "q34_ko_summarization_small_long",
    "q37_ko_embedding_long_small",
    "q39_ko_qa_context",
)

TOKEN_RE = re.compile(r"[\w가-힣]+", re.UNICODE)
STOPWORDS = {
    "한국어", "모델", "모델을", "모델이", "모델의", "위한", "사용", "사용할",
    "추천", "추천해줘", "찾아줘", "찾는", "있는", "있고", "모두", "확인된",
    "지원", "지원하는", "처리", "처리할", "가능한", "용", "중", "이상", "이하",
    "and", "the", "for", "model", "models", "with", "from", "to",
}


def load_validator_module():
    path = ROOT / "05_validate_retrieval.py"
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location("model_scout_validator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def tokens(value: Any) -> List[str]:
    if isinstance(value, (list, tuple, set)):
        return [token for item in value for token in tokens(item)]
    if isinstance(value, dict):
        return [token for key, value in value.items() for token in tokens(key)] + [
            token for value in value.values() for token in tokens(value)
        ]
    return [token.casefold() for token in TOKEN_RE.findall(str(value or ""))]


def query_keywords(text: str) -> List[str]:
    return sorted({token for token in tokens(text) if len(token) > 1 and token not in STOPWORDS})


def field_tokens(row: Mapping[str, Any]) -> Dict[str, List[str]]:
    metadata = row.get("filter_metadata") or {}
    task = row.get("task") or {}
    return {
        # Equivalent to a high-boost keyword field in an OpenSearch multi_match.
        "model_id": tokens(row.get("model_id")),
        "task": tokens([task.get("primary"), task.get("matched")]),
        "metadata": tokens(metadata),
        "content": tokens(row.get("embedding_text")),
    }


class FieldedBM25:
    """Small stdlib BM25 implementation with deterministic field boosts."""

    def __init__(self, rows: Sequence[Mapping[str, Any]]) -> None:
        self.rows = list(rows)
        self.fields = ("model_id", "task", "metadata", "content")
        self.boosts = {"model_id": 4.0, "task": 2.0, "metadata": 2.0, "content": 1.0}
        self.k1 = 1.2
        self.b = 0.75
        self.docs: List[Dict[str, List[str]]] = [field_tokens(row) for row in self.rows]
        self.avg_len = {
            field: (sum(len(doc[field]) for doc in self.docs) / max(len(self.docs), 1))
            for field in self.fields
        }
        self.doc_freq: Dict[str, Dict[str, int]] = {field: Counter() for field in self.fields}
        for doc in self.docs:
            for field in self.fields:
                for token in set(doc[field]):
                    self.doc_freq[field][token] += 1

    def score(self, index: int, query_tokens: Sequence[str]) -> float:
        score = 0.0
        n_docs = len(self.docs)
        doc = self.docs[index]
        for field in self.fields:
            values = doc[field]
            if not values:
                continue
            counts = Counter(values)
            avg_len = self.avg_len[field] or 1.0
            for token in query_tokens:
                tf = counts.get(token, 0)
                if not tf:
                    continue
                df = self.doc_freq[field].get(token, 0)
                idf = math.log(1.0 + (n_docs - df + 0.5) / (df + 0.5))
                norm = tf + self.k1 * (1.0 - self.b + self.b * len(values) / avg_len)
                score += self.boosts[field] * idf * (tf * (self.k1 + 1.0) / norm)
        return score

    def rank(
        self,
        candidates: Sequence[int],
        query: Mapping[str, Any],
        top_k: int,
        validator: Any,
        benchmark_boosts: Mapping[str, Mapping[str, Any]],
    ) -> List[int]:
        query_tokens = query_keywords(query.get("text", ""))
        scored = []
        for index in candidates:
            row = self.rows[index]
            model_id = row.get("model_id", "")
            conflict = validator.detect_task_conflict(row)
            benchmark = benchmark_boosts.get(model_id, {})
            adjusted = (
                self.score(index, query_tokens)
                - float(conflict.get("ranking_penalty", 0.0))
                + float(benchmark.get("boost", 0.0))
            )
            scored.append((adjusted, model_id, index))
        scored.sort(key=lambda item: (-item[0], item[1]))
        return [index for _, _, index in scored[:top_k]]


def canonical_key(row: Mapping[str, Any]) -> str:
    metadata = row.get("filter_metadata") or {}
    return str(metadata.get("canonical_model_id") or row.get("canonical_model_id") or row.get("model_id"))


def dedupe_indices(rows: Sequence[Mapping[str, Any]], indices: Iterable[int]) -> List[int]:
    seen = set()
    output = []
    for index in indices:
        key = canonical_key(rows[index])
        if key in seen:
            continue
        seen.add(key)
        output.append(index)
    return output


def exact_keyword_hit(row: Mapping[str, Any], keywords: Sequence[str]) -> bool:
    doc_tokens = set()
    for field_values in field_tokens(row).values():
        doc_tokens.update(field_values)
    return bool(doc_tokens.intersection(keywords))


def cosine_matrix_latency(rows: Sequence[Mapping[str, Any]], candidate_sets: Sequence[Sequence[int]]) -> List[float]:
    import numpy as np  # only needed for the dense latency probe

    # float64 avoids an Accelerate/OpenBLAS float32 overflow warning on some
    # macOS Python builds even though the stored values are finite and small.
    vectors = np.asarray([row.get("embedding") or [] for row in rows], dtype=np.float64)
    norms = np.linalg.norm(vectors, axis=1)
    safe = np.where(norms == 0, 1.0, norms)
    vectors = vectors / safe[:, None]
    q = vectors[0]
    times: List[float] = []
    for candidates in candidate_sets:
        matrix = vectors[np.asarray(candidates, dtype=np.int64)]
        # Warm the BLAS path and keep platform-specific floating-point warnings
        # out of the comparison output; the values are used for timing only.
        with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
            _ = matrix @ q
        started = time.perf_counter()
        with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
            _ = matrix @ q
        times.append((time.perf_counter() - started) * 1000.0)
    return times


def main() -> int:
    import numpy as np  # FieldedBM25 is importable without numpy

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query-file", type=Path, default=GOLDEN_QUERY_PATH)
    parser.add_argument("--dense-report", type=Path, default=DENSE_REPORT_PATH)
    parser.add_argument("--report-json", type=Path, default=REPORT_JSON)
    parser.add_argument("--report-md", type=Path, default=REPORT_MD)
    parser.add_argument(
        "--all-golden",
        action="store_true",
        help="evaluate all queries in retrieval_queries.jsonl instead of the fixed 30-query sample",
    )
    args = parser.parse_args()

    validator = load_validator_module()
    rows = validator.load_rows()
    queries = {query["id"]: query for query in read_jsonl(args.query_file)}
    missing = [query_id for query_id in SELECTED_QUERY_IDS if query_id not in queries]
    if missing:
        raise RuntimeError(f"selected golden queries missing: {missing}")
    selected = list(queries.values()) if args.all_golden else [queries[query_id] for query_id in SELECTED_QUERY_IDS]
    dense_report = json.loads(args.dense_report.read_text(encoding="utf-8"))
    dense_by_id = {report["query_id"]: report for report in dense_report.get("reports", [])}
    missing_dense = [query["id"] for query in selected if query["id"] not in dense_by_id]
    if missing_dense:
        raise RuntimeError(f"dense validation report missing selected queries: {missing_dense}")

    bm25 = FieldedBM25(rows)
    per_query: List[Dict[str, Any]] = []
    sparse_latency: List[float] = []
    dense_candidate_sets: List[List[int]] = []
    sparse_candidate_sets: List[List[int]] = []
    id_to_index = {row.get("model_id"): index for index, row in enumerate(rows)}

    for query in selected:
        candidates = []
        for index, row in enumerate(rows):
            eligible, _ = validator.hard_filter(row, query)
            if eligible:
                candidates.append(index)
        dense_candidate_sets.append(candidates)
        benchmark_boosts = validator.benchmark_adjustments(rows, query)
        started = time.perf_counter()
        sparse_indices = bm25.rank(
            candidates,
            query,
            len(candidates),
            validator,
            benchmark_boosts,
        )
        sparse_indices = dedupe_indices(rows, sparse_indices)[: int(query.get("top_k", 5))]
        sparse_latency.append((time.perf_counter() - started) * 1000.0)
        sparse_candidate_sets.append(sparse_indices)

        dense_results = dense_by_id[query["id"]].get("results", [])[: int(query.get("top_k", 5))]
        dense_ids = [result.get("model_id") for result in dense_results]
        sparse_ids = [rows[index].get("model_id") for index in sparse_indices]
        keywords = query_keywords(query.get("text", ""))
        dense_hits = sum(
            1
            for model_id in dense_ids
            if model_id in id_to_index and exact_keyword_hit(rows[id_to_index[model_id]], keywords)
        )
        sparse_hits = sum(1 for index in sparse_indices if exact_keyword_hit(rows[index], keywords))
        per_query.append({
            "query_id": query["id"],
            "text": query.get("text", ""),
            "suite": query.get("suite"),
            "query_type": query.get("query_type", "unclassified"),
            "routing_hint": query.get("routing_hint"),
            "tasks": query.get("tasks", []),
            "candidate_count": len(candidates),
            "keywords": keywords,
            "dense_top5": dense_ids,
            "sparse_top5": sparse_ids,
            "dense_agreement_at_5": len(set(dense_ids) & set(sparse_ids)) / max(len(dense_ids), 1),
            "dense_exact_keyword_hits_at_5": dense_hits,
            "sparse_exact_keyword_hits_at_5": sparse_hits,
            "sparse_latency_ms": sparse_latency[-1],
        })

    # Rank-only dense latency: no additional query embedding call is made.
    dense_rank_latency = cosine_matrix_latency(rows, dense_candidate_sets)
    for report, latency in zip(per_query, dense_rank_latency):
        report["dense_rank_latency_ms"] = latency

    def mean(key: str) -> float:
        return round(statistics.mean(report[key] for report in per_query), 3)

    type_metrics: Dict[str, Dict[str, Any]] = {}
    for query_type in sorted({report["query_type"] for report in per_query}):
        group = [report for report in per_query if report["query_type"] == query_type]
        type_metrics[query_type] = {
            "queries": len(group),
            "nonempty_queries": sum(1 for report in group if report["candidate_count"] > 0),
            "agreement_at_5_mean": round(statistics.mean(report["dense_agreement_at_5"] for report in group), 3),
            "dense_keyword_hit_rate_at_5": round(
                sum(report["dense_exact_keyword_hits_at_5"] for report in group) / (len(group) * 5), 3
            ),
            "sparse_keyword_hit_rate_at_5": round(
                sum(report["sparse_exact_keyword_hits_at_5"] for report in group) / (len(group) * 5), 3
            ),
        }

    summary = {
        "golden_query_file": str(args.query_file),
        "dense_report": str(args.dense_report),
        "query_selection": {
            "total_golden_queries": len(queries),
            "selected": len(selected),
            "selected_ids": [query["id"] for query in selected],
            "selection_rule": (
                "all golden queries"
                if args.all_golden
                else "27 standard (including q31-q33 benchmark queries) + q34/q37/q39 adversarial queries"
            ),
        },
        "rows": len(rows),
        "dense_source": "previous stage4_retrieval_validation.json vector run; no new embedding API calls",
        "sparse_source": "local fielded BM25 shadow equivalent; OpenSearch localhost:9200 was unavailable",
        "recall_at_5_note": "No human relevance labels are present. dense_agreement_at_5 is a proxy, not semantic Recall@5.",
        "metrics": {
            "dense_agreement_proxy_at_5_mean": round(statistics.mean(report["dense_agreement_at_5"] for report in per_query), 3),
            "dense_agreement_proxy_at_5_median": round(statistics.median(report["dense_agreement_at_5"] for report in per_query), 3),
            "dense_exact_keyword_hit_rate_at_5": round(sum(report["dense_exact_keyword_hits_at_5"] for report in per_query) / (len(per_query) * 5), 3),
            "sparse_exact_keyword_hit_rate_at_5": round(sum(report["sparse_exact_keyword_hits_at_5"] for report in per_query) / (len(per_query) * 5), 3),
            "dense_rank_latency_ms_mean": mean("dense_rank_latency_ms"),
            "dense_rank_latency_ms_p95": round(float(np.percentile([report["dense_rank_latency_ms"] for report in per_query], 95)), 3),
            "sparse_bm25_latency_ms_mean": mean("sparse_latency_ms"),
            "sparse_bm25_latency_ms_p95": round(float(np.percentile([report["sparse_latency_ms"] for report in per_query], 95)), 3),
            "dense_query_embedding_latency": "not measured; OpenAI API unavailable in this environment",
            "nonempty_queries": sum(1 for report in per_query if report["candidate_count"] > 0),
            "empty_queries": sum(1 for report in per_query if report["candidate_count"] == 0),
            "queries_sparse_keyword_better": sum(
                1
                for report in per_query
                if report["sparse_exact_keyword_hits_at_5"] > report["dense_exact_keyword_hits_at_5"]
            ),
            "queries_dense_keyword_better": sum(
                1
                for report in per_query
                if report["dense_exact_keyword_hits_at_5"] > report["sparse_exact_keyword_hits_at_5"]
            ),
        },
        "by_query_type": type_metrics,
        "per_query": per_query,
    }
    args.report_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    metrics = summary["metrics"]
    lines = [
        "# Dense-only와 Sparse(BM25 shadow) 비교",
        "",
        (
            f"골든셋 `{args.query_file}`의 전체 {len(queries)}개를 평가했다."
            if args.all_golden
            else f"골든셋 `{args.query_file}`의 {len(queries)}개 중 30개를 고정 선택했다."
        ),
        (
            "전체 표준·adversarial 질의를 사용했다."
            if args.all_golden
            else "선택은 표준 질의 27개(benchmark q31~q33 포함)와 adversarial q34/q37/q39 3개이며, 9개 task·두 pool·수치 조건·benchmark 조건을 포함한다."
        ),
        "",
        "## 평가 범위",
        "",
        "- Dense: 기존 `stage4_retrieval_validation.json`의 vector 실행 결과를 재사용했다. 새 OpenAI 임베딩 호출은 하지 않았다.",
        "- Sparse: OpenSearch의 `multi_match`와 같은 field boost를 적용한 로컬 BM25 shadow index다. 로컬 OpenSearch(`localhost:9200`)가 없어 서버 latency는 측정하지 않았다.",
        "- Recall@5: 사람이 판정한 relevant model ID가 없으므로 진짜 semantic Recall@5는 계산할 수 없다. 아래 agreement는 dense top-5를 기준으로 한 비교 proxy다.",
        "- Exact keyword hit는 lexical 검색에 유리한 지표이므로 sparse의 절대 정확도 증거로 해석하지 않는다.",
        "",
        "## 결과",
        "",
        "| 지표 | Dense-only | Sparse BM25 shadow |",
        "|---|---:|---:|",
        f"| Dense top-5와 Sparse top-5 agreement (proxy) | - | {metrics['dense_agreement_proxy_at_5_mean']:.3f} 평균 / {metrics['dense_agreement_proxy_at_5_median']:.3f} 중앙값 |",
        f"| Exact keyword hit@5 | {metrics['dense_exact_keyword_hit_rate_at_5']:.3f} | {metrics['sparse_exact_keyword_hit_rate_at_5']:.3f} |",
        f"| 검색 rank latency 평균 (ms) | {metrics['dense_rank_latency_ms_mean']:.3f} | {metrics['sparse_bm25_latency_ms_mean']:.3f} |",
        f"| 검색 rank latency p95 (ms) | {metrics['dense_rank_latency_ms_p95']:.3f} | {metrics['sparse_bm25_latency_ms_p95']:.3f} |",
        "",
        "Dense latency는 query embedding API 호출 시간을 제외한 로컬 vector rank 비용이다. 실제 서비스에서는 OpenAI query embedding 네트워크 시간이 추가된다.",
        "",
        "## 질의별 결과",
        "",
        "| 질의 | 후보 | agreement@5 | Dense keyword hit | Sparse keyword hit | Dense ms | Sparse ms |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for report in per_query:
        lines.append(
            f"| `{report['query_id']}` | {report['candidate_count']} | {report['dense_agreement_at_5']:.2f} | "
            f"{report['dense_exact_keyword_hits_at_5']}/5 | {report['sparse_exact_keyword_hits_at_5']}/5 | "
            f"{report['dense_rank_latency_ms']:.3f} | {report['sparse_latency_ms']:.3f} |"
        )
    lines.extend([
        "",
        "## 해석",
        "",
        "Sparse는 모델명, task, language, parameter/context 같은 명시적 조건과 MTEB·WER 같은 keyword가 질의에 직접 포함될 때 강점이 있다.",
        "Dense는 표현이 다른 한국어 질의의 의미 유사도와 README semantic summary를 보완한다. 따라서 현재 자료만으로 sparse를 dense의 대체로 채택하지 않고, 위 결과를 기준으로 hybrid 후보를 검토하는 것이 안전하다.",
        "이번 비교만으로 sparse 도입을 확정할 수는 없다. hard-filter 통과 여부는 같지만 사람의 relevant model ID 라벨이 없고, latency도 서로 다른 구현(local NumPy와 Python BM25)에서 측정되었다.",
        "정식 Recall@5 결론을 내리려면 질의별 relevant model ID를 사람이 라벨링한 별도 golden relevance set을 추가해야 한다.",
    ])
    args.report_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"report_json": str(args.report_json), "report_md": str(args.report_md), "queries": len(selected), "rows": len(rows), "metrics": metrics}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
