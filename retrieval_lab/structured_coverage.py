#!/usr/bin/env python3
"""structured_constraint 질의의 조건을 만족하는 모델이 코퍼스에 몇 개인지 센다.

이 유형은 조건이 수치(파라미터·context)와 라이선스다. 둘 다 코퍼스 필드로
기계 검증되지만, parameter_count는 코퍼스의 약 39%가 비어 있다. 그래서 같은
질의도 "모르는 값을 통과시키느냐"에 따라 후보 수가 크게 달라진다.

세 가지를 함께 센다.

    strict     값을 아는 모델 중 조건을 만족하는 것만 (require_known=true)
    lenient    값이 없는 모델도 통과 (require_known=false, 현재 기본값)
    unknown    조건 필드가 비어 있어 판정할 수 없는 모델

lenient와 strict의 차이가 곧 "필터가 거르지 못하고 흘려보내는 양"이고,
sg_h004에서 50M 이하 질의에 2B~12B 모델이 올라온 원인이다.

실행:
    python -m retrieval_lab.structured_coverage
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
LABEL_DIR = ROOT / "test" / "golden" / "labels"
POOLS = ("core", "low_popularity")
QUERY_FILES = ("semantic_golden_queries.jsonl", "semantic_judged_queries.jsonl")

# 채점용 임시 라이선스 정책. 골든셋 README가 쓰는 기준과 같다.
COMMERCIAL_OK = {"apache-2.0", "mit", "bsd-3-clause", "bsd", "cc-by-4.0", "cc0-1.0",
                 "cc-by-sa-4.0", "openrail", "openmdw-1.1", "gpl-3.0", "agpl-3.0"}
COMMERCIAL_BLOCKED_MARK = "nc"  # cc-by-nc-4.0 등
# other/gemma/llama/미기재는 '확인 필요'로 두고 위반으로 세지 않는다.


def load_corpus() -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for pool in POOLS:
        path = DATA_DIR / f"hf_models_stage4_{pool}.jsonl"
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    rows.append(json.loads(line))
    return rows


def load_queries() -> List[Dict[str, Any]]:
    queries: List[Dict[str, Any]] = []
    for name in QUERY_FILES:
        path = LABEL_DIR / name
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    item = json.loads(line)
                    if item.get("plan_query_type") == "structured_constraint":
                        queries.append(item)
    return queries


def task_ok(row: Dict[str, Any], tasks: Sequence[str]) -> bool:
    if not tasks:
        return True
    meta = row["filter_metadata"]
    if meta.get("primary_task") in tasks:
        return True
    return bool(set(meta.get("matched_tasks") or []) & set(tasks))


def license_violates(row: Dict[str, Any], requirement: Optional[str]) -> bool:
    """상업 조건에서 명백한 위반만 센다. other/미기재는 '확인 필요'로 둔다."""
    if requirement != "commercial":
        return False
    value = str(row["filter_metadata"].get("license") or "").lower()
    return COMMERCIAL_BLOCKED_MARK in value.split("-")


def count_query(rows: Sequence[Dict[str, Any]], query: Dict[str, Any]) -> Dict[str, int]:
    tasks = query.get("tasks") or []
    max_param = query.get("max_parameters_billion")
    min_context = query.get("min_context_length")
    requirement = query.get("license_requirement")

    pool = [row for row in rows
            if row["filter_metadata"].get("korean_verified")
            and task_ok(row, tasks)
            and not license_violates(row, requirement)]

    strict = lenient = unknown = 0
    for row in pool:
        meta = row["filter_metadata"]
        missing = False
        passes = True
        if max_param is not None:
            value = meta.get("parameter_count_billion")
            if value is None:
                missing = True
            elif value > max_param:
                passes = False
        if min_context is not None:
            value = meta.get("context_length")
            if value is None:
                missing = True
            elif value < min_context:
                passes = False
        if not passes:
            continue
        if missing:
            unknown += 1
            lenient += 1          # 현재 기본값은 unknown을 통과시킨다
        else:
            strict += 1
            lenient += 1
    return {"pool": len(pool), "strict": strict, "lenient": lenient, "unknown": unknown}


def main() -> None:
    rows = load_corpus()
    queries = load_queries()
    print(f"코퍼스 {len(rows):,}개 · structured_constraint 질의 {len(queries)}개\n")

    header = (f"{'질의':<10} {'조건':<34} {'task풀':>7} {'strict':>7} "
              f"{'lenient':>8} {'unknown':>8}")
    print(header)
    print("-" * len(header))

    totals = {"strict": 0, "lenient": 0, "unknown": 0}
    for query in queries:
        parts = []
        if query.get("max_parameters_billion") is not None:
            parts.append(f"param<={query['max_parameters_billion']}B")
        if query.get("min_context_length") is not None:
            parts.append(f"ctx>={query['min_context_length']}")
        if query.get("license_requirement") == "commercial":
            parts.append("상업")
        counts = count_query(rows, query)
        for key in totals:
            totals[key] += counts[key]
        print(f"{query['id']:<10} {' · '.join(parts) or '수치 조건 없음':<34} "
              f"{counts['pool']:>7} {counts['strict']:>7} "
              f"{counts['lenient']:>8} {counts['unknown']:>8}")

    print(f"\n합계 strict {totals['strict']:,} · lenient {totals['lenient']:,} "
          f"· 그중 판정 불가 {totals['unknown']:,}")
    if totals["lenient"]:
        share = totals["unknown"] / totals["lenient"] * 100
        print(f"lenient 후보의 {share:.0f}%가 조건 값을 모르는 채 통과한다.")

    # 조건 필드별 코퍼스 결측률
    known_param = sum(1 for row in rows
                      if row["filter_metadata"].get("parameter_count_billion") is not None)
    known_context = sum(1 for row in rows
                        if row["filter_metadata"].get("context_length") is not None)
    print(f"\n코퍼스 결측률  parameter_count {len(rows) - known_param:,}/{len(rows):,} "
          f"({(len(rows)-known_param)/len(rows)*100:.0f}%) · "
          f"context_length {len(rows) - known_context:,}/{len(rows):,} "
          f"({(len(rows)-known_context)/len(rows)*100:.0f}%)")


if __name__ == "__main__":
    main()
