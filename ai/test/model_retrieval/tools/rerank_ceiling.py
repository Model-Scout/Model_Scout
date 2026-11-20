#!/usr/bin/env python3
"""리랭커를 넣을 값이 있는지, 모델 없이 천장으로 먼저 판단한다.

리랭커는 상위 N개를 다시 줄 세우는 것이므로, **정답이 그 N개 안에 들어와 있지
않으면 아무것도 못 한다.** 그래서 "완벽한 리랭커"(N개 안의 정답을 모두 맨 위로)
의 성적을 먼저 구한다. 이게 어떤 리랭커도 넘을 수 없는 선이다.

    oracle@N = min(k, |정답 ∩ 상위N|) / |정답|

이 값이 지금과 비슷하면 리랭커를 넣어도 올라갈 자리가 없다는 뜻이고, 크게
높으면 정답은 이미 가까이 와 있으니 재순위가 효과를 낸다는 뜻이다. N 을 키우며
재서 "몇 개를 다시 세워야 하는지"도 같이 본다.

운영은 need 당 top-5 를 돌려준다(MAX_SEARCH_RESULTS=5). 리랭커를 넣는다면
RPC 에서 N 개를 받아 재순위한 뒤 5개를 내보내는 구조가 된다.

    python test/model_retrieval/tools/rerank_ceiling.py
    python test/model_retrieval/tools/rerank_ceiling.py --run scores_idf_dectf_sg_nt
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import statistics
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Sequence

AI = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RUNS = AI / "test" / "model_retrieval" / "runs"

_spec = importlib.util.spec_from_file_location("fc", HERE / "final_compare.py")
fc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fc)
tune = fc.tune

DEPTHS = (5, 10, 20, 30, 50, 100)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", default="idf_dectf_sg_nt", help="(가) 적용 상태의 측정")
    ap.add_argument("--k", type=int, default=5, help="사용자에게 보여 줄 개수")
    ap.add_argument("--min-grade", type=int, default=2)
    args = ap.parse_args()
    k, mg = args.k, args.min_grade

    run = json.loads((RUNS / f"scores_{args.run}.json").read_text(encoding="utf-8"))
    predicted = fc.predicted_types([q["text"] for q in run["queries"]])

    print(f"{args.run} · 보여 줄 개수 k={k} · min_grade={mg}\n")
    print("완벽한 리랭커의 천장 — 상위 N개를 다시 세웠을 때 recall@k\n")
    header = f"{'유형':22s} {'지금':>7s}" + "".join(f"{f'N={d}':>9s}" for d in DEPTHS)
    print(header)
    print("-" * len(header))

    rows: Dict[str, Dict[str, Any]] = {}
    totals: Dict[Any, List[float]] = {"now": []}
    for depth in DEPTHS:
        totals[depth] = []
    first_hit: List[int] = []
    unreachable = Counter()

    for query_type in sorted(fc.WEIGHTS):
        line = f"{query_type:22s}"
        now_values, by_depth = [], {d: [] for d in DEPTHS}
        for query in run["queries"]:
            if query["query_type"] != query_type:
                continue
            relevant = {m for m, g in query["grades"].items() if g >= mg}
            if not relevant:
                continue
            weight = fc.WEIGHTS.get(predicted.get(query["text"]) or "", fc.PRODUCTION_WEIGHT)
            order = [m for m, _, _ in sorted(
                query["scored"], key=lambda r: (-(weight * r[1] + (1 - weight) * r[2]), r[0]))]
            now_values.append(sum(1 for m in order[:k] if m in relevant) / len(relevant))
            for depth in DEPTHS:
                found = len(relevant & set(order[:depth]))
                by_depth[depth].append(min(k, found) / len(relevant))
            ranks = [i for i, m in enumerate(order, 1) if m in relevant]
            if ranks:
                first_hit.append(min(ranks))
                if min(ranks) > max(DEPTHS):
                    unreachable[query_type] += 1
            else:
                unreachable[query_type] += 1
        totals["now"] += now_values
        line += f"{statistics.mean(now_values):>7.3f}"
        for depth in DEPTHS:
            totals[depth] += by_depth[depth]
            line += f"{statistics.mean(by_depth[depth]):>9.3f}"
        print(line)
        rows[query_type] = {"now": statistics.mean(now_values),
                            **{d: statistics.mean(by_depth[d]) for d in DEPTHS}}

    print("-" * len(header))
    line = f"{'전체':22s}{statistics.mean(totals['now']):>7.3f}"
    for depth in DEPTHS:
        line += f"{statistics.mean(totals[depth]):>9.3f}"
    print(line)

    now = statistics.mean(totals["now"])
    print(f"\n{'N 을 키워서 얻는 몫':22s}" + "".join(
        f"{statistics.mean(totals[d]) - now:>+9.3f}" for d in DEPTHS))

    print(f"""
읽는 법
  N=5 가 '지금'과 같다면 당연하다. 이미 5개를 보여 주고 있다
  N=50 이 크게 높다면 정답은 50위 안에 와 있고 순서만 틀린 것이다 → 리랭커가 듣는다
  N 을 키워도 안 오르면 정답이 아예 멀리 있다 → 리랭커로는 못 건진다""")

    if first_hit:
        print(f"\n첫 정답의 순위: 중앙 {statistics.median(first_hit):.0f}위 · "
              f"상위 10 {sum(1 for r in first_hit if r <= 10)}/{len(first_hit)} · "
              f"상위 50 {sum(1 for r in first_hit if r <= 50)}/{len(first_hit)}")
    if unreachable:
        total = sum(unreachable.values())
        print(f"\n{max(DEPTHS)}위 안에 정답이 하나도 없는 질의 {total}개 — 리랭커로 건질 수 없다")
        for query_type, count in unreachable.most_common():
            print(f"  {query_type:24s} {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
