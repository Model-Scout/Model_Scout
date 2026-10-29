#!/usr/bin/env python3
"""structured_constraint 질의의 조건 충족 여부를 규칙으로 판정한다.

lexical_exact와 달리 판정이 세 값이다. 조건 필드가 비어 있는 모델이 코퍼스의
약 39%(parameter_count)라 "조건을 만족한다"와 "조건을 어긴다"만으로는 결과를
설명할 수 없기 때문이다.

    True   조건을 만족함이 데이터로 확인됨
    False  조건을 어김이 데이터로 확인됨
    None   조건 값이 없어 판정 불가

이 구분이 중요한 이유는 현재 하드 필터가 None을 통과시키기 때문이다
(require_known_parameters=false). 커버리지 조사에서 후보 11,632개 중 4,031개
(35%)가 조건 값을 모르는 채 통과했고, sg_h004에서는 후보 15개 중 14개가
그런 경우였다. 이 지표는 그 양을 직접 센다.

조건은 질의 필드에서 읽는다. lexical_rules처럼 질의별로 손으로 적지 않는 이유는
structured_constraint 질의 24개 모두 조건이 필드에 채워져 있음을 확인했기
때문이다(max_parameters_billion / min_context_length / license_requirement / tasks).

라이선스 정책은 골든셋 README의 채점용 임시 정책을 그대로 쓴다. apache-2.0·mit
등은 상업 허용, 이름에 nc가 들어가면 위반, other·gemma·llama·미기재는 확인 필요다.
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence

# 상업 이용이 명확히 허용되는 라이선스.
COMMERCIAL_ALLOWED = {
    "apache-2.0", "mit", "bsd", "bsd-3-clause", "bsd-2-clause",
    "cc-by-4.0", "cc-by-3.0", "cc-by-sa-4.0", "cc0-1.0",
    "openrail", "bigscience-openrail-m", "openmdw-1.1",
    "gpl-3.0", "agpl-3.0", "lgpl-3.0", "artistic-2.0", "wtfpl", "unlicense",
}

# 비상업 표기. cc-by-nc-4.0, cc-by-nc-sa-2.0 등.
NON_COMMERCIAL_MARK = "nc"


def _meta(row: Mapping[str, Any]) -> Mapping[str, Any]:
    return row.get("filter_metadata") or {}


def license_state(row: Mapping[str, Any], requirement: Optional[str]) -> Optional[bool]:
    """상업 이용 가능 여부. 조건이 없으면 True, 판단할 수 없으면 None."""
    if requirement != "commercial":
        return True
    value = str(_meta(row).get("license") or "").strip().lower()
    if not value:
        return None
    if NON_COMMERCIAL_MARK in value.split("-"):
        return False
    if value in COMMERCIAL_ALLOWED:
        return True
    # other, gemma, llama3.x 등은 조건부라 모델 카드를 봐야 한다.
    return None


def numeric_state(value: Any, *, maximum: Any = None, minimum: Any = None) -> Optional[bool]:
    if value is None:
        return None
    if maximum is not None and value > maximum:
        return False
    if minimum is not None and value < minimum:
        return False
    return True


def task_state(row: Mapping[str, Any], tasks: Sequence[str]) -> Optional[bool]:
    if not tasks:
        return True
    meta = _meta(row)
    primary = meta.get("primary_task")
    if primary in tasks:
        return True
    if set(meta.get("matched_tasks") or []) & set(tasks):
        return True
    if primary is None and not meta.get("matched_tasks"):
        return None
    return False


def conditions_of(query: Mapping[str, Any]) -> Dict[str, Any]:
    """질의 필드에서 조건만 뽑는다. 값이 없는 조건은 넣지 않는다."""
    out: Dict[str, Any] = {}
    if query.get("tasks"):
        out["tasks"] = list(query["tasks"])
    if query.get("max_parameters_billion") is not None:
        out["max_parameters_billion"] = query["max_parameters_billion"]
    if query.get("min_context_length") is not None:
        out["min_context_length"] = query["min_context_length"]
    if query.get("license_requirement") == "commercial":
        out["license_requirement"] = "commercial"
    if query.get("korean_required"):
        out["korean_required"] = True
    return out


def evaluate(row: Mapping[str, Any], conditions: Mapping[str, Any]) -> Dict[str, Optional[bool]]:
    """조건별 판정. 값이 없으면 None으로 남긴다."""
    meta = _meta(row)
    states: Dict[str, Optional[bool]] = {}
    if "tasks" in conditions:
        states["task"] = task_state(row, conditions["tasks"])
    if "korean_required" in conditions:
        verified = meta.get("korean_verified")
        states["korean"] = True if verified is True else (None if verified is None else False)
    if "max_parameters_billion" in conditions:
        states["parameters"] = numeric_state(
            meta.get("parameter_count_billion"), maximum=conditions["max_parameters_billion"])
    if "min_context_length" in conditions:
        states["context"] = numeric_state(
            meta.get("context_length"), minimum=conditions["min_context_length"])
    if "license_requirement" in conditions:
        states["license"] = license_state(row, conditions["license_requirement"])
    return states


def verdict(row: Mapping[str, Any], conditions: Mapping[str, Any]) -> Optional[bool]:
    """전체 판정. 하나라도 위반이면 False, 하나라도 모르면 None, 전부 만족이면 True.

    위반이 판정 불가보다 우선한다. 50M 이하를 요구한 질의에 context를 모르는
    12B 모델이 왔다면, 모르는 값이 있어도 그 모델은 명백히 조건 위반이다.
    """
    states = evaluate(row, conditions)
    if not states:
        return True
    if any(state is False for state in states.values()):
        return False
    if any(state is None for state in states.values()):
        return None
    return True


def unknown_fields(row: Mapping[str, Any], conditions: Mapping[str, Any]) -> List[str]:
    return sorted(name for name, state in evaluate(row, conditions).items() if state is None)


def violated_fields(row: Mapping[str, Any], conditions: Mapping[str, Any]) -> List[str]:
    return sorted(name for name, state in evaluate(row, conditions).items() if state is False)


def score(
    ranked: Sequence[str],
    corpus: Mapping[str, Mapping[str, Any]],
    conditions: Mapping[str, Any],
    ks: Iterable[int] = (5, 10),
) -> Dict[str, float]:
    """top-k를 충족·위반·판정불가로 나눈 비율."""
    out: Dict[str, float] = {}
    for k in ks:
        head = [corpus[model_id] for model_id in ranked[:k] if model_id in corpus]
        if not head:
            out[f"cond_ok@{k}"] = 0.0
            out[f"cond_violation@{k}"] = 0.0
            out[f"cond_unknown@{k}"] = 0.0
            continue
        verdicts = [verdict(row, conditions) for row in head]
        total = len(verdicts)
        out[f"cond_ok@{k}"] = sum(1 for v in verdicts if v is True) / total
        out[f"cond_violation@{k}"] = sum(1 for v in verdicts if v is False) / total
        out[f"cond_unknown@{k}"] = sum(1 for v in verdicts if v is None) / total
    return out
