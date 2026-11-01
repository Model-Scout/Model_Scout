#!/usr/bin/env python3
"""09 - Model Scout read-only MCP server.

This server exposes a small, safe tool surface for a LangChain agent:

* ``search_models`` calls the production Supabase hybrid-search RPC.
* ``get_model`` reads one active model without returning its raw vector.
* ``get_model_evidence`` reads compact README evidence parent/child records.
* ``compare_models`` reads a bounded set of active models for comparison.

The server intentionally does not expose arbitrary SQL, INSERT, UPDATE, DELETE,
DDL, or Supabase sync operations. Database connections are read-only and use
the same SUPABASE_DB_* environment variables as 08_sync_supabase.py.

Run directly through stdio (normally launched by 10_model_scout_langchain_agent.py):

    python 09_model_scout_mcp_readonly.py
"""

from __future__ import annotations

import json
import math
import os
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence

import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from openai import OpenAI

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:  # pragma: no cover - exercised during setup only
    raise SystemExit(
        "MCP dependencies are missing. Install with: "
        "python -m pip install -r requirements_mcp.txt"
    ) from exc


ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

DEFAULT_EMBEDDING_MODEL = "text-embedding-3-small"
MAX_SEARCH_RESULTS = 5
MAX_COMPARE_MODELS = 10
MAX_EVIDENCE_PARENTS = 8
MAX_EVIDENCE_CHILDREN = 5
MAX_TEXT_CHARS = 900
MAX_QUOTE_CHARS = 600
SEARCH_EVIDENCE_PARENTS = 1
SEARCH_EVIDENCE_CHILDREN = 2
SEARCH_TEXT_CHARS = 350

DOMAIN_MARKERS = {
    "금융": ("금융", "financial", "finance", "banking", "stock", "투자", "nmixx-fin"),
    "법률": ("법률", "legal", "law", "법학"),
    "의료": ("의료", "medical", "clinical", "healthcare", "biomedical"),
    "교육": ("교육", "education", "student", "academic"),
    "코드": ("코드 생성", "code generation", "coding", "programming", "소프트웨어 개발"),
    "음성": ("음성", "speech recognition", "automatic speech recognition", "asr", "transcription"),
}
GENERAL_MARKERS = (
    "general-purpose",
    "general purpose",
    "multilingual",
    "paraphrase",
    "sentence embedding",
    "sentence similarity",
    "다국어",
    "문장 임베딩",
    "문장 유사",
)

# Hugging Face uses both tags for embedding-oriented models in this corpus.
# The agent may naturally say "embedding" or "document-embedding", so expand
# those aliases before they reach the strict RPC task filter.
TASK_FILTER_ALIASES = {
    "embedding": ("feature-extraction", "sentence-similarity"),
    "embeddings": ("feature-extraction", "sentence-similarity"),
    "document-embedding": ("feature-extraction", "sentence-similarity"),
    "document-embeddings": ("feature-extraction", "sentence-similarity"),
    "text-embedding": ("feature-extraction", "sentence-similarity"),
    "semantic-search": ("feature-extraction", "sentence-similarity"),
}
EMBEDDING_QUERY_MARKERS = (
    "임베딩",
    "벡터 검색",
    "벡터검색",
    "문서 유사도",
    "문장 유사도",
    "embedding",
    "vector search",
    "semantic search",
    "sentence similarity",
    "retrieval embedding",
)
KOREAN_QUERY_MARKERS = ("한국어", "국문", "korean")

DB_ENV = (
    "SUPABASE_DB_HOST",
    "SUPABASE_DB_PORT",
    "SUPABASE_DB_NAME",
    "SUPABASE_DB_USER",
    "SUPABASE_PASSWORD",
)

mcp = FastMCP("model-scout-readonly")


def _missing_environment(names: Iterable[str]) -> List[str]:
    return [name for name in names if not os.getenv(name)]


def _embedding_model() -> str:
    return os.getenv("STAGE4_EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL)


def _expand_task_filters(task_filters: Optional[Sequence[str]]) -> List[str]:
    """Normalize natural embedding labels to the corpus' actual task tags."""

    expanded: List[str] = []
    for value in task_filters or []:
        normalized = str(value).strip().lower()
        if not normalized:
            continue
        values = TASK_FILTER_ALIASES.get(normalized, (normalized,))
        for item in values:
            if item not in expanded:
                expanded.append(item)
    return expanded


def _contains_marker(query: str, markers: Sequence[str]) -> bool:
    normalized = query.casefold()
    return any(marker.casefold() in normalized for marker in markers)


def _db_connection() -> psycopg2.extensions.connection:
    """Open a bounded, TLS, PostgreSQL read-only connection."""

    missing = _missing_environment(DB_ENV)
    if missing:
        raise RuntimeError(
            "Missing Supabase environment variables: " + ", ".join(missing)
        )

    connection = psycopg2.connect(
        host=os.environ["SUPABASE_DB_HOST"],
        port=int(os.environ["SUPABASE_DB_PORT"]),
        dbname=os.environ["SUPABASE_DB_NAME"],
        user=os.environ["SUPABASE_DB_USER"],
        password=os.environ["SUPABASE_PASSWORD"],
        sslmode="require",
        connect_timeout=15,
        options="-c default_transaction_read_only=on -c statement_timeout=15000",
    )
    connection.set_session(readonly=True, autocommit=True)
    return connection


@contextmanager
def _read_connection() -> Iterator[psycopg2.extensions.connection]:
    """Close every short-lived MCP connection after the tool call."""

    connection = _db_connection()
    try:
        yield connection
    finally:
        connection.close()


def _vector_literal(values: Sequence[float]) -> str:
    if len(values) != 1536:
        raise ValueError(f"Expected 1536 query dimensions, got {len(values)}")
    cleaned: List[str] = []
    for value in values:
        number = float(value)
        if not math.isfinite(number):
            raise ValueError("Query embedding contains a non-finite value")
        cleaned.append(format(number, ".9g"))
    return "[" + ",".join(cleaned) + "]"


def _query_embedding(query: str) -> List[float]:
    text = query.strip()
    if not text:
        raise ValueError("query must not be empty")
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for semantic model search")

    response = OpenAI(api_key=os.environ["OPENAI_API_KEY"]).embeddings.create(
        model=_embedding_model(),
        input=text,
    )
    return list(response.data[0].embedding)


def _truncate(value: Any, limit: int = MAX_TEXT_CHARS) -> Any:
    if not isinstance(value, str):
        return value
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def _exact_quote(value: Any, limit: int = MAX_QUOTE_CHARS) -> Optional[str]:
    """Return a contiguous README excerpt without adding generated wording."""
    if not isinstance(value, str):
        return None
    quote = value.strip()
    if not quote:
        return None
    # A truncated quote is still an exact contiguous excerpt.  The flag in
    # the citation tells the caller that the complete evidence block is longer.
    return quote[:limit]


def _readme_section(parent: Mapping[str, Any], child: Optional[Mapping[str, Any]] = None) -> str:
    """Normalize the evidence location to a human-readable README section."""
    child = child or {}
    heading_path = child.get("heading_path") or parent.get("heading_path")
    if isinstance(heading_path, list) and heading_path:
        return " > ".join(str(part) for part in heading_path)
    section = child.get("section") or parent.get("section")
    return str(section).strip() if section else "README root"


def _evidence_level(parent: Mapping[str, Any], child: Optional[Mapping[str, Any]] = None) -> str:
    child = child or {}
    value = child.get("evidence_level") or parent.get("evidence_level")
    if value:
        return str(value).strip()
    # The quote itself is an exact excerpt from the persisted README.  When
    # the older evidence index has no explicit level field, expose that fact
    # as explicit source evidence rather than losing the distinction.
    source = child if child else parent
    return "explicit" if isinstance(source.get("text"), str) and source.get("text").strip() else "unknown"


def _compact_citations(
    parents: Any,
    *,
    limit: int = 3,
    quote_limit: int = MAX_QUOTE_CHARS,
) -> List[Dict[str, Any]]:
    """Expose exact README excerpts in a small, audit-friendly shape."""
    if not isinstance(parents, list):
        return []

    candidates_with_score = []
    seen_quotes = set()
    order = 0
    for parent in parents:
        if not isinstance(parent, Mapping):
            continue
        raw_children = parent.get("children") or []
        children = raw_children if isinstance(raw_children, list) else []
        candidates: List[Optional[Mapping[str, Any]]] = [
            child for child in children if isinstance(child, Mapping)
        ]
        # Keep a parent fallback for README sections that have no atomic child.
        candidates.append(None)
        for child in candidates:
            source = child if child is not None else parent
            raw_text = source.get("text")
            quote = _exact_quote(raw_text, quote_limit)
            if not quote or quote in seen_quotes:
                continue
            seen_quotes.add(quote)
            normalized = quote.casefold()
            section = _readme_section(parent, child)
            score = min(len(quote), 300) / 100
            score += sum(
                1
                for marker in (
                    "embedding",
                    "sentence",
                    "semantic",
                    "korean",
                    "usage",
                    "retrieval",
                    "query",
                )
                if marker in normalized or marker in section.casefold()
            )
            if section.casefold() == "document":
                score -= 1
            if normalized.startswith(("---", "license:", "- feature-extraction", "pipeline_tag:")):
                score -= 2
            candidates_with_score.append(
                (
                    -score,
                    order,
                    {
                        "supporting_quote": quote,
                        "readme_section": section,
                        "evidence_level": _evidence_level(parent, child),
                        "evidence_refs": source.get("evidence_refs") or [],
                        "quote_truncated": isinstance(raw_text, str) and len(raw_text.strip()) > quote_limit,
                    },
                )
            )
            order += 1

    candidates_with_score.sort(key=lambda item: (item[0], item[1]))
    return [item[2] for item in candidates_with_score[:limit]]


def _domain_scope(row: Mapping[str, Any]) -> Dict[str, Any]:
    """Classify scope conservatively from stored metadata and model ID."""
    searchable = {
        "model_id": row.get("model_id"),
        "filter_metadata": row.get("filter_metadata"),
        "technical_metadata": row.get("technical_metadata"),
        "semantic_metadata": row.get("semantic_metadata"),
    }
    haystack = json.dumps(searchable, ensure_ascii=False, default=str).casefold()

    matched_domains = [
        domain
        for domain, markers in DOMAIN_MARKERS.items()
        if any(marker.casefold() in haystack for marker in markers)
    ]
    if matched_domains:
        return {
            "label": "domain_specific",
            "domains": matched_domains,
            "basis": "stored metadata/model ID keyword evidence",
        }

    matched_general = [
        marker
        for marker in GENERAL_MARKERS
        if marker.casefold() in haystack
    ]
    if matched_general:
        return {
            "label": "general_purpose",
            "domains": [],
            "basis": "stored metadata/model ID keyword evidence",
            "matched_terms": matched_general[:3],
        }

    return {
        "label": "unknown",
        "domains": [],
        "basis": "no explicit domain scope found in stored metadata/model ID",
    }


def _compact_evidence(
    parents: Any,
    *,
    parent_limit: int = MAX_EVIDENCE_PARENTS,
    child_limit: int = MAX_EVIDENCE_CHILDREN,
    text_limit: int = MAX_TEXT_CHARS,
) -> List[Dict[str, Any]]:
    """Keep source text useful to the agent without dumping full README data."""

    if not isinstance(parents, list):
        return []

    compact: List[Dict[str, Any]] = []
    for parent in parents[:parent_limit]:
        if not isinstance(parent, Mapping):
            continue
        item: Dict[str, Any] = {}
        for key in ("parent_id", "section", "heading_path", "child_ids"):
            if key in parent:
                item[key] = parent[key]
        if "text" in parent:
            item["text"] = _truncate(parent["text"], text_limit)

        children: List[Dict[str, Any]] = []
        raw_children = parent.get("children") or []
        if isinstance(raw_children, list):
            for child in raw_children[:child_limit]:
                if not isinstance(child, Mapping):
                    continue
                child_item: Dict[str, Any] = {}
                for key in (
                    "child_id",
                    "content_type",
                    "heading_path",
                    "evidence_level",
                    "evidence_refs",
                ):
                    if key in child:
                        child_item[key] = child[key]
                if "text" in child:
                    child_item["text"] = _truncate(child["text"], text_limit)
                children.append(child_item)
        if children:
            item["children"] = children
        compact.append(item)
    return compact


def _score(value: Any) -> Optional[float]:
    if value is None:
        return None
    return float(value)


def _compact_filter_metadata(value: Any) -> Dict[str, Any]:
    if not isinstance(value, Mapping):
        return {}
    keys = (
        "primary_task",
        "matched_tasks",
        "candidate_tier",
        "candidate_type",
        "korean_verified",
        "korean_evidence",
        "multilingual_verified",
        "languages",
        "parameter_count",
        "parameter_count_billion",
        "context_length",
        "architecture",
        "model_type",
        "quantization",
        "artifacts",
        "hardware",
        "runtime_compatibility",
        "license",
        "popularity_tier",
        "evidence_completeness",
        "task_conflict",
        "task_conflict_severity",
    )
    return {key: value[key] for key in keys if key in value}


def _compact_claims(value: Any, limit: int = 3) -> List[Any]:
    if not isinstance(value, list):
        return []
    compact: List[Any] = []
    for item in value[:limit]:
        if isinstance(item, Mapping):
            selected = {}
            for key in (
                "text",
                "claim",
                "summary",
                "supporting_quote",
                "evidence_level",
                "evidence_refs",
            ):
                if key in item:
                    selected[key] = _truncate(item[key], 350)
            compact.append(selected or dict(item))
        else:
            compact.append(_truncate(item, 350))
    return compact


def _compact_semantic_metadata(value: Any) -> Dict[str, Any]:
    if not isinstance(value, Mapping):
        return {}
    result: Dict[str, Any] = {}
    summary = value.get("summary")
    if summary:
        result["summary"] = _truncate(summary, 500)
    for key in (
        "documented_strengths",
        "documented_limitations",
        "use_cases",
        "benchmarks",
        "license_notes",
        "unknowns",
        "warnings",
    ):
        claims = _compact_claims(value.get(key))
        if claims:
            result[key] = claims
    if "evidence_completeness" in value:
        result["evidence_completeness"] = value["evidence_completeness"]
    return result


def _compact_benchmark_metadata(value: Any) -> Dict[str, Any]:
    if not isinstance(value, Mapping):
        return {}
    result: Dict[str, Any] = {
        key: value[key]
        for key in ("benchmark_version", "readme_available", "readme_path", "readme_sha256")
        if key in value
    }
    summary = value.get("summary")
    if isinstance(summary, Mapping):
        result["summary"] = {
            key: summary[key]
            for key in (
                "numeric_results",
                "ranking_eligible",
                "mentions_only",
                "quantized_ambiguous",
                "retained_result_count",
                "results_truncated",
            )
            if key in summary
        }
    compact_results: List[Dict[str, Any]] = []
    for item in (value.get("results") or [])[:8]:
        if not isinstance(item, Mapping):
            continue
        compact_results.append(
            {
                key: item[key]
                for key in (
                    "benchmark",
                    "dataset",
                    "metric",
                    "score",
                    "higher_is_better",
                    "model_name",
                    "variant_kind",
                    "comparability",
                    "evidence_ref",
                )
                if key in item
            }
        )
    if compact_results:
        result["results_preview"] = compact_results
    mentions = _compact_claims(value.get("mentions"), limit=3)
    if mentions:
        result["mentions_preview"] = mentions
    return result


def _compact_provenance(value: Any) -> Dict[str, Any]:
    if not isinstance(value, Mapping):
        return {}
    result: Dict[str, Any] = {}
    for source_name in ("hub", "readme", "model_card"):
        source = value.get(source_name)
        if isinstance(source, Mapping):
            result[source_name] = {
                key: source[key]
                for key in ("url", "path", "available", "source", "error")
                if key in source
            }
        elif source is not None:
            result[source_name] = _truncate(source, 500)
    for key in ("url", "readme_url", "model_card_url"):
        if key in value:
            result[key] = value[key]
    return result


def _compact_search_row(row: Mapping[str, Any]) -> Dict[str, Any]:
    """Return agent-facing fields; never return the raw 1536-dimension vector."""

    model_id = row.get("model_id")
    evidence_index = row.get("evidence_index")
    evidence_preview = _compact_evidence(
        evidence_index,
        parent_limit=SEARCH_EVIDENCE_PARENTS,
        child_limit=SEARCH_EVIDENCE_CHILDREN,
        text_limit=SEARCH_TEXT_CHARS,
    )
    citations = _compact_citations(evidence_index, limit=1)
    primary_citation = citations[0] if citations else {
        "supporting_quote": None,
        "readme_section": None,
        "evidence_level": "unknown",
        "evidence_refs": [],
        "quote_truncated": False,
    }
    return {
        "model_id": model_id,
        "model_url": f"https://huggingface.co/{model_id}" if model_id else None,
        "source_pool": row.get("source_pool"),
        "ranking": {
            "rank_score": _score(row.get("similarity")),
            "dense_similarity": _score(row.get("dense_similarity")),
            "sparse_score": _score(row.get("sparse_score")),
            "interpretation": "ranking score, not calibrated confidence",
        },
        "candidate": row.get("candidate") or {},
        "task": row.get("task") or {},
        "language": row.get("language") or {},
        "popularity": row.get("popularity") or {},
        "family": row.get("family") or {},
        "filter_metadata": _compact_filter_metadata(row.get("filter_metadata")),
        "technical_metadata": _compact_filter_metadata(row.get("technical_metadata")),
        "semantic_metadata": _compact_semantic_metadata(row.get("semantic_metadata")),
        "benchmark_metadata": _compact_benchmark_metadata(row.get("benchmark_metadata")),
        "source_provenance": _compact_provenance(row.get("source_provenance")),
        "task_consistency": row.get("task_consistency") or {},
        "domain_scope": _domain_scope(row),
        "audit_evidence": primary_citation,
        "evidence_preview": evidence_preview,
    }


def _model_select_sql() -> str:
    return """
        select
            m.model_id,
            m.source_pool,
            m.source_stage1_version,
            m.source_stage2_version,
            m.source_stage3_version,
            m.source_stage4_version,
            m.candidate,
            m.task,
            m.language,
            m.popularity,
            m.family,
            m.filter_metadata,
            m.technical_metadata,
            m.semantic_metadata,
            m.evidence,
            m.benchmark_metadata,
            m.source_provenance,
            m.task_consistency,
            m.document_hash,
            m.embedding_model,
            m.embedding_dimensions,
            e.parents as evidence_index,
            e.parent_count,
            e.child_count
        from public.model_scout_models as m
        left join public.model_scout_evidence as e
          on e.model_id = m.model_id
         and e.active = true
        where m.active = true
    """


@mcp.tool(
    description=(
        "Search active Korean-model recommendations using the production Supabase "
        "hybrid vector + sparse RPC. Use explicit filters when the user gives them. "
        "Returned scores are ranking scores, not confidence probabilities."
    )
)
def search_models(
    query: str,
    match_count: int = 5,
    pool_filter: Optional[str] = None,
    task_filters: Optional[List[str]] = None,
    korean_required: bool = False,
    min_parameter_count_billion: Optional[float] = None,
    max_parameter_count_billion: Optional[float] = None,
    min_context_length: Optional[int] = None,
    max_context_length: Optional[int] = None,
    require_known_parameters: bool = False,
    require_known_context: bool = False,
    popularity_tier_filter: Optional[str] = None,
) -> Dict[str, Any]:
    """Search the production corpus through the read-only match RPC."""

    count = min(max(int(match_count), 1), MAX_SEARCH_RESULTS)
    requested_task_filters = list(task_filters or [])
    applied_task_filters = _expand_task_filters(requested_task_filters)
    embedding_intent_detected = _contains_marker(query, EMBEDDING_QUERY_MARKERS)
    if not applied_task_filters and embedding_intent_detected:
        # Prevent a natural-language embedding request from falling through to
        # semantically similar translation or generation models when the agent
        # forgets to provide a task filter.
        applied_task_filters = list(TASK_FILTER_ALIASES["embedding"])
    korean_intent_detected = _contains_marker(query, KOREAN_QUERY_MARKERS)
    applied_korean_required = bool(korean_required or korean_intent_detected)
    embedding = _query_embedding(query)
    statement = """
        select
            model_id,
            source_pool,
            candidate,
            task,
            language,
            popularity,
            family,
            filter_metadata,
            technical_metadata,
            semantic_metadata,
            evidence,
            benchmark_metadata,
            source_provenance,
            task_consistency,
            evidence_index,
            dense_similarity,
            sparse_score,
            similarity
        from public.match_model_scout_models(
            %s::vector,
            %s::integer,
            %s::text,
            %s::text[],
            %s::boolean,
            %s::numeric,
            %s::numeric,
            %s::integer,
            %s::integer,
            %s::boolean,
            %s::boolean,
            %s::text,
            %s::text,
            %s::real,
            %s::real
        )
    """
    parameters = (
        _vector_literal(embedding),
        count,
        pool_filter,
        applied_task_filters or None,
        applied_korean_required,
        min_parameter_count_billion,
        max_parameter_count_billion,
        min_context_length,
        max_context_length,
        bool(require_known_parameters),
        bool(require_known_context),
        popularity_tier_filter,
        query,
        0.65,
        0.35,
    )

    with _read_connection() as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(statement, parameters)
            rows = cursor.fetchall()

    return {
        "query": query,
        "embedding_model": _embedding_model(),
        "filters": {
            "pool_filter": pool_filter,
            "requested_task_filters": requested_task_filters,
            "task_filters": applied_task_filters,
            "korean_required": applied_korean_required,
            "min_parameter_count_billion": min_parameter_count_billion,
            "max_parameter_count_billion": max_parameter_count_billion,
            "min_context_length": min_context_length,
            "max_context_length": max_context_length,
            "require_known_parameters": require_known_parameters,
            "require_known_context": require_known_context,
            "popularity_tier_filter": popularity_tier_filter,
        },
        "routing": {
            "embedding_intent_detected": embedding_intent_detected,
            "korean_intent_detected": korean_intent_detected,
        },
        "count": len(rows),
        "results": [_compact_search_row(row) for row in rows],
    }


@mcp.tool(
    description=(
        "Get the complete active metadata for one exact model ID. "
        "Use this after search_models when a user asks for details."
    )
)
def get_model(model_id: str) -> Dict[str, Any]:
    """Read one active model by its exact Hugging Face model ID."""

    normalized_id = model_id.strip()
    if not normalized_id:
        raise ValueError("model_id must not be empty")

    with _read_connection() as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(
                _model_select_sql() + " and m.model_id = %s",
                (normalized_id,),
            )
            row = cursor.fetchone()

    if row is None:
        return {"found": False, "model_id": normalized_id}
    result = _compact_search_row(row)
    result["found"] = True
    result["versions"] = {
        "stage1": row.get("source_stage1_version"),
        "stage2": row.get("source_stage2_version"),
        "stage3": row.get("source_stage3_version"),
        "stage4": row.get("source_stage4_version"),
    }
    result["embedding"] = {
        "model": row.get("embedding_model"),
        "dimensions": row.get("embedding_dimensions"),
        "document_hash": row.get("document_hash"),
    }
    result["evidence_counts"] = {
        "parents": row.get("parent_count") or 0,
        "children": row.get("child_count") or 0,
    }
    return result


@mcp.tool(
    description=(
        "Get source-backed README evidence for one exact model. "
        "Use this before making claims about strengths, limitations, benchmarks, "
        "runtime support, or documented use cases."
    )
)
def get_model_evidence(
    model_id: str,
    parent_limit: int = 5,
    child_limit: int = 4,
) -> Dict[str, Any]:
    """Read compact, source-backed parent/child evidence for one model."""

    normalized_id = model_id.strip()
    if not normalized_id:
        raise ValueError("model_id must not be empty")

    parent_limit = min(max(int(parent_limit), 1), MAX_EVIDENCE_PARENTS)
    child_limit = min(max(int(child_limit), 1), MAX_EVIDENCE_CHILDREN)

    with _read_connection() as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(
                _model_select_sql() + " and m.model_id = %s",
                (normalized_id,),
            )
            row = cursor.fetchone()

    if row is None:
        return {"found": False, "model_id": normalized_id, "parents": []}

    filter_metadata = row.get("filter_metadata") or {}
    evidence_index = row.get("evidence_index")
    citations = _compact_citations(evidence_index, limit=3)
    primary_citation = citations[0] if citations else {
        "supporting_quote": None,
        "readme_section": None,
        "evidence_level": "unknown",
        "evidence_refs": [],
        "quote_truncated": False,
    }
    return {
        "found": True,
        "model_id": normalized_id,
        "model_url": f"https://huggingface.co/{normalized_id}",
        "source_pool": row.get("source_pool"),
        "source_provenance": row.get("source_provenance") or {},
        "evidence_completeness": filter_metadata.get("evidence_completeness"),
        "domain_scope": _domain_scope(row),
        "audit_evidence": {
            **primary_citation,
            "additional_citations": citations[1:],
        },
        "parent_count": row.get("parent_count") or 0,
        "child_count": row.get("child_count") or 0,
        "parents": _compact_evidence(
            evidence_index,
            parent_limit=parent_limit,
            child_limit=child_limit,
        ),
    }


@mcp.tool(
    description=(
        "Compare up to ten exact active model IDs using the same metadata shape "
        "as search results. This is read-only and does not re-rank models."
    )
)
def compare_models(model_ids: List[str]) -> Dict[str, Any]:
    """Read a bounded set of exact models for deterministic comparison."""

    normalized_ids: List[str] = []
    for model_id in model_ids:
        value = str(model_id).strip()
        if value and value not in normalized_ids:
            normalized_ids.append(value)
    if not normalized_ids:
        raise ValueError("model_ids must contain at least one non-empty ID")
    if len(normalized_ids) > MAX_COMPARE_MODELS:
        raise ValueError(f"compare_models accepts at most {MAX_COMPARE_MODELS} IDs")

    with _read_connection() as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(
                _model_select_sql() + " and m.model_id = any(%s::text[])",
                (normalized_ids,),
            )
            rows = cursor.fetchall()

    by_id = {row["model_id"]: _compact_search_row(row) for row in rows}
    return {
        "requested_model_ids": normalized_ids,
        "found_count": len(by_id),
        "missing_model_ids": [
            model_id for model_id in normalized_ids if model_id not in by_id
        ],
        "models": [by_id[model_id] for model_id in normalized_ids if model_id in by_id],
    }


def main() -> int:
    # stdio is the transport used by LangChain's MultiServerMCPClient.
    mcp.run(transport="stdio")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
