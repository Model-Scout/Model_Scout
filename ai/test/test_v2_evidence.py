"""What a v2 card states reaches the answer: exact formats, official description and its limits.
Unknown stays unknown; ranking is not touched."""

import importlib.util
import sys
from pathlib import Path

import pytest

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))
import hypergraph_search as hs  # noqa: E402

spec = importlib.util.spec_from_file_location("rg17_evidence", AI / "17_recommend_graph.py")
rg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rg)

CARD = "\n".join([
    "Dataset 데이터셋: seoul_open_data/OA-16161 (서울시 용산구 병원 인허가 정보)",
    "데이터 형식: API (api), CSV (csv)",
    "상업 이용: 상업 이용 가능 (commercial)",
    "데이터 지역 범위: 서울 용산구 (제목에 명시)",
    "갱신 주기(포털 표기): 매일",
    "Description: 용산구 병원 정보 * 좌표안내 : 중부원점TM(EPSG:5174) 좌표계이며 위경도 좌표는 제공하고 있지 않음 "
    "* 본 데이터는 3일전 자료를 제공합니다. 서울시 용산구 병원 인허가 정보. 제공 필드: 사업장명, 좌표정보(X), 좌표정보(Y)",
])


@pytest.fixture
def v2(monkeypatch):
    monkeypatch.setattr(hs, "CORPUS", "v2")
    monkeypatch.setattr(hs, "_card_texts", lambda names: {"seoul_open_data/OA-16161": CARD})


def test_card_facts_keep_exact_formats_and_quote_the_limits(v2):
    facts = hs.dataset_facts(["seoul_open_data/OA-16161"])["seoul_open_data/OA-16161"]
    assert facts["formats"] == "API (api), CSV (csv)" and facts["update_cycle_portal"] == "매일"
    assert facts["limits"] == ["좌표안내 : 중부원점TM(EPSG:5174) 좌표계이며 위경도 좌표는 제공하고 있지 않음",
                               "본 데이터는 3일전 자료를 제공합니다"]  # the field list naming 좌표정보(X) is not a limit
    assert "publisher" not in facts  # not on the card: absent, not invented


def test_v1_has_no_card_facts(monkeypatch):
    monkeypatch.setattr(hs, "CORPUS", "v1")
    assert hs.dataset_facts(["a/b"]) == {}


def test_a_failed_card_lookup_is_reported_not_raised(monkeypatch):
    monkeypatch.setattr(hs, "CORPUS", "v2")

    def down(names):
        raise OSError("db down")

    monkeypatch.setattr(hs, "_card_texts", down)
    assert hs.dataset_facts(["a/b"]) == {"a/b": {"unavailable": "데이터 카드 조회 실패 (OSError)"}}


def test_the_answer_ends_with_the_limits_of_the_datasets_it_names():
    limits = ["본 데이터는 3일전 자료를 제공합니다"]
    datasets = {"per_model": {}, "project_training": [],
                "service_data": [{"dataset": "seoul_open_data/OA-16161", "facts": {"limits": limits}},
                                 {"dataset": "seoul_open_data/OA-99999", "facts": {"limits": ["다른 자료"]}}]}
    note = rg.data_limits_note("OA-16161 추천: seoul_open_data/OA-16161", datasets)
    assert "seoul_open_data/OA-16161: 본 데이터는 3일전 자료를 제공합니다" in note and "OA-99999" not in note
    assert rg.data_limits_note("아무 데이터도 없음", datasets) == ""


def test_the_explainer_is_told_unknown_is_not_absent():
    assert "never that the data lacks it" in rg.EXPLAIN_PROMPT


def test_the_api_status_reaches_the_answer_as_stated_on_the_card(monkeypatch):
    monkeypatch.setattr(hs, "CORPUS", "v2")
    cards = {"data_go_kr/1": "데이터 형식: CSV (csv)\nAPI 제공 여부: 미확인",
             "data_go_kr/2": "데이터 형식: API (api), CSV (csv)\nAPI 제공 여부: 파일 자동변환 OpenAPI (상세 페이지에 주소 있음)"}
    monkeypatch.setattr(hs, "_card_texts", lambda names: cards)
    facts = hs.dataset_facts(["data_go_kr/1", "data_go_kr/2"])
    assert facts["data_go_kr/1"]["api_status"] == "미확인" and facts["data_go_kr/2"]["api_status"].startswith("파일 자동변환")
    datasets = {"per_model": {}, "project_training": [],
                "service_data": [{"dataset": d, "facts": f} for d, f in facts.items()]}
    note = rg.data_limits_note("data_go_kr/1 과 data_go_kr/2 추천", datasets)
    assert "data_go_kr/1: API 제공 여부: 미확인" in note and "data_go_kr/2: API 제공 여부: 파일 자동변환" in note
    assert "never \"no API\"" in rg.EXPLAIN_PROMPT and "no evidence of real-time" in rg.EXPLAIN_PROMPT


def test_limits_keep_whole_sentences_and_conflicts_reach_the_answer(monkeypatch):
    monkeypatch.setattr(hs, "CORPUS", "v2")
    long_limit = ("의료법 제35조에 따라 개설된 부속 의료기관은 직원 등 외의 자, 즉 " + "가" * 150
                  + " 대상 외의 자를 대상으로 의료행위를 하여서는 안될 것임")
    cards = {"seoul_open_data/OA-16254": f"Description: 병원 정보 ※ {long_limit}",
             "seoul_open_data/OA-15531": "Description: 중심지\n설명 간 불일치(확인 필요): 좌표계: 공식 설명은 Bessel, 수집 제목·설명은 GRS80"}
    monkeypatch.setattr(hs, "_card_texts", lambda names: cards)
    monkeypatch.setattr(hs, "LIMIT_RE", __import__("re").compile(r"하여서는 안"))
    facts = hs.dataset_facts(list(cards))
    assert facts["seoul_open_data/OA-16254"]["limits"] == [long_limit]  # 부정 조건절까지 그대로
    assert facts["seoul_open_data/OA-15531"]["conflicts"].startswith("좌표계: 공식 설명은 Bessel")
    datasets = {"per_model": {}, "project_training": [], "service_data": [{"dataset": d, "facts": f} for d, f in facts.items()]}
    note = rg.data_limits_note("seoul_open_data/OA-16254, seoul_open_data/OA-15531", datasets)
    assert "안될 것임" in note and "설명 간 불일치(확인 필요): 좌표계" in note
    assert "never present one of them as the fact" in rg.EXPLAIN_PROMPT
