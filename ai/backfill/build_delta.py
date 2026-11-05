#!/usr/bin/env python3
"""받아둔 HF 응답에서 빈 필드를 채울 값을 뽑고, 출처와 신뢰도를 함께 기록한다.

이 파일이 검토 대상이다. 모델마다 "무엇을, 어떤 근거로, 얼마나 믿고" 채웠는지
적는다. 추측이 섞였는지 사람이 바로 볼 수 있어야 한다.

신뢰도 등급 — 프로젝트 원칙(충족 / 확인 필요 / 미확인)에 맞춘다
    high    HF가 실제 파일을 파싱해 내놓은 값
            gguf.total, gguf.context_length, gguf.architecture,
            safetensors.total, config.*
            → 지금 쓰고 있는 safetensors.parameters와 같은 등급이다
    medium  작성자가 선언한 base_model을 따라가 원본에서 상속한 값
            → derived_from에 원본을 적는다
    low     쓰지 않는다. 모델명에서 숫자를 긁는 것이 여기 해당한다
            "Mistral-Small-4-119B-GGUF"에서 정규식은 4B를 잡지만 실제는 119B다

MoE 경고
    MoE 모델은 전체 파라미터와 활성 파라미터가 다르다(24B-A2B = 전체 24B /
    활성 2B). VRAM은 전체 기준, 속도는 활성 기준이라 "3B 이하" 질의의 답이
    뒤집힌다. gguf.total이 어느 쪽인지 단정할 수 없으므로 의심되는 모델은
    moe_suspect로 표시해 사람이 판정하게 한다.

교차 검증
    기존 artifacts.gguf 플래그(파일명 패턴으로 판정)와 HF의 gguf 메타데이터가
    어긋나는 모델을 따로 센다. 둘 중 하나가 틀렸다는 신호다.

    python ai/backfill/build_delta.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

HERE = Path(__file__).resolve().parent
AI_ROOT = HERE.parent
RAW_DIR = HERE / "raw"
DELTA_PATH = HERE / "delta.jsonl"
REPORT_PATH = HERE / "reports" / "delta_summary.md"

# "24B-A2B", "8x7B", "A3B" — 활성 파라미터를 따로 표기하는 관례
MOE_PATTERN = re.compile(r"(\d+x\d+b|[-_]a\d+(?:\.\d+)?b)", re.IGNORECASE)
MOE_KEYS = ("expert_count", "expert_used_count", "n_expert", "num_experts")


def corpus_rows() -> List[Dict[str, Any]]:
    sys.path.insert(0, str(AI_ROOT / "test" / "golden" / "v2" / "tools"))
    import corpus_v2

    return corpus_v2.load_rows()


def load_raw(model_id: str) -> Optional[Dict[str, Any]]:
    safe = model_id.replace("/", "__")
    path = RAW_DIR / safe[:2].lower() / f"{safe}.json"
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    return None if "__error__" in payload else payload


# GGUF 헤더에 센티넬이 그대로 들어오는 경우가 있다. aya-23-8B-GGUF 의
# context_length 가 4294967295(2**32-1)로 왔는데 실제로는 8K다. 범위를 벗어난
# 값은 "모름"으로 두는 편이 틀린 값을 넣는 것보다 낫다.
SENTINELS = {0, -1, 2**16 - 1, 2**31 - 1, 2**32 - 1, 2**63 - 1}
CONTEXT_RANGE = (128, 16_777_216)            # 128 ~ 16M 토큰
PARAM_RANGE = (1_000_000, 2_000_000_000_000)  # 1M ~ 2T


def sane(value: Any, low: int, high: int) -> bool:
    return isinstance(value, int) and value not in SENTINELS and low <= value <= high


def pick_parameter_count(raw: Dict[str, Any]) -> Optional[Tuple[int, str, str]]:
    """(값, 출처, 신뢰도). 이름 파싱은 하지 않는다."""
    gguf = raw.get("gguf") or {}
    if sane(gguf.get("total"), *PARAM_RANGE):
        return gguf["total"], "huggingface_api.gguf.total", "high"
    safetensors = raw.get("safetensors") or {}
    if sane(safetensors.get("total"), *PARAM_RANGE):
        return safetensors["total"], "huggingface_api.safetensors.total", "high"
    parameters = safetensors.get("parameters")
    if isinstance(parameters, dict):
        total = sum(value for value in parameters.values() if isinstance(value, int))
        if sane(total, *PARAM_RANGE):
            return total, "huggingface_api.safetensors.parameters(sum)", "high"
    return None


def pick_context_length(raw: Dict[str, Any]) -> Optional[Tuple[int, str, str]]:
    gguf = raw.get("gguf") or {}
    if sane(gguf.get("context_length"), *CONTEXT_RANGE):
        return gguf["context_length"], "huggingface_api.gguf.context_length", "high"
    config = raw.get("config") or {}
    for key in ("max_position_embeddings", "n_positions", "max_sequence_length"):
        if sane(config.get(key), *CONTEXT_RANGE):
            return config[key], f"huggingface_api.config.{key}", "high"
    return None


def pick_architecture(raw: Dict[str, Any]) -> Optional[Tuple[Any, str, str]]:
    config = raw.get("config") or {}
    archs = config.get("architectures")
    if isinstance(archs, list) and archs:
        return archs, "huggingface_api.config.architectures", "high"
    gguf = raw.get("gguf") or {}
    if isinstance(gguf.get("architecture"), str) and gguf["architecture"]:
        return [gguf["architecture"]], "huggingface_api.gguf.architecture", "high"
    return None


def pick_model_type(raw: Dict[str, Any]) -> Optional[Tuple[str, str, str]]:
    config = raw.get("config") or {}
    if isinstance(config.get("model_type"), str) and config["model_type"]:
        return config["model_type"], "huggingface_api.config.model_type", "high"
    gguf = raw.get("gguf") or {}
    if isinstance(gguf.get("architecture"), str) and gguf["architecture"]:
        return gguf["architecture"], "huggingface_api.gguf.architecture", "high"
    return None


def pick_license(raw: Dict[str, Any]) -> Optional[Tuple[str, str, str]]:
    card = raw.get("cardData") or {}
    value = card.get("license")
    if isinstance(value, list):
        value = value[0] if value else None
    if isinstance(value, str) and value:
        return value, "huggingface_api.cardData.license", "high"
    return None


def disk_size_gib(raw: Dict[str, Any]) -> Optional[Tuple[float, str, str]]:
    """실제 파일 크기. '내 GPU에 들어가나'는 추정보다 이쪽이 정확하다."""
    siblings = raw.get("siblings") or []
    weights = [
        sibling for sibling in siblings
        if isinstance(sibling.get("size"), int)
        and sibling.get("rfilename", "").lower().endswith(
            (".gguf", ".safetensors", ".bin", ".pth", ".npz")
        )
    ]
    if not weights:
        return None
    # GGUF는 양자화별로 여러 파일이 있다. 가장 작은 것이 "최소 요구량"이다.
    smallest = min(sibling["size"] for sibling in weights)
    return round(smallest / 2**30, 2), "huggingface_api.siblings[].size(min)", "high"


def moe_suspect(model_id: str, raw: Dict[str, Any]) -> Optional[str]:
    if MOE_PATTERN.search(model_id):
        return f"model_id 패턴: {MOE_PATTERN.search(model_id).group(0)}"
    gguf = raw.get("gguf") or {}
    for key in MOE_KEYS:
        if key in gguf:
            return f"gguf.{key}={gguf[key]}"
    config = raw.get("config") or {}
    for key in MOE_KEYS:
        if key in config:
            return f"config.{key}={config[key]}"
    return None


PICKERS = (
    ("parameter_count", pick_parameter_count),
    ("context_length", pick_context_length),
    ("architecture", pick_architecture),
    ("model_type", pick_model_type),
    ("license", pick_license),
)


def main() -> None:
    rows = corpus_rows()
    records: List[Dict[str, Any]] = []
    stats: Dict[str, Dict[str, int]] = {name: {} for name, _ in PICKERS}
    stats["disk_size_gib"] = {}
    no_raw = still_empty = 0
    moe_rows: List[Dict[str, Any]] = []
    gguf_conflicts: List[str] = []

    for row in rows:
        model_id = row["model_id"]
        meta = row.get("filter_metadata") or {}
        raw = load_raw(model_id)
        if raw is None:
            continue

        # 교차 검증: 기존 artifacts.gguf(파일명 패턴)와 HF의 gguf 메타데이터
        has_gguf_meta = bool((raw.get("gguf") or {}).get("total"))
        flagged_gguf = bool((meta.get("artifacts") or {}).get("gguf"))
        if has_gguf_meta != flagged_gguf:
            gguf_conflicts.append(model_id)

        patches: Dict[str, Any] = {}
        for name, picker in PICKERS:
            current = meta.get(name)
            filled = current not in (None, "", [], {})
            if filled:
                continue
            found = picker(raw)
            if not found:
                continue
            value, source, confidence = found
            patches[name] = {
                "before": current,
                "after": value,
                "source": source,
                "confidence": confidence,
            }
            stats[name][source] = stats[name].get(source, 0) + 1

        # 새 필드. 기존 필드 채우기와 섞지 않도록 분리해서 기록한다.
        new_fields: Dict[str, Any] = {}
        size = disk_size_gib(raw)
        if size:
            value, source, confidence = size
            new_fields["disk_size_gib"] = {
                "after": value, "source": source, "confidence": confidence,
            }
            stats["disk_size_gib"][source] = stats["disk_size_gib"].get(source, 0) + 1

        if not patches and not new_fields:
            still_empty += 1
            continue

        record: Dict[str, Any] = {"model_id": model_id, "patches": patches}
        if new_fields:
            record["new_fields"] = new_fields

        reason = moe_suspect(model_id, raw)
        if reason and "parameter_count" in patches:
            record["moe_suspect"] = reason
            patches["parameter_count"]["confidence"] = "medium"
            patches["parameter_count"]["note"] = (
                "MoE 의심. gguf.total이 전체인지 활성인지 확인 필요"
            )
            moe_rows.append(record)
        records.append(record)

    with DELTA_PATH.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"델타 {len(records)}건  (조회했으나 채울 것 없음 {still_empty})")
    print()
    for name, by_source in stats.items():
        total = sum(by_source.values())
        if not total:
            continue
        print(f"{name}  +{total}")
        for source, count in sorted(by_source.items(), key=lambda item: -item[1]):
            print(f"    {count:5d}  {source}")
    print()
    print(f"⚠️ MoE 의심 (사람 확인 필요)         {len(moe_rows)}")
    print(f"⚠️ artifacts.gguf 와 HF 메타 불일치  {len(gguf_conflicts)}")
    print(f"→ {DELTA_PATH}")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps({
        "delta_records": len(records),
        "by_field": stats,
        "moe_suspects": [record["model_id"] for record in moe_rows],
        "gguf_flag_conflicts": gguf_conflicts[:200],
        "gguf_flag_conflict_total": len(gguf_conflicts),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
