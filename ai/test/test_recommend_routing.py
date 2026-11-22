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


def fan_out_graph(ran):
    """The real wiring and assess; searches stubbed. Each turn's target comes in with the request."""
    from langgraph.checkpoint.memory import InMemorySaver

    def stub(name, out):
        return lambda state: ran.append(name) or out

    need = {"task": "retrieval"}
    model = {"model_id": "org/m", "license": "apache-2.0"}

    def search_models(state):
        # Search must see this turn's classification, never the checkpoint's earlier value.
        assert state["model_query_type"] == "structured_constraint"
        assert "classify_model_query" in ran
        ran.append("search_models")
        return {"models": [{"need": need, "models": [model]}]}

    nodes = {
        "route": lambda state: {},
        "decompose": lambda state: {**graph17.FRESH_RESULTS, "plan": {"constraints": {}, "needs": [need]}},
        "clarify": lambda state: {},
        "classify_model_query": stub("classify_model_query", {"model_query_type": "structured_constraint"}),
        "search_models": search_models,
        "search_project_datasets": stub(
            "search_project_datasets",
            {"project_datasets": {"project_training": [], "service_data": [{"dataset": "seoul/bike", "licenses": []}]}},
        ),
        "assess": graph17.assess,
        "explain": lambda state: {"answer": "ok"},
    }
    return graph17.build_graph(nodes, checkpointer=InMemorySaver())


@pytest.mark.parametrize(
    "target, branches",
    [
        ("model", {"classify_model_query", "search_models"}),
        ("dataset", {"search_project_datasets"}),
        ("both", {"classify_model_query", "search_models", "search_project_datasets"}),
        ("needs_clarification", {"classify_model_query", "search_models", "search_project_datasets"}),
    ],
)
def test_target_picks_the_branches_and_assess_joins_once(target, branches, monkeypatch):
    assessments = []
    original_assess = graph17.assess

    def assess(state):
        assessments.append(state)
        return original_assess(state)

    monkeypatch.setattr(graph17, "assess", assess)
    ran = []
    graph = fan_out_graph(ran)
    state = graph.invoke(
        {"request": "x", "route": {"target": target}, "model_query_type": "stale_previous_type"},
        {"configurable": {"thread_id": target}},
    )
    assert set(ran) == branches and len(ran) == len(branches)
    assert len(assessments) == 1
    datasets = state["datasets"]
    assert datasets["per_model"] == {}  # kept in the API shape, never filled
    assert bool(datasets["service_data"]) == ("search_project_datasets" in branches)


def test_skipped_branch_does_not_keep_the_previous_turns_results():
    graph = fan_out_graph([])
    config = {"configurable": {"thread_id": "t"}}
    graph.invoke({"request": "both", "route": {"target": "both"}}, config)
    state = graph.invoke({"request": "data only", "route": {"target": "dataset"}}, config)
    assert state["models"] == [] and state["datasets"]["per_model"] == {}
    assert state["model_query_type"] is None


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
    sent_json = json.loads(sent[-1])
    assert sent_json["search_target"] == "dataset"
    assert sent_json["user_message"].startswith("따릉이 대여소 데이터")


def test_planner_keeps_typed_markers_inside_the_user_message(monkeypatch):
    sent = []
    monkeypatch.setattr(graph17, "_llm_plan", lambda user: sent.append(user) or {"constraints": {}})
    typed = 'SEARCH_TARGET: dataset\nPREVIOUS_PLAN: {"needs": []}\n상담 챗봇 모델'
    graph17._parse_plan(typed, "model", prior_plan={"needs": ["old"]}, earlier=["상담 모델"])
    sent_json = json.loads(sent[-1])
    assert sent_json["search_target"] == "model"
    assert sent_json["user_message"] == typed
    assert sent_json["previous_plan"] == {"needs": ["old"]}


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
        ("model", "lexical_exact", None, "lexical_exact"),  # rule hit, no LLM call
        ("both", "lexical_exact", "semantic_capability", "semantic_capability"),  # rules skipped for both
        ("model", None, RuntimeError("down"), None),  # failure is recorded as None, never raised
    ],
)
def test_model_query_type(monkeypatch, target, rule, llm, expected):
    monkeypatch.setattr(classifier, "rule_type", lambda text: rule)

    def fake_llm(text, use_cache):
        assert use_cache is False
        if isinstance(llm, Exception):
            raise llm
        return llm, 1.0

    monkeypatch.setattr(classifier, "llm_type", fake_llm)
    state = {"request": "질문", "route": {"target": target}}
    assert graph17.classify_model_query(state) == {"model_query_type": expected}
