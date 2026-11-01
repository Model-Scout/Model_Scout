#!/usr/bin/env python3
"""미판정을 오답으로 세지 않는 보정 지표로 실험을 다시 채점한다.

왜 필요한가
-----------
판정 풀이 BM25 + 다운로드 상위로 만들어졌는데(`test/golden/build_judging_pool.py`)
실제 검색은 Dense + Sparse 하이브리드다. 풀 밖에서 온 결과는 미판정이고, 미판정은
오답으로 계산된다. 그래서 Recall 차이가 품질 차이인지 "풀과 얼마나 닮았나"인지
구분되지 않는다.

보정(Sakai의 condensed list)은 순위에서 미판정을 빼고 남은 순위로 지표를 계산한다.
미판정을 끌어온 것에 벌점을 주지 않는다.

    원래   Recall@10 = |정답 ∩ top-10|            / |정답|
    보정   Recall@10 = |정답 ∩ (판정된 것만 앞 10개)| / |정답|

한계: 미판정이 판정된 것과 같은 비율로 정답을 담고 있다고 가정한다. 낙관 쪽으로
치우치므로 원래 수치와 나란히 읽는다. 둘이 같은 방향이면 그 결론은 믿을 만하고,
갈라지면 라벨을 더 채워야 한다.

실행:
    python -m retrieval_lab.condensed_eval --types lexical_exact
    python -m retrieval_lab.condensed_eval --types benchmark_lookup --weights
    python -m retrieval_lab.condensed_eval --types structured_constraint --pool-check
"""

from __future__ import annotations

import argparse
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

from retrieval_lab import corpus as corpus_mod, golden
from retrieval_lab.pipeline import Retriever
from retrieval_lab.planner import (
    BASELINE,
    ELEMENTS,
    PLAN_QUERY_TYPES,
    RetrievalPlan,
    hard_filter_plan,
    with_dense_weight,
    with_strategies,
)

# experiment.py의 KNOWN_ONLY_FILTERS와 같은 값. 하드 필터 실험도 함께 비교한다.
KNOWN_ONLY_FILTERS = {"require_known_parameters": True, "require_known_context": True}
WEIGHT_GRID = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)


def arms(query_type: str) -> List[Tuple[str, RetrievalPlan]]:
    """Baseline · 사전 검색 단일 · 하드 필터. experiment.py의 single 단계와 같은 구성."""
    base = replace(BASELINE, query_type=query_type)
    out = [("Baseline", with_strategies(base, ()))]
    out += [(name.replace("_", "-"), with_strategies(base, (name,))) for name in ELEMENTS]
    out.append(("Known values only", replace(base, hard_filters=dict(KNOWN_ONLY_FILTERS))))
    return out


def score(retriever: Retriever, queries: Sequence[golden.GoldenQuery], plan: RetrievalPlan,
          min_grade: int, k: int = 10) -> Dict[str, float]:
    """원래 Recall@k, 보정 Recall@k, Judged@k의 질의 평균."""
    raw: List[float] = []
    condensed: List[float] = []
    judged_rate: List[float] = []
    for query in queries:
        relevant = {model_id for model_id, grade in query.grades.items() if grade >= min_grade}
        if not relevant:
            continue
        query_plan = replace(plan, query_type=query.plan_query_type,
                             hard_filters=hard_filter_plan(plan.hard_filters, query.query))
        ranked = retriever.run(query.text, query_plan).ranked
        judged = query.judged or set()
        head = ranked[:k]
        raw.append(len(relevant & set(head)) / len(relevant))
        # 미판정을 뺀 순위에서 앞 k개
        kept = [model_id for model_id in ranked if model_id in judged][:k]
        condensed.append(len(relevant & set(kept)) / len(relevant))
        judged_rate.append(sum(1 for m in head if m in judged) / len(head) if head else 0.0)
    n = len(raw)
    if not n:
        return {}
    return {"raw": sum(raw) / n, "condensed": sum(condensed) / n,
            "judged": sum(judged_rate) / n, "queries": n}


def verdict(label: str, row: Dict[str, float], base: Dict[str, float]) -> str:
    """원래와 보정이 같은 방향인지. 갈라지면 라벨을 더 채워야 한다는 신호다."""
    if label == "Baseline" or not row or not base:
        return ""
    was = row["raw"] - base["raw"]
    now = row["condensed"] - base["condensed"]
    sign = lambda d: "개선" if d > 1e-9 else ("저하" if d < -1e-9 else "동일")
    flip = "  ** 뒤집힘 **" if sign(was) != sign(now) else ""
    return "%+.1f%% → %+.1f%%   %s → %s%s" % (
        100 * was / base["raw"] if base["raw"] else 0.0,
        100 * now / base["condensed"] if base["condensed"] else 0.0,
        sign(was), sign(now), flip)


def pool_check(retriever: Retriever, queries: Sequence[golden.GoldenQuery],
               query_type: str, supplement: Path | None) -> None:
    """보완 라벨이 Baseline top-10에서만 왔는지 — 왔다면 비교가 순환한다."""
    if supplement is None or not supplement.exists():
        print("  (--supplement 파일이 없어 건너뜀)")
        return
    base_plan = with_strategies(replace(BASELINE, query_type=query_type), ())
    tops = {}
    for query in queries:
        query_plan = replace(base_plan, query_type=query.plan_query_type,
                             hard_filters=hard_filter_plan({}, query.query))
        tops[query.query_id] = set(retriever.run(query.text, query_plan).ranked[:10])
    marks = [mark for marks in golden.load_supplement(supplement).values() for mark in marks]
    mine = [m for m in marks if m["query_id"] in tops]
    inside = sum(1 for m in mine if m["model_id"] in tops[m["query_id"]])
    if not mine:
        print("  이 유형에 해당하는 보완 라벨 없음")
        return
    print("  보완 %d건 중 Baseline top-10에 있던 것 %d건 (%.0f%%)"
          % (len(mine), inside, 100.0 * inside / len(mine)))
    if inside == len(mine):
        print("  → 전부 Baseline에서 왔다. Baseline에서 멀어지는 설정이 불리해지는 순환이다.")
        print("    합집합 판정(pooled judgment)으로 메워야 한다.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--types", nargs="+", default=["lexical_exact", "structured_constraint"],
                        help="채점할 plan_query_type")
    parser.add_argument("--supplement", type=Path, default=None,
                        help="추가 판정 파일. 생략하면 유형별 기본 파일을 찾고, 없으면 공유 라벨만 쓴다")
    parser.add_argument("--min-grade", type=int, default=1, help="관련으로 셀 최소 점수")
    parser.add_argument("--weights", action="store_true", help="가중치 곡선도 보정해서 본다")
    parser.add_argument("--pool-check", action="store_true", help="보완 라벨의 출처를 점검한다")
    args = parser.parse_args()

    unknown = sorted(set(args.types) - set(PLAN_QUERY_TYPES))
    if unknown:
        parser.error(f"알 수 없는 유형: {unknown}")

    rows = corpus_mod.load_rows()
    retriever = Retriever(rows)
    corpus_ids = {row["model_id"] for row in rows}

    for query_type in args.types:
        supplement = args.supplement
        if supplement is None:
            guess = golden.LABEL_DIR / f"supplement_{query_type}.jsonl"
            supplement = guess if guess.exists() else None
        queries = golden.load(corpus_ids=corpus_ids, types=[query_type], supplement_path=supplement)
        if not queries:
            print(f"\n[{query_type}] 라벨된 질의 없음, 건너뜀")
            continue

        label_src = supplement.name if supplement else "공유 라벨만"
        print("\n" + "=" * 86)
        print(f"{query_type}  질의 {len(queries)}개  ·  min_grade={args.min_grade}  ·  {label_src}")
        print("=" * 86)
        print("%-20s %8s %9s %10s  %s" % ("실험", "원래", "보정", "Judged@10", "차이"))

        base: Dict[str, float] = {}
        for label, plan in arms(query_type):
            row = score(retriever, queries, plan, args.min_grade)
            if not row:
                continue
            if label == "Baseline":
                base = row
            print("%-20s %8.3f %9.3f %10.3f  %s"
                  % (label, row["raw"], row["condensed"], row["judged"], verdict(label, row, base)))

        if args.weights:
            print("\n가중치 곡선 (사전 검색 OFF)")
            print("%-20s %8s %9s %10s" % ("dense", "원래", "보정", "Judged@10"))
            for dense in WEIGHT_GRID:
                plan = with_dense_weight(replace(BASELINE, query_type=query_type), dense)
                row = score(retriever, queries, plan, args.min_grade)
                if row:
                    print("%-20.1f %8.3f %9.3f %10.3f"
                          % (dense, row["raw"], row["condensed"], row["judged"]))
            print("  정점이 원래와 보정에서 다르면 그 '최적 가중치'는 판정 커버리지의 산물이다.")

        if args.pool_check:
            print("\n판정 풀 순환 점검")
            pool_check(retriever, queries, query_type, supplement)


if __name__ == "__main__":
    main()
