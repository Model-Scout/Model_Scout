#!/usr/bin/env python3
"""운영의 pre-retrieval 을 그대로 재현한다. 하드 필터가 어디서 오는지가 핵심이다.

지금까지의 측정은 골든셋이 **질문에서 직접 적어 둔 조건**(oracle)을 하드 필터로 썼다.
운영은 그 조건을 LLM 분해가 뽑아낸다. 둘이 다르면 측정이 운영보다 후하다.

운영 경로 (17_recommend_graph.search_models)

    분해(LLM) → needs[].task, needs[].model_query, constraints
    tags = hf_tags(task)                       MODEL_HF_TASKS 중 같은 분류만
    tags 가 비고 reranking 도 아니면           → unsupported. 모델을 아예 안 돌려준다
    max_params = min(명시한 크기 제한, GPU 로 환산한 크기)
    search_models(model_query, task_filters=tags, korean_required=True, ...)

여기서 두 가지를 그대로 가져온다.
  · hf_tags — 분류 키를 코퍼스의 HF 태그로 바꾼다. 못 바꾸면 검색 자체가 없다
  · max_params_for_gpu — "RTX 4090" 같은 말을 파라미터 상한으로 바꾼다

korean_required=True 는 운영이 항상 걸지만, 코퍼스 4017행 전부가
korean_verified=true 라 실제로는 아무것도 걸러내지 않는다(측정으로 확인).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

AI = Path(__file__).resolve().parents[3]

# 17_recommend_graph.py 에서 그대로 옮긴다. 운영이 바뀌면 여기도 바꿔야 한다.
MODEL_HF_TASKS = (
    "text-generation", "image-text-to-text", "sentence-similarity", "translation",
    "automatic-speech-recognition", "feature-extraction", "text-classification",
    "question-answering", "summarization",
)
MODEL_TASK_FALLBACK = {
    "retrieval": "embedding", "tool_use": "generation", "information_extraction": "generation",
    "table_qa": "generation", "ocr": "visual_qa", "chart_understanding": "visual_qa",
}
QUERY_ONLY_TASKS = {"reranking"}

# 분해(LLM)가 실제로 내놓지만 MODEL_TASK_FALLBACK 에 없어서 검색이 아예 막히는 키들.
# 240질의에서 language_modeling 42건·vision 8건 — 전체의 21% 가 모델 0개로 끝난다.
# image_generation 은 코퍼스에 그 분류가 없어 고칠 수 없다(진짜 미지원).
TASK_FALLBACK_FIX = {"language_modeling": "generation", "vision": "visual_qa"}


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _helpers():
    """taxonomy.normalize 와 project_checks.max_params_for_gpu. langgraph 는 필요 없다."""
    if str(AI) not in sys.path:
        sys.path.insert(0, str(AI))
    import project_checks
    from taxonomy import normalize
    return normalize, project_checks.max_params_for_gpu


def hf_tags(task_key: str, normalize, *, fix: bool = False) -> List[str]:
    fallback = {**MODEL_TASK_FALLBACK, **(TASK_FALLBACK_FIX if fix else {})}
    task_key = fallback.get(task_key, task_key)
    return [tag for tag in MODEL_HF_TASKS if normalize("task", tag) == task_key]


def conditions_from_decompose(entry: Dict[str, Any], *, fix_task: bool = False) -> Dict[str, Any]:
    """분해 결과 한 건 → 09.search_models 가 받는 하드 필터.

    needs[0] 만 쓴다. 골든셋 질문은 모델 하나를 찾는 질문이고, 운영도 need 마다
    따로 검색하므로 need 하나가 한 번의 검색에 대응한다.
    """
    normalize, max_params_for_gpu = _helpers()
    needs = entry.get("needs") or []
    constraints = entry.get("constraints") or {}

    tags = hf_tags(needs[0]["task"], normalize, fix=fix_task) if needs else []
    task_key = needs[0]["task"] if needs else None
    unsupported = not tags and task_key not in QUERY_ONLY_TASKS

    gpu = constraints.get("gpu_memory_gb")
    limits = [v for v in (constraints.get("max_parameter_count_billion"),
                          max_params_for_gpu(gpu) if gpu else None) if v]

    conditions: Dict[str, Any] = {
        "tasks": tags or None,
        "korean_required": True,            # 운영이 항상 건다(코퍼스 100% 통과라 무효)
        "max_parameters_billion": min(limits) if limits else None,
        "min_context_length": constraints.get("min_context_length"),
        "commercial_status": ["permitted"] if constraints.get("commercial_only") else None,
        "require_artifact": list(constraints.get("required_artifacts") or []) or None,
        "max_artifact_gib": constraints.get("max_artifact_gib"),
        "exclude_gated": bool(constraints.get("exclude_gated")),
    }
    return {"conditions": {k: v for k, v in conditions.items() if v not in (None, [], False)},
            "unsupported": unsupported, "task": task_key, "hf_tags": tags}


def main() -> int:
    """oracle 조건과 분해 조건이 어디서 갈리는지 센다."""
    import json
    from collections import Counter

    here = Path(__file__).resolve().parent
    ev = _load("ev", here / "evaluator.py")
    cache = json.loads((AI / "test" / "model_retrieval" / "queries" / "decompose_cache.json")
                       .read_text(encoding="utf-8"))
    items = ev.load_queries(None)

    print(f"질의 {len(items)}개 — oracle 조건(골든셋) vs 분해 조건(운영)\n")
    unsupported: List[str] = []
    diff = Counter()
    by_type: Dict[str, Counter] = {}
    for item in items:
        entry = cache.get(item["text"]) or {}
        got = conditions_from_decompose(entry)
        oracle = {k: v for k, v in (item.get("conditions") or {}).items() if v not in (None, [], False)}
        mine = dict(got["conditions"])
        mine.pop("korean_required", None)       # 무효한 필터는 비교에서 뺀다
        oracle.pop("korean_required", None)
        counter = by_type.setdefault(item["query_type"], Counter())
        counter["n"] += 1
        if got["unsupported"]:
            unsupported.append(f"{item['qid']} task={got['task']}")
            counter["unsupported"] += 1
        for key in set(oracle) | set(mine):
            if oracle.get(key) != mine.get(key):
                diff[key] += 1
                counter["cond_diff"] += 1
        if "tasks" in oracle and oracle.get("tasks") != mine.get("tasks"):
            counter["tasks_diff"] += 1

    print(f"{'유형':24s} {'질의':>4s} {'검색불가':>7s} {'조건불일치':>9s} {'task불일치':>10s}")
    for query_type, c in sorted(by_type.items()):
        print(f"{query_type:24s} {c['n']:>4d} {c['unsupported']:>7d} {c['cond_diff']:>9d} {c['tasks_diff']:>10d}")

    print(f"\n조건 키별 불일치 횟수")
    for key, count in diff.most_common():
        print(f"  {key:26s} {count}")

    if unsupported:
        print(f"\n분해가 코퍼스에 없는 분류를 골라 검색 자체가 안 되는 질의 {len(unsupported)}개")
        for line in unsupported[:15]:
            print(f"  {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
