#!/usr/bin/env python3
"""상위 N개를 LLM 으로 다시 줄 세우고, 천장 대비 얼마를 가져가는지 잰다.

rerank_ceiling.py 가 낸 것은 "완벽한 리랭커"의 선이다(N=20 에서 0.648). 실제
리랭커는 그 일부만 가져가므로, 붙이기 전에 진짜 값을 알아야 한다. 여기서 재는
값이 운영에 넣을지 말지의 근거다.

재순위는 운영의 search_models 안에서 need 마다 일어나게 된다. need 는 이미
ThreadPoolExecutor(max_workers=MAX_NEEDS) 로 병렬이라, 추가 지연은 호출 1회분이다.

후보 설명은 scan.stage_texts 로 만든다. 골든셋 채점이 보는 것과 같은 텍스트라,
리랭커가 채점자와 같은 근거를 보고 판단하게 된다.

    python test/model_retrieval/tools/rerank_llm.py --limit 20     # 먼저 20개만
    python test/model_retrieval/tools/rerank_llm.py                # 전체 240개
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import random
import re
import statistics
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

AI = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RUNS = AI / "test" / "model_retrieval" / "runs"
CACHE = AI / "test" / "model_retrieval" / "cache" / "rerank_llm.json"
sys.path.insert(0, str(HERE))

PROMPT_VERSION = 2
PROMPT = """You rank Hugging Face models for a Korean model-recommendation service.

The user asked a question. Below are candidate models with what their model cards actually say.
Order the candidates by how well each one answers THAT question, best first.

Rules:
- Judge only on the evidence shown. If a card does not show what the question asks for, rank it low.
- When the question asks for models that REPORT a benchmark score, only the "scores:" line counts.
  Those are the scores the service can actually display. Prose that merely names a benchmark, or an
  example that transcribes a sample from it, is not a reported score: rank such a model low, and
  rank "scores: none extracted" lowest. The name appearing in "card:" text proves nothing.
- A question naming a model or family wants that model and its conversions, not similar models.
- A stated constraint (size, context, license, file format) that the card contradicts ranks low.
- When the question only filters (size, license, format, context) and every candidate already meets
  it, keep the order you were given; it is ordered by how widely each model is used.
- Rank every candidate exactly once.

Return JSON only: {"order": [<candidate numbers, best first>]}"""


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def benchmark_scores(row: Dict[str, Any], limit: int = 10) -> List[str]:
    """추출된 점수만. 골든셋 채점도 이 필드를 보고, 서비스도 이 값을 보여 준다."""
    seen: Dict[str, str] = {}
    for item in (row.get("benchmark_metadata") or {}).get("results") or []:
        name = (item.get("dataset") or item.get("benchmark") or "").strip().strip("`")
        if not name or name.upper() == "BENCHMARK" or name in seen:
            continue
        metric = (item.get("metric") or "").strip()
        score = item.get("score")
        seen[name] = f"{name} {metric} {score}".strip() if score is not None else f"{name} {metric}".strip()
        if len(seen) >= limit:
            break
    return list(seen.values())


def card(row: Dict[str, Any], scan, chars: int = 420) -> str:
    """후보 한 줄 설명. 길이를 묶어 20개가 한 프롬프트에 들어가게 한다."""
    meta = row.get("filter_metadata") or {}
    facts = [
        f"task={(row.get('task') or {}).get('primary') or '?'}",
        f"params={meta.get('parameter_count_billion')}B" if meta.get("parameter_count_billion") else "",
        f"context={meta.get('context_length')}" if meta.get("context_length") else "",
        f"license={meta.get('commercial_status') or meta.get('license') or '?'}",
        f"formats={','.join((meta.get('artifact_formats') or [])[:3])}" if meta.get("artifact_formats") else "",
    ]
    texts = scan.stage_texts(row)
    evidence = " ".join(
        texts.get(stage, "") for stage in ("semantic_metadata", "filter_metadata", "evidence")
    )
    evidence = re.sub(r"\s+", " ", evidence)[:chars]
    # 점수는 benchmark_metadata 에서 뽑은 것만 적는다. 서비스가 보여 줄 수 있는 값이고,
    # 카드 본문에 벤치마크 이름만 스치는 모델과 갈라야 한다(그 차이로 리랭커가 속았다).
    marks = benchmark_scores(row)
    lines = [f"{row['model_id']}  [{' '.join(f for f in facts if f)}]"]
    lines.append(f"  scores: {'; '.join(marks) if marks else 'none extracted'}")
    lines.append(f"  card: {evidence}")
    return "\n".join(lines)


def ask(client, model: str, question: str, cards: Sequence[str]) -> Optional[List[int]]:
    body = "\n\n".join(f"[{i}] {c}" for i, c in enumerate(cards, 1))
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        response_format={"type": "json_object"},
        max_tokens=400,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": f"Question (Korean):\n{question}\n\nCandidates:\n{body}"},
        ],
    )
    payload = json.loads(response.choices[0].message.content or "{}")
    order = payload.get("order")
    if not isinstance(order, list):
        return None
    seen, out = set(), []
    for value in order:
        try:
            index = int(value)
        except (TypeError, ValueError):
            continue
        if 1 <= index <= len(cards) and index not in seen:
            seen.add(index)
            out.append(index)
    return out or None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", default="idf_dectf_sg_nt", help="(가) 적용 상태의 측정")
    ap.add_argument("--depth", type=int, default=20, help="다시 세울 후보 수")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--min-grade", type=int, default=2)
    ap.add_argument("--model", default="gpt-4o-mini")
    ap.add_argument("--limit", type=int, default=0, help="질의 수 제한(먼저 작게 돌려 볼 때)")
    args = ap.parse_args()
    k, mg, depth = args.k, args.min_grade, args.depth

    import corpus
    import scan
    fc = _load("fc", HERE / "final_compare.py")
    tune = fc.tune

    rows = corpus.load_corpus()
    scan.bind(rows)
    by_id = {r["model_id"]: r for r in rows}
    run = json.loads((RUNS / f"scores_{args.run}.json").read_text(encoding="utf-8"))
    predicted = fc.predicted_types([q["text"] for q in run["queries"]])

    cached: Dict[str, List[str]] = (
        json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {})
    client = None

    queries = [q for q in run["queries"] if {m for m, g in q["grades"].items() if g >= mg}]
    if args.limit:
        queries = queries[:args.limit]

    print(f"{args.run} · 상위 {depth}개를 {args.model} 로 재정렬 · 질의 {len(queries)}개")
    print(f"recall@{k} · min_grade={mg}\n")

    results: List[Dict[str, Any]] = []
    started = time.perf_counter()
    latencies: List[float] = []
    failures = 0
    for n, query in enumerate(queries, 1):
        relevant = {m for m, g in query["grades"].items() if g >= mg}
        weight = fc.WEIGHTS.get(predicted.get(query["text"]) or "", fc.PRODUCTION_WEIGHT)
        order = [m for m, _, _ in sorted(
            query["scored"], key=lambda r: (-(weight * r[1] + (1 - weight) * r[2]), r[0]))]
        head, tail = order[:depth], order[depth:]

        key = f"v{PROMPT_VERSION}|{args.model}|{depth}|{query['qid']}"
        if key in cached:
            ranked = cached[key]
        else:
            if client is None:
                from dotenv import load_dotenv
                load_dotenv(AI / ".env")
                if not os.getenv("OPENAI_API_KEY"):
                    raise SystemExit("OPENAI_API_KEY 가 없다")
                from openai import OpenAI
                client = OpenAI(timeout=60.0, max_retries=2)
            cards = [card(by_id[m], scan) for m in head if m in by_id]
            usable = [m for m in head if m in by_id]
            clock = time.perf_counter()
            try:
                picks = ask(client, args.model, query["text"], cards)
            except Exception as error:                     # 한 질의 실패가 측정을 멈추지 않는다
                print(f"  ⚠ {query['qid']} {type(error).__name__}: {error}"[:120])
                picks = None
            latencies.append(time.perf_counter() - clock)
            if picks is None:
                failures += 1
                ranked = head                              # 실패하면 원래 순서를 쓴다
            else:
                chosen = [usable[i - 1] for i in picks]
                ranked = chosen + [m for m in head if m not in set(chosen)]
            cached[key] = ranked
            CACHE.parent.mkdir(parents=True, exist_ok=True)
            CACHE.write_text(json.dumps(cached, ensure_ascii=False) + "\n", encoding="utf-8")

        new_order = ranked + tail
        before = sum(1 for m in order[:k] if m in relevant) / len(relevant)
        after = sum(1 for m in new_order[:k] if m in relevant) / len(relevant)
        ceiling = min(k, len(relevant & set(head))) / len(relevant)
        results.append({"qid": query["qid"], "type": query["query_type"],
                        "before": before, "after": after, "ceiling": ceiling})
        if n % 20 == 0 or n == len(queries):
            print(f"  {n}/{len(queries)}  ({time.perf_counter()-started:.0f}s)", flush=True)

    print(f"\n{'유형':22s} {'지금':>7s} {'리랭커':>8s} {'천장':>7s} {'천장 달성':>9s}")
    print("-" * 58)
    for query_type in sorted({r["type"] for r in results}):
        group = [r for r in results if r["type"] == query_type]
        before = statistics.mean(r["before"] for r in group)
        after = statistics.mean(r["after"] for r in group)
        ceiling = statistics.mean(r["ceiling"] for r in group)
        share = (after - before) / (ceiling - before) if ceiling > before else float("nan")
        print(f"{query_type:22s} {before:>7.3f} {after:>8.3f} {ceiling:>7.3f} "
              f"{share:>8.0%}" if share == share else
              f"{query_type:22s} {before:>7.3f} {after:>8.3f} {ceiling:>7.3f} {'—':>9s}")
    print("-" * 58)
    before = statistics.mean(r["before"] for r in results)
    after = statistics.mean(r["after"] for r in results)
    ceiling = statistics.mean(r["ceiling"] for r in results)
    print(f"{'전체':22s} {before:>7.3f} {after:>8.3f} {ceiling:>7.3f} "
          f"{(after-before)/(ceiling-before):>8.0%}")

    boot = tune.paired_bootstrap([r["after"] - r["before"] for r in results],
                                 random.Random(tune.SEED))
    mark = "✅ 유의함" if boot["lo"] > 0 else ("❌ 손해" if boot["hi"] < 0 else "— 유의하지 않음")
    print(f"\n짝지은 부트스트랩 {len(results)}질의: {boot['mean']:+.3f} "
          f"[{boot['lo']:+.3f}, {boot['hi']:+.3f}]  {mark}")
    worse = sum(1 for r in results if r["after"] < r["before"])
    print(f"리랭커가 더 나빠진 질의 {worse}/{len(results)}")
    if latencies:
        print(f"호출 지연: 중앙 {statistics.median(latencies):.1f}s · "
              f"최대 {max(latencies):.1f}s (need 는 병렬이라 이 한 번이 추가 지연이다)")
    if failures:
        print(f"응답을 못 읽은 질의 {failures}개 — 원래 순서를 그대로 썼다")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
