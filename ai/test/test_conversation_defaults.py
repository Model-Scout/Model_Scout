"""Conversation policy and real checkpoint/resume flow, without external LLM or DB calls."""

import importlib.util
import sys
from pathlib import Path

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location("conversation_graph", ROOT / "17_recommend_graph.py")
rg = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = rg
spec.loader.exec_module(rg)


def plan(**constraints):
    return {
        "summary_ko": "고객 상담", "needs": [], "dataset_terms": ["상담"],
        "dataset_query": "고객 상담 데이터", "clarifying_questions": [],
        "constraints": {**rg.constraint_defaults(), **constraints},
    }


def test_missing_settings_do_not_become_invented_filters(monkeypatch):
    proposed = plan(gpu_memory_gb=8, commercial_only=True)
    proposed["clarifying_questions"] = ["GPU 메모리는 얼마인가요?", "상업용인가요?"]
    monkeypatch.setattr(rg, "_llm_plan", lambda user: proposed)
    result = rg._parse_plan("고객 상담 모델 찾아줘", "model")
    assert result["constraints"] == rg.constraint_defaults()
    assert result["clarifying_questions"] == []


def test_refinement_retains_unmentioned_conditions_and_allows_removal(monkeypatch):
    previous = plan(gpu_memory_gb=8, commercial_only=True, required_artifacts=["gguf"])
    monkeypatch.setattr(rg, "_llm_plan", lambda user: plan())
    kept = rg._parse_plan("고객 상담에 집중해줘", previous=previous["constraints"])
    assert kept["constraints"] == previous["constraints"]
    removed = rg._parse_plan("GPU 제한 없이 찾아줘", previous=previous["constraints"])
    assert removed["constraints"]["gpu_memory_gb"] is None
    assert removed["constraints"]["commercial_only"] is True
    assert removed["constraints"]["required_artifacts"] == ["gguf"]


def test_follow_up_can_pause_resume_and_preserve_conditions(monkeypatch):
    old_plan = plan(gpu_memory_gb=8, commercial_only=True)
    planned = []

    def fake_parse(user, target, said=None, previous=None, prior_plan=None, **kwargs):
        planned.append((user, target, said, previous, prior_plan))
        return plan(**(previous or {}))

    monkeypatch.setattr(rg, "_parse_plan", fake_parse)

    def decompose(state):
        result = plan(**old_plan["constraints"])
        if state.get("turns"):
            result["clarifying_questions"] = ["어떤 상담 내용을 처리하나요?"]
        return {"plan": result, "asking": {"asked": [], "planned": True, "done": False}}

    def explain(state):
        return {"answer": "추천 완료", "turns": [{"request": state["request"], "answer": "추천 완료"}]}

    graph = rg.build_graph({
        "decompose": decompose, "clarify": rg.clarify, "explain": explain,
    }, checkpointer=InMemorySaver())
    config = {"configurable": {"thread_id": "conversation"}}
    graph.invoke({"request": "상담 모델", "route": {"target": "model"}}, config)
    graph.invoke({"request": "상담 목적을 바꿀게"}, config)
    assert rg.pending_questions(graph, config) == ["어떤 상담 내용을 처리하나요?"]
    assert len(graph.get_state(config).values["turns"]) == 1
    graph.invoke(Command(resume="배송 문의"), config)
    state = graph.get_state(config).values
    assert not rg.pending_questions(graph, config)
    assert len(state["turns"]) == 2
    assert state["plan"]["constraints"]["gpu_memory_gb"] == 8
    assert state["plan"]["constraints"]["commercial_only"] is True
    assert planned[-1][4] is not None  # the follow-up planner sees the previous plan
    assert planned[-1][2] == "배송 문의"
    # A different chat never inherits the first chat's history or pending question.
    assert not graph.get_state({"configurable": {"thread_id": "other"}}).values


def test_unknown_answer_uses_defaults_without_another_question(monkeypatch):
    monkeypatch.setattr(rg, "interrupt", lambda payload: "모르겠어 기본값으로 추천해줘")
    monkeypatch.setattr(rg, "_route", lambda request: (_ for _ in ()).throw(AssertionError("no LLM call")))
    monkeypatch.setattr(rg, "_parse_plan", lambda *a, **kw: (_ for _ in ()).throw(AssertionError("no LLM call")))
    result = rg.clarify({
        "request": "추천해줘", "route": {"target": "needs_clarification", "model": "unknown", "data": "unknown"},
    })
    assert result["route"]["target"] == "both" and result["route"]["status"] == "default"
    assert result["asking"]["done"] is True


def test_delegating_a_planning_question_keeps_the_plan(monkeypatch):
    monkeypatch.setattr(rg, "interrupt", lambda payload: "아직 정하지 않았어")
    proposed = {**plan(gpu_memory_gb=8), "clarifying_questions": ["어떤 상담인가요?"]}
    result = rg.clarify({"request": "상담 앱", "route": {"target": "model"}, "plan": proposed,
                         "asking": {"asked": [], "planned": True, "done": False}})
    assert result["plan"]["constraints"]["gpu_memory_gb"] == 8
    assert result["plan"]["clarifying_questions"] == [] and result["asking"]["done"] is True


def test_constraint_mentions_handle_korean_particles_and_words():
    import re
    params, gpu = rg.CONSTRAINT_MENTIONS["max_parameter_count_billion"], rg.CONSTRAINT_MENTIONS["gpu_memory_gb"]
    assert all(re.search(params, s, re.I) for s in ("7B로 바꿔", "7b짜리", "7b 이하"))
    assert not re.search(params, "EXAONE-3.5-7.8B로 바꿔", re.I)  # a size inside a model name is not a limit
    assert not re.search(gpu, "고객 상담 프로그램 만들래", re.I)
    assert re.search(gpu, "램 16기가", re.I)
