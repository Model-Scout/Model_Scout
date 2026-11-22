#!/usr/bin/env python3
"""리콜이 왜 낮은지 질의마다 어디서 깨졌는지로 가른다. 무엇을 고칠지 이걸 보고 정한다.

recall@5 가 0.39 인 것은 알지만, 그게 "정답을 걸러서" 인지 "순위를 못 매겨서" 인지
모르면 엉뚱한 곳을 고친다. 한 질의가 깨지는 자리는 네 곳 중 하나다.

  A 검색 안 함       분해가 코퍼스에 없는 분류를 골라 need 가 unsupported 로 끝났다
  B 하드 필터가 죽임  정답이 하드 필터를 통과하지 못했다 → pre-retrieval 문제
  C 후보에 못 들어옴  필터는 통과했는데 dense 상위 300 밖이고 sparse 도 0 이다
                     → 후보 생성(dense 채널) 문제
  D 순위를 못 매김    후보에는 있는데 상위 5 밖이다 → 랭킹(가중치·sparse) 문제

B·C·D 는 고치는 방법이 완전히 다르다. B 는 조건 추출을, C 는 임베딩·질의
변환을, D 는 점수식을 건드려야 한다. 어디에 얼마가 있는지가 이 도구의 답이다.

    python test/model_retrieval/tools/failure_analysis.py
    python test/model_retrieval/tools/failure_analysis.py --run scores_plainto_dec
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

AI = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RUNS = AI / "test" / "model_retrieval" / "runs"
sys.path.insert(0, str(HERE))


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", default="scores_idf_dectf", help="runs/ 의 측정 이름")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--min-grade", type=int, default=2)
    ap.add_argument("--show", type=int, default=6, help="유형마다 보여 줄 실패 예")
    args = ap.parse_args()
    k, mg = args.k, args.min_grade

    import corpus
    fc = _load("fc", HERE / "final_compare.py")
    pre = _load("preretrieval", HERE / "preretrieval.py")

    rows = corpus.load_corpus()
    run = json.loads((RUNS / f"{args.run}.json").read_text(encoding="utf-8"))
    cache = json.loads((AI / "test" / "model_retrieval" / "queries" / "decompose_cache.json")
                       .read_text(encoding="utf-8"))
    predicted = fc.predicted_types([q["text"] for q in run["queries"]])
    fixed = "dectf" in args.run

    print(f"{args.run} · recall@{k} · min_grade={mg}\n")
    buckets: Dict[str, Counter] = defaultdict(Counter)
    examples: Dict[str, List[str]] = defaultdict(list)
    best_ranks: List[int] = []

    for query in run["queries"]:
        query_type = query["query_type"]
        relevant = {m for m, g in query["grades"].items() if g >= mg}
        if not relevant:
            continue
        buckets[query_type]["n"] += 1

        weight = fc.WEIGHTS.get(predicted.get(query["text"]) or "", fc.PRODUCTION_WEIGHT)
        order = [m for m, _, _ in sorted(query["scored"],
                                         key=lambda r: (-(weight * r[1] + (1 - weight) * r[2]), r[0]))]
        if any(m in relevant for m in order[:k]):
            buckets[query_type]["성공"] += 1
            continue

        got = pre.conditions_from_decompose(cache.get(query["text"]) or {}, fix_task=fixed)
        if not query["scored"]:
            mode = "A 검색안함"
        else:
            survived = {row["model_id"] for row in corpus.eligible(rows, got["conditions"])}
            if not (relevant & survived):
                mode = "B 필터가죽임"
            elif not (relevant & set(order)):
                mode = "C 후보밖"
            else:
                mode = "D 순위밖"
                ranks = [i for i, m in enumerate(order, 1) if m in relevant]
                best_ranks.append(min(ranks))
        buckets[query_type][mode] += 1
        if len(examples[mode]) < args.show * 2:
            examples[mode].append(f"{query['qid']:6s} {query_type:22s} {query['text'][:46]}")

    modes = ["A 검색안함", "B 필터가죽임", "C 후보밖", "D 순위밖"]
    print(f"{'유형':22s} {'질의':>4s} {'성공':>5s}" + "".join(f"{m:>12s}" for m in modes))
    print("-" * (22 + 11 + 12 * len(modes)))
    totals = Counter()
    for query_type in sorted(buckets):
        counter = buckets[query_type]
        totals.update(counter)
        print(f"{query_type:22s} {counter['n']:>4d} {counter['성공']:>5d}"
              + "".join(f"{counter[m]:>12d}" for m in modes))
    print("-" * (22 + 11 + 12 * len(modes)))
    print(f"{'합계':22s} {totals['n']:>4d} {totals['성공']:>5d}"
          + "".join(f"{totals[m]:>12d}" for m in modes))
    print(f"{'실패 중 비중':22s} {'':>4s} {'':>5s}"
          + "".join(f"{totals[m] / max(totals['n'] - totals['성공'], 1):>11.0%}" for m in modes))

    if best_ranks:
        print(f"\nD(순위밖) 질의에서 첫 정답의 순위: 중앙 {statistics.median(best_ranks):.0f}위 · "
              f"최선 {min(best_ranks)}위 · 상위 10 안 {sum(1 for r in best_ranks if r <= 10)}/{len(best_ranks)}건")
        print("  → 이건 k 를 늘리거나 재순위(rerank)로 건질 수 있는 몫이다")

    for mode in modes:
        if not examples[mode]:
            continue
        print(f"\n{mode} 예")
        for line in examples[mode][:args.show]:
            print(f"  {line}")

    print("""
고칠 곳
  B 가 크면  조건 추출(분해 프롬프트·검증)을 고친다. 필터를 과하게 걸고 있다
  C 가 크면  후보 생성을 고친다 — 질의 변환(영어 재작성·multi_query·HyDE),
             임베딩 대상, dense 깊이
  D 가 크면  점수식을 고친다 — sparse 설계, 유형별 가중치, 재순위""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
