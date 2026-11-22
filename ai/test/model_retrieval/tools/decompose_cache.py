#!/usr/bin/env python3
"""질문 원문을 운영 decompose 로 한 번 돌려 model_query 를 뽑아 캐시한다.

운영 검색은 사용자 원문을 보지 않는다. 17_recommend_graph 의 decompose(LLM)가
needs = [{task, purpose_ko, model_query}] 로 바꾼 뒤, search_models 에
need["model_query"] 를 넘긴다(17_recommend_graph.py:565).

그래서 검색만 떼어 재려면 원문이 아니라 model_query 를 넣어야 한다. 이 도구가
그 변환을 한 번만 돌려 고정한다. temperature 0 이고 첫 턴 계획은 입력에만
의존하므로(_first_plan) 같은 질문은 같은 결과가 나온다.

    python test/model_retrieval/tools/decompose_cache.py queries/spec_benchmark.py …
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

AI = Path(__file__).resolve().parents[3]
CACHE = AI / "test" / "model_retrieval" / "queries" / "decompose_cache.json"


def _stub_langgraph() -> None:
    """langgraph 없이 17_recommend_graph 를 읽기 위한 최소 스텁.

    분해(decompose)만 쓰므로 그래프 조립 쪽은 실행되지 않는다. langgraph 는
    requirements_mcp.txt 에만 있어 평가용 venv 에는 없는 때가 많다. 여기서
    설치를 강요하지 않으려고 이름만 채운다.
    """
    import types

    if "langgraph.graph" in sys.modules:
        return
    for name in ("langgraph", "langgraph.graph", "langgraph.checkpoint",
                 "langgraph.checkpoint.memory", "langgraph.types"):
        sys.modules.setdefault(name, types.ModuleType(name))
    graph = sys.modules["langgraph.graph"]
    graph.END, graph.START = "__end__", "__start__"

    class _StateGraph:  # 조립만 받아 두고 아무것도 하지 않는다
        def __init__(self, *a, **k): pass
        def add_node(self, *a, **k): return self
        def add_edge(self, *a, **k): return self
        def add_conditional_edges(self, *a, **k): return self
        def compile(self, *a, **k): return self

    graph.StateGraph = _StateGraph
    sys.modules["langgraph.checkpoint.memory"].InMemorySaver = object
    sys.modules["langgraph.types"].interrupt = lambda *a, **k: None
    sys.modules["langgraph.types"].Command = object


def load_graph():
    _stub_langgraph()
    if str(AI) not in sys.path:          # 17_recommend_graph 가 project_checks 등을 ai/ 에서 찾는다
        sys.path.insert(0, str(AI))
    spec = importlib.util.spec_from_file_location("recommend_graph", AI / "17_recommend_graph.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["recommend_graph"] = module
    spec.loader.exec_module(module)
    return module


def load_spec(path: Path) -> List[Dict[str, Any]]:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return list(module.QUERIES)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("specs", nargs="+", type=Path)
    ap.add_argument("--target", default="model", help="route 의 search_target")
    ap.add_argument("--provider", default="openai", choices=("openai", "ollama"),
                    help="분해 LLM 제공자. 운영 .env 는 ollama/gemma3:4b 이지만 이 머신에 "
                         "Ollama 가 없어 기본은 openai 다. 어느 쪽으로 만들었는지 캐시에 남는다")
    ap.add_argument("--model", default=None, help="분해 LLM 이름(기본: 제공자 기본값)")
    args = ap.parse_args()

    # recommendation_llm.provider()/model_name() 이 읽는 값. import 전에 정해야 한다.
    import os
    os.environ["RECOMMEND_LLM_PROVIDER"] = args.provider
    # pop 으로는 안 된다. recommendation_llm 이 load_dotenv 로 .env 값을 다시 채운다.
    # .env 는 로컬 Ollama 용(gemma3:4b)이라 OpenAI 로 돌릴 때는 명시적으로 덮어쓴다.
    os.environ["RECOMMEND_LLM_MODEL"] = args.model or (
        "gpt-4.1-mini" if args.provider == "openai" else "gemma3:4b")

    raw: Dict[str, Any] = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    meta = raw.pop("__meta__", {})
    cache = raw
    graph = load_graph()
    meta = {"llm": graph.LLM_MODEL, "provider": args.provider, "target": args.target,
            "note": "운영 .env 는 ollama/gemma3:4b 다. 이 머신에 Ollama 가 없어 OpenAI 로 만들었다. "
                    "배포가 정말 gemma3:4b 면 같은 설정이 유지되는지 다시 돌려 확인해야 한다.",
            **{k: v for k, v in meta.items() if k not in ("llm", "provider", "target", "note")}}

    todo = []
    for path in args.specs:
        for item in load_spec(path if path.is_absolute() else AI / "test" / "model_retrieval" / path):
            if item["text"] not in cache and item["text"] != "__meta__":
                todo.append((item["qid"], item["text"]))
    print(f"캐시 {len(cache)}건 · 새로 돌릴 질문 {len(todo)}건 (LLM={graph.LLM_MODEL})")

    done = failed = 0
    started = time.perf_counter()
    for i, (qid, text) in enumerate(todo, 1):
        try:
            plan = graph._first_plan(" ".join(text.split()), args.target)
            cache[text] = {
                "qid": qid,
                "needs": [{"task": n.get("task"), "purpose_ko": n.get("purpose_ko"),
                           "model_query": n.get("model_query")} for n in plan.get("needs") or []],
                "constraints": plan.get("constraints"),
                "clarifying_questions": plan.get("clarifying_questions") or [],
            }
            done += 1
        except Exception as error:  # noqa: BLE001
            failed += 1
            print(f"  실패 {qid}: {type(error).__name__}: {error}")
        if i % 10 == 0 or i == len(todo):
            CACHE.write_text(json.dumps({"__meta__": meta, **cache}, ensure_ascii=False, indent=1) + "\n",
                             encoding="utf-8")
            print(f"  {i}/{len(todo)}  ({time.perf_counter()-started:.0f}s)", flush=True)
    CACHE.write_text(json.dumps({"__meta__": meta, **cache}, ensure_ascii=False, indent=1) + "\n",
                     encoding="utf-8")
    print(f"완료 {done} · 실패 {failed} · 캐시 {len(cache)}건 → {CACHE.relative_to(AI)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
