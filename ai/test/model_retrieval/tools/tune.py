#!/usr/bin/env python3
"""유형별 dense/sparse 가중치를 고르고, 그 이득이 진짜인지 검증한다.

핵심은 **고르는 질의와 재는 질의를 분리**하는 것이다. 설정을 N개 놓고 같은
질의로 1등을 뽑으면 그 점수에는 운이 섞여 새 질의에서 재현되지 않는다.

  · 5-fold 교차검증 — 폴드 4개로 가중치를 고르고 남은 1개로 잰다.
    이 평균이 "새 질의에서 기대할 수 있는 성능"이다.
  · 짝지은 부트스트랩 — 같은 질의를 두 설정으로 쟀으므로 질의 단위 차이를
    1만 번 재표집해 95% 구간을 낸다. 구간이 0 을 품으면 이득이라 말하지 않는다.

점수는 evaluator.py 가 남긴 (model_id, dense, sparse) 에서 계산한다. 가중치를
바꿔도 재질의가 필요 없다.

    python test/model_retrieval/tools/tune.py runs/scores_plainto.json
"""

from __future__ import annotations

import argparse
import json
import random
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

AI = Path(__file__).resolve().parents[3]
# 0.0~1.0 을 0.05 간격으로. 운영 기본값 0.65 가 반드시 들어가야 비교가 된다.
WEIGHTS = [round(x / 20, 2) for x in range(0, 21)]
FOLDS = 5
BOOTSTRAP = 10000
SEED = 20261119
K = 10


def recall_at_k(scored: Sequence[Sequence], grades: Dict[str, int], dense_w: float,
                k: int = K, min_grade: int = 1) -> float:
    relevant = {m for m, g in grades.items() if g >= min_grade}
    if not relevant:
        return float("nan")
    sparse_w = round(1.0 - dense_w, 4)
    ranked = sorted(scored, key=lambda r: (-(dense_w * r[1] + sparse_w * r[2]), r[0]))
    top = [m for m, _, _ in ranked[:k]]
    return sum(1 for m in top if m in relevant) / len(relevant)


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def paired_bootstrap(deltas: Sequence[float], rng: random.Random) -> Dict[str, float]:
    if not deltas:
        return {"mean": 0.0, "lo": 0.0, "hi": 0.0}
    n = len(deltas)
    means = sorted(mean([deltas[rng.randrange(n)] for _ in range(n)]) for _ in range(BOOTSTRAP))
    return {"mean": mean(deltas), "lo": means[int(0.025 * BOOTSTRAP)], "hi": means[int(0.975 * BOOTSTRAP) - 1]}


def analyse(queries: List[Dict[str, Any]], min_grade: int, min_delta: float,
            k: int = K) -> Dict[str, Any]:
    """질의 묶음 하나(한 유형)의 결과."""
    per_weight: Dict[float, Dict[str, float]] = {}
    for w in WEIGHTS:
        per_weight[w] = {q["qid"]: recall_at_k(q["scored"], q["grades"], w, k=k, min_grade=min_grade)
                         for q in queries}
    qids = [q["qid"] for q in queries if not any(
        per_weight[w][q["qid"]] != per_weight[w][q["qid"]] for w in WEIGHTS)]   # NaN 제외
    base = 0.65   # 운영 기본값(09_model_scout_mcp_readonly.py:790)

    def score_on(w: float, ids: Sequence[str]) -> float:
        return mean([per_weight[w][i] for i in ids])

    def pick(ids: Sequence[str]) -> float:
        floor = score_on(base, ids) + min_delta
        best, best_w = floor, base
        for w in WEIGHTS:
            v = score_on(w, ids)
            if v > best or (v == best and abs(w - base) < abs(best_w - base)):
                best, best_w = v, w
        return best_w

    rng = random.Random(SEED)
    folds = [qids[i::FOLDS] for i in range(FOLDS)]
    random.Random(SEED).shuffle(qids)
    folds = [qids[i::FOLDS] for i in range(FOLDS)]
    rows, deltas, chosen = [], [], []
    for i, test in enumerate(folds):
        if not test:
            continue
        train = [q for q in qids if q not in set(test)]
        w = pick(train)
        chosen.append(w)
        rows.append({"fold": i + 1, "n": len(test), "weight": w,
                     "tuned": score_on(w, test), "baseline": score_on(base, test)})
        deltas += [per_weight[w][q] - per_weight[base][q] for q in test]
    boot = paired_bootstrap(deltas, rng)
    final = pick(qids)
    return {
        "n_queries": len(qids),
        "baseline_weight": base,
        "baseline": score_on(base, qids),
        "final_weight": final,
        "optimistic": score_on(final, qids),
        "cv_tuned": mean([r["tuned"] for r in rows]),
        "cv_baseline": mean([r["baseline"] for r in rows]),
        "delta": boot["mean"],
        "ci95": [boot["lo"], boot["hi"]],
        "significant": boot["lo"] > 0,
        "stable": len(set(chosen)) == 1,
        "picked_per_fold": chosen,
        "curve": {str(w): score_on(w, qids) for w in WEIGHTS},
        "folds": rows,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scores", nargs="+", type=Path)
    ap.add_argument("--min-grade", type=int, default=1, choices=(1, 2))
    ap.add_argument("--min-delta", type=float, default=0.005)
    ap.add_argument("--beginner", action="store_true", help="초보 질문만")
    ap.add_argument("--k", type=int, default=K, help="상위 몇 개로 재는가. 운영은 5(MAX_SEARCH_RESULTS)")
    args = ap.parse_args()

    for path in args.scores:
        full = path if path.is_absolute() else AI / "test" / "model_retrieval" / path
        data = json.loads(full.read_text(encoding="utf-8"))
        queries = [q for q in data["queries"] if q["grades"]]
        if args.beginner:
            queries = [q for q in queries if q.get("origin") == "beginner"]
        by_type: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        for q in queries:
            by_type[q["query_type"]].append(q)

        print(f"\n{full.name}  (sparse={data['sparse_mode']} · 검색어={data['search_text']} "
              f"· min_grade={args.min_grade}{' · 초보만' if args.beginner else ''})")
        print(f"{'유형':24s} {'N':>3s} {'기준':>6s} {'교차검증':>8s} {'이득':>7s} {'95% 구간':>18s} {'유의':>4s} {'가중치':>6s}")
        print("-" * 96)
        out = {}
        for kind in sorted(by_type):
            r = analyse(by_type[kind], args.min_grade, args.min_delta, args.k)
            out[kind] = r
            ci = f"[{r['ci95'][0]:+.3f}, {r['ci95'][1]:+.3f}]"
            print(f"{kind:24s} {r['n_queries']:>3d} {r['baseline']:>6.3f} {r['cv_tuned']:>8.3f} "
                  f"{r['delta']:>+7.3f} {ci:>18s} {'✅' if r['significant'] else '—':>4s} "
                  f"{r['final_weight']:>6.1f}")
        result = full.with_name(full.stem.replace("scores", "tuned") + ".json")
        result.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"→ {result.relative_to(AI)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
