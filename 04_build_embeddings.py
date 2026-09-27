#!/usr/bin/env python3
"""Build Stage 4 search documents and optional OpenAI embeddings.

The default command is a network-free dry-run. Use ``--execute`` to call the
configured embedding provider. Stage 4 preserves no-source rows as metadata-only
documents and validates the Stage 1/2/3 lineage before processing.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import tempfile
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
POOLS = ("core", "low_popularity")
DEFAULT_MODEL = "text-embedding-3-small"
DEFAULT_BATCH_SIZE = 32
STAGE4_VERSION = 1
EXPECTED_STAGE1_VERSION = 7
EXPECTED_STAGE2_VERSION = 6
EXPECTED_STAGE3_VERSION = 1


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


def annotate_task_conflict(row: Dict[str, Any]) -> Dict[str, Any]:
    """Return a row copy with an auditable task consistency signal."""

    result = dict(row)
    signal = detect_task_conflict(result)
    result["task_consistency"] = signal
    filter_metadata = dict(result.get("filter_metadata") or {})
    filter_metadata["task_conflict"] = signal["conflict"]
    filter_metadata["task_conflict_severity"] = signal["severity"]
    filter_metadata["task_conflict_evidence"] = signal["evidence"]
    filter_metadata["task_conflict_penalty"] = signal["ranking_penalty"]
    result["filter_metadata"] = filter_metadata
    return result



def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(path)
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number}: expected JSON object")
            rows.append(value)
    return rows


def write_jsonl_atomic(rows: Sequence[Dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    os.close(fd)
    temporary = Path(name)
    try:
        with temporary.open("w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return " ".join(str(value).split())


def list_text(value: Any) -> str:
    if not isinstance(value, list):
        return text(value)
    return ", ".join(text(item) for item in value if text(item))


def claim_lines(value: Any) -> List[str]:
    if not isinstance(value, list):
        return []
    lines = []
    for claim in value:
        if isinstance(claim, dict) and text(claim.get("text")):
            lines.append(f"[{text(claim.get('evidence_level')) or 'unknown'}] {text(claim['text'])}")
    return lines


def build_embedding_text(row: Dict[str, Any]) -> str:
    source = row.get("source_stage2") or {}
    task = source.get("task") or {}
    candidate = source.get("candidate") or {}
    language = source.get("language") or {}
    language_stage1 = language.get("stage1") or {}
    model = source.get("model") or {}
    family = source.get("family") or {}
    popularity = source.get("popularity") or {}
    stage1_popularity = popularity.get("stage1") or {}
    semantic = row.get("semantic") or {}
    summary = semantic.get("summary") or {}

    korean = language.get("korean")
    multilingual = language.get("multilingual")
    korean_verified = korean.get("verified") if isinstance(korean, dict) else korean
    multilingual_verified = multilingual.get("verified") if isinstance(multilingual, dict) else multilingual

    lines = [
        f"model_id: {text(row.get('model_id'))}",
        f"author: {text(source.get('author'))}",
        f"task: {text(task.get('primary'))}",
        f"matched_tasks: {list_text(task.get('matched'))}",
        f"Korean support evidence: {text(candidate.get('type'))}; {list_text(candidate.get('evidence'))}",
        f"declared languages: {list_text(language.get('declared_languages')) or list_text(language_stage1.get('languages'))}",
        f"language flags: korean_verified={korean_verified}; multilingual_verified={multilingual_verified}; bilingual={language.get('bilingual')}",
        f"architecture: {text(model.get('type'))}; {list_text(model.get('architectures'))}",
        f"parameter count: {text(model.get('parameter_count'))}; billion: {text(model.get('parameter_count_billion'))}",
        f"context length: {text(model.get('context_length'))}",
        f"dtype: {text(model.get('dtype'))}",
        f"quantization: {text(source.get('quantization'))}",
        f"artifacts: {text(source.get('artifacts'))}",
        f"license: {text(source.get('license'))}",
        f"canonical model: {text(family.get('canonical_model_id'))}",
        f"variant: {family.get('is_variant')}; variant types: {list_text(family.get('variant_types'))}",
        f"hardware estimate: {text(source.get('hardware'))}",
        f"stage1 downloads: {text(stage1_popularity.get('downloads'))}; popularity tier: {text(stage1_popularity.get('tier'))}",
        f"documented summary: {text(summary.get('text'))}",
    ]
    for label, field in (
        ("documented strengths", "documented_strengths"),
        ("documented limitations", "documented_limitations"),
        ("use cases", "use_cases"),
        ("benchmarks", "benchmarks"),
        ("license notes", "license_notes"),
        ("warnings", "warnings"),
    ):
        values = claim_lines(semantic.get(field))
        lines.append(f"{label}: " + (" | ".join(values) if values else "unknown"))
    lines.append(f"unknowns: {list_text(semantic.get('unknowns')) or 'none documented'}")
    lines.append(f"evidence completeness: {text(semantic.get('evidence_completeness')) or 'unknown'}")
    return "\n".join(lines)


def build_filter_metadata(row: Dict[str, Any], document_hash: str) -> Dict[str, Any]:
    source = row.get("source_stage2") or {}
    task = source.get("task") or {}
    candidate = source.get("candidate") or {}
    language = source.get("language") or {}
    language_stage1 = language.get("stage1") or {}
    model = source.get("model") or {}
    family = source.get("family") or {}
    popularity = source.get("popularity") or {}
    stage1_popularity = popularity.get("stage1") or {}
    semantic = row.get("semantic") or {}
    korean = language.get("korean")
    multilingual = language.get("multilingual")
    document = {
        "primary_task": task.get("primary"),
        "matched_tasks": task.get("matched") or [],
        "candidate_tier": candidate.get("tier"),
        "candidate_type": candidate.get("type"),
        "korean_verified": korean.get("verified") if isinstance(korean, dict) else korean,
        "korean_evidence": korean.get("evidence", []) if isinstance(korean, dict) else [],
        "multilingual_verified": multilingual.get("verified") if isinstance(multilingual, dict) else multilingual,
        "languages": language.get("declared_languages") or language_stage1.get("languages") or [],
        "parameter_count": model.get("parameter_count"),
        "parameter_count_billion": model.get("parameter_count_billion"),
        "context_length": model.get("context_length"),
        "architecture": model.get("architectures") or [],
        "model_type": model.get("type"),
        "quantization": source.get("quantization"),
        "artifacts": source.get("artifacts"),
        "hardware": source.get("hardware"),
        "runtime_compatibility": source.get("runtime_compatibility") or {},
        "license": source.get("license"),
        "canonical_model_id": family.get("canonical_model_id"),
        "is_variant": family.get("is_variant"),
        "variant_types": family.get("variant_types") or [],
        "downloads": stage1_popularity.get("downloads"),
        "popularity_tier": stage1_popularity.get("tier"),
        "semantic_status": row.get("status"),
        "evidence_completeness": semantic.get("evidence_completeness", "unknown") if semantic else "unknown",
        "document_hash": document_hash,
    }


def build_document(row: Dict[str, Any], model: str) -> Dict[str, Any]:
    embedding_text = build_embedding_text(row)
    document_hash = digest(embedding_text)
    source = row.get("source_stage2") or {}
    source_stage = source.get("stage") or {}
    stage3 = row.get("stage3") or {}
    filters = build_filter_metadata(row, document_hash)
    return {
        "model_id": row.get("model_id"),
        "source_pool": row.get("source_pool"),
        "embedding_text": embedding_text,
        "embedding": None,
        "embedding_provider": "openai",
        "embedding_model": model,
        "embedding_dimensions": None,
        "document_hash": document_hash,
        "source_stage1_version": source_stage.get("source_stage1_version"),
        "source_stage2_version": source_stage.get("stage2_version"),
        "source_stage3_version": stage3.get("stage3_version"),
        "candidate": source.get("candidate"),
        "popularity": source.get("popularity"),
        "task": source.get("task"),
        "canonical_model_id": (source.get("family") or {}).get("canonical_model_id"),
        "semantic_status": row.get("status"),
        "evidence_completeness": ((row.get("semantic") or {}).get("evidence_completeness") or "unknown"),
        "filter_metadata": filters,
    }
    return annotate_task_conflict(document)


def select_rows(rows: Sequence[Dict[str, Any]], limit: Optional[int], strategy: str) -> List[Dict[str, Any]]:
    if limit is None or strategy == "first":
        return list(rows if limit is None else rows[:limit])
    buckets: Dict[str, List[Dict[str, Any]]] = {}
    type_rank = {"korean_translation_pair": 0, "korean_name_strong": 1, "korean_explicit": 2}
    for row in rows:
        source = row.get("source_stage2") or {}
        candidate = source.get("candidate") or {}
        task = source.get("task") or {}
        semantic = row.get("semantic") or {}
        family = source.get("family") or {}
        quantization = source.get("quantization") or {}
        key = "|".join((
            "0_no_source" if row.get("status") == "no_source" else "1_completed",
            str(type_rank.get(candidate.get("type"), 9)),
            str(task.get("primary") or "unknown"),
            str(semantic.get("evidence_completeness") or "unknown"),
            "variant" if family.get("is_variant") else "canonical",
            "quantized" if isinstance(quantization, dict) and quantization.get("enabled") else "unquantized",
        ))
        buckets.setdefault(key, []).append(row)
    for bucket in buckets.values():
        bucket.sort(key=lambda item: item.get("model_id") or "")
    ordered = [buckets[key] for key in sorted(buckets)]
    selected: List[Dict[str, Any]] = []
    index = 0
    while len(selected) < limit and ordered:
        next_ordered = []
        for bucket in ordered:
            if index < len(bucket) and len(selected) < limit:
                selected.append(bucket[index])
            if index + 1 < len(bucket):
                next_ordered.append(bucket)
        ordered = next_ordered
        index += 1
    return selected


def validate_source(rows: Sequence[Dict[str, Any]], pool: str) -> None:
    ids = [row.get("model_id") for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError(f"{pool}: duplicate Stage 3 model_id")
    for row in rows:
        if row.get("source_pool") != pool:
            raise ValueError(f"{pool}: source_pool mismatch for {row.get('model_id')}")
        stage3 = row.get("stage3") or {}
        source_stage = (row.get("source_stage2") or {}).get("stage") or {}
        if stage3.get("stage3_version") != EXPECTED_STAGE3_VERSION:
            raise ValueError(f"{pool}: unsupported Stage 3 version for {row.get('model_id')}")
        if source_stage.get("source_stage1_version") != EXPECTED_STAGE1_VERSION or source_stage.get("stage2_version") != EXPECTED_STAGE2_VERSION:
            raise ValueError(f"{pool}: Stage 1/2 version mismatch for {row.get('model_id')}")


def validate_documents(rows: Sequence[Dict[str, Any]], pool: str) -> Dict[str, Any]:
    ids = [row.get("model_id") for row in rows]
    bad = [row.get("model_id") for row in rows if row.get("source_pool") != pool or not row.get("embedding_text") or row.get("document_hash") != digest(row["embedding_text"])]
    return {"pool": pool, "rows": len(rows), "duplicates": len(ids) - len(set(ids)), "bad_count": len(bad), "bad_examples": bad[:20]}


def validate_stage3_pool_disjointness(pools: Sequence[str]) -> None:
    """Reject stale Stage 3 rows shared by multiple source pools."""
    owners: Dict[str, str] = {}
    duplicates: List[str] = []
    for pool in pools:
        path = DATA_DIR / f"hf_models_stage3_{pool}.jsonl"
        for row in read_jsonl(path):
            model_id = row.get("model_id")
            if not model_id:
                continue
            previous_pool = owners.get(model_id)
            if previous_pool is not None:
                duplicates.append(f"{model_id} ({previous_pool}, {pool})")
            else:
                owners[model_id] = pool
    if duplicates:
        examples = ", ".join(duplicates[:20])
        raise ValueError(
            "Stage 3 pools contain duplicate model_id values; "
            f"reconcile Stage 3 snapshots before embedding: {examples}"
        )


def validate_embedded_output(documents: Sequence[Dict[str, Any]], source_rows: Sequence[Dict[str, Any]], pool: str) -> Dict[str, Any]:
    source_ids = [row.get("model_id") for row in source_rows]
    output_ids = [row.get("model_id") for row in documents]
    dimensions = {len(row.get("embedding") or []) for row in documents}
    bad = []
    if set(source_ids) != set(output_ids):
        bad.append("id_set_mismatch")
    if len(output_ids) != len(set(output_ids)):
        bad.append("duplicate_ids")
    if len(dimensions) != 1 or 0 in dimensions:
        bad.append("vector_dimension_mismatch")
    for row in documents:
        vector = row.get("embedding") or []
        if not vector or any(not math.isfinite(float(value)) for value in vector):
            bad.append(f"invalid_vector:{row.get('model_id')}")
        if row.get("source_pool") != pool or row.get("source_stage1_version") != EXPECTED_STAGE1_VERSION or row.get("source_stage2_version") != EXPECTED_STAGE2_VERSION or row.get("source_stage3_version") != EXPECTED_STAGE3_VERSION:
            bad.append(f"lineage:{row.get('model_id')}")
    return {"pool": pool, "rows": len(documents), "dimensions": sorted(dimensions), "bad_count": len(bad), "bad_examples": bad[:20]}


def embed_documents(documents: List[Dict[str, Any]], model: str, batch_size: int, checkpoint: Optional[Path] = None) -> None:
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required with --execute")
    client = OpenAI(api_key=api_key)
    for start in range(0, len(documents), batch_size):
        batch = documents[start : start + batch_size]
        response = client.embeddings.create(model=model, input=[row["embedding_text"] for row in batch])
        items = sorted(response.data, key=lambda item: item.index)
        if len(items) != len(batch):
            raise RuntimeError(f"embedding count mismatch: {len(batch)} requested, {len(items)} returned")
        dimensions = len(items[0].embedding) if items else 0
        for row, item in zip(batch, items):
            vector = item.embedding
            if not vector or any(not math.isfinite(float(value)) for value in vector):
                raise RuntimeError(f"invalid embedding for {row['model_id']}")
            row["embedding"] = vector
            row["embedding_dimensions"] = dimensions
        if checkpoint is not None:
            write_jsonl_atomic(documents, checkpoint)
        print(f"embedded {min(start + len(batch), len(documents))}/{len(documents)}", flush=True)


def reusable(existing: Dict[str, Any], document: Dict[str, Any], model: str) -> bool:
    vector = existing.get("embedding")
    return bool(
        existing.get("document_hash") == document.get("document_hash")
        and existing.get("embedding_model") == model
        and isinstance(vector, list)
        and vector
    )



def _parse_db_vector(value: Any) -> List[float]:
    """Parse PostgreSQL pgvector text without requiring the pgvector package."""
    if isinstance(value, str):
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            value = value[1:-1]
            return [float(item) for item in value.split(",") if item.strip()]
    if isinstance(value, (list, tuple)):
        return [float(item) for item in value]
    return []


def load_db_embedding_cache(model_ids: Sequence[str]) -> Dict[str, Dict[str, Any]]:
    """Load reusable vectors from Supabase for a DB-canonical Stage 4 run.

    This is opt-in so ordinary local Stage 4 runs remain network-free apart from
    the embedding provider. The returned shape matches the local Stage 4 cache.
    """
    ids = sorted({str(model_id) for model_id in model_ids if model_id})
    if not ids:
        return {}
    required = (
        "SUPABASE_DB_HOST",
        "SUPABASE_DB_PORT",
        "SUPABASE_DB_NAME",
        "SUPABASE_DB_USER",
        "SUPABASE_PASSWORD",
    )
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise RuntimeError(
            "--db-cache requires Supabase database settings: " + ", ".join(missing)
        )
    try:
        import psycopg2
    except ImportError as exc:
        raise RuntimeError("--db-cache requires psycopg2-binary") from exc

    connection = psycopg2.connect(
        host=os.environ["SUPABASE_DB_HOST"],
        port=int(os.environ["SUPABASE_DB_PORT"]),
        dbname=os.environ["SUPABASE_DB_NAME"],
        user=os.environ["SUPABASE_DB_USER"],
        password=os.environ["SUPABASE_PASSWORD"],
        connect_timeout=15,
    )
    cache: Dict[str, Dict[str, Any]] = {}
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT model_id, document_hash, embedding_model,
                       embedding_dimensions, embedding::text
                FROM public.model_scout_models
                WHERE active = true AND model_id = ANY(%s)
                """,
                (ids,),
            )
            for model_id, document_hash, embedding_model, dimensions, vector_text in cursor.fetchall():
                vector = _parse_db_vector(vector_text)
                if len(vector) != int(dimensions or 0):
                    continue
                cache[model_id] = {
                    "model_id": model_id,
                    "document_hash": document_hash,
                    "embedding_model": embedding_model,
                    "embedding_dimensions": int(dimensions),
                    "embedding": vector,
                }
    finally:
        connection.close()
    return cache

def run_pool(
    pool: str,
    model: str,
    limit: Optional[int],
    execute: bool,
    batch_size: int,
    sample_strategy: str,
    db_cache: bool = False,
) -> Dict[str, Any]:
    source_rows = read_jsonl(DATA_DIR / f"hf_models_stage3_{pool}.jsonl")
    validate_source(source_rows, pool)
    selected = select_rows(source_rows, limit, sample_strategy)
    documents = [build_document(row, model) for row in selected]
    report = validate_documents(documents, pool)
    if report["duplicates"] or report["bad_count"]:
        raise ValueError(f"{pool}: invalid Stage 4 documents: {report}")

    reused = 0
    db_reused = 0
    output: Optional[Path] = None
    if execute:
        canonical_output = DATA_DIR / f"hf_models_stage4_{pool}.jsonl"
        checkpoint_path = (
            DATA_DIR if limit is None else ROOT / "test"
        ) / f".stage4_{pool}_checkpoint.jsonl"
        existing: Dict[str, Dict[str, Any]] = {}
        if limit is None and canonical_output.exists():
            existing = {
                item.get("model_id"): item
                for item in read_jsonl(canonical_output)
                if item.get("model_id")
            }
        elif checkpoint_path.exists():
            existing = {
                item.get("model_id"): item
                for item in read_jsonl(checkpoint_path)
                if item.get("model_id")
            }

        if db_cache:
            # Supabase is authoritative once this mode is enabled. This matters
            # when the tracked baseline is intentionally no longer committed:
            # a model changed after the baseline must reuse the vector already
            # written to DB on the previous successful run.
            db_existing = load_db_embedding_cache(
                [document.get("model_id") for document in documents]
            )
            # If the local vector snapshot is absent, refuse to silently turn a
            # partial DB migration into a full paid re-embedding run. A small
            # number of missing IDs is expected for genuinely new models.
            if not existing and documents:
                coverage = len(db_existing) / len(documents)
                if not db_existing or coverage < 0.90:
                    raise RuntimeError(
                        "Supabase embedding cache coverage is too low for DB-canonical "
                        f"Stage 4 ({len(db_existing)}/{len(documents)}); refusing a full re-embedding run"
                    )
            existing.update(db_existing)
            db_reused = len(db_existing)

        pending: List[Dict[str, Any]] = []
        for document in documents:
            old = existing.get(document.get("model_id"))
            if old and reusable(old, document, model):
                document["embedding"] = old["embedding"]
                document["embedding_dimensions"] = old.get("embedding_dimensions")
                reused += 1
            else:
                pending.append(document)
        if pending:
            try:
                embed_documents(pending, model, batch_size, checkpoint_path)
            except Exception as exc:
                error_path = DATA_DIR / f"hf_models_stage4_{pool}_errors.jsonl"
                errors = [
                    {
                        "model_id": item.get("model_id"),
                        "source_pool": pool,
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                        "stage4_version": STAGE4_VERSION,
                    }
                    for item in pending
                ]
                write_jsonl_atomic(errors, error_path)
                raise
        output = canonical_output if limit is None else ROOT / "test" / f"stage4_{pool}_pilot.jsonl"
        write_jsonl_atomic(documents, output)
        final_report = validate_embedded_output(documents, selected, pool)
        if final_report["bad_count"]:
            raise ValueError(f"{pool}: Stage 4 output validation failed: {final_report}")
        print(json.dumps({"pool": pool, "output_validation": final_report}, ensure_ascii=False), flush=True)
        if checkpoint_path.exists():
            checkpoint_path.unlink()

    summary = {
        "pool": pool,
        "rows": len(documents),
        "execute": execute,
        "reused": reused,
        "db_reused": db_reused,
        "embedded": len(documents) - reused,
        "output": str(output) if output else None,
    }
    print(json.dumps(summary, ensure_ascii=False), flush=True)
    return summary

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool", choices=("core", "low_popularity", "all"), default="all")
    parser.add_argument("--model", default=None)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--sample-strategy", choices=("stratified", "first"), default="stratified")
    parser.add_argument("--execute", action="store_true", help="call the embedding API; default is a network-free dry run")
    parser.add_argument(
        "--db-cache",
        action="store_true",
        help="reuse matching embeddings from Supabase before calling the embedding API",
    )
    args = parser.parse_args()
    if args.limit is not None and args.limit <= 0:
        parser.error("--limit must be positive")
    if args.batch_size <= 0:
        parser.error("--batch-size must be positive")
    if args.db_cache and not args.execute:
        parser.error("--db-cache requires --execute")

    load_dotenv(ROOT / ".env")
    model = args.model or os.getenv("STAGE4_EMBEDDING_MODEL") or DEFAULT_MODEL
    pools = POOLS if args.pool == "all" else (args.pool,)
    if args.pool == "all":
        validate_stage3_pool_disjointness(pools)
    summaries = [
        run_pool(
            pool,
            model,
            args.limit,
            args.execute,
            args.batch_size,
            args.sample_strategy,
            db_cache=args.db_cache,
        )
        for pool in pools
    ]
    print(json.dumps({"stage4_version": STAGE4_VERSION, "model": model, "summaries": summaries}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


if __name__ == "__main__":
    raise SystemExit(main())
