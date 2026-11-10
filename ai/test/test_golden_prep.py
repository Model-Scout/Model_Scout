"""공공데이터 골든셋 보완 준비(golden_prep.py) 회귀 테스트. 외부·유료 호출 없음.

    python -m pytest -q test/test_golden_prep.py
"""

import importlib.util
import sys
from pathlib import Path

import pytest

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))

_spec = importlib.util.spec_from_file_location("golden_prep", AI / "test" / "public_data" / "corpus_v2" / "golden_prep.py")
gp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gp)


def query(qid="p001", text="주차장 위치를 찾아주는 앱", region=None, commercial=False, delivery="any", realtime=False,
          aspects=("주차장 위치",), behavior="recommend"):
    return {"query_id": qid, "query": text, "query_type": "service_idea", "aspects": list(aspects),
            "conditions": {"region": region, "delivery": delivery, "realtime": realtime, "commercial": commercial},
            "expected_behavior": behavior, "pool_terms": ["주차장"]}


def card(**over):
    f = {"title": "전국 주차장 정보", "source": "data_go_kr", "url": None, "publisher": "국토교통부", "publisher_region": None,
         "coverage_regions": ["전국"], "coverage_status": "stated_in_title", "coverage_district": None, "period": [],
         "language_edition": None, "spatial_unit": [], "series_id": None, "formats": ["api"],
         "licenses": ["공공누리 제1유형"], "commercial_use": "commercial", "license_text": "공공누리 1유형 : 출처표시",
         "official_status": "ok", "official_verification": "compat", "official_checked_at": None,
         "update_cycle_portal": "연간", "last_modified": None, "category": None, "keywords": [], "fields": [],
         "field_count": None, "regional_variants": [], "regional_variant_count": None, "description": "주차장 위치 제공"}
    f.update(over)
    return f


# ---------------------------------------------------------------- 2. 필수 조건 먼저, 미확인이면 2점 없음


def test_all_conditions_met_and_topic_found_can_be_two():
    assert gp.suggestion(query(), card())["proposal"] == "2 후보"


@pytest.mark.parametrize("over", [
    {"coverage_regions": [], "coverage_status": "unknown"},
    {"coverage_regions": ["경기"], "coverage_status": "inferred_from_publisher"},
    {"coverage_regions": ["서울"], "coverage_status": "stated_in_title", "coverage_district": "강서구"},
])
def test_unnamed_region_is_left_to_the_question_purpose(over):
    """지역 미지정을 전국 필수로 보지 않고, 지역 데이터를 일괄 1점으로 내리지도 않는다."""
    s = gp.suggestion(query(), card(**over))
    assert "region" not in s["checks"] and s["checks"]["region_scope"]["status"] == gp.PURPOSE
    assert s["proposal"] == "2 후보" and any("목적 판단" in b for b in s["basis"])


def test_inferred_region_match_is_unknown_not_met():
    s = gp.suggestion(query(region="경기"), card(coverage_regions=["경기"], coverage_status="inferred_from_publisher"))
    assert s["checks"]["region"]["status"] == gp.UNKNOWN and s["proposal"].startswith("보류")


def test_missing_information_is_a_hold_never_a_one():
    s = gp.suggestion(query(region="대구"), card(coverage_regions=[], coverage_status="unknown"))
    assert s["proposal"].startswith("보류") and "1" not in s["proposal"]


@pytest.mark.parametrize("delivery, formats, status", [
    ("api", ["api"], gp.MET), ("api", ["csv"], gp.UNMET), ("api", [], gp.UNKNOWN),
    ("file", ["csv", "api"], gp.MET), ("file", ["api"], gp.UNMET), ("file", [], gp.UNKNOWN),
])
def test_explicit_api_or_file_requirement_is_not_relaxed(delivery, formats, status):
    s = gp.suggestion(query(delivery=delivery), card(formats=formats))
    assert s["checks"]["delivery"]["status"] == status
    expected = {gp.MET: "2 후보", gp.UNMET: "0 후보 (wrong_delivery)", gp.UNKNOWN: "보류 (확인 필요: delivery)"}[status]
    assert s["proposal"] == expected


def test_partial_fit_needs_evidence_of_what_is_missing():
    q = query(aspects=("주차장 위치", "주차 요금"))
    no_fields = gp.suggestion(q, card(description="주차장 위치 제공", fields=[]))
    assert no_fields["proposal"].startswith("보류")  # 카드가 짧을 뿐, 요금이 없다는 근거가 아님
    with_fields = gp.suggestion(q, card(description="주차장 위치 제공", fields=["주차장명 (NM)", "위도 (LAT)"]))
    assert with_fields["proposal"] == "1 후보 (부분 적합)"


@pytest.mark.parametrize("use, status", [(None, gp.UNKNOWN), ("conditional", gp.UNKNOWN), ("non_commercial", gp.UNMET)])
def test_commercial_condition(use, status):
    s = gp.suggestion(query(commercial=True), card(commercial_use=use))
    assert s["checks"]["commercial"]["status"] == status
    assert not s["proposal"].startswith("2")
    if status == gp.UNMET:
        assert s["proposal"] == "0 후보 (license)"


def test_unmet_condition_comes_before_topic():
    s = gp.suggestion(query(region="대구"), card(coverage_regions=["서울"], description="무관"))
    assert s["proposal"] == "0 후보 (wrong_region)"


# ---------------------------------------------------------------- 3. p026 공공누리 1유형 한정


P026 = "상업 서비스에 쓸 거라 출처 표시만 하면 되는 공공누리 1유형 데이터만 원해. 전국 공중화장실 위치 데이터 있어?"


@pytest.mark.parametrize("text, status", [
    ("공공누리 1유형 : 출처표시 (상업적 이용 및 변경 가능)", gp.MET),
    ("공공저작물 : 출처표시 (제 1유형)", gp.MET),
    ("공공저작물 : 출처표시, 변경금지 (제 3유형)", gp.UNMET),  # 상업 이용은 되지만 1유형이 아님
    ("이용허락범위 제한 없음", gp.UNMET),  # 1유형 한정 조건 유지 (2026-11-09)
    ("제3자 권리 포함 : 저작권 표시, 공공저작물 : 출처표시 (제 1유형)", gp.UNMET),
    (None, gp.UNKNOWN),
])
def test_p026_type1_only_is_checked_as_written(text, status):
    s = gp.suggestion(query("p026", P026, commercial=True, aspects=("공중화장실 위치",)),
                      card(license_text=text, description="공중화장실 위치"))
    assert s["checks"]["kogl_type1_only"]["status"] == status
    if status == gp.UNMET:
        assert s["proposal"] == "0 후보 (license)"
    if status == gp.UNKNOWN:
        assert s["proposal"].startswith("보류")


def test_type1_check_only_for_queries_that_ask_for_it():
    assert "kogl_type1_only" not in gp.suggestion(query(commercial=True), card())["checks"]


# ---------------------------------------------------------------- 4. 목표 ID도 같은 기준, 표시 없음은 미확인


@pytest.mark.parametrize("ext, over", [
    ({"language": "en"}, {"language_edition": None}),
    ({"district": "도봉구"}, {"coverage_district": None}),
    ({"period": "2007"}, {"period": []}),
    ({"spatial_unit": "집계구"}, {"spatial_unit": []}),
])
def test_missing_edition_mark_is_unknown_not_a_default(ext, over):
    s = gp.suggestion(query(region="서울"), card(coverage_regions=["서울"], **over), ext)
    key = next(iter(ext))
    assert s["checks"][key]["status"] == gp.UNKNOWN and not s["proposal"].startswith("2")


def test_language_and_district_marks_are_compared():
    s = gp.suggestion(query(region="서울"), card(coverage_regions=["서울"], language_edition="zh"), {"language": "en"})
    assert s["checks"]["language"]["status"] == gp.UNMET and s["proposal"].startswith("0 후보 (wrong_language")
    s = gp.suggestion(query(region="서울"), card(coverage_regions=["서울"], coverage_district="강서구"), {"district": "도봉구"})
    assert s["proposal"] == "0 후보 (wrong_region)"


def test_designer_target_gets_no_special_proposal():
    q = gp.proposed_query(gp.PROPOSALS[0])  # d1 도봉구
    target = card(title="서울시 도봉구 모범음식점 지정 현황", coverage_regions=["서울"], coverage_district="도봉구",
                  description="모범음식점")
    unknown_district = {**target, "coverage_district": None}
    s_target = gp.suggestion(q, target, q["conditions_extension"])
    assert s_target == gp.suggestion({**q, "designer_targets": []}, target, q["conditions_extension"])
    assert not gp.suggestion(q, unknown_district, q["conditions_extension"])["proposal"].startswith("2")


# ---------------------------------------------------------------- 5. 전체 근거 보존, 갱신 주기만으로 0점 없음


def test_facts_keep_the_full_description_and_every_field():
    readme = "# t\n\n## 제공 필드\n\n" + "\n".join(f"- 필드{i} (F{i}): 설명 {i}" for i in range(500))
    row = {"source": "seoul_open_data", "description": "가" * 5000, "card_data": {"pretty_name": "t"}}
    f = gp.facts({}, row, readme)
    assert len(f["description"]) == 5000 and len(f["fields"]) == 500 and f["fields"][7] == "필드7 (F7): 설명 7"


@pytest.mark.parametrize("cycle", ["연간", None, "실시간"])
def test_portal_cycle_alone_never_decides_realtime(cycle):
    s = gp.suggestion(query(realtime=True), card(update_cycle_portal=cycle))
    assert s["checks"]["realtime"]["status"] == gp.UNKNOWN
    assert s["proposal"].startswith("보류")


def test_realtime_hint_fields_are_listed_as_evidence():
    s = gp.suggestion(query(realtime=True), card(fields=["측정일시 (MSRDT): 측정 시각", "주차면수 (CAP)"]))
    assert "측정일시" in s["checks"]["realtime"]["basis"]


# ---------------------------------------------------------------- 6. 비공공·보류 분리, 검색 조건 명시


def label(**over):
    base = {"query_id": "p001", "relevant": {"data_go_kr/1": 2}, "must_exclude": ["data_go_kr/2"],
            "judged_irrelevant": ["data_go_kr/3"], "unjudged": ["data_go_kr/4"],
            "conditions": {"region": "대구", "delivery": "api", "realtime": True, "commercial": True},
            "dataset_terms": ["주차장"]}
    base.update(over)
    return base


@pytest.mark.parametrize("dataset_id, state", [
    ("data_go_kr/1", "정답 2점"), ("data_go_kr/2", "제외 0점"), ("data_go_kr/3", "오답 0점"),
    ("data_go_kr/4", "보류"), ("data_go_kr/9", "미판정"), ("org/hf-set", "비공공데이터"),
])
def test_label_state_keeps_hold_and_non_public_apart(dataset_id, state):
    assert gp.label_state(label(), dataset_id, {}) == state


def test_split_v1_copy_is_still_unjudged():
    assert gp.label_state(label(), "data_go_kr/9", {"data_go_kr/9": "data_go_kr/1"}) == "미판정 (v1 판정 데이터의 분리 사본)"


@pytest.mark.parametrize("mode", gp.MODES)
def test_search_records_the_filters_it_passed(monkeypatch, mode):
    calls = []
    monkeypatch.setattr(gp.hs, "rank_datasets", lambda concepts, **kw: calls.append((concepts, kw)) or [])
    monkeypatch.setattr(gp.hs, "concepts_from_terms", lambda terms: {f"t/{t}" for t in terms})
    _, settings = gp.search(label(), [0.1], mode)
    concepts, kw = calls[0]
    assert kw["commercial_only"] is True and settings["commercial_only"] is True and kw["roles"] == ["service"]
    assert settings["not_passed"] == ["delivery", "realtime"]
    if mode == "question_only":
        assert concepts == [] and "keywords" not in kw and settings["keywords"] == []
    else:
        assert kw["keywords"] == ["주차장", "대구"] == settings["keywords"]


# ---------------------------------------------------------------- 1·7. 검토 목록 구성과 자료 분리


def review(top, high_rows=()):
    queries = {"p001": query()}
    labels = {"p001": label(conditions=query()["conditions"])}
    decisions = {("p001", "data_go_kr/4"): {"score": "?", "reason": "", "note": "원문 확인", "judge": "codex", "judged_on": "d"}}
    return gp.build_review(queries, labels, decisions, top, list(high_rows), {}, {}, lambda did: card())


def hit(did, mode="question_only", rank=1, state="미판정"):
    return {"query_id": "p001", "mode": mode, "rank": rank, "dataset_id": did, "label_state": state}


def test_hold_rows_are_listed_even_when_the_search_missed_them():
    items, context, _ = review([hit("data_go_kr/9")])
    by_id = {c["review_id"]: c for c in context}
    assert set(by_id) == {"p001|data_go_kr/4", "p001|data_go_kr/9"}
    assert by_id["p001|data_go_kr/4"]["review_sources"] == ["existing_hold"]
    assert by_id["p001|data_go_kr/4"]["discovery"] is None
    assert by_id["p001|data_go_kr/4"]["existing_judgment"]["note"] == "원문 확인"


def test_sources_merge_when_one_row_is_on_several_lists():
    high = {"query_id": "p001", "dataset_id": "data_go_kr/4", "review_reasons": ["v1_copies_now_separate"],
            "v1_copies_now_separate": ["data_go_kr/9"]}
    _, context, suggestions = review([hit("data_go_kr/4", state="보류"), hit("data_go_kr/9", rank=2)], [high])
    row = next(c for c in context if c["review_id"] == "p001|data_go_kr/4")
    assert row["review_sources"] == ["existing_hold", "high_review"] and row["discovery"] == {"question_only": 1}
    assert row["high_review"]["v1_copies_in_prelim_top10"] == ["data_go_kr/9"]
    assert next(s for s in suggestions if s["review_id"] == "p001|data_go_kr/4")["high_review_note"]


def test_judging_file_holds_no_rank_mode_or_proposal():
    items, context, suggestions = review([hit("data_go_kr/9", mode="pool_terms", rank=3)])
    assert [i["review_id"] for i in items] == [c["review_id"] for c in context] == [s["review_id"] for s in suggestions]
    for item in items:
        flat = str(item)
        for leaked in ("rank", "mode", "proposal", "checks", "review_sources", "existing_judgment", "discovery"):
            assert f"'{leaked}'" not in flat
        assert item["judgment"] == {"score": None, "reason": None, "note": None}
    assert next(c for c in context if c["review_id"] == "p001|data_go_kr/9")["discovery"] == {"pool_terms": 3}
    assert all("proposal" in s for s in suggestions)


def test_judged_results_are_not_put_back_on_the_list():
    items, _, _ = review([hit("data_go_kr/1", state="정답 2점"), hit("data_go_kr/3", state="오답 0점")])
    assert {i["dataset_id"] for i in items} == {"data_go_kr/4"}


def test_missing_query_vectors_stop_instead_of_calling_the_api(tmp_path, monkeypatch):
    monkeypatch.setattr(gp, "VECTOR_CACHE", tmp_path / "none.jsonl")
    monkeypatch.setattr(gp.hs, "query_model", lambda: "m")
    monkeypatch.setattr(gp.hs, "_embed_query", lambda *a: pytest.fail("API 호출"))
    with pytest.raises(SystemExit, match="p001"):
        gp.query_vectors([query()], allow_embed=False)
