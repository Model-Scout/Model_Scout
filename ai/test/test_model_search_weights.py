"""검색 교체분을 검증한다 — 분해 분류 키 매핑과 유형별 dense_weight.

두 변경이 조용히 되돌아가거나 어긋나면 검색이 눈에 띄지 않게 나빠진다.

  ① MODEL_TASK_FALLBACK  분해(LLM)가 내놓는 language_modeling·vision 을 코퍼스의
     분류로 옮긴다. 매핑이 없으면 hf_tags() 가 빈 배열이 되고 need 가 unsupported
     로 끝나 검색이 아예 돌지 않는다. 골든셋 240질의에서 50개가 그렇게 빈손이었다.
  ② MODEL_DENSE_WEIGHTS  classify_model_query 가 낸 유형으로 가중치를 고른다.
     분류기가 낼 수 있는 유형과 키가 정확히 같아야 하고, 분류 실패는 예전 값으로
     떨어져야 한다.

09 쪽 가중치 계산(None → 0.65, 범위 넘으면 자르기)은 MCP 의존성 없이 보기 위해
소스에서 식을 꺼내 확인한다.

    python test/test_model_search_weights.py
"""

from __future__ import annotations

import importlib.util
import re
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def _stub_langgraph() -> None:
    """langgraph 없이 17_recommend_graph 를 읽는다. 그래프 조립은 실행되지 않는다."""
    if "langgraph.graph" in sys.modules:
        return
    for name in ("langgraph", "langgraph.graph", "langgraph.checkpoint",
                 "langgraph.checkpoint.memory", "langgraph.types"):
        sys.modules.setdefault(name, types.ModuleType(name))
    graph = sys.modules["langgraph.graph"]
    graph.END, graph.START = "__end__", "__start__"

    class _StateGraph:
        def __init__(self, *a, **k): pass
        def add_node(self, *a, **k): return self
        def add_edge(self, *a, **k): return self
        def add_conditional_edges(self, *a, **k): return self
        def compile(self, *a, **k): return self

    graph.StateGraph = _StateGraph
    sys.modules["langgraph.checkpoint.memory"].InMemorySaver = object
    sys.modules["langgraph.types"].interrupt = lambda *a, **k: None
    sys.modules["langgraph.types"].Command = object


def _graph():
    _stub_langgraph()
    spec = importlib.util.spec_from_file_location("recommend_graph", ROOT / "17_recommend_graph.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["recommend_graph"] = module
    spec.loader.exec_module(module)
    return module


# --------------------------------------------------------------------------- 분류 키 매핑

def test_decompose_task_keys_reach_a_corpus_task():
    """분해가 실제로 내놓는 키가 모두 검색 가능한 태그로 이어지는지."""
    graph = _graph()
    # 240질의에서 관측한 키와 건수. image_generation 은 코퍼스에 그 분류가 없다.
    observed = {
        "language_modeling": 42, "vision": 8, "reranking": 3, "classification": 39,
        "speech_recognition": 30, "generation": 30, "translation": 25, "embedding": 24,
        "ocr": 13, "summarization": 8, "question_answering": 7,
        "information_extraction": 4, "visual_qa": 2, "retrieval": 2, "table_qa": 1,
    }
    blocked = [
        key for key in observed
        if not graph.hf_tags(key) and key not in graph.QUERY_ONLY_TASKS
    ]
    assert blocked == [], f"검색이 아예 막히는 분류 키 {blocked}"


def test_the_two_added_mappings_point_at_the_right_tag():
    graph = _graph()
    assert graph.hf_tags("language_modeling") == ["text-generation"]
    assert graph.hf_tags("vision") == ["image-text-to-text"]


def test_image_generation_stays_unsupported():
    """고칠 수 없는 것을 고친 척하지 않는다. 코퍼스에 이미지 생성 모델이 없다."""
    graph = _graph()
    assert graph.hf_tags("image_generation") == []
    assert "image_generation" not in graph.QUERY_ONLY_TASKS


# --------------------------------------------------------------------------- 유형별 가중치

def test_weights_cover_exactly_the_classifier_types():
    """분류기가 낼 수 있는 유형과 가중치 표의 키가 같아야 한다.

    분류기에 유형이 생겼는데 표에 없으면 그 유형은 조용히 0.65 로 떨어진다.
    표에만 있는 키는 영원히 쓰이지 않는다. 둘 다 눈에 안 띄므로 여기서 막는다.
    """
    graph = _graph()
    from retrieval_lab import classifier
    assert set(graph.MODEL_DENSE_WEIGHTS) == set(classifier.TYPES), (
        f"가중치 표 {sorted(graph.MODEL_DENSE_WEIGHTS)} != "
        f"분류기 유형 {sorted(classifier.TYPES)}"
    )


def test_weights_are_in_range():
    graph = _graph()
    for query_type, weight in graph.MODEL_DENSE_WEIGHTS.items():
        assert 0.0 <= weight <= 1.0, f"{query_type} 가중치 {weight}"


def test_unclassified_query_keeps_the_previous_split():
    """분류 실패(None)는 예전과 똑같이 동작해야 한다. 가중치가 들어오지 않는다."""
    graph = _graph()
    assert graph.MODEL_DENSE_WEIGHTS.get(None or "") is None
    assert graph.MODEL_DENSE_WEIGHTS.get("") is None


def test_benchmark_lookup_leans_on_sparse():
    """측정의 핵심 결론이 표에 남아 있는지. 벤치마크 질의는 sparse 쪽이 더 무겁다.

    0.30 이면 sparse 0.70 이다. 이 유형만 운영 기본값(0.65)의 반대편에 있다.
    """
    graph = _graph()
    assert graph.MODEL_DENSE_WEIGHTS["benchmark_lookup"] < 0.5


# --------------------------------------------------------------------------- 09 의 가중치 계산

def test_09_defaults_to_the_previous_weight():
    source = (ROOT / "09_model_scout_mcp_readonly.py").read_text(encoding="utf-8")
    assert "DEFAULT_DENSE_WEIGHT = 0.65" in source
    assert "0.65,\n        0.35," not in source, "가중치가 아직 하드코딩돼 있다"


def test_09_clamps_and_splits_the_weight():
    """None 은 예전 값, 범위 밖은 자르고, sparse 는 나머지가 되는지."""
    source = (ROOT / "09_model_scout_mcp_readonly.py").read_text(encoding="utf-8")
    match = re.search(
        r"applied_dense_weight = \(\n(.*?)\n    \)\n", source, re.S)
    assert match, "applied_dense_weight 계산을 찾지 못했다"
    expression = match.group(1)

    def applied(dense_weight, DEFAULT_DENSE_WEIGHT=0.65):
        return eval(expression, {"min": min, "max": max, "float": float},
                    {"dense_weight": dense_weight, "DEFAULT_DENSE_WEIGHT": DEFAULT_DENSE_WEIGHT})

    assert applied(None) == 0.65
    assert applied(0.30) == 0.30
    assert applied(1.0) == 1.0
    assert applied(-1.0) == 0.0, "음수를 자르지 않는다"
    assert applied(7.0) == 1.0, "1 보다 큰 값을 자르지 않는다"
    assert round(1.0 - applied(0.30), 4) == 0.70

    # 가중치가 RPC 로 가는 자리에 들어갔는지, 그리고 둘의 합이 1 인지
    assert "applied_dense_weight,\n        round(1.0 - applied_dense_weight, 4)," in source


def test_ttl_cache_key_includes_the_weight():
    """같은 질의를 다른 가중치로 부른 결과가 섞이면 안 된다."""
    source = (ROOT / "17_recommend_graph.py").read_text(encoding="utf-8")
    body = source[source.index("def _model_rows("):source.index("def search_models(")]
    assert "dense_weight," in body, "_model_rows 인자에 dense_weight 가 없다"
    assert "dense_weight=dense_weight" in body, "09 호출에 dense_weight 를 넘기지 않는다"


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
