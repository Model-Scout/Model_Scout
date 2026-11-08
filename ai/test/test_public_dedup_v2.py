"""공공데이터 중복 처리와 검색 문서 회귀 테스트. 외부 호출 없음.

    python -m pytest -q test/test_public_dedup_v2.py
"""

import importlib.util
import sys
from pathlib import Path

import pytest

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))

import dataset_dedup as dd  # noqa: E402

spec = importlib.util.spec_from_file_location("chunks14", AI / "14_build_dataset_chunks.py")
chunks14 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chunks14)


def seoul(item, title, fields=("주소", "이름"), license="공공누리 제1유형"):
    return {
        "dataset_id": f"seoul_open_data/{item}",
        "source": "seoul_open_data",
        "licenses": [license] if license else [],
        "readme_chars": 100,
        "description": f"같은 설명. 제공 필드: {', '.join(fields)}",
        "card_data": {"pretty_name": title},
        "_fields": frozenset(fields),
    }


def portal(item, title, org="경기도", description="같은 설명 " * 30, license="이용허락범위 제한 없음"):
    return {
        "dataset_id": f"data_go_kr/{item}",
        "source": "data_go_kr",
        "org": org,
        "licenses": [license] if license else [],
        "readme_chars": 100,
        "description": description,
        "card_data": {"pretty_name": title},
    }


@pytest.fixture(autouse=True)
def fields_from_rows(monkeypatch):
    monkeypatch.setattr(dd, "seoul_fields", lambda row: row.get("_fields", frozenset()))


@pytest.mark.parametrize(
    "a, b",
    [
        (seoul("1", "서울시 강서구 모범음식점 취소 현황"), seoul("2", "서울시 동대문구 모범음식점 취소 현황")),
        (seoul("1", "서울시 강서구 노동조합 현황"), portal("2", "노동조합 현황(2015)")),
        (seoul("1", "서울시 강북구 전통시장 현황"), seoul("2", "서울시 전통시장 현황")),
        (seoul("1", "자치구 단위 서울 생활인구(내국인)"), seoul("2", "집계구 단위 서울 생활인구(내국인)")),
        (seoul("1", "서울시 실시간 도시데이터"), seoul("2", "서울시 실시간 도시데이터(영문)")),
        (seoul("1", "서울시 한강공원 이용객 현황(2017년)"), seoul("2", "서울시 한강공원 이용객 현황 (2009~2013년)")),
        (seoul("1", "서울교통공사_지하철혼잡도정보"), portal("2", "서울교통공사_지하철혼잡도정보", org="서울교통공사")),
        (portal("1", "표준_20240101"), portal("2", "표준_20250101")),
    ],
)
def test_different_or_unproven_rows_stay_separate(a, b):
    assert dd.duplicate_map([], [a, b]) == {}


def test_period_end_year_keeps_rows_apart():
    a, b = seoul("1", "서울시 지도점검(2010년-2017년)"), seoul("2", "서울시 지도점검(2010년-2018년)")
    assert dd.duplicate_map([], [a, b]) == {}


def test_extended_edition_with_more_columns_stays_separate():
    plain = seoul("1", "서울시 전통시장 현황", fields=("주소",))
    plain["description"] = "서울시 전통시장 현황. 전통시장 정보 제공 필드: 주소"
    extended = seoul("2", "서울시 전통시장 현황", fields=("주소", "X좌표"))
    extended["description"] = "서울시 전통시장 현황. (AI친화) 제공 필드: 주소, X좌표"
    assert dd.duplicate_map([], [plain, extended]) == {}


def test_same_title_is_not_enough():
    different_fields = seoul("1", "서울시 전통시장 현황", fields=("주소",)), seoul("2", "서울시 전통시장 현황", fields=("연락처",))
    assert dd.duplicate_map([], list(different_fields)) == {}
    different_text = portal("1", "주차장 현황", description="가" * 120), portal("2", "주차장 현황", description="나" * 120)
    assert dd.duplicate_map([], list(different_text)) == {}
    other_publisher = portal("1", "주차장 현황", org="경기도"), portal("2", "주차장 현황", org="부산광역시")
    assert dd.duplicate_map([], list(other_publisher)) == {}
    other_license = seoul("1", "서울시 정보"), seoul("2", "서울시 정보", license="공공누리 제4유형")
    assert dd.duplicate_map([], list(other_license)) == {}
    short_text = portal("1", "주차장 현황", description="짧음"), portal("2", "주차장 현황", description="짧음")
    assert dd.duplicate_map([], list(short_text)) == {}


def license_chain():
    return [
        seoul("A", "서울시 정보", license="공공누리 제1유형"),
        seoul("B", "서울시 정보", license=None),
        seoul("C", "서울시 정보", license="공공누리 제4유형"),
    ]


def test_unknown_license_cannot_chain_commercial_and_non_commercial():
    rows = license_chain()
    assert dd.same_data_evidence(rows[0], rows[1]) is None
    assert dd.same_data_evidence(rows[1], rows[2]) is None
    assert dd.duplicate_map([], rows) == {}
    assert dd.duplicate_map([], [seoul("B", "서울시 정보", license=None), seoul("D", "서울시 정보", license=None)]) == {}


def test_all_three_stay_searchable_and_are_only_related():
    rows = license_chain()
    group = dd.public_series(rows, dd.duplicate_map([], rows))[0]
    assert set(group["members"]) == {r["dataset_id"] for r in rows}
    assert all(r["answer_substitutable"] is False for r in group["relations"])


@pytest.mark.parametrize(
    "chained",
    [
        {"seoul_open_data/A": "seoul_open_data/B", "seoul_open_data/C": "seoul_open_data/B"},
        {"seoul_open_data/B": "seoul_open_data/A", "seoul_open_data/C": "seoul_open_data/A"},
        {"seoul_open_data/C": "seoul_open_data/A"},
        {"seoul_open_data/B": "seoul_open_data/A"},
    ],
)
def test_build_gate_checks_the_whole_final_group(chained):
    bad = {member: {"canonical": canonical, "reason": "x"} for member, canonical in chained.items()}
    with pytest.raises(ValueError, match="license"):
        dd.check_public_duplicates(bad, license_chain())


def test_rows_with_full_evidence_merge():
    assert len(dd.duplicate_map([], [seoul("1", "서울시 전통시장 현황"), seoul("2", "서울시 전통시장 현황")])) == 1
    assert len(dd.duplicate_map([], [portal("1", "주차장 현황"), portal("2", "주차장 현황")])) == 1


def test_publisher_location_is_not_coverage():
    gyeonggi = dd.public_identity(portal("1", "관광지 현황", org="경기도"))
    assert gyeonggi["publisher_region"] == "경기"
    assert gyeonggi["coverage_status"] == "inferred_from_publisher"
    agency = dd.public_identity(portal("2", "수도권 교통 현황", org="인천국제공항공사"))
    assert agency["publisher_region"] == "인천" and agency["coverage_regions"] == []
    assert agency["coverage_status"] == "unknown"
    national_org = dd.public_identity(portal("3", "소상공인 서울 개업 현황", org="소상공인시장진흥공단"))
    assert national_org["publisher_region"] is None and national_org["coverage_regions"] == ["서울"]
    assert dd.public_identity(portal("4", "전국주차장정보표준데이터", org="공공데이터활용지원센터"))["coverage_regions"] == ["전국"]
    no_evidence = dd.public_identity(portal("5", "기상특보 조회서비스", org="기상청"))
    assert no_evidence["coverage_regions"] == [] and no_evidence["coverage_status"] == "unknown"


@pytest.mark.parametrize("title", ["소상공인시장진흥공단_전통시장 경기동향(BSI) 현황", "환경기초시설 정보제공서비스"])
def test_region_substrings_do_not_count(title):
    assert dd.public_identity(portal("1", title, org="기관"))["coverage_regions"] == []


def test_identity_parts():
    title = dd.public_identity(seoul("1", "서울특별시_실시간 인구데이터(영문)_20250814"))
    assert title["language_edition"] == "en" and title["revision"] == "20250814" and title["period"] == []
    assert dd.public_identity(seoul("2", "서울시 강서구 노동조합 현황"))["coverage_district"] == "강서구"
    assert dd.public_identity(seoul("3", "서울시 문화시설 현황 (중국어_간체_2015년)"))["language_edition"] == "zh"
    assert dd.public_identity(seoul("4", "서울시 한강공원 이용객 현황 (2009~2013년)"))["period"] == ["2009", "2013"]
    assert dd.public_identity(seoul("7", "서울시 환경 지도점검 현황(2010년-2017년)"))["period"] == ["2010", "2017"]
    assert dd.public_identity(seoul("5", "집계구 단위 서울 생활인구"))["spatial_unit"] == ["집계구"]
    busan = dd.public_identity(portal("6", "부산광역시_서구 어린이집 현황_20250826", org="부산광역시"))
    assert busan["coverage_regions"] == ["부산"] and busan["coverage_district"] == "서구"


def test_series_records_relations_but_never_substitutes_answers():
    rows = [
        seoul("1", "서울시 전통시장 현황"),
        seoul("2", "서울시 강북구 전통시장 현황"),
        seoul("3", "서울시 전통시장 현황 (영어)"),
        seoul("4", "서울시 전통시장 현황(2017년)"),
        portal("5", "전통시장 현황", org="경기도"),
    ]
    duplicates = dd.duplicate_map([], rows)
    assert duplicates == {}
    group = dd.public_series(rows, duplicates)[0]
    relations = {r["dataset_id"]: r for r in group["relations"]}
    assert all(r["verified"] is False and r["answer_substitutable"] is False for r in relations.values())
    assert set(group["members"]) == {r["dataset_id"] for r in rows}
    seen = {t for r in relations.values() for t in r["relation_to_anchor"]}
    assert {"language_variant", "edition_variant", "region_variant"} <= seen


def test_anchor_prefers_whole_korean_undated_row():
    rows = [seoul("1", "서울시 강북구 전통시장 현황"), seoul("2", "서울시 전통시장 현황")]
    group = dd.public_series(rows, {})[0]
    assert group["anchor"] == "seoul_open_data/2"
    assert group["relations"][0]["relation_to_anchor"] == ["subset_candidate"]


def test_build_gate_rejects_cross_scope_merge_and_high_rate():
    rows = [seoul("1", "서울시 강서구 정보"), seoul("2", "서울시 마포구 정보")]
    bad = {"seoul_open_data/1": {"canonical": "seoul_open_data/2", "reason": "x"}}
    with pytest.raises(ValueError, match="different scopes"):
        dd.check_public_duplicates(bad, rows)
    same = [seoul(str(i), "서울시 정보") for i in range(4)]
    many = {f"seoul_open_data/{i}": {"canonical": "seoul_open_data/3", "reason": "x"} for i in range(3)}
    with pytest.raises(ValueError, match="merge rate"):
        dd.check_public_duplicates(many, same)
    assert dd.check_public_duplicates({}, rows) == 0


def entity(**extra):
    return {"readme_status": "ok", "summary_ko": None, **extra}


def build(row, ent, tmp_path, readme):
    path = tmp_path / "readme.md"
    path.write_text(readme, encoding="utf-8")
    row["readme_path"] = str(path)
    return chunks14.build_chunks(row, ent, [], {})


def test_portal_card_keeps_publisher_coverage_category_keywords(tmp_path):
    row = {
        "dataset_id": "data_go_kr/1",
        "source": "data_go_kr",
        "description": "설명",
        "card_data": {"pretty_name": "관광지 현황"},
        "category": "문화관광",
        "tags": ["관광지", "여행"],
        "regional_variants": ["수원시_관광지", "성남시_관광지"],
        "regional_variant_count": 40,
    }
    ent = entity(
        publisher="경기도",
        publisher_region="경기",
        coverage_regions=["경기"],
        coverage_status="inferred_from_publisher",
    )
    built = build(row, ent, tmp_path, "# 관광지 현황\n\n설명\n")
    card = built[0]["text"]
    for needle in ("제공기관: 경기도", "제공기관 소재지: 경기", "제공기관 소재지로 추정", "분류: 문화관광", "키워드: 관광지, 여행"):
        assert needle in card
    variants = built[1]
    assert variants["kind"] == "section" and "수원시_관광지" in variants["text"] and "전체 40건" in variants["text"]


def test_unknown_coverage_is_not_national(tmp_path):
    row = {"dataset_id": "data_go_kr/2", "source": "data_go_kr", "description": "설명", "card_data": {"pretty_name": "기상특보"}}
    ent = entity(publisher="기상청", coverage_regions=[], coverage_status="unknown")
    card = build(row, ent, tmp_path, "# 기상특보\n")[0]["text"]
    assert "데이터 지역 범위: 미확인" in card and "전국" not in card


def test_seoul_all_fields_reach_search_documents(tmp_path):
    names = [f"필드{i}" for i in range(60)]
    row = {
        "dataset_id": "seoul_open_data/OA-1",
        "source": "seoul_open_data",
        "description": "제공 필드: " + ", ".join(names[:40]),
        "card_data": {"pretty_name": "서울시 정보"},
    }
    readme = "# 서울시 정보\n\n## 제공 필드\n\n" + "\n".join(f"- {n} (F{i})" for i, n in enumerate(names)) + "\n"
    built = build(row, entity(coverage_regions=["서울"], coverage_status="stated_in_title"), tmp_path, readme)
    text = "\n".join(chunk["text"] for chunk in built)
    assert all(name in text for name in names)
    assert built[1]["heading_path"] == ["제공 필드"]


def test_long_field_and_variant_names_are_never_cut(tmp_path):
    names = [f"아주긴필드이름입니다번호{i:03d}" for i in range(800)]
    row = {
        "dataset_id": "seoul_open_data/OA-9",
        "source": "seoul_open_data",
        "description": "제공 필드: " + ", ".join(names[:40]),
        "card_data": {"pretty_name": "서울시 정보"},
    }
    readme = "# 서울시 정보\n\n## 제공 필드\n\n" + "\n".join(f"- {n} (F{i})" for i, n in enumerate(names)) + "\n"
    built = build(row, entity(coverage_regions=["서울"], coverage_status="stated_in_title"), tmp_path, readme)
    extra = [chunk["text"] for chunk in built[1:]]
    assert len(extra) > 15 and all(any(n in text for text in extra) for n in names)
    assert len({chunk["chunk_id"] for chunk in built}) == len(built)
    portal_row = {
        "dataset_id": "data_go_kr/9",
        "source": "data_go_kr",
        "description": "설명",
        "card_data": {"pretty_name": "표준"},
        "regional_variants": [f"충청남도교육청_논산계룡교육지원청_평생교육시설정보{i}" for i in range(30)],
    }
    parts = build(portal_row, entity(coverage_regions=[], coverage_status="unknown"), tmp_path, "# 표준\n")[1:]
    assert all(any(v in part["text"] for part in parts) for v in portal_row["regional_variants"])


def test_seoul_without_missing_fields_stays_card_only(tmp_path):
    row = {
        "dataset_id": "seoul_open_data/OA-2",
        "source": "seoul_open_data",
        "description": "제공 필드: 주소, 이름",
        "card_data": {"pretty_name": "서울시 정보"},
    }
    readme = "# 서울시 정보\n\n## 제공 필드\n\n- 주소 (ADDR)\n- 이름 (NM)\n"
    built = build(row, entity(coverage_regions=["서울"], coverage_status="stated_in_title"), tmp_path, readme)
    assert [chunk["kind"] for chunk in built] == ["card"]


def test_long_description_overflows_to_a_chunk(tmp_path):
    row = {"dataset_id": "data_go_kr/3", "source": "data_go_kr", "description": "가" * 1500 + "끝말", "card_data": {"pretty_name": "긴 설명"}}
    built = build(row, entity(coverage_regions=[], coverage_status="unknown"), tmp_path, "# 긴 설명\n")
    assert "끝말" not in built[0]["text"] and "끝말" in built[-1]["text"]


def test_v1_policy_still_rebuilds_title_merges():
    rows = [seoul("1", "서울시 강서구 노동조합 현황"), portal("2", "노동조합 현황(2015)")]
    assert len(dd.duplicate_map([], rows, "title")) == 1


def test_v1_entity_keeps_v1_card_only_document(tmp_path):
    row = {
        "dataset_id": "data_go_kr/4",
        "source": "data_go_kr",
        "description": "설명",
        "card_data": {"pretty_name": "관광지 현황"},
        "category": "문화관광",
        "tags": ["관광지"],
        "regional_variants": ["수원시_관광지"],
    }
    built = build(row, entity(), tmp_path, "# 관광지 현황\n\n## 섹션\n\n" + "본문 " * 40)
    assert [chunk["kind"] for chunk in built] == ["card"]
    assert "제공기관" not in built[0]["text"] and "분류" not in built[0]["text"]
