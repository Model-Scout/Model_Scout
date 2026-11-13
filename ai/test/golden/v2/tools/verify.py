#!/usr/bin/env python3
"""골든셋 v2를 기계적으로 검증한다. 사람이 판단할 것과 분리하기 위한 도구다.

사람이 볼 것은 "질의문이 자연스러운가", "조건이 질의문에서 나왔는가"뿐이다.
숫자가 맞는지는 이 스크립트가 전부 확인한다.

    python test/golden/v2/tools/verify.py            # 전체
    python test/golden/v2/tools/verify.py abstention # 한 유형
    python test/golden/v2/tools/verify.py --structure-only

--structure-only 는 코퍼스 스냅샷(corpus_snapshot.jsonl, gitignore 대상) 없이 질의 파일의
형식·ID 중복·유형별 개수·조건 키·조건 근거만 본다. eligible 수와 정답 후보는 스냅샷에
묶인 값이라 그 스냅샷이 있는 곳에서만 전체 검증으로 확인한다. 재적재 Action 이 이 모드를 쓴다.
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


REQUIRED_KEYS = (
    "query_id",
    "query_type",
    "query",
    "conditions",
    "conditions_fidelity",
    "expected_behavior",
    "expected_any",
    "acceptable",
    "eligible_count",
    "corpus_snapshot",
)


def read_records(query_type: str, judged_dir: Path = None) -> List[Dict[str, Any]]:
    path = (judged_dir or V2 / "judged") / f"{query_type}.jsonl"
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def structure_issues(record: Dict[str, Any], query_type: str) -> List[str]:
    """스냅샷 없이 판단할 수 있는 한 질의의 문제."""
    missing_keys = [key for key in REQUIRED_KEYS if key not in record]
    if missing_keys:
        return [f"필수 키 없음 {missing_keys}"]
    issues: List[str] = []
    if record["query_type"] != query_type:
        issues.append(f"query_type={record['query_type']} (파일은 {query_type})")
    if not isinstance(record["query"], str) or not record["query"].strip():
        issues.append("질의문이 비어 있음")
    conditions = record["conditions"]
    fidelity = record["conditions_fidelity"] or {}
    if not isinstance(conditions, dict) or not isinstance(fidelity, dict):
        return issues + ["conditions/conditions_fidelity 가 객체가 아님"]
    # ① conditions의 키가 하드 필터가 읽는 것인지
    unknown = set(conditions) - HARD_FILTER_KEYS
    if unknown:
        issues.append(f"하드 필터가 모르는 조건 {sorted(unknown)}")
    # ② 모든 조건에 질의문 근거가 적혀 있는지 — 1층(완전성)의 검증 수단
    missing = {key for key in conditions if not str(fidelity.get(key) or "").strip()}
    if missing:
        issues.append(f"질의문 근거 없는 조건 {sorted(missing)}")
    expected = record["expected_behavior"]
    wanted = "abstain" if query_type == "abstention" else "recommend"
    if expected != wanted:
        issues.append(f"expected_behavior={expected}")
    if query_type == "abstention" and (record["expected_any"] or record["acceptable"]):
        issues.append("abstention인데 정답이 기록돼 있음")
    return issues


def check_structure(types: List[str], judged_dir: Path = None) -> List[str]:
    """--structure-only. 질의 ID 는 유형을 넘어 유일해야 한다."""
    problems: List[str] = []
    seen: Dict[str, str] = {}
    for query_type in types:
        path = (judged_dir or V2 / "judged") / f"{query_type}.jsonl"
        if not path.exists():
            problems.append(f"{path.name} 없음")
            continue
        try:
            records = read_records(query_type, judged_dir)
        except json.JSONDecodeError as error:
            problems.append(f"{path.name}: JSON 형식 오류 {error}")
            continue
        if len(records) != QUERY_COUNT_PER_TYPE:
            problems.append(f"{query_type}: 질의 수 {len(records)}개 (기대 {QUERY_COUNT_PER_TYPE}개)")
        for record in records:
            qid = record.get("query_id", "?")
            if qid in seen:
                problems.append(f"{qid}: query_id 중복 ({seen[qid]}, {query_type})")
            seen[qid] = query_type
            problems.extend(f"{qid}: {issue}" for issue in structure_issues(record, query_type))
    return problems


def check_type(query_type: str) -> List[str]:
    path = V2 / "judged" / f"{query_type}.jsonl"
    if not path.exists():
        return [f"{path.name} 없음"]
    records = read_records(query_type)

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
    args = sys.argv[1:]
    structure_only = "--structure-only" in args
    types = [arg for arg in args if arg != "--structure-only"] or [
        path.stem for path in sorted((V2 / "judged").glob("*.jsonl"))
    ]
    if not types:
        raise SystemExit("judged/ 가 비어 있습니다")
    if structure_only:
        problems = check_structure(types)
        if problems:
            print(f"❌ 구조 문제 {len(problems)}건")
            for problem in problems:
                print(f"  · {problem}")
            raise SystemExit(1)
        print(f"✅ 구조 검증 통과 — {len(types)}개 유형 (코퍼스 스냅샷 기반 eligible 검증은 하지 않음)")
        return

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
