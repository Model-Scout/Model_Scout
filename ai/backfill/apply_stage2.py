#!/usr/bin/env python3
"""델타를 Stage 2에 적용해 병행 데이터셋을 만든다. 기존 파일은 건드리지 않는다.

출력은 ``ai/backfill/out/``에만 쓴다. ``ai/data/``의 원본은 읽기만 한다.
팀이 확인하고 승인하면 그때 교체한다.

무엇을 바꾸나
    model.parameter_count / parameter_count_billion (검증 high만)
    model.context_length (+ context_evidence 에 출처 추가)
    model.architectures / model.type
    model.metadata_status.{parameter_count,context_length}  known/unknown 갱신
    hardware.weights_only.*        high 파라미터가 생기면 VRAM 추정이 따라온다
    license                        비어 있던 경우만
    model.disk_size_gib            ★ 새 필드 (별도 제안)

무엇을 안 바꾸나
    이미 값이 있는 필드는 손대지 않는다. 덮어쓰기가 아니라 빈칸 채우기다.
    stage2_version 도 올리지 않는다. 올리면 08_sync_supabase 의 정합성 검증과
    Stage 3 재실행 판정에 걸린다. 대신 backfill 표시를 따로 남긴다.

    python ai/backfill/apply_stage2.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List

HERE = Path(__file__).resolve().parent
AI_ROOT = HERE.parent
DATA_DIR = AI_ROOT / "data"
OUT_DIR = HERE / "out"
DELTA_PATH = HERE / "delta.jsonl"
REPORT_PATH = HERE / "reports" / "apply_summary.json"

POOLS = ("core", "low_popularity")
BACKFILL_VERSION = 2

# 02_enrich_metadata.estimate_hardware 와 같은 식. 가중치만 고려한 추정치다.
BYTES_PER_PARAM = {"fp16_gib": 2.0, "int8_gib": 1.0, "int4_gib": 0.5}


def load_delta() -> Dict[str, Dict[str, Any]]:
    if not DELTA_PATH.exists():
        raise SystemExit(f"{DELTA_PATH} 없음. build_delta.py 를 먼저 실행하세요.")
    delta: Dict[str, Dict[str, Any]] = {}
    with DELTA_PATH.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                record = json.loads(line)
                delta[record["model_id"]] = record
    return delta


def weights_only(parameter_count: int) -> Dict[str, float]:
    gib = parameter_count / 2**30
    return {key: round(gib * factor, 2) for key, factor in BYTES_PER_PARAM.items()}


def apply_record(row: Dict[str, Any], record: Dict[str, Any]) -> List[str]:
    """한 행에 패치를 적용하고 무엇을 바꿨는지 돌려준다."""
    changed: List[str] = []
    model = row.setdefault("model", {})
    patches = record.get("patches") or {}

    entry = patches.get("parameter_count")
    quarantined: Dict[str, Any] = {}
    # GGUF의 total은 파일 헤더가 주는 1차 정보지만, 멀티모달·MoE·부분 변환본에서는
    # 전체 파라미터와 다를 수 있다. 검증이 medium인 값은 검색 필터/VRAM/임베딩에
    # 넣지 않는다. delta.jsonl에는 후보값과 사유를 남겨 사람이 후속 확인할 수 있다.
    if entry and entry.get("confidence") != "high" and model.get("parameter_count") in (None, ""):
        quarantined["parameter_count"] = {
            "proposed": entry.get("after"),
            "source": entry.get("source"),
            "confidence": entry.get("confidence"),
            "validation_notes": entry.get("validation_notes", []),
        }
    elif entry and model.get("parameter_count") in (None, ""):
        count = entry["after"]
        model["parameter_count"] = count
        model["parameter_count_billion"] = round(count / 1e9, 3)
        model.setdefault("metadata_status", {})["parameter_count"] = "known"
        changed.append("parameter_count")
        # 파라미터가 생기면 VRAM 추정이 따라온다. 이게 가장 큰 실익이다.
        hardware = row.setdefault("hardware", {})
        current = hardware.get("weights_only") or {}
        if not any(value for value in current.values()):
            estimate = weights_only(count)
            estimate["detected_quantization_gib"] = current.get("detected_quantization_gib")
            hardware["weights_only"] = estimate
            changed.append("hardware.weights_only")

    entry = patches.get("context_length")
    if entry and model.get("context_length") in (None, ""):
        model["context_length"] = entry["after"]
        model.setdefault("context_evidence", []).append(
            {"value": entry["after"], "source": entry["source"]}
        )
        model.setdefault("metadata_status", {})["context_length"] = "known"
        changed.append("context_length")

    entry = patches.get("architecture")
    if entry and not model.get("architectures"):
        model["architectures"] = entry["after"]
        changed.append("architectures")

    entry = patches.get("model_type")
    if entry and not model.get("type"):
        model["type"] = entry["after"]
        changed.append("model.type")

    entry = patches.get("license")
    if entry and not row.get("license"):
        row["license"] = entry["after"]
        changed.append("license")

    # 새 필드는 기존 필드 채우기와 섞지 않는다. 제안을 분리해 심사받기 위해서다.
    new_fields = record.get("new_fields") or {}
    if "disk_size_gib" in new_fields and model.get("disk_size_gib") is None:
        model["disk_size_gib"] = new_fields["disk_size_gib"]["after"]
        changed.append("disk_size_gib")

    if changed or quarantined:
        row["backfill"] = {
            "version": BACKFILL_VERSION,
            "fields": changed,
            "sources": {
                name: entry["source"] for name, entry in patches.items()
            },
            "confidence": {
                name: entry["confidence"] for name, entry in patches.items()
            },
            "moe_suspect": record.get("moe_suspect"),
        }
    if quarantined:
        row["backfill_review"] = quarantined
    return changed


def main() -> None:
    delta = load_delta()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    totals: Dict[str, int] = {}
    touched = moe = quarantined_parameters = 0
    per_pool: Dict[str, Dict[str, int]] = {}

    for pool in POOLS:
        source = DATA_DIR / f"hf_models_stage2_{pool}.jsonl"
        target = OUT_DIR / f"hf_models_stage2_{pool}.jsonl"
        rows_out: List[str] = []
        pool_touched = 0
        with source.open(encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                row = json.loads(line)
                record = delta.get(row["model_id"])
                if record:
                    changed = apply_record(row, record)
                    has_quarantine = bool(row.get("backfill_review"))
                    if changed or has_quarantine:
                        pool_touched += 1
                        touched += 1
                        if record.get("moe_suspect"):
                            moe += 1
                        for field in changed:
                            totals[field] = totals.get(field, 0) + 1
                    if has_quarantine and "parameter_count" in row["backfill_review"]:
                        quarantined_parameters += 1
                rows_out.append(json.dumps(row, ensure_ascii=False))
        target.write_text("\n".join(rows_out) + "\n", encoding="utf-8")
        per_pool[pool] = {"rows": len(rows_out), "patched": pool_touched}
        print(f"{pool:16s} {len(rows_out):5d}행  패치 {pool_touched:5d}  → {target.name}")

    print()
    print("필드별 적용 수")
    for field, count in sorted(totals.items(), key=lambda item: -item[1]):
        print(f"  {field:24s} {count:5d}")
    print()
    print(f"패치된/검토표시 모델 {touched}  (그중 MoE 의심 {moe})")
    print(f"검색·임베딩에서 보류한 medium 파라미터 {quarantined_parameters}")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps({
        "backfill_version": BACKFILL_VERSION,
        "models_patched": touched,
        "moe_suspects": moe,
        "parameter_count_quarantined": quarantined_parameters,
        "by_field": totals,
        "by_pool": per_pool,
        "note": "stage2_version은 올리지 않았다. medium 파라미터는 delta에만 보존하고 검색/임베딩에는 쓰지 않는다.",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"→ {OUT_DIR}")


if __name__ == "__main__":
    main()
