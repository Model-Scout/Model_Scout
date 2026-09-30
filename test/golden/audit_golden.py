#!/usr/bin/env python3
"""Audit the semantic golden labels without any API call.

Two kinds of checks per query:
1. Source reliability: case confidence, URL check, whether an original quote
   backs the label, and whether the answer had to be mapped to a variant.
2. Label consistency against the DB: the expected answer must survive the same
   hard filters the retriever uses, must_exclude models must actually violate
   the stated rule, and expected models must not violate the query's license.

Each query gets a reliability tier (A/B/C) and a list of issues. Label errors
(an evaluable query whose answer can never be retrieved, a must_exclude that
does not violate its rule) are reported separately so they get fixed before
metrics are trusted.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[2]
GOLDEN_DIR = ROOT / "test" / "golden"
QUERY_PATH = GOLDEN_DIR / "semantic_golden_queries.jsonl"
CASE_PATHS = (
    GOLDEN_DIR / "korean_model_selection_cases_v2.jsonl",
    GOLDEN_DIR / "korean_model_selection_cases_round2.jsonl",
)
OUTPUT_JSON = GOLDEN_DIR / "golden_audit.json"
OUTPUT_MD = GOLDEN_DIR / "golden_audit.md"


def load_module(name: str, path: Path):
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def audit_query(query: Dict[str, Any], case: Dict[str, Any], rows: Dict[str, Dict[str, Any]], validator, scorer) -> Dict[str, Any]:
    labels = query["labels"]
    behavior = labels["expected_behavior"]
    commercial = query.get("license_requirement") == "commercial"
    issues: List[str] = []
    errors: List[str] = []

    def eligible(model_id: str) -> bool:
        row = rows.get(model_id.casefold())
        return bool(row) and validator.hard_filter(row, query)[0]

    expected_in_db = [m for m in labels["expected_any"] if m.casefold() in rows]
    expected_reachable = [m for m in expected_in_db if eligible(m)]
    acceptable_reachable = [m for m in labels["acceptable"] if eligible(m)]
    selected = {(item.get("model_id") or "").casefold() for item in case.get("selected", [])} - {""}
    original_reachable = [m for m in expected_reachable if m.casefold() in selected]

    if query.get("evaluable_now") and behavior == "recommend":
        if not expected_reachable:
            errors.append("정답 모델이 DB에 없거나 조건 필터를 통과하지 못함")
        elif not original_reachable:
            issues.append("사례 원본이 아닌 변환본으로만 정답 도달")
        filtered_out = [m for m in expected_in_db if m not in expected_reachable]
        if filtered_out:
            issues.append("DB에 있지만 필터에서 탈락하는 정답: " + ", ".join(filtered_out))
    if commercial:
        for model_id in expected_in_db:
            if scorer.license_class(rows[model_id.casefold()].get("license")) == "noncommercial":
                errors.append(f"상업 조건인데 정답이 비상업 라이선스: {model_id}")
    for item in labels["must_exclude"]:
        row = rows.get(item["model_id"].casefold())
        if not row:
            issues.append(f"must_exclude가 DB에 없어 검증이 공허함: {item['model_id']}")
            continue
        if item.get("violated_rule") == "license_commercial" and scorer.license_class(row.get("license")) == "commercial_ok":
            errors.append(f"must_exclude 라이선스가 상업 허용으로 기록됨: {item['model_id']} ({row.get('license')})")
    if behavior == "must_exclude_only" and not any(item["model_id"].casefold() in rows for item in labels["must_exclude"]):
        errors.append("must_exclude 모델이 모두 DB에 없어 채점이 항상 통과함")

    confidence = case.get("confidence") or "unknown"
    has_quote = bool(query.get("evidence_quote"))
    url_status = (case.get("url_check") or {}).get("status")
    if not has_quote:
        issues.append("정답 근거 원문 인용 없음")
    if url_status not in ("exists_fetched", "exists_search_confirmed"):
        issues.append(f"URL 확인 안 됨({url_status})")
    if query["label_type"] == "derived_counterfactual":
        issues.append("원 사례에 조건을 추가한 파생 질의")

    mapped = behavior == "recommend" and expected_reachable and not original_reachable
    if confidence == "low":
        tier = "C"
    elif confidence == "high" and has_quote and not mapped:
        tier = "A"
    else:
        tier = "B"

    return {
        "query_id": query["id"],
        "source_case_id": query["source_case_id"],
        "label_type": query["label_type"],
        "evaluable_now": query.get("evaluable_now"),
        "task": query["tasks"][0],
        "tier": tier,
        "case_confidence": confidence,
        "has_quote": has_quote,
        "url_status": url_status,
        "expected_reachable": expected_reachable,
        "acceptable_reachable": acceptable_reachable,
        "issues": issues,
        "errors": errors,
    }


def render_markdown(audits: List[Dict[str, Any]]) -> str:
    evaluable = [item for item in audits if item["evaluable_now"]]
    tiers = Counter(item["tier"] for item in evaluable)
    errors = [item for item in audits if item["errors"]]
    lines = [
        "# Semantic 골든셋 라벨 점검",
        "",
        "API 호출 없이 라벨의 출처 신뢰도와 DB 정합성을 점검한 결과다. `audit_golden.py`로 재생성한다.",
        "",
        "## 신뢰도 등급 기준",
        "",
        "| 등급 | 기준 |",
        "|---|---|",
        "| A | 사례 confidence=high, 원문 인용 있음, 사례가 고른 원본 모델이 그대로 정답으로 도달 |",
        "| B | confidence=medium, 또는 인용 없음, 또는 변환본(GGUF 등)으로 매핑해야 정답 도달 |",
        "| C | confidence=low (모델 비교 없이 사용만 기록한 사례 등) |",
        "",
        "## 요약",
        "",
        f"- 전체 질의 {len(audits)}개, 채점 가능 {len(evaluable)}개",
        f"- 채점 가능 질의 등급: A {tiers.get('A', 0)} · B {tiers.get('B', 0)} · C {tiers.get('C', 0)}",
        f"- 라벨 오류: {len(errors)}개 질의",
        "",
        "## 라벨 오류",
        "",
    ]
    if errors:
        for item in errors:
            lines.append(f"- `{item['query_id']}`: " + "; ".join(item["errors"]))
    else:
        lines.append("없음. 채점 가능한 모든 질의의 정답이 조건 필터를 통과하고, must_exclude는 실제로 규칙을 위반한다.")
    lines += [
        "",
        "## 질의별 점검",
        "",
        "| 질의 | 사례 | task | 채점 | 등급 | 도달 가능한 정답 | 주의 |",
        "|---|---|---|---|---|---:|---|",
    ]
    for item in audits:
        lines.append(
            f"| `{item['query_id']}` | {item['source_case_id']} | {item['task']} | {'✅' if item['evaluable_now'] else '-'} "
            f"| {item['tier']} | {len(item['expected_reachable'])} | {'; '.join(item['issues']) or '-'} |"
        )
    lines += [
        "",
        "## 이 점검이 보장하지 않는 것",
        "",
        "- 정답이 **유일하게** 맞는지는 보장하지 않는다. 사례에 없던 더 좋은 모델이 DB에 있으면 검색이 맞아도 오답으로 집계된다.",
        "  채점 리포트에서 틀린 질의의 top-k를 사람이 보고 acceptable에 추가하는 누락 점검(false negative audit)이 필요하다.",
        "- 사례 작성자의 판단이 옳은지는 검증하지 않는다. 등급은 근거의 강도이지 정답의 품질이 아니다.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--queries", type=Path, default=QUERY_PATH)
    parser.add_argument("--output-json", type=Path, default=OUTPUT_JSON)
    parser.add_argument("--output-md", type=Path, default=OUTPUT_MD)
    args = parser.parse_args()

    validator = load_module("model_scout_validator", ROOT / "05_validate_retrieval.py")
    scorer = load_module("model_scout_semantic_eval", ROOT / "test" / "evaluate_semantic_golden.py")
    cases = {case["case_id"]: case for path in CASE_PATHS for case in read_jsonl(path)}
    rows = {row["model_id"].casefold(): row for row in validator.load_rows()}
    stage2 = {row["model_id"].casefold(): row for pool in validator.POOLS
              for row in read_jsonl(ROOT / "data" / f"hf_models_stage2_{pool}.jsonl")}
    for key, row in rows.items():
        row["license"] = (stage2.get(key) or {}).get("license", (row.get("filter_metadata") or {}).get("license"))

    audits = [audit_query(query, cases.get(query["source_case_id"], {}), rows, validator, scorer)
              for query in read_jsonl(args.queries)]
    args.output_json.write_text(json.dumps(audits, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.output_md.write_text(render_markdown(audits), encoding="utf-8")
    evaluable = [item for item in audits if item["evaluable_now"]]
    print(json.dumps({
        "queries": len(audits),
        "evaluable": len(evaluable),
        "tiers": dict(Counter(item["tier"] for item in evaluable)),
        "queries_with_errors": [item["query_id"] for item in audits if item["errors"]],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
