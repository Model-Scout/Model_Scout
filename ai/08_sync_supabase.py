#!/usr/bin/env python3
"""Load the final Core/Low recommendation corpus into Supabase.

The default mode is offline validation. ``--initial --apply`` is a one-time
snapshot load. After initialization, ``--refresh --apply`` uses the previous
Supabase watermark to scan only Hugging Face models whose ``last_modified``
changed, runs Stage 2-4 resume processing only for eligible changed models,
and upserts only those rows. It never performs a full refresh.

The script intentionally excludes Likely, Fallback, raw README files, pilot
outputs, and validation reports. Full README text is not duplicated in the
database; Stage 3 evidence spans and provenance are retained instead.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple
from urllib.parse import quote

from dotenv import load_dotenv
from retrieval_metadata import augment_filter_metadata

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
SCHEMA_PATH = ROOT / "supabase_schema.sql"
POOLS = ("core", "low_popularity")
MODEL_IDS_PATH = DATA_DIR / ".incremental_model_ids.json"
BENCHMARK_CHANGED_IDS_PATH = DATA_DIR / ".benchmark_changed_model_ids.json"
BENCHMARK_STATE_PATH = DATA_DIR / "hf_models_benchmark_state.json"
BENCHMARK_STATE_CANDIDATE_PATH = DATA_DIR / ".hf_models_benchmark_state_candidate.json"
# stage2 7: 데이터 계약 필드(ai/contract/)가 들어온 버전.
EXPECTED_VERSIONS = {"stage1": 7, "stage2": 7, "stage3": 1, "stage4": 1}
DEFAULT_TTL_HOURS = 24
DEFAULT_BATCH_SIZE = 100
API_MAX_RETRIES = 3
API_RETRY_BASE_SECONDS = 2


def model_page_url(model_id: str) -> str:
    return f"https://huggingface.co/{quote(str(model_id), safe='/')}"


def model_readme_url(model_id: str) -> str:
    return f"{model_page_url(model_id)}/blob/main/README.md"


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(path)
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def stage4_delta_path(pool: str) -> Path:
    return DATA_DIR / f".stage4_delta_{pool}.jsonl"


def benchmark_delta_path(pool: str) -> Path:
    return DATA_DIR / f".hf_models_benchmark_delta_{pool}.jsonl"


def write_model_ids(model_ids: Sequence[str]) -> None:
    MODEL_IDS_PATH.write_text(
        json.dumps(sorted(set(model_ids)), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def read_model_ids(path: Path) -> Set[str]:
    if not path.exists():
        return set()
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list):
        raise ValueError(f"{path}: expected a JSON list of model IDs")
    return {item for item in value if isinstance(item, str) and item}


def clear_incremental_artifacts() -> None:
    for pool in POOLS:
        for path in (
            stage4_delta_path(pool),
            benchmark_delta_path(pool),
            DATA_DIR / f".hf_models_benchmark_changed_ids_{pool}.json",
        ):
            if path.exists():
                path.unlink()
    for path in (
        MODEL_IDS_PATH,
        BENCHMARK_CHANGED_IDS_PATH,
        BENCHMARK_STATE_CANDIDATE_PATH,
    ):
        if path.exists():
            path.unlink()


def promote_benchmark_state() -> None:
    if BENCHMARK_STATE_CANDIDATE_PATH.exists():
        BENCHMARK_STATE_CANDIDATE_PATH.replace(BENCHMARK_STATE_PATH)


def json_text(value: Any) -> str:
    return json.dumps(value if value is not None else {}, ensure_ascii=False, separators=(",", ":"))


def vector_literal(values: Sequence[float]) -> str:
    return "[" + ",".join(format(float(value), ".9g") for value in values) + "]"


def load_corpora(
    stage4_delta: bool = False,
) -> Tuple[List[Dict[str, Any]], Dict[str, Dict[str, Any]], Dict[str, Dict[str, Any]]]:
    stage4: List[Dict[str, Any]] = []
    stage2: Dict[str, Dict[str, Any]] = {}
    stage3: Dict[str, Dict[str, Any]] = {}
    for pool in POOLS:
        stage4_path = stage4_delta_path(pool) if stage4_delta else DATA_DIR / f"hf_models_stage4_{pool}.jsonl"
        if stage4_path.exists():
            stage4.extend(read_jsonl(stage4_path))
        for row in read_jsonl(DATA_DIR / f"hf_models_stage2_{pool}.jsonl"):
            stage2[row["model_id"]] = row
        # 계약 레코드는 Stage 2가 별도 파일에 쓴다(한 건 약 9KB). 여기서 다시
        # 붙여 technical_metadata와 source_provenance로 보낸다. 파일이 없으면
        # 계약 필드 없이 돈다 — 구 데이터로 적재를 다시 할 때 멈추지 않게 한다.
        for record in read_jsonl(DATA_DIR / f"hf_models_stage2_contract_{pool}.jsonl"):
            row = stage2.get(record.get("model_id"))
            if row is not None:
                row["contract"] = record
        for row in read_jsonl(DATA_DIR / f"hf_models_stage3_{pool}.jsonl"):
            stage3[row["model_id"]] = row
    return stage4, stage2, stage3


def apply_benchmark_deltas(stage4: Sequence[Dict[str, Any]]) -> None:
    """Attach only changed benchmark projections to the Stage 4 delta rows."""
    sidecars: Dict[str, Dict[str, Any]] = {}
    for pool in POOLS:
        path = benchmark_delta_path(pool)
        if path.exists():
            for row in read_jsonl(path):
                model_id = row.get("model_id")
                if model_id:
                    sidecars[model_id] = row
    for row in stage4:
        model_id = row.get("model_id")
        if model_id in sidecars:
            metadata = dict(sidecars[model_id])
            metadata.pop("model_id", None)
            metadata.pop("source_pool", None)
            row["benchmark_metadata"] = metadata


def stage3_pools_need_reconciliation() -> bool:
    """Return whether persisted Stage 3 pools overlap by model ID."""
    owners: Dict[str, str] = {}
    for pool in POOLS:
        path = DATA_DIR / f"hf_models_stage3_{pool}.jsonl"
        if not path.exists():
            continue
        for row in read_jsonl(path):
            model_id = row.get("model_id")
            if not model_id:
                continue
            previous_pool = owners.get(model_id)
            if previous_pool is not None:
                return True
            owners[model_id] = pool
    return False


def load_evidence_indices() -> Dict[str, Dict[str, Any]]:
    """Load the deterministic Stage 3 Parent-Child sidecars by model ID."""
    indices: Dict[str, Dict[str, Any]] = {}
    for pool in POOLS:
        path = DATA_DIR / f"hf_models_stage3_parent_child_{pool}.jsonl"
        for row in read_jsonl(path):
            model_id = row.get("model_id")
            if not model_id:
                raise ValueError(f"Parent-Child sidecar row has no model_id: {path}")
            if model_id in indices:
                raise ValueError(f"Duplicate Parent-Child sidecar model_id: {model_id}")
            indices[model_id] = row
    return indices


def validate_evidence_indices(
    stage4: Sequence[Dict[str, Any]],
    evidence: Dict[str, Dict[str, Any]],
    expected_model_ids: Optional[Sequence[str]] = None,
) -> Dict[str, Any]:
    """Validate sidecar referential integrity before a DB write."""
    expected = set(expected_model_ids) if expected_model_ids is not None else {
        row["model_id"] for row in stage4
    }
    actual = set(evidence)
    missing = sorted(expected - actual)
    extra = [] if expected_model_ids is not None else sorted(actual - expected)
    problems: List[str] = [f"missing sidecar: {mid}" for mid in missing[:10]]
    problems.extend(f"extra sidecar: {mid}" for mid in extra[:10])
    parent_count = 0
    child_count = 0
    for model_id, row in evidence.items():
        if row.get("source_pool") not in POOLS:
            problems.append(f"{model_id}: invalid sidecar source_pool")
        if row.get("source_stage3_version") != EXPECTED_VERSIONS["stage3"]:
            problems.append(f"{model_id}: sidecar Stage 3 version mismatch")
        parents = row.get("parents") or []
        if not isinstance(parents, list):
            problems.append(f"{model_id}: parents is not a list")
            continue
        seen_parents = set()
        seen_children = set()
        for parent in parents:
            parent_id = parent.get("parent_id") if isinstance(parent, dict) else None
            if not parent_id or parent_id in seen_parents:
                problems.append(f"{model_id}: invalid or duplicate parent_id")
                continue
            seen_parents.add(parent_id)
            children = parent.get("children") or []
            child_ids = parent.get("child_ids") or []
            actual_child_ids = [
                child.get("child_id") for child in children
                if isinstance(child, dict) and child.get("child_id")
            ]
            if sorted(child_ids) != sorted(actual_child_ids):
                problems.append(f"{model_id}: parent child_ids mismatch")
            for child in children:
                child_id = child.get("child_id") if isinstance(child, dict) else None
                if not child_id or child_id in seen_children:
                    problems.append(f"{model_id}: invalid or duplicate child_id")
                    continue
                if child.get("parent_id") != parent_id:
                    problems.append(f"{model_id}: child parent_id mismatch")
                seen_children.add(child_id)
        if row.get("parent_count") != len(seen_parents):
            problems.append(f"{model_id}: parent_count mismatch")
        if row.get("child_count") != len(seen_children):
            problems.append(f"{model_id}: child_count mismatch")
        parent_count += len(seen_parents)
        child_count += len(seen_children)
    if problems:
        raise ValueError("Parent-Child sidecar validation failed: " + "; ".join(problems[:30]))
    return {"rows": len(evidence), "parent_count": parent_count, "child_count": child_count}


def validate_corpus(
    stage4: Sequence[Dict[str, Any]],
    stage2: Dict[str, Dict[str, Any]],
    stage3: Dict[str, Dict[str, Any]],
    incremental_ids: Optional[Sequence[str]] = None,
) -> Dict[str, Any]:
    problems: List[str] = []
    ids = [row.get("model_id") for row in stage4]
    if len(ids) != len(set(ids)):
        problems.append("duplicate Stage 4 model_id")
    stage2_ids = set(stage2)
    stage3_ids = set(stage3)
    stage4_ids = set(ids)
    missing_stage3 = sorted(stage2_ids - stage3_ids)
    missing_stage4 = (
        sorted(set(incremental_ids or ()) - stage4_ids)
        if incremental_ids is not None
        else sorted(stage2_ids - stage4_ids)
    )
    extra_incremental = (
        sorted(stage4_ids - set(incremental_ids or ()))
        if incremental_ids is not None
        else []
    )
    extra_stage3 = sorted(stage3_ids - stage2_ids)
    extra_stage4 = sorted(stage4_ids - stage2_ids)
    if missing_stage3:
        problems.append("missing Stage 3 rows: " + ", ".join(missing_stage3[:30]))
    if missing_stage4:
        problems.append("missing Stage 4 rows: " + ", ".join(missing_stage4[:30]))
    if extra_incremental:
        problems.append("unexpected incremental Stage 4 rows: " + ", ".join(extra_incremental[:30]))
    if extra_stage3:
        problems.append("stale Stage 3 rows: " + ", ".join(extra_stage3[:30]))
    if extra_stage4:
        problems.append("stale Stage 4 rows: " + ", ".join(extra_stage4[:30]))
    pool_counts = {pool: 0 for pool in POOLS}
    for row in stage4:
        model_id = row.get("model_id")
        pool = row.get("source_pool")
        if pool not in POOLS:
            problems.append(f"{model_id}: invalid source_pool={pool!r}")
            continue
        pool_counts[pool] += 1
        if row.get("source_stage1_version") != EXPECTED_VERSIONS["stage1"]:
            problems.append(f"{model_id}: Stage 1 version mismatch")
        if row.get("source_stage2_version") != EXPECTED_VERSIONS["stage2"]:
            problems.append(f"{model_id}: Stage 2 version mismatch")
        if row.get("source_stage3_version") != EXPECTED_VERSIONS["stage3"]:
            problems.append(f"{model_id}: Stage 3 version mismatch")
        if row.get("embedding_dimensions") != 1536:
            problems.append(f"{model_id}: embedding dimension is not 1536")
        embedding = row.get("embedding")
        if not isinstance(embedding, list) or len(embedding) != 1536:
            problems.append(f"{model_id}: invalid embedding")
        candidate = row.get("candidate") or {}
        if candidate.get("tier") != "A_verified":
            problems.append(f"{model_id}: non-A candidate in DB corpus")
        if model_id not in stage2:
            problems.append(f"{model_id}: missing Stage 2 detail")
        if model_id not in stage3:
            problems.append(f"{model_id}: missing Stage 3 detail")
    if incremental_ids is not None:
        pool_counts = {pool: 0 for pool in POOLS}
        for row in stage3.values():
            pool = row.get("source_pool")
            if pool in pool_counts:
                pool_counts[pool] += 1
    if problems:
        raise ValueError("Supabase corpus validation failed:\n" + "\n".join(problems[:30]))
    return {"rows": len(stage4), "pool_counts": pool_counts, "stage2_rows": len(stage2), "stage3_rows": len(stage3)}



def write_stage4_manifest(
    stage4: Sequence[Dict[str, Any]],
    validation: Dict[str, Any],
    corpus_rows: Optional[int] = None,
) -> Path:
    """Persist a small tracked snapshot description without embedding arrays."""
    dimensions = sorted({int(row.get("embedding_dimensions") or 0) for row in stage4})
    models = sorted({str(row.get("embedding_model") or "") for row in stage4 if row.get("embedding_model")})
    previous_manifest_path = DATA_DIR / "hf_models_stage4_manifest.json"
    if (not dimensions or not models) and previous_manifest_path.exists():
        previous = json.loads(previous_manifest_path.read_text(encoding="utf-8"))
        dimensions = dimensions or previous.get("embedding_dimensions", [])
        models = models or previous.get("embedding_models", [])
    manifest = {
        "stage4_version": EXPECTED_VERSIONS["stage4"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "rows": len(stage4) if corpus_rows is None else corpus_rows,
        "pool_counts": validation.get("pool_counts", {}),
        "embedding_dimensions": dimensions,
        "embedding_models": models,
        "source_stage_versions": EXPECTED_VERSIONS,
        "vector_storage": "supabase_pgvector",
    }
    path = DATA_DIR / "hf_models_stage4_manifest.json"
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path

def provenance(
    model_id: str,
    stage2: Dict[str, Any],
    stage3: Dict[str, Any],
) -> Dict[str, Any]:
    source = stage2.get("source") or {}
    readme = source.get("readme") or {}
    return {
        "hub": source.get("hub") or {},
        "config": source.get("config") or {},
        "tokenizer_config": source.get("tokenizer_config") or {},
        "model_card": source.get("model_card") or {},
        "model_url": model_page_url(model_id),
        "readme_url": model_readme_url(model_id),
        "readme": {
            key: readme.get(key)
            for key in (
                "available",
                "path",
                "original_chars",
                "saved_chars",
                "truncated",
                "error",
            )
        }
        | {
            "source_url": readme.get("source_url") or model_page_url(model_id),
            "readme_url": readme.get("readme_url") or model_readme_url(model_id),
        },
        "stage2": stage2.get("stage") or {},
        "stage3": stage3.get("stage3") or {},
        "validation": stage3.get("validation") or {},
        # 데이터 계약의 출처 기록. 필드마다 "어떻게 알게 됐는지"가 여기 있다.
        # conflicts와 review_queue가 사람이 봐야 하는 목록이다.
        "contract": (stage2.get("contract") or {}).get("provenance") or {},
    }


def payloads(
    stage4: Sequence[Dict[str, Any]],
    stage2: Dict[str, Dict[str, Any]],
    stage3: Dict[str, Dict[str, Any]],
    run_id: str,
) -> List[Tuple[Any, ...]]:
    rows: List[Tuple[Any, ...]] = []
    now = datetime.now(timezone.utc)
    for row in stage4:
        model_id = row["model_id"]
        source2 = stage2[model_id]
        source3 = stage3[model_id]
        contract = source2.get("contract") or {}
        technical = {
            "model": source2.get("model") or {},
            "quantization": source2.get("quantization") or {},
            "artifacts": source2.get("artifacts") or {},
            "hardware": source2.get("hardware") or {},
            "runtime_compatibility": source2.get("runtime_compatibility") or {},
            "license": source2.get("license"),
            "base_models": source2.get("base_models") or [],
            "datasets": source2.get("datasets") or [],
            "metrics": source2.get("metrics") or [],
            # 계약의 상세. filter_metadata에는 필터용 스칼라만 올라가므로
            # 포맷별 용량·양자화 목록·배포 대상 등급·라이선스 원문 위치는 여기 있다.
            "contract": {
                key: contract.get(key)
                for key in ("identity", "legal", "artifacts", "deployment", "technical")
                if contract.get(key) is not None
            },
        }
        rows.append(
            (
                model_id,
                row["source_pool"],
                row["source_stage1_version"],
                row["source_stage2_version"],
                row["source_stage3_version"],
                EXPECTED_VERSIONS["stage4"],
                json_text(row.get("candidate")),
                json_text(row.get("task")),
                json_text(source2.get("language")),
                json_text(source2.get("popularity")),
                json_text(source2.get("family")),
                json_text(row.get("filter_metadata")),
                json_text(technical),
                json_text(source3.get("semantic")),
                json_text(source3.get("evidence")),
                json_text(row.get("benchmark_metadata")),
                json_text(provenance(model_id, source2, source3)),
                json_text(row.get("task_consistency")),
                row.get("document_hash"),
                row.get("embedding_model") or "text-embedding-3-small",
                row.get("embedding_dimensions") or 1536,
                vector_literal(row["embedding"]),
                run_id,
                now,
            )
        )
    return rows


def evidence_payloads(
    stage4: Sequence[Dict[str, Any]],
    evidence: Dict[str, Dict[str, Any]],
    run_id: str,
) -> List[Tuple[Any, ...]]:
    """Build one JSONB Parent-Child sidecar payload per selected model."""
    now = datetime.now(timezone.utc)
    rows: List[Tuple[Any, ...]] = []
    for model in stage4:
        model_id = model["model_id"]
        sidecar = evidence[model_id]
        rows.append((
            model_id,
            model["source_pool"],
            sidecar.get("source_stage3_version") or EXPECTED_VERSIONS["stage3"],
            sidecar.get("schema_version") or 1,
            sidecar.get("evidence_index_version") or 1,
            sidecar.get("source_stage3_hash") or "",
            int(sidecar.get("parent_count") or 0),
            int(sidecar.get("child_count") or 0),
            json_text(sidecar.get("parents") or []),
            run_id,
            now,
        ))
    return rows


def db_connection():
    import psycopg2

    required = ("SUPABASE_DB_HOST", "SUPABASE_DB_PORT", "SUPABASE_DB_NAME", "SUPABASE_DB_USER", "SUPABASE_PASSWORD")
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise RuntimeError("Missing Supabase environment variables: " + ", ".join(missing))
    return psycopg2.connect(
        host=os.environ["SUPABASE_DB_HOST"],
        port=int(os.environ["SUPABASE_DB_PORT"]),
        dbname=os.environ["SUPABASE_DB_NAME"],
        user=os.environ["SUPABASE_DB_USER"],
        password=os.environ["SUPABASE_PASSWORD"],
        sslmode="require",
        connect_timeout=15,
    )


def backfill_runtime_metadata() -> Dict[str, int]:
    """Patch only the runtime metadata keys in existing DB rows.

    This is a metadata migration, not a Stage 1-4 refresh: embeddings,
    semantic metadata, and model rows are otherwise left untouched.
    """
    stage2_rows: List[Dict[str, Any]] = []
    for pool in POOLS:
        stage2_rows.extend(read_jsonl(DATA_DIR / f"hf_models_stage2_{pool}.jsonl"))

    conn = db_connection()
    updated = 0
    missing = 0
    try:
        with conn:
            with conn.cursor() as cur:
                for row in stage2_rows:
                    model_id = row.get("model_id")
                    runtime = row.get("runtime_compatibility") or {}
                    cur.execute(
                        """
                        update public.model_scout_models
                        set filter_metadata = coalesce(filter_metadata, '{}'::jsonb)
                            || %s::jsonb,
                            technical_metadata = coalesce(technical_metadata, '{}'::jsonb)
                            || %s::jsonb,
                            refreshed_at = now()
                        where model_id = %s
                          and (
                              not (coalesce(filter_metadata, '{}'::jsonb)
                                   ? 'runtime_compatibility')
                              or not (coalesce(technical_metadata, '{}'::jsonb)
                                      ? 'runtime_compatibility')
                              or coalesce(
                                  technical_metadata->'runtime_compatibility'->>'version',
                                  ''
                              ) <> %s
                          )
                        """,
                        (
                            json_text({"runtime_compatibility": runtime}),
                            json_text({"runtime_compatibility": runtime}),
                            model_id,
                            str(runtime.get("version", "1")),
                        ),
                    )
                    updated += cur.rowcount
                    if cur.rowcount == 0:
                        cur.execute(
                            "select 1 from public.model_scout_models where model_id = %s",
                            (model_id,),
                        )
                        if cur.fetchone() is None:
                            missing += 1
    finally:
        conn.close()
    return {"source_rows": len(stage2_rows), "updated": updated, "missing_db_rows": missing}


def backfill_search_metadata_db() -> Dict[str, int]:
    """Patch deterministic language-pair/search aliases in existing DB rows."""
    stage4_rows: List[Dict[str, Any]] = []
    for pool in POOLS:
        stage4_rows.extend(read_jsonl(DATA_DIR / f"hf_models_stage4_{pool}.jsonl"))
    conn = db_connection()
    updated = 0
    missing = 0
    try:
        with conn.cursor() as cur:
            for row in stage4_rows:
                model_id = row.get("model_id")
                if not model_id:
                    continue
                metadata = augment_filter_metadata(
                    str(model_id),
                    row.get("filter_metadata") or {},
                    row.get("task") or {},
                )
                patch = {
                    key: metadata.get(key)
                    for key in ("search_metadata_version", "language_codes", "translation_pairs", "search_aliases")
                }
                cur.execute(
                    """
                    update public.model_scout_models
                    set filter_metadata = coalesce(filter_metadata, '{}'::jsonb) || %s::jsonb,
                        updated_at = now()
                    where model_id = %s
                    """,
                    (json_text(patch), model_id),
                )
                if cur.rowcount:
                    updated += cur.rowcount
                else:
                    missing += 1
        conn.commit()
    finally:
        conn.close()
    return {"source_rows": len(stage4_rows), "updated": updated, "missing_db_rows": missing}


def apply_sync(
    rows: Sequence[Tuple[Any, ...]],
    evidence_rows: Sequence[Tuple[Any, ...]],
    run_id: str,
    batch_size: int,
    *,
    incremental: bool = False,
    removed_ids: Sequence[str] = (),
    source_watermark: Optional[str] = None,
    corpus_rows: Optional[int] = None,
) -> Dict[str, Any]:
    import psycopg2.extras

    stage_versions = dict(EXPECTED_VERSIONS)
    stage_versions["sync_mode"] = "incremental" if incremental else "initial"
    if source_watermark:
        stage_versions["source_watermark"] = source_watermark
    if corpus_rows is not None:
        stage_versions["corpus_rows"] = corpus_rows

    statement = """
        insert into public.model_scout_models (
            model_id, source_pool, source_stage1_version, source_stage2_version,
            source_stage3_version, source_stage4_version, candidate, task, language,
            popularity, family, filter_metadata, technical_metadata, semantic_metadata,
            evidence, benchmark_metadata, source_provenance, task_consistency,
            document_hash, embedding_model, embedding_dimensions, embedding,
            last_seen_run, refreshed_at
        ) values %s
        on conflict (model_id) do update set
            source_pool = excluded.source_pool,
            source_stage1_version = excluded.source_stage1_version,
            source_stage2_version = excluded.source_stage2_version,
            source_stage3_version = excluded.source_stage3_version,
            source_stage4_version = excluded.source_stage4_version,
            candidate = excluded.candidate,
            task = excluded.task,
            language = excluded.language,
            popularity = excluded.popularity,
            family = excluded.family,
            filter_metadata = excluded.filter_metadata,
            technical_metadata = excluded.technical_metadata,
            semantic_metadata = excluded.semantic_metadata,
            evidence = excluded.evidence,
            benchmark_metadata = excluded.benchmark_metadata,
            source_provenance = excluded.source_provenance,
            task_consistency = excluded.task_consistency,
            document_hash = excluded.document_hash,
            embedding_model = excluded.embedding_model,
            embedding_dimensions = excluded.embedding_dimensions,
            embedding = excluded.embedding,
            last_seen_run = excluded.last_seen_run,
            active = true,
            stale_at = null,
            refreshed_at = excluded.refreshed_at,
            updated_at = now()
    """
    template = "(" + ", ".join(
        ["%s"] * 6
        + ["%s::jsonb"] * 12
        + ["%s"] * 3
        + ["%s::vector", "%s", "%s"]
    ) + ")"

    conn = db_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                verify_vector_extension(cur)
                cur.execute(
                    """
                    insert into public.model_scout_sync_runs
                        (run_id, status, stage_versions, row_count)
                    values (%s, 'running', %s::jsonb, %s)
                    """,
                    (run_id, json_text(stage_versions), len(rows)),
                )
                if rows:
                    psycopg2.extras.execute_values(
                        cur,
                        statement,
                        rows,
                        template=template,
                        page_size=batch_size,
                    )

                evidence_statement = """
                    insert into public.model_scout_evidence (
                        model_id, source_pool, source_stage3_version, schema_version,
                        evidence_index_version, source_stage3_hash, parent_count, child_count,
                        parents, last_seen_run, refreshed_at
                    ) values %s
                    on conflict (model_id) do update set
                        source_pool = excluded.source_pool,
                        source_stage3_version = excluded.source_stage3_version,
                        schema_version = excluded.schema_version,
                        evidence_index_version = excluded.evidence_index_version,
                        source_stage3_hash = excluded.source_stage3_hash,
                        parent_count = excluded.parent_count,
                        child_count = excluded.child_count,
                        parents = excluded.parents,
                        last_seen_run = excluded.last_seen_run,
                        active = true,
                        refreshed_at = excluded.refreshed_at,
                        updated_at = now()
                """
                evidence_template = "(" + ", ".join(
                    ["%s"] * 8 + ["%s::jsonb", "%s", "%s"]
                ) + ")"
                psycopg2.extras.execute_values(
                    cur, evidence_statement, evidence_rows,
                    template=evidence_template, page_size=batch_size,
                )
                if incremental:
                    if removed_ids:
                        cur.execute(
                            """
                            update public.model_scout_models
                            set active = false, stale_at = now(), updated_at = now()
                            where model_id = any(%s)
                              and active = true
                            """,
                            (list(removed_ids),),
                        )
                        deactivated = cur.rowcount
                        cur.execute(
                            """
                            update public.model_scout_evidence
                               set active = false, updated_at = now()
                             where model_id = any(%s) and active = true
                            """,
                            (list(removed_ids),),
                        )
                    else:
                        deactivated = 0
                else:
                    cur.execute(
                        """
                        update public.model_scout_models
                        set active = false, stale_at = now(), updated_at = now()
                        where source_pool in ('core', 'low_popularity')
                          and active = true
                          and last_seen_run is distinct from %s::uuid
                        """,
                        (run_id,),
                    )
                    deactivated = cur.rowcount
                    cur.execute(
                        """
                        update public.model_scout_evidence
                           set active = false, updated_at = now()
                         where active = true and last_seen_run is distinct from %s::uuid
                        """,
                        (run_id,),
                    )

                cur.execute(
                    """
                    update public.model_scout_sync_runs
                    set status = 'completed', completed_at = now()
                    where run_id = %s::uuid
                    """,
                    (run_id,),
                )
        return {
            "run_id": run_id,
            "sync_mode": stage_versions["sync_mode"],
            "upserted": len(rows),
            "evidence_upserted": len(evidence_rows),
            "deactivated": deactivated,
            "corpus_rows": corpus_rows,
        }
    except Exception as exc:
        try:
            conn.rollback()
            with conn.cursor() as cur:
                cur.execute(
                    """
                    update public.model_scout_sync_runs
                    set status = 'failed', completed_at = now(), error = %s
                    where run_id = %s::uuid
                    """,
                    (str(exc)[:2000], run_id),
                )
            conn.commit()
        except Exception:
            pass
        raise
    finally:
        conn.close()



def ensure_schema() -> None:
    conn = db_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                verify_vector_extension(cur)
                cur.execute(schema_sql_without_extension())
    finally:
        conn.close()



def schema_sql_without_extension() -> str:
    """Return schema DDL without re-creating an existing pgvector extension."""
    lines = SCHEMA_PATH.read_text(encoding="utf-8").splitlines()
    return "\n".join(
        line for line in lines
        if not re.match(
            r"^\s*create\s+extension\s+if\s+not\s+exists\s+vector\s*;",
            line,
            flags=re.IGNORECASE,
        )
    )


def verify_vector_extension(cur: Any) -> None:
    """Fail clearly when the Supabase project has not enabled pgvector."""
    cur.execute("select 1 from pg_extension where extname = 'vector'")
    if cur.fetchone() is None:
        raise RuntimeError(
            "Supabase pgvector extension is not enabled. Enable the vector extension "
            "once in the Supabase dashboard, then rerun this command."
        )

def ttl_is_fresh(metadata: Optional[Dict[str, Any]], ttl_hours: float) -> bool:
    if not metadata:
        return False
    completed = parse_utc(metadata.get("completed_at"))
    if completed is None:
        return False
    return completed >= datetime.now(timezone.utc) - timedelta(hours=ttl_hours)



def run_command(command: Sequence[str]) -> None:
    print("RUN", " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def parse_utc(value: Any) -> Optional[datetime]:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    text = str(value).strip()
    if not text:
        return None
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)



def latest_completed_sync() -> Optional[Dict[str, Any]]:
    conn = db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                select run_id, completed_at, stage_versions, row_count
                from public.model_scout_sync_runs
                where status = 'completed'
                  and stage_versions @> %s::jsonb
                  and coalesce(stage_versions->>'sync_mode', 'initial') in ('initial', 'incremental')
                order by completed_at desc
                limit 1
                """,
                (json_text(EXPECTED_VERSIONS),),
            )
            row = cur.fetchone()
            if not row:
                return None
            versions = row[2] if isinstance(row[2], dict) else json.loads(row[2] or "{}")
            completed = row[1].isoformat() if hasattr(row[1], "isoformat") else str(row[1])
            return {
                "run_id": str(row[0]),
                "completed_at": completed,
                "stage_versions": versions,
                "row_count": row[3],
            }
    finally:
        conn.close()




def load_stage1_module() -> Any:
    source = ROOT / "01_collect_models.py"
    spec = importlib.util.spec_from_file_location("model_scout_stage1_incremental", source)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {source}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_incremental_scan(
    task_observed: Dict[str, bool],
    existing_count: int,
) -> None:
    """Reject an incremental run where a task was not successfully observed.

    ``task_observed`` records successful API iteration, while ``task_seen``
    records models returned after the watermark.  A task can be observed
    successfully and still have zero changed models, which is the normal
    no-change case and must not block the refresh.
    """
    if not existing_count:
        return

    missing = sorted(task for task, observed in task_observed.items() if not observed)
    if missing:
        raise RuntimeError(
            "Incremental Hugging Face scan did not successfully observe task(s): "
            + ", ".join(missing)
            + "; refusing to update the snapshot"
        )


def publish_stage1_snapshot(stage1: Any, all_models: Dict[str, Dict[str, Any]], state: Dict[str, Any]) -> None:
    """Validate a complete Stage 1 snapshot before replacing published files."""
    output_names = (
        "CORE_OUTPUT",
        "LOW_POPULARITY_OUTPUT",
        "LIKELY_OUTPUT",
        "FALLBACK_OUTPUT",
        "GROUP_OUTPUT",
        "STATE_OUTPUT",
    )
    final_paths = {
        name: DATA_DIR / Path(getattr(stage1, name)).name for name in output_names
    }
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    previous_counts = stage1.snapshot_counts(final_paths)

    with tempfile.TemporaryDirectory(prefix=".stage1_publish_", dir=str(DATA_DIR)) as temp_name:
        temp_dir = Path(temp_name)
        original_data_dir = stage1.DATA_DIR
        original_paths = {name: getattr(stage1, name) for name in output_names}
        staged_paths = {name: temp_dir / path.name for name, path in final_paths.items()}

        try:
            stage1.DATA_DIR = temp_dir
            for name, path in staged_paths.items():
                setattr(stage1, name, path)

            stage1.save_all(all_models, state)
            stage1.validate_outputs(require_complete=False)
            current_counts = stage1.snapshot_counts(staged_paths)
            stage1.validate_snapshot_drop(previous_counts, current_counts)

            backups = []
            published = []
            try:
                for final_path in final_paths.values():
                    if final_path.exists():
                        backup_path = temp_dir / f"{final_path.name}.previous"
                        final_path.replace(backup_path)
                        backups.append((final_path, backup_path))

                for name, final_path in final_paths.items():
                    staged_paths[name].replace(final_path)
                    published.append(final_path)
            except Exception:
                for final_path in published:
                    if final_path.exists():
                        final_path.unlink()
                for final_path, backup_path in reversed(backups):
                    if backup_path.exists():
                        backup_path.replace(final_path)
                raise
        finally:
            stage1.DATA_DIR = original_data_dir
            for name, path in original_paths.items():
                setattr(stage1, name, path)


def incremental_stage1_update(watermark: str) -> Dict[str, Any]:
    """Scan only Hugging Face models modified after the previous sync watermark."""
    from huggingface_hub import HfApi

    stage1 = load_stage1_module()
    source_paths = (
        DATA_DIR / "hf_models_stage1_core.jsonl",
        DATA_DIR / "hf_models_stage1_low_popularity.jsonl",
        DATA_DIR / "hf_models_stage1_likely.jsonl",
        DATA_DIR / "hf_models_stage1_fallback.jsonl",
    )
    all_models: Dict[str, Dict[str, Any]] = {}
    for source_path in source_paths:
        for row in read_jsonl(source_path):
            model_id = row.get("model_id")
            if model_id:
                all_models[model_id] = row
    existing_ids = set(all_models)

    changed_ids = set()
    eligible_ids = set()
    scanned = 0
    task_scanned: Dict[str, int] = {}
    task_seen: Dict[str, int] = {task: 0 for task in stage1.TASKS}
    task_observed: Dict[str, bool] = {task: False for task in stage1.TASKS}
    watermark_dt = parse_utc(watermark)
    scan_started = datetime.now(timezone.utc)
    api = HfApi(token=os.getenv("HF_TOKEN"))

    def models_for_task(task: str):
        options = {
            "pipeline_tag": task,
            "sort": "last_modified",
            "direction": -1,
            "limit": None,
            "full": True,
            "cardData": True,
        }
        for attempt in range(API_MAX_RETRIES + 1):
            try:
                try:
                    models = api.list_models(**options)
                except TypeError:
                    options.pop("direction", None)
                    models = api.list_models(**options)
                iterator = iter(models)
                try:
                    first = next(iterator)
                except StopIteration:
                    # A successful empty response means no changed models,
                    # not an API failure.
                    task_observed[task] = True
                    return
                task_observed[task] = True
                yield first
                yield from iterator
                return
            except KeyboardInterrupt:
                raise
            except Exception as exc:
                if attempt >= API_MAX_RETRIES:
                    raise
                delay = API_RETRY_BASE_SECONDS * (2**attempt)
                print(
                    f"[API RETRY] task={task} attempt={attempt + 1}/{API_MAX_RETRIES} "
                    f"after {type(exc).__name__}: sleeping {delay}s",
                    flush=True,
                )
                time.sleep(delay)

    for task in stage1.TASKS:
        task_count = 0
        for model in models_for_task(task):
            task_seen[task] = task_seen.get(task, 0) + 1
            modified = parse_utc(
                getattr(model, "last_modified", None)
                or getattr(model, "lastModified", None)
            )
            if watermark_dt and modified and modified < watermark_dt:
                break
            model_id = getattr(model, "id", None) or getattr(model, "modelId", None)
            if not model_id:
                continue
            task_count += 1
            scanned += 1
            changed_ids.add(model_id)
            if stage1.is_noise_model(model_id):
                continue
            downloads = int(getattr(model, "downloads", None) or 0)
            classification = stage1.classify_candidate(model)
            if (
                classification is None
                or classification.get("tier") not in stage1.CANDIDATE_TYPES
                or downloads < stage1.MIN_DOWNLOADS
            ):
                continue
            replacement = stage1.build_row(model, classification)
            previous = all_models.get(model_id) or {}
            replacement["matched_tasks"] = list(
                dict.fromkeys((previous.get("matched_tasks") or []) + [task])
            )
            all_models[model_id] = replacement
            eligible_ids.add(model_id)
        task_scanned[task] = task_count

    validate_incremental_scan(task_observed, len(existing_ids))
    removed_ids = sorted((changed_ids & existing_ids) - eligible_ids)
    for model_id in removed_ids:
        all_models.pop(model_id, None)
    processable_ids = sorted(
        model_id
        for model_id in changed_ids
        if model_id in all_models
        and (all_models[model_id].get("candidate") or {}).get("tier") == "A_verified"
        and (all_models[model_id].get("popularity") or {}).get("downloads", 0) >= stage1.MIN_DOWNLOADS
    )

    state_path = DATA_DIR / "hf_models_stage1_state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    state["last_incremental_scan"] = {
        "started_at": scan_started.isoformat(),
        "watermark": watermark,
        "scanned": scanned,
        "changed": len(changed_ids),
        "eligible": len(eligible_ids),
        "processable": len(processable_ids),
        "removed": len(removed_ids),
        "task_scanned": task_scanned,
        "task_seen": task_seen,
        "task_observed": task_observed,
    }
    state["unique_candidates"] = len(all_models)
    if changed_ids or removed_ids:
        publish_stage1_snapshot(stage1, all_models, state)
    result = {
        "watermark": watermark,
        "scan_started_at": scan_started.isoformat(),
        "scanned": scanned,
        "changed_ids": sorted(changed_ids),
        "processable_ids": processable_ids,
        "removed_ids": removed_ids,
        "task_scanned": task_scanned,
        "task_seen": task_seen,
        "task_observed": task_observed,
    }
    print(
        json.dumps(
            {
                "incremental_stage1": {
                    "scanned": scanned,
                    "changed": len(changed_ids),
                    "processable": len(processable_ids),
                    "removed": len(removed_ids),
                    "watermark": watermark,
                }
            },
            ensure_ascii=False,
        ),
        flush=True,
    )
    return result



def incremental_refresh_pipeline(watermark: str) -> Dict[str, Any]:
    scan = incremental_stage1_update(watermark)
    # Preserve benchmark changes left by a previous failed run. Cleanup must
    # never discard the retry queue before it is merged into this scan.
    pending_benchmark_ids = read_model_ids(BENCHMARK_CHANGED_IDS_PATH)
    for pool in POOLS:
        pending_benchmark_ids.update(
            read_model_ids(DATA_DIR / f".hf_models_benchmark_changed_ids_{pool}.json")
        )
    clear_incremental_artifacts()
    needs_reconciliation = stage3_pools_need_reconciliation()
    processable_ids = set(scan["processable_ids"])
    processable_ids.update(pending_benchmark_ids)
    python = sys.executable
    if not processable_ids and not scan["removed_ids"] and not needs_reconciliation:
        print(json.dumps({"incremental_pipeline": "no eligible changes"}, ensure_ascii=False), flush=True)
        scan["requires_sync"] = False
        scan["stage4_mode"] = "delta"
        return scan
    if needs_reconciliation and not scan["processable_ids"] and not scan["removed_ids"]:
        print(
            json.dumps(
                {"incremental_pipeline": "reconcile stale Stage 3 pools"},
                ensure_ascii=False,
            ),
            flush=True,
        )
    write_model_ids(processable_ids)
    run_command(
        [
            python,
            str(ROOT / "02_enrich_metadata.py"),
            "--pool",
            "all",
            "--model-ids-file",
            str(MODEL_IDS_PATH),
        ]
    )
    # Stage 2's language gate drops models whose README targets another language. They never
    # change on the Hub, so the Stage 1 scan alone would leave their old DB rows active.
    language_excluded = set()
    for pool in POOLS:
        report = DATA_DIR / f"hf_models_stage2_{pool}_language_excluded.json"
        if report.exists():
            language_excluded.update(json.loads(report.read_text(encoding="utf-8")))
    processable_ids -= language_excluded
    scan["removed_ids"] = sorted(set(scan["removed_ids"]) | language_excluded)
    run_command(
        [
            python,
            str(ROOT / "03_generate_semantic_metadata.py"),
            "--pool",
            "all",
            "--model-ids-file",
            str(MODEL_IDS_PATH),
        ]
    )
    for pool in POOLS:
        run_command([python, str(ROOT / "03_repair_truncated_semantic.py"), "--pool", pool, "--apply"])
    # Relationship-only parent/child index; no LLM or embedding API call.
    run_command([python, str(ROOT / "evidence_index.py"), "--pool", "all"])
    run_command([
        python,
        str(ROOT / "06_extract_benchmark_metadata.py"),
        "--pool", "all",
    ])
    # The full benchmark pass writes the current changed-ID queue. Include it
    # in the targeted Stage 4 update; otherwise a newly changed README would
    # be detected but never reach the embedding delta.
    processable_ids.update(read_model_ids(BENCHMARK_CHANGED_IDS_PATH))
    write_model_ids(processable_ids)
    scan["sync_ids"] = sorted(processable_ids)
    if needs_reconciliation:
        run_command([python, str(ROOT / "04_build_embeddings.py"), "--pool", "all", "--execute", "--db-cache"])
        run_command([python, str(ROOT / "06_extract_benchmark_metadata.py"), "--pool", "all", "--apply"])
        scan["stage4_mode"] = "full"
    elif processable_ids:
        run_command([
            python,
            str(ROOT / "04_build_embeddings.py"),
            "--pool", "all", "--execute", "--db-cache",
            "--model-ids-file", str(MODEL_IDS_PATH),
        ])
        scan["stage4_mode"] = "delta"
    else:
        scan["stage4_mode"] = "delta"
    scan["requires_sync"] = True
    return scan



def apply_evidence_backfill(
    evidence_rows: Sequence[Tuple[Any, ...]],
    run_id: str,
    batch_size: int,
) -> Dict[str, Any]:
    """Insert all Parent-Child sidecars without rerunning Stages 1-4."""
    import psycopg2.extras

    stage_versions = dict(EXPECTED_VERSIONS)
    stage_versions.update({
        "sync_mode": "evidence_backfill",
        "evidence_index_version": 1,
    })
    statement = """
        insert into public.model_scout_evidence (
            model_id, source_pool, source_stage3_version, schema_version,
            evidence_index_version, source_stage3_hash, parent_count, child_count,
            parents, last_seen_run, refreshed_at
        ) values %s
        on conflict (model_id) do update set
            source_pool = excluded.source_pool,
            source_stage3_version = excluded.source_stage3_version,
            schema_version = excluded.schema_version,
            evidence_index_version = excluded.evidence_index_version,
            source_stage3_hash = excluded.source_stage3_hash,
            parent_count = excluded.parent_count,
            child_count = excluded.child_count,
            parents = excluded.parents,
            last_seen_run = excluded.last_seen_run,
            active = true,
            refreshed_at = excluded.refreshed_at,
            updated_at = now()
    """
    template = "(" + ", ".join(
        ["%s"] * 8 + ["%s::jsonb", "%s", "%s"]
    ) + ")"
    conn = db_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into public.model_scout_sync_runs
                        (run_id, status, stage_versions, row_count)
                    values (%s, 'running', %s::jsonb, %s)
                    """,
                    (run_id, json_text(stage_versions), len(evidence_rows)),
                )
                model_ids = [row[0] for row in evidence_rows]
                cur.execute(
                    "select model_id from public.model_scout_models "
                    "where model_id = any(%s) and active = true",
                    (model_ids,),
                )
                existing = {row[0] for row in cur.fetchall()}
                missing = sorted(set(model_ids) - existing)
                if missing:
                    raise RuntimeError(
                        "Cannot backfill evidence for missing active model rows: "
                        + ", ".join(missing[:20])
                    )
                psycopg2.extras.execute_values(
                    cur, statement, evidence_rows,
                    template=template, page_size=batch_size,
                )
                cur.execute(
                    """
                    update public.model_scout_sync_runs
                       set status = 'completed', completed_at = now()
                     where run_id = %s::uuid
                    """,
                    (run_id,),
                )
                return {
                    "run_id": run_id,
                    "sync_mode": "evidence_backfill",
            "evidence_upserted": len(evidence_rows),
                }
    except Exception as exc:
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        update public.model_scout_sync_runs
                           set status = 'failed', completed_at = now(), error = %s
                         where run_id = %s::uuid
                        """,
                        (str(exc)[:2000], run_id),
                    )
        except Exception:
            pass
        raise
    finally:
        conn.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write Supabase")
    parser.add_argument(
        "--initial",
        action="store_true",
        help="one-time full snapshot upload; rejected after a successful sync",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="incrementally scan only Hugging Face models modified since the last sync",
    )
    parser.add_argument("--force", action="store_true", help="ignore TTL; still incremental")
    parser.add_argument(
        "--ensure-schema",
        action="store_true",
        help="apply supabase_schema.sql explicitly, separate from data sync",
    )
    parser.add_argument(
        "--backfill-evidence",
        action="store_true",
        help="load Parent-Child sidecars into Supabase without rerunning Stages 1-4",
    )
    parser.add_argument(
        "--backfill-search-metadata",
        action="store_true",
        help="patch deterministic translation-pair/search aliases in existing DB rows",
    )
    parser.add_argument(
        "--backfill-runtime",
        action="store_true",
        help="patch runtime_compatibility JSON keys without rerunning Stage 1-4",
    )
    parser.add_argument(
        "--ttl-hours",
        type=float,
        default=None,
    )
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    args = parser.parse_args()
    if args.batch_size < 1:
        parser.error("--batch-size must be positive")
    if sum(bool(value) for value in (args.refresh, args.initial, args.ensure_schema, args.backfill_runtime, args.backfill_evidence, args.backfill_search_metadata)) > 1:
        parser.error("--refresh, --initial, --backfill-runtime, and --backfill-evidence are mutually exclusive")
    if (args.refresh or args.initial) and not args.apply:
        parser.error("--refresh/--initial require --apply")
    if args.backfill_runtime and not args.apply:
        parser.error("--backfill-runtime requires --apply")
    if args.backfill_search_metadata and not args.apply:
        parser.error("--backfill-search-metadata requires --apply")
    load_dotenv(ROOT / ".env")
    if args.ensure_schema:
        ensure_schema()
        print(json.dumps({"schema": "ensured"}, ensure_ascii=False))
        return 0
    if args.backfill_evidence and not args.apply:
        parser.error("--backfill-evidence requires --apply")
    if args.backfill_search_metadata:
        print(json.dumps({"search_metadata_backfill": backfill_search_metadata_db()}, ensure_ascii=False, indent=2))
        return 0
    if args.backfill_evidence:
        stage4, stage2, stage3 = load_corpora()
        validation = validate_corpus(stage4, stage2, stage3)
        evidence = load_evidence_indices()
        evidence_validation = validate_evidence_indices(stage4, evidence)
        run_id = str(uuid.uuid4())
        evidence_rows = evidence_payloads(stage4, evidence, run_id)
        result = apply_evidence_backfill(evidence_rows, run_id, args.batch_size)
        result["validation"] = validation
        result["evidence_validation"] = evidence_validation
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    if args.backfill_runtime:
        print(json.dumps({"runtime_backfill": backfill_runtime_metadata()}, indent=2))
        return 0
    ttl_hours = args.ttl_hours if args.ttl_hours is not None else float(
        os.getenv("MODEL_SCOUT_TTL_HOURS", DEFAULT_TTL_HOURS)
    )


    refresh_info: Optional[Dict[str, Any]] = None
    latest: Optional[Dict[str, Any]] = None
    if args.apply:
        latest = latest_completed_sync()

    if args.refresh:
        if latest is None:
            raise RuntimeError(
                "No completed Supabase sync watermark exists. Run the one-time "
                "`python 08_sync_supabase.py --initial --apply` first."
            )
        if not args.force and ttl_is_fresh(latest, ttl_hours):
            print(
                json.dumps(
                    {
                        "skipped": True,
                        "reason": "TTL not expired",
                        "ttl_hours": ttl_hours,
                        "last_completed_at": latest.get("completed_at"),
                        "last_run_id": latest.get("run_id"),
                    },
                    ensure_ascii=False,
                )
            )
            return 0
        versions = latest.get("stage_versions") or {}
        watermark = versions.get("source_watermark") or latest.get("completed_at")
        if not watermark:
            raise RuntimeError("Could not determine incremental source watermark")
        refresh_info = incremental_refresh_pipeline(watermark)
    elif args.initial:
        if latest is not None:
            raise RuntimeError(
                "A successful Supabase sync already exists. Full snapshot uploads are "
                "disabled after initialization; use --refresh --apply."
            )
    elif args.apply and latest is not None:
        raise RuntimeError(
            "A successful Supabase sync already exists. Refusing a full upload; use "
            "--refresh --apply for incremental updates."
        )
    elif not args.apply:
        # Offline validation remains available and never contacts Supabase.
        pass

    if (
        refresh_info is not None
        and not refresh_info.get("requires_sync", True)
        and not refresh_info.get("removed_ids")
    ):
        print(json.dumps({"sync": "no eligible changes", "db_write": False}, ensure_ascii=False))
        return 0

    delta_mode = refresh_info is not None and refresh_info.get("stage4_mode") == "delta"
    stage4, stage2, stage3 = load_corpora(stage4_delta=delta_mode)
    if delta_mode:
        apply_benchmark_deltas(stage4)
    incremental_ids = (
        set(refresh_info.get("sync_ids", refresh_info.get("processable_ids", [])))
        if delta_mode and refresh_info is not None
        else None
    )
    validation = validate_corpus(
        stage4,
        stage2,
        stage3,
        incremental_ids=incremental_ids,
    )
    evidence = load_evidence_indices()
    evidence_validation = validate_evidence_indices(
        stage4,
        evidence,
        expected_model_ids=incremental_ids,
    )
    write_stage4_manifest(stage4, validation, corpus_rows=len(stage2))
    changed_ids = incremental_ids
    removed_ids = refresh_info.get("removed_ids", []) if refresh_info else []
    selected_stage4 = (
        [row for row in stage4 if row.get("model_id") in changed_ids]
        if changed_ids is not None
        else stage4
    )
    run_id = str(uuid.uuid4())
    rows = payloads(selected_stage4, stage2, stage3, run_id)
    evidence_rows = evidence_payloads(selected_stage4, evidence, run_id)
    result: Dict[str, Any] = {
        "validation": validation,
        "evidence_validation": evidence_validation,
        "run_id": run_id,
        "apply": args.apply,
        "selected_pools": list(POOLS),
        "sync_mode": "incremental" if refresh_info else "initial",
        "changed_rows": len(selected_stage4),
        "removed_rows": len(removed_ids),
    }
    if args.apply:
        result["sync"] = apply_sync(
            rows,
            evidence_rows,
            run_id,
            args.batch_size,
            incremental=refresh_info is not None,
            removed_ids=removed_ids,
            source_watermark=(refresh_info or {}).get("scan_started_at"),
            corpus_rows=len(stage2),
            )
        promote_benchmark_state()
        # Only remove one-run queues after the database transaction has
        # succeeded. Persistent per-pool benchmark state remains intact.
        clear_incremental_artifacts()
    else:
        result["dry_run"] = {
            "rows": len(rows),
            "estimated_json_bytes": sum(len(json.dumps(row, ensure_ascii=False, default=str)) for row in rows),
        }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0



if __name__ == "__main__":
    raise SystemExit(main())
