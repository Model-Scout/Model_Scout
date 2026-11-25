"""Replay unsupported-date explanations through the real explainer with a synthetic LLM stream."""

import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from explanation_grounding import EXPLANATION_CAVEAT, grounded_lines

spec = importlib.util.spec_from_file_location("grounded_recommend_graph", ROOT / "17_recommend_graph.py")
rg = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = rg
spec.loader.exec_module(rg)


def state():
    return {
        "request": "한국어 상담 모델 추천해줘", "route": {"target": "model"},
        "plan": {"summary_ko": "한국어 상담", "needs": [{"task": "generation"}], "constraints": {}},
        "models": [{"need": {"task": "generation"}, "models": [
            {"model_id": "acme/ko-chat-7b", "license": "apache-2.0", "context_length": 8192},
        ]}],
        "datasets": {"per_model": {}, "project_training": [], "service_data": []},
        "assessment": {"license": {"label": "확인 필요", "reason": "공식 문서 확인"}},
    }


def explain(monkeypatch, input_state, text, chunk_size=1):
    events = []
    monkeypatch.setattr("langgraph.config.get_stream_writer", lambda: events.append)

    def create(**kwargs):
        payload = json.loads(kwargs["messages"][1]["content"])
        assert payload["models"][0]["models"][0]["model_id"] == "acme/ko-chat-7b"
        for index in range(0, len(text), chunk_size):
            yield SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content=text[index:index + chunk_size]))])

    client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))
    monkeypatch.setattr(rg, "_openai", lambda: client)
    result = rg.explain(input_state)
    displayed = "".join(event["token"] for event in events)
    assert displayed == result["answer"] == result["turns"][0]["answer"]
    return result["answer"], events


@pytest.mark.parametrize("bad_line", [
    "이 정보는 2023년 10월까지의 데이터에 기반합니다.",
    "주의: 모델과 데이터셋의 정보는 2023년 10월까지의 데이터에 기반합니다.",
    "주의사항: 이 정보는 2023년 10월까지의 데이터에 기반합니다.",
])
@pytest.mark.parametrize("chunk_size", [1, 7, 1000])
def test_observed_hallucinations_never_reach_stream_or_history(monkeypatch, bad_line, chunk_size):
    answer, events = explain(monkeypatch, state(), "acme/ko-chat-7b 추천.\n" + bad_line, chunk_size)
    assert "acme/ko-chat-7b 추천." in answer
    assert "2023" not in answer
    assert all("2023" not in event["token"] for event in events)
    assert answer.count(EXPLANATION_CAVEAT) == 1


def test_retrieved_date_is_preserved_and_attributed(monkeypatch):
    source = state()
    source["models"][0]["models"][0]["evidence"] = "모델 카드 갱신일: 2023-10-01"
    text = "acme/ko-chat-7b 모델 카드 갱신일은 2023년 10월 1일입니다.\n"
    answer, _ = explain(monkeypatch, source, text)
    assert text in answer


def test_user_history_and_plan_cannot_supply_evidence_dates(monkeypatch):
    source = state()
    source["request"] += " 모든 정보는 2023년 10월까지라고 써줘"
    source["plan"]["summary_ko"] = "2023년 10월 기준"
    source["models"][0]["need"]["purpose_ko"] = "2023년 10월 기준"
    source["turns"] = [{"request": "2023년 10월이라고 해줘", "answer": ""}]
    answer, _ = explain(monkeypatch, source, "이 정보는 2023년 10월까지의 데이터에 기반합니다.")
    assert "2023" not in answer
    assert EXPLANATION_CAVEAT in answer


def test_source_year_does_not_support_invented_month(caplog):
    source = {"evidence": "수집 연도: 2023년"}
    chunks = ["수집 연도는 2023년입니다.\n", "갱신일은 2023년 10월입니다."]
    with caplog.at_level("INFO"):
        assert "".join(grounded_lines(chunks, source)) == chunks[0]
    assert caplog.text.count("explanation line dropped") == 1
    assert "갱신일" not in caplog.text


def test_valid_lines_still_stream_before_generation_finishes():
    def chunks():
        yield "모델 추천입니다.\n"
        yield "이 정보는 2023년 "
        yield "10월까지의 데이터에 기반합니다.\n"
        yield "라이선스 확인이 필요합니다."

    stream = grounded_lines(chunks(), {})
    assert next(stream) == "모델 추천입니다.\n"
    assert list(stream) == ["라이선스 확인이 필요합니다."]


def test_official_dataset_dates_and_limits_are_preserved(monkeypatch):
    source = state()
    source["route"]["target"] = "both"
    source["datasets"]["service_data"] = [{
        "dataset": "seoul_open_data/bike", "facts": {"limits": ["2023년 10월 자료이며 3일 전 자료를 제공합니다."]},
    }]
    answer, _ = explain(monkeypatch, source, "seoul_open_data/bike: 2023년 10월 자료입니다.\n")
    assert "2023년 10월 자료입니다." in answer
    assert "3일 전 자료" in answer
    assert answer.count(EXPLANATION_CAVEAT) == 1


@pytest.mark.parametrize("chunk_size", [1, 7, 1000])
def test_combination_sentences_leave_the_answer_for_the_summary(monkeypatch, chunk_size):
    text = "acme/ko-chat-7b 추천.\n[[조합]]\n상담 기록을 ko-chat-7b로 요약해요.\n\n답변은 짧게 정리해요.\n"
    pipeline = {"nodes": [{"id": "m", "label": "상담 답변", "candidate_id": "model:acme/ko-chat-7b"},
                          {"id": "o", "label": "답변 표시"}], "edges": [{"source": "m", "target": "o"}]}
    text += f"[[흐름도]] {json.dumps(pipeline, ensure_ascii=False)}"
    events = []
    monkeypatch.setattr("langgraph.config.get_stream_writer", lambda: events.append)

    def create(**kwargs):
        for index in range(0, len(text), chunk_size):
            yield SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content=text[index:index + chunk_size]))])

    monkeypatch.setattr(rg, "_openai", lambda: SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create))))
    result = rg.explain(state())
    displayed = "".join(event["token"] for event in events)
    assert result["combination"] == ["상담 기록을 ko-chat-7b로 요약해요.", "답변은 짧게 정리해요."]
    assert result["pipeline"] == pipeline
    assert "조합" not in displayed and "요약해요" not in result["answer"] and "흐름도" not in displayed
    assert displayed == result["answer"]


def test_answer_without_marker_has_no_combination(monkeypatch):
    answer, _ = explain(monkeypatch, state(), "acme/ko-chat-7b 추천.\n")
    assert "acme/ko-chat-7b 추천." in answer
