"""data_conditions.check (no LLM) and how 17 runs the reader beside the planner."""

import importlib.util
import sys
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import data_conditions as dc  # noqa: E402

spec = importlib.util.spec_from_file_location("recommend_graph_dc", ROOT / "17_recommend_graph.py")
graph17 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = graph17
spec.loader.exec_module(graph17)


def llm(**fields):
    return {**dc.defaults(), **fields}


def test_regions_scope_and_detail_are_kept_apart():
    said = "청주 공중화장실 위치, 전국 단위면 더 좋아"
    out = dc.check(llm(region="충북", region_detail="청주", region_evidence="청주"), said)
    assert (out["region"], out["region_detail"]) == ("충북", "청주")  # 충북 to search, 청주 to tell results apart
    out = dc.check(llm(region="청주", region_evidence="청주"), said)
    assert (out["region"], out["region_detail"]) == (None, "청주")  # a 시군구 is never a 시도
    out = dc.check(llm(region="전국", region_detail="전국", region_evidence="전국 단위"), said)
    assert (out["region"], out["region_detail"], out["region_scope"]) == (None, None, "전국")


def test_a_quote_must_exist_and_back_the_value():
    said = "식품 영양성분을 API로 받고 싶어요"
    out = dc.check(llm(delivery="api", formats=["CSV"], delivery_evidence="API로"), said)
    assert out["delivery"] == "api" and out["formats"] == []  # "API로" never backs CSV
    assert dc.check(llm(delivery="file", delivery_evidence="API로"), said)["delivery"] is None  # real words, wrong value
    assert dc.check(llm(current_value=True, freshness_evidence="실시간"), said)["current_value"] is False  # not said
    negated = dc.check(llm(delivery="api", delivery_evidence="API 말고 파일로"), "API 말고 파일로 주세요")
    assert negated["delivery"] is None
    assert dc.check(llm(delivery="file", delivery_evidence="API 말고 파일로"), "API 말고 파일로 주세요")["delivery"] == "file"
    spatial = dc.check(llm(delivery="file", formats=["SHP"], delivery_evidence="SHP 파일"), "침수흔적도를 SHP 파일로")
    assert spatial["delivery"] == "file" and spatial["formats"] == ["SHP"]


def test_a_follow_up_keeps_checked_conditions_and_may_change_them():
    first = dc.check(llm(delivery="api", delivery_evidence="API로", preferences=["접근성 정보 우선"]),
                     "API로 받고 싶어, 접근성 정보 우선")
    kept = dc.check(first, "상업용만", previous=first)  # carried over unchanged
    assert kept["delivery"] == "api" and kept["preferences"] == ["접근성 정보 우선"]
    changed = dc.check({**first, "delivery": "file", "delivery_evidence": "파일로"}, "API로 받고 싶어 이제 파일로 줘", previous=first)
    assert changed["delivery"] == "file"
    unbacked = dc.check({**first, "kogl_type1_only": True, "kogl_type1_only_evidence": "1유형"}, "상업용만", previous=first)
    assert unbacked["kogl_type1_only"] is False


def test_reader_runs_only_on_dataset_turns_and_never_fails_the_turn():
    calls = []
    graph17._read_conditions = lambda *a: calls.append(a) or {"status": "ok", **dc.defaults()}
    plan, cond = graph17._with_conditions("model", lambda: "plan", "모델 찾아줘")
    assert (plan, cond, calls) == ("plan", None, [])
    assert graph17._with_conditions("dataset", lambda: "plan", "q")[1]["status"] == "ok"

    def broken(*a):
        raise RuntimeError("api down")
    graph17._read_conditions = broken
    assert graph17._with_conditions("both", lambda: "plan", "q") == ("plan", {"status": "unavailable", "reason": "RuntimeError"})

    graph17._read_conditions = lambda *a: time.sleep(0.5)
    old, graph17.CONDITIONS_TIMEOUT_S = graph17.CONDITIONS_TIMEOUT_S, 0.05
    try:
        assert graph17._with_conditions("dataset", lambda: "plan", "q")[1] == {"status": "unavailable", "reason": "timeout"}
    finally:
        graph17.CONDITIONS_TIMEOUT_S = old


@pytest.mark.parametrize("prompt_phrase", ["dataset_terms: 1-5 short words", "dataset_query: one Korean sentence"])
def test_planner_prompt_is_untouched(prompt_phrase):
    assert prompt_phrase in graph17.DECOMPOSE_PROMPT and "data_conditions" not in graph17.DECOMPOSE_PROMPT
    assert "data_conditions" not in graph17.ProjectPlan.model_fields
