#!/usr/bin/env python3
"""백필 Stage 2·4를 골든셋 v2의 판정 스냅샷에 반영한다.

백필 Stage 4에는 검색·필터용 구조화 메타데이터와 embedding_text만 있다. 반면
골든셋의 사람 판정에는 Stage 3 claim, benchmark, atomic evidence가 필요하다.
따라서 기존 Supabase 스냅샷의 의미·근거 데이터는 유지하고, 백필 결과의 기술
메타데이터와 filter_metadata만 병합한다.

이 도구는 로컬의 gitignore 대상 corpus_snapshot.jsonl과 BGE 인덱스를 재생성한다.
추적되는 것은 이 절차와 corpus_snapshot.meta.json뿐이다.

    cd ai
    ../.venv/bin/python test/golden/v2/tools/adopt_backfill.py
    ../.venv/bin/python test/golden/v2/tools/verify.py
"""

from __future__ import annotations

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List


V2 = Path(__file__).resolve().parents[1]
AI_ROOT = Path(__file__).resolve().parents[4]
BACKFILL = AI_ROOT / "backfill"
SNAPSHOT = V2 / "corpus_snapshot.jsonl"
META = V2 / "corpus_snapshot.meta.json"


def read_jsonl(paths: Iterable[Path]) -> Dict[str, Dict[str, Any]]:
    rows: Dict[str, Dict[str, Any]] = {}
    for path in paths:
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                row = json.loads(line)
                model_id = row["model_id"]
                if model_id in rows:
                    raise RuntimeError(f"중복 model_id: {model_id}")
                rows[model_id] = row
    return rows


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ensure_same_ids(name: str, expected: set[str], actual: set[str]) -> None:
    missing = expected - actual
    extra = actual - expected
    if missing or extra:
        raise RuntimeError(
            f"{name} model_id 집합 불일치: "
            f"missing={len(missing)}, extra={len(extra)}"
        )


def merge_row(
    original: Dict[str, Any],
    stage2: Dict[str, Any],
    stage4: Dict[str, Any],
) -> Dict[str, Any]:
    """원래의 semantic/evidence는 보존하고 백필된 결정론적 정보만 반영한다."""
    row = dict(original)

    technical = dict(row.get("technical_metadata") or {})
    for key in (
        "model",
        "hardware",
        "artifacts",
        "quantization",
        "runtime_compatibility",
        "license",
        "base_models",
        "datasets",
        "metrics",
    ):
        if key in stage2:
            technical[key] = stage2[key]
    row["technical_metadata"] = technical

    # 운영 검색이 보는 값은 백필 Stage 4와 한 글자도 같게 한다.
    row["filter_metadata"] = stage4["filter_metadata"]
    for key in (
        "source_pool",
        "candidate",
        "popularity",
        "task",
        "task_consistency",
        "document_hash",
        "embedding_model",
        "embedding_dimensions",
    ):
        if key in stage4:
            row[key] = stage4[key]

    # Stage 2에서 직접 보강된 구조화 정보도 원본 스냅샷과 맞춘다.
    for key in ("language", "family"):
        if key in stage2:
            row[key] = stage2[key]

    provenance = dict(row.get("source_provenance") or {})
    stage2_provenance = dict(provenance.get("stage2") or {})
    stage2_provenance["metadata_backfill"] = {
        "method": "hf_gguf_header_and_config",
        "stage2_output": "ai/backfill/out/hf_models_stage2_{pool}.jsonl",
    }
    provenance["stage2"] = stage2_provenance
    row["source_provenance"] = provenance
    return row


def copy_bge_index() -> None:
    source = BACKFILL / "index"
    destination = V2 / "index"
    destination.mkdir(parents=True, exist_ok=True)
    for name in ("bge_m3_doc_embeddings.npy", "bge_m3_doc_manifest.json"):
        source_path = source / name
        if not source_path.exists():
            raise FileNotFoundError(f"백필 BGE 인덱스 없음: {source_path}")
        shutil.copy2(source_path, destination / name)


def main() -> None:
    if not SNAPSHOT.exists():
        raise FileNotFoundError(f"기존 스냅샷 없음: {SNAPSHOT}")

    original = read_jsonl([SNAPSHOT])
    stage2 = read_jsonl([
        BACKFILL / "out" / "hf_models_stage2_core.jsonl",
        BACKFILL / "out" / "hf_models_stage2_low_popularity.jsonl",
    ])
    stage4 = read_jsonl([
        BACKFILL / "out" / "hf_models_stage4_core.jsonl",
        BACKFILL / "out" / "hf_models_stage4_low_popularity.jsonl",
    ])
    ids = set(original)
    ensure_same_ids("백필 Stage 2", ids, set(stage2))
    ensure_same_ids("백필 Stage 4", ids, set(stage4))

    rows = [merge_row(original[model_id], stage2[model_id], stage4[model_id])
            for model_id in sorted(ids)]
    with SNAPSHOT.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")

    old_meta = json.loads(META.read_text(encoding="utf-8"))
    stage4_report_path = BACKFILL / "reports" / "stage4_rebuild.json"
    stage4_report = json.loads(stage4_report_path.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).isoformat()
    old_meta.update({
        "source": "frozen Supabase active snapshot + ai/backfill Stage 2/4",
        "rows": len(rows),
        "metadata_variant": "backfill-v2-high-confidence-parameters",
        "backfill_adopted_at": now,
        "backfill": {
            "stage2_core_sha256": sha256(BACKFILL / "out" / "hf_models_stage2_core.jsonl"),
            "stage2_low_popularity_sha256": sha256(BACKFILL / "out" / "hf_models_stage2_low_popularity.jsonl"),
            "stage4_core_sha256": sha256(BACKFILL / "out" / "hf_models_stage4_core.jsonl"),
            "stage4_low_popularity_sha256": sha256(BACKFILL / "out" / "hf_models_stage4_low_popularity.jsonl"),
            "stage4_rebuild": (
                f"{stage4_report['vectors_new']} embeddings regenerated, "
                f"{stage4_report['vectors_reused']} reused"
            ),
            "parameter_policy": (
                "high-confidence 값만 filter_metadata/embedding에 반영; "
                "medium-confidence 값은 backfill_review에 격리"
            ),
            "note": "Stage 3 semantic claims and atomic evidence remain from the frozen Supabase snapshot.",
        },
    })
    META.write_text(json.dumps(old_meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    copy_bge_index()
    print(f"✅ 골든셋 v2 스냅샷을 백필 코퍼스 {len(rows)}행으로 동기화했습니다.")
    print("✅ Stage 3 의미·근거는 보존했고, Stage 2·4 기술/필터 정보와 BGE 인덱스를 교체했습니다.")


if __name__ == "__main__":
    main()
