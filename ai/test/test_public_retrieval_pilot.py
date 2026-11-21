"""Unit checks for test/public_data/retrieval/pilot.py (no corpus load, no API)."""

import importlib.util
import sys
from pathlib import Path

AI = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("public_pilot", AI / "test" / "public_data" / "retrieval" / "pilot.py")
pilot = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = pilot
spec.loader.exec_module(pilot)


def test_tokens_words_bigrams_ids_numbers():
    toks = pilot.tokens("공영주차장 data_go_kr/15000115 공공누리 1유형 GGUF")
    assert {"공영주차장", "data", "go", "kr", "15000115", "1유형", "gguf"} <= set(toks)
    assert {"#공영", "#영주", "#주차", "#차장", "#유형"} <= set(toks)
    assert "#1유" not in toks  # bigrams come from Hangul-only runs


def test_bm25_matches_compound_through_bigrams():
    bm = pilot.BM25(["서울 공영주차장 위치 정보", "전국 도서관 목록", "주차 요금 안내"])
    scores = bm.scores("주차장을 찾고 싶어")
    assert scores[0] > scores[2] > 0 and scores[1] == 0


class FakeConditions:
    def __init__(self, statuses):
        self.statuses = statuses

    def check(self, spec, dataset_id):
        return self.statuses[dataset_id]


def test_filter_drops_only_confirmed_unmet():
    cond = FakeConditions({"a": {"region": pilot.gp.MET}, "b": {"region": pilot.gp.UNMET},
                           "c": {"region": pilot.gp.UNKNOWN}, "d": {"region": pilot.gp.PARTIAL}})
    kept, removed, _ = pilot.apply_filter(["a", "b", "c", "d"], {}, cond)
    assert kept == ["a", "c", "d"] and removed == ["b"]


def test_score_collapses_copies_and_separates_held():
    label = {"relevant": {"x": 2, "y": 1}, "must_exclude": [], "judged_irrelevant": ["z"], "unjudged": ["h"],
             "expected_behavior": "recommend"}
    alias = {"x": {"x", "x2"}, "x2": {"x", "x2"}}
    ranking = ["x2", "x", "h", "new", "y", "z"]
    s = pilot.score_query(ranking, label, alias, {d: {} for d in ranking})
    assert s["duplicates_collapsed"] == 1 and s["held@10"] == 1 and s["unjudged@10"] == 1
    assert s["raw"]["recall@10"] == 1.0 and s["raw"]["mrr@5"] == 1.0
    assert s["condensed"]["precision@5"] == 2 / 5  # x, y, z left after held and unjudged drop
    assert s["raw2"]["recall@10"] == 1.0


def test_coverage_counts_relevant_kinds_once_and_requires_tags():
    specs = {"q": {"type": "multi_dataset", "expected_behavior": "recommend", "aspects": ["A", "B", "C"]}}
    labels = [{"query_id": "q", "relevant": {"a": 1, "a2": 1, "b": 1}}]
    alias = {"a": {"a", "a2"}, "a2": {"a", "a2"}}
    covers = [{"query_id": "q", "dataset_id": "a", "covers": ["A"]}, {"query_id": "q", "dataset_id": "b", "covers": ["B"]}]
    rankings = [{"path": "p", "query_id": "q", "top": ["a2", "x", "a", "b"]}]
    cov = pilot.coverage_at_k(rankings, labels, specs, alias, covers)
    assert cov["p"]["q"]["covered"] == ["A", "B"] and cov["p"]["q"]["missing"] == ["C"]
    assert abs(cov["p"]["q"]["coverage@10"] - 2 / 3) < 1e-9
    try:
        pilot.coverage_at_k(rankings, [{"query_id": "q", "relevant": {"c": 1}}], specs, alias, covers)
    except SystemExit:
        pass
    else:
        raise AssertionError("an untagged relevant pair must stop the run")


def test_diagnose_stage_order():
    dspec = importlib.util.spec_from_file_location("public_diagnose", AI / "test" / "public_data" / "retrieval" / "diagnose.py")
    diagnose = importlib.util.module_from_spec(dspec)
    dspec.loader.exec_module(diagnose)
    final = ["a", "b", "c", "d", "e", "f"]
    same = lambda d: d  # noqa: E731
    assert diagnose.stage_of("a", [], [], [], final, same) == "top_5"
    assert diagnose.stage_of("f", [], [], [], final, same) == "rank_6_10"
    assert diagnose.stage_of("x", ["y"], ["z"], [], final, same) == "no_candidate"
    assert diagnose.stage_of("x", ["x"], [], ["x"], final, same) == "filtered"
    assert diagnose.stage_of("x", [], ["x"], [], final, same) == "below_10"


def test_fusion_merges_keep_every_candidate_once():
    fspec = importlib.util.spec_from_file_location("public_fusion", AI / "test" / "public_data" / "retrieval" / "fusion_compare.py")
    fc = importlib.util.module_from_spec(fspec)
    fspec.loader.exec_module(fc)
    dense, sparse = ["a", "b", "c", "d"], ["x", "a", "y"]
    assert fc.interleave(dense, sparse) == ["a", "x", "b", "c", "y", "d"]
    head = fc.protect(dense, sparse, m=2)
    assert head[:3] == ["a", "x", "b"] and sorted(head) == sorted(set(dense + sparse))
    assert fc.rrf(60)(dense, sparse)[0] == "a"  # in both channels


def test_decompose_v2_extraction_scoring_and_policy():
    vspec = importlib.util.spec_from_file_location("public_decompose_v2", AI / "test" / "public_data" / "retrieval" / "decompose_v2.py")
    dv = importlib.util.module_from_spec(vspec)
    vspec.loader.exec_module(dv)
    spec = {"conditions": {"region": "경남", "delivery": "file", "realtime": False, "commercial": False},
            "region_scope": None, "kogl_type1_only": False}
    want = dv.truth(spec)
    got = {**want, "region": "경상남도", "delivery": None, "realtime": True}
    got["region"] = dv.canon_region(got["region"])
    cmp = dv.compare(want, got)
    assert cmp["region"] == "ok" and cmp["delivery"] == "missed" and cmp["realtime"] == "added" and cmp["commercial"] == "none"
    assert dv.compare({**want, "region": "서울"}, want)["region"] == "wrong"
    # policy: an extracted 전국 never becomes a region filter
    assert dv.as_filter({**want, "region": None, "region_scope": "전국"})["region"] is None
    base = dv.extracted_base({"dataset_terms": ["경상남도", "전통시장", "전국"], "commercial_only": True})
    assert base["region"] == "경남" and base["region_scope"] == "전국" and base["delivery"] is None and base["commercial"]
    plan = {"explicit": {**{c: None for c in dv.CONDS}, **{f"{c}_evidence": "" for c in dv.CONDS}, "delivery": "file", "delivery_evidence": "CSV로"}}
    assert dv.evidence_problems("전국 주차장 CSV 파일로 받고 싶어", plan) == ["delivery: 근거 'CSV로'가 원문에 없음"]


def test_decompose_v2_region_names():
    vspec = importlib.util.spec_from_file_location("public_decompose_v2b", AI / "test" / "public_data" / "retrieval" / "decompose_v2.py")
    dv = importlib.util.module_from_spec(vspec)
    vspec.loader.exec_module(dv)
    assert [dv.canon_region(x) for x in ("서울시", "서울특별시", "제주도", "경상남도", "부산", "대구광역시")] == ["서울", "서울", "제주", "경남", "부산", "대구"]
    assert dv.canon_region("시내버스") == "시내버스" and dv.canon_region(None) is None


def test_decompose_v2_compare_accepts_finer_region_and_skips_exempt():
    vspec = importlib.util.spec_from_file_location("public_decompose_v2c", AI / "test" / "public_data" / "retrieval" / "decompose_v2.py")
    dv = importlib.util.module_from_spec(vspec)
    vspec.loader.exec_module(dv)
    spec = {"conditions": {"region": "충북", "delivery": "api", "realtime": True, "commercial": False},
            "region_scope": None, "kogl_type1_only": False, "region_detail": "청주", "scoring_exempt": ["realtime"]}
    want = dv.truth(spec)
    got = {**want, "region": "청주", "realtime": False}
    cmp = dv.compare(want, got, spec)
    assert cmp["region"] == "ok" and cmp["realtime"] == "exempt" and cmp["delivery"] == "ok"
    assert dv.compare(want, {**got, "region": "대전"}, spec)["region"] == "wrong"
    assert dv.compare(want, got)["region"] == "wrong"  # without the spec's detail, 청주 ≠ 충북


def test_decompose_v2_finer_region_is_not_a_filter():
    vspec = importlib.util.spec_from_file_location("public_decompose_v2d", AI / "test" / "public_data" / "retrieval" / "decompose_v2.py")
    dv = importlib.util.module_from_spec(vspec)
    vspec.loader.exec_module(dv)
    got = {"region": "청주", "region_scope": None, "delivery": "api", "realtime": False, "commercial": False, "kogl_type1_only": False}
    assert dv.as_filter(got)["region"] is None and dv.as_filter({**got, "region": "충북"})["region"] == "충북"
    base = dv.extracted_base({"dataset_terms": ["청주", "공중화장실"], "commercial_only": False}, detail="청주")
    assert base["region"] == "청주"
    kept = {"dataset_query": "충북 청주 공중화장실 위치", "dataset_terms": ["충북", "공중화장실"]}
    assert dv.detail_kept(kept, "청주") and not dv.detail_kept({**kept, "dataset_query": "충북 공중화장실"}, "청주")


def test_rescore_refuses_changed_question_or_conditions():
    import pytest
    specs = {"p1": {"query_id": "p1", "query": "서울 주차장", "conditions": {"region": "서울"}, "type": "single"}}
    prior = {"search_inputs": pilot.search_inputs(specs)}
    pilot.rescore_guard(prior, {"p1": {**specs["p1"], "type": "multi_dataset", "aspects": ["a"]}})  # no new search needed
    for changed in ({"conditions": {"region": "부산"}}, {"query": "서울 공영주차장"}):
        with pytest.raises(SystemExit):
            pilot.rescore_guard(prior, {"p1": {**specs["p1"], **changed}})
