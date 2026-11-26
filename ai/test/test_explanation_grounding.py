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


def test_export_uses_the_active_projects_requests_and_clarifications(monkeypatch):
    source = state()
    source.update(
        request="서울로 바꿔 줘\n(질문) 진료과를 제한할까요?\n(답변) 전체요",
        original_request="서울로 바꿔 줘",
        clarification_history=[{"question": "진료과를 제한할까요?", "answer": "전체요"}],
        project_turn_start=1,
        turns=[
            {"request": "이전 프로젝트", "answer": "", "user_inputs": ["이전 프로젝트"]},
            {"request": "병원 검색", "answer": "", "user_inputs": ["병원 검색\n조건: 한국어."]},
            {"request": "이 후보는 왜 추천했어?", "answer": "", "user_inputs": []},
        ],
    )
    monkeypatch.setattr("langgraph.config.get_stream_writer", lambda: lambda _: None)
    monkeypatch.setattr(rg, "_openai", lambda: SimpleNamespace(chat=SimpleNamespace(
        completions=SimpleNamespace(create=lambda **_: iter(())))))
    result = rg.explain(source)
    assert result["requirements"] == [
        "병원 검색\n조건: 한국어.", "서울로 바꿔 줘", "(질문) 진료과를 제한할까요?\n(답변) 전체요",
    ]
    assert result["turns"][0]["user_inputs"] == result["requirements"][1:]


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


def backend_pipeline():
    sys.path.insert(0, str(ROOT.parent))
    from backend.app.result import Pipeline
    return Pipeline


def test_a_flow_with_long_node_ids_still_meets_the_backend_contract():
    # The writer's flow for "사진 속 한국어 글자를 읽어서 번역해주는 앱": "translation" (11 letters) broke the id rule,
    # and the backend dropped the whole flow.
    graph = {"nodes": [{"id": "input", "label": "사진 입력"},
                       {"id": "ocr", "label": "ko-hand-ocr-vl", "candidate_id": "model:localdeel/ko-hand-ocr-vl"},
                       {"id": "translation", "label": "lfm2-1.2b-koen-mt-v4-100k-GGUF",
                        "candidate_id": "model:gyung/lfm2-1.2b-koen-mt-v4-100k-GGUF"},
                       {"id": "Output", "label": "번역 결과" * 10, "note": "결과를 화면에 보여 줘요" * 5}],
             "edges": [{"source": "input", "target": "ocr", "label": "사진"},
                       {"source": "ocr", "target": "translation", "label": "인식된 한국어 텍스트" * 4},
                       {"source": "translation", "target": "Output", "label": "번역된 텍스트"}]}
    Pipeline = backend_pipeline()
    with pytest.raises(ValueError):
        Pipeline.model_validate(json.loads(json.dumps(graph)))  # as the writer wrote it
    tidy = rg.tidy_pipeline(graph)
    Pipeline.model_validate(tidy)
    assert [n["id"] for n in tidy["nodes"]] == ["input", "ocr", "n1", "n2"]
    assert [(e["source"], e["target"]) for e in tidy["edges"]] == [("input", "ocr"), ("ocr", "n1"), ("n1", "n2")]
    assert tidy["nodes"][2]["label"] == "lfm2-1.2b-koen-mt-v4-100k-GGUF"  # a fitting label is kept as written


def test_a_flow_that_already_fits_is_left_alone():
    graph = {"nodes": [{"id": "n1", "label": "입력"}, {"id": "m1", "label": "모델", "candidate_id": "model:a/b"},
                       {"id": "verylongid", "label": "결과"}],
             "edges": [{"source": "n1", "target": "m1"}, {"source": "m1", "target": "verylongid"}]}
    tidy = rg.tidy_pipeline(json.loads(json.dumps(graph)))
    assert [n["id"] for n in tidy["nodes"]] == ["n1", "m1", "n2"]  # the new id skips the one already taken
    assert tidy["edges"][1] == {"source": "m1", "target": "n2"}
    backend_pipeline().model_validate(tidy)


def test_a_flow_naming_candidates_without_their_ids_is_linked_back():
    # The writer's flow for "법률상담 챗봇을 만드려고 하는데 모델이랑 데이터 알려줘": every node lost its candidate_id,
    # so the backend dropped it ("needs a candidate"), though the labels were the candidates' own names.
    models = [{"model_id": "www622846/qwen3.5-9b-rp-lora-v2"}, {"model_id": "woong0322/ko-legal-sbert-finetuned"}]
    datasets = {"project_training": [{"dataset": "woalsdnd/law.go.kr", "title": None}],
                "service_data": [{"dataset": "data_go_kr/1", "title": "법률상담 사례"},
                                 {"dataset": "a/same"}, {"dataset": "b/same"}]}
    graph = {"nodes": [{"id": "input", "label": "법률 상담 질문"}, {"id": "m1", "label": "qwen3.5-9b-rp-lora-v2"},
                       {"id": "m2", "label": "Ko-Legal-SBERT-finetuned"}, {"id": "d1", "label": "law.go.kr"},
                       {"id": "d2", "label": "법률상담 사례"}, {"id": "d3", "label": "same"},
                       {"id": "output", "label": "답변"}],
             "edges": [{"source": "input", "target": "m2"}, {"source": "m2", "target": "d1"},
                       {"source": "d1", "target": "m1"}, {"source": "d2", "target": "m1"}, {"source": "d3", "target": "m1"},
                       {"source": "input", "target": "m1"}, {"source": "m1", "target": "output"}]}
    tidy = rg.tidy_pipeline(graph, rg.candidate_names(models, datasets))
    linked = {n["id"]: n.get("candidate_id") for n in tidy["nodes"]}
    assert linked == {"input": None, "m1": "model:www622846/qwen3.5-9b-rp-lora-v2",
                      "m2": "model:woong0322/ko-legal-sbert-finetuned", "d1": "dataset:woalsdnd/law.go.kr",
                      "d2": "dataset:data_go_kr/1", "d3": None, "output": None}  # "same" is two datasets: never picked
    backend_pipeline().model_validate(tidy)


def test_answer_without_marker_has_no_combination(monkeypatch):
    answer, _ = explain(monkeypatch, state(), "acme/ko-chat-7b 추천.\n")
    assert "acme/ko-chat-7b 추천." in answer
