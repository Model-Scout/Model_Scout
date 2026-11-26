import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import dataset_rerank as dr  # noqa: E402


def rows(n):
    return [{"dataset": f"d{i}", "title": f"t{i}", "source": "data_go_kr"} for i in range(1, n + 1)]


def client(reply=None, error=None, seen=None):
    def create(**kwargs):
        if seen is not None:
            seen.update(kwargs)
        if error:
            raise error
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])

    chat = SimpleNamespace(completions=SimpleNamespace(create=create))
    return lambda: SimpleNamespace(with_options=lambda **kw: SimpleNamespace(chat=chat))


def facts(names):
    return {n: {"coverage": "서울 (제목에 명시)"} for n in names}


def ids(out):
    return [r["dataset"] for r in out]


def test_reorders_the_top_and_keeps_the_rest():
    out = dr.rerank("q", rows(22), client(json.dumps({"order": [3, 1]})), "m", facts)
    assert ids(out)[:3] == ["d3", "d1", "d2"]  # unranked candidates keep their order behind the picks
    assert ids(out)[20:] == ["d21", "d22"] and len(out) == 22


@pytest.mark.parametrize("reply, error", [("not json", None), ('{"order": "x"}', None), ('{"order": [0, 99]}', None),
                                          (None, TimeoutError())])
def test_any_failure_keeps_the_search_order(reply, error):
    assert ids(dr.rerank("q", rows(5), client(reply, error), "m", facts)) == ids(rows(5))


def test_card_lookup_failure_keeps_the_search_order():
    def broken(names):
        raise OSError

    assert ids(dr.rerank("q", rows(5), client('{"order": [2, 1]}'), "m", broken)) == ids(rows(5))


def test_off_or_unmeasured_provider_makes_no_call(monkeypatch):
    monkeypatch.setenv("DATASET_RERANK", "off")
    assert dr.model("openai") is None
    monkeypatch.delenv("DATASET_RERANK")
    assert dr.model("openai") == dr.MEASURED_MODEL and dr.model("ollama") is None
    assert ids(dr.rerank("q", rows(5), client(error=AssertionError()), None, facts)) == ids(rows(5))


def test_the_call_is_bounded_and_shows_the_question_and_card_facts():
    seen = {}
    dr.rerank("서울 주차장", rows(3), client('{"order": [1]}', seen=seen), "m", facts)
    user = seen["messages"][1]["content"]
    assert seen["timeout"] <= 15 and seen["temperature"] == 0
    assert "서울 주차장" in user and "[3] t3" in user and "지역: 서울" in user


def test_service_list_is_searched_deeper_reordered_and_cut(monkeypatch):
    spec = importlib.util.spec_from_file_location("graph17_rerank", ROOT / "17_recommend_graph.py")
    g = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = g
    spec.loader.exec_module(g)
    monkeypatch.delenv("DATASET_RERANK")
    limits = []

    def rank(concepts, **kw):
        limits.append(kw["limit"])
        return [dict(r, score=1.0, reasons=[], downloads=None, url="", summary_ko="", licenses=[], evidence=[])
                for r in rows(kw["limit"])]

    monkeypatch.setattr(g, "rank_datasets", rank)
    monkeypatch.setattr(g, "embed_query", lambda text: [0.0])
    monkeypatch.setattr(g, "dataset_facts", facts)
    monkeypatch.setattr(g, "llm_provider", lambda: "openai")
    monkeypatch.setattr(g, "_openai", client(json.dumps({"order": [20, 19]})))
    plan = {"constraints": {}, "needs": [], "dataset_terms": ["주차장"], "dataset_query": "주차장"}
    state = {"request": "주차장 데이터", "plan": plan, "route": {"target": "dataset", "data_kind": "service"}}
    out = g._rank_lists(state, ["주차장"], g.PROJECT_PROFILE)
    assert limits == [dr.RERANK_DEPTH]
    assert [d["dataset"] for d in out["service_data"]] == ["d20", "d19", "d1", "d2", "d3", "d4"]
