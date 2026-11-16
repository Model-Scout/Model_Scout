"""eligible 전수 스캔: 모든 eligible 모델을 네 분류 중 하나에 넣는다.

검색기(BM25·dense·RRF Top-K)를 쓰지 않는다. 하드 필터로 eligible 을 만든 뒤,
eligible 모델 하나하나를 아래 순서의 저장된 근거에서 질의의 relevance rule 과
대조한다.

    1 model_id  2 canonical_model_id  3 filter_metadata  4 technical_metadata
    5 semantic_metadata  6 benchmark_metadata  7 source_provenance  8 evidence(README span)

분류

    proposed_grade_2      필수 능력이 1·2·5 단계(모델명·원본명·의미 claim)에서 명시적으로 확인되고
                          2점 조건(예: 한국어 전용, 원본)을 만족
    proposed_grade_1      필수 능력은 확인되지만 다국어·범용·부가 기능·변환본이거나,
                          근거가 3·4·6·7 단계의 메타데이터에만 있음
    unresolved_for_human  근거가 8 단계 README 원문에만 있어 사람이 읽어야 함
    auto_rejected         기계적으로 확인 가능한 이유가 있음(이유 코드 저장)

"근거 없음"은 실제로 그 능력이 없다는 뜻이 아니라, 현재 Model Scout 데이터로 이
질의의 정답임을 증명할 수 없다는 뜻이다.
"""

from __future__ import annotations

import json
import random
import re
from collections import Counter
from functools import lru_cache
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import corpus

STAGES = (
    "model_id", "canonical_model_id", "filter_metadata", "technical_metadata",
    "semantic_metadata", "benchmark_metadata", "source_provenance", "evidence",
)
STRONG_STAGES = {"model_id", "canonical_model_id", "semantic_metadata"}
WEAK_STAGES = {"filter_metadata", "technical_metadata", "benchmark_metadata", "source_provenance"}
CLASSES = ("proposed_grade_2", "proposed_grade_1", "auto_rejected", "unresolved_for_human")
REVIEW_LIMIT = 25

# auto_rejected 이유 코드. 사람이 읽는 설명은 worksheet 가 붙인다.
REJECT_REASONS = {
    "no_supporting_evidence": "요구 능력을 뒷받침하는 저장된 근거 없음",
    "conflicting_use": "명시된 용도와 충돌하는 표지(모델명·의미 claim)",
    "other_task": "요구 능력과 다른 task 로만 확인됨",
    "other_family": "지정한 모델 계열이 아님",
    "not_named_model": "질문이 지목한 모델 이름이 아님",
    "no_benchmark_results": "벤치마크 결과 없음",
    "other_benchmark_dataset": "다른 benchmark dataset 만 있음",
    "other_metric": "같은 dataset 이지만 다른 metric",
    "variant_mismatch": "variant 관계가 질문과 맞지 않음",
}

# 변환·양자화·재업로드 표지. 포맷을 요구하지 않은 질의에서 이런 모델은 1점 후보로 내린다.
VARIANT_ID_RE = re.compile(
    r"(?i)(gguf|ggml|awq|gptq|exl2|mlx|onnx|int4|int8|4bit|8bit|4-bit|8-bit|bnb|fp8|nvfp4|w4a|q[2-8]_|"
    r"quant|imatrix|ct2|ctranslate|openvino|-i1-|heretic|abliterat|uncensored)")
KOREAN_SPECIFIC_RE = re.compile(
    r"(?i)(^|[^a-z])(ko|kor|korean)([^a-z]|$)|klue|kobart|kot5|kogpt|kosimcse|koelectra|kobert|"
    r"kanana|exaone|hyperclova|midm|solar|polyglot-ko|bllossom|한국")


# --------------------------------------------------------------------------- 단계별 텍스트

def _flatten(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float, bool)):
        return str(value)
    if isinstance(value, dict):
        return " ".join(f"{k} {_flatten(v)}" for k, v in value.items())
    if isinstance(value, (list, tuple)):
        return " ".join(_flatten(v) for v in value)
    return str(value)


# 능력의 근거가 되는 긍정 claim. 한계·경고("의료 조언 용도 아님")는 능력 근거로 세지 않고
# 충돌 검사에만 쓴다.
SEMANTIC_CLAIM_FIELDS = ("use_cases", "documented_strengths", "benchmarks")
SEMANTIC_CAVEAT_FIELDS = ("documented_limitations", "warnings")


def semantic_claims(row: Mapping[str, Any], fields: Sequence[str] = SEMANTIC_CLAIM_FIELDS) -> List[Tuple[str, str]]:
    sem = row.get("semantic_metadata") or {}
    out: List[Tuple[str, str]] = []
    summary = (sem.get("summary") or {}).get("text") if isinstance(sem.get("summary"), dict) else None
    if summary and fields is SEMANTIC_CLAIM_FIELDS:
        out.append(("summary", summary))
    for field in fields:
        for item in sem.get(field) or []:
            if isinstance(item, dict) and item.get("text"):
                out.append((field, item["text"]))
    return out


def _filter_text(meta: Mapping[str, Any]) -> str:
    keys = ("primary_task", "matched_tasks", "languages", "architecture", "model_type", "license",
            "commercial_status", "artifact_formats", "quantization", "runtime_compatibility", "variant_types")
    return _flatten({k: meta.get(k) for k in keys})


def _technical_text(tech: Mapping[str, Any]) -> str:
    return _flatten({k: tech.get(k) for k in ("base_models", "datasets", "metrics", "model")})


def _benchmark_text(bench: Mapping[str, Any]) -> str:
    return _flatten([{k: r.get(k) for k in ("benchmark", "dataset", "metric")} for r in bench.get("results") or []])


def _provenance_text(prov: Mapping[str, Any]) -> str:
    card = prov.get("model_card") or {}
    hub = prov.get("hub") or {}
    return _flatten({"card": {k: card.get(k) for k in ("tags", "pipeline_tag", "datasets", "language", "base_model")},
                     "hub": {k: hub.get(k) for k in ("tags", "pipeline_tag")}})


def _evidence_text(row: Mapping[str, Any]) -> str:
    spans = row.get("evidence_spans") or {}
    parts = []
    for parent in spans.get("parents") or []:
        parts.append(parent.get("text") or "")
    sem = row.get("semantic_metadata") or {}
    for field in SEMANTIC_CLAIM_FIELDS:
        for item in sem.get(field) or []:
            if isinstance(item, dict):
                parts.append(item.get("supporting_quote") or "")
    return "\n".join(parts)


@lru_cache(maxsize=None)
def _stage_texts_cached(model_id: str) -> Tuple[str, ...]:
    row = _ROWS[model_id]
    meta = corpus.meta_of(row)
    return (
        model_id,
        corpus.canonical_of(row),
        _filter_text(meta),
        _technical_text(row.get("technical_metadata") or {}),
        " ".join(text for _, text in semantic_claims(row)),
        _benchmark_text(row.get("benchmark_metadata") or {}),
        _provenance_text(row.get("source_provenance") or {}),
        _evidence_text(row),
        " ".join(text for _, text in semantic_claims(row, SEMANTIC_CAVEAT_FIELDS)),
    )


_ROWS: Dict[str, Mapping[str, Any]] = {}


def bind(rows: Sequence[Mapping[str, Any]]) -> None:
    """스캔할 코퍼스를 지정한다(텍스트 캐시 초기화)."""
    _ROWS.clear()
    _ROWS.update(corpus.by_id(rows))
    _stage_texts_cached.cache_clear()


def stage_texts(row: Mapping[str, Any]) -> Dict[str, str]:
    if row["model_id"] not in _ROWS:
        _ROWS[row["model_id"]] = row
    return dict(zip((*STAGES, "semantic_caveats"), _stage_texts_cached(row["model_id"])))


def _compile(patterns: Sequence[str]) -> Optional[re.Pattern]:
    return re.compile("|".join(f"(?:{p})" for p in patterns), re.IGNORECASE) if patterns else None


# 매칭 직전에 이런 말이 있으면 능력의 근거가 아니라 부정·면책 문장이다
# ("not recommended for critical scenarios such as medical", "의료 진단에 쓰지 않는다").
NEGATION_RE = re.compile(
    r"(?i)(\bnot\b|\bno\b|n't|cannot|unable|never|avoid|without|neither|nor|prohibit|disclaim|"
    r"않|금지|불가|아닙니다|아니다|대체할 수 없)[^.!?\n]{0,80}$")


def negated(text: str, start: int) -> bool:
    return bool(NEGATION_RE.search(text[max(0, start - 90):start]))


def first_hit(texts: Mapping[str, str], pattern: Optional[re.Pattern], stages: Iterable[str] = STAGES,
              allow_negated: bool = False) -> Optional[Tuple[str, str]]:
    if pattern is None:
        return None
    for stage in stages:
        text = texts.get(stage) or ""
        for match in pattern.finditer(text):
            if not allow_negated and stage not in ("model_id", "canonical_model_id") and negated(text, match.start()):
                continue
            start = max(0, match.start() - 60)
            return stage, text[start:match.end() + 60].replace("\n", " ")
    return None


# --------------------------------------------------------------------------- 모델 속성

def variant_info(row: Mapping[str, Any]) -> Dict[str, Any]:
    family = row.get("family") or {}
    meta = corpus.meta_of(row)
    is_variant = bool(meta.get("is_variant") or family.get("is_variant"))
    id_marker = VARIANT_ID_RE.search(row["model_id"])
    return {
        "canonical_model_id": corpus.canonical_of(row),
        "is_variant": is_variant,
        "variant_types": family.get("variant_types") or meta.get("variant_types") or [],
        "relation_source": family.get("canonical_source"),
        "declared_base_models": family.get("declared_base_models") or [],
        "conversion_marker": id_marker.group(0) if id_marker else None,
    }


def is_conversion(row: Mapping[str, Any]) -> bool:
    """같은 가중치의 변환·양자화·재업로드인가. base_model 태그만 있는 파인튜닝은 별개 모델이다."""
    info = variant_info(row)
    return bool(info["conversion_marker"]) or bool(info["variant_types"])


def format_requested(query_or_rule: Mapping[str, Any], conditions: Mapping[str, Any]) -> bool:
    return bool(query_or_rule.get("format_requested") or conditions.get("require_artifact"))


def korean_specific(row: Mapping[str, Any]) -> bool:
    meta = corpus.meta_of(row)
    languages = set(meta.get("languages") or [])
    if KOREAN_SPECIFIC_RE.search(row["model_id"]) or KOREAN_SPECIFIC_RE.search(corpus.canonical_of(row)):
        return True
    return bool(languages) and languages <= {"ko", "en"} and "ko" in languages


# --------------------------------------------------------------------------- 분류

def _decision(cls: str, reason: str, **extra: Any) -> Dict[str, Any]:
    return {"class": cls, "reason": reason, **extra}


def classify_semantic(row: Mapping[str, Any], rule: Mapping[str, Any]) -> Dict[str, Any]:
    """semantic_capability / semantic_constraint / structured_constraint 공통 규칙."""
    texts = stage_texts(row)
    scan = rule.get("scan") or {}
    must = _compile(scan.get("must_any") or [])
    must_id = _compile(scan.get("must_id_any") or [])
    conflict = _compile(scan.get("conflict_any") or [])
    strong = _compile(scan.get("grade_2_any") or [])
    wants_format = bool(rule.get("format_requested"))

    if must is None and must_id is None:  # 능력 조건이 없는 질의: 하드 필터가 정답을 정한다
        hit: Optional[Tuple[str, str]] = ("filter_metadata", "하드 필터 조건만으로 판정")
    else:
        # 모델명 전용 패턴(예: koelectra-...-bias)은 README 본문에서는 잡음이 많아 1·2단계에서만 본다
        hit = first_hit(texts, must_id, ("model_id", "canonical_model_id")) or first_hit(texts, must)
    conflict_hit = first_hit(texts, conflict, ("model_id", "canonical_model_id", "semantic_metadata", "semantic_caveats"),
                             allow_negated=True)
    also = _compile(scan.get("also_any") or [])
    if hit is not None and also is not None and not first_hit(texts, also):
        # 두 개념을 모두 요구하는 질의(예: 금융 + 감정 분류)에서 한쪽 근거만 있는 모델
        return _decision("auto_rejected", "no_supporting_evidence",
                         evidence={"found": hit[0], "missing_patterns": scan.get("also_any")})
    if hit is None:
        return _decision("auto_rejected", "no_supporting_evidence",
                         evidence={"searched_stages": list(STAGES), "patterns": scan.get("must_any"),
                                   "id_patterns": scan.get("must_id_any")})
    if conflict_hit and hit[0] not in STRONG_STAGES:
        return _decision("auto_rejected", "conflicting_use",
                         evidence={"stage": conflict_hit[0], "snippet": conflict_hit[1]})
    if hit[0] == "evidence":
        return _decision("unresolved_for_human", "README 원문에만 근거가 있어 사람이 읽어야 한다",
                         evidence={"stage": hit[0], "snippet": hit[1]})

    downgrade = []
    if hit[0] in WEAK_STAGES and (must is not None or must_id is not None):
        downgrade.append("근거가 메타데이터에만 있음")
    if strong is not None and not first_hit(texts, strong, ("model_id", "canonical_model_id", "semantic_metadata")):
        downgrade.append("2점 조건(전용·명시 용도) 근거 없음")
    if rule.get("grade_2_requires_korean_specific") and not korean_specific(row):
        downgrade.append("다국어·범용 모델")
    if not wants_format and is_conversion(row):
        downgrade.append("원본의 변환·양자화·재업로드")
    if conflict_hit:
        downgrade.append(f"충돌 표지도 있음: {conflict_hit[1][:60]}")
    if downgrade:
        return _decision("proposed_grade_1", "; ".join(downgrade), evidence={"stage": hit[0], "snippet": hit[1]})
    return _decision("proposed_grade_2", "필수 능력이 명시적 근거로 확인됨",
                     evidence={"stage": hit[0], "snippet": hit[1]})


def matching_results(row: Mapping[str, Any], spec: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    """같은 dataset·metric 결과만. 두 번째 값은 없을 때의 이유 코드."""
    results = (row.get("benchmark_metadata") or {}).get("results") or []
    if not results:
        return [], "no_benchmark_results"
    dataset = re.compile(spec["dataset_regex"], re.IGNORECASE)
    metric = re.compile(spec["metric_regex"], re.IGNORECASE)
    # dataset 이 비어 있으면 benchmark 이름으로 본다. 둘을 이어 붙이면 앵커(^…$)가 깨진다.
    same_dataset = [r for r in results if dataset.search((r.get("dataset") or r.get("benchmark") or "").strip())]
    if not same_dataset:
        return [], "other_benchmark_dataset"
    same = [r for r in same_dataset if metric.search(r.get("metric") or "")]
    if not same:
        return [], "other_metric"
    return same, ""


def classify_benchmark(row: Mapping[str, Any], rule: Mapping[str, Any]) -> Dict[str, Any]:
    spec = rule["benchmark"]
    found, why = matching_results(row, spec)
    if not found:
        return _decision("auto_rejected", why, evidence={"dataset_regex": spec["dataset_regex"],
                                                       "metric_regex": spec["metric_regex"]})
    best = sorted(found, key=lambda r: (r.get("score") is None, -(r.get("score") or 0) if r.get("higher_is_better", True)
                                        else (r.get("score") or 0)))[0]
    shown = {k: best.get(k) for k in ("benchmark", "dataset", "metric", "score", "split", "self_reported",
                                      "comparability", "variant_kind", "variant_safe", "evidence_ref")}
    weak = []
    if best.get("variant_safe") is False or best.get("comparability") not in (None, "safe_same_source"):
        weak.append(f"비교 가능성 {best.get('comparability')} / variant_safe={best.get('variant_safe')}")
    if is_conversion(row) and not rule.get("format_requested"):
        weak.append("원본의 변환·양자화·재업로드")
    if weak:
        return _decision("proposed_grade_1", "; ".join(weak), evidence={"stage": "benchmark_metadata", "result": shown,
                                                                     "matching_results": len(found)})
    return _decision("proposed_grade_2", "같은 dataset·metric 점수가 저장돼 있음",
                     evidence={"stage": "benchmark_metadata", "result": shown, "matching_results": len(found)})


def family_of(row: Mapping[str, Any], families: Sequence[Mapping[str, Any]]) -> Optional[str]:
    for fam in families:
        pattern = re.compile(fam["id_regex"], re.IGNORECASE)
        if pattern.search(row["model_id"]) or pattern.search(corpus.canonical_of(row)):
            return fam["name"]
    return None


def classify_family(row: Mapping[str, Any], rule: Mapping[str, Any], reject_code: str) -> Dict[str, Any]:
    """model_comparison / lexical_exact: 모델명·원본명에서 확인되는 계열만 후보.

    원본명이 canonical 에만 걸리고 모델명에 변환 표지가 없으면 같은 가중치가 아니라
    그 모델을 베이스로 만든 다른 모델(파인튜닝)이므로 제외한다.
    """
    fam = family_of(row, rule["families"])
    if fam is None:
        return _decision("auto_rejected", reject_code, evidence={"families": [f["id_regex"] for f in rule["families"]]})
    in_id = family_of({"model_id": row["model_id"]}, rule["families"]) is not None
    conversion = VARIANT_ID_RE.search(row["model_id"])
    if not in_id and not conversion:
        return _decision("auto_rejected", "variant_mismatch", family=fam,
                         evidence={"stage": "canonical_model_id", "canonical_model_id": corpus.canonical_of(row),
                                   "note": "원본을 베이스로 만든 다른 모델(파인튜닝 등)"})
    stage = "model_id" if in_id else "canonical_model_id"
    if any(re.fullmatch(p, row["model_id"], re.IGNORECASE) for p in rule.get("originals") or []):
        return _decision("proposed_grade_2", f"{fam} 원본 모델", family=fam, evidence={"stage": stage})
    wanted_format = _compile(rule.get("format_any") or [])
    if rule.get("format_requested") and wanted_format and wanted_format.search(row["model_id"]):
        return _decision("proposed_grade_2", f"{fam} 계열이며 요청한 포맷", family=fam, evidence={"stage": stage})
    return _decision("proposed_grade_1", f"{fam} 계열의 변환·양자화·재업로드", family=fam, evidence={"stage": stage})


def classify(row: Mapping[str, Any], query: Mapping[str, Any]) -> Dict[str, Any]:
    rule = dict(query["relevance_rule"])
    rule["format_requested"] = format_requested(rule, query.get("conditions") or {})
    kind = query["query_type"]
    if kind == "benchmark_lookup":
        return classify_benchmark(row, rule)
    if kind == "model_comparison":
        return classify_family(row, rule, "other_family")
    if kind == "lexical_exact":
        return classify_family(row, rule, "not_named_model")
    return classify_semantic(row, rule)


# --------------------------------------------------------------------------- 질의 단위

def relaxations(rows: Sequence[Mapping[str, Any]], conditions: Mapping[str, Any]) -> Dict[str, Any]:
    """조건을 하나씩 뺐을 때의 후보 수와, 정확히 한 조건만 불충족한 near-miss 모델."""
    counts = {}
    near_miss: Dict[str, List[str]] = {}
    for row in rows:
        failed = corpus.condition_failures(row, conditions)
        if len(failed) == 1:
            near_miss.setdefault(failed[0], []).append(row["model_id"])
    for key in conditions:
        reduced = {k: v for k, v in conditions.items() if k != key}
        counts[key] = len(corpus.eligible(rows, reduced))
    individual = {key: len(corpus.eligible(rows, {key: value})) for key, value in conditions.items()}
    return {
        "relaxed_candidate_counts": counts,
        "individual_condition_counts": individual,
        "near_miss_by_condition": {k: sorted(v) for k, v in sorted(near_miss.items())},
        "near_miss_count": sum(len(v) for v in near_miss.values()),
    }


def field_range(rows: Sequence[Mapping[str, Any]], field: str) -> Tuple[Optional[float], Optional[float]]:
    values = sorted(v for v in (corpus._number(corpus.meta_of(r).get(field)) for r in rows) if v is not None)
    if not values:
        return None, None
    return values[max(0, int(len(values) * 0.01))], values[min(len(values) - 1, int(len(values) * 0.99))]


NUMERIC_FIELD = {
    "min_parameters_billion": "parameter_count_billion", "max_parameters_billion": "parameter_count_billion",
    "min_context_length": "context_length", "max_context_length": "context_length",
    "max_artifact_gib": "artifact_runnable_gib",
}


def extreme_reasons(rows: Sequence[Mapping[str, Any]], conditions: Mapping[str, Any], relax: Mapping[str, Any]) -> List[str]:
    """억지로 0개를 만든 abstention 을 잡는다. 빈 목록이면 현실적인 조합."""
    reasons = []
    for key, count in relax["individual_condition_counts"].items():
        if count < 5:
            reasons.append(f"{key} 조건 하나만으로도 코퍼스에서 {count}개뿐(조건 자체가 비현실적)")
    for key, value in conditions.items():
        field = NUMERIC_FIELD.get(key)
        if field is None:
            continue
        low, high = field_range(rows, field)
        if low is None:
            continue
        if key.startswith("max") and value < low:
            reasons.append(f"{key}={value} 가 코퍼스 하위 1%({low}) 보다 작다")
        if key.startswith("min") and value > high:
            reasons.append(f"{key}={value} 가 코퍼스 상위 1%({high}) 보다 크다")
    pairs = (("min_parameters_billion", "max_parameters_billion"), ("min_context_length", "max_context_length"))
    for low_key, high_key in pairs:
        if low_key in conditions and high_key in conditions and conditions[low_key] > conditions[high_key]:
            reasons.append(f"{low_key} > {high_key} 직접 모순")
    if not any(count > 0 for count in relax["relaxed_candidate_counts"].values()):
        reasons.append("어떤 조건 하나를 완화해도 후보가 0개")
    return reasons


def scan_query(query: Mapping[str, Any], rows: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    """질의 하나를 전수 스캔한다. 돌려준 분류 합계는 eligible 수와 같아야 한다."""
    conditions = query.get("conditions") or {}
    pool = corpus.eligible(rows, conditions)
    decisions = {row["model_id"]: classify(row, query) for row in pool} if query["expected_behavior"] != "abstain" else {}
    by_class: Dict[str, List[str]] = {cls: [] for cls in CLASSES}
    for model_id, decision in sorted(decisions.items()):
        by_class[decision["class"]].append(model_id)
    reject_reasons = Counter(d["reason"] for d in decisions.values() if d["class"] == "auto_rejected")
    result: Dict[str, Any] = {
        "corpus_count": len(rows),
        "eligible_count": len(pool),
        "eligible_ids_sha256": corpus.model_ids_sha256(r["model_id"] for r in pool),
        "counts": {cls: len(ids) for cls, ids in by_class.items()},
        "auto_reject_reasons": dict(reject_reasons.most_common()),
        "unknown_excluded": corpus.unknown_exclusions(rows, conditions),
        "classes": by_class,
        "decisions": decisions,
    }
    result["review_count"] = (result["counts"]["proposed_grade_2"] + result["counts"]["proposed_grade_1"]
                              + result["counts"]["unresolved_for_human"])
    result["invariant_ok"] = sum(result["counts"].values()) == len(pool) and set(decisions) == {r["model_id"] for r in pool}
    if query["expected_behavior"] == "abstain":
        relax = relaxations(rows, conditions)
        result["abstention"] = {**relax, "temptation_count": max(relax["relaxed_candidate_counts"].values() or [0]),
                                "extreme_reasons": extreme_reasons(rows, conditions, relax)}
    families = Counter(corpus.canonical_of(_ROWS.get(mid) or {"model_id": mid})
                       for mid in by_class["proposed_grade_2"] + by_class["proposed_grade_1"])
    result["family_counts"] = dict(families.most_common())
    return result


def reject_audit_sample(scan: Mapping[str, Any], seed: str, per_reason: int = 3) -> Dict[str, List[str]]:
    """auto_rejected 규칙을 감사할 소수 무작위 표본(이유별). 전수 검수가 아니다."""
    groups: Dict[str, List[str]] = {}
    for model_id, decision in scan["decisions"].items():
        if decision["class"] == "auto_rejected":
            groups.setdefault(decision["reason"], []).append(model_id)
    rng = random.Random(seed)
    return {reason: sorted(rng.sample(sorted(ids), min(per_reason, len(ids)))) for reason, ids in sorted(groups.items())}


def dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
