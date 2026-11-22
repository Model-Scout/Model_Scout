"""재순위가 어디에 걸리고, 실패할 때 무엇을 하는지 본다.

리랭커는 질의 유형 셋에만 걸린다. 전체에 걸면 점수는 같은데(0.511 vs 0.506) 호출이
두 배가 되고, 판단할 것이 없는 유형(조건만 거는 질의)의 순서까지 흔든다.

실패가 추천을 멈추면 안 된다. LLM 이 죽거나 엉뚱한 JSON 을 주면 받은 순서를 그대로
돌려줘야 한다 — 순서가 나쁜 답이 답이 없는 것보다 낫다.

    python test/test_model_rerank.py
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def _module():
    spec = importlib.util.spec_from_file_location("model_rerank", ROOT / "model_rerank.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["model_rerank"] = module
    spec.loader.exec_module(module)
    return module


def rows(n: int) -> List[Dict[str, Any]]:
    return [{"model_id": f"org/m{i}", "task": "text-generation", "parameters_b": 1.0,
             "evidence": f"model {i}"} for i in range(1, n + 1)]


class _Client:
    """주문한 순서를 돌려주는 가짜 OpenAI 클라이언트."""

    def __init__(self, payload: Any, boom: BaseException | None = None):
        self.payload, self.boom, self.calls = payload, boom, 0
        outer = self

        class _Completions:
            def create(self, **kwargs):
                outer.calls += 1
                outer.kwargs = kwargs
                if outer.boom:
                    raise outer.boom
                text = outer.payload if isinstance(outer.payload, str) else json.dumps(outer.payload)
                return type("R", (), {"choices": [type("C", (), {
                    "message": type("M", (), {"content": text})()})()]})()

        self.chat = type("Chat", (), {"completions": _Completions()})()


# --------------------------------------------------------------------------- 어디에 걸리나

def test_only_the_measured_types_are_reranked():
    mr = _module()
    for query_type in ("lexical_exact", "model_comparison", "benchmark_lookup",
                       "semantic_capability"):
        assert mr.wanted(query_type, "openai"), query_type
    for query_type in ("semantic_constraint", "structured_constraint"):
        assert not mr.wanted(query_type, "openai"), f"{query_type} 는 손해였다"


def test_an_unclassified_query_is_not_reranked():
    mr = _module()
    assert not mr.wanted(None, "openai") and not mr.wanted("", "openai")


def test_an_unmeasured_provider_does_not_rerank():
    """운영 생성 모델이 로컬 gemma3:4b 일 수 있다. 재지 않은 모델로 조용히 섞지 않는다."""
    mr = _module()
    import os
    os.environ.pop(mr.MODEL_ENV, None)
    assert mr.model("openai") == mr.MEASURED_MODEL
    assert mr.model("ollama") is None
    assert not mr.wanted("lexical_exact", "ollama")


def test_an_explicit_model_override_turns_it_back_on():
    mr = _module()
    import os
    os.environ[mr.MODEL_ENV] = "qwen2.5:14b"
    try:
        assert mr.model("ollama") == "qwen2.5:14b"
        assert mr.wanted("lexical_exact", "ollama")
    finally:
        os.environ.pop(mr.MODEL_ENV, None)


def test_rerank_types_are_real_query_types():
    mr = _module()
    from retrieval_lab import classifier
    assert mr.RERANK_TYPES <= set(classifier.TYPES)


def test_the_graph_reranks_with_the_user_words_not_the_search_string():
    """질의문이 의도를 담고 model_query 는 키워드만 담는다."""
    source = (ROOT / "17_recommend_graph.py").read_text(encoding="utf-8")
    body = source[source.index("def search_models(state"):source.index("def search_project_datasets(")]
    call = re.search(r"model_rerank\.rerank\((.*?)\)\n", body, re.S)
    assert call, "17 이 재순위를 부르지 않는다"
    assert 'state["request"]' in call.group(1), "model_query 로 재순위하고 있다"
    assert "model_rerank.RERANK_DEPTH" in body, "깊은 후보를 요청하지 않는다"
    assert "match_count," in body, "match_count 가 캐시 키에 없다"


# --------------------------------------------------------------------------- 실패할 때

def test_an_llm_failure_keeps_the_given_order():
    mr = _module()
    given = rows(6)
    client = _Client(None, boom=RuntimeError("down"))
    assert [r["model_id"] for r in mr.rerank("질문", given, lambda: client, "m")] == \
           [r["model_id"] for r in given]


def test_garbage_json_keeps_the_given_order():
    mr = _module()
    given = rows(6)
    for payload in ("not json at all", {}, {"order": "nope"}, {"order": []}):
        got = mr.rerank("질문", given, lambda: _Client(payload), "m")
        assert [r["model_id"] for r in got] == [r["model_id"] for r in given], payload


def test_out_of_range_and_duplicate_picks_are_dropped():
    mr = _module()
    given = rows(4)
    got = mr.rerank("질문", given, lambda: _Client({"order": [3, 3, 99, 0, -1, 1]}), "m")
    assert [r["model_id"] for r in got] == ["org/m3", "org/m1", "org/m2", "org/m4"]


def test_a_partial_order_keeps_the_rest_behind_in_place():
    mr = _module()
    given = rows(5)
    got = mr.rerank("질문", given, lambda: _Client({"order": [5, 2]}), "m")
    assert [r["model_id"] for r in got] == ["org/m5", "org/m2", "org/m1", "org/m3", "org/m4"]


def test_nothing_is_lost_or_duplicated():
    mr = _module()
    given = rows(12)
    got = mr.rerank("질문", given, lambda: _Client({"order": [7, 1, 12]}), "m")
    assert sorted(r["model_id"] for r in got) == sorted(r["model_id"] for r in given)
    assert len(got) == len(given)


def test_one_candidate_needs_no_call():
    mr = _module()
    client = _Client({"order": [1]})
    assert mr.rerank("질문", rows(1), lambda: client, "m") == rows(1)
    assert client.calls == 0


def test_candidates_past_the_depth_keep_their_place():
    mr = _module()
    given = rows(mr.RERANK_DEPTH + 3)
    got = mr.rerank("질문", given, lambda: _Client({"order": [2, 1]}), "m")
    tail = [r["model_id"] for r in given[mr.RERANK_DEPTH:]]
    assert [r["model_id"] for r in got][-3:] == tail
    assert len(got) == len(given)


# --------------------------------------------------------------------------- 카드

def test_the_card_separates_reported_scores_from_card_prose():
    """이게 갈리지 않으면, 샘플만 전사한 모델이 점수를 보고한 모델 위로 간다."""
    mr = _module()
    with_score = mr.card({"model_id": "a/b", "benchmarks": [
        {"dataset": "LibriSpeech (clean)", "metric": "wer", "score": 7.5}]})
    assert "scores: LibriSpeech (clean) wer 7.5" in with_score

    prose_only = mr.card({"model_id": "a/c", "benchmarks": [],
                          "evidence": "transcribes a LibriSpeech sample"})
    assert "scores: none extracted" in prose_only
    assert "LibriSpeech" in prose_only, "본문은 그대로 보여 준다 — 판단은 프롬프트가 한다"


def test_placeholder_benchmark_names_are_dropped():
    mr = _module()
    got = mr.card({"model_id": "a/b", "benchmarks": [
        {"dataset": "BENCHMARK", "metric": "x", "score": 1},
        {"dataset": "`t <= 100 ms`", "metric": "", "score": None}]})
    assert "BENCHMARK" not in got.split("card:")[0]


def test_the_prompt_tells_the_model_where_a_score_counts_from():
    mr = _module()
    assert "scores:" in mr.PROMPT and "none extracted" in mr.PROMPT


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
