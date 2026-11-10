"""공공데이터 보완(PR-D)과 v2 공공데이터 파이프라인 회귀 테스트. 외부 호출 없음.

    python -m pytest -q test/test_public_enrich.py
"""

import importlib.util
import json
import sys
from pathlib import Path

import pytest

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))

import corpus_manifest as cm  # noqa: E402
import public_v2_pipeline as pipeline  # noqa: E402
from taxonomy import normalize  # noqa: E402


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, AI / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


enrich = load("enrich18", "18_enrich_public_datasets.py")
graph13 = load("graph13", "13_build_hypergraph.py")
chunks14 = load("chunks14_enrich", "14_build_dataset_chunks.py")

@pytest.fixture(autouse=True)
def isolated_cache(tmp_path, monkeypatch):
    """No test may write the real cache or stored pages."""
    monkeypatch.setattr(enrich, "RAW_DIR", tmp_path / "raw")
    monkeypatch.setattr(enrich, "CACHE", tmp_path / "cache.jsonl")
    monkeypatch.setattr(enrich.collect18, "CATALOG_DIR", tmp_path / "catalog")


# 서울 열린데이터광장 상세 페이지의 실제 구조를 줄인 것
SEOUL_PAGE = """<html><body>
<button onclick="dataSetView('OA-1','S', 1)"><i>Sheet</i></button>
<button onclick="dataSetView('OA-1','A', 1)"><i>Open API</i></button>
<th>데이터 갱신일</th><td>2026.11.08.</td><th>갱신주기</th><td>비정기(수시, 자료변경시)</td><th>분류</th><td>보건</td>
<th>제3저작권자</th><td>없음 --> 없음</td><th>원본형태</th><td>DB</td>
<th>이용허락범위</th><td><!-- x --> 공공누리 1유형 : 출처표시 (상업적 이용 및 변경 가능)</td><th>AI유형</th>
<span title="a.xlsx" onclick="javascript:downloadFile('1');">강서구_모범음식점.xlsx</span>
<span title="b.hwp" onclick="javascript:downloadFile('2');">안내.hwp</span>
<script>function sheetDown() { /* 파일 다운로드 */ }</script>
</body></html>"""


def catalog(**extra):
    return json.dumps({"@type": "Dataset", "name": "이름", "license": {"name": "이용허락범위 제한 없음"}, **extra}, ensure_ascii=False)


def row(dataset_id="seoul_open_data/OA-1", url=None, **extra):
    source = dataset_id.split("/")[0]
    url = url or ("https://data.seoul.go.kr/dataList/OA-1/A/1/datasetView.do" if source == "seoul_open_data" else None)
    return {"dataset_id": dataset_id, "source": source, "url": url, "formats": ["api"], "licenses": [], "sha": "s1", **extra}


def gokr(kind, item="15000001", **extra):
    return row(f"data_go_kr/{item}", url=f"https://www.data.go.kr/data/{item}/{kind}.do", **extra)


# ---------------------------------------------------------------- 공식 페이지 해석


def test_seoul_page_gives_license_tabs_files_and_cycle():
    meta = enrich.parse_seoul(SEOUL_PAGE)
    assert meta["status"] == "ok"
    assert enrich.official_license(meta["license_text"]) == "공공누리 제1유형"
    assert meta["tabs"] == ["A", "S"] and meta["files"] == ["강서구_모범음식점.xlsx", "안내.hwp"]
    assert meta["cycle"] == "비정기(수시, 자료변경시)"


SEOUL_BUSY = "<html><p>서울 열린데이터광장 서비스 이용에 불편을 드려 죄송합니다. 서비스 지연이 발생하고 있습니다. 다시 시도하여 주십시오.(103)</p></html>"


class FakeSession:
    def __init__(self, body=None, error=None):
        self.body, self.error = body, error

    def get(self, url, **kwargs):
        if self.error:
            raise self.error
        return type("R", (), {"status_code": 200, "text": self.body, "raise_for_status": lambda self: None})()


def test_seoul_busy_page_is_a_failed_lookup_not_a_deletion():
    # 실제로 "missing"으로 캐시됐던 서울 페이지는 이 지연 안내였다
    assert enrich.lookup(FakeSession(SEOUL_BUSY), row()) == {"status": "failed"}


@pytest.mark.parametrize("source_row, body, error, status", [
    (row(), "<html>모르는 모양</html>", None, "parse_error"),
    (gokr("openapi"), "<html>not json</html>", None, "parse_error"),
    (gokr("openapi"), '{"@type": "Dataset"}', None, "parse_error"),  # 이름도 삭제 안내도 없음
    (gokr("openapi"), '["x"]', None, "parse_error"),
    (gokr("openapi"), None, __import__("requests").ConnectionError("down"), "failed"),
    (row("data_go_kr/x", url="https://example.org/elsewhere"), None, None, "no_page"),
    (gokr("standard"), '{"@type": "Dataset", "description": "해당 데이터는 존재하지 않습니다."}', None, "deleted"),
])
def test_lookup_separates_deletion_from_fetch_and_parse_problems(monkeypatch, source_row, body, error, status):
    monkeypatch.setattr(enrich, "MAX_RETRIES", 0)
    assert enrich.lookup(FakeSession(body, error), source_row)["status"] == status


def test_catalog_follows_the_page_kind_not_the_list_the_row_came_from():
    # 파일 목록에서 왔지만 실제로는 OpenAPI 페이지인 행 (json+xml 213건)
    assert enrich.catalog_url(gokr("openapi", formats=["json+xml"], list_type="file")).endswith("/15000001/openapi.json")
    assert enrich.catalog_url(gokr("standard")).endswith("/15000001/standard.json")
    assert enrich.catalog_url(gokr("fileData")).endswith("/15000001/fileData.json")


def test_catalog_json_ld():
    meta = enrich.parse_data_go_kr(catalog(
        encodingFormat="JSON+XML", dateModified="2026-04-02",
        additionalProperty=[{"name": "제공형태", "value": "REST"}, {"name": "업데이트 주기", "value": "실시간"}],
    ))
    assert meta == {"status": "ok", "license_text": "이용허락범위 제한 없음", "encoding": "JSON+XML",
                    "delivery": "REST", "cycle": "실시간", "modified": "2026-04-02"}
    assert enrich.parse_data_go_kr('{"@type": "Dataset", "description": "해당 데이터는 존재하지 않습니다."}') == {"status": "deleted"}


@pytest.mark.parametrize("text, facet_value", [
    ("공공저작물 : 출처표시 (제 1유형)", "commercial"),
    ("공공저작물 : 출처표시, 상업적 이용금지, 변경금지 (제 4유형)", "non_commercial"),
    ("이용허락범위 제한 없음", "commercial"),
    ("제3자 권리 포함 : 저작권 표시, 공공저작물 : 자유이용 (제 0유형)", "conditional"),
    ("이용제한없음 : 자유이용", "commercial"),
    ("제3자 권리 포함 : 저작권 표시, 공공저작물 : 출처표시 (제 1유형)", "conditional"),
    ("제3자 권리 포함 : 저작권 표시, 공공저작물 : 출처표시, 변경금지 (제 3유형)", "conditional"),
    # 제3자 권리가 있어도 비상업 조건은 그대로 남아야 한다
    ("제3자 권리 포함 : 저작권 표시, 비영리, 변경금지, 공공저작물 : 출처표시, 상업적 이용금지, 변경금지 (제 4유형)", "non_commercial"),
    ("제3자 권리 포함 : 저작권 표시, 비영리, 공공저작물 : 출처표시, 상업적 이용금지 (제 2유형)", "non_commercial"),
    ("공공누리 3유형 : 출처표시+변경금지", "commercial"),
    ("제3자 권리 포함 : 저작권 표시, 비영리, 동일조건 변경허락, null", "non_commercial"),
    ("제3자 권리 포함 : 저작권 표시, 비영리, 공공저작물 : 출처표시 (제 1유형)", "non_commercial"),
])
def test_official_license_maps_to_a_known_commercial_use(text, facet_value):
    assert normalize("commercial_use", enrich.official_license(text)) == facet_value


# ---------------------------------------------------------------- 제공 방식


def test_seoul_delivery_adds_sheet_csv_and_readable_files_only():
    assert enrich.official_formats(row(), enrich.parse_seoul(SEOUL_PAGE)) == ["api", "csv", "xlsx"]


def test_seoul_api_only_page():
    meta = {"status": "ok", "tabs": ["A"], "files": []}
    assert enrich.official_formats(row(), meta) == ["api"]


def test_unread_page_keeps_collected_delivery_except_known_api_pages():
    assert enrich.official_formats(row(formats=["api"]), {"status": "failed"}) == ["api"]
    assert enrich.official_formats(gokr("fileData", formats=["csv"]), {"status": "failed"}) == ["csv"]
    assert enrich.official_formats(gokr("openapi", formats=["json+xml"]), {"status": "unchecked"}) == ["api"]


def test_standard_delivery_comes_from_the_page_not_a_default():
    standard = gokr("standard", formats=["csv", "api"])
    assert enrich.official_formats(standard, {"status": "ok", "encoding": "CSV"}) == ["csv"]
    assert enrich.official_formats(standard, {"status": "ok", "encoding": "JSON+XML", "delivery": "LINK"}) == ["api", "json", "xml"]
    assert enrich.official_formats(standard, {"status": "ok"}) == []  # 미확인, 예전처럼 csv·api로 채우지 않음


def test_file_page_format_from_catalog():
    assert enrich.official_formats(gokr("fileData", formats=["csv"]), {"status": "ok", "encoding": "XLSX"}) == ["xlsx"]


# ---------------------------------------------------------------- 행 보완


def test_failed_lookup_keeps_collected_license_and_marks_the_row():
    out = enrich.enrich_row(row(licenses=["공공누리 제1유형"]), {"status": "failed"})
    assert out["licenses"] == ["공공누리 제1유형"] and out["official"]["status"] == "failed"
    assert out["update_cycle"] is None


def test_official_license_replaces_a_blank():
    out = enrich.enrich_row(row(), enrich.parse_seoul(SEOUL_PAGE))
    assert out["licenses"] == ["공공누리 제1유형"] and out["update_cycle"] == "비정기(수시, 자료변경시)"
    assert out["official"]["license_text"].startswith("공공누리 1유형")


def test_list_type_follows_page_kind():
    assert enrich.enrich_row(gokr("openapi", list_type="file"), {"status": "unchecked"})["list_type"] == "openapi"


def run_enrich(tmp_path, monkeypatch, rows, lookup):
    monkeypatch.setattr(enrich, "INPUT", tmp_path / "in.jsonl")
    monkeypatch.setattr(enrich, "OUT_DIR", tmp_path / "out")
    monkeypatch.setattr(enrich, "OUTPUT", tmp_path / "out" / "public_datasets.jsonl")
    monkeypatch.setattr(enrich, "CACHE", tmp_path / "cache.jsonl")
    monkeypatch.setattr(enrich, "lookup", lookup)
    monkeypatch.setattr(sys, "argv", ["18_enrich"])
    (tmp_path / "in.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    enrich.main()
    return enrich.read_jsonl(tmp_path / "out" / "public_datasets.jsonl")


def test_new_and_changed_rows_are_looked_up_unchanged_rows_are_not(tmp_path, monkeypatch):
    seen = []

    def lookup(session, r):
        seen.append(r["dataset_id"])
        return {"status": "ok", "license_text": "공공누리 1유형", "tabs": ["A"], "files": []}

    first = [row("seoul_open_data/OA-1"), row("seoul_open_data/OA-2")]
    run_enrich(tmp_path, monkeypatch, first, lookup)
    assert sorted(seen) == ["seoul_open_data/OA-1", "seoul_open_data/OA-2"]
    seen.clear()
    later = [row("seoul_open_data/OA-1"), row("seoul_open_data/OA-2", sha="s2"), row("seoul_open_data/OA-3")]
    out = run_enrich(tmp_path, monkeypatch, later, lookup)
    assert sorted(seen) == ["seoul_open_data/OA-2", "seoul_open_data/OA-3"]
    assert all(r["licenses"] == ["공공누리 제1유형"] for r in out)


def test_failed_lookup_is_not_cached_and_retried_next_run(tmp_path, monkeypatch):
    out = run_enrich(tmp_path, monkeypatch, [row()], lambda session, r: {"status": "failed"})
    assert out[0]["official"]["status"] == "failed" and not (tmp_path / "cache.jsonl").read_text(encoding="utf-8").strip()
    out = run_enrich(tmp_path, monkeypatch, [row()], lambda session, r: {"status": "ok", "license_text": "공공누리 1유형", "tabs": [], "files": []})
    assert out[0]["official"]["status"] == "ok"


def test_enrichment_writes_a_manifest_over_the_collected_file(tmp_path, monkeypatch):
    run_enrich(tmp_path, monkeypatch, [row()], lambda session, r: {"status": "deleted"})
    assert cm.check_manifest(tmp_path / "out") == []
    (tmp_path / "in.jsonl").write_text(json.dumps(row(sha="new")) + "\n", encoding="utf-8")  # 새로 수집됨
    assert any("in.jsonl 변경됨" in p for p in cm.check_manifest(tmp_path / "out"))


# ---------------------------------------------------------------- 단계 연결


def test_13_v2_refuses_collected_rows_that_skipped_enrichment(tmp_path, monkeypatch):
    run_enrich(tmp_path, monkeypatch, [row()], lambda session, r: {"status": "deleted"})
    (tmp_path / "in.jsonl").write_text(json.dumps(row(sha="new")) + "\n", encoding="utf-8")
    monkeypatch.setattr(graph13, "ENRICH_DIR", tmp_path / "out")
    monkeypatch.setattr(graph13, "load_model_rows", lambda: pytest.fail("그래프 생성까지 진행됨"))
    monkeypatch.setattr(sys, "argv", ["13", "--corpus", "v2"])
    with pytest.raises(SystemExit, match="run 18_enrich_public_datasets.py first"):
        graph13.main()


def test_v1_reads_the_collected_file_and_v2_the_enriched_one():
    assert graph13.PUBLIC_INPUTS["v1"] == chunks14.PUBLIC_INPUTS["v1"] == graph13.PUBLIC_INPUT
    assert graph13.PUBLIC_INPUTS["v2"] == chunks14.PUBLIC_INPUTS["v2"] == enrich.OUTPUT


def test_v2_card_shows_unknown_license_and_portal_cycle():
    entity = {"coverage_status": "unknown"}
    lines = chunks14.portal_card_lines({"source": "seoul_open_data", "licenses": [], "update_cycle": "실시간"}, entity)
    assert "이용허락: 확인 필요" in lines and "갱신 주기(포털 표기): 실시간" in lines
    lines = chunks14.portal_card_lines({"source": "seoul_open_data", "licenses": ["공공누리 제1유형"]}, entity)
    assert not any(line.startswith(("이용허락", "갱신 주기")) for line in lines)


# ---------------------------------------------------------------- 품질 검사


def built(n=100, **override):
    collected = [row(f"seoul_open_data/OA-{i}") for i in range(n)]
    enriched = [enrich.enrich_row(r, {"status": "ok", "license_text": "공공누리 1유형", "tabs": ["A"], "files": []}) for r in collected]
    entities = {f"dataset:{r['dataset_id']}": {"source": "seoul_open_data", "coverage_status": "unknown"} for r in collected}
    chunks = [{"dataset_id": r["dataset_id"], "kind": "card"} for r in collected]
    parts = {"collected": collected, "enriched": enriched, "entities": entities, "duplicates": {}, "chunks": chunks}
    parts.update(override)
    return parts


def test_quality_passes_a_complete_build():
    problems, report = pipeline.quality(**built())
    assert problems == [] and report["public_cards"] == 100 and report["licensed"]["enriched"] == 100


def test_quality_fails_when_too_many_pages_were_not_read():
    parts = built()
    for r in parts["enriched"][:3]:
        r["official"]["status"] = "failed"
    assert any("조회·해석 문제 3개" in p for p in pipeline.quality(**parts)[0])


def test_quality_fails_on_license_wording_the_taxonomy_does_not_know():
    parts = built()
    parts["enriched"][0]["licenses"] = []
    parts["enriched"][0]["official"]["license_text"] = "새 이용조건"
    assert any("새 이용조건" in p for p in pipeline.quality(**parts)[0])


def test_quality_fails_when_a_new_row_has_no_entity_or_card():
    parts = built()
    parts["entities"].pop("dataset:seoul_open_data/OA-5")
    parts["chunks"] = parts["chunks"][:-1]
    problems = pipeline.quality(**parts)[0]
    assert any("그래프에 없는" in p for p in problems) and any("검색 문서가 없는" in p for p in problems)


def test_quality_fails_when_enrichment_dropped_or_reordered_rows():
    parts = built()
    parts["enriched"] = parts["enriched"][1:]
    assert any("데이터 목록" in p for p in pipeline.quality(**parts)[0])


# ---------------------------------------------------------------- 1. 목록 갱신과 개별 항목 캐시


def test_pipeline_collect_refreshes_lists(monkeypatch):
    calls = []
    monkeypatch.setattr(pipeline, "run", lambda *args: calls.append(args))
    monkeypatch.setattr(pipeline, "check", lambda: ([], {}))
    monkeypatch.setattr(sys, "argv", ["pipeline", "--collect", "--offline"])
    pipeline.main()
    assert calls[0] == ("18_collect_public_datasets.py", "--source", "all", "--refresh-lists", "--renew-fields")
    assert [c[0] for c in calls[1:]] == ["18_enrich_public_datasets.py", "13_build_hypergraph.py", "14_build_dataset_chunks.py"]


@pytest.mark.parametrize("portal, env", [("seoul", "SEOUL_OPEN_API_KEY"), ("data_go_kr", "DATA_GO_KR_API_KEY")])
def test_refresh_lists_renews_lists_but_keeps_item_caches(monkeypatch, portal, env):
    collector = enrich.collect18
    lists, items = [], []
    monkeypatch.setenv(env, "test-key")
    monkeypatch.setattr(collector, "cached", lambda name, fetch, refresh: lists.append((name, refresh)) or [])
    monkeypatch.setattr(collector, "cached_items", lambda name, *args, **kw: items.append((name, args[3])) or {})
    getattr(collector, f"collect_{portal}")(None, False, 1, refresh_lists=True)
    assert lists and all(refresh for _, refresh in lists)
    assert items and not any(refresh for _, refresh in items)


def test_item_cache_fetches_only_ids_new_to_a_refreshed_list(tmp_path, monkeypatch):
    collector = enrich.collect18
    monkeypatch.setattr(collector, "CATALOG_DIR", tmp_path)
    fetched = []

    def one(item):
        fetched.append(item)
        return f"v{item}"

    collector.cached_items("x", [1, 2], str, one, False, 1)
    collector.cached_items("x", [1, 2, 3], str, one, False, 1)
    assert fetched == [1, 2, 3]


def test_lists_are_reused_without_refresh_and_renewed_with_it(tmp_path, monkeypatch):
    collector = enrich.collect18
    monkeypatch.setattr(collector, "CATALOG_DIR", tmp_path)
    assert collector.cached("l", lambda: [{"id": 1}], False) == [{"id": 1}]
    assert collector.cached("l", lambda: [{"id": 2}], False) == [{"id": 1}]
    assert collector.cached("l", lambda: [{"id": 2}], True) == [{"id": 2}]


# ---------------------------------------------------------------- 2. 만료 주기와 파서 버전


OK = {"status": "ok", "license_text": "공공누리 1유형", "tabs": ["A", "S"], "files": []}


def cache_entry(r, days_ago, status="ok", parser=None, **meta):
    from datetime import datetime, timedelta, timezone

    checked = (datetime.now(timezone.utc) - timedelta(days=days_ago)).isoformat(timespec="seconds")
    answer = {**OK} if status == "ok" else {"status": status}
    return {"dataset_id": r["dataset_id"], "row_sha": r["sha"], "parser_version": parser or enrich.PARSER_VERSION,
            "checked_at": checked, **answer, **meta}


def write_cache(tmp_path, *entries):
    (tmp_path / "cache.jsonl").write_text("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in entries), encoding="utf-8")


@pytest.mark.parametrize("days_ago, status, parser, looked_up", [
    (29, "ok", None, False),
    (31, "ok", None, True),  # 공식 페이지가 바뀌었을 수 있다
    (6, "deleted", None, False),
    (8, "deleted", None, True),  # 삭제도 주기적으로 다시 확인
    (1, "ok", "old-parser", True),  # 파서가 바뀌었다
])
def test_cached_answers_expire_and_follow_the_parser(tmp_path, monkeypatch, days_ago, status, parser, looked_up):
    r = row()
    write_cache(tmp_path, cache_entry(r, days_ago, status, parser))
    seen = []

    def lookup(session, x):
        seen.append(x)
        return OK

    run_enrich(tmp_path, monkeypatch, [r], lookup)
    assert bool(seen) == looked_up


def test_parser_version_tracks_the_parsing_code():
    import hashlib
    import inspect

    sources = "".join(inspect.getsource(f) for f in (enrich.plain_text, enrich.first, enrich.parse_data_go_kr, enrich.parse_seoul))
    patterns = "".join(r.pattern for r in (enrich.SEOUL_TAB_RE, enrich.SEOUL_FILE_RE, enrich.SEOUL_BUSY_RE))
    assert enrich.PARSER_VERSION == hashlib.sha256(sources.encode() + patterns.encode()).hexdigest()[:12]


def test_successful_recheck_replaces_the_answer_and_its_time(tmp_path, monkeypatch):
    r = row()
    old = cache_entry(r, 40, license_text="공공누리 4유형")
    write_cache(tmp_path, old)
    out = run_enrich(tmp_path, monkeypatch, [r], lambda session, x: OK)[0]
    assert out["licenses"] == ["공공누리 제1유형"] and out["official"]["recheck"] is None
    assert out["official"]["checked_at"] > old["checked_at"]


# ---------------------------------------------------------------- 3. 재조회 실패 시 직전 확인값 보존


def test_failed_recheck_of_a_changed_row_keeps_confirmed_values_and_asks_for_review(tmp_path, monkeypatch):
    entry = cache_entry(row(), 3, license_text="공공누리 4유형 : 출처표시+상업적 이용금지+변경금지", cycle="매일")
    write_cache(tmp_path, entry)
    out = run_enrich(tmp_path, monkeypatch, [row(sha="changed")], lambda session, x: {"status": "failed"})[0]
    assert out["licenses"] == ["공공누리 제4유형"] and out["update_cycle"] == "매일" and out["formats"] == ["api", "csv"]
    assert out["official"]["status"] == "ok" and out["official"]["checked_at"] == entry["checked_at"]
    assert out["official"]["recheck"] == "failed"
    assert out["official"]["needs_review"] and out["official"]["review_reasons"] == ["row_changed_since_check"]
    cached = json.loads((tmp_path / "cache.jsonl").read_text(encoding="utf-8"))
    assert cached["checked_at"] == entry["checked_at"]  # 실패는 캐시를 덮어쓰지 않는다


def test_failed_recheck_of_an_expired_unchanged_row_keeps_values_without_review(tmp_path, monkeypatch):
    r = row()
    write_cache(tmp_path, cache_entry(r, 40))
    out = run_enrich(tmp_path, monkeypatch, [r], lambda session, x: {"status": "parse_error"})[0]
    assert out["official"]["status"] == "ok" and out["official"]["recheck"] == "parse_error"
    assert not out["official"]["needs_review"] and out["licenses"] == ["공공누리 제1유형"]


def test_failed_recheck_after_a_parser_change_asks_for_review(tmp_path, monkeypatch):
    r = row()
    write_cache(tmp_path, cache_entry(r, 1, parser="old-parser"))
    out = run_enrich(tmp_path, monkeypatch, [r], lambda session, x: {"status": "failed"})[0]
    assert out["official"]["review_reasons"] == ["parser_changed_since_check"]


def run_with_flag(tmp_path, monkeypatch, flag, input_row, lookup=None):
    monkeypatch.setattr(enrich, "INPUT", tmp_path / "in.jsonl")
    monkeypatch.setattr(enrich, "OUT_DIR", tmp_path / "out")
    monkeypatch.setattr(enrich, "OUTPUT", tmp_path / "out" / "public_datasets.jsonl")
    monkeypatch.setattr(enrich, "CACHE", tmp_path / "cache.jsonl")
    monkeypatch.setattr(enrich, "lookup", lookup or (lambda session, x: pytest.fail("오프라인인데 조회함")))
    monkeypatch.setattr(sys, "argv", ["18_enrich", flag])
    (tmp_path / "in.jsonl").write_text(json.dumps(input_row) + "\n", encoding="utf-8")
    enrich.main()
    return enrich.read_jsonl(tmp_path / "out" / "public_datasets.jsonl")[0]


def test_forced_refresh_failure_keeps_fresh_values_and_reports_the_recheck(tmp_path, monkeypatch):
    write_cache(tmp_path, cache_entry(row(), 1))
    out = run_with_flag(tmp_path, monkeypatch, "--refresh", row(), lambda session, x: {"status": "failed"})
    assert out["official"]["status"] == "ok" and out["official"]["recheck"] == "failed"


def test_offline_run_of_a_changed_row_keeps_values_marked_unchecked(tmp_path, monkeypatch):
    write_cache(tmp_path, cache_entry(row(), 1))
    out = run_with_flag(tmp_path, monkeypatch, "--offline", row(sha="changed"))
    assert out["official"]["status"] == "ok" and out["official"]["recheck"] == "unchecked"
    assert out["official"]["needs_review"]


# ---------------------------------------------------------------- 4. 품질 검사의 상태 구분


def statuses(parts, status, n, recheck=None):
    for r in parts["enriched"][:n]:
        r["official"].update(status=status, recheck=recheck)
    return pipeline.quality(**parts)


@pytest.mark.parametrize("status", ["deleted", "failed", "parse_error", "no_page", "unchecked"])
def test_quality_fails_when_every_row_has_the_same_non_answer(status):
    problems, _ = statuses(built(), status, 100)
    assert problems


def test_quality_counts_no_page_and_parse_errors_as_lookup_problems():
    parts = built()
    parts["enriched"][0]["official"]["status"] = "no_page"
    parts["enriched"][1]["official"]["status"] = "parse_error"
    parts["enriched"][2]["official"]["status"] = "parse_error"
    problems, report = pipeline.quality(**parts)
    assert report["lookup_problems"] == {"parse_error": 2, "no_page": 1}
    assert any("조회·해석 문제 3개" in p for p in problems)


def test_quality_counts_failed_rechecks_even_when_older_values_are_in_use():
    problems, report = statuses(built(), "ok", 3, recheck="failed")
    assert report["lookup_problems"] == {"재확인 failed": 3} and problems


def test_quality_reports_a_few_real_deletions_without_failing():
    problems, report = statuses(built(), "deleted", 2)
    assert problems == [] and report["deleted_on_portal"] == ["seoul_open_data/OA-0", "seoul_open_data/OA-1"]


def test_quality_lists_rows_to_review():
    parts = built()
    parts["enriched"][4]["official"].update(needs_review=True, review_reasons=["row_changed_since_check"])
    assert pipeline.quality(**parts)[1]["needs_review"] == {"count": 1, "dataset_ids": ["seoul_open_data/OA-4"]}


def test_quality_counts_an_unknown_status_as_a_problem():
    problems, report = statuses(built(), "missing", 100)  # 예전 형식의 상태
    assert report["lookup_problems"] == {"missing": 100} and problems


def test_old_cache_entries_without_an_answer_are_looked_up_again(tmp_path, monkeypatch):
    r = row()
    write_cache(tmp_path, cache_entry(r, 1, status="missing"))
    seen = []

    def lookup(session, x):
        seen.append(x)
        return {"status": "failed"}

    out = run_enrich(tmp_path, monkeypatch, [r], lookup)[0]
    assert seen and out["official"]["status"] == "failed" and out["official"]["recheck"] is None


def test_quality_fails_on_empty_input():
    assert pipeline.quality(collected=[], enriched=[], entities={}, duplicates={}, chunks=[])[0]


# ---------------------------------------------------------------- 저장된 원문 재파싱과 호환 이관


def no_lookup(session, x):
    pytest.fail(f"조회하면 안 됨: {x['dataset_id']}")


def test_lookup_keeps_the_page_behind_an_answer(monkeypatch):
    meta = enrich.lookup(FakeSession(SEOUL_PAGE), row())
    assert meta["status"] == "ok" and enrich.load_raw({"dataset_id": row()["dataset_id"], **meta}) == SEOUL_PAGE


def test_failed_parse_does_not_replace_the_stored_page(monkeypatch):
    sha = enrich.save_raw(row()["dataset_id"], SEOUL_PAGE)
    assert enrich.lookup(FakeSession("<html>모르는 모양</html>"), row()) == {"status": "parse_error"}
    assert enrich.load_raw({"dataset_id": row()["dataset_id"], "raw_sha256": sha}) == SEOUL_PAGE


def test_parser_change_reparses_the_stored_page_without_fetching(tmp_path, monkeypatch):
    r = row()
    sha = enrich.save_raw(r["dataset_id"], SEOUL_PAGE)
    entry = cache_entry(r, 2, parser="old-parser", raw_sha256=sha, license_text="공공누리 4유형", tabs=["A"])
    write_cache(tmp_path, entry)
    out = run_enrich(tmp_path, monkeypatch, [r], no_lookup)[0]
    assert out["official"]["verification"] == "reparsed" and out["official"]["parser_version"] == enrich.PARSER_VERSION
    assert out["official"]["checked_at"] == entry["checked_at"]  # 원문을 받은 시점은 그대로
    assert out["licenses"] == ["공공누리 제1유형"] and out["formats"] == ["api", "csv", "xlsx"]
    cached = json.loads((tmp_path / "cache.jsonl").read_text(encoding="utf-8"))
    assert cached["reparsed_from"] == "old-parser" and {"license_text", "tabs", "files"} <= set(cached["reparse_changed"])


@pytest.mark.parametrize("stored", ["none", "tampered"])
def test_parser_change_without_a_usable_page_is_fetched(tmp_path, monkeypatch, stored):
    r = row()
    sha = enrich.save_raw(r["dataset_id"], SEOUL_PAGE)
    if stored == "none":
        enrich.raw_path(r["dataset_id"]).unlink()
    else:
        enrich.raw_path(r["dataset_id"]).write_bytes(__import__("gzip").compress(b"<html>other</html>"))
    write_cache(tmp_path, cache_entry(r, 2, parser="old-parser", raw_sha256=sha))
    seen = []
    run_enrich(tmp_path, monkeypatch, [r], lambda session, x: seen.append(x) or OK)
    assert seen


def compat(accepted_for):
    return {"basis_id": "b1", "from_parser": None, "accepted_for": accepted_for, "migrated_at": "2026-11-08T00:00:00+00:00"}


def test_compat_migrated_answer_is_used_but_reported_separately(tmp_path, monkeypatch):
    r = row()
    entry = cache_entry(r, 2, compat=compat(enrich.PARSER_VERSION))
    entry["parser_version"] = None  # 원래 버전(기록 없음) 보존
    write_cache(tmp_path, entry)
    out = run_enrich(tmp_path, monkeypatch, [r], no_lookup)[0]
    assert out["official"]["verification"] == "compat" and out["official"]["parser_version"] is None
    assert out["official"]["checked_at"] == entry["checked_at"] and out["official"]["recheck"] is None


@pytest.mark.parametrize("accepted_for, days_ago", [("another-parser", 2), (None, 31)])
def test_compat_ends_with_a_new_parser_or_the_age_limit(tmp_path, monkeypatch, accepted_for, days_ago):
    r = row()
    entry = cache_entry(r, days_ago, compat=compat(accepted_for or enrich.PARSER_VERSION))
    entry["parser_version"] = None
    write_cache(tmp_path, entry)
    seen = []
    out = run_enrich(tmp_path, monkeypatch, [r], lambda session, x: seen.append(x) or OK)[0]
    assert seen and out["official"]["verification"] == "fetched"


def test_quality_reports_how_answers_were_verified():
    parts = built()
    parts["enriched"][0]["official"]["verification"] = "compat"
    assert pipeline.quality(**parts)[1]["verification"]["compat"] == 1


# ---------------------------------------------------------------- 데이터 버전 고정


def test_pin_detects_a_rebuilt_stage(tmp_path, monkeypatch):
    dirs = []
    for name in ("enrich", "hypergraph", "documents"):
        d = tmp_path / name
        d.mkdir()
        (d / "out.jsonl").write_text("{}\n", encoding="utf-8")
        cm.write_manifest(d, stage=name, corpus="v2", options={}, inputs=[], code=[], outputs=[d / "out.jsonl"], counts={"n": 1})
        dirs.append((name, d))
    monkeypatch.setattr(pipeline, "STAGES", tuple(dirs))
    monkeypatch.setattr(pipeline, "PIN", tmp_path / "data_version.json")
    report = {k: 0 for k in ("rows", "official_status", "verification", "lookup_problems", "licensed",
                             "license_needs_check", "public_entities", "public_cards")}
    pin = pipeline.write_pin(report)
    assert pipeline.verify_pin() == [] and pin["data_version"] == cm.load_manifest(dirs[2][1])["stage_id"][:16]
    (dirs[1][1] / "out.jsonl").write_text('{"x": 1}\n', encoding="utf-8")  # 그래프를 다시 만듦
    cm.write_manifest(dirs[1][1], stage="hypergraph", corpus="v2", options={}, inputs=[], code=[],
                      outputs=[dirs[1][1] / "out.jsonl"], counts={"n": 2})
    assert any(p.startswith("hypergraph") for p in pipeline.verify_pin())


# ---------------------------------------------------------------- 서울 필드 캐시 갱신 정책


def items_run(monkeypatch, entries, items, **policy):
    collector = enrich.collect18
    collector.CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    (collector.CATALOG_DIR / "f.jsonl").write_text("".join(json.dumps(e) + "\n" for e in entries), encoding="utf-8")
    fetched = []

    def one(item):
        fetched.append(item["id"])
        if item.get("fail"):
            raise RuntimeError("down")
        return f"new-{item['id']}"

    values = collector.cached_items("f", items, lambda i: i["id"], one, False, 1, **policy)
    return fetched, values


def days_ago(n):
    from datetime import datetime, timedelta, timezone

    return (datetime.now(timezone.utc) - timedelta(days=n)).isoformat(timespec="seconds")


def version(item):
    return item["v"]


def test_default_item_cache_only_fetches_new_ids(monkeypatch):
    entries = [{"key": "a", "value": "old-a"}, {"key": "b", "value": "old-b", "fetched_at": days_ago(400), "version": "1"}]
    fetched, values = items_run(monkeypatch, entries, [{"id": "a", "v": "9"}, {"id": "b", "v": "9"}, {"id": "c", "v": "1"}])
    assert fetched == ["c"] and values["a"] == "old-a" and values["b"] == "old-b"


def test_changed_catalog_row_renews_the_field_list(monkeypatch):
    entries = [{"key": "a", "value": "old-a", "fetched_at": days_ago(1), "version": "1"},
               {"key": "b", "value": "old-b", "fetched_at": days_ago(1), "version": "1"}]
    fetched, values = items_run(monkeypatch, entries, [{"id": "a", "v": "2"}, {"id": "b", "v": "1"}],
                                version=version, max_age_days=30, max_renew=10)
    assert fetched == ["a"] and values == {"a": "new-a", "b": "old-b"}


def test_old_or_undated_field_lists_are_renewed_oldest_first_within_the_budget(monkeypatch):
    entries = [{"key": "a", "value": "x", "fetched_at": days_ago(40), "version": "1"},
               {"key": "b", "value": "x", "fetched_at": days_ago(5), "version": "1"},
               {"key": "c", "value": "x"},  # 예전 형식: 언제 받았는지 모름
               {"key": "d", "value": "x", "fetched_at": days_ago(35), "version": "1"},
               {"key": "e", "value": "x", "fetched_at": days_ago(1), "version": "1"}]
    items = [{"id": k, "v": "1"} for k in "abcd"] + [{"id": "e", "v": "2"}]
    fetched, _ = items_run(monkeypatch, entries, items, version=version, max_age_days=30, max_renew=3)
    assert fetched == ["e", "c", "a"]  # 변경 먼저, 그다음 가장 오래된 것; d는 다음 실행으로


def test_failed_renewal_keeps_the_cached_field_list(monkeypatch):
    entries = [{"key": "a", "value": "old-a", "fetched_at": days_ago(40), "version": "1"}]
    _, values = items_run(monkeypatch, entries, [{"id": "a", "v": "1", "fail": True}], version=version, max_age_days=30)
    assert values == {"a": "old-a"}
    stored = json.loads((enrich.collect18.CATALOG_DIR / "f.jsonl").read_text(encoding="utf-8"))
    assert stored["fetched_at"] == entries[0]["fetched_at"]


def test_failed_new_item_still_raises(monkeypatch):
    with pytest.raises(RuntimeError):
        items_run(monkeypatch, [], [{"id": "a", "v": "1", "fail": True}])


def test_catalog_version_ignores_counters_only():
    base = {"INF_ID": "OA-1", "INF_NM": "이름", "VIEW_CNT": 3, "HIT": 1}
    same = enrich.collect18.catalog_version
    assert same(base) == same({**base, "VIEW_CNT": 99, "HIT": 7})
    assert same(base) != same({**base, "INF_NM": "새 이름"})


@pytest.mark.parametrize("renew", [True, False])
def test_seoul_renewal_applies_to_field_lists_only(monkeypatch, renew):
    collector = enrich.collect18
    calls = {}
    monkeypatch.setenv("SEOUL_OPEN_API_KEY", "test-key")
    monkeypatch.setattr(collector, "cached", lambda name, fetch, refresh: [])
    monkeypatch.setattr(collector, "cached_items", lambda name, *args, **kw: calls.__setitem__(name, kw) or {})
    collector.collect_seoul(None, False, 1, renew_fields=renew)
    assert calls["seoul_licenses_by_id"] == {}
    if renew:
        assert calls["seoul_fields_by_id"] == {"version": collector.catalog_version, "max_age_days": 30, "max_renew": 300}
    else:
        assert calls["seoul_fields_by_id"] == {}
