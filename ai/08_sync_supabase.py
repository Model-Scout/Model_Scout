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


# Position of the vector literal in a payloads() tuple. It is stored as halfvec (2 bytes per
# dimension), so its text length says nothing about storage.
PAYLOAD_VECTOR_INDEX = 21


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


SYNC_MODES = ("initial", "incremental", "reingest")


def db_active_model_ids(cur: Any = None) -> Set[str]:
    """Supabase 의 현재 active Core/Low 모델 ID. 읽기만 한다.

    재적재의 비활성화 대상은 로컬 Stage 4 가 아니라 이 목록과 비교해 정한다.
    로컬 Stage 4 와 DB active 행 수가 어긋났던 적이 있어, 로컬 기준으로 빼면
    DB 에만 남은 행이 계속 active 로 남는다.
    """
    query = (
        "select model_id from public.model_scout_models "
        "where active = true and source_pool in ('core', 'low_popularity')"
    )
    if cur is not None:
        cur.execute(query)
        return {row[0] for row in cur.fetchall()}
    conn = db_connection()
    try:
        with conn.cursor() as own:
            own.execute(query)
            return {row[0] for row in own.fetchall()}
    finally:
        conn.close()


def apply_sync(
    rows: Sequence[Tuple[Any, ...]],
    evidence_rows: Sequence[Tuple[Any, ...]],
    run_id: str,
    batch_size: int,
    *,
    sync_mode: str = "initial",
    removed_ids: Sequence[str] = (),
    deactivate_missing: bool = False,
    stage4_ids: Optional[Sequence[str]] = None,
    source_watermark: Optional[str] = None,
    corpus_rows: Optional[int] = None,
    extra_versions: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Upsert rows and deactivate what the mode says is gone, in one transaction.

    비활성화 정책은 모드마다 다르다.

      initial      이번 run 이 올리지 않은 Core/Low active 행 전부
      incremental  removed_ids 만
      reingest     removed_ids 와, deactivate_missing 이면 "DB active - stage4_ids"
                   까지. 같은 트랜잭션 안에서 DB active 를 다시 읽고
                   assert_deactivation_plan 을 통과해야만 쓴다
    """
    import psycopg2.extras

    if sync_mode not in SYNC_MODES:
        raise ValueError(f"unknown sync_mode: {sync_mode!r}")
    if deactivate_missing and (sync_mode != "reingest" or stage4_ids is None):
        raise ValueError("deactivate_missing needs sync_mode='reingest' and stage4_ids")
    stage_versions = dict(EXPECTED_VERSIONS)
    stage_versions["sync_mode"] = sync_mode
    if source_watermark:
        stage_versions["source_watermark"] = source_watermark
    if corpus_rows is not None:
        stage_versions["corpus_rows"] = corpus_rows
    stage_versions.update(extra_versions or {})
    plan: Optional[Dict[str, Any]] = None

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
                if sync_mode == "reingest":
                    # upsert 전에 읽는다. upsert 가 active=true 로 되살리는 행이
                    # 섞이면 "원래 active 였던 것"을 알 수 없다.
                    plan = deactivation_plan(
                        db_active_model_ids(cur),
                        stage4_ids if stage4_ids is not None else (),
                        removed_ids,
                        deactivate_missing=deactivate_missing,
                    )
                    assert_deactivation_plan(plan)
                    removed_ids = plan["candidate_ids"]
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
                if sync_mode in ("incremental", "reingest"):
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
        result = {
            "run_id": run_id,
            "sync_mode": stage_versions["sync_mode"],
            "upserted": len(rows),
            "evidence_upserted": len(evidence_rows),
            "deactivated": deactivated,
            "corpus_rows": corpus_rows,
        }
        if plan is not None:
            result["deactivation"] = plan
        return result
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



def latest_completed_sync(any_versions: bool = False) -> Optional[Dict[str, Any]]:
    """The newest completed run that a watermark can be taken from.

    --refresh needs a run with the current stage versions: an incremental scan over an older schema
    would leave unchanged models without the new fields. --reingest passes any_versions=True, because
    upgrading the versions is its job; otherwise the first reingest after a version bump finds no
    run at all and refuses to apply.
    """
    conn = db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                select run_id, completed_at, stage_versions, row_count
                from public.model_scout_sync_runs
                where status = 'completed'
                  and (%s or stage_versions @> %s::jsonb)
                  and coalesce(stage_versions->>'sync_mode', 'initial') in ('initial', 'incremental', 'reingest')
                order by completed_at desc
                limit 1
                """,
                (any_versions, json_text(EXPECTED_VERSIONS)),
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
    with tempfile.TemporaryDirectory(prefix="model_scout_contract_baseline_") as baseline_dir:
        baseline = snapshot_contract_baseline(Path(baseline_dir))
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
        # Contract gate before the paid stages, as in --reingest. A changed model whose new
        # Stage 2 record lost values it had at the same Hub revision stops the run here.
        scan["contract_gate"] = contract_gate(require=True, baseline=baseline)
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



def snapshot_contract_baseline(dest_dir: Path) -> Optional[Path]:
    """Stage 2 가 덮어쓰기 전의 계약 레코드를 한 파일로 모은다. 없으면 None.

    두 풀을 합친다. Core ↔ Low 로 옮긴 모델도 이전 값과 비교돼야 하기 때문이다.
    """
    lines: List[str] = []
    for pool in POOLS:
        path = DATA_DIR / f"hf_models_stage2_contract_{pool}.jsonl"
        if path.exists():
            lines.extend(line for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
    if not lines:
        return None
    baseline = dest_dir / "contract_baseline.jsonl"
    baseline.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return baseline


def contract_gate(require: bool = False, baseline: Optional[Path] = None) -> Dict[str, Any]:
    """적재 전 데이터 계약 검사. 유료 단계 앞의 게이트다.

    baseline 이 있으면 같은 모델의 이전 계약 레코드와 비교해 값 손실·근거 하락을
    잡는다(contract/validate.py --baseline). 같은 Hub revision 에서 값을 잃었으면 실패,
    revision 이 바뀐 모델은 경고로만 보고한다. 이전 레코드가 없는 첫 계약 실행은
    스키마·출처 검사만 하고 비교는 건너뛰며, 그 이유를 결과에 남긴다.

    비용 순서가 Stage 2(무료) → Stage 3(LLM) → Stage 4(임베딩) → DB 쓰기이므로
    여기서 멈춰야 돈이 나가지 않는다.

    백필 작업에서 실제로 났던 사고를 막는 것이 목적이다. Stage 4 문서를 직접
    조립했더니 task·candidate·popularity·search_aliases 등 12개 키가 빠졌고,
    형식은 유효한 JSON이라 임베딩까지 정상 생성됐다. 비교 결과가 전부 0으로
    나온 뒤에야 알았다.
    """
    python = sys.executable
    results: Dict[str, Any] = {
        "baseline": str(baseline.name) if baseline else None,
        "baseline_skipped": None if baseline else "이전 계약 레코드 없음 (첫 계약 실행) — 회귀 비교 생략",
    }
    for pool in POOLS:
        path = DATA_DIR / f"hf_models_stage2_contract_{pool}.jsonl"
        if not path.exists():
            if require:
                # 재적재는 Stage 2를 전수로 돌리므로 이 파일이 반드시 생긴다.
                # 없다면 Stage 2가 조용히 실패했거나 구 코드가 돈 것이다.
                raise RuntimeError(
                    f"[{pool}] {path.name} 이 없다. Stage 2 가 계약 레코드를 쓰지 않았다 — "
                    "검증 없이 적재하지 않는다"
                )
            results[pool] = {"skipped": "계약 파일 없음 (구 Stage 2 데이터)"}
            continue
        command = [python, str(ROOT / "contract" / "validate.py"), str(path)]
        with tempfile.TemporaryDirectory() as temp:
            summary_path = Path(temp) / "summary.json"
            command += ["--summary-json", str(summary_path)]
            if baseline is not None:
                command += ["--baseline", str(baseline)]
            completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
            summary = (
                json.loads(summary_path.read_text(encoding="utf-8")) if summary_path.exists() else None
            )
        results[pool] = {
            "returncode": completed.returncode,
            "summary": summary,
            "report": completed.stdout.strip().splitlines()[-12:],
        }
        if completed.returncode != 0:
            raise RuntimeError(
                f"[{pool}] 데이터 계약 위반으로 적재를 중단한다:\n{completed.stdout}"
            )
    return results


# 재적재 안전장치. full_reingest_pipeline 은 하위 프로세스를 띄우므로 단위
# 테스트가 어렵다. 판단 로직만 떼어 내 test/test_reingest_safety.py 가 검사한다.

# Stage 2 가 조용히 대량 실패했는지 보는 하한. 언어 게이트 제외분은 정상 감소이므로
# 분모에서 뺀다. 2%는 개별 모델의 일시적 조회 실패를 허용하는 폭이다.
STAGE2_VOLUME_TOLERANCE = 0.98


def language_excluded_ids(data_dir: Path = None) -> Set[str]:
    """Stage 2 의 언어 게이트가 떨어뜨린 모델. Hub 에서 바뀌지 않으므로 계속 제외된다.

    Supabase 행을 비활성화해 주지 않으면 낡은 데이터로 계속 active 로 남는다.
    incremental_refresh_pipeline 이 하는 것과 같은 처리다.
    """
    base = data_dir if data_dir is not None else DATA_DIR
    excluded: Set[str] = set()
    for pool in POOLS:
        report = base / f"hf_models_stage2_{pool}_language_excluded.json"
        if report.exists():
            excluded.update(json.loads(report.read_text(encoding="utf-8")))
    return excluded


def stage2_volume_floor(expected: int, excluded: int) -> float:
    """Stage 2 결과가 이보다 적으면 대량 실패로 본다."""
    return max(expected - excluded, 0) * STAGE2_VOLUME_TOLERANCE


def assert_stage2_volume(expected: int, produced: int, excluded: int) -> None:
    """Stage 2 가 대량 실패했으면 유료 단계로 넘어가기 전에 끊는다.

    실패한 모델은 출력에서 그냥 사라지므로, 뒤 단계에서는 "원래 없던 모델"과
    구별되지 않는다. 적재까지 가면 그 행들이 전부 비활성화돼 복구가 번거롭다.
    """
    if not expected:
        return
    floor = stage2_volume_floor(expected, excluded)
    if produced < floor:
        raise RuntimeError(
            f"Stage 2 결과가 {produced}행이다. Stage 1 {expected}행에서 언어 게이트 "
            f"제외 {excluded}건을 빼면 {expected - excluded}행이어야 하고 허용 하한은 "
            f"{floor:.0f}행이다. 대량 실패로 보이므로 재적재를 중단한다"
        )


# ── Stage 1 전체 재스캔(--full-stage1) ──────────────────────────────────────
#
# 01_collect_models.py 의 run_collection() 이 이미 checkpoint 폴더에 수집하고,
# 모든 task 성공·파티션별 50% 감소 가드를 통과해야만 공개 파일을 교체한다.
# 그 경로를 하위 프로세스로 그대로 쓰고, 여기서는 재적재 관점의 가드만 더한다.

STAGE1_PARTITIONS = {
    "core": "hf_models_stage1_core.jsonl",
    "low_popularity": "hf_models_stage1_low_popularity.jsonl",
    "likely": "hf_models_stage1_likely.jsonl",
    "fallback": "hf_models_stage1_fallback.jsonl",
}
STAGE1_SNAPSHOT_FILES = tuple(STAGE1_PARTITIONS.values()) + (
    "hf_models_stage1_groups.jsonl",
    "hf_models_stage1_state.json",
)
# 비율 가드는 기준이 이보다 작으면 적용하지 않는다. 01 의 SNAPSHOT_DROP_MIN_ROWS 와 같다.
REINGEST_GUARD_MIN_ROWS = 100
# 처리 대상(Core ∪ Low)에서 빠지는 모델과 DB 에서 비활성화될 모델의 상한.
# 2026-11-13 첫 장기 공백 뒤 full-scan 에서 전체 task·cutoff·후보 감사를 모두
# 통과했지만 3,886개 중 957개(24.6%)가 교체됐다. 그 diff 를 사람이 검토했으므로
# 이번 전체 재적재에는 30%를 허용한다. 가드를 없애지는 않는다. apply와 스냅샷
# 반영이 끝나면 후속 PR에서 정상 운영값 10%로 반드시 되돌린다.
REINGEST_MAX_REMOVED_FRACTION = 0.30
REINGEST_MAX_DEACTIVATION_FRACTION = 0.30


class Stage1RemovalGuardError(RuntimeError):
    """Stage 1 교체율 가드가 막은 diff를 실패 보고서까지 운반한다."""

    def __init__(self, message: str, diff: Dict[str, Any]):
        super().__init__(message)
        self.diff = diff
        self.scan_started_at: Optional[str] = None


def stage1_partition_ids(data_dir: Optional[Path] = None) -> Dict[str, List[str]]:
    """Stage 1 파티션별 모델 ID. 파일이 없으면 빈 목록이다."""
    base = data_dir if data_dir is not None else DATA_DIR
    ids: Dict[str, List[str]] = {}
    for partition, name in STAGE1_PARTITIONS.items():
        path = base / name
        rows = read_jsonl(path) if path.exists() else []
        ids[partition] = [row["model_id"] for row in rows if row.get("model_id")]
    return ids


def stage1_diff(
    previous: Dict[str, Sequence[str]],
    current: Dict[str, Sequence[str]],
) -> Dict[str, Any]:
    """Stage 1 전후 차이. 처리 대상은 A 후보 중 Core ∪ Low 뿐이다.

    Likely(B)·Fallback(C)은 후보 분포로만 보고한다. Stage 2 로 가지 않으므로
    추가·제거 수에 섞으면 실제 DB 영향보다 훨씬 크게 보인다.
    """
    def processable(ids: Dict[str, Sequence[str]]) -> Set[str]:
        return set(ids.get("core", ())) | set(ids.get("low_popularity", ()))

    def tiers(ids: Dict[str, Sequence[str]]) -> Dict[str, int]:
        return {
            "A_verified": len(processable(ids)),
            "B_likely": len(ids.get("likely", ())),
            "C_fallback": len(ids.get("fallback", ())),
        }

    before, after = processable(previous), processable(current)
    previous_core, current_core = set(previous.get("core", ())), set(current.get("core", ()))
    previous_low = set(previous.get("low_popularity", ()))
    current_low = set(current.get("low_popularity", ()))
    return {
        "previous_processable": len(before),
        "current_processable": len(after),
        "pool_counts": {
            "previous": {pool: len(previous.get(pool, ())) for pool in POOLS},
            "current": {pool: len(current.get(pool, ())) for pool in POOLS},
        },
        "candidate_tiers": {"previous": tiers(previous), "current": tiers(current)},
        "added_ids": sorted(after - before),
        "removed_ids": sorted(before - after),
        "core_to_low_ids": sorted(previous_core & current_low),
        "low_to_core_ids": sorted(previous_low & current_core),
    }


def fraction_guard(base: int, count: int, max_fraction: float) -> Dict[str, Any]:
    """count 가 base 의 max_fraction 을 넘는지. base 가 작으면 판단하지 않는다."""
    allowed = int(base * max_fraction) if base >= REINGEST_GUARD_MIN_ROWS else None
    return {
        "base": base,
        "count": count,
        "max_fraction": max_fraction,
        "max_allowed": allowed,
        "blocked": allowed is not None and count > allowed,
    }


def assert_stage1_removal(diff: Dict[str, Any]) -> Dict[str, Any]:
    """새 Stage 1 이 처리 대상을 너무 많이 잃었으면 Stage 2 전에 끊는다.

    Core ↔ Low 이동은 제거가 아니다. 두 풀을 합친 집합에서 사라진 것만 센다.
    """
    guard = fraction_guard(
        diff["previous_processable"], len(diff["removed_ids"]), REINGEST_MAX_REMOVED_FRACTION
    )
    # 실패해도 added/removed ID와 함께 이 판정을 artifact에 남긴다.
    diff["removal_guard"] = guard
    if guard["blocked"]:
        raise Stage1RemovalGuardError(
            f"새 Stage 1 이 처리 대상 {guard['base']}개 중 {guard['count']}개를 잃었다 "
            f"(상한 {guard['max_allowed']}개). 수집 이상으로 보고 재적재를 중단한다",
            diff,
        )
    return guard


def deactivation_plan(
    db_active_ids: Sequence[str],
    stage4_ids: Sequence[str],
    removed_ids: Sequence[str] = (),
    *,
    deactivate_missing: bool,
) -> Dict[str, Any]:
    """재적재가 비활성화할 DB 행.

    deactivate_missing 이면 "DB active - 새 Stage 4" 전체가 대상이다. 아니면
    (Stage 1 재사용) 예전처럼 removed_ids(언어 게이트 제외분)만 대상이고,
    DB 에만 남은 행은 보고만 한다.
    """
    active = set(db_active_ids)
    stage4 = set(stage4_ids)
    missing = active - stage4
    explicit = set(removed_ids) & active
    candidates = (missing | explicit) if deactivate_missing else explicit
    plan = {
        "deactivate_missing": deactivate_missing,
        "db_active": len(active),
        "stage4": len(stage4),
        "db_only_ids": sorted(missing),
        "candidate_ids": sorted(candidates),
        "candidate_count": len(candidates),
    }
    plan["guard"] = fraction_guard(len(active), len(candidates), REINGEST_MAX_DEACTIVATION_FRACTION)
    return plan


def assert_deactivation_plan(plan: Dict[str, Any]) -> None:
    guard = plan["guard"]
    if guard["blocked"]:
        raise RuntimeError(
            f"DB active {guard['base']}행 중 {guard['count']}행을 비활성화하게 된다 "
            f"(상한 {guard['max_allowed']}행). 적재를 중단한다 — dry-run 보고서의 "
            "deactivation.candidate_ids 를 확인한다"
        )


def run_full_stage1_scan() -> Dict[str, Any]:
    """01_collect_models.py 로 Stage 1 을 처음부터 다시 만든다.

    scan_started_at 은 수집 **시작 전** 시각이다. 완료 시각을 watermark 로 쓰면
    스캔 도중 Hub 에서 바뀐 모델을 다음 --refresh 가 건너뛴다.

    01 이 실패하면 공개 파일은 그대로다(01 이 보장한다). 01 이 공개한 뒤 여기
    가드에서 멈추면 백업으로 되돌려, 실패한 재적재가 로컬 Stage 1 을 바꿔 두지
    않게 한다.
    """
    import shutil

    previous = stage1_partition_ids()
    scan_started = datetime.now(timezone.utc)
    with tempfile.TemporaryDirectory(prefix=".stage1_reingest_backup_", dir=str(DATA_DIR)) as name:
        backup = Path(name)
        for filename in STAGE1_SNAPSHOT_FILES:
            if (DATA_DIR / filename).exists():
                shutil.copy2(DATA_DIR / filename, backup / filename)
        try:
            # 낡은 미완료 checkpoint 를 이어 받으면 scan_started_at 이전에 본
            # 모델이 섞인다. 재적재는 항상 처음부터 수집한다.
            run_command([sys.executable, str(ROOT / "01_collect_models.py"), "--no-resume"])
            diff = stage1_diff(previous, stage1_partition_ids())
            assert_stage1_removal(diff)
        except Stage1RemovalGuardError as error:
            error.scan_started_at = scan_started.isoformat()
            for filename in STAGE1_SNAPSHOT_FILES:
                if (backup / filename).exists():
                    (backup / filename).replace(DATA_DIR / filename)
            raise
        except Exception:
            for filename in STAGE1_SNAPSHOT_FILES:
                if (backup / filename).exists():
                    (backup / filename).replace(DATA_DIR / filename)
            raise
    return {"scan_started_at": scan_started.isoformat(), "diff": diff}


def carried_watermark(latest: Optional[Dict[str, Any]]) -> Optional[str]:
    """재적재가 물려받을 직전 watermark.

    재적재는 Stage 1 을 스캔하지 않는다. 자기 시작 시각을 watermark 로 올려
    버리면 **직전 Stage 1 스캔 이후부터 재적재 사이에 Hub 에서 바뀐 모델을 다음
    --refresh 가 영구히 건너뛴다.** 그 구간은 아무도 본 적이 없다.
    """
    if not latest:
        return None
    value = ((latest.get("stage_versions") or {}).get("source_watermark")
             or latest.get("completed_at"))
    return str(value) if value else None


def resolved_source_watermark(refresh_info: Optional[Dict[str, Any]]) -> Optional[str]:
    """이번 실행이 저장할 watermark.

    --reingest 는 직전 값을 그대로 돌려준다(Stage 1 을 스캔하지 않았다).
    --refresh 는 자기 스캔 시작 시각을 돌려준다.
    """
    info = refresh_info or {}
    if "source_watermark" in info:
        return info["source_watermark"]
    return info.get("scan_started_at")


def reingest_result(
    *,
    previous_watermark: Optional[str],
    started_at: str,
    steps: Sequence[str],
    contract_gate_report: Dict[str, Any],
    language_excluded: Set[str],
    stage2_rows: int,
    stage1_scan: Optional[Dict[str, Any]] = None,
    stage1_processable: Optional[int] = None,
    language_excluded_in_stage1: Optional[int] = None,
) -> Dict[str, Any]:
    """재적재가 main 의 적재 호출부로 넘기는 값.

    조립을 따로 둔 이유는 full_reingest_pipeline 이 하위 프로세스를 띄워 단위
    테스트가 어렵기 때문이다. 여기 두 값이 조용히 비면 사고가 난다.

      source_watermark  Stage 1 재사용이면 직전 값, 전체 재스캔이면 스캔 시작
                        시각이다. 비면 apply_sync 가 키를 넣지 않는다
      removed_ids       비면 언어 게이트로 새로 제외된 모델이 낡은 데이터로
                        계속 active 로 남는다
    """
    full_stage1 = stage1_scan is not None
    return {
        "mode": "reingest",
        "stage1_mode": "full-scan" if full_stage1 else "reuse",
        "started_at": started_at,
        # 재사용: Stage 1 을 스캔하지 않았으므로 watermark 를 전진시키지 않는다.
        # 전체 재스캔: 스캔을 시작한 시각까지는 Hub 를 다 봤다.
        "source_watermark": stage1_scan["scan_started_at"] if full_stage1 else previous_watermark,
        "previous_watermark": previous_watermark,
        "steps": list(steps),
        "contract_gate": contract_gate_report,
        "requires_sync": True,
        "stage4_mode": "full",
        "removed_ids": sorted(language_excluded),
        "stage2_rows": stage2_rows,
        "stage1_processable": stage1_processable,
        "language_excluded_total": len(language_excluded),
        "language_excluded_in_stage1": language_excluded_in_stage1,
        "stage1_diff": stage1_scan["diff"] if full_stage1 else None,
    }


def full_reingest_pipeline(
    previous_watermark: Optional[str],
    full_stage1: bool = False,
) -> Dict[str, Any]:
    """스키마가 바뀐 뒤의 전체 재적재.

    ``--refresh``를 쓸 수 없는 이유
    -----------------------------
    ``--refresh``는 watermark 이후 **변경된 모델만** 처리한다. 스키마가 바뀐
    첫 적재에는 쓸 수 없다. ``gated``·``sha``·``siblings[].size``는 Hub에서
    모델이 바뀌지 않은 모델에도 없기 때문이다. 변경 기준으로 고르면 그 셋을
    영원히 못 채운다.

    그런데도 비싼 단계를 전수로 돌리지는 않는다
    -----------------------------------------
    - Stage 2는 STAGE2_VERSION이 올라가 ``resume_matches``가 전부 불일치로 보고
      다시 수집한다. HF API만 쓰므로 무료다(약 8분).
    - Stage 3는 README 내용이 같으면 재사용한다. 실측 3,872건 중 3,721건
      (96.1%)이 재사용 가능이고 LLM 호출은 151건이다.
    - Stage 4는 ``document_hash``가 바뀐 문서만 재임베딩한다. 실측 약 1,340건,
      text-embedding-3-small 기준 약 $0.02다.

    기본(``full_stage1=False``)은 Stage 1을 다시 스캔하지 않는다. 바꾸려는 것은
    모델의 **사실**이고 모델 **목록**이 아니다. 목록까지 새로 만들려면
    ``--full-stage1``로 ``run_full_stage1_scan``을 먼저 돌린다. 그때는 스캔 시작
    시각이 새 watermark다.

    재사용 모드에서는 watermark를 전진시키지 않는다
    -------------------------------------------
    ``--refresh``는 저장된 ``source_watermark`` 이후에 Hub에서 바뀐 모델만
    스캔한다. 재적재가 자기 시작 시각을 watermark로 올려 버리면, **직전 Stage 1
    스캔 이후부터 재적재 사이에 바뀐 모델을 다음 ``--refresh``가 영구히
    건너뛴다.** Stage 1을 돌지 않았으므로 그 구간은 아무도 본 적이 없다.

    ``previous_watermark``를 그대로 돌려줘서 다음 ``--refresh``가 끊긴 지점부터
    이어 가게 한다.
    """
    python = sys.executable
    clear_incremental_artifacts()
    started = datetime.now(timezone.utc)
    steps: List[str] = []

    stage1_scan = run_full_stage1_scan() if full_stage1 else None
    if stage1_scan is not None:
        steps.append("stage1:full-scan")

    # Stage 2 — 전체. model-ids-file을 주지 않으면 풀 전체를 본다.
    # 기준은 (새) Stage 1 의 처리 대상이다.
    stage1_ids = {
        row["model_id"]
        for pool in POOLS
        for row in read_jsonl(DATA_DIR / f"hf_models_stage1_{pool}.jsonl")
    }
    # Stage 2 가 계약 sidecar 를 덮어쓰기 전에 이전 레코드를 떠 둔다. 게이트가 회귀 비교에 쓴다.
    with tempfile.TemporaryDirectory(prefix="model_scout_contract_baseline_") as baseline_dir:
        baseline = snapshot_contract_baseline(Path(baseline_dir))
        run_command([python, str(ROOT / "02_enrich_metadata.py"), "--pool", "all"])
        steps.append("stage2:full")

        # Stage 2의 언어 게이트는 README가 다른 언어를 겨냥한 모델을 떨어뜨린다.
        # Hub에서 바뀌지 않으므로 다음에도 계속 제외되는데, Supabase 행을 비활성화해
        # 주지 않으면 낡은 데이터로 계속 활성 상태로 남는다. --refresh가 하는 것과
        # 같은 처리다.
        language_excluded = language_excluded_ids()
        # 제외 보고서는 누적이라 지금 Stage 1 에 없는 옛 ID 도 있다. 볼륨 가드에서는
        # 이번 처리 대상 중 제외된 수만 빼야 대량 실패를 가려 주지 않는다.
        excluded_in_stage1 = len(language_excluded & stage1_ids)
        produced = sum(len(read_jsonl(DATA_DIR / f"hf_models_stage2_{pool}.jsonl")) for pool in POOLS)
        assert_stage2_volume(len(stage1_ids), produced, excluded_in_stage1)
        steps.append(f"stage2:{produced}rows")

        # Stage 2.5 — 계약 게이트. 유료 단계 앞이다.
        gate = contract_gate(require=True, baseline=baseline)
        steps.append("contract_gate")

    # Stage 3 — README가 바뀐 모델만 LLM을 부른다.
    run_command([python, str(ROOT / "03_generate_semantic_metadata.py"), "--pool", "all"])
    for pool in POOLS:
        run_command([python, str(ROOT / "03_repair_truncated_semantic.py"), "--pool", pool, "--apply"])
    run_command([python, str(ROOT / "evidence_index.py"), "--pool", "all"])
    steps.append("stage3:readme-delta")

    # Stage 3.5 — 벤치마크. API 호출이 없다.
    run_command([python, str(ROOT / "06_extract_benchmark_metadata.py"), "--pool", "all", "--apply"])
    steps.append("stage3.5:benchmark")

    # Stage 4 — document_hash가 바뀐 문서만 재임베딩한다.
    run_command([python, str(ROOT / "04_build_embeddings.py"), "--pool", "all", "--execute", "--db-cache"])
    steps.append("stage4:hash-delta")

    return reingest_result(
        previous_watermark=previous_watermark,
        started_at=started.isoformat(),
        steps=steps,
        contract_gate_report=gate,
        language_excluded=language_excluded,
        stage2_rows=produced,
        stage1_scan=stage1_scan,
        stage1_processable=len(stage1_ids),
        language_excluded_in_stage1=excluded_in_stage1,
    )


# ── DB 용량 ──────────────────────────────────────────────────────────────────
#
# 모델 테이블과 데이터셋 테이블(20_sync_dataset_index.py)은 같은 Supabase Pro DB 를 쓴다.
# Pro 의 기본 디스크는 8GB지만, 오작동으로 데이터가 급증하지 않도록 프로젝트 내부
# 안전 한도는 1GB로 더 낮게 둔다.
# 재적재는 모든 행을 다시 쓰고, 옛 행은 VACUUM 전까지 자리를 차지한다. 그래서 최고치는
# "지금 크기 + 이번에 쓸 양"이다. 한도는 20 과 같은 SUPABASE_DB_BUDGET_MB 를 쓴다.
DEFAULT_DB_BUDGET_MB = 1024
# search_tsv(생성 컬럼) 평균 크기. supabase_migration_model_search_tsv.sql 의 실측값이다.
TSV_BYTES_PER_MODEL = 7400
ROW_OVERHEAD_BYTES = 400
STORAGE_TABLES = (
    "public.model_scout_models",
    "public.model_scout_evidence",
    "public.model_scout_dataset_chunks",
    "public.model_scout_datasets",
)


def estimate_write_bytes(
    rows: Sequence[Tuple[Any, ...]],
    evidence_rows: Sequence[Tuple[Any, ...]],
    storage: Optional[Dict[str, int]] = None,
    added_bytes: int = 0,
) -> int:
    """이번 실행이 새로 쓰는 바이트.

    DB 에 모델 행이 있으면 실측으로 센다. 전체 행을 다시 쓰면 지금 모델·evidence 테이블
    (인덱스 포함)만큼 한 벌이 더 생기고, 이번에 새로 붙는 내용(added_bytes, 계약 레코드)이
    더해진다. added_bytes 는 압축 전 길이라 실제보다 크다. 행 수가 늘면 그 비율만큼 키운다.

    비어 있는 DB(첫 적재)는 실측할 것이 없으므로 아래 상한으로 센다.

    JSON 은 압축 전 텍스트 길이로 센다. jsonb 는 TOAST 에서 압축되므로 실제보다 크게
    나온다 — 가드는 보수적으로 둔다. 벡터는 halfvec 크기(2 B × 차원)로 센다.
    """
    if storage and storage.get("model_rows"):
        current = storage.get("model_scout_models", 0) + storage.get("model_scout_evidence", 0)
        scale = max(1.0, len(rows) / storage["model_rows"])
        return int(current * scale) + added_bytes
    total = 0
    for row in rows:
        total += sum(
            len(value.encode("utf-8"))
            for index, value in enumerate(row)
            if isinstance(value, str) and index != PAYLOAD_VECTOR_INDEX
        )
        total += 2 * 1536 + TSV_BYTES_PER_MODEL + ROW_OVERHEAD_BYTES
    for row in evidence_rows:
        total += sum(len(value.encode("utf-8")) for value in row if isinstance(value, str))
        total += ROW_OVERHEAD_BYTES
    return total


def db_storage(cur: Any = None) -> Dict[str, int]:
    """DB 전체와 테이블별 크기(바이트). 읽기만 한다."""
    query = "select pg_database_size(current_database())" + "".join(
        f", coalesce(pg_total_relation_size(to_regclass('{name}')), 0)" for name in STORAGE_TABLES
    ) + ", (select count(*) from public.model_scout_models)"

    def read(cursor: Any) -> Dict[str, int]:
        cursor.execute(query)
        values = cursor.fetchone()
        sizes = {name.split(".", 1)[1]: int(value) for name, value in zip(STORAGE_TABLES, values[1:-1])}
        return {"database": int(values[0]), **sizes, "model_rows": int(values[-1])}

    if cur is not None:
        return read(cur)
    conn = db_connection()
    try:
        with conn.cursor() as own:
            return read(own)
    finally:
        conn.close()


def capacity_plan(storage: Dict[str, int], write_bytes: int, budget_mb: Optional[float] = None) -> Dict[str, Any]:
    budget = float(
        budget_mb if budget_mb is not None
        else os.getenv("SUPABASE_DB_BUDGET_MB", DEFAULT_DB_BUDGET_MB)
    )
    peak = storage["database"] + write_bytes
    return {
        "tables_mb": {
            name: round(size / 1e6, 1) for name, size in storage.items() if name not in ("database", "model_rows")
        },
        "model_rows": storage.get("model_rows"),
        "database_mb": round(storage["database"] / 1e6, 1),
        "estimated_write_mb": round(write_bytes / 1e6, 1),
        "projected_peak_mb": round(peak / 1e6, 1),
        "budget_mb": budget,
        "blocked": peak / 1e6 > budget,
    }


def assert_capacity(plan: Dict[str, Any]) -> None:
    if plan["blocked"]:
        raise RuntimeError(
            f"DB 예상 최고치 {plan['projected_peak_mb']}MB 가 한도 {plan['budget_mb']:.0f}MB 를 넘는다 "
            f"(지금 {plan['database_mb']}MB + 이번 쓰기 {plan['estimated_write_mb']}MB). 적재하지 않는다 — "
            "VACUUM FULL·비활성 행 삭제로 공간을 먼저 확보하거나, 유료 플랜이면 SUPABASE_DB_BUDGET_MB 를 올린다"
        )


def reingest_report_summary(result: Dict[str, Any]) -> Dict[str, Any]:
    """GitHub Step Summary 용 수치. ID 목록은 빼고 개수만 남긴다."""
    refresh = result.get("reingest") or {}
    diff = refresh.get("stage1_diff") or {}
    deactivation = result.get("deactivation") or {}
    summary: Dict[str, Any] = {
        "apply": result.get("apply"),
        "stage1_mode": refresh.get("stage1_mode"),
        "previous_watermark": refresh.get("previous_watermark"),
        "source_watermark": refresh.get("source_watermark"),
        "stage1_processable": refresh.get("stage1_processable"),
        "language_excluded_in_stage1": refresh.get("language_excluded_in_stage1"),
        "stage2_rows": refresh.get("stage2_rows"),
        "stage4_rows": (result.get("validation") or {}).get("rows"),
        "db_active": deactivation.get("db_active"),
        "db_only": len(deactivation.get("db_only_ids") or []),
        "deactivation_candidates": deactivation.get("candidate_count"),
        "deactivation_blocked": (deactivation.get("guard") or {}).get("blocked"),
        "capacity": result.get("capacity"),
    }
    if diff:
        summary["stage1_diff"] = {
            "previous_processable": diff.get("previous_processable"),
            "current_processable": diff.get("current_processable"),
            "added": len(diff.get("added_ids") or []),
            "removed": len(diff.get("removed_ids") or []),
            "core_to_low": len(diff.get("core_to_low_ids") or []),
            "low_to_core": len(diff.get("low_to_core_ids") or []),
            "candidate_tiers": diff.get("candidate_tiers"),
        }
    return summary


def write_reingest_report(result: Dict[str, Any], path: Path) -> List[Path]:
    """감사용 JSON 을 쓴다. 전체 ID 목록은 여기, 요약은 *.summary.json 에 둔다."""
    path.parent.mkdir(parents=True, exist_ok=True)
    refresh = result.get("reingest") or {}
    outputs = {
        path: result,
        path.with_name(path.stem + ".summary.json"): reingest_report_summary(result),
        path.with_name(path.stem + ".stage1-diff.json"): refresh.get("stage1_diff"),
        path.with_name(path.stem + ".deactivation.json"): result.get("deactivation"),
    }
    written = []
    for target, value in outputs.items():
        if value is None:
            continue
        write_json_atomic(target, value)
        written.append(target)
    return written


def stage1_guard_failure_result(error: Stage1RemovalGuardError) -> Dict[str, Any]:
    """Stage 2 전에 멈춰도 GitHub artifact로 올릴 수 있는 실패 결과."""
    return {
        "apply": False,
        "sync_mode": "reingest",
        "db_write": False,
        "error": {
            "type": "stage1_removal_guard",
            "message": str(error),
            "failed_before": "stage2",
        },
        "reingest": {
            "mode": "reingest",
            "stage1_mode": "full-scan",
            "source_watermark": error.scan_started_at,
            "steps": ["stage1:full-scan", "stage1:removal-guard-blocked"],
            "requires_sync": False,
            "stage1_diff": error.diff,
        },
    }


def write_json_atomic(path: Path, value: Any) -> None:
    """반쯤 쓴 JSON 이 artifact 로 올라가지 않게 임시 파일에 쓴 뒤 바꿔 끼운다."""
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


# ── 승인한 dry-run 산출물을 그대로 적재 ─────────────────────────────────────
#
# dry-run 이 만든 Stage 1~4 를 번들로 묶어 artifact 로 올리고, apply 는 그 번들을 받아
# 검증한 뒤 DB 에만 쓴다. apply 가 Stage 1~4 를 다시 만들면 그 사이 Hub·LLM·임베딩이
# 달라져 사람이 검토한 결과와 실제로 적재한 결과가 달라질 수 있다.

BUNDLE_VERSION = 1
BUNDLE_MANIFEST = "manifest.json"
BUNDLE_REINGEST = "reingest.json"
BUNDLE_REPORT = "reingest-report.json"
# DATA_DIR 기준 경로. apply 의 DB 적재(load_corpora·load_evidence_indices)와 적재 뒤
# 스냅샷 커밋이 읽는 파일이다. 하나라도 없으면 apply 하지 않는다.
BUNDLE_REQUIRED_FILES = (
    *STAGE1_SNAPSHOT_FILES,
    *(f"hf_models_stage2_{pool}.jsonl" for pool in POOLS),
    *(f"hf_models_stage2_contract_{pool}.jsonl" for pool in POOLS),
    *(f"hf_models_stage3_{pool}.jsonl" for pool in POOLS),
    *(f"hf_models_stage3_parent_child_{pool}.jsonl" for pool in POOLS),
    *(f"hf_models_stage4_{pool}.jsonl" for pool in POOLS),
    "hf_models_stage4_manifest.json",
)
# 있으면 담는다. 없어도 적재는 된다(첫 실행에는 언어 제외 보고서가 없을 수 있다).
BUNDLE_OPTIONAL_FILES = (
    *(f"hf_models_stage2_{pool}_language_excluded.json" for pool in POOLS),
    "hf_models_stage3_parent_child_manifest.json",
    "hf_models_benchmark_state.json",
    ".hf_models_benchmark_state_candidate.json",
)
BUNDLE_DIRS = tuple(f"readmes/{pool}" for pool in POOLS)


class BundleError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def model_ids_sha256(model_ids: Sequence[str]) -> str:
    import hashlib

    return hashlib.sha256("\n".join(sorted(model_ids)).encode("utf-8")).hexdigest()


def bundle_path(target: str) -> str:
    """DATA_DIR 기준 경로 → 번들 안 경로. upload-artifact 는 숨김 파일을 빼므로 점을 뗀다."""
    return "data/" + "/".join(part.lstrip(".") for part in target.split("/"))


def git_identity() -> Dict[str, str]:
    """이 실행의 저장소·커밋·브랜치·run. Actions 가 넣는 환경 변수, 없으면 로컬 git."""
    def git(*args: str) -> str:
        done = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
        return done.stdout.strip() if done.returncode == 0 else ""

    return {
        "repository": os.getenv("GITHUB_REPOSITORY") or "local",
        "git_sha": os.getenv("GITHUB_SHA") or git("rev-parse", "HEAD"),
        "git_ref": os.getenv("GITHUB_REF_NAME") or git("rev-parse", "--abbrev-ref", "HEAD"),
        "run_id": os.getenv("GITHUB_RUN_ID") or "local",
    }


def bundle_targets() -> List[str]:
    """번들에 담을 DATA_DIR 기준 파일 목록(디렉터리는 파일로 펼친다)."""
    targets = list(BUNDLE_REQUIRED_FILES)
    targets += [name for name in BUNDLE_OPTIONAL_FILES if (DATA_DIR / name).exists()]
    for folder in BUNDLE_DIRS:
        base = DATA_DIR / folder
        if base.exists():
            targets += sorted(
                path.relative_to(DATA_DIR).as_posix() for path in base.rglob("*") if path.is_file()
            )
    return targets


def write_reingest_bundle(
    bundle_dir: Path,
    *,
    refresh_info: Dict[str, Any],
    report: Dict[str, Any],
    stage4_ids: Sequence[str],
    latest_sync_run_id: Optional[str],
) -> Dict[str, Any]:
    """dry-run 산출물과 manifest(파일별 SHA256·크기, 모델 ID hash, 출처)를 쓴다.

    비밀값은 담지 않는다. 담는 것은 DATA_DIR 의 산출물과 이번 실행의 보고서뿐이다.
    """
    import shutil

    missing = [name for name in BUNDLE_REQUIRED_FILES if not (DATA_DIR / name).exists()]
    if missing:
        raise BundleError("번들에 필요한 산출물이 없다: " + ", ".join(missing))
    if bundle_dir.exists():
        shutil.rmtree(bundle_dir)
    bundle_dir.mkdir(parents=True)
    files: List[Dict[str, Any]] = []
    for target in bundle_targets():
        relative = bundle_path(target)
        destination = bundle_dir / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DATA_DIR / target, destination)
        files.append({"path": relative, "target": target,
                      "sha256": sha256_file(destination), "bytes": destination.stat().st_size})
    for name, value in ((BUNDLE_REINGEST, refresh_info), (BUNDLE_REPORT, report)):
        write_json_atomic(bundle_dir / name, value)
        files.append({"path": name, "target": None,
                      "sha256": sha256_file(bundle_dir / name), "bytes": (bundle_dir / name).stat().st_size})
    identity = git_identity()
    manifest = {
        "bundle_version": BUNDLE_VERSION,
        "repository": identity["repository"],
        "git_sha": identity["git_sha"],
        "git_ref": identity["git_ref"],
        "dry_run_run_id": identity["run_id"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "stage_versions": EXPECTED_VERSIONS,
        "stage1_mode": refresh_info.get("stage1_mode"),
        "stage1_scan_started_at": (
            refresh_info.get("source_watermark") if refresh_info.get("stage1_mode") == "full-scan" else None
        ),
        "source_watermark": refresh_info.get("source_watermark"),
        "supabase_latest_sync_run_id": latest_sync_run_id,
        "model_count": len(set(stage4_ids)),
        "model_ids_sha256": model_ids_sha256(set(stage4_ids)),
        "files": files,
    }
    write_json_atomic(bundle_dir / BUNDLE_MANIFEST, manifest)
    return manifest


def bundled_stage4_ids(bundle_dir: Path) -> List[str]:
    ids: List[str] = []
    for pool in POOLS:
        ids += [row["model_id"] for row in read_jsonl(bundle_dir / bundle_path(f"hf_models_stage4_{pool}.jsonl"))]
    return ids


def verify_reingest_bundle(
    bundle_dir: Path,
    *,
    approved_run_id: str,
    repository: str,
    git_sha: str,
    latest_sync_run_id: Optional[str],
) -> Dict[str, Any]:
    """apply 전에 번들을 검증한다. 문제를 전부 모아 한 번에 실패한다. DB 에는 쓰지 않는다."""
    manifest_path = bundle_dir / BUNDLE_MANIFEST
    if not manifest_path.exists():
        raise BundleError(f"번들 manifest 가 없다: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    problems: List[str] = []

    def expect(key: str, actual: Any, wanted: Any, why: str) -> None:
        if actual != wanted:
            problems.append(f"{key}: 번들 {actual!r} ≠ {wanted!r} — {why}")

    expect("bundle_version", manifest.get("bundle_version"), BUNDLE_VERSION, "다른 형식의 번들")
    expect("dry_run_run_id", str(manifest.get("dry_run_run_id")), str(approved_run_id), "승인한 dry-run 이 아니다")
    expect("repository", manifest.get("repository"), repository, "다른 저장소의 artifact")
    expect("git_ref", manifest.get("git_ref"), "main", "main 에서 만든 dry-run 이 아니다")
    expect("git_sha", manifest.get("git_sha"), git_sha, "dry-run 이후 main 이 바뀌었다 — dry-run 을 다시 한다")
    expect("stage_versions", manifest.get("stage_versions"), EXPECTED_VERSIONS, "코드의 Stage 버전과 다르다")
    expect("supabase_latest_sync_run_id", manifest.get("supabase_latest_sync_run_id"), latest_sync_run_id,
           "dry-run 이후 다른 sync 가 DB 를 바꿨다")

    listed = {entry["path"] for entry in manifest.get("files") or []}
    for entry in manifest.get("files") or []:
        target = entry.get("target")
        if target is not None and (target.startswith("/") or ".." in Path(target).parts):
            problems.append(f"{entry['path']}: 허용되지 않는 대상 경로 {target!r}")
            continue
        path = bundle_dir / entry["path"]
        if not path.exists():
            problems.append(f"{entry['path']}: 파일 누락")
        elif path.stat().st_size != entry.get("bytes"):
            problems.append(f"{entry['path']}: 크기 불일치")
        elif sha256_file(path) != entry.get("sha256"):
            problems.append(f"{entry['path']}: SHA256 불일치")
    present = {
        path.relative_to(bundle_dir).as_posix()
        for path in bundle_dir.rglob("*") if path.is_file()
    } - {BUNDLE_MANIFEST}
    for extra in sorted(present - listed):
        problems.append(f"{extra}: manifest 에 없는 파일")
    targets = {entry.get("target") for entry in manifest.get("files") or []}
    for name in BUNDLE_REQUIRED_FILES:
        if name not in targets:
            problems.append(f"{name}: 필수 산출물이 번들에 없다")
    if BUNDLE_REINGEST not in listed:
        problems.append(f"{BUNDLE_REINGEST}: 재적재 결과가 번들에 없다")
    if not problems:
        actual = model_ids_sha256(set(bundled_stage4_ids(bundle_dir)))
        expect("model_ids_sha256", actual, manifest.get("model_ids_sha256"), "Stage 4 모델 집합이 바뀌었다")
    if problems:
        raise BundleError("승인한 dry-run 번들을 적재하지 않는다:\n- " + "\n- ".join(problems))
    manifest["bundle_sha256"] = sha256_file(manifest_path)
    manifest["reingest"] = json.loads((bundle_dir / BUNDLE_REINGEST).read_text(encoding="utf-8"))
    return manifest


def install_reingest_bundle(bundle_dir: Path, manifest: Dict[str, Any]) -> None:
    """검증한 번들의 산출물을 DATA_DIR 에 그대로 놓는다. README 폴더는 번들과 똑같이 맞춘다."""
    import shutil

    for folder in BUNDLE_DIRS:
        if (DATA_DIR / folder).exists():
            shutil.rmtree(DATA_DIR / folder)
    for entry in manifest["files"]:
        if entry.get("target") is None:
            continue
        destination = DATA_DIR / entry["target"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(bundle_dir / entry["path"], destination)


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
    parser.add_argument(
        "--reingest",
        action="store_true",
        help="전체 재적재. 스키마가 바뀐 첫 적재에 쓴다. --refresh는 변경된 모델만 "
             "보므로 새 필드를 채울 수 없다",
    )
    parser.add_argument(
        "--full-stage1",
        action="store_true",
        help="--reingest 와 함께만. Stage 1 을 Hugging Face 에서 처음부터 다시 수집한 뒤 "
             "Stage 2~4 를 돈다. 없으면 저장소의 Stage 1 을 재사용한다",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="결과 JSON 을 이 경로에 쓴다(하위 프로세스 로그가 섞이지 않는다). "
             "같은 폴더에 *.summary/*.stage1-diff/*.deactivation.json 도 쓴다",
    )
    parser.add_argument(
        "--bundle-dir",
        type=Path,
        default=None,
        help="--reingest dry-run 전용. 검토할 Stage 1~4 산출물과 manifest 를 이 폴더에 묶는다",
    )
    parser.add_argument(
        "--from-bundle",
        type=Path,
        default=None,
        help="--reingest --apply 에 필수. 승인한 dry-run 번들을 검증해 Stage 1~4 를 다시 "
             "만들지 않고 그대로 적재한다",
    )
    parser.add_argument(
        "--approved-run-id",
        default=None,
        help="--from-bundle 과 함께. 사람이 검토·승인한 dry-run 의 GitHub run ID",
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
    if sum(bool(value) for value in (args.refresh, args.initial, args.reingest, args.ensure_schema, args.backfill_runtime, args.backfill_evidence, args.backfill_search_metadata)) > 1:
        parser.error("--refresh, --initial, --reingest, --backfill-runtime, and --backfill-evidence are mutually exclusive")
    if args.full_stage1 and not args.reingest:
        parser.error("--full-stage1 requires --reingest")
    if args.bundle_dir is not None and (not args.reingest or args.apply):
        parser.error("--bundle-dir is for a --reingest dry-run (without --apply)")
    if args.reingest and args.apply and (args.from_bundle is None or not args.approved_run_id):
        # 재적재 apply 는 사람이 검토한 dry-run 산출물만 적재한다. 다시 만들지 않는다.
        parser.error("--reingest --apply requires --from-bundle and --approved-run-id")
    if args.from_bundle is not None and not (args.reingest and args.apply):
        parser.error("--from-bundle requires --reingest --apply")
    if args.from_bundle is not None and args.full_stage1:
        parser.error("--from-bundle replays the dry-run; its Stage 1 mode comes from the bundle")
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
    previous: Optional[Dict[str, Any]] = None
    bundle_manifest: Optional[Dict[str, Any]] = None
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
    elif args.reingest:
        # watermark를 전진시키지 않기 위해 직전 값을 읽는다. 버전은 따지지 않는다 —
        # 재적재는 버전을 올리는 작업이라 직전 run 은 대개 옛 버전이다.
        previous = latest_completed_sync(any_versions=True)
        if args.apply and previous is None:
            raise RuntimeError(
                "완료된 Supabase sync 기록이 없다. 먼저 "
                "`python 08_sync_supabase.py --initial --apply`를 돌려야 한다."
            )
        if args.from_bundle is not None:
            # 승인한 dry-run 산출물을 검증하고 그대로 놓는다. Stage 1~4 를 다시 돌리지 않는다.
            identity = git_identity()
            bundle_manifest = verify_reingest_bundle(
                args.from_bundle,
                approved_run_id=args.approved_run_id,
                repository=identity["repository"],
                git_sha=identity["git_sha"],
                latest_sync_run_id=(previous or {}).get("run_id"),
            )
            install_reingest_bundle(args.from_bundle, bundle_manifest)
            refresh_info = bundle_manifest["reingest"]
        else:
            # --apply 없이 돈다. DB를 건드리지 않고 dry-run 리포트(와 번들)만 낸다 —
            # 팀이 diff를 보고 승인한 번들만 apply 가 적재한다.
            try:
                refresh_info = full_reingest_pipeline(
                    carried_watermark(previous), full_stage1=args.full_stage1
                )
            except Stage1RemovalGuardError as error:
                # Stage 2 전에 실패해도 정확히 무엇이 추가·제거됐는지 Action
                # artifact에서 검토할 수 있어야 다음 한도 변경을 근거로 결정한다.
                if args.report is not None:
                    write_reingest_report(stage1_guard_failure_result(error), args.report)
                raise
    elif args.initial:
        if latest is not None:
            raise RuntimeError(
                "A successful Supabase sync already exists. Full snapshot uploads are "
                "disabled after initialization; use --refresh --apply."
            )
    elif args.apply and latest is not None:
        raise RuntimeError(
            "A successful Supabase sync already exists. Refusing a full upload; use "
            "--refresh --apply for incremental updates, or --reingest --apply after a "
            "schema change."
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
    sync_mode = (refresh_info or {}).get("mode", "incremental") if refresh_info else "initial"
    reingest = sync_mode == "reingest"
    # 전체 재스캔일 때만 "DB active - 새 Stage 4" 를 비활성화한다. 재사용 모드는
    # 예전처럼 언어 게이트 제외분만 내리고 DB 에만 있는 행은 보고만 한다.
    deactivate_missing = reingest and refresh_info.get("stage1_mode") == "full-scan"
    stage4_ids = sorted(row["model_id"] for row in stage4) if reingest else None
    if bundle_manifest is not None and model_ids_sha256(set(stage4_ids or ())) != bundle_manifest["model_ids_sha256"]:
        raise BundleError("적재하려는 Stage 4 모델 집합이 승인한 번들과 다르다")
    result: Dict[str, Any] = {
        "validation": validation,
        "evidence_validation": evidence_validation,
        "run_id": run_id,
        "apply": args.apply,
        "selected_pools": list(POOLS),
        "sync_mode": sync_mode,
        "changed_rows": len(selected_stage4),
        "removed_rows": len(removed_ids),
    }
    if reingest:
        result["reingest"] = refresh_info
    exit_code = 0
    if reingest:
        # 읽기 전용 조회. 쓰기 전에 판단해야 한도를 넘긴 뒤에 알게 되지 않는다.
        storage = db_storage()
        # 계약 레코드는 technical_metadata 와 source_provenance 에 새로 붙는 부분이다.
        contract_bytes = sum(
            len(json_text(stage2[row["model_id"]].get("contract")).encode("utf-8")) for row in selected_stage4
        )
        result["capacity"] = capacity_plan(
            storage, estimate_write_bytes(rows, evidence_rows, storage, contract_bytes)
        )
    if args.apply:
        if reingest and result["capacity"]["blocked"]:
            if args.report is not None:
                write_reingest_report(result, args.report)  # 멈춘 이유를 artifact 로 남긴다
            assert_capacity(result["capacity"])
        result["sync"] = apply_sync(
            rows,
            evidence_rows,
            run_id,
            args.batch_size,
            sync_mode=sync_mode,
            removed_ids=removed_ids,
            deactivate_missing=deactivate_missing,
            stage4_ids=stage4_ids,
            source_watermark=resolved_source_watermark(refresh_info),
            corpus_rows=len(stage2),
            extra_versions=(
                {
                    "stage1_mode": refresh_info["stage1_mode"],
                    "approved_dry_run_id": bundle_manifest["dry_run_run_id"],
                    "bundle_sha256": bundle_manifest["bundle_sha256"],
                    "model_ids_sha256": bundle_manifest["model_ids_sha256"],
                }
                if reingest and bundle_manifest is not None
                else {"stage1_mode": refresh_info["stage1_mode"]} if reingest else None
            ),
        )
        if "deactivation" in result["sync"]:
            result["deactivation"] = result["sync"]["deactivation"]
        promote_benchmark_state()
        # Only remove one-run queues after the database transaction has
        # succeeded. Persistent per-pool benchmark state remains intact.
        clear_incremental_artifacts()
    else:
        result["dry_run"] = {
            "rows": len(rows),
            "estimated_json_bytes": sum(len(json.dumps(row, ensure_ascii=False, default=str)) for row in rows),
            "db_write": False,
        }
        if reingest:
            # 읽기 전용 조회. apply 는 같은 계산을 쓰기 트랜잭션 안에서 다시 한다.
            plan = deactivation_plan(
                db_active_model_ids(), stage4_ids, removed_ids,
                deactivate_missing=deactivate_missing,
            )
            result["deactivation"] = plan
            result["dry_run"]["expected_source_watermark"] = resolved_source_watermark(refresh_info)
            if plan["guard"]["blocked"] or result["capacity"]["blocked"]:
                # 보고서는 끝까지 남기되 실행은 실패로 표시한다.
                exit_code = 3
    if bundle_manifest is not None:
        result["bundle"] = {key: bundle_manifest[key] for key in (
            "dry_run_run_id", "git_sha", "bundle_sha256", "model_ids_sha256", "model_count")}
    if args.report is not None:
        write_reingest_report(result, args.report)
    if args.bundle_dir is not None and reingest:
        manifest = write_reingest_bundle(
            args.bundle_dir,
            refresh_info=refresh_info,
            report=result,
            stage4_ids=stage4_ids or [],
            latest_sync_run_id=(previous or {}).get("run_id"),
        )
        print(json.dumps({"bundle": {"files": len(manifest["files"]),
                                     "model_ids_sha256": manifest["model_ids_sha256"]}}))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return exit_code



if __name__ == "__main__":
    raise SystemExit(main())
