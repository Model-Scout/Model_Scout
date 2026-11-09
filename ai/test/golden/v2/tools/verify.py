#!/usr/bin/env python3
"""골든셋 v2를 기계적으로 검증한다. 사람이 판단할 것과 분리하기 위한 도구다.

사람이 볼 것은 "질의문이 자연스러운가", "조건이 질의문에서 나왔는가"뿐이다.
숫자가 맞는지는 이 스크립트가 전부 확인한다.

    python test/golden/v2/tools/verify.py            # 전체
    python test/golden/v2/tools/verify.py abstention # 한 유형
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_v2  # noqa: E402

V2 = Path(__file__).resolve().parents[1]
QUERY_COUNT_PER_TYPE = 10
HUMAN_REVIEW_LIMIT = 25

# planner.HARD_FILTER_KEYS — 하드 필터가 실제로 읽는 조건만 conditions에 올 수 있다.
HARD_FILTER_KEYS = {
    "pools",
    "tasks",
    "korean_required",
    "max_parameters_billion",
    "min_context_length",
    "max_context_length",
    # 명시적으로 "스펙이 공개된 모델"만 찾는 질의를 지원하기 위해 남겨 둔다.
    # 수치 상·하한 질의에서는 누락 값이 자동 탈락하므로 v2 사양은 이 키를 쓰지 않는다.
    "require_known_parameters",
    "require_known_context",
    "popularity_tier",
    # 데이터 계약 필터. planner.HARD_FILTER_KEYS 와 같아야 한다.
    "commercial_status",
    "require_artifact",
    "max_artifact_gib",
    "exclude_gated",
}


def check_type(query_type: str) -> List[str]:
    path = V2 / "judged" / f"{query_type}.jsonl"
    if not path.exists():
        return [f"{path.name} 없음"]
    with path.open(encoding="utf-8") as handle:
        records = [json.loads(line) for line in handle if line.strip()]

    problems: List[str] = []
    snapshot_meta = json.loads((V2 / "corpus_snapshot.meta.json").read_text(encoding="utf-8"))

    if len(records) != QUERY_COUNT_PER_TYPE:
        problems.append(f"질의 수 {len(records)}개 (기대 {QUERY_COUNT_PER_TYPE}개)")

    print(f"\n{'=' * 78}")
    print(f"{query_type} — 질의 {len(records)}개")
    print("=" * 78)
    print(f"{'id':7s} {'조건키':>6s} {'근거':>5s} {'eligible':>9s} {'기대':>5s} {'판정자':>8s}  결과")
    print("-" * 78)

    seen_ids = set()
    for record in records:
        qid = record["query_id"]
        conditions: Dict[str, Any] = record["conditions"]
        fidelity: Dict[str, Any] = record.get("conditions_fidelity") or {}
        issues: List[str] = []

        if qid in seen_ids:
            issues.append("query_id 중복")
        seen_ids.add(qid)

        # ① conditions의 키가 하드 필터가 읽는 것인지
        unknown = set(conditions) - HARD_FILTER_KEYS
        if unknown:
            issues.append(f"하드 필터가 모르는 조건 {sorted(unknown)}")

        # ② 모든 조건에 질의문 근거가 적혀 있는지 — 1층(완전성)의 검증 수단
        missing = set(conditions) - set(fidelity)
        if missing:
            issues.append(f"질의문 근거 없는 조건 {sorted(missing)}")

        # ③ 기록된 eligible 수가 지금도 재현되는지
        actual = corpus_v2.count(**conditions)
        if actual != record["eligible_count"]:
            issues.append(f"eligible 기록 {record['eligible_count']} ≠ 실측 {actual}")

        # ④ 유형별 불변식
        judged = record.get("judged_by")
        expected = record["expected_behavior"]
        if query_type == "abstention":
            if expected != "abstain":
                issues.append(f"expected_behavior={expected}")
            if actual != 0:
                issues.append(f"abstention인데 후보 {actual}개")
            if record["expected_any"] or record["acceptable"]:
                issues.append("abstention인데 정답이 기록돼 있음")
        else:
            if expected != "recommend":
                issues.append(f"expected_behavior={expected}")
            verification = record.get("verification") or {}
            # 사람 판정 전(judged_by=null)에는 정답이 비어 있는 것이 정상이다.
            # 규칙 스캔이 후보를 전수 훑어 🚩/⚠️로 올려둔 상태다.
            if judged and not record["expected_any"] and not record["acceptable"]:
                issues.append("판정 완료인데 정답이 비어 있음")
            if not judged:
                human_candidates = (
                    len(verification.get("flagged_for_human") or [])
                    + len(verification.get("unsure_for_human") or [])
                )
                if human_candidates == 0:
                    issues.append("추천 질의인데 규칙 스캔 후보가 0개")
                elif human_candidates > HUMAN_REVIEW_LIMIT:
                    issues.append(
                        f"사람 검수 후보 {human_candidates}개 > {HUMAN_REVIEW_LIMIT}개"
                    )
            graded = set(record["expected_any"]) | set(record["acceptable"])
            eligible_ids = {row["model_id"] for row in corpus_v2.eligible(conditions)}
            outside = graded - eligible_ids
            if outside:
                issues.append(f"eligible 밖의 정답 {len(outside)}개 — 검색이 찾을 수 없음")

            # 모델 비교는 각 이름의 계열을 모두 검색해야 답변이 실제 비교가 된다.
            # 후보 생성 시점과 사람 확정 후 모두, 한쪽 계열이 비어 있지 않게 강제한다.
            comparison_groups = record.get("comparison_groups") or {}
            membership = verification.get("comparison_group_membership") or {}
            if comparison_groups:
                for group in comparison_groups:
                    group_candidates = {
                        model_id
                        for model_id, groups in membership.items()
                        if group in groups
                    }
                    if not group_candidates:
                        issues.append(f"비교 대상 {group} 후보가 0개")
                    if judged and not (graded & group_candidates):
                        issues.append(f"판정 완료인데 비교 대상 {group} 정답이 없음")

        # ⑤ 코퍼스 기준이 스냅샷과 같은지
        if record["corpus_snapshot"]["sync_run_id"] != snapshot_meta["last_sync_run_id"]:
            issues.append("다른 코퍼스 스냅샷으로 판정됨")

        mark = "✅" if not issues else "❌ " + " / ".join(issues)
        expect = "0" if query_type == "abstention" else "-"
        print(f"{qid:7s} {len(conditions):6d} {len(fidelity):5d} {actual:9d} "
              f"{expect:>5s} {judged or '미판정':>8s}  {mark}")
        problems.extend(f"{qid}: {issue}" for issue in issues)

    return problems


def main() -> None:
    types = sys.argv[1:] or [
        path.stem for path in sorted((V2 / "judged").glob("*.jsonl"))
    ]
    if not types:
        raise SystemExit("judged/ 가 비어 있습니다")

    meta = json.loads((V2 / "corpus_snapshot.meta.json").read_text(encoding="utf-8"))
    rows = len(corpus_v2.load_rows())
    print(f"판정 기준 코퍼스 {rows}행 (기록 {meta['rows']}행, "
          f"sync_run_id {meta['last_sync_run_id'][:8]}, {meta['corpus_refreshed_at'][:10]})")
    if rows != meta["rows"]:
        raise SystemExit(f"❌ 스냅샷 행 수 불일치: 실제 {rows} ≠ 기록 {meta['rows']}")

    problems: List[str] = []
    for query_type in types:
        problems.extend(check_type(query_type))

    print()
    if problems:
        print(f"❌ 문제 {len(problems)}건")
        for problem in problems:
            print(f"  · {problem}")
        raise SystemExit(1)
    print("✅ 기계 검증 전부 통과")
    print()
    print("남은 것은 사람 판단입니다 — worksheets/<유형>.md 를 보세요.")
    print("  · 질의문이 실제로 누가 물어볼 만한가")
    print("  · 조건이 질의문의 요구를 넘지 않는가")


if __name__ == "__main__":
    main()
