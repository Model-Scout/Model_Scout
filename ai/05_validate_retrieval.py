#!/usr/bin/env python3
"""Validate Stage 4 recommendation filters and vector ranking.

The validator keeps hard eligibility filters separate from ranking. Task
metadata conflicts are advisory: conflicted rows remain eligible but receive a
small, auditable score penalty.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Tuple
from urllib.parse import quote

from dotenv import load_dotenv

from benchmark_metadata import benchmark_key, match_benchmark_records
from evidence_index import attach_evidence_hits, load_index
from retrieval_metadata import normalize_query_terms


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT.parent / "backend" / "data"
QUERY_PATH = ROOT / "test" / "retrieval_queries.jsonl"
REPORT_JSON = ROOT / "test" / "stage4_retrieval_validation.json"
REPORT_MD = ROOT / "test" / "stage4_retrieval_validation.md"
POOLS = ("core", "low_popularity")
BENCHMARK_PRESENCE_BOOST = 0.015
BENCHMARK_SCORE_BOOST = 0.04


# Inlined deterministic task-conflict helper. Keep identical in Stage 4 builder and validator.
TASK_CONFLICT_VERSION = 1
TASK_CONFLICT_PENALTY = 0.08
TASK_CONFLICT_PENALTY_MEDIUM = 0.05


def _text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple, set)):
        return " ".join(_text(item) for item in value)
    if isinstance(value, dict):
        return " ".join(f"{_text(k)} {_text(v)}" for k, v in value.items())
    return str(value)


def _identity_text(row: Dict[str, Any]) -> str:
    """Return stable identity/task metadata, excluding free-form claims.

    Free-form semantic claims can contain words such as ``embedding`` even for
    a generative model.  Using model identity, task, architecture, and model
    type keeps this detector conservative.
    """

    metadata = row.get("filter_metadata") or {}
    task = row.get("task") or {}
    values: Iterable[Any] = (
        row.get("model_id"),
        row.get("canonical_model_id"),
        metadata.get("canonical_model_id"),
        task.get("primary"),
        task.get("matched"),
        metadata.get("primary_task"),
        metadata.get("matched_tasks"),
        metadata.get("architecture"),
        metadata.get("model_type"),
    )
    return " ".join(_text(value) for value in values).casefold()


def _contains_any(text: str, patterns: Iterable[str]) -> str | None:
    for pattern in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE):
            return pattern
    return None


def detect_task_conflict(row: Dict[str, Any]) -> Dict[str, Any]:
    """Detect task metadata contradictions without changing candidate recall."""

    task = row.get("task") or {}
    metadata = row.get("filter_metadata") or {}
    primary = task.get("primary") or metadata.get("primary_task") or ""
    identity = _identity_text(row)
    evidence: List[str] = []
    severity = "none"

    if primary == "text-generation":
        marker = _contains_any(
            identity,
            (
                r"bge[-_ ]?reranker",
                r"re[-_ ]?ranker",
                r"cross[-_ ]?encoder",
                r"\branker\b",
                r"\bclassifier\b",
                r"classification",
                r"sentence[-_ ]?transformer",
                r"\bembedding\b",
                r"\bcolbert\b",
                r"retriever",
                r"similarity",
            ),
        )
        if marker:
            evidence.append(f"text_generation_identity_marker:{marker}")
            severity = "high"

    if primary == "question-answering":
        marker = _contains_any(
            identity,
            (
                r"opus[-_ ]?mt",
                r"nllb",
                r"m2m100",
                r"translate",
                r"translation",
                r"translator",
                r"vnjp",
            ),
        )
        if marker:
            evidence.append(f"question_answering_identity_marker:{marker}")
            severity = "medium" if severity == "none" else severity

    if severity == "high":
        penalty = TASK_CONFLICT_PENALTY
    elif severity == "medium":
        penalty = TASK_CONFLICT_PENALTY_MEDIUM
    else:
        penalty = 0.0

    return {
        "version": TASK_CONFLICT_VERSION,
        "conflict": bool(evidence),
        "severity": severity,
        "evidence": evidence,
        "ranking_penalty": penalty,
    }





def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def load_catalog(data_dir: Path, pools: Sequence[str] = POOLS) -> Dict[Tuple[str, str], Dict[str, Any]]:
    """Load Stage 2/3 details for post-ranking result hydration."""
    catalog: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for pool in pools:
        stage2 = {
            row.get("model_id"): row
            for row in read_jsonl(data_dir / f"hf_models_stage2_{pool}.jsonl")
        }
        stage3 = {
            row.get("model_id"): row
            for row in read_jsonl(data_dir / f"hf_models_stage3_{pool}.jsonl")
        }
        for model_id in set(stage2) | set(stage3):
            if model_id:
                catalog[(pool, model_id)] = {
                    "stage2": stage2.get(model_id),
                    "stage3": stage3.get(model_id),
                }
    return catalog


def _claim_evidence(semantic: Mapping[str, Any], evidence: Mapping[str, Any]) -> Dict[str, Any]:
    """Keep claim-level quotes and referenced spans without duplicating README."""
    span_by_id = {
        span.get("evidence_id"): span
        for span in evidence.get("spans", [])
        if isinstance(span, dict) and span.get("evidence_id")
    }
    fields = (
        "summary", "documented_strengths", "documented_limitations", "use_cases",
        "benchmarks", "license_notes", "unknowns", "warnings",
    )
    claims: Dict[str, Any] = {}
    referenced_spans: Dict[str, Dict[str, Any]] = {}
    for field in fields:
        value = semantic.get(field)
        if isinstance(value, dict):
            value = [value]
        if not isinstance(value, list):
            continue
        normalized = []
        for claim in value:
            if not isinstance(claim, dict):
                normalized.append(claim)
                continue
            item = {
                key: claim.get(key)
                for key in ("text", "evidence_refs", "supporting_quote", "evidence_level")
                if key in claim
            }
            supporting = []
            for ref in claim.get("evidence_refs") or []:
                span = span_by_id.get(ref)
                if not span:
                    continue
                referenced_spans[ref] = {
                    key: span.get(key)
                    for key in (
                        "evidence_id", "chunk_id", "heading_path", "parent_section",
                        "content_type", "text", "content_hash",
                    )
                    if key in span
                }
                supporting.append({
                    "evidence_id": ref,
                    "quote": span.get("text"),
                    "heading_path": span.get("heading_path"),
                })
            if supporting:
                item["supporting_spans"] = supporting
            normalized.append(item)
        claims[field] = normalized
    return {
        "claims": claims,
        "readme": evidence.get("readme"),
        "field_evidence_ids": evidence.get("field_evidence_ids", {}),
        "spans": list(referenced_spans.values()),
    }


def hydrate_result(
    compact_row: Mapping[str, Any],
    catalog: Mapping[Tuple[str, str], Mapping[str, Any]],
) -> Dict[str, Any]:
    """Attach exact Stage 2 technical fields and Stage 3 evidence."""
    result = dict(compact_row)
    pool = str(compact_row.get("source_pool") or compact_row.get("pool") or "")
    model_id = str(compact_row.get("model_id") or "")
    detail = catalog.get((pool, model_id), {})
    stage2 = detail.get("stage2") or {}
    stage3 = detail.get("stage3") or {}
    source = stage2.get("source") or {}
    readme = source.get("readme") or {}
    source_url = readme.get("source_url") or f"https://huggingface.co/{quote(model_id, safe='/')}"
    readme_url = readme.get("readme_url") or f"{source_url}/blob/main/README.md"
    result["technical"] = {
        "model": stage2.get("model"),
        "quantization": stage2.get("quantization"),
        "artifacts": stage2.get("artifacts"),
        "hardware": stage2.get("hardware"),
        "license": stage2.get("license"),
        "base_models": stage2.get("base_models", []),
        "datasets": stage2.get("datasets", []),
        "metrics": stage2.get("metrics", []),
    }
    result["lineage"] = {
        "family": stage2.get("family"),
        "stage1_quality": stage2.get("stage1_quality"),
        "language": stage2.get("language"),
        "source": stage2.get("source"),
    }
    semantic = stage3.get("semantic") or {}
    evidence = stage3.get("evidence") or {}
    result["recommendation"] = {
        "summary": semantic.get("summary"),
        "documented_strengths": semantic.get("documented_strengths", []),
        "documented_limitations": semantic.get("documented_limitations", []),
        "use_cases": semantic.get("use_cases", []),
        "warnings": semantic.get("warnings", []),
        "evidence_completeness": semantic.get(
            "evidence_completeness", result.get("evidence_completeness", "unknown")
        ),
    }
    result["evidence"] = _claim_evidence(semantic, evidence)
    result["provenance"] = {
        "model_url": source_url,
        "readme_url": readme_url,
        "source_pool": pool,
        "stage1_version": compact_row.get("source_stage1_version"),
        "stage2_version": compact_row.get("source_stage2_version"),
        "stage3_version": compact_row.get("source_stage3_version"),
        "stage3_status": stage3.get("status"),
    }
    result["llm_context"] = {
        "model_id": model_id,
        "technical": result["technical"],
        "recommendation": result["recommendation"],
        "evidence": result["evidence"],
        "provenance": result["provenance"],
        "benchmark_metadata": result.get("benchmark_metadata") or {},
    }
    result["detail_joined"] = bool(stage2 or stage3)
    return result


def load_benchmark_sidecars() -> Dict[str, Dict[str, Any]]:
    sidecars: Dict[str, Dict[str, Any]] = {}
    for pool in POOLS:
        path = DATA_DIR / f"hf_models_benchmark_{pool}.jsonl"
        if not path.exists():
            continue
        for row in read_jsonl(path):
            if row.get("model_id"):
                sidecars[row["model_id"]] = row
    return sidecars


class FieldedBM25:
    """Small in-process fielded BM25 index for the current Stage 4 corpus.

    The index is rebuilt once per validation run. It is intentionally deterministic,
    uses the same eligible rows as dense ranking, and gives exact model/task/language
    fields more weight than free-form semantic claims.
    """

    FIELD_WEIGHTS = {
        "model_id": 5.0,
        "translation_pairs": 6.0,
        "languages": 3.0,
        "task": 3.0,
        "benchmark": 2.5,
        "metadata": 1.5,
        "content": 1.0,
    }

    def __init__(self, rows: Sequence[Dict[str, Any]], k1: float = 1.2, b: float = 0.75) -> None:
        self.k1 = k1
        self.b = b
        self.rows = list(rows)
        self.row_index = {str(row.get("model_id")): index for index, row in enumerate(self.rows)}
        self._score_cache: Dict[str, Dict[str, float]] = {}
        self.documents: List[Dict[str, List[str]]] = []
        self.avg_len: Dict[str, float] = {}
        self.doc_freq: Dict[str, Dict[str, int]] = {}
        for row in self.rows:
            fields = self._fields(row)
            self.documents.append(fields)
        for field in self.FIELD_WEIGHTS:
            lengths = [len(doc[field]) for doc in self.documents]
            self.avg_len[field] = (sum(lengths) / len(lengths)) if lengths else 1.0
            freq: Dict[str, int] = {}
            for doc in self.documents:
                for token in set(doc[field]):
                    freq[token] = freq.get(token, 0) + 1
            self.doc_freq[field] = freq

    @staticmethod
    def _tokens(value: Any) -> List[str]:
        text = str(value or "").casefold()
        return [token for token in re.findall(r"[\w가-힣]+(?:[-_][\w가-힣]+)?", text) if len(token) > 1]

    def _fields(self, row: Dict[str, Any]) -> Dict[str, List[str]]:
        metadata = filter_metadata(row)
        task = row.get("task") or {}
        benchmark = row.get("benchmark_metadata") or {}
        aliases = metadata.get("search_aliases") or []
        pairs = metadata.get("translation_pairs") or []
        languages = metadata.get("language_codes") or metadata.get("declared_languages") or metadata.get("languages") or []
        return {
            "model_id": self._tokens(row.get("model_id")),
            "translation_pairs": self._tokens(pairs + [str(pair).replace("-", "_") for pair in pairs]),
            "languages": self._tokens(languages + aliases),
            "task": self._tokens([task.get("primary"), task.get("matched")]),
            "benchmark": self._tokens(benchmark),
            "metadata": self._tokens(metadata),
            "content": self._tokens(row.get("embedding_text")),
        }

    def score(self, row: Dict[str, Any], query: Dict[str, Any]) -> float:
        query_key = str(query.get("text") or "").casefold()
        row_key = str(row.get("model_id") or "")
        cached = self._score_cache.setdefault(query_key, {})
        if row_key in cached:
            return cached[row_key]
        terms = normalize_query_terms(query_key)
        if not terms:
            return 0.0
        index = self.row_index.get(str(row.get("model_id")), -1)
        fields = self.documents[index] if index >= 0 else self._fields(row)
        n_docs = max(1, len(self.rows))
        score = 0.0
        for field, weight in self.FIELD_WEIGHTS.items():
            tokens = fields[field]
            if not tokens:
                continue
            length = len(tokens)
            avg_len = self.avg_len.get(field) or 1.0
            term_freq: Dict[str, int] = {}
            for token in tokens:
                term_freq[token] = term_freq.get(token, 0) + 1
            for term in terms:
                tf = term_freq.get(term)
                if not tf:
                    continue
                df = self.doc_freq.get(field, {}).get(term, 0)
                idf = math.log(1.0 + (n_docs - df + 0.5) / (df + 0.5))
                denom = tf + self.k1 * (1.0 - self.b + self.b * length / avg_len)
                score += weight * idf * (tf * (self.k1 + 1.0) / denom)
        # Smoothly normalize BM25 so strong exact-field matches remain separated
        # instead of clipping a large portion of the corpus to 1.0.
        normalized = max(0.0, min(1.0, score / (score + 10.0)))
        cached[row_key] = normalized
        return normalized


def load_rows() -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    sidecars = load_benchmark_sidecars()
    for pool in POOLS:
        for row in read_jsonl(DATA_DIR / f"hf_models_stage4_{pool}.jsonl"):
            enriched = dict(row)
            # Prefer the compact metadata embedded in Stage 4. Keep the
            # sidecar fallback so older Stage 4 snapshots remain readable.
            enriched["benchmark_metadata"] = row.get("benchmark_metadata") or sidecars.get(
                row.get("model_id"), {}
            )
            rows.append(enriched)
    return rows


def load_queries(path: Path = QUERY_PATH) -> List[Dict[str, Any]]:
    return read_jsonl(path)


def task_match(row: Dict[str, Any], query: Dict[str, Any]) -> bool:
    task = row.get("task") or {}
    available = set(task.get("matched") or [])
    if task.get("primary"):
        available.add(task["primary"])
    return bool(available & set(query.get("tasks") or []))


def filter_metadata(row: Dict[str, Any]) -> Dict[str, Any]:
    return row.get("filter_metadata") or {}


def numeric_ok(
    value: Any,
    minimum: Any = None,
    maximum: Any = None,
    required: bool = False,
) -> bool:
    known = (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )
    if not known:
        return not required
    if minimum is not None and value < minimum:
        return False
    if maximum is not None and value > maximum:
        return False
    return True


def hard_filter(row: Dict[str, Any], query: Dict[str, Any]) -> Tuple[bool, List[str]]:
    metadata = filter_metadata(row)
    reasons: List[str] = []
    allowed_pools = query.get("pools") or list(POOLS)
    if row.get("source_pool") not in allowed_pools:
        reasons.append("pool")
    if query.get("korean_required") and metadata.get("korean_verified") is not True:
        reasons.append("korean")
    if not task_match(row, query):
        reasons.append("task")
    if not numeric_ok(
        metadata.get("context_length"),
        query.get("min_context_length"),
        query.get("max_context_length"),
        bool(query.get("require_known_context")),
    ):
        reasons.append("context")
    if not numeric_ok(
        metadata.get("parameter_count_billion"),
        maximum=query.get("max_parameters_billion"),
        required=bool(query.get("require_known_parameters")),
    ):
        reasons.append("parameter_count")
    if query.get("popularity_tier") and metadata.get("popularity_tier") != query["popularity_tier"]:
        reasons.append("popularity")
    return not reasons, reasons


def lexical_score(row: Dict[str, Any], query: Dict[str, Any]) -> float:
    haystack = (
        f"{row.get('embedding_text') or ''} "
        f"{json.dumps(filter_metadata(row), ensure_ascii=False, sort_keys=True)}"
    ).casefold()
    tokens = [
        token
        for token in re.findall(r"[\w가-힣]+", query.get("text", "").casefold())
        if len(token) > 1
    ]
    score = float(sum(1 for token in tokens if token in haystack))
    metadata = filter_metadata(row)
    if metadata.get("korean_verified") is True:
        score += 10.0
    if row.get("evidence_completeness") == "high":
        score += 1.0
    return score


def lexical_relevance(
    row: Dict[str, Any],
    query: Dict[str, Any],
    sparse_index: FieldedBM25 | None = None,
) -> float:
    """Return a bounded fielded-BM25 score for sparse retrieval.

    ``sparse_index`` is optional for callers that use this helper directly; the
    fallback still uses normalized query terms and the full searchable document.
    """
    if sparse_index is not None:
        return sparse_index.score(row, query)
    terms = normalize_query_terms(query.get("text") or "")
    haystack = (
        f"{row.get('embedding_text') or ''} "
        f"{json.dumps(filter_metadata(row), ensure_ascii=False, sort_keys=True)}"
    ).casefold()
    if not terms:
        return 0.0
    return min(1.0, sum(1 for term in terms if term in haystack) / max(1.0, len(terms)))



def retrieval_weights(query: Dict[str, Any], has_dense_vector: bool) -> Tuple[float, float]:
    """Translate the query planner hint into dense/sparse weights."""
    if not has_dense_vector:
        return 0.0, 1.0
    hint = query.get("routing_hint") or {}
    bias_value = {"low": 1.0, "medium": 2.0, "high": 3.0}
    dense = bias_value.get(str(hint.get("dense_bias") or "medium"), 2.0)
    sparse = bias_value.get(str(hint.get("sparse_bias") or "medium"), 2.0)
    primary = str(hint.get("primary") or "hybrid")
    if primary == "dense":
        dense, sparse = max(dense, 3.0), min(sparse, 1.0)
    elif primary in {"bm25", "metadata"}:
        dense, sparse = min(dense, 1.0), max(sparse, 3.0)
    elif primary == "benchmark_lookup":
        dense, sparse = min(dense, 2.0), max(sparse, 3.0)
    total = dense + sparse
    return dense / total, sparse / total


def supabase_rpc_params(
    query: Dict[str, Any],
    query_embedding: Sequence[float],
    match_count: int = 20,
) -> Dict[str, Any]:
    """Map the query schema to the filtered Supabase RPC contract."""
    pools = list(query.get("pools") or [])
    dense_weight, sparse_weight = retrieval_weights(query, has_dense_vector=True)
    return {
        "query_embedding": list(query_embedding),
        "match_count": max(1, min(int(match_count), 100)),
        "pool_filter": pools[0] if len(pools) == 1 else None,
        "task_filters": list(query.get("tasks") or []),
        "korean_required": bool(query.get("korean_required")),
        "min_parameter_count_billion": query.get("min_parameters_billion"),
        "max_parameter_count_billion": query.get("max_parameters_billion"),
        "min_context_length": query.get("min_context_length"),
        "max_context_length": query.get("max_context_length"),
        "require_known_parameters": bool(query.get("require_known_parameters")),
        "require_known_context": bool(query.get("require_known_context")),
        "popularity_tier_filter": query.get("popularity_tier"),
        # Expand language names and ordered translation pairs before the DB FTS
        # function receives the query; the original text remains in the report.
        "query_text": " ".join(sorted(normalize_query_terms(query.get("text") or ""))) or query.get("text") or "",
        "dense_weight": dense_weight,
        "sparse_weight": sparse_weight,
    }


def cosine(left: Sequence[float], right: Sequence[float]) -> float:
    if not left or not right or len(left) != len(right):
        return -1.0
    dot = sum(float(a) * float(b) for a, b in zip(left, right))
    left_norm = math.sqrt(sum(float(value) ** 2 for value in left))
    right_norm = math.sqrt(sum(float(value) ** 2 for value in right))
    if not left_norm or not right_norm:
        return -1.0
    return dot / (left_norm * right_norm)


def ranking_score(
    row: Dict[str, Any],
    query: Dict[str, Any],
    query_vector: Sequence[float] | None,
    benchmark_boost: float = 0.0,
    sparse_index: FieldedBM25 | None = None,
) -> Tuple[float, float, Dict[str, Any]]:
    signal = detect_task_conflict(row)
    has_dense_vector = query_vector is not None
    dense_score = (
        max(0.0, cosine(query_vector, row.get("embedding") or []))
        if has_dense_vector
        else 0.0
    )
    sparse_score = lexical_relevance(row, query, sparse_index=sparse_index)
    dense_weight, sparse_weight = retrieval_weights(query, has_dense_vector)
    raw = (dense_weight * dense_score) + (sparse_weight * sparse_score)
    signal = dict(signal)
    signal.update(
        {
            "dense_score": dense_score,
            "sparse_score": sparse_score,
            "dense_weight": dense_weight,
            "sparse_weight": sparse_weight,
            "retrieval_route": "hybrid" if has_dense_vector else "sparse",
        }
    )
    return raw, raw - float(signal["ranking_penalty"]) + benchmark_boost, signal


def benchmark_adjustments(
    rows: Sequence[Dict[str, Any]], query: Dict[str, Any]
) -> Dict[str, Dict[str, Any]]:
    """Return safe, query-specific benchmark boosts.

    A benchmark name alone gives a presence boost only. Numeric comparison is
    enabled only when dataset and metric are both explicit, so scores from
    different datasets or metrics are never compared.
    """

    spec = query.get("benchmark") or {}
    if not spec:
        return {}
    matched: Dict[str, List[Dict[str, Any]]] = {}
    for row in rows:
        records = match_benchmark_records(row, spec)
        if records:
            matched[row.get("model_id", "")] = records
    if not matched:
        return {}

    exact_numeric = bool(spec.get("dataset") and spec.get("metric"))
    selected: Dict[str, Dict[str, Any]] = {}
    for model_id, records in matched.items():
        numeric = [record for record in records if isinstance(record.get("score"), (int, float))]
        record = numeric[0] if numeric else records[0]
        selected[model_id] = {"record": record, "boost": BENCHMARK_PRESENCE_BOOST}

    if not exact_numeric:
        return selected

    comparable: Dict[Tuple[str, str, str, str, str], List[Tuple[str, float, bool]]] = {}
    for model_id, item in selected.items():
        record = item["record"]
        score = record.get("score")
        if not isinstance(score, (int, float)):
            continue
        comparable.setdefault(benchmark_key(record), []).append(
            (model_id, float(score), bool(record.get("higher_is_better", True)))
        )
    for values in comparable.values():
        if len(values) < 2:
            continue
        higher_is_better = values[0][2]
        scores = [value[1] for value in values]
        low, high = min(scores), max(scores)
        for model_id, score, _ in values:
            if high == low:
                quality = 1.0
            elif higher_is_better:
                quality = (score - low) / (high - low)
            else:
                quality = (high - score) / (high - low)
            selected[model_id]["boost"] = BENCHMARK_PRESENCE_BOOST + BENCHMARK_SCORE_BOOST * quality
    return selected


def dedupe_canonical(rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    selected: List[Dict[str, Any]] = []
    seen = set()
    for row in rows:
        metadata = filter_metadata(row)
        key = metadata.get("canonical_model_id") or row.get("canonical_model_id") or row.get("model_id")
        if key in seen:
            continue
        seen.add(key)
        selected.append(row)
    return selected


def diversify_results(
    rows: Sequence[Dict[str, Any]],
    limit: int,
    max_per_author: int = 2,
) -> List[Dict[str, Any]]:
    """Prefer distinct model families and authors while preserving score order."""
    selected: List[Dict[str, Any]] = []
    seen_canonical: set[str] = set()
    author_counts: Dict[str, int] = {}
    deferred: List[Dict[str, Any]] = []

    for row in rows:
        metadata = filter_metadata(row)
        canonical = str(
            metadata.get("canonical_model_id")
            or row.get("canonical_model_id")
            or row.get("model_id")
        )
        if canonical in seen_canonical:
            continue
        model_id = str(row.get("model_id") or "")
        author = model_id.split("/", 1)[0] if "/" in model_id else model_id
        if author_counts.get(author, 0) >= max_per_author:
            deferred.append(row)
            continue
        selected.append(row)
        seen_canonical.add(canonical)
        author_counts[author] = author_counts.get(author, 0) + 1
        if len(selected) >= limit:
            return selected

    for row in deferred:
        metadata = filter_metadata(row)
        canonical = str(
            metadata.get("canonical_model_id")
            or row.get("canonical_model_id")
            or row.get("model_id")
        )
        if canonical in seen_canonical:
            continue
        selected.append(row)
        seen_canonical.add(canonical)
        if len(selected) >= limit:
            break
    return selected


def relaxation_suggestions(
    rows: Sequence[Dict[str, Any]],
    query: Dict[str, Any],
    limit: int = 3,
) -> List[Dict[str, Any]]:
    """Explain safe, single-condition relaxations when hard filtering is empty."""
    plans: List[Tuple[str, str, Dict[str, Any], int]] = []

    def add_plan(code: str, label: str, changes: Dict[str, Any], relaxed: Dict[str, Any]) -> None:
        count = sum(1 for row in rows if hard_filter(row, relaxed)[0])
        if count:
            plans.append((code, label, changes, count))

    if query.get("require_known_parameters"):
        relaxed = dict(query)
        relaxed["require_known_parameters"] = False
        add_plan(
            "allow_unknown_parameters",
            "파라미터가 확인되지 않은 후보도 포함",
            {"require_known_parameters": False},
            relaxed,
        )
    if query.get("require_known_context"):
        relaxed = dict(query)
        relaxed["require_known_context"] = False
        add_plan(
            "allow_unknown_context",
            "context 길이가 확인되지 않은 후보도 포함",
            {"require_known_context": False},
            relaxed,
        )
    if query.get("min_context_length") is not None:
        relaxed = dict(query)
        relaxed.pop("min_context_length", None)
        add_plan(
            "remove_min_context",
            "최소 context 조건을 해제",
            {"min_context_length": None},
            relaxed,
        )
    if query.get("max_context_length") is not None:
        relaxed = dict(query)
        relaxed.pop("max_context_length", None)
        add_plan(
            "remove_max_context",
            "최대 context 조건을 해제",
            {"max_context_length": None},
            relaxed,
        )
    if query.get("max_parameters_billion") is not None:
        relaxed = dict(query)
        relaxed.pop("max_parameters_billion", None)
        add_plan(
            "remove_parameter_ceiling",
            "파라미터 상한을 해제",
            {"max_parameters_billion": None},
            relaxed,
        )
    if query.get("pools") and set(query["pools"]) != set(POOLS):
        relaxed = dict(query)
        relaxed["pools"] = list(POOLS)
        add_plan(
            "include_all_pools",
            "Core와 Low Popularity를 모두 검색",
            {"pools": list(POOLS)},
            relaxed,
        )
    if query.get("korean_required"):
        relaxed = dict(query)
        relaxed["korean_required"] = False
        add_plan(
            "remove_korean_constraint",
            "한국어 조건을 해제",
            {"korean_required": False},
            relaxed,
        )

    priority = {
        "allow_unknown_parameters": 0,
        "allow_unknown_context": 1,
        "include_all_pools": 2,
        "remove_min_context": 3,
        "remove_max_context": 3,
        "remove_parameter_ceiling": 4,
        "remove_korean_constraint": 5,
    }
    plans.sort(key=lambda item: (priority.get(item[0], 99), -item[3], item[0]))
    return [
        {
            "code": code,
            "label": label,
            "changes": changes,
            "candidate_count": count,
        }
        for code, label, changes, count in plans[:limit]
    ]


def check_results(rows: Sequence[Dict[str, Any]], query: Dict[str, Any]) -> Dict[str, Any]:
    task_violations = sum(1 for row in rows if not task_match(row, query))
    korean_violations = sum(
        1
        for row in rows
        if query.get("korean_required") and filter_metadata(row).get("korean_verified") is not True
    )
    unknown_parameter_violations = sum(
        1
        for row in rows
        if query.get("require_known_parameters")
        and not numeric_ok(filter_metadata(row).get("parameter_count_billion"), required=True)
    )
    unknown_context_violations = sum(
        1
        for row in rows
        if query.get("require_known_context")
        and not numeric_ok(filter_metadata(row).get("context_length"), required=True)
    )
    canonical_ids = [
        filter_metadata(row).get("canonical_model_id") or row.get("model_id")
        for row in rows
    ]
    canonical_duplicates = len(canonical_ids) - len(set(canonical_ids))
    return {
        "task_violations": task_violations,
        "korean_violations": korean_violations,
        "unknown_parameter_violations": unknown_parameter_violations,
        "unknown_context_violations": unknown_context_violations,
        "canonical_duplicates": canonical_duplicates,
        "task_conflicts": sum(1 for row in rows if detect_task_conflict(row)["conflict"]),
        "passed": not any(
            (
                task_violations,
                korean_violations,
                unknown_parameter_violations,
                unknown_context_violations,
                canonical_duplicates,
            )
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true", help="embed query text with OpenAI before ranking")
    parser.add_argument(
        "--evidence-rerank",
        action="store_true",
        help="rerank base model candidates with Stage 3 child evidence (no API call)",
    )
    parser.add_argument("--evidence-top-k", type=int, default=3)
    parser.add_argument("--evidence-candidate-limit", type=int, default=50)
    parser.add_argument("--evidence-weight", type=float, default=0.08)
    parser.add_argument("--top-k", type=int, default=None)
    parser.add_argument("--query-file", type=Path, default=QUERY_PATH)
    parser.add_argument("--report-json", type=Path, default=REPORT_JSON)
    parser.add_argument("--report-md", type=Path, default=REPORT_MD)
    args = parser.parse_args()

    load_dotenv(ROOT / ".env")
    rows = load_rows()
    sparse_index = FieldedBM25(rows)
    queries = load_queries(args.query_file)
    mode = "vector" if args.execute else "lexical_offline"

    query_vectors: Dict[int, List[float]] = {}
    if args.execute:
        from openai import OpenAI

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY required with --execute")
        client = OpenAI(api_key=api_key)
        response = client.embeddings.create(
            model=os.getenv("STAGE4_EMBEDDING_MODEL", "text-embedding-3-small"),
            input=[query["text"] for query in queries],
        )
        for item in response.data:
            query_vectors[item.index] = item.embedding
    catalog = load_catalog(DATA_DIR, POOLS)
    evidence_catalog = {}
    if args.evidence_rerank:
        evidence_catalog = load_index(
            [
                DATA_DIR / f"hf_models_stage3_parent_child_{pool}.jsonl"
                for pool in POOLS
            ]
        )
        if not evidence_catalog:
            raise RuntimeError(
                "--evidence-rerank requires Stage 3 parent-child sidecars; "
                "run evidence_index.py --pool all first"
            )

    reports: List[Dict[str, Any]] = []
    for query_index, query in enumerate(queries):
        eligible_rows: List[Dict[str, Any]] = []
        excluded = 0
        for row in rows:
            eligible, _ = hard_filter(row, query)
            if not eligible:
                excluded += 1
                continue
            eligible_rows.append(row)

        benchmark_info = benchmark_adjustments(eligible_rows, query)
        candidates: List[Dict[str, Any]] = []
        for row in eligible_rows:
            benchmark_signal = benchmark_info.get(row.get("model_id", ""), {})
            benchmark_boost = float(benchmark_signal.get("boost", 0.0))
            raw, adjusted, signal = ranking_score(
                row,
                query,
                query_vectors.get(query_index),
                benchmark_boost=benchmark_boost,
                sparse_index=sparse_index,
            )
            enriched = dict(row)
            enriched["_raw_score"] = raw
            enriched["_adjusted_score"] = adjusted
            enriched["_task_conflict"] = signal
            enriched["_benchmark_signal"] = benchmark_signal
            enriched["_dense_score"] = signal["dense_score"]
            enriched["_sparse_score"] = signal["sparse_score"]
            enriched["_retrieval_route"] = signal["retrieval_route"]
            candidates.append(enriched)

        candidates.sort(key=lambda row: (row["_adjusted_score"], row.get("model_id", "")), reverse=True)
        if args.evidence_rerank:
            candidates = attach_evidence_hits(
                candidates,
                str(query.get("text") or ""),
                evidence_catalog,
                top_k=args.evidence_top_k,
                candidate_limit=args.evidence_candidate_limit,
                weight=args.evidence_weight,
            )
        top_limit = args.top_k or query.get("top_k", 5)
        top = diversify_results(candidates, top_limit)
        checks = check_results(top, query)
        empty_reason = (
            "현재 조건을 모두 만족하는 후보가 없습니다."
            if not candidates
            else None
        )
        suggestions = (
            relaxation_suggestions(rows, query)
            if not candidates
            else []
        )
        result_rows = []
        for row in top:
            metadata = filter_metadata(row)
            task = row.get("task") or {}
            signal = row["_task_conflict"]
            benchmark_signal = row.get("_benchmark_signal") or {}
            benchmark_record = benchmark_signal.get("record") or {}
            result_rows.append(
                hydrate_result(
                    {
                    "model_id": row.get("model_id"),
                    "pool": row.get("source_pool"),
                    "source_pool": row.get("source_pool"),
                    "task": task.get("primary"),
                    "candidate_type": (row.get("candidate") or {}).get("type"),
                    "canonical_model_id": metadata.get("canonical_model_id"),
                    "parameter_count": metadata.get("parameter_count"),
                    "context_length": metadata.get("context_length"),
                    "evidence_completeness": row.get("evidence_completeness"),
                    "raw_score": round(row["_raw_score"], 6),
                    "base_score": round(row["_adjusted_score"], 6),
                    "score": round(float(row.get("_evidence_adjusted_score", row["_adjusted_score"])), 6),
                    "dense_score": round(float(row.get("_dense_score", 0.0)), 6),
                    "sparse_score": round(float(row.get("_sparse_score", 0.0)), 6),
                    "retrieval_route": row.get("_retrieval_route", "sparse"),
                    "evidence_score": round(float(row.get("_evidence_score") or 0.0), 6),
                    "evidence_hits": row.get("_evidence_hits") or [],
                    "task_conflict": signal["conflict"],
                    "task_conflict_severity": signal["severity"],
                    "task_conflict_evidence": signal["evidence"],
                    "task_conflict_penalty": signal["ranking_penalty"],
                    "benchmark_match": bool(benchmark_signal),
                    "benchmark_boost": benchmark_signal.get("boost", 0.0),
                    "benchmark": benchmark_record.get("benchmark"),
                    "benchmark_dataset": benchmark_record.get("dataset"),
                    "benchmark_metric": benchmark_record.get("metric"),
                    "benchmark_score": benchmark_record.get("score"),
                    "benchmark_evidence_ref": benchmark_record.get("evidence_ref"),
                    "benchmark_metadata": row.get("benchmark_metadata") or {},
                    },
                    catalog,
                )
            )
        reports.append(
            {
                "query_id": query["id"],
                "text": query["text"],
                "mode": mode,
                "candidate_count": len(candidates),
                "excluded_count": excluded,
                "top_k": len(top),
                "empty_reason": empty_reason,
                "relaxation_suggestions": suggestions,
                "checks": checks,
                "results": result_rows,
            }
        )

    summary = {
        "mode": mode,
        "query_count": len(queries),
        "row_count": len(rows),
        "passed_queries": sum(1 for report in reports if report["checks"]["passed"]),
        "failed_queries": sum(1 for report in reports if not report["checks"]["passed"]),
        "empty_queries": sum(1 for report in reports if report["candidate_count"] == 0),
        "task_conflict_penalty_enabled": True,
        "benchmark_queries": sum(1 for query in queries if query.get("benchmark")),
        "retrieval_routes": sorted(
            {
                result.get("retrieval_route", "sparse")
                for report in reports
                for result in report.get("results", [])
            }
        ),
        "hybrid_fusion_enabled": bool(args.execute),
        "evidence_rerank_enabled": bool(args.evidence_rerank),
        "evidence_index_version": 1 if args.evidence_rerank else None,
        "evidence_rerank_weight": args.evidence_weight if args.evidence_rerank else 0.0,
        "benchmark_boost_enabled": any(
            bool((row.get("benchmark_metadata") or {}).get("results")) for row in rows
        ),
        "reports": reports,
    }
    args.report_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        f"# Stage 4 retrieval validation ({mode})",
        "",
        f"질의: {len(queries)} · 통과: {summary['passed_queries']} · 실패: {summary['failed_queries']} · 빈 결과: {summary['empty_queries']}",
        "",
        "task conflict는 후보를 삭제하지 않고 점수에 penalty를 적용했다.",
        f"benchmark 질의: {summary['benchmark_queries']}개 · benchmark 점수는 동일 dataset·metric 조건에서만 비교했다.",
    ]
    for report in reports:
        checks = report["checks"]
        lines.extend(
            [
                "",
                f"## {report['query_id']} {report['text']}",
                f"후보 {report['candidate_count']}개, 결과 {report['top_k']}개, 통과={checks['passed']}",
                f"task 위반={checks['task_violations']}, 한국어 위반={checks['korean_violations']}, "
                f"unknown 위반={checks['unknown_parameter_violations'] + checks['unknown_context_violations']}, "
                f"canonical 중복={checks['canonical_duplicates']}, task conflict={checks['task_conflicts']}",
            ]
        )
        if report.get("empty_reason"):
            lines.append(f"- {report['empty_reason']}")
            for suggestion in report.get("relaxation_suggestions", []):
                lines.append(
                    f"- 조건 완화 제안: {suggestion['label']} "
                    f"(후보 {suggestion['candidate_count']}개)"
                )
        for result in report["results"]:
            conflict = f" [task_conflict penalty={result['task_conflict_penalty']}]" if result["task_conflict"] else ""
            benchmark = (
                f" [benchmark {result['benchmark']} {result['benchmark_metric']}"
                f" score={result['benchmark_score']} boost={result['benchmark_boost']}]"
                if result["benchmark_match"] else ""
            )
            lines.append(
                f"- `{result['model_id']}` · {result['task']} · score={result['score']:.4f} "
                f"(raw={result['raw_score']:.4f}, route={result.get('retrieval_route', 'sparse')}, "
                f"dense={result.get('dense_score', 0.0):.4f}, "
                f"sparse={result.get('sparse_score', 0.0):.4f}){conflict}{benchmark}"
            )
            if result["task_conflict"]:
                lines.append(f"  - conflict evidence: {', '.join(result['task_conflict_evidence'])}")
    args.report_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "mode": mode,
                "queries": len(queries),
                "passed": summary["passed_queries"],
                "failed": summary["failed_queries"],
                "empty": summary["empty_queries"],
                "task_conflict_penalty": True,
                "benchmark_queries": summary["benchmark_queries"],
                "benchmark_boost": True,
                "report": str(args.report_md),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
