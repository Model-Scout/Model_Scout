#!/usr/bin/env python3
"""lexical_exact 질의의 요구사항을 규칙으로 판정한다.

이 유형의 질의는 "맞다/틀리다"를 사람 판정 없이 가릴 수 있다. 중국어→한국어를
요구한 질의에 한국어→중국어 모델이 나오면, 누가 점수를 매기지 않아도 틀렸다.
그래서 Recall(판정된 라벨에 의존)과 달리 라벨 공백에 흔들리지 않는다.

질의 22개는 세 종류로 나뉘고 신호가 서로 다르다.

    direction  10개  translation_pairs는 코퍼스의 0.6%만 채워져 있어 이름과
                     다국어 모델(languages에 양쪽 포함)까지 함께 본다.
    format      7개  artifacts 플래그에 ct2/openvino 칸이 없어 이름이 필요하다.
    family      5개  이름과 canonical이 거의 일치해 이름만으로 충분하다.

요구사항은 질의문에서 추출하지 않고 여기에 명시한다. 추출기의 성능이
검색 지표에 섞여 들어가는 것을 막기 위해서다.
"""

from __future__ import annotations

import re
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Set

# 번역으로 볼 task. 다국어 모델이 방향을 지원하는지 볼 때 쓴다.
TRANSLATION_TASKS = {"translation", "text2text-generation", "text-generation"}

# model_id 안의 방향 표기. `opus-mt-tc-big-en-ko`, `aihub-ja-ko-translator` 등.
NAME_PAIR_PATTERN = re.compile(r"(?:^|[-_./])([a-z]{2})[-_]([a-z]{2})(?=$|[-_./])")
ISO_CODES = {"ko", "en", "ja", "zh", "fr", "de", "es", "ru"}

# 형식별 신호. artifacts 플래그가 없는 형식은 이름으로만 찾는다.
FORMAT_RULES: Dict[str, Dict[str, str]] = {
    "gguf": {"artifact": "gguf", "name": r"gguf"},
    "onnx": {"artifact": "onnx", "name": r"onnx"},
    "mlx": {"variant": "mlx", "name": r"(?:^|[-_./])mlx(?:$|[-_./])"},
    "awq": {"variant": "awq", "name": r"(?:^|[-_./])awq(?:$|[-_./])"},
    "ct2": {"name": r"ct2|faster[-_]whisper|ctranslate"},
    "openvino": {"name": r"openvino|(?:^|[-_./])ov(?:$|[-_./])"},
}

# 질의별 요구사항. kind 외의 키는 kind마다 다르다.
REQUIREMENTS: Dict[str, Dict[str, Any]] = {
    # --- direction: source -> target 번역 ---
    "sg_g002": {"kind": "direction", "source": "ja", "target": "ko"},
    "sg_g003": {"kind": "direction", "source": "ja", "target": "ko"},
    "sg_g005": {"kind": "direction", "source": "en", "target": "ko"},
    "sg_h012": {"kind": "direction", "source": "ko", "target": "en"},
    "sg_h013": {"kind": "direction", "source": "en", "target": "ko"},
    "sg_h051": {"kind": "direction", "source": "ja", "target": "ko"},
    "sg_h054": {"kind": "direction", "source": "zh", "target": "ko"},
    "sg_h055": {"kind": "direction", "source": "en", "target": "ko"},
    "sg_h073": {"kind": "direction", "source": "ko", "target": "zh"},
    # ko->fr 과 ko->de 중 하나만 맞아도 된다.
    "sg_h074": {"kind": "direction", "source": "ko", "target": ["fr", "de"]},
    # --- format: 실행 형식과 용도 ---
    "sg_h049": {"kind": "format", "format": "gguf",
                "tasks": ["feature-extraction", "sentence-similarity"]},
    "sg_h075": {"kind": "format", "format": "gguf", "tasks": ["text-generation"]},
    "sg_h077": {"kind": "format", "format": "ct2",
                "tasks": ["automatic-speech-recognition"]},
    "sg_h078": {"kind": "format", "format": "onnx",
                "tasks": ["feature-extraction", "sentence-similarity"]},
    "sg_h079": {"kind": "format", "format": "mlx", "tasks": ["text-generation"]},
    "sg_h080": {"kind": "format", "format": "awq", "tasks": ["text-generation"]},
    "sg_h165": {"kind": "format", "format": "openvino",
                "tasks": ["automatic-speech-recognition"]},
    # --- family: 계열·베이스 모델 ---
    "sg_h076": {"kind": "family", "pattern": r"koelectra",
                "tasks": ["text-classification"]},
    "sg_h081": {"kind": "family", "pattern": r"klue[-_./]?roberta|roberta[-_./]?klue",
                "tasks": ["feature-extraction", "sentence-similarity"]},
    "sg_h082": {"kind": "family", "pattern": r"kanana", "tasks": ["image-text-to-text"]},
    "sg_h083": {"kind": "family", "pattern": r"kobart", "tasks": ["summarization"]},
    "sg_h166": {"kind": "family", "pattern": r"(?:^|[-_./])midm", "tasks": ["text-generation"]},
}


def _meta(row: Mapping[str, Any]) -> Mapping[str, Any]:
    return row.get("filter_metadata") or {}


def _as_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    return list(value)


# ---------------------------------------------------------------- direction


def explicit_pairs(row: Mapping[str, Any]) -> Set[str]:
    """모델이 밝힌 방향. 선언된 translation_pairs와 이름에서 읽은 것을 합친다."""
    pairs = {str(pair).lower() for pair in _as_list(_meta(row).get("translation_pairs"))}
    for source, target in NAME_PAIR_PATTERN.findall(str(row.get("model_id", "")).lower()):
        if source in ISO_CODES and target in ISO_CODES and source != target:
            pairs.add(f"{source}-{target}")
    return pairs


def _covers_multilingual(row: Mapping[str, Any], source: str, targets: Sequence[str]) -> bool:
    """쌍 표기가 없는 다국어 번역 모델(NLLB, mBART 등)을 인정한다."""
    meta = _meta(row)
    if meta.get("primary_task") not in TRANSLATION_TASKS:
        return False
    languages = {str(code).lower() for code in _as_list(meta.get("languages"))}
    return source in languages and any(target in languages for target in targets)


def direction_match(row: Mapping[str, Any], source: str, targets: Sequence[str]) -> bool:
    pairs = explicit_pairs(row)
    if any(f"{source}-{target}" in pairs for target in targets):
        return True
    return _covers_multilingual(row, source, targets)


def direction_violation(row: Mapping[str, Any], source: str, targets: Sequence[str]) -> bool:
    """역방향 전용 모델인가. 양방향을 다 하는 다국어 모델은 위반이 아니다."""
    pairs = explicit_pairs(row)
    if not pairs:
        return False
    if any(f"{source}-{target}" in pairs for target in targets):
        return False
    return any(f"{target}-{source}" in pairs for target in targets)


# ------------------------------------------------------------------- format


def format_match(row: Mapping[str, Any], key: str) -> bool:
    rule = FORMAT_RULES[key]
    meta = _meta(row)
    if rule.get("artifact") and (meta.get("artifacts") or {}).get(rule["artifact"]):
        return True
    if rule.get("variant") and rule["variant"] in _as_list(meta.get("variant_types")):
        return True
    return bool(re.search(rule["name"], str(row.get("model_id", "")).lower()))


# ------------------------------------------------------------------- family


def family_match(row: Mapping[str, Any], pattern: str) -> bool:
    regex = re.compile(pattern)
    if regex.search(str(row.get("model_id", "")).lower()):
        return True
    canonical = str(_meta(row).get("canonical_model_id") or "").lower()
    return bool(regex.search(canonical))


# -------------------------------------------------------------------- 판정


def satisfies(row: Mapping[str, Any], requirement: Mapping[str, Any]) -> bool:
    """이 모델이 질의의 어휘 요구를 만족하는가. task 조건이 있으면 함께 본다."""
    kind = requirement["kind"]
    if kind == "direction":
        ok = direction_match(row, requirement["source"], _as_list(requirement["target"]))
    elif kind == "format":
        ok = format_match(row, requirement["format"])
    elif kind == "family":
        ok = family_match(row, requirement["pattern"])
    else:
        raise ValueError(f"알 수 없는 요구 유형: {kind}")
    if not ok:
        return False
    tasks = _as_list(requirement.get("tasks"))
    if tasks and _meta(row).get("primary_task") not in tasks:
        return False
    return True


def violates(row: Mapping[str, Any], requirement: Mapping[str, Any]) -> bool:
    """명백히 반대인 결과인가. 지금은 번역 방향만 위반을 정의할 수 있다."""
    if requirement["kind"] != "direction":
        return False
    return direction_violation(row, requirement["source"], _as_list(requirement["target"]))


def score(
    ranked: Sequence[str],
    corpus: Mapping[str, Mapping[str, Any]],
    requirement: Mapping[str, Any],
    ks: Iterable[int] = (5, 10),
) -> Dict[str, float]:
    """top-k 중 요구를 만족한 비율과 역방향이 섞인 비율."""
    out: Dict[str, float] = {}
    for k in ks:
        head = [corpus[model_id] for model_id in ranked[:k] if model_id in corpus]
        if not head:
            out[f"lex_match@{k}"] = 0.0
            out[f"lex_violation@{k}"] = 0.0
            continue
        out[f"lex_match@{k}"] = sum(satisfies(row, requirement) for row in head) / len(head)
        out[f"lex_violation@{k}"] = sum(violates(row, requirement) for row in head) / len(head)
    return out


def requirement_for(query_id: str) -> Optional[Dict[str, Any]]:
    return REQUIREMENTS.get(query_id)
