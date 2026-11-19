#!/usr/bin/env python3
"""하드 필터가 정답을 죽인 질의에서, 어느 조건이 죽였는지 지목한다.

failure_analysis.py 가 실패의 42% 를 "B 필터가 죽임" 으로 가렸다. 필터는 분해가
뽑은 조건에서 나오므로, 어느 조건 키가 범인인지 알면 분해 쪽에서 무엇을 고칠지가
정해진다. 조건을 하나씩 빼 보고 정답이 살아나는지 본다(제외 실험).

    python test/model_retrieval/tools/filter_blame.py
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Set

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
    ap.add_argument("--run", default="scores_idf_dectf")
    ap.add_argument("--min-grade", type=int, default=2)
    ap.add_argument("--show", type=int, default=10)
    args = ap.parse_args()
    mg = args.min_grade

    import corpus
    pre = _load("preretrieval", HERE / "preretrieval.py")

    rows = corpus.load_corpus()
    run = json.loads((RUNS / f"{args.run}.json").read_text(encoding="utf-8"))
    cache = json.loads((AI / "test" / "model_retrieval" / "queries" / "decompose_cache.json")
                       .read_text(encoding="utf-8"))

    blame = Counter()
    blame_by_type: Dict[str, Counter] = defaultdict(Counter)
    oracle_gap = Counter()
    cases: List[str] = []

    for query in run["queries"]:
        relevant = {m for m, g in query["grades"].items() if g >= mg}
        if not relevant or not query["scored"]:
            continue
        got = pre.conditions_from_decompose(cache.get(query["text"]) or {}, fix_task=True)
        conditions = got["conditions"]
        survived = {r["model_id"] for r in corpus.eligible(rows, conditions)}
        if relevant & survived:
            continue                                   # 필터는 통과했다. B 아님

        # 조건을 하나씩 빼면 정답이 살아나는가
        culprits = []
        for key in conditions:
            relaxed = {k: v for k, v in conditions.items() if k != key}
            if relevant & {r["model_id"] for r in corpus.eligible(rows, relaxed)}:
                culprits.append(key)
        if not culprits:
            culprits = ["(여러 조건이 함께)"]
        for key in culprits:
            blame[key] += 1
            blame_by_type[query["query_type"]][key] += 1

        # 골든셋이 적어 둔 조건이면 살았을까 — 분해가 과하게 거는 것인지 가린다
        oracle = {k: v for k, v in (query.get("conditions") or {}).items()
                  if v not in (None, [], False)}
        if relevant & {r["model_id"] for r in corpus.eligible(rows, oracle)}:
            oracle_gap["분해만 죽임"] += 1
        else:
            oracle_gap["조건 자체가 정답과 안 맞음"] += 1

        if len(cases) < args.show:
            cases.append(
                f"{query['qid']:6s} {query['query_type']:22s} 범인={','.join(culprits)}\n"
                f"         질문: {query['text'][:62]}\n"
                f"         분해 조건: {json.dumps(conditions, ensure_ascii=False)[:100]}\n"
                f"         골든셋 조건: {json.dumps(oracle, ensure_ascii=False)[:100]}")

    total = sum(oracle_gap.values())
    print(f"하드 필터가 2점 정답을 전부 죽인 질의 {total}개\n")
    print("범인 조건 (하나씩 빼서 정답이 살아나면 그 조건)")
    for key, count in blame.most_common():
        print(f"  {key:26s} {count:3d}건")

    print(f"\n분해 탓인가, 조건 자체가 틀렸나")
    for key, count in oracle_gap.most_common():
        print(f"  {key:26s} {count:3d}건  ({count/total:.0%})")

    print(f"\n유형별 범인")
    for query_type in sorted(blame_by_type):
        items = ", ".join(f"{k}:{v}" for k, v in blame_by_type[query_type].most_common(3))
        print(f"  {query_type:24s} {items}")

    print(f"\n사례")
    for case in cases:
        print(f"  {case}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
