"""Router wiring in the recommendation graph: which searches run per target; no live LLM or DB."""

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location("recommend_graph", ROOT / "17_recommend_graph.py")
graph17 = importlib.util.module_from_spec(spec)
sys.modules["recommend_graph"] = graph17
spec.loader.exec_module(graph17)

from retrieval_lab import classifier, router  # noqa: E402


def _no_search(*args, **kwargs):
    pytest.fail("search must be skipped for this target")


def test_dataset_target_skips_model_search(monkeypatch):
    monkeypatch.setattr(graph17, "_model_rows", _no_search)
    assert graph17.search_models({"route": {"target": "dataset"}, "plan": {}}) == {"models": []}


def test_model_target_skips_dataset_search(monkeypatch):
    monkeypatch.setattr(graph17, "load_graph", _no_search)
    out = graph17.search_datasets({"route": {"target": "model"}, "plan": {}, "models": []})
    assert out["datasets"] == {"per_model": {}, "project_training": [], "service_data": []}


def test_router_failure_searches_both(monkeypatch):
    monkeypatch.setattr(
        router, "route", lambda text, use_cache: router.RoutingResult(None, "unavailable", "error", 1.0)
    )
    assert graph17.route({"request": "x"})["route"] == {"target": "both", "status": "unavailable"}


def test_follow_up_keeps_first_target(monkeypatch):
    monkeypatch.setattr(router, "route", _no_search)
    assert graph17.route({"request": "x", "route": {"target": "dataset", "status": "ok"}}) == {}


def test_unclear_target_asks_and_reroutes(monkeypatch):
    asked = []
    monkeypatch.setattr(graph17, "interrupt", lambda value: asked.append(value) or "데이터셋만")
    monkeypatch.setattr(graph17, "_parse_plan", lambda request: {"clarifying_questions": []})
    monkeypatch.setattr(router, "route", lambda text, use_cache: router.RoutingResult("dataset", "ok", "llm", 1.0))
    out = graph17.clarify(
        {"request": "좋은 거 찾아줘", "route": {"target": "needs_clarification"}, "plan": {"clarifying_questions": []}}
    )
    assert asked == [{"questions": [graph17.TARGET_QUESTION]}]
    assert out["route"]["target"] == "dataset"


@pytest.mark.parametrize(
    "target,rule,llm,expected",
    [
        ("dataset", None, None, None),  # no model search, no call
        ("model", "lexical_exact", None, "lexical_exact"),  # rule hit, no LLM call
        ("both", "lexical_exact", "semantic_capability", "semantic_capability"),  # rules skipped for both
        ("model", None, RuntimeError("down"), None),  # failure is recorded as None, never raised
    ],
)
def test_model_query_type(monkeypatch, target, rule, llm, expected):
    monkeypatch.setattr(classifier, "rule_type", lambda text: rule)

    def fake_llm(text, use_cache):
        assert use_cache is False and target != "dataset"
        if isinstance(llm, Exception):
            raise llm
        return llm, 1.0

    monkeypatch.setattr(classifier, "llm_type", fake_llm)
    state = {"request": "질문", "route": {"target": target}}
    assert graph17.classify_model_query(state) == {"model_query_type": expected}
