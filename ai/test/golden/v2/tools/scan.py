"""eligible 전수를 5단계 규칙으로 스캔해 사람이 볼 것만 추린다.

검색기를 판정에 쓰지 않는다. dense 점수나 BM25 순위로 후보를 고르면 그 검색기를
평가할 수 없게 된다(순환 평가). 그래서 결정론적 문자열·구조 규칙만 쓰고, 순위를
만들지 않고 전수를 본다.

규칙은 확실하지 않으므로 느슨하게 둔다. 조금이라도 걸리면 사람에게 올린다.

    🚩 flag     조건에 걸리는 근거를 찾음        → 정답 맞나?   (정밀도)
    ⚠️ unsure   걸러냈지만 근거가 약함           → 진짜 아닌가? (재현율)
    ✅ reject   어느 단계도 걸리지 않음          → 분류 이유만 읽고 넘김

⚠️ 더미가 재현율 방어선이다. 빠진 정답은 걸러낸 쪽에 숨어 있으므로 플래그만
보면 영원히 못 찾는다.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

# 단계별로 보는 곳. 뒤 단계로 갈수록 "어려운" 판정이다.
STAGE_NAMES = {
    1: "model_id",
    2: "filter_metadata",
    3: "semantic_metadata",
    4: "benchmark_metadata",
    5: "evidence",
}


def _text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False)


def _flags(value: Any) -> str:
    """불린 맵에서 참인 키만 남긴다.

    ``artifacts``는 ``{"gguf": false, "onnx": false, "safetensors": true}`` 꼴이다.
    JSON으로 그냥 덤프하면 값이 false인 키 이름까지 본문에 들어가서, "GGUF 형식"
    질의가 GGUF를 안 가진 모델에도 걸린다(요약 후보 14개가 전부 걸렸다). 참인
    키만 남겨 형식·양자화 질의가 실제 보유 여부를 보게 한다.
    """
    if not isinstance(value, dict):
        return _text(value)
    parts = []
    for key, inner in value.items():
        if inner is True:
            parts.append(str(key))
        elif isinstance(inner, dict):
            parts.append(_flags(inner))
        elif inner not in (False, None):
            parts.append(f"{key} {_text(inner)}")
    return " ".join(parts)


def stage_haystacks(row: Dict[str, Any]) -> Dict[int, str]:
    """각 단계가 보는 텍스트. 단계를 섞지 않는다 — 난이도 판정에 쓰기 때문이다."""
    filter_metadata = row.get("filter_metadata") or {}
    semantic = row.get("semantic_metadata") or {}
    benchmark = row.get("benchmark_metadata") or {}
    spans = row.get("evidence_spans") or {}

    return {
        1: row.get("model_id", "").casefold(),
        2: " ".join(
            [
                _text(filter_metadata.get(key))
                for key in (
                    "primary_task", "matched_tasks", "architecture", "model_type",
                    "license", "hardware", "canonical_model_id", "variant_types",
                )
            ]
            # 불린 맵은 참인 키만 — false인 키 이름이 걸리면 안 된다.
            + [_flags(filter_metadata.get(key)) for key in ("artifacts", "quantization")]
        ).casefold(),
        3: " ".join(
            _text(semantic.get(key))
            for key in (
                "summary", "use_cases", "documented_strengths",
                "documented_limitations", "license_notes", "benchmarks", "warnings",
            )
        ).casefold(),
        4: _text(benchmark.get("results")).casefold() + " " + _text(benchmark.get("summary")).casefold(),
        5: _text(spans.get("parents")).casefold(),
    }


@dataclass
class Rule:
    """질의 하나의 판정 규칙. 판정 전에 글로 고정해 유형 간 기준이 흔들리지 않게 한다."""

    must_any: Sequence[str]           # 하나라도 걸려야 후보. 용도·대상을 나타내는 말
    grade_2_any: Sequence[str] = ()   # 추가로 걸리면 2점 유력
    reject_any: Sequence[str] = ()    # 걸리면 명백한 오답 (다른 용도 전용 등)
    must_label: str = ""
    grade_2_label: str = ""
    grade_1_label: str = ""
    # must에 걸리지 않았어도 이 말이 보이면 ⚠️ 애매로 올린다. 재현율 방어선.
    weak_any: Sequence[str] = field(default_factory=tuple)
    # 이 질의에서 권위 있는 근거로 볼 단계. 비우면 RELIABLE_STAGES(①②③)를 쓴다.
    # benchmark_lookup은 ④(benchmark_metadata.results)가 바로 답이므로 (4,)를 넣는다.
    reliable_stages: Sequence[int] = field(default_factory=tuple)


@dataclass
class Hit:
    model_id: str
    pile: str                        # flag | unsure | reject
    stages: Dict[int, List[str]]     # 단계 -> 걸린 말들
    grade_2_stages: Dict[int, List[str]]
    reject_stages: Dict[int, List[str]]
    proposal: Optional[int]          # 제안 등급 2 / 1 / None
    reason: str

    @property
    def decisive_stage(self) -> int:
        """가장 얕은 단계. model_id가 이미 말해주면 README가 뭐라 하든 쉬운 판정이다."""
        return min(self.stages) if self.stages else 0

    @property
    def difficulty(self) -> str:
        """①② 단계에서 판정되면 쉬움, ③ 이후까지 가야 하면 어려움."""
        return "easy" if 0 < self.decisive_stage <= 2 else "hard"


def _matches(haystacks: Dict[int, str], needles: Iterable[str]) -> Dict[int, List[str]]:
    found: Dict[int, List[str]] = {}
    for stage, haystack in haystacks.items():
        if not haystack:
            continue
        hits = [needle for needle in needles if needle.casefold() in haystack]
        if hits:
            found[stage] = hits
    return found


# ①~③은 모델의 정체·추출된 주장이므로 믿을 수 있는 신호다. ④⑤는 벤치마크 표와
# README 원문이라 어떤 단어든 우연히 나타난다("요약"을 언급만 한 LLM 카드 등).
# 그래서 기본값에서는 ④⑤에서만 걸린 것을 플래그가 아니라 ⚠️ 애매로 보낸다.
#
# 단, benchmark_lookup은 다르다. 그 유형이 묻는 것이 "이 벤치마크 점수를 공개했는가"
# 이므로 ④(benchmark_metadata.results)가 바로 권위 있는 근거다. 그래서 Rule마다
# 어느 단계를 신뢰할지 정할 수 있게 둔다.
RELIABLE_STAGES = (1, 2, 3)


def scan_row(row: Dict[str, Any], rule: Rule) -> Hit:
    haystacks = stage_haystacks(row)
    must = _matches(haystacks, rule.must_any)
    grade_2 = _matches(haystacks, rule.grade_2_any)
    reject = _matches(haystacks, rule.reject_any)
    weak = _matches(haystacks, rule.weak_any)
    model_id = row["model_id"]

    trusted = rule.reliable_stages or RELIABLE_STAGES
    reliable = {stage: hits for stage, hits in must.items() if stage in trusted}

    if reliable:
        # 2점 신호도 믿을 수 있는 단계에서 나와야 한다.
        strong = {stage: hits for stage, hits in grade_2.items() if stage in RELIABLE_STAGES}
        proposal = 2 if strong else 1
        decisive = min(reliable)
        reason = f"{STAGE_NAMES[decisive]}에서 {', '.join(reliable[decisive])}"
        if reject:
            proposal = 1
            stage = min(reject)
            reason += f" / 다만 {STAGE_NAMES[stage]}에 {', '.join(reject[stage])}"
        return Hit(model_id, "flag", reliable, grade_2, reject, proposal, reason)

    # must가 ④⑤에서만 걸렸거나, weak이 걸린 경우 — 사람이 "진짜 아닌가"를 본다.
    faint = {stage: hits for stage, hits in {**must, **weak}.items()}
    if faint:
        stage = min(faint)
        where = "README 원문" if stage == 5 else STAGE_NAMES[stage]
        return Hit(
            model_id, "unsure", {}, grade_2, reject, None,
            f"믿을 수 있는 단계엔 없고 {where}에만 {', '.join(faint[stage])}",
        )

    return Hit(model_id, "reject", {}, grade_2, reject, None, "1~5단계 모두 해당 없음")


def scan(rows: Sequence[Dict[str, Any]], rule: Rule) -> Tuple[List[Hit], List[Hit], List[Hit]]:
    flags: List[Hit] = []
    unsure: List[Hit] = []
    reject: List[Hit] = []
    for row in rows:
        hit = scan_row(row, rule)
        {"flag": flags, "unsure": unsure, "reject": reject}[hit.pile].append(hit)
    # 깊은 단계에서 걸린 것(어려운 판정)을 먼저 보여준다.
    flags.sort(key=lambda h: (-(h.proposal or 0), -h.decisive_stage, h.model_id))
    unsure.sort(key=lambda h: (-h.decisive_stage, h.model_id))
    return flags, unsure, reject


def reject_reasons(rows: Sequence[Dict[str, Any]], hits: Sequence[Hit], task: str) -> Dict[str, List[str]]:
    """오답 더미를 소분류한다. 사람이 '어디를 더 봐야 하나'를 판단할 수 있게."""
    by_id = {row["model_id"]: row for row in rows}
    groups: Dict[str, List[str]] = {}
    for hit in hits:
        row = by_id[hit.model_id]
        filter_metadata = row.get("filter_metadata") or {}
        semantic = row.get("semantic_metadata") or {}
        primary = filter_metadata.get("primary_task")
        if primary and primary != task:
            key = f"주 task가 {primary}"
        elif not (semantic.get("use_cases") or semantic.get("summary")):
            key = "claim 자체가 비어 있음"
        else:
            key = "용도 언급 없음"
        groups.setdefault(key, []).append(hit.model_id)
    return dict(sorted(groups.items(), key=lambda item: -len(item[1])))


TOKEN = re.compile(r"[\w가-힣]+")


def query_tokens(text: str) -> List[str]:
    return [token for token in TOKEN.findall(text.casefold()) if len(token) > 1]
