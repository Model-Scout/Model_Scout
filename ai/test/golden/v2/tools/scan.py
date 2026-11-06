"""eligible 전수를 6단계 규칙으로 스캔해 사람이 볼 것만 추린다.

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
    # 다른 모델 열을 잘못 읽었거나 양자화/변환본의 표인 경우다. 이 단계는
    # 사람에게 보여 주되, 자동 정답 후보로 올리면 안 된다.
    6: "unverified_benchmark",
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


_BENCHMARK_FIELDS = ("dataset", "benchmark", "metric", "config", "split", "revision")


def _benchmark_result_text(result: Any) -> str:
    """벤치마크명 판정에 쓸 최소 필드만 남긴다.

    ``supporting_quote``나 표의 다른 모델명까지 통째로 검색하면, 한 표 안의 다른
    열에 있는 MMLU가 현재 모델의 MMLU 결과인 것처럼 잡힌다. 그래서 dataset 등
    결과 자체를 설명하는 필드만 사용한다.
    """
    if not isinstance(result, dict):
        return ""
    return " ".join(_text(result.get(key)) for key in _BENCHMARK_FIELDS).casefold()


def _trusted_benchmark_result(result: Any) -> bool:
    """현재 모델에 안전하게 귀속되는 수치 결과인지 판정한다.

    추출기가 명시적으로 variant/source 불일치라고 표시한 결과는 지우지 않는다.
    다만 ⑥으로 보내 사람이 확인하게 하고, ④의 자동 2점 근거로는 쓰지 않는다.
    """
    if not isinstance(result, dict) or result.get("score") in (None, ""):
        return False
    return (
        result.get("ranking_eligible") is not False
        and result.get("variant_safe") is not False
        and result.get("model_name_matches_source") is not False
    )


def _benchmark_result_haystacks(benchmark: Any) -> Tuple[List[str], List[str]]:
    """(안전하게 귀속된 결과, 출처가 불명확한 결과)를 돌려준다."""
    if not isinstance(benchmark, dict):
        return [], []
    results = benchmark.get("results")
    if not isinstance(results, list):
        return [], []

    trusted: List[str] = []
    unverified: List[str] = []
    for result in results:
        text = _benchmark_result_text(result)
        if not text:
            continue
        (trusted if _trusted_benchmark_result(result) else unverified).append(text)
    return trusted, unverified


def stage_haystacks(row: Dict[str, Any]) -> Dict[int, str]:
    """각 단계가 보는 텍스트. 단계를 섞지 않는다 — 난이도 판정에 쓰기 때문이다."""
    filter_metadata = row.get("filter_metadata") or {}
    semantic = row.get("semantic_metadata") or {}
    benchmark = row.get("benchmark_metadata") or {}
    spans = row.get("evidence_spans") or {}
    trusted_benchmarks, unverified_benchmarks = _benchmark_result_haystacks(benchmark)

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
        # ④는 현재 모델에 귀속되는 구조화된 결과만. supporting_quote 같은 원문은
        # ⑤에 남겨, 다른 모델의 표 열이 자동 정답이 되는 일을 막는다.
        4: " ".join(trusted_benchmarks),
        5: _text(spans.get("parents")).casefold(),
        # ⑥은 실제로 추출됐지만 출처/variant가 불명확한 benchmark 결과다.
        6: " ".join(unverified_benchmarks),
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
    # benchmark_lookup은 raw README 문자열 대신 결과 행의 dataset/benchmark 필드를
    # 판정한다. exclude는 MMLU-Pro처럼 이름은 겹치지만 다른 benchmark를 막는다.
    benchmark_terms: Sequence[str] = field(default_factory=tuple)
    benchmark_exclude: Sequence[str] = field(default_factory=tuple)
    # model_comparison 전용. ``모델명 언급``과 ``그 모델 계열``을 구분하기 위해
    # model_id와 canonical_model_id에서만 판정하는 비교 대상별 별칭이다.
    # 예: {"KoBART": ("kobart",), "KoT5": ("kot5", "ko-t5")}
    comparison_groups: Dict[str, Sequence[str]] = field(default_factory=dict)
    # 비우면 모든 비교 대상 계열의 원본을 2점 후보로 본다. 특정 대상 자체가
    # 넓은 다국어 계열인 경우에는 1점만 허용할 수 있다.
    comparison_grade_2_groups: Sequence[str] = field(default_factory=tuple)


@dataclass
class Hit:
    model_id: str
    pile: str                        # flag | unsure | reject
    stages: Dict[int, List[str]]     # 단계 -> 걸린 말들
    grade_2_stages: Dict[int, List[str]]
    reject_stages: Dict[int, List[str]]
    proposal: Optional[int]          # 제안 등급 2 / 1 / None
    reason: str
    # model_comparison에서 이 모델이 어느 비교 대상 계열에 속하는지. 다른 유형은 비어 있다.
    comparison_groups: Tuple[str, ...] = ()

    @property
    def decisive_stage(self) -> int:
        """가장 얕은 단계. model_id가 이미 말해주면 README가 뭐라 하든 쉬운 판정이다."""
        return min(self.stages) if self.stages else 0

    @property
    def difficulty(self) -> str:
        """①② 단계에서 판정되면 쉬움, ③ 이후까지 가야 하면 어려움."""
        return "easy" if 0 < self.decisive_stage <= 2 else "hard"


def _contains(haystack: str, needle: str) -> bool:
    """문자열 일부가 아닌 토큰/구 단위로만 맞춘다.

    예를 들어 ``mmlu``는 ``MMLU``에는 맞지만 ``KMMLU``/``MMMLU``/``MMLU-Pro``에는
    맞지 않는다. benchmark 별칭을 구분할 때만 사용한다.
    """
    return bool(re.search(r"(?<![\w-])" + re.escape(needle.casefold()) + r"(?![\w-])", haystack))


def _matches(haystacks: Dict[int, str], needles: Iterable[str]) -> Dict[int, List[str]]:
    """일반 의미 규칙은 어간을 허용하는 느슨한 부분 문자열 매칭을 쓴다.

    예: ``summar`` → summarization, ``transcri`` → transcription. benchmark 이름만
    _benchmark_matches()에서 엄격하게 구분한다.
    """
    found: Dict[int, List[str]] = {}
    for stage, haystack in haystacks.items():
        if not haystack:
            continue
        hits = [needle for needle in needles if needle.casefold() in haystack]
        if hits:
            found[stage] = hits
    return found


def _benchmark_matches(
    row: Dict[str, Any], terms: Iterable[str], excludes: Iterable[str],
) -> Dict[int, List[str]]:
    """결과 행 단위로 benchmark alias를 판정한다.

    한 모델 카드에 MMLU와 MMLU-Pro가 함께 있어도, 원본 MMLU 행은 살리고
    MMLU-Pro 행만 제외해야 한다. 그래서 합쳐진 haystack이 아니라 결과 행마다
    include/exclude를 적용한다.
    """
    benchmark = row.get("benchmark_metadata") or {}
    trusted, unverified = _benchmark_result_haystacks(benchmark)
    found: Dict[int, List[str]] = {}
    for stage, rows in ((4, trusted), (6, unverified)):
        matches: List[str] = []
        for text in rows:
            if any(_contains(text, excluded) for excluded in excludes):
                continue
            matches.extend(term for term in terms if _contains(text, term))
        if matches:
            found[stage] = list(dict.fromkeys(matches))
    return found


def _merge_matches(*maps: Dict[int, List[str]]) -> Dict[int, List[str]]:
    """같은 단계의 must/weak 근거를 덮어쓰지 않고 합친다."""
    merged: Dict[int, List[str]] = {}
    for matches in maps:
        for stage, terms in matches.items():
            merged.setdefault(stage, []).extend(terms)
    return {stage: list(dict.fromkeys(terms)) for stage, terms in merged.items()}


# ①~③은 모델의 정체·추출된 주장이므로 믿을 수 있는 신호다. ④⑤⑥은 벤치마크 표와
# README 원문 또는 출처 불명확 결과라 어떤 단어든 우연히 나타날 수 있다. 그래서
# 기본값에서는 ④⑤⑥에서만 걸린 것을 플래그가 아니라 ⚠️ 애매로 보낸다.
#
# 단, benchmark_lookup은 다르다. 그 유형이 묻는 것이 "이 벤치마크 점수를 공개했는가"
# 이므로 ④(benchmark_metadata.results)가 바로 권위 있는 근거다. 그래서 Rule마다
# 어느 단계를 신뢰할지 정할 수 있게 둔다.
RELIABLE_STAGES = (1, 2, 3)

# Stage 1 family 그룹화가 아직 self-canonical로 남긴 재업로드·형식 변환본도 있다.
# 모델 ID에 명시된 형식/변환 표지는 원본 2점 자동 제안을 막는 보수적 신호로만 쓴다.
_COMPARISON_VARIANT_NAME = re.compile(
    r"(?:^|[/_-])(?:gguf|onnx|ct2[a-z0-9]*|ctranslate2?|mlx|awq|gptq|"
    r"int[48]|fp(?:8|16)|q[2-8](?:_[a-z0-9]+)?|quant(?:ized)?|"
    r"finetun(?:e|ed|ing)|fine[-_]?tuned|distill(?:ed|ation))(?:$|[/_-])",
    re.IGNORECASE,
)


def _comparison_identity_matches(row: Dict[str, Any], rule: Rule) -> Dict[str, List[str]]:
    """비교 대상의 계보를 ``model_id``·``canonical_model_id``에서만 찾는다.

    README가 "BGE-M3를 이겼다"고 썼다고 해서 그 모델이 BGE-M3 계열인 것은 아니다.
    비교 질의에서는 이 구분이 핵심이므로 semantic_metadata·evidence는 정체성 근거로
    쓰지 않는다. canonical_model_id는 Stage 1의 family/variant 그룹화 결과라 변환본·
    재업로드가 원본 계열에 연결된 경우만 보완한다.
    """
    metadata = row.get("filter_metadata") or {}
    sources = {
        "model_id": str(row.get("model_id") or "").casefold(),
        "canonical_model_id": str(metadata.get("canonical_model_id") or "").casefold(),
    }
    matches: Dict[str, List[str]] = {}
    for group, aliases in rule.comparison_groups.items():
        matched_sources: List[str] = []
        for source, text in sources.items():
            if any(alias.casefold() in text for alias in aliases):
                matched_sources.append(source)
        if matched_sources:
            matches[group] = matched_sources
    return matches


def _scan_comparison_row(row: Dict[str, Any], rule: Rule) -> Hit:
    """모델 비교 질의의 엄격한 계열 판정.

    자동 2점은 직접 이름이 맞고 원본/비변형으로 표시된 경우에만 제안한다. canonical
    연결만 된 모델, 양자화본·변환본은 같은 계열이라도 1점 후보로 남겨 사람이 확정한다.
    """
    model_id = row["model_id"]
    matches = _comparison_identity_matches(row, rule)
    if not matches:
        return Hit(model_id, "reject", {}, {}, {}, None, "model_id·canonical_model_id에 비교 대상 계열 없음")

    metadata = row.get("filter_metadata") or {}
    direct_groups = {group for group, sources in matches.items() if "model_id" in sources}
    eligible_for_two = set(rule.comparison_grade_2_groups or tuple(rule.comparison_groups))
    name_marks_variant = bool(_COMPARISON_VARIANT_NAME.search(model_id))
    is_original = metadata.get("is_variant") is not True and not name_marks_variant
    proposal = 2 if is_original and bool(direct_groups & eligible_for_two) else 1

    groups = tuple(sorted(matches))
    evidence = "; ".join(
        f"{', '.join(sources)}에서 {group}" for group, sources in sorted(matches.items())
    )
    if proposal == 1 and metadata.get("is_variant") is True:
        evidence += " / variant로 표시됨"
    elif proposal == 1 and name_marks_variant:
        evidence += " / model_id에 변환·양자화 표지 있음"
    elif proposal == 1 and not (direct_groups & eligible_for_two):
        evidence += " / 이 비교 대상은 1점 계열로 정의됨"

    return Hit(
        model_id,
        "flag",
        {1: list(groups)},
        {1: list(groups)} if proposal == 2 else {},
        {},
        proposal,
        evidence,
        groups,
    )


def scan_row(row: Dict[str, Any], rule: Rule) -> Hit:
    if rule.comparison_groups:
        return _scan_comparison_row(row, rule)

    haystacks = stage_haystacks(row)
    if rule.benchmark_terms:
        must = _benchmark_matches(row, rule.benchmark_terms, rule.benchmark_exclude)
        grade_2 = _benchmark_matches(row, rule.benchmark_terms, rule.benchmark_exclude)
    else:
        must = _matches(haystacks, rule.must_any)
        grade_2 = _matches(haystacks, rule.grade_2_any)
    reject = _matches(haystacks, rule.reject_any)
    weak = _matches(haystacks, rule.weak_any)
    model_id = row["model_id"]

    trusted = rule.reliable_stages or RELIABLE_STAGES
    reliable = {stage: hits for stage, hits in must.items() if stage in trusted}

    if reliable:
        # 2점 신호도 믿을 수 있는 단계에서 나와야 한다.
        strong = {stage: hits for stage, hits in grade_2.items() if stage in trusted}
        proposal = 2 if strong else 1
        decisive = min(reliable)
        reason = f"{STAGE_NAMES[decisive]}에서 {', '.join(reliable[decisive])}"
        if reject:
            proposal = 1
            stage = min(reject)
            reason += f" / 다만 {STAGE_NAMES[stage]}에 {', '.join(reject[stage])}"
        return Hit(model_id, "flag", reliable, grade_2, reject, proposal, reason)

    # must가 신뢰 단계 밖(⑤⑥)에만 걸렸거나, weak이 걸린 경우 — 사람이 본다.
    faint = _merge_matches(must, weak)
    if faint:
        stage = min(faint)
        where = {
            5: "README 원문",
            6: "출처 불명확 benchmark 결과",
        }.get(stage, STAGE_NAMES[stage])
        return Hit(
            model_id, "unsure", {}, grade_2, reject, None,
            f"믿을 수 있는 단계엔 없고 {where}에만 {', '.join(faint[stage])}",
        )

    return Hit(model_id, "reject", {}, grade_2, reject, None, "1~6단계 모두 해당 없음")


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
