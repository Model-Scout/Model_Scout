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
