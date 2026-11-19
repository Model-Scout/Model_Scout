#!/usr/bin/env python3
"""운영 현행과 바꾼 뒤를 같은 자리에서 비교한다. 이 숫자가 교체 근거다.

세 가지를 한 번에 섞어 재면 무엇이 얼마나 기여했는지 알 수 없으므로 단계로 쌓는다.

  ① 운영 현행          분해 조건 그대로 · plainto sparse · dense_weight 0.65
  ② +분류 키 수정      MODEL_TASK_FALLBACK 두 줄. 검색이 아예 없던 질의가 살아난다
  ③ +C안 sparse        IDF 가중 매칭 비율
  ④ +유형별 가중치     분류기가 **예측한** 유형으로 가중치를 고른다

④가 핵심이다. 유형별 가중치는 런타임 분류를 믿는 것이므로, 정답 유형으로 재면
운영에서 재현되지 않는다. 그래서 17_recommend_graph.classify_model_query 와 같은
방법(rule_type → llm_type)으로 예측한 유형을 쓴다. 비교를 위해 정답 유형으로 잰
값(상한)도 같이 낸다.

운영은 need 당 top-5 를 돌려주므로(match_count=6 → MAX_SEARCH_RESULTS=5) k=5 다.

    python test/model_retrieval/tools/final_compare.py
    python test/model_retrieval/tools/final_compare.py --min-grade 1
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import statistics
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

AI = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RUNS = AI / "test" / "model_retrieval" / "runs"
CLASSIFY_CACHE = AI / "test" / "model_retrieval" / "cache" / "classify.json"

_spec = importlib.util.spec_from_file_location("tune", HERE / "tune.py")
tune = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tune)

# 09_model_scout_mcp_readonly.py 가 지금 쓰는 값
PRODUCTION_WEIGHT = 0.65

# 배포할 유형별 dense_weight. scores_idf_dectf.json 의 곡선에서 골랐다.
# benchmark_lookup 은 0.10~0.50 이 평탄해 중앙값을 집었다(폴드마다 흔들리지 않는 자리).
WEIGHTS = {
    "benchmark_lookup": 0.30,
    "lexical_exact": 1.00,
    "model_comparison": 0.90,
    "semantic_capability": 0.90,
    "semantic_constraint": 0.80,
    "structured_constraint": 0.40,
}


def load(name: str) -> Dict[str, Any]:
    return json.loads((RUNS / f"scores_{name}.json").read_text(encoding="utf-8"))


def predicted_types(texts: Sequence[str]) -> Dict[str, Optional[str]]:
    """17.classify_model_query 와 같은 순서로 유형을 예측한다. LLM 은 캐시에서 읽는다."""
    import sys
    if str(AI) not in sys.path:
        sys.path.insert(0, str(AI))
    from retrieval_lab import classifier

    cached = json.loads(CLASSIFY_CACHE.read_text(encoding="utf-8")) if CLASSIFY_CACHE.exists() else {}
    out: Dict[str, Optional[str]] = {}
    for text in texts:
        out[text] = classifier.rule_type(text) or cached.get(text)
    return out


def recall(queries: Sequence[Dict[str, Any]], weight_of, k: int, min_grade: int) -> List[float]:
    values = []
    for q in queries:
        value = tune.recall_at_k(q["scored"], q["grades"], weight_of(q), k=k, min_grade=min_grade)
        if value == value:                       # NaN(정답 0개) 은 평균에서 뺀다
            values.append(value)
    return values


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--min-grade", type=int, default=2, choices=(1, 2))
    ap.add_argument("--k", type=int, default=5)
    args = ap.parse_args()
    k, mg = args.k, args.min_grade

    runs = {"현행": load("plainto_dec"), "분류키": load("plainto_dectf"), "C안": load("idf_dectf")}
    types = sorted(WEIGHTS)
    predicted = predicted_types([q["text"] for q in runs["C안"]["queries"]])
    wrong = sum(1 for q in runs["C안"]["queries"]
                if predicted.get(q["text"]) != q["query_type"])
    print(f"recall@{k} · min_grade={mg} · 질의 {len(runs['C안']['queries'])}개")
    print(f"유형 분류는 운영과 같은 방법으로 예측한 값이다 (틀린 것 {wrong}개)\n")

    stages = [
        ("① 운영 현행", runs["현행"], lambda q: PRODUCTION_WEIGHT),
        ("② +분류키 수정", runs["분류키"], lambda q: PRODUCTION_WEIGHT),
        ("③ +C안 sparse", runs["C안"], lambda q: PRODUCTION_WEIGHT),
        ("④ +유형별 가중치", runs["C안"],
         lambda q: WEIGHTS.get(predicted.get(q["text"]) or "", PRODUCTION_WEIGHT)),
        ("   (상한) 정답 유형", runs["C안"], lambda q: WEIGHTS.get(q["query_type"], PRODUCTION_WEIGHT)),
    ]

    header = f"{'유형':22s}" + "".join(f"{name[:14]:>16s}" for name, _, _ in stages)
    print(header)
    print("-" * len(header))
    totals: Dict[str, List[float]] = {name: [] for name, _, _ in stages}
    for query_type in types:
        line = f"{query_type:22s}"
        for name, run, weight_of in stages:
            qs = [q for q in run["queries"] if q["query_type"] == query_type]
            values = recall(qs, weight_of, k, mg)
            totals[name] += values
            line += f"{statistics.mean(values) if values else 0.0:>16.3f}"
        print(line)
    print("-" * len(header))
    means = {name: statistics.mean(v) for name, v in totals.items()}
    print(f"{'전체 평균':22s}" + "".join(f"{means[name]:>16.3f}" for name, _, _ in stages))
    order = [name for name, _, _ in stages]
    print(f"{'앞 단계 대비':22s}" + "".join(
        f"{'—':>16s}" if i == 0 else f"{means[order[i]] - means[order[i-1]]:>+16.3f}"
        for i in range(len(order))))

    base, final = means[order[0]], means[order[3]]
    print(f"\n운영 현행 {base:.3f} → 교체 후 {final:.3f}   "
          f"절대 {final - base:+.3f} · 상대 {(final/base - 1) * 100:+.0f}%")
    for name, run, _ in stages[:4]:
        zero = sum(1 for q in run["queries"] if not q["scored"])
        print(f"  {name:20s} 결과 0건 질의 {zero:>3d}/{len(run['queries'])}")

    # 질의 단위로 짝지어 유의성을 본다
    paired = []
    first, last = stages[0], stages[3]
    by_qid = {q["qid"]: q for q in last[1]["queries"]}
    import random
    for q in first[1]["queries"]:
        other = by_qid.get(q["qid"])
        if other is None:
            continue
        a = tune.recall_at_k(q["scored"], q["grades"], PRODUCTION_WEIGHT, k=k, min_grade=mg)
        b = tune.recall_at_k(other["scored"], other["grades"], last[2](other), k=k, min_grade=mg)
        if a == a and b == b:
            paired.append(b - a)
    boot = tune.paired_bootstrap(paired, random.Random(tune.SEED))
    mark = "✅ 유의함" if boot["lo"] > 0 else "— 유의하지 않음"
    print(f"\n짝지은 부트스트랩 {len(paired)}질의: {boot['mean']:+.3f} "
          f"[{boot['lo']:+.3f}, {boot['hi']:+.3f}]  {mark}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
