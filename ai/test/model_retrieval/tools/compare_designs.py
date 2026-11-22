#!/usr/bin/env python3
"""sparse 설계들을 서로 비교한다. 기준은 "지금 운영"이다.

tune.py 는 한 설계 안에서 가중치만 비교한다. 설계를 바꾸는 판단에는 설계 사이의
비교가 필요하고, 그때 두 가지를 틀리기 쉽다.

  ① 설계마다 제 가중치로 최고점을 뽑아 비교하면, 고른 자리에서 재는 것이라
     이득이 부풀려진다. → 폴드 4개로 가중치를 고르고 남은 폴드에서만 잰다.
  ② 설계마다 질의 집합이 조금 다르면(정답 0개로 빠지는 질의) 평균이 안 맞는다.
     → 모든 설계에 공통으로 있는 질의만 쓴다.

기준선은 **운영 현행**이다. plainto 설계 · dense_weight 0.65 고정, 튜닝 없음.
각 설계의 숫자는 "같은 질의를 운영 대신 이 설계로 검색했을 때" 를 뜻한다.

    python test/model_retrieval/tools/compare_designs.py runs/scores_*.json
    python test/model_retrieval/tools/compare_designs.py runs/scores_*.json --min-grade 2
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import random
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence

AI = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent

_spec = importlib.util.spec_from_file_location("tune", HERE / "tune.py")
tune = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tune)

BASE_DESIGN = "plainto"     # 운영이 쓰는 sparse 계산
BASE_WEIGHT = 0.65          # 09_model_scout_mcp_readonly.py:790


def load(path: Path) -> Dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return {"mode": data["sparse_mode"], "queries": data["queries"], "path": path}


def per_query_recall(queries: Sequence[Dict[str, Any]], min_grade: int, k: int) -> Dict[str, Dict[float, float]]:
    """질의별 · 가중치별 recall@10. NaN(정답 0개)인 질의는 뺀다."""
    out: Dict[str, Dict[float, float]] = {}
    for q in queries:
        row = {w: tune.recall_at_k(q["scored"], q["grades"], w, k=k, min_grade=min_grade)
               for w in tune.WEIGHTS}
        if any(v != v for v in row.values()):
            continue
        out[q["qid"]] = row
    return out


def out_of_fold(recall: Dict[str, Dict[float, float]], qids: Sequence[str],
                min_delta: float) -> Dict[str, float]:
    """질의마다 "그 질의를 빼고 고른 가중치"로 잰 recall. 고르기와 재기를 분리한다."""
    order = list(qids)
    random.Random(tune.SEED).shuffle(order)
    folds = [order[i::tune.FOLDS] for i in range(tune.FOLDS)]
    picked: Dict[str, float] = {}
    for test in folds:
        if not test:
            continue
        train = [q for q in order if q not in set(test)]
        floor = tune.mean([recall[q][BASE_WEIGHT] for q in train]) + min_delta
        best, best_w = floor, BASE_WEIGHT
        for w in tune.WEIGHTS:
            v = tune.mean([recall[q][w] for q in train])
            if v > best or (v == best and abs(w - BASE_WEIGHT) < abs(best_w - BASE_WEIGHT)):
                best, best_w = v, w
        for q in test:
            picked[q] = recall[q][best_w]
    return picked


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scores", nargs="+", type=Path)
    ap.add_argument("--min-grade", type=int, default=1, choices=(1, 2))
    ap.add_argument("--min-delta", type=float, default=0.005)
    ap.add_argument("--k", type=int, default=tune.K, help="상위 몇 개로 재는가. 운영은 5")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()

    designs = [load(p) for p in args.scores]
    modes = [d["mode"] for d in designs]
    if BASE_DESIGN not in modes:
        raise SystemExit(f"기준선이 없다. scores_{BASE_DESIGN}.json 을 같이 넣어야 한다")

    types = sorted({q["query_type"] for d in designs for q in d["queries"]})
    rng = random.Random(tune.SEED)
    report: Dict[str, Any] = {"min_grade": args.min_grade, "base_design": BASE_DESIGN,
                              "base_weight": BASE_WEIGHT, "types": {}}

    print(f"기준선 = 운영 현행 (sparse={BASE_DESIGN} · dense_weight {BASE_WEIGHT} 고정 · 튜닝 없음)")
    print(f"설계별 숫자 = 유형마다 폴드 밖에서 고른 가중치로 잰 recall@{args.k} (min_grade={args.min_grade})\n")

    for query_type in types:
        recalls: Dict[str, Dict[str, Dict[float, float]]] = {}
        for d in designs:
            qs = [q for q in d["queries"] if q["query_type"] == query_type]
            recalls[d["mode"]] = per_query_recall(qs, args.min_grade, args.k)
        common = sorted(set.intersection(*(set(r) for r in recalls.values())))
        if not common:
            continue

        base = {q: recalls[BASE_DESIGN][q][BASE_WEIGHT] for q in common}
        base_mean = tune.mean([base[q] for q in common])

        print(f"── {query_type}   공통 질의 {len(common)}개 · 운영 현행 {base_mean:.3f}")
        print(f"   {'설계':10s} {'recall@k':>9s} {'운영 대비':>9s} {'95% 구간':>18s} {'유의':>4s} {'가중치':>12s}")
        rows = []
        for d in designs:
            mode = d["mode"]
            oof = out_of_fold(recalls[mode], common, args.min_delta)
            value = tune.mean([oof[q] for q in common])
            boot = tune.paired_bootstrap([oof[q] - base[q] for q in common], rng)
            # 보고용으로 전체 질의에서 고른 가중치도 같이 적는다
            picks = sorted({w for w in tune.WEIGHTS}, key=lambda w: (
                -tune.mean([recalls[mode][q][w] for q in common]), abs(w - BASE_WEIGHT)))
            sig = "✅" if boot["lo"] > 0 else ("❌" if boot["hi"] < 0 else "—")
            print(f"   {mode:10s} {value:>9.3f} {boot['mean']:>+9.3f} "
                  f"  [{boot['lo']:+.3f}, {boot['hi']:+.3f}] {sig:>4s} {picks[0]:>12.2f}")
            rows.append({"design": mode, "recall": value, "delta": boot["mean"],
                         "ci95": [boot["lo"], boot["hi"]], "significant": boot["lo"] > 0,
                         "weight_full": picks[0]})
        best = max(rows, key=lambda r: r["recall"])
        print(f"   → 가장 높은 설계: {best['design']} ({best['recall']:.3f})\n")
        report["types"][query_type] = {"n": len(common), "base": base_mean, "designs": rows,
                                       "best": best["design"]}

    path = args.out or (AI / "test" / "model_retrieval" / "runs" /
                        f"designs_mg{args.min_grade}_k{args.k}.json")
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"→ {path.relative_to(AI)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
