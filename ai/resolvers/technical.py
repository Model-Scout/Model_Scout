"""파라미터 수·컨텍스트·아키텍처·dtype을 출처 우선순위로 결정한다.

기존 ``02_enrich_metadata.extract_parameter_count()``는 한 곳만 봤다.

    safetensors = safe_get(info, "safetensors", None)
    if safetensors is None:
        return None          # 여기서 끝난다

GGUF 전용 레포에는 safetensors가 없다. 그래서 파라미터 수를 모르는 모델이
1,527개(39.4%) 생겼다. HF API는 같은 응답에 ``gguf``를 돌려준다.

    "gguf": {"total": 27009346304, "architecture": "gemma3", "context_length": 131072}

둘 다 **HF가 실제 파일 헤더를 파싱해 내놓은 값**이다. 등급이 같다.

MoE
---
전체 파라미터와 활성 파라미터가 다르다(24B-A2B = 전체 24B / 활성 2B). VRAM은
전체 기준, 속도는 활성 기준이라 "3B 이하" 질의의 답이 뒤집힌다. ``gguf.total``이
어느 쪽인지 응답만으로 단정할 수 없으므로 의심되는 모델은 conflict로 둔다.

모델명에서 숫자를 긁지 않는다
---------------------------
``Mistral-Small-4-119B-GGUF``에서 정규식은 4B를 잡지만 실제는 119B다. 이름은
어떤 신뢰 등급도 아니다. MoE 의심 판정에만 쓰고 값으로는 쓰지 않는다.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional

from . import facts

# "24B-A2B", "8x7B", "A3B" — 활성 파라미터를 따로 표기하는 관례
MOE_NAME = re.compile(r"(\d+x\d+b|[-_.]a\d+(?:\.\d+)?b)", re.IGNORECASE)
MOE_CONFIG_KEYS = (
    "num_experts", "num_local_experts", "n_experts", "expert_count",
    "num_experts_per_tok", "n_expert_used", "expert_used_count",
)

# 멀티모달 모델은 torch_dtype과 컨텍스트를 하위 섹션에 둔다.
# 02_enrich_metadata.NESTED_CONFIG_KEYS와 같은 목록이어야 한다 — 최상위만 보면
# 기존에 채워져 있던 dtype을 잃는다(실측: 19.1% → 13.1%로 떨어졌다).
NESTED_CONFIG_KEYS = ("text_config", "language_config", "decoder", "llm_config")

CONTEXT_CONFIG_KEYS = (
    "max_position_embeddings",
    "n_positions",
    "max_sequence_length",
    "max_seq_len",
)

# safetensors.parameters 의 dtype 키 → 계약의 dtype 표기
DTYPE_NAMES = {
    "BF16": "bfloat16", "F16": "float16", "FP16": "float16",
    "F32": "float32", "FP32": "float32", "F64": "float64",
    "I8": "int8", "U8": "uint8", "I16": "int16", "I32": "int32", "I64": "int64",
    "F8_E4M3": "float8", "F8_E5M2": "float8",
}


def _config(raw: Dict[str, Any], config_json: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """API 응답의 ``config``와 내려받은 ``config.json``을 합친다.

    API가 architectures·model_type·tokenizer_config를 이미 준다. config.json
    다운로드는 거기 없는 키(max_position_embeddings, torch_dtype, 전문가 수)
    때문에만 필요하다.
    """
    merged: Dict[str, Any] = {}
    merged.update(raw.get("config") or {})
    merged.update(config_json or {})
    return merged


def _sections(config: Dict[str, Any]) -> List[Dict[str, Any]]:
    """최상위와 중첩 섹션을 순서대로. 최상위가 먼저다."""
    out = [config]
    for key in NESTED_CONFIG_KEYS:
        value = config.get(key)
        if isinstance(value, dict):
            out.append(value)
    return out


def _from_sections(config: Dict[str, Any], keys, low: int, high: int):
    """중첩 섹션까지 보며 첫 유효 값을 찾는다. (값, '경로')"""
    for index, section in enumerate(_sections(config)):
        prefix = "" if index == 0 else f"{NESTED_CONFIG_KEYS[index - 1]}."
        for key in keys:
            if facts.sane_int(section.get(key), low, high):
                return section[key], f"{prefix}{key}"
    return None, None


def is_moe(raw: Dict[str, Any], config: Dict[str, Any]) -> bool:
    model_id = raw.get("id") or raw.get("modelId") or ""
    if any(config.get(key) for key in MOE_CONFIG_KEYS):
        return True
    architecture = " ".join(config.get("architectures") or []) + " " + str(config.get("model_type") or "")
    if "moe" in architecture.lower():
        return True
    return bool(MOE_NAME.search(model_id))


def _config_dtype(config: Dict[str, Any]):
    """``torch_dtype``/``dtype``을 중첩 섹션까지 찾는다. (값, '경로') 또는 None."""
    for index, section in enumerate(_sections(config)):
        prefix = "" if index == 0 else f"{NESTED_CONFIG_KEYS[index - 1]}."
        for key in ("torch_dtype", "dtype"):
            value = section.get(key)
            if value:
                return DTYPE_NAMES.get(str(value).upper(), str(value).lower()), f"{prefix}{key}"
    return None


def resolve(
    raw: Dict[str, Any],
    config_json: Optional[Dict[str, Any]] = None,
    *,
    retrieved_at: Optional[str] = None,
) -> Dict[str, Any]:
    """계약의 ``technical`` 그룹과 provenance·conflicts를 만든다."""
    config = _config(raw, config_json)
    gguf = raw.get("gguf") or {}
    safetensors = raw.get("safetensors") or {}
    conflicts: List[Dict[str, Any]] = []
    provenance: Dict[str, Any] = {}

    def record(field: str, resolution: facts.Resolution) -> Any:
        provenance[field] = dict(resolution.entry, retrieved_at=retrieved_at)
        if resolution.conflict_candidates:
            conflicts.append({"field": field, "candidates": resolution.conflict_candidates})
        return resolution.value

    # ── architecture / model_type ──────────────────────────────────────────
    # gguf.architecture는 **경쟁 후보가 아니라 대체 출처**다. 두 값은 어휘가
    # 다르다: config는 클래스 이름("Qwen3_5ForConditionalGeneration"), gguf는
    # 소문자 계열명("qwen35")이다. 같은 등급의 경쟁 후보로 넣으면 같은 모델을
    # 두 이름으로 부른 것이 conflict가 된다 — 실측 56개가 전부 그랬다.
    # config가 있으면 그것만 쓰고, 없을 때만 gguf로 내려간다.
    if config.get("architectures"):
        architecture_candidates = [{"value": list(config["architectures"]), "status": "verified",
                                    "source": ["hf_api:config.architectures"]}]
    elif gguf.get("architecture"):
        architecture_candidates = [{"value": [gguf["architecture"]], "status": "verified",
                                    "source": ["hf_api:gguf.architecture"],
                                    "note": "config.architectures가 없어 GGUF 헤더의 계열명을 쓴다. "
                                            "클래스 이름이 아니라 소문자 계열명이다"}]
    else:
        architecture_candidates = []
    architecture = record("technical.architecture", facts.pick(
        architecture_candidates,
        unknown_note="config.architectures와 gguf.architecture가 둘 다 없다")) or []

    if config.get("model_type"):
        type_candidates = [{"value": config["model_type"], "status": "verified",
                            "source": ["hf_api:config.model_type"]}]
    elif gguf.get("architecture"):
        type_candidates = [{"value": gguf["architecture"], "status": "verified",
                            "source": ["hf_api:gguf.architecture"],
                            "note": "config.model_type이 없어 GGUF 헤더의 계열명을 쓴다"}]
    else:
        type_candidates = []
    model_type = record("technical.model_type", facts.pick(
        type_candidates, unknown_note="config.model_type과 gguf.architecture가 둘 다 없다"))

    # ── parameter_count ───────────────────────────────────────────────────
    low, high = facts.PARAM_RANGE
    st_total = safetensors.get("total")
    gg_total = gguf.get("total")
    moe = is_moe(raw, config)

    candidates = []
    if facts.sane_int(st_total, low, high):
        candidates.append({"value": st_total, "status": "verified",
                           "source": ["hf_api:safetensors.total"]})
    if facts.sane_int(gg_total, low, high):
        # MoE에서는 gguf.total이 전체인지 활성인지 단정할 수 없다. safetensors가
        # 함께 있으면 그쪽을 쓰고, GGUF만 있으면 아래에서 conflict로 처리한다.
        candidates.append({"value": gg_total, "status": "verified",
                           "source": ["hf_api:gguf.total"]})

    if moe and not facts.sane_int(st_total, low, high) and facts.sane_int(gg_total, low, high):
        total = None
        provenance["technical.parameter_count_total"] = dict(
            facts.fact("conflict", (),
                       f"MoE 의심 모델이고 safetensors가 없다. gguf.total={gg_total}이 "
                       f"전체인지 활성인지 응답만으로 단정할 수 없다"),
            retrieved_at=retrieved_at,
        )
        conflicts.append({
            "field": "technical.parameter_count_total",
            "candidates": [
                {"value": gg_total, "source": "hf_api:gguf.total"},
                {"value": None, "source": "config:num_experts_per_tok"},
            ],
        })
        provenance["technical.parameter_count_active"] = dict(
            facts.unknown("total이 미해결이라 active를 정할 수 없다"), retrieved_at=retrieved_at
        )
        active = None
    else:
        # 출처마다 임베딩 레이어 포함 여부가 달라 1% 안쪽으로 어긋나는 일이 흔하다.
        total = record("technical.parameter_count_total",
                       facts.pick(candidates, tolerance=0.01,
                                  unknown_note="safetensors.total과 gguf.total이 둘 다 없다"))
        if total is None:
            provenance["technical.parameter_count_active"] = dict(
                facts.unknown("total을 모른다"), retrieved_at=retrieved_at)
            active = None
        elif moe:
            per_tok = config.get("num_experts_per_tok") or config.get("n_expert_used")
            experts = config.get("num_experts") or config.get("num_local_experts")
            if isinstance(per_tok, int) and isinstance(experts, int) and 0 < per_tok <= experts:
                active = int(total * per_tok / experts)
                provenance["technical.parameter_count_active"] = dict(
                    facts.fact("inferred", ["config:num_experts_per_tok"],
                               f"전체 {total} × {per_tok}/{experts} 전문가. 어텐션·임베딩은 "
                               f"항상 활성이므로 실제 활성 파라미터는 이보다 크다"),
                    retrieved_at=retrieved_at)
            else:
                active = None
                provenance["technical.parameter_count_active"] = dict(
                    facts.unknown("MoE인데 전문가 수를 모른다"), retrieved_at=retrieved_at)
        else:
            active = total
            provenance["technical.parameter_count_active"] = dict(
                facts.fact("verified", provenance["technical.parameter_count_total"]["source"],
                           "MoE가 아니므로 total과 같다"),
                retrieved_at=retrieved_at)

    # ── context_length ────────────────────────────────────────────────────
    low_ctx, high_ctx = facts.CONTEXT_RANGE
    ctx_candidates = []
    ctx_value, ctx_path = _from_sections(config, CONTEXT_CONFIG_KEYS, low_ctx, high_ctx)
    if ctx_value is not None:
        ctx_candidates.append({"value": ctx_value, "status": "verified",
                               "source": [f"hf_api:config.{ctx_path}"]})
    if facts.sane_int(gguf.get("context_length"), low_ctx, high_ctx):
        ctx_candidates.append({"value": gguf["context_length"], "status": "verified",
                               "source": ["hf_api:gguf.context_length"]})
    tokenizer = config.get("tokenizer_config") or {}
    if facts.sane_int(tokenizer.get("model_max_length"), low_ctx, high_ctx):
        ctx_candidates.append({"value": tokenizer["model_max_length"], "status": "documented",
                               "source": ["hf_api:config.tokenizer_config.model_max_length"]})
    context_length = record("technical.context_length", facts.pick(
        ctx_candidates,
        unknown_note="config의 컨텍스트 키와 gguf.context_length가 둘 다 없거나 센티넬이다"))

    # ── dtype ─────────────────────────────────────────────────────────────
    parameters = safetensors.get("parameters") or {}
    dtype = None
    if isinstance(parameters, dict) and parameters:
        # 가장 많은 파라미터를 차지하는 dtype이 그 모델의 dtype이다.
        dominant = max(parameters.items(), key=lambda item: item[1] if isinstance(item[1], int) else 0)[0]
        dtype = DTYPE_NAMES.get(str(dominant).upper(), str(dominant).lower())
        provenance["technical.dtype"] = dict(
            facts.fact("verified", ["hf_api:safetensors.parameters"]), retrieved_at=retrieved_at)
    elif _config_dtype(config):
        dtype, dtype_path = _config_dtype(config)
        provenance["technical.dtype"] = dict(
            facts.fact("verified", [f"hf_api:config.{dtype_path}"]), retrieved_at=retrieved_at)
    elif (raw.get("gguf") or {}).get("total"):
        provenance["technical.dtype"] = dict(
            facts.not_applicable("GGUF는 파일별 양자화 레이블이 dtype 역할을 한다"),
            retrieved_at=retrieved_at)
    else:
        provenance["technical.dtype"] = dict(
            facts.unknown("safetensors.parameters와 config.torch_dtype이 둘 다 없다"),
            retrieved_at=retrieved_at)

    return {
        "technical": {
            "architecture": architecture,
            "model_type": model_type,
            "parameter_count_total": total,
            "parameter_count_active": active,
            "context_length": context_length,
            "dtype": dtype,
        },
        "provenance": provenance,
        "conflicts": conflicts,
        "is_moe": moe,
    }
