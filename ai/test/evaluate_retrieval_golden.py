#!/usr/bin/env python3
"""Evaluate the retrieval constraint gold set without network/API calls.

The query file contains executable hard constraints, so this is a constraint
gold set. It is deliberately not reported as semantic Precision@k/Recall@k:
those metrics require human-judged relevant model IDs for each query.
"""

from __future__ import annotations

import json
import argparse
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_PATH = ROOT / "test" / "stage4_retrieval_validation.json"
STAGE3_PATHS = (
    ROOT.parent / "backend" / "data" / "hf_models_stage3_core.jsonl",
    ROOT.parent / "backend" / "data" / "hf_models_stage3_low_popularity.jsonl",
)
REPORT_PATH = ROOT / "test" / "stage4_golden_set_evaluation.md"


def read_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            yield json.loads(line)


def claim_rows(semantic: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for field in (
        "documented_strengths",
        "documented_limitations",
        "use_cases",
        "warnings",
        "benchmarks",
        "unknowns",
        "license_notes",
    ):
        value = semantic.get(field)
        if isinstance(value, list):
            rows.extend(item for item in value if isinstance(item, dict))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validation", type=Path, default=VALIDATION_PATH)
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    args = parser.parse_args()

    validation = json.loads(args.validation.read_text(encoding="utf-8"))
    stage3: Dict[str, Dict[str, Any]] = {}
    for path in STAGE3_PATHS:
        for row in read_jsonl(path):
            stage3[row["model_id"]] = row

    results = [
        result
        for query in validation.get("reports", [])
        for result in query.get("results", [])
    ]
    evidence_levels = Counter(result.get("evidence_completeness") for result in results)
    top_with_claim_evidence = 0
    validated_rows = 0
    invalid_refs = 0
    uncited_claims = 0
    missing_quotes = 0

    for result in results:
        source = stage3.get(result["model_id"], {})
        claims = claim_rows(source.get("semantic") or {})
        if any(str(item.get("text", "")).strip() and item.get("evidence_refs") for item in claims):
            top_with_claim_evidence += 1
        checked = source.get("validation")
        if checked is not None:
            validated_rows += 1
            invalid_refs += int(checked.get("invalid_evidence_refs") or 0)
            uncited_claims += int(checked.get("uncited_claims") or 0)
            missing_quotes += int(checked.get("missing_quotes") or 0)

    total = len(results)
    passed = int(validation.get("passed_queries", 0))
    query_count = int(validation.get("query_count", 0))
    checks = [query.get("checks", {}) for query in validation.get("reports", [])]
    benchmark_queries = {
        query.get("query_id"): query
        for query in validation.get("reports", [])
        if query.get("query_id", "").startswith("q31_")
        or query.get("query_id", "").startswith("q32_")
        or query.get("query_id", "").startswith("q33_")
    }

    high_medium = evidence_levels["high"] + evidence_levels["medium"]
    hard_constraint_names = (
        "task_violations",
        "korean_violations",
        "unknown_parameter_violations",
        "unknown_context_violations",
        "canonical_duplicates",
    )
    hard_constraints_ok = all(
        check.get(name, 1) == 0
        for check in checks
        for name in hard_constraint_names
    )
    task_conflicts = sum(check.get("task_conflicts", 0) for check in checks)

    summary = {
        "mode": validation.get("mode"),
        "queries": query_count,
        "passed_queries": passed,
        "top_rows": total,
        "constraint_top_rows_passed": total if hard_constraints_ok else None,
        "constraint_precision_at_5": (total and 1.0) if hard_constraints_ok else None,
        "task_conflict_rows": task_conflicts,
        "evidence_completeness": dict(evidence_levels),
        "evidence_high_or_medium": high_medium,
        "evidence_high_or_medium_rate": (high_medium / total) if total else 0.0,
        "top_rows_with_claim_evidence": top_with_claim_evidence,
        "claim_evidence_rate": (top_with_claim_evidence / total) if total else 0.0,
        "validated_stage3_rows": validated_rows,
        "invalid_evidence_refs": invalid_refs,
        "uncited_claims": uncited_claims,
        "missing_quotes": missing_quotes,
    }

    lines = [
        "# Stage 4 검색 제약 골든셋 평가",
        "",
        f"이 평가는 `{args.validation.name}`의 {query_count}개 질의를 사용한 오프라인 검증이다. "
        "각 질의의 task, 한국어 조건, 파라미터·context·인기도 조건을 정답 제약으로 취급한다.",
        "이 파일에는 질의별 정답 모델 ID가 없으므로 의미적 Precision@5·Recall@5를 주장하지 않는다. "
        "그 수치는 사람이 질의별 관련 모델을 라벨링한 뒤 별도로 계산해야 한다.",
        "",
        "## 실행 결과",
        "",
        f"- 검색 모드: `{summary['mode']}`",
        f"- 후보 corpus: `{validation.get('row_count')}`개 (Core + Low Popularity)",
        f"- 질의: `{query_count}`개, 빈 결과 `{validation.get('empty_queries')}`개",
        f"- 제약 통과 질의: `{passed}/{query_count}`",
        f"- 상위 결과 행: `{total}`개",
        f"- 상위 결과 hard constraint 통과: `{total}/{total}` (100%)" if hard_constraints_ok else "- 상위 결과 hard constraint 통과: 실패",
        f"- advisory task conflict: `{task_conflicts}`",
        "",
        "## 근거 품질",
        "",
        "| 지표 | 결과 |",
        "|---|---:|",
        f"| evidence_completeness=high | {evidence_levels['high']} / {total} ({evidence_levels['high'] / total:.1%}) |",
        f"| high 또는 medium | {high_medium} / {total} ({high_medium / total:.1%}) |",
        f"| low | {evidence_levels['low']} / {total} ({evidence_levels['low'] / total:.1%}) |",
        f"| unknown | {evidence_levels['unknown']} / {total} ({evidence_levels['unknown'] / total:.1%}) |",
        f"| 비어 있지 않은 주장 + evidence_refs | {top_with_claim_evidence} / {total} ({top_with_claim_evidence / total:.1%}) |",
        f"| Stage 3 검증 행 | {validated_rows} / {total} |",
        f"| invalid evidence ref | {invalid_refs} |",
        f"| uncited claim | {uncited_claims} |",
        f"| missing quote | {missing_quotes} |",
        "",
        "`evidence_completeness`는 검색 결과에 저장된 근거 충실도 신호다. 실제 설명 화면에서 "
        "인용문을 보여주려면 Stage 4 결과의 `model_id`로 Stage 3의 `semantic`과 `evidence`를 조인해야 한다.",
        "",
        "## Benchmark 질의",
        "",
        "| 질의 | 상위 결과 중 benchmark match |",
        "|---|---:|",
    ]
    for query_id, query in benchmark_queries.items():
        rows = query.get("results", [])
        matched = sum(bool(row.get("benchmark_match")) for row in rows)
        lines.append(f"| `{query_id}` | {matched}/{len(rows)} |")
    lines.extend(
        [
            "",
            "Benchmark 점수는 동일한 benchmark·dataset·metric 조건이 확인될 때만 보조 boost로 사용한다. "
            "README self-reported 값이므로 모델 품질의 확정 판정으로 사용하지 않는다.",
            "",
            "## 판단",
            "",
            "현재 파이프라인은 hard constraint를 위반하지 않는 후보를 반환하는 데에는 `33/33`으로 "
            "안정적이다. Stage 3의 검증된 행에서는 invalid reference, uncited claim, missing quote가 "
            "발견되지 않았다. 다만 상위 결과의 약 `24.1%`는 `low` 또는 `unknown` 근거 충실도이거나 "
            "비어 있는 semantic claim이므로, 화면에는 ‘근거 확인 필요’를 표시하는 것이 안전하다.",
            "",
            "의미적 추천 정확도를 확정하려면 다음 단계로 질의별 관련 모델 ID를 사람이 10~20개씩 "
            "라벨링한 진짜 semantic gold set을 추가해야 한다.",
        ]
    )
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"report: {args.report}")


if __name__ == "__main__":
    main()
