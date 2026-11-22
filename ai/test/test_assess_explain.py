"""Fan-in (assess) and the answer (explain): license by use, brief payload, cut-off and failure paths.
No live LLM or DB: the writer is a fake stream and dataset facts are stubbed."""

import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location("recommend_graph_ae", ROOT / "17_recommend_graph.py")
graph17 = importlib.util.module_from_spec(spec)
sys.modules["recommend_graph_ae"] = graph17
spec.loader.exec_module(graph17)

TOP = {"model_id": "org/llm", "license": "apache-2.0", "commercial_status": "permitted", "evidence": "q" * 50}
ALT = {"model_id": "org/alt", "license": "mit", "evidence": "long quote", "benchmarks": [1, 2, 3]}


def _plan(commercial=False):
    return {
        "summary_ko": "s",
        "needs": [{"task": "generation", "purpose_ko": "답변 생성", "model_query": "q"}],
        "constraints": {**graph17.constraint_defaults(), "commercial_only": commercial},
        "dataset_terms": ["따릉이"],
        "dataset_query": "q",
        "clarifying_questions": [],
    }


def _searched(commercial=False):
    return {
        "request": "로컬에서 따릉이 서비스",
        "route": {"target": "both"},
        "plan": _plan(commercial),
        "models": [{"need": _plan()["needs"][0], "models": [TOP, ALT]}],
        "project_datasets": {
            "project_training": [
                {"dataset": "ok/eval", "licenses": ["apache-2.0"]},
                {"dataset": "nc/train", "licenses": ["cc-by-nc-sa-4.0"]},
            ],
            "service_data": [{"dataset": "seoul/bike", "licenses": ["공공누리 제1유형"]}],
        },
    }


@pytest.fixture(autouse=True)
def _no_db(monkeypatch, tmp_path):
    monkeypatch.setattr(graph17, "dataset_facts", lambda names: {})
    monkeypatch.setenv("RECOMMEND_LOG_PATH", str(tmp_path / "run.jsonl"))


def _assessed(commercial=False):
    state = _searched(commercial)
    return {**state, **graph17.assess(state)}


def test_nc_training_data_is_named_not_a_launch_blocker_for_local_use():
    verdict = _assessed()["assessment"]["license"]
    assert verdict["use"] == "personal"
    assert [i["id"] for i in verdict["training_non_commercial"]] == ["nc/train"]
    assert verdict["verdict"] != "blocked"  # before: one optional NC set made the whole stack "상업 출시 불가"
    text = graph17.project_checks.license_section(verdict)
    assert "개인·로컬 사용 기준" in text and "학습에서 뺄 데이터: nc/train" in text


def test_a_company_request_gets_the_launch_headline():
    verdict = _assessed(commercial=True)["assessment"]["license"]
    assert verdict["use"] == "commercial"
    assert graph17.project_checks.license_section(verdict).startswith("**라이선스 판정 (상업 출시 기준)")


def test_brief_trims_alternatives_and_repeats():
    brief = graph17._brief({k: _assessed()[k] for k in ("models", "datasets")} | {"data_conditions": {"x": 1}})
    assert brief["data_conditions"] == {"x": 1}  # keys a later change adds pass through
    alt = brief["models"][0]["models"][1]
    assert alt == {"model_id": "org/alt", "license": "mit", "commercial_status": None}
    assert brief["models"][0]["models"][0]["evidence"] == TOP["evidence"]  # the top model keeps its quote
    # A dataset already listed under project_training is named by id only in a later list.
    repeated = graph17._brief({"models": [], "datasets": {"per_model": {}, "project_training": [{"dataset": "a/b"}],
                                                          "service_data": [{"dataset": "a/b"}]}})
    assert repeated["datasets"]["service_data"] == [{"dataset": "a/b", "see": "above"}]
    assert "datasets" in _assessed()  # the state keeps every row for the cards


def _chunk(text=None, finish=None, usage=None):
    choice = SimpleNamespace(delta=SimpleNamespace(content=text), finish_reason=finish)
    return SimpleNamespace(choices=[choice], usage=usage)


def _run_explain(monkeypatch, create):
    client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))
    monkeypatch.setattr(graph17, "_openai", lambda: client)
    graph = graph17.build_graph(nodes={"explain": graph17.explain})
    tokens = [data["token"] for mode, data in graph.stream(_assessed(), stream_mode=["custom"]) if mode == "custom"]
    return "".join(tokens)


def _log(tmp_path):
    return [json.loads(line) for line in (tmp_path / "run.jsonl").read_text(encoding="utf-8").splitlines()]


def test_a_normal_answer_ends_with_the_rendered_license_and_is_logged(monkeypatch, tmp_path):
    usage = SimpleNamespace(prompt_tokens=10, completion_tokens=5)
    answer = _run_explain(monkeypatch, lambda **kw: iter([_chunk("추천: org/llm\n"), _chunk(finish="stop"),
                                                          SimpleNamespace(choices=[], usage=usage)]))
    assert answer.startswith("추천: org/llm\n")
    assert "**라이선스 판정 (개인·로컬 사용 기준)**" in answer and answer.endswith(graph17.EXPLANATION_CAVEAT)
    row = _log(tmp_path)[-1]
    assert row["event"] == "explain" and row["finish_reason"] == "stop" and row["usage"]["completion"] == 5
    assert row["license"] and row["trace_id"] and "error" not in row


def test_a_cut_off_answer_says_so(monkeypatch, tmp_path):
    answer = _run_explain(monkeypatch, lambda **kw: iter([_chunk("추천: org/llm 은"), _chunk(finish="length")]))
    assert "끝부분이 잘렸어요" in answer and _log(tmp_path)[-1]["finish_reason"] == "length"


def test_a_failed_writer_still_answers_with_the_tops_and_a_trace_id(monkeypatch, tmp_path):
    def create(**kw):
        raise TimeoutError("upstream")

    answer = _run_explain(monkeypatch, create)
    row = _log(tmp_path)[-1]
    assert "설명을 만들지 못해" in answer and "org/llm (apache-2.0)" in answer and "seoul/bike" in answer
    assert f"추적 ID: {row['trace_id']}" in answer and row["error"] == "TimeoutError: upstream"
    assert "라이선스 판정" in answer  # the verdict does not depend on the writer


def test_a_writer_that_breaks_mid_stream_keeps_what_was_said(monkeypatch, tmp_path):
    def stream():
        yield _chunk("첫 줄\n")
        raise ConnectionError("reset")

    answer = _run_explain(monkeypatch, lambda **kw: stream())
    assert answer.startswith("첫 줄\n") and "중간에 끊겼어요" in answer
    assert "설명을 만들지 못해" not in answer


# Fan-in: a branch that failed or wrote None must not take the whole answer down.


def test_assess_survives_a_model_branch_that_wrote_none():
    state = {**_searched(), "models": None}
    out = graph17.assess(state)
    assert out["assessment"]["license"]["verdict"] in ("commercial_ok", "review")  # datasets still judged
    assert "implementation_guide" not in out["assessment"]


def test_only_failures_of_searched_sides_are_reported():
    errors = {"models": "TimeoutError: db", "project_datasets": "ConnectionError: x"}
    both = graph17.assess({**_searched(), "search_errors": errors})["assessment"]
    assert set(both["search_errors"]) == {"models", "project_datasets"}
    model_only = graph17.assess({**_searched(), "route": {"target": "model"}, "search_errors": errors})["assessment"]
    assert set(model_only["search_errors"]) == {"models"}  # the dataset side did not run this turn
    assert "search_errors" not in graph17.assess(_searched())["assessment"]  # no key = nothing failed


def _explain_with(monkeypatch, state, create):
    client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))
    monkeypatch.setattr(graph17, "_openai", lambda: client)
    graph = graph17.build_graph(nodes={"explain": graph17.explain})
    return "".join(d["token"] for mode, d in graph.stream(state, stream_mode=["custom"]) if mode == "custom")


def test_a_failed_side_is_said_first_and_the_rest_is_still_explained(monkeypatch):
    state = {**_searched(), "search_errors": {"models": "TimeoutError: db"}, "models": []}
    state = {**state, **graph17.assess(state)}
    sent = {}

    def create(**kw):
        sent.update(kw)
        return iter([_chunk("데이터 설명\n"), _chunk(finish="stop")])

    answer = _explain_with(monkeypatch, state, create)
    assert answer.startswith("**일부 검색이 실패했어요.** 모델 검색 결과가")
    assert "데이터 설명" in answer and "search_errors" in sent["messages"][1]["content"]


def test_nothing_found_after_failures_skips_the_paid_writer(monkeypatch):
    state = {**_searched(), "models": [], "project_datasets": {},
             "search_errors": {"models": "TimeoutError", "project_datasets": "TimeoutError"}}
    state = {**state, **graph17.assess(state)}
    answer = _explain_with(monkeypatch, state, lambda **kw: pytest.fail("writer must not be called"))
    assert "모델 검색, 데이터셋 검색 결과가" in answer and answer.endswith(graph17.EXPLANATION_CAVEAT)


# Time limits (openai) and the GPU sentence.


def test_openai_writer_gets_a_read_timeout_and_ollama_keeps_its_own(monkeypatch):
    seen = []

    def create(**kw):
        seen.append(kw.get("timeout"))
        return iter([_chunk("ok\n"), _chunk(finish="stop")])

    monkeypatch.setenv("RECOMMEND_LLM_PROVIDER", "openai")
    _run_explain(monkeypatch, create)
    monkeypatch.setenv("RECOMMEND_LLM_PROVIDER", "ollama")
    _run_explain(monkeypatch, create)
    assert seen == [graph17.EXPLAIN_READ_TIMEOUT_S, None]


def _slow(first_line):
    def create(**kw):
        def stream():
            yield _chunk(first_line)
            import time
            time.sleep(0.05)
            yield _chunk("늦게 온 줄\n")
            yield _chunk(finish="stop")
        return stream()
    return create


def test_a_writer_past_the_deadline_stops_and_keeps_what_was_said(monkeypatch, tmp_path):
    monkeypatch.setenv("RECOMMEND_LLM_PROVIDER", "openai")
    monkeypatch.setattr(graph17, "EXPLAIN_DEADLINE_S", 0.01)
    answer = _run_explain(monkeypatch, _slow("첫 줄\n"))
    assert answer.startswith("첫 줄\n") and "늦게 온 줄" not in answer and "중간에 끊겼어요" in answer
    assert _log(tmp_path)[-1]["error"].startswith("TimeoutError")


def test_a_deadline_before_any_text_summarises_even_after_a_failure_notice(monkeypatch):
    monkeypatch.setenv("RECOMMEND_LLM_PROVIDER", "openai")
    monkeypatch.setattr(graph17, "EXPLAIN_DEADLINE_S", 0.01)
    state = {**_searched(), "search_errors": {"project_datasets": "TimeoutError"}}
    state = {**state, **graph17.assess(state)}
    answer = _explain_with(monkeypatch, state, _slow(""))  # no writer text: the notice must not count as text
    assert answer.startswith("**일부 검색이 실패했어요.**")
    assert "설명을 만들지 못해" in answer and "org/llm (apache-2.0)" in answer and "중간에 끊겼어요" not in answer


def test_the_prompt_has_no_gpu_example_to_copy():
    assert "8GB" not in graph17.EXPLAIN_PROMPT  # the writer copied this example when no GPU was given
    assert "only when gpu_fit is not\nnull" in graph17.EXPLAIN_PROMPT


# Output filters, replay, provider options.


def test_images_and_unknown_links_are_removed_but_retrieved_links_stay():
    evidence = {"models": [{"model_id": "org/llm", "url": "https://huggingface.co/org/llm"}],
                "datasets": {"per_model": {}, "project_training": [], "service_data": []}}
    record = {}
    lines = list(graph17.safe_lines([
        "![x](https://tracker.example/p.gif) 추천\n",
        "[모델](https://huggingface.co/org/llm) 와 [가짜](https://evil.example/a)\n",
        "원문: https://evil.example/b\n",
    ], evidence, record))
    assert lines == [" 추천\n", "[모델](https://huggingface.co/org/llm) 와 가짜\n", "원문: (링크 생략)\n"]


def test_a_made_up_id_under_a_retrieved_owner_drops_the_line_only():
    evidence = {"models": [{"model_id": "org/llm"}],
                "datasets": {"per_model": {}, "project_training": [{"dataset": "ok/eval"}],
                             "service_data": [{"dataset": "seoul_open_data/OA-13252"}]}}
    record = {}
    lines = list(graph17.safe_lines([
        "- org/llm 추천.\n",  # retrieved (trailing period is punctuation)
        "- org/llm-v9 도 좋아요\n",  # made up under a retrieved owner
        "- seoul_open_data/OA-99999 대여소\n",  # made up service data id
        "- TCP/IP, fp16/int8 은 그대로\n",  # unknown owners: not ids we can judge
        "- ok/eval가 평가용\n",  # a Korean particle right after the id
    ], evidence, record))
    assert lines == ["- org/llm 추천.\n", "- TCP/IP, fp16/int8 은 그대로\n", "- ok/eval가 평가용\n"]
    assert record["dropped_lines"] == 2


def _conversation_explain(monkeypatch, create, state=None):
    client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))
    monkeypatch.setattr(graph17, "_openai", lambda: client)
    graph = graph17.build_graph(nodes={"explain": graph17.explain})
    config = {"configurable": {"thread_id": "t", "trace_id": "abc"}}
    return "".join(d["token"] for mode, d in graph.stream(state or _assessed(), config, stream_mode=["custom"])
                   if mode == "custom")


def test_the_same_input_in_a_conversation_is_replayed_without_a_writer_call(monkeypatch, tmp_path):
    monkeypatch.setattr(graph17, "_answers", {})
    calls = []

    def create(**kw):
        calls.append(1)
        return iter([_chunk("추천: org/llm\n"), _chunk(finish="stop")])

    first = _conversation_explain(monkeypatch, create)
    second = _conversation_explain(monkeypatch, create)
    assert first == second and len(calls) == 1
    assert [r.get("writer") for r in _log(tmp_path) if r["event"] == "explain"] == [None, "cache"]


def test_a_cut_answer_is_not_replayed(monkeypatch):
    monkeypatch.setattr(graph17, "_answers", {})
    calls = []

    def create(**kw):
        calls.append(1)
        return iter([_chunk("추천: org/llm 은"), _chunk(finish="length")])

    _conversation_explain(monkeypatch, create)
    _conversation_explain(monkeypatch, create)
    assert len(calls) == 2


def test_stream_options_go_to_openai_only(monkeypatch):
    seen = []

    def create(**kw):
        seen.append("stream_options" in kw)
        return iter([_chunk("ok\n"), _chunk(finish="stop")])

    monkeypatch.setenv("RECOMMEND_LLM_PROVIDER", "openai")
    _run_explain(monkeypatch, create)
    monkeypatch.setenv("RECOMMEND_LLM_PROVIDER", "ollama")
    _run_explain(monkeypatch, create)
    assert seen == [True, False]


# Logs: what the fan-in saw, which prompt wrote the answer, one id per turn.


def test_assess_logs_lists_card_lookup_and_verdicts(monkeypatch, tmp_path):
    monkeypatch.setattr(graph17, "dataset_facts",
                        lambda names: {n: {"unavailable": "데이터 카드 조회 실패 (TimeoutError)"} for n in names})
    graph17.assess({**_searched(), "search_errors": {"models": "x"}})
    row = [r for r in _log(tmp_path) if r["event"] == "assess"][-1]
    assert row["found"] == {"models": 1, "project_training": 2, "service_data": 1}
    assert row["facts"]["lookup_failed"] == row["facts"]["found"] + row["facts"]["lookup_failed"] > 0
    assert row["license"]["use"] == "personal" and row["license"]["training_non_commercial"] == 1
    assert row["search_errors"] == ["models"] and row["elapsed_s"] >= 0


def test_explain_logs_prompt_model_size_and_dropped_ids(monkeypatch, tmp_path):
    _run_explain(monkeypatch, lambda **kw: iter([_chunk("- org/llm-v9 추천\n"), _chunk("- org/llm 추천\n"),
                                                  _chunk(finish="stop")]))
    row = _log(tmp_path)[-1]
    assert row["prompt"] == graph17.PROMPT_VERSION and len(row["prompt"]) == 8
    assert row["model"] == graph17.LLM_MODEL and row["payload_chars"] > 0
    assert row["dropped_ids"] == ["org/llm-v9"] and row["dropped_lines"] == 1


def test_assess_and_explain_share_one_id_per_turn_built_from_the_conversation(monkeypatch, tmp_path):
    monkeypatch.setattr(graph17, "_answers", {})
    client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(
        create=lambda **kw: iter([_chunk("ok\n"), _chunk(finish="stop")]))))
    monkeypatch.setattr(graph17, "_openai", lambda: client)
    graph = graph17.build_graph(nodes={"assess": graph17.assess, "explain": graph17.explain})
    config = {"configurable": {"thread_id": "1a2b3c4d-0000-group"}}
    turn = {**_searched(), "turns": [{"request": "earlier", "answer": "a"}]}
    answer = "".join(d["token"] for mode, d in graph.stream(turn, config, stream_mode=["custom"]) if mode == "custom")
    ids = {r["event"]: r["trace_id"] for r in _log(tmp_path)}
    assert ids == {"assess": "1a2b3c4d-2", "explain": "1a2b3c4d-2"}  # second turn of that group
    assert "추적 ID" not in answer  # a normal answer shows no id; cut/failed ones do


def test_sft_candidates_always_come_with_the_reason_in_the_guide():
    sft = {"need": {"task": "classification", "purpose_ko": "고유 카테고리로 분류하려면 SFT를 검토할 수 있어요.",
                    "model_query": "q"}, "models": [ALT], "kind": "sft"}
    guide = graph17.assess({**_searched(), "models": [*_searched()["models"], sft]})["assessment"]["implementation_guide"]
    assert guide["fine_tuning"].startswith("고유 카테고리로 분류하려면 SFT를 검토할 수 있어요.")
    assert "implementation_guide" not in graph17.assess(_searched())["assessment"]  # no SFT group, no guide
