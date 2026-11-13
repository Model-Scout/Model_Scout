"""Routing contract and lexical regression tests; no live LLM or model download."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from retrieval_lab import classifier, router


@pytest.mark.parametrize("text", [
    "일본어 문서를 한국어로 번역할 모델, GPU 6GB에서 쓸 거야",
    "영→한 번역 모델", "ko -> fr 번역", "한국어→영어 번역 모델",
    "GGUF로 된 3B 이하 한국어 요약 모델", "KoELECTRA 기반 감성분석 모델",
    "KLUE-RoBERTa 베이스 임베딩 모델", "KoBART 기반 요약 모델",
    "KLUE-RoBERTa를 베이스로 만든 한국어 임베딩 모델",
])
def test_lexical_anchors_do_not_need_an_llm(text):
    assert classifier.rule_type(text) == "lexical_exact"


@pytest.mark.parametrize("text", [
    "GGUF 모델의 KMMLU 벤치마크 점수 알려줘",
    "영어와 한국어로 대화하는 모델", "GPU 8GB에서 돌릴 요약 모델",
    "ONNX는 필요 없고 한국어 요약만 잘하면 돼",
    "GGUF 말고 성능 좋은 모델 찾아줘",
    "한국어 음성을 받아 적으면서 영어로 번역까지 해 주는 모델",
])
def test_ambiguous_or_benchmark_requests_are_left_to_llm(text):
    assert classifier.rule_type(text) is None


def test_named_comparison_precedes_format():
    assert classifier.rule_type("a와 b GGUF 성능 비교", ["org/a", "org/b"]) == "model_comparison"


@pytest.mark.parametrize("payload", [
    {"target": "dataset", "model_query_type": "semantic_capability"},
    {"target": "both", "model_query_type": "invented"},
    {"target": "huggingface", "model_query_type": None},
    {"target": "dataset"}, [], None,
])
def test_invalid_response_cannot_dispatch(payload):
    with pytest.raises(ValueError):
        router.validate_response(payload)


@pytest.mark.parametrize("text,payload", [
    ("모델 학습에 쓸 공공데이터", {"target": "dataset", "model_query_type": None}),
    ("HF 학습 데이터셋", {"target": "dataset", "model_query_type": None}),
    ("Kaggle 교통량 데이터", {"target": "dataset", "model_query_type": None}),
    ("GGUF 모델", {"target": "model", "model_query_type": "lexical_exact"}),
    ("GGUF 모델 학습 데이터만", {"target": "dataset", "model_query_type": None}),
    ("교통량 데이터와 예측 모델", {"target": "both", "model_query_type": "semantic_capability"}),
    ("HF에서 좋은 거", {"target": "needs_clarification", "model_query_type": None}),
])
def test_single_call_then_cache(monkeypatch, tmp_path, text, payload):
    calls = []

    def fake_call(query, model, prompt):
        calls.append((query, model, prompt))
        return payload

    monkeypatch.setattr(router, "CACHE_DIR", tmp_path)
    monkeypatch.setattr(classifier, "_call_llm", fake_call)
    first = router.route(text)
    second = router.route(text)
    assert len(calls) == 1
    assert (first.target, first.model_query_type, first.status) == (
        payload["target"], payload["model_query_type"], "ok")
    assert second.source == "cache"
    assert (second.target, second.model_query_type) == (first.target, first.model_query_type)


def test_empty_model_type_is_filled_by_classifier(monkeypatch, tmp_path):
    calls = []
    monkeypatch.setattr(router, "CACHE_DIR", tmp_path / "routing")
    monkeypatch.setattr(classifier, "CACHE_PATH", tmp_path / "classifier.json")

    def fake(text, model, prompt=None):
        calls.append(prompt)
        return {"target": "both", "model_query_type": None} if prompt else {"type": "semantic_capability"}

    monkeypatch.setattr(classifier, "_call_llm", fake)
    result = router.route("교통량 데이터랑 예측 모델 같이 찾아줘")
    assert (result.status, result.target, result.model_query_type) == ("ok", "both", "semantic_capability")
    assert len(calls) == 2


def test_model_type_in_target_slot_means_model():
    assert router.validate_response({"target": "model_comparison", "model_query_type": None}) == ("model", "model_comparison")


def test_extra_response_fields_are_ignored():
    assert router.validate_response({"target": "dataset", "model_query_type": None, "reason": "x"}) == ("dataset", None)


def test_dataset_clause_does_not_override_both_model_intent(monkeypatch, tmp_path):
    monkeypatch.setattr(router, "CACHE_DIR", tmp_path)
    monkeypatch.setattr(classifier, "_call_llm", lambda *a, **kw: {
        "target": "both", "model_query_type": "semantic_capability"})
    result = router.route("영→한 번역 데이터와 한국어 요약 모델 각각 찾아줘")
    assert result.model_query_type == "semantic_capability"


def test_invalid_response_is_not_cached_or_retried(monkeypatch, tmp_path):
    calls = []
    monkeypatch.setattr(router, "CACHE_DIR", tmp_path)

    def invalid(*args, **kwargs):
        calls.append(1)
        return {"target": "model", "model_query_type": "invalid"}

    monkeypatch.setattr(classifier, "_call_llm", invalid)
    result = router.route("한국어 모델")
    assert result.status == "invalid_response"
    assert result.target is None
    assert len(calls) == 1
    assert not list(tmp_path.iterdir())


def test_unavailable_is_not_user_ambiguity(monkeypatch, tmp_path):
    monkeypatch.setattr(router, "CACHE_DIR", tmp_path)

    def unavailable(*args, **kwargs):
        raise TimeoutError("provider timed out")

    monkeypatch.setattr(classifier, "_call_llm", unavailable)
    result = router.route("한국어 모델")
    assert (result.status, result.target) == ("unavailable", None)


def test_empty_query_does_not_call_llm(monkeypatch):
    monkeypatch.setattr(classifier, "_call_llm", lambda *a, **kw: pytest.fail("Unexpected API request"))
    assert router.route("  ").target == "needs_clarification"


def test_prompt_change_invalidates_cache():
    assert "모델 학습" in router.PROMPT
    assert "Hugging Face datasets" in router.PROMPT
    assert router.cache_path("query", "model-a") != router.cache_path("query", "model-b")


def test_invalid_legacy_output_is_logged_not_cached(monkeypatch, tmp_path, caplog):
    monkeypatch.setattr(classifier, "CACHE_PATH", tmp_path / "legacy.json")
    monkeypatch.setattr(classifier, "_call_llm", lambda *a, **kw: {"type": "invented"})
    assert classifier.llm_type("모델", "test-model")[0] == "semantic_capability"
    assert "Invalid model classification" in caplog.text
    assert not classifier.CACHE_PATH.exists()
