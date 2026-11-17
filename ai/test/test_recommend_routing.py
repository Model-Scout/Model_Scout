"""Router wiring in the recommendation graph: which searches run per target; no live LLM or DB."""

import importlib.util
import json
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


@pytest.mark.parametrize(
    "old,new,status,expected",
    [
        ("dataset", "model", "ok", "both"),  # "모델도 찾아줘" widens to both
        ("model", "dataset", "ok", "both"),
        ("dataset", "dataset", "ok", None),  # same side: unchanged
        ("dataset", "needs_clarification", "ok", None),  # refinement ("상업용만"): unchanged
        ("dataset", None, "error", None),  # router down: unchanged, not widened to both
        ("both", "model", "ok", None),  # never narrows
        ("needs_clarification", "model", "ok", "model"),
    ],
)
def test_follow_up_reroutes_and_only_widens(monkeypatch, old, new, status, expected):
    monkeypatch.setattr(router, "route", lambda text, use_cache: router.RoutingResult(new, status, "llm", 1.0))
    out = graph17.route({"request": "x", "route": {"target": old, "status": "ok"}})
    assert out == ({"route": {"target": expected, "status": "ok"}} if expected else {})


@pytest.mark.parametrize(
    "old,text,expected",
    [
        ("dataset", "이제 모델만 찾아줘", "model"),
        ("both", "데이터는 빼줘", "model"),
        ("both", "모델 말고 데이터만 보여줘", "dataset"),
        ("both", "데이터는 이미 있어. 모델만 추천해줘", "model"),
        ("dataset", "데이터는 빼고 모델 찾아줘", "model"),
        ("model", "모델만 다시 보여줘", None),  # already model: unchanged
    ],
)
def test_follow_up_explicit_change_replaces_target(monkeypatch, old, text, expected):
    monkeypatch.setattr(router, "route", _no_search)  # explicit wording needs no router call
    out = graph17.route({"request": text, "route": {"target": old, "status": "ok"}})
    assert out == ({"route": {"target": expected, "status": "ok"}} if expected else {})


FOLLOW_UPS = [
    json.loads(line)
    for line in (ROOT / "test" / "golden" / "labels" / "follow_up_routing.jsonl").read_text(encoding="utf-8").splitlines()
    if line.strip()
]


@pytest.mark.parametrize("row", FOLLOW_UPS, ids=[r["id"] for r in FOLLOW_UPS])
def test_follow_up_golden_split_between_rule_and_llm(monkeypatch, row):
    """by=rule rows are decided without an LLM; by=llm rows must reach the LLM path (its future eval set)."""
    asked = []
    monkeypatch.setattr(graph17, "_follow_up_by_llm", lambda text, old: asked.append(text) or old)
    target, decided_by = graph17.follow_up_target(row["text"], row["previous"])
    assert decided_by == row["by"]
    if row["by"] == "rule":
        assert target == row["target"] and not asked
    else:
        assert asked == [row["text"]]


def test_service_wording_is_not_an_only_marker():
    assert graph17._side_change("모델 만들고 싶어", "dataset") is None


def test_unsupported_task_is_not_searched_unfiltered(monkeypatch):
    searched = []
    monkeypatch.setattr(graph17, "_load_09", lambda: type("M", (), {"contract_filters_enabled": staticmethod(lambda: False)}))
    monkeypatch.setattr(
        graph17, "_model_rows", lambda query, tags, *a: searched.append(tags) or {"rows": [], "contract_filters_applied": False}
    )
    plan = {
        "needs": [
            {"task": "forecasting", "purpose_ko": "p", "model_query": "수요 예측"},
            {"task": "reranking", "purpose_ko": "p", "model_query": "리랭커"},  # tagless but covered
            {"task": "tool_use", "purpose_ko": "p", "model_query": "함수 호출"},  # an LLM feature
            {"task": "ocr", "purpose_ko": "p", "model_query": "문서 OCR"},  # a VLM feature
        ],
        "constraints": {},
    }
    groups = graph17.search_models({"route": {"target": "both"}, "plan": plan})["models"]
    assert groups[0] == {"need": plan["needs"][0], "models": [], "unsupported": True}
    assert searched == [(), ("text-generation",), ("image-text-to-text",)]
    assert not any("unsupported" in g for g in groups[1:])


def test_planner_sees_search_target(monkeypatch):
    sent = []
    monkeypatch.setattr(graph17, "_llm_plan", lambda user: sent.append(user) or {"constraints": {}})
    graph17.decompose({"request": "따릉이 대여소 데이터 찾아줘 planner-target-test", "route": {"target": "dataset"}})
    assert sent[-1].startswith("SEARCH_TARGET: dataset\n")


def test_unclear_target_asks_and_reroutes(monkeypatch):
    asked = []
    monkeypatch.setattr(graph17, "interrupt", lambda value: asked.append(value) or "데이터셋만")
    planned = []
    monkeypatch.setattr(
        graph17, "_parse_plan", lambda request, target: planned.append(target) or {"clarifying_questions": []}
    )
    monkeypatch.setattr(router, "route", lambda text, use_cache: router.RoutingResult("dataset", "ok", "llm", 1.0))
    out = graph17.clarify(
        {"request": "좋은 거 찾아줘", "route": {"target": "needs_clarification"}, "plan": {"clarifying_questions": []}}
    )
    assert asked == [{"questions": [graph17.TARGET_QUESTION]}]
    assert out["route"]["target"] == "dataset"
    assert planned == ["dataset"]  # re-planned for the answered target, not the unclear one


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
