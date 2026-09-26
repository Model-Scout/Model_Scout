#!/usr/bin/env python3
"""Score a retrieval report against the case-based semantic golden set.

Unlike evaluate_retrieval_golden.py (constraint gold set), this uses labeled
model IDs from real model-selection cases, so it reports hit@k and MRR.

Run the retrieval first:
    python 05_validate_retrieval.py --query-file test/golden/semantic_golden_queries.jsonl \
        --report-json test/golden/semantic_golden_retrieval.json \
        --report-md test/golden/semantic_golden_retrieval.md
then:
    python test/evaluate_semantic_golden.py

Only `evaluable_now` queries are scored. `recall_check` and `blocked` queries
are listed with whether their expected models are in the DB yet, so Stage 1
changes can be tracked with the same file.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence


ROOT = Path(__file__).resolve().parents[1]
GOLDEN_DIR = ROOT / "test" / "golden"
QUERY_PATH = GOLDEN_DIR / "semantic_golden_queries.jsonl"
REPORT_PATH = GOLDEN_DIR / "semantic_golden_retrieval.json"
OUTPUT_JSON = GOLDEN_DIR / "semantic_golden_evaluation.json"
OUTPUT_MD = GOLDEN_DIR / "semantic_golden_evaluation.md"
STAGE2_PATHS = (
    ROOT / "data" / "hf_models_stage2_core.jsonl",
    ROOT / "data" / "hf_models_stage2_low_popularity.jsonl",
)

# Provisional license policy for scoring only. Licenses outside both sets
# (other, llama*, gemma, custom, missing) count as "review", not violations.
COMMERCIAL_OK = {
    "apache-2.0", "mit", "bsd", "bsd-2-clause", "bsd-3-clause", "cc0-1.0",
    "cc-by-4.0", "cc-by-sa-4.0", "cc-by-3.0", "openrail", "openrail++",
    "bigscience-openrail-m", "creativeml-openrail-m", "unlicense", "mpl-2.0",
}
REVIEW_FLAGS = ("review_required", "needs_review")


def read_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            yield json.loads(line)


def norm(model_id: Optional[str]) -> str:
    return (model_id or "").casefold()


def license_class(license_value: Any) -> str:
    values = license_value if isinstance(license_value, list) else [license_value]
    names = [norm(str(value)) for value in values if value]
    if not names:
        return "review"
    if any("-nc" in name or "noncommercial" in name or "non-commercial" in name for name in names):
        return "noncommercial"
    if all(name in COMMERCIAL_OK for name in names):
        return "commercial_ok"
    return "review"


def result_ids(result: Dict[str, Any], family: bool = False) -> set:
    ids = {norm(result.get("model_id"))}
    if family:
        # canonical_model_id follows declared base models, so a fine-tune can share
        # its base model's canonical ID. Family matches are reported separately.
        ids.add(norm(result.get("canonical_model_id")))
    return ids - {""}


def first_rank(results: Sequence[Dict[str, Any]], targets: Sequence[str], family: bool = False) -> Optional[int]:
    wanted = {norm(model_id) for model_id in targets}
    for rank, result in enumerate(results, start=1):
        if result_ids(result, family) & wanted:
            return rank
    return None


def has_review_flag(result: Dict[str, Any]) -> bool:
    return any(result.get(flag) for flag in REVIEW_FLAGS)


def oversize_reason(stage2: Optional[Dict[str, Any]], budget_gb: float) -> Optional[str]:
    if not stage2:
        return "not_in_stage2"
    if (stage2.get("model") or {}).get("parameter_count") is None:
        return "parameter_count_unknown"
    weights = (stage2.get("hardware") or {}).get("weights_only") or {}
    sizes = [weights.get(key) for key in ("detected_quantization_gib", "int4_gib", "int8_gib", "fp16_gib")]
    smallest = next((size for size in sizes if isinstance(size, (int, float))), None)
    if smallest is None:
        return "size_unknown"
    if smallest > budget_gb:
        return f"min_weights_{smallest}GiB>{budget_gb}GB"
    return None


def score_query(query: Dict[str, Any], results: List[Dict[str, Any]], stage2: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    labels = query["labels"]
    behavior = labels["expected_behavior"]
    expected_rank = first_rank(results, labels["expected_any"])
    acceptable_rank = first_rank(results, labels["expected_any"] + labels["acceptable"])
    family_rank = first_rank(results, labels["expected_any"], family=True)
    excluded = {norm(item["model_id"]) for item in labels["must_exclude"]}
    must_exclude_hits = [result["model_id"] for result in results if result_ids(result) & excluded]
    review_ids = {norm(item["model_id"] if isinstance(item, dict) else item) for item in labels["needs_review"]}
    review_missing = [
        result["model_id"] for result in results
        if result_ids(result) & review_ids and not has_review_flag(result)
    ]

    license_violations: List[str] = []
    license_review: List[str] = []
    if query.get("license_requirement") == "commercial":
        for result in results:
            row = stage2.get(norm(result.get("model_id")))
            kind = license_class(row.get("license") if row else None)
            if kind == "noncommercial":
                license_violations.append(result["model_id"])
            elif kind == "review" and not has_review_flag(result):
                license_review.append(result["model_id"])

    oversize_unflagged: List[Dict[str, str]] = []
    warn_rule = labels.get("warn_rule") or {}
    if behavior == "warn_on_oversize":
        budget = float(warn_rule.get("vram_budget_gb") or query.get("gpu_vram_gb") or 0)
        for result in results:
            reason = oversize_reason(stage2.get(norm(result.get("model_id"))), budget)
            if reason and not has_review_flag(result):
                oversize_unflagged.append({"model_id": result["model_id"], "reason": reason})

    if behavior == "recommend":
        passed = expected_rank is not None and not must_exclude_hits and not license_violations and not review_missing
    elif behavior == "must_exclude_only":
        passed = not must_exclude_hits and not license_violations
    elif behavior == "warn_on_oversize":
        passed = not oversize_unflagged
    else:
        passed = False

    return {
        "query_id": query["id"],
        "label_type": query["label_type"],
        "expected_behavior": behavior,
        "passed": passed,
        "result_count": len(results),
        "expected_rank": expected_rank,
        "acceptable_rank": acceptable_rank,
        "family_rank": family_rank,
        "reciprocal_rank": round(1 / expected_rank, 4) if expected_rank else 0.0,
        "must_exclude_hits": must_exclude_hits,
        "license_violations": license_violations,
        "license_review_unflagged": license_review,
        "needs_review_unflagged": review_missing,
        "oversize_unflagged": oversize_unflagged,
        "known_failure_cause": query.get("known_failure_cause"),
        "top_models": [result["model_id"] for result in results],
    }


def recall_status(query: Dict[str, Any], stage2: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    labels = query["labels"]
    in_db = [model_id for model_id in labels["expected_any"] if norm(model_id) in stage2]
    return {
        "query_id": query["id"],
        "label_type": query["label_type"],
        "blocked_by": query.get("blocked_by") or [],
        "expected_any": labels["expected_any"],
        "expected_in_db": in_db,
    }


def ratio(numerator: int, denominator: int) -> str:
    return f"{numerator}/{denominator}" if denominator else "0/0"


def render_markdown(summary: Dict[str, Any], scored: List[Dict[str, Any]], pending: List[Dict[str, Any]]) -> str:
    lines = [
        "# Semantic 골든셋 평가",
        "",
        "실제 모델 선정 사례(`test/golden/korean_model_selection_cases_v2.jsonl`)에서 만든 정답 라벨로 검색 결과를 채점한다.",
        "`evaluable_now=true`인 질의만 점수에 포함하고, recall_check·blocked 질의는 정답 모델의 DB 포함 여부만 추적한다.",
        "",
        "## 요약",
        "",
        f"- 검색 모드: `{summary['mode']}`",
        f"- 채점 질의: {summary['scored_queries']}개, 통과 {summary['passed']}개",
        f"- recommend 질의 hit@{summary['top_k']}: {summary['hit_at_k']}",
        f"- recommend 질의 acceptable hit@{summary['top_k']}: {summary['acceptable_hit_at_k']}",
        f"- recommend 질의 같은 계열(canonical) hit@{summary['top_k']}: {summary['family_hit_at_k']}",
        f"- recommend 질의 MRR: {summary['mrr']}",
        f"- must_exclude 위반 질의: {summary['must_exclude_violation_queries']}",
        f"- 상업 조건 라이선스 위반 질의: {summary['license_violation_queries']}",
        "",
        "## 질의별 결과",
        "",
        "| 질의 | 동작 | 통과 | 정답 순위 | 허용 순위 | 계열 순위 | 실패 원인 |",
        "|---|---|---|---:|---:|---:|---|",
    ]
    for item in scored:
        causes = []
        if item["expected_behavior"] == "recommend" and item["expected_rank"] is None:
            causes.append("정답 없음")
        if item["must_exclude_hits"]:
            causes.append("must_exclude: " + ", ".join(item["must_exclude_hits"]))
        if item["license_violations"]:
            causes.append("비상업 라이선스: " + ", ".join(item["license_violations"]))
        if item["needs_review_unflagged"]:
            causes.append("경고 누락: " + ", ".join(item["needs_review_unflagged"]))
        if item["oversize_unflagged"]:
            causes.append(f"크기 경고 누락 {len(item['oversize_unflagged'])}개")
        if item["known_failure_cause"] and not item["passed"]:
            causes.append(f"알려진 원인: {item['known_failure_cause']}")
        lines.append(
            f"| `{item['query_id']}` | {item['expected_behavior']} | {'✅' if item['passed'] else '❌'} "
            f"| {item['expected_rank'] or '-'} | {item['acceptable_rank'] or '-'} | {item['family_rank'] or '-'} "
            f"| {'; '.join(causes) or '-'} |"
        )
    lines += [
        "",
        "## 아직 채점하지 않는 질의",
        "",
        "| 질의 | 유형 | 막힌 이유 | 정답 중 DB에 있는 모델 |",
        "|---|---|---|---|",
    ]
    for item in pending:
        lines.append(
            f"| `{item['query_id']}` | {item['label_type']} | {', '.join(item['blocked_by']) or 'answer_not_in_db'} "
            f"| {', '.join(item['expected_in_db']) or '없음'} |"
        )
    lines += [
        "",
        "## 해석 시 주의",
        "",
        "- 라이선스 판정은 채점용 임시 정책이다. apache-2.0·mit 등은 상업 허용, 이름에 `nc`가 들어가면 위반, `other`·gemma·llama·미기재는 `확인 필요`로 본다.",
        "- 현재 검색 결과에는 `확인 필요` 경고 필드가 없어서, 경고가 필요한 모델이 top-k에 나오면 모두 경고 누락으로 집계된다.",
        "- 정답은 사례 작성자가 고른 모델 하나이지 유일한 정답이 아니다. acceptable hit를 함께 본다.",
        "- 정답·허용 순위는 model_id가 정확히 같을 때만 센다. 계열 순위는 canonical_model_id 일치까지 포함하며, canonical이 선언된 base model을 따르므로 다른 파인튜닝 모델도 같은 계열로 잡힐 수 있다.",
        "- `lexical_offline` 모드는 정수 점수 동점이 많아 순위 신뢰도가 낮다. 성능 판단은 `--execute`(vector) 결과로 한다.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--queries", type=Path, default=QUERY_PATH)
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    parser.add_argument("--output-json", type=Path, default=OUTPUT_JSON)
    parser.add_argument("--output-md", type=Path, default=OUTPUT_MD)
    args = parser.parse_args()

    queries = list(read_jsonl(args.queries))
    report = json.loads(args.report.read_text(encoding="utf-8"))
    results_by_query = {item["query_id"]: item.get("results") or [] for item in report.get("reports", [])}
    stage2 = {norm(row["model_id"]): row for path in STAGE2_PATHS for row in read_jsonl(path)}

    scored = [
        score_query(query, results_by_query.get(query["id"], []), stage2)
        for query in queries
        if query.get("evaluable_now")
    ]
    pending = [recall_status(query, stage2) for query in queries if not query.get("evaluable_now")]
    recommend = [item for item in scored if item["expected_behavior"] == "recommend"]
    top_k = max((query.get("top_k", 5) for query in queries), default=5)
    summary = {
        "mode": report.get("mode") or (report.get("reports") or [{}])[0].get("mode"),
        "top_k": top_k,
        "scored_queries": len(scored),
        "passed": sum(item["passed"] for item in scored),
        "hit_at_k": ratio(sum(item["expected_rank"] is not None for item in recommend), len(recommend)),
        "acceptable_hit_at_k": ratio(sum(item["acceptable_rank"] is not None for item in recommend), len(recommend)),
        "family_hit_at_k": ratio(sum(item["family_rank"] is not None for item in recommend), len(recommend)),
        "mrr": round(sum(item["reciprocal_rank"] for item in recommend) / len(recommend), 4) if recommend else 0.0,
        "must_exclude_violation_queries": ratio(sum(bool(item["must_exclude_hits"]) for item in scored), len(scored)),
        "license_violation_queries": ratio(
            sum(bool(item["license_violations"]) for item in scored),
            sum(1 for query in queries if query.get("evaluable_now") and query.get("license_requirement") == "commercial"),
        ),
        "pending_queries": len(pending),
    }
    args.output_json.write_text(
        json.dumps({"summary": summary, "scored": scored, "pending": pending}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.output_md.write_text(render_markdown(summary, scored, pending), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
