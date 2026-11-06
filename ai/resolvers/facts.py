"""출처·신뢰도·상태를 다루는 공통 규칙.

데이터 계약(`contract/README.md` 2절)의 status/confidence 규칙을 코드로 옮긴 것이다.
등급을 임의로 매기지 못하게 생성자에서 막는다 — 추측이 고신뢰로 승격되는 것이
이 프로젝트에서 실제로 났던 사고다.
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional, Sequence

SENTINELS = {0, -1, 2 ** 16 - 1, 2 ** 31 - 1, 2 ** 32 - 1, 2 ** 63 - 1}
CONTEXT_RANGE = (128, 16_777_216)
PARAM_RANGE = (1_000_000, 2_000_000_000_000)

SOURCE_PREFIXES = (
    "hf_api", "hf_file", "hf_blob", "model_card",
    "readme", "official_doc", "derived_from", "config",
)

# status → 허용되는 confidence. 계약 README의 표와 같아야 한다.
_CONFIDENCE_FOR = {
    "verified": "high",
    "documented": "medium",
    "inferred": "low",
    "conflict": "none",
    "unknown": "none",
    "not_applicable": "none",
}
_NEEDS_SOURCE = {"verified", "documented", "inferred"}

# 품질 하락 검사용 순위. validate.check_regression과 같은 값이어야 한다.
RANK = {"verified": 4, "documented": 3, "inferred": 2, "not_applicable": 1, "conflict": 0, "unknown": 0}


def sane_int(value: Any, low: int, high: int) -> bool:
    """센티넬과 범위를 걸러낸다.

    GGUF 헤더는 "모름"을 2³²−1 같은 값으로 적는다. 그대로 받으면 컨텍스트
    42억 토큰짜리 모델이 생긴다.
    """
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
        and value not in SENTINELS
        and low <= value <= high
    )


def fact(status: str, source: Sequence[str] = (), note: Optional[str] = None,
         retrieved_at: Optional[str] = None) -> Dict[str, Any]:
    """provenance.fields 한 항목을 만든다. confidence는 status가 결정한다."""
    if status not in _CONFIDENCE_FOR:
        raise ValueError(f"알 수 없는 status: {status}")
    sources = list(source)
    for item in sources:
        if not any(item.startswith(prefix + ":") for prefix in SOURCE_PREFIXES):
            raise ValueError(f"출처 접두사가 없다: {item!r} (허용: {SOURCE_PREFIXES})")
    if status in _NEEDS_SOURCE and not sources:
        raise ValueError(f"status={status}는 출처가 있어야 한다")
    if status not in _NEEDS_SOURCE and sources:
        raise ValueError(f"status={status}인데 출처가 있다: {sources}")
    entry: Dict[str, Any] = {
        "status": status,
        "confidence": _CONFIDENCE_FOR[status],
        "source": sources,
        "retrieved_at": retrieved_at,
    }
    if note:
        entry["note"] = note
    return entry


def unknown(note: Optional[str] = None) -> Dict[str, Any]:
    return fact("unknown", (), note)


def not_applicable(note: Optional[str] = None) -> Dict[str, Any]:
    return fact("not_applicable", (), note)


class Resolution:
    """값 하나와 그 출처. 여러 후보 중에서 고른 결과를 담는다."""

    __slots__ = ("value", "entry", "conflict_candidates")

    def __init__(self, value: Any, entry: Dict[str, Any],
                 conflict_candidates: Optional[List[Dict[str, Any]]] = None) -> None:
        self.value = value
        self.entry = entry
        self.conflict_candidates = conflict_candidates or []

    @property
    def status(self) -> str:
        return self.entry["status"]

    def __repr__(self) -> str:  # pragma: no cover
        return f"Resolution({self.value!r}, {self.entry['status']})"


def pick(candidates: Iterable[Dict[str, Any]], *, tolerance: float = 0.0,
         unknown_note: Optional[str] = None) -> Resolution:
    """후보들 중 가장 믿을 만한 값을 고르고, 같은 등급이 서로 다르면 conflict로 둔다.

    후보는 {"value", "status", "source"} 꼴이다. 등급이 높은 순으로 보고, 최고
    등급 안에서 값이 갈리면 값을 쓰지 않는다. **틀린 값으로 필터를 통과시키는
    것이 탈락보다 나쁘다.**

    ``tolerance``는 수치 후보의 허용 상대 오차다. 파라미터 수는 출처마다
    임베딩 레이어 포함 여부가 달라 1% 안쪽으로 어긋나는 일이 흔하다. 그걸
    conflict로 보면 정상 모델이 대량으로 탈락한다.
    """
    usable = [c for c in candidates if c.get("value") is not None]
    if not usable:
        return Resolution(None, unknown(unknown_note))

    best_rank = max(RANK[c["status"]] for c in usable)
    top = [c for c in usable if RANK[c["status"]] == best_rank]

    first = top[0]["value"]
    differing = []
    for candidate in top[1:]:
        value = candidate["value"]
        if value == first:
            continue
        if (
            tolerance
            and isinstance(value, (int, float))
            and isinstance(first, (int, float))
            and max(abs(value), abs(first)) > 0
            and abs(value - first) / max(abs(value), abs(first)) <= tolerance
        ):
            continue
        differing.append(candidate)

    if differing:
        return Resolution(
            None,
            fact("conflict", (), "같은 등급의 출처가 다른 값을 말한다"),
            [{"value": c["value"], "source": c["source"][0]} for c in top],
        )

    sources: List[str] = []
    for candidate in top:
        for item in candidate["source"]:
            if item not in sources:
                sources.append(item)
    return Resolution(first, fact(top[0]["status"], sources, top[0].get("note")))
