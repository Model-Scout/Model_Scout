"""분해가 뽑은 조건이 하드 필터로 갈 때, 묻지 않은 제약이 끼지 않는지 본다.

하드 필터는 통과/탈락을 가르므로 한 번 잘못 걸면 정답이 채점에 오지도 못한다.
모델 검색 골든셋에서 실패의 42% 가 이 경로였고, 범인은 둘이었다.

  tasks (26건)                   분해가 묻지도 않은 분류를 단정한다
  max_parameters_billion (12건)  모델 이름의 "7.8B" 를 크기 상한으로 읽는다

두 번째가 특히 나쁘다. "EXAONE-3.5-7.8B-Instruct 를 쓰려고 합니다" 는 이름으로
콕 집은 요청인데, 7.8 을 상한으로 걸면 그 카드가 7.818 을 기록하고 있어
7.818 <= 7.8 이 거짓이 되고 **사용자가 지목한 그 모델이 탈락한다.**

explicit_constraints 의 가드가 이걸 막아야 한다. 가드가 느슨해지면 조용히
되돌아가므로, 실제 질문 문구로 양쪽을 확인한다.

    python test/test_model_search_constraints.py
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


# 골든셋 질문 그대로. 분해가 이름의 숫자를 상한으로 읽었고 골든셋 조건은 비어 있었다.
NAMES_NOT_LIMITS = (
    "LGAI 의 EXAONE-3.5-7.8B-Instruct 를 쓰려고 합니다. 어디서 받나요?",
    "EXAONE-4.0-1.2B 원본이랑 양자화 버전들을 한 번에 보고 싶어요.",
    "EXAONE-4.0-32B 를 찾고 있습니다.",
    "카카오가 공개한 kanana-1.5-8b-instruct 모델을 받고 싶어요.",
    "Solar-Open-100B 모델이 있나요?",
    "google 의 madlad400-3b-mt 번역 모델이 있나요?",
    "llama-3.2-Korean-Bllossom-3B 원본과 GGUF 버전을 같이 찾아 주세요.",
    "kanana 1.5 2.1b instruct 를 GGUF 로 받을 수 있나요?",
)

# 실제로 크기를 제한하는 질문. 숫자가 있는 것과 말로만 하는 것 양쪽.
REAL_LIMITS = (
    "모바일 앱에 넣을 작은 한국어 기계독해 모델이 필요해. 파라미터 1B 이하면 좋겠어.",
    "상업 이용 가능, 파라미터 3B 이하, 컨텍스트 32K 토큰 이상인 한국어 LLM 목록이 필요해.",
    "벡터 DB 비용 때문에 작고 빠른 한국어 임베딩 모델이 필요해. 100M 파라미터 이하.",
    "회의록 요약하는 걸 만들고 싶은데 제 컴퓨터에서 돌아갈 만큼 작았으면 해요.",
    "병원 안내 챗봇을 만들려는데 서버가 작아서 큰 모델은 못 올려요.",
    "게임 캐릭터 대화를 제 컴퓨터에서 돌리고 싶어요. 너무 크면 안 돌아갈 것 같은데요.",
    "제 노트북에서 돌려 보고 싶은데 한국어랑 영어 번역되는 걸로 가벼운 게 있을까요?",
)


def _survives(graph, text: str, value: float = 7.8):
    """분해가 상한 value 를 냈을 때, 가드를 지나고도 남아 있는지."""
    constraints = {**graph.constraint_defaults(), "max_parameter_count_billion": value}
    return graph.explicit_constraints(constraints, text)["max_parameter_count_billion"]


def test_a_model_name_is_not_a_size_limit():
    graph = _graph()
    leaked = [t for t in NAMES_NOT_LIMITS if _survives(graph, t) is not None]
    assert leaked == [], f"이름 속 숫자가 상한으로 남았다: {leaked}"


def test_a_stated_limit_survives():
    graph = _graph()
    dropped = [t for t in REAL_LIMITS if _survives(graph, t, 3.0) is None]
    assert dropped == [], f"실제 크기 제한이 사라졌다: {dropped}"


def test_the_guard_needs_a_bounding_word():
    """맨 숫자+B 만으로는 상한이 되지 않아야 한다. 이게 옛 가드의 구멍이었다."""
    graph = _graph()
    assert _survives(graph, "7.8B 모델") is None
    assert _survives(graph, "7.8B 이하 모델") is not None


def test_the_exact_boundary_case_that_was_broken():
    """7.818 짜리 카드를 7.8 상한이 떨어뜨렸던 그 질문."""
    graph = _graph()
    text = "LGAI 의 EXAONE-3.5-7.8B-Instruct 를 쓰려고 합니다. 어디서 받나요?"
    assert _survives(graph, text, 7.8) is None, (
        "7.8 이 상한으로 남으면 parameter_count_billion=7.818 인 그 모델이 탈락한다")


def test_size_bound_is_shared_with_the_measurement_tool():
    """측정 도구가 운영과 다른 규칙을 쓰면 측정이 운영을 설명하지 못한다."""
    graph = _graph()
    spec = importlib.util.spec_from_file_location(
        "preretrieval", ROOT / "test" / "model_retrieval" / "tools" / "preretrieval.py")
    pre = importlib.util.module_from_spec(spec)
    sys.modules["preretrieval"] = pre
    spec.loader.exec_module(pre)
    assert pre.SIZE_BOUND == graph.SIZE_BOUND, "SIZE_BOUND 가 갈렸다"


def test_the_guard_only_removes_never_invents():
    """가드는 분해가 내지 않은 조건을 만들어 내지 않는다."""
    graph = _graph()
    constraints = graph.constraint_defaults()
    out = graph.explicit_constraints(constraints, "파라미터 1B 이하인 가벼운 모델")
    assert out["max_parameter_count_billion"] is None


def test_cpu_only_is_kept_only_when_the_user_says_it():
    graph = _graph()
    on = {**graph.constraint_defaults(), "cpu_only": True}
    assert graph.explicit_constraints(on, "영어 뉴스 요약 서비스, 조건: 실행 환경 CPU만.")["cpu_only"] is True
    assert graph.explicit_constraints(on, "GPU 없이 돌리고 싶어")["cpu_only"] is True
    assert graph.explicit_constraints(on, "영어 뉴스 요약 서비스")["cpu_only"] is False  # never invented
    assert graph.explicit_constraints(graph.constraint_defaults(), "상업용만", previous=on)["cpu_only"] is True


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
