#!/usr/bin/env python3
"""pre-retrieval 수정을 하나씩 쌓아 재고, 어느 것이 실제로 리콜을 올리는지 가른다.

failure_analysis.py 가 실패를 네 자리로 갈랐다. B(하드 필터가 정답을 죽임)가 42%,
D(순위밖)가 56% 고, C(후보밖)는 0% 였다 — 운영 RPC 는 필터를 통과한 행 전부를
채점하므로(order by similarity limit match_count) 후보 생성이라는 단계가 없다.
그래서 질의 변환(HyDE·multi_query)으로 후보를 넓히는 일은 할 게 없고, 손댈 곳은
B(조건 추출)와 D(점수식)뿐이다.

B 의 범인은 두 개였다.
  tasks (26건)                  분해가 묻지도 않은 분류를 단정한다
  max_parameters_billion (12건) 모델 이름의 "7.8B" 를 크기 상한으로 읽는다

여기서 두 수정의 효과를 운영 sparse(plainto)와 C안(idf) 양쪽에서 잰다. 유형
가중치는 예측 유형으로 고른다(런타임과 같게).

    python test/model_retrieval/tools/fix_ladder.py
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import random
import statistics
from pathlib import Path
from typing import Any, Dict, List, Sequence

AI = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RUNS = AI / "test" / "model_retrieval" / "runs"

_spec = importlib.util.spec_from_file_location("fc", HERE / "final_compare.py")
fc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fc)
tune = fc.tune

STAGES = [
    ("① 운영 현행",        "plainto_dec",          False),
    ("② +분류키",          "plainto_dectf",        False),
    ("③ +크기가드",        "plainto_dectf_sg",     False),
    ("④ +벤치task해제",    "plainto_dectf_sg_nt",  False),
    ("⑤ +유형가중치",      "plainto_dectf_sg_nt",  True),
    ("⑥ +C안 sparse",     "idf_dectf_sg_nt",      True),
]


def load(name: str) -> Dict[str, Any]:
    return json.loads((RUNS / f"scores_{name}.json").read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--min-grade", type=int, default=2)
    args = ap.parse_args()
    k, mg = args.k, args.min_grade

    runs = {name: load(source) for name, source, _ in STAGES}
    predicted = fc.predicted_types([q["text"] for q in runs["① 운영 현행"]["queries"]])

    def weight_of(query: Dict[str, Any], per_type: bool) -> float:
        if not per_type:
            return fc.PRODUCTION_WEIGHT
        return fc.WEIGHTS.get(predicted.get(query["text"]) or "", fc.PRODUCTION_WEIGHT)

    types = sorted(fc.WEIGHTS)
    header = f"{'유형':22s}" + "".join(f"{name[:13]:>15s}" for name, _, _ in STAGES)
    print(f"recall@{k} · min_grade={mg} · 유형은 예측값\n")
    print(header)
    print("-" * len(header))

    totals: Dict[str, List[float]] = {name: [] for name, _, _ in STAGES}
    success: Dict[str, List[float]] = {name: [] for name, _, _ in STAGES}
    for query_type in types:
        line = f"{query_type:22s}"
        for name, _, per_type in STAGES:
            values, hits = [], []
            for query in runs[name]["queries"]:
                if query["query_type"] != query_type:
                    continue
                relevant = {m for m, g in query["grades"].items() if g >= mg}
                if not relevant:
                    continue
                weight = weight_of(query, per_type)
                value = tune.recall_at_k(query["scored"], query["grades"], weight, k=k, min_grade=mg)
                order = [m for m, _, _ in sorted(
                    query["scored"], key=lambda r: (-(weight * r[1] + (1 - weight) * r[2]), r[0]))]
                values.append(value)
                hits.append(1.0 if any(m in relevant for m in order[:k]) else 0.0)
            totals[name] += values
            success[name] += hits
            line += f"{statistics.mean(values) if values else 0.0:>15.3f}"
        print(line)

    print("-" * len(header))
    means = {name: statistics.mean(totals[name]) for name, _, _ in STAGES}
    order_names = [name for name, _, _ in STAGES]
    print(f"{'전체 recall':22s}" + "".join(f"{means[n]:>15.3f}" for n in order_names))
    print(f"{'앞 단계 대비':22s}" + "".join(
        f"{'—':>15s}" if i == 0 else f"{means[order_names[i]] - means[order_names[i-1]]:>+15.3f}"
        for i in range(len(order_names))))
    print(f"{'성공률(≥1개 적중)':22s}" + "".join(
        f"{statistics.mean(success[n]):>14.0%} " for n in order_names))

    first, last = order_names[0], order_names[-1]
    base = {q["qid"]: q for q in runs[first]["queries"]}
    deltas = []
    for query in runs[last]["queries"]:
        other = base.get(query["qid"])
        if other is None:
            continue
        a = tune.recall_at_k(other["scored"], other["grades"], fc.PRODUCTION_WEIGHT, k=k, min_grade=mg)
        b = tune.recall_at_k(query["scored"], query["grades"], weight_of(query, True), k=k, min_grade=mg)
        if a == a and b == b:
            deltas.append(b - a)
    boot = tune.paired_bootstrap(deltas, random.Random(tune.SEED))
    mark = "✅ 유의함" if boot["lo"] > 0 else "— 유의하지 않음"
    print(f"\n{first} → {last}: {means[first]:.3f} → {means[last]:.3f}  "
          f"절대 {means[last]-means[first]:+.3f} · 상대 {(means[last]/means[first]-1)*100:+.0f}%")
    print(f"짝지은 부트스트랩 {len(deltas)}질의: {boot['mean']:+.3f} "
          f"[{boot['lo']:+.3f}, {boot['hi']:+.3f}]  {mark}")

    # SQL 없이 지금 배포할 수 있는 구간
    shipped = order_names[4]
    print(f"\nSQL 없이 배포 가능한 구간({first} → {shipped}): "
          f"{means[first]:.3f} → {means[shipped]:.3f} "
          f"({(means[shipped]/means[first]-1)*100:+.0f}%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
