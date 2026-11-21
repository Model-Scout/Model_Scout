"""condition_checks.judge on hand-made cards (no corpus, no LLM)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import condition_checks as cc  # noqa: E402
import data_conditions as dc  # noqa: E402

CHEONGJU_CSV = {**dc.defaults(), "region": "충북", "region_detail": "청주", "delivery": "file", "formats": ["CSV"]}


def entity(title, regions, status="stated_in_title", source="data_go_kr", **more):
    return {"title": title, "coverage_regions": regions, "coverage_status": status, "source": source, **more}


def verdicts(conditions, ent, facts, commercial=False):
    out = cc.judge(conditions, commercial, ent, facts)
    return {c["key"]: c["status"] for c in out["checks"]}, out


def test_the_four_cheongju_cases():
    csv = {"formats": "API (api), CSV (csv)"}
    got, _ = verdicts(CHEONGJU_CSV, entity("충청북도 청주시 공중화장실 현황", ["충북"]), csv)
    assert got == {"region": "충족", "region_detail": "충족", "delivery": "충족", "format": "충족"}
    got, out = verdicts(CHEONGJU_CSV, entity("충청북도 공중화장실 현황", ["충북"]), csv)
    assert got["region"] == "충족" and got["region_detail"] == "미확인"  # 충북 data: 청주 not established
    assert "청주 포함 여부" in next(c["scope"] for c in out["checks"] if c["key"] == "region_detail")
    got, _ = verdicts(CHEONGJU_CSV, entity("충청북도 청주시 공중화장실 정보", ["충북"]), {"formats": "API (api)"})
    assert got["delivery"] == "미확인" and got["format"] == "미확인"  # API only listed is not "no file"
    got, _ = verdicts(CHEONGJU_CSV, entity("충청북도 제천시 공중화장실 현황", ["충북"]), csv)
    assert got["region_detail"] == "불충족"
    _, out = verdicts(CHEONGJU_CSV, entity("대구광역시_시내버스 정류소 위치정보", ["대구"]), csv)
    assert next(c["basis"] for c in out["checks"] if c["key"] == "region_detail") == "제목에 대구"  # not "광역시"


def test_nationwide_request_with_regional_data_is_a_partial_alternative_not_a_pass():
    want = {**dc.defaults(), "region_scope": "전국"}
    got, out = verdicts(want, entity("서울특별시 전통시장 현황", ["서울"]), {})
    assert got["region_scope"] == "불충족" and out["partial_alternative"].startswith("서울 한정")
    got, out = verdicts(want, entity("전국전통시장표준데이터", ["전국"]), {})
    assert got["region_scope"] == "충족" and out["partial_alternative"] is None
    got, _ = verdicts({**dc.defaults(), "region": "충북"}, entity("전국공중화장실표준데이터", ["전국"]), {})
    assert got["region"] == "미확인"  # nationwide data may hold 충북, the card does not say


def test_facts_that_never_settle_a_condition():
    api = {**dc.defaults(), "delivery": "api"}
    got, out = verdicts(api, entity("x", ["전국"]), {"formats": "API (api), CSV (csv)",
                                                     "api_status": "파일 자동변환 OpenAPI (상세 페이지에 주소 있음)"})
    assert got["delivery"] == "충족" and "실제 호출은 확인하지 않음" in out["checks"][0]["scope"]
    assert verdicts(api, entity("x", ["전국"]), {"formats": "API (api)", "api_status": "미확인"})[0]["delivery"] == "미확인"
    # a file-only listing is not "no API" either: no card states an absence
    assert verdicts(api, entity("x", ["전국"]), {"formats": "CSV (csv), XLSX(엑셀) (xlsx)"})[0]["delivery"] == "미확인"
    now = {**dc.defaults(), "current_value": True, "update_interval": "1시간"}
    got, out = verdicts(now, entity("x", ["서울"]), {"update_cycle_portal": "실시간"})
    assert got == {"current_value": "미확인", "update_interval": "미확인"}  # the portal's 실시간 label proves nothing
    assert verdicts({**dc.defaults(), "delivery": "file"}, entity("x", []), {})[0]["delivery"] == "미확인"


def test_licenses_and_scope_of_judging():
    type1 = {**dc.defaults(), "kogl_type1_only": True}
    assert verdicts(type1, entity("x", [], licenses=["공공누리 제1유형"]), {})[0]["kogl_type1_only"] == "충족"
    assert verdicts(type1, entity("x", [], licenses=["공공누리 제1유형(제3자 권리 포함)"]), {})[0]["kogl_type1_only"] == "불충족"
    assert verdicts(type1, entity("x", [], licenses=["이용허락범위 제한 없음"]), {})[0]["kogl_type1_only"] == "불충족"
    assert verdicts(type1, entity("x", []), {})[0]["kogl_type1_only"] == "미확인"
    got, _ = verdicts(dc.defaults(), entity("x", []), {"commercial_use": "비상업 전용 (non commercial)"}, commercial=True)
    assert got == {"commercial": "불충족"}
    assert cc.judge(CHEONGJU_CSV, False, entity("x", [], source="huggingface"), {}) == {"checks": [], "partial_alternative": None}
    assert verdicts(dc.defaults(), entity("x", ["서울"]), {})[0] == {}  # no stated condition, no verdict
    assert cc.unread("timeout")["checks"][0]["status"] == "미확인"


def test_reader_guards_for_known_misreads():
    # p043: a file the user feeds in is not how data is delivered; p024: calling an API "실시간" is not current values
    said = "아파트 층간소음 녹음 파일로 소음 분류 모델을 학습시키고 싶어"
    assert dc.check({**dc.defaults(), "delivery": "file", "delivery_evidence": "녹음 파일로"}, said)["delivery"] is None
    said = "제주도 관광지 정보를 API로 실시간 호출할 수 있는 데이터"
    out = dc.check({**dc.defaults(), "current_value": True, "freshness_evidence": "실시간 호출할 수 있는"}, said)
    assert out["current_value"] is False
    assert dc.check({**dc.defaults(), "current_value": True, "freshness_evidence": "실시간 위치"}, "버스 실시간 위치")["current_value"]
