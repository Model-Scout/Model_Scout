#!/usr/bin/env python3
"""recall@5 가 낮은 것이 검색 탓인지 지표 탓인지 가른다.

정답이 20개인 질의에서 5개만 돌려주면 recall@5 는 아무리 잘해도 0.25 다.
골든셋의 정답 집합이 크면 recall@5 의 **천장**이 1 이 아니다. 그 천장을 먼저
재고, 천장 대비 얼마나 왔는지(= 달성률)를 본다.

서비스가 실제로 물어야 하는 것은 다르다. "쓸 만한 모델이 상위 5개 안에 하나라도
있었나" 다. 그것이 success@5 다.

    python test/model_retrieval/tools/metric_sanity.py
"""

from __future__ import annotations

import argparse
import importlib.util
import json
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


def ranked(query: Dict[str, Any], weight: float) -> List[str]:
    rows = sorted(query["scored"], key=lambda r: (-(weight * r[1] + (1 - weight) * r[2]), r[0]))
    return [m for m, _, _ in rows]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--min-grade", type=int, default=2)
    args = ap.parse_args()
    k, mg = args.k, args.min_grade

    run = json.loads((RUNS / "scores_idf_dectf.json").read_text(encoding="utf-8"))
    base = json.loads((RUNS / "scores_plainto_dec.json").read_text(encoding="utf-8"))
    predicted = fc.predicted_types([q["text"] for q in run["queries"]])

    def weight_for(query: Dict[str, Any]) -> float:
        return fc.WEIGHTS.get(predicted.get(query["text"]) or "", fc.PRODUCTION_WEIGHT)

    print(f"지표 점검 · k={k} · min_grade={mg}\n")
    print(f"{'유형':22s} {'정답수':>6s} {'천장':>7s} {'현행':>7s} {'교체후':>7s} "
          f"{'달성률':>7s} {'성공률':>7s} {'1등적중':>7s}")
    print("-" * 82)

    rows: List[Dict[str, Any]] = []
    for query_type in sorted(fc.WEIGHTS):
        qs = [q for q in run["queries"] if q["query_type"] == query_type]
        bq = {q["qid"]: q for q in base["queries"] if q["query_type"] == query_type}
        sizes, ceil, got, old, success, top1 = [], [], [], [], [], []
        for q in qs:
            relevant = {m for m, g in q["grades"].items() if g >= mg}
            if not relevant:
                continue
            sizes.append(len(relevant))
            ceil.append(min(k, len(relevant)) / len(relevant))
            order = ranked(q, weight_for(q))
            got.append(sum(1 for m in order[:k] if m in relevant) / len(relevant))
            success.append(1.0 if any(m in relevant for m in order[:k]) else 0.0)
            top1.append(1.0 if order and order[0] in relevant else 0.0)
            other = bq.get(q["qid"])
            if other:
                old.append(tune.recall_at_k(other["scored"], other["grades"],
                                            fc.PRODUCTION_WEIGHT, k=k, min_grade=mg))
        old = [v for v in old if v == v]
        rate = statistics.mean(got) / statistics.mean(ceil)
        print(f"{query_type:22s} {statistics.median(sizes):>6.0f} {statistics.mean(ceil):>7.3f} "
              f"{statistics.mean(old):>7.3f} {statistics.mean(got):>7.3f} "
              f"{rate:>6.0%} {statistics.mean(success):>7.0%} {statistics.mean(top1):>7.0%}")
        rows.append({"type": query_type, "ceiling": statistics.mean(ceil), "got": statistics.mean(got),
                     "old": statistics.mean(old), "success": statistics.mean(success),
                     "top1": statistics.mean(top1), "n": len(got)})

    print("-" * 82)
    total = sum(r["n"] for r in rows)
    def wavg(key: str) -> float:
        return sum(r[key] * r["n"] for r in rows) / total
    print(f"{'전체':22s} {'':>6s} {wavg('ceiling'):>7.3f} {wavg('old'):>7.3f} "
          f"{wavg('got'):>7.3f} {wavg('got')/wavg('ceiling'):>6.0%} "
          f"{wavg('success'):>7.0%} {wavg('top1'):>7.0%}")

    print(f"""
읽는 법
  정답수   그 유형 질의의 정답 개수 중앙값. 이것이 크면 recall@{k} 천장이 낮다
  천장     상위 {k}개를 전부 정답으로 채웠을 때의 recall@{k}. 1.0 이 아니다
  달성률   교체 후 / 천장. 지표의 한계를 뺀 실제 성적
  성공률   상위 {k}개 안에 정답이 하나라도 있던 질의 비율  ← 사용자가 겪는 것
  1등적중  1등이 정답이던 비율. 데이터셋 추천이 이 1등에만 걸린다""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
