#!/usr/bin/env python3
"""유형별 가중치를 쓰려면 런타임 유형 분류가 맞아야 한다. 그 정확도를 골든셋으로 잰다.

17_recommend_graph.classify_model_query 는 이미 질의 유형을 내고 state 에 넣는다.
그런데 로그만 찍고 아무도 쓰지 않는다("logged only until the planner uses it").
유형별 가중치는 바로 이 값을 쓰게 된다. 그래서 틀리는 비율과 **틀렸을 때 얼마나
손해인지**를 먼저 알아야 한다.

분류는 두 단계다.
  rule_type  정규식 빠른 경로. 확실한 것만 잡고 나머지는 None
  llm_type   나머지를 LLM 이 분류. 운영은 use_cache=False 로 매번 부른다

    python test/model_retrieval/tools/classify_check.py            # 규칙만(무료)
    python test/model_retrieval/tools/classify_check.py --llm      # 규칙+LLM
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List

AI = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CACHE = AI / "test" / "model_retrieval" / "cache" / "classify.json"


def _evaluator():
    spec = importlib.util.spec_from_file_location("ev", HERE / "evaluator.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--llm", action="store_true", help="규칙이 못 잡은 것을 LLM 으로 분류한다(비용 발생)")
    args = ap.parse_args()

    if str(AI) not in sys.path:
        sys.path.insert(0, str(AI))
    from retrieval_lab import classifier

    items = _evaluator().load_queries(None)
    cached: Dict[str, str] = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}

    rows: List[Dict[str, Any]] = []
    for item in items:
        text = item["text"]
        rule = classifier.rule_type(text)
        got = rule
        source = "rule" if rule else None
        if not got:
            if text in cached:
                got, source = cached[text], "llm(캐시)"
            elif args.llm:
                got = classifier.llm_type(text, use_cache=False)[0]
                cached[text] = got
                source = "llm"
        rows.append({"qid": item["qid"], "truth": item["query_type"], "got": got,
                     "source": source, "text": text})

    if args.llm:
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        CACHE.write_text(json.dumps(cached, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    judged = [r for r in rows if r["got"]]
    right = [r for r in judged if r["got"] == r["truth"]]
    print(f"질의 {len(rows)}개 · 분류된 것 {len(judged)}개 · 맞은 것 {len(right)}개")
    if judged:
        print(f"정확도 {len(right)/len(judged)*100:.1f}%  (분류 못 한 "
              f"{len(rows)-len(judged)}개는 운영에서 LLM 이 맡는다)\n")

    by_truth: Dict[str, Counter] = defaultdict(Counter)
    for r in rows:
        by_truth[r["truth"]][r["got"] or "(미분류)"] += 1
    print("정답 유형 → 분류 결과")
    for truth in sorted(by_truth):
        total = sum(by_truth[truth].values())
        hit = by_truth[truth][truth]
        print(f"\n  {truth:24s} {hit}/{total} 맞음")
        for got, n in by_truth[truth].most_common():
            if got != truth:
                print(f"      → {got:24s} {n}")

    rule_rows = [r for r in rows if r["source"] == "rule"]
    if rule_rows:
        ok = sum(1 for r in rule_rows if r["got"] == r["truth"])
        print(f"\n규칙 빠른 경로만: {len(rule_rows)}개 잡고 {ok}개 맞음 "
              f"({ok/len(rule_rows)*100:.0f}%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
