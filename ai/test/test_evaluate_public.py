"""Hand-computed checks for the common public-data evaluator (no corpus, no network)."""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

import pytest

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))
_spec = importlib.util.spec_from_file_location("evaluate_public", AI / "test" / "public_data" / "evaluate_public.py")
ev = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ev)

V5 = AI / "test" / "public_data" / "corpus_v2" / "golden_prep" / "batch3" / "labels_llm_v5.jsonl"


def label(qid="q1", relevant=None, must_exclude=(), irrelevant=(), unjudged=(), behavior="recommend", qtype="t"):
    relevant = dict(relevant or {})
    grades = set(relevant.values())
    return {
        "query_id": qid, "query_type": qtype, "expected_behavior": behavior,
        "relevant": relevant, "must_exclude": list(must_exclude), "judged_irrelevant": list(irrelevant),
        "unjudged": list(unjudged),
        "evaluable": (not unjudged) if behavior == "abstain" else bool(grades),
    }


def one(lab, ranked, canonical=None):
    return ev.score_query(lab, ranked, canonical or {})


# ---------------------------------------------------------------- extremes


def test_perfect_ranking_scores_one():
    lab = label(relevant={"a": 2, "b": 2, "c": 1})
    m = one(lab, ["a", "b", "c"])
    for key in ("recall@5", "recall@10", "mrr@5", "ndcg@5", "map@5", "hit@10"):
        assert m["any"]["raw"][key] == pytest.approx(1.0), key
    assert m["direct"]["raw"]["recall@10"] == 1.0


def test_empty_and_all_wrong_rankings_score_zero():
    lab = label(relevant={"a": 2}, irrelevant=["x", "y"])
    for ranked in ([], ["x", "y"]):
        m = one(lab, ranked)
        assert m["any"]["raw"]["recall@10"] == 0.0
        assert m["any"]["raw"]["mrr@5"] == 0.0
        assert m["any"]["raw"]["ndcg@5"] == 0.0


# ---------------------------------------------------------------- hand-computed


def test_hand_computed_metrics():
    # relevant: a=2, b=1, c=1 ; ranked: x a y b  (x, y judged irrelevant)
    lab = label(relevant={"a": 2, "b": 1, "c": 1}, irrelevant=["x", "y"])
    m = one(lab, ["x", "a", "y", "b"])
    anyr = m["any"]["raw"]
    assert anyr["recall@10"] == pytest.approx(2 / 3)
    assert anyr["precision@10"] == pytest.approx(2 / 10)
    assert anyr["mrr@5"] == pytest.approx(1 / 2)
    assert anyr["map@5"] == pytest.approx((1 / 2 + 2 / 4) / 3)
    dcg = 2 / math.log2(3) + 1 / math.log2(5)
    idcg = 2 / math.log2(2) + 1 / math.log2(3) + 1 / math.log2(4)
    assert anyr["ndcg@5"] == pytest.approx(dcg / idcg)
    direct = m["direct"]["raw"]  # only "a" counts
    assert direct["recall@10"] == 1.0
    assert direct["mrr@5"] == pytest.approx(1 / 2)


def test_recall_does_not_cap_at_ten():
    relevant = {f"r{i}": 1 for i in range(20)}
    m = one(label(relevant=relevant), [f"r{i}" for i in range(10)])
    assert m["any"]["raw"]["recall@10"] == pytest.approx(0.5)


# ---------------------------------------------------------------- rules


def test_query_without_grade2_is_left_out_of_direct():
    m = one(label(relevant={"b": 1}), ["b"])
    assert m["direct"] is None
    assert m["any"]["raw"]["recall@10"] == 1.0


def test_held_dataset_is_miss_in_raw_and_dropped_in_condensed():
    lab = label(relevant={"a": 2}, unjudged=["h"])
    m = one(lab, ["h", "a"])
    assert m["any"]["raw"]["mrr@5"] == pytest.approx(1 / 2)
    assert m["any"]["condensed"]["mrr@5"] == 1.0
    assert m["held@10"] == 1
    assert m["judged@10"] == pytest.approx(1 / 2)


def test_unjudged_dataset_is_dropped_in_condensed_and_listed():
    lab = label(relevant={"a": 2})
    m = one(lab, ["new", "a"])
    assert m["any"]["raw"]["mrr@5"] == pytest.approx(1 / 2)
    assert m["any"]["condensed"]["mrr@5"] == 1.0
    assert m["unjudged_top10"] == ["new"]


def test_copies_count_once():
    canonical = {"a_copy": "a"}
    lab = label(relevant={"a": 2, "a_copy": 2, "b": 1})
    assert ev.canonical_grades(lab, canonical) == {"a": 2, "b": 1}
    m = one(lab, ["a_copy", "a", "b"], canonical)
    # a and its copy are one dataset: two distinct answers, both found, no double hit
    assert m["any"]["raw"]["recall@10"] == 1.0
    assert m["any"]["raw"]["precision@10"] == pytest.approx(2 / 10)


def test_must_exclude_is_counted_as_violation():
    lab = label(relevant={"a": 2}, must_exclude=["bad"])
    m = one(lab, ["bad", "a"])
    assert m["must_exclude@10"] == 1
    assert m["any"]["raw"]["mrr@5"] == pytest.approx(1 / 2)


def test_abstention_reports_counts_not_accuracy():
    lab = label(relevant={}, must_exclude=["bad"], behavior="abstain")
    m = one(lab, ["bad", "x"])
    assert m["any"] is None and m["direct"] is None
    assert m["abstain"] == {"returned": 2, "judged_relevant_or_excluded": 1}


# ---------------------------------------------------------------- run checks and real labels


def test_run_must_cover_exactly_the_evaluable_queries():
    labels = [label("q1", {"a": 2}), label("q2", {"b": 2})]
    with pytest.raises(ValueError, match="missing"):
        ev.evaluate(labels, {"q1": ["a"]}, {})
    with pytest.raises(ValueError, match="not in labels"):
        ev.evaluate(labels, {"q1": ["a"], "q2": ["b"], "zz": []}, {})


def test_summary_means_by_type():
    labels = [label("q1", {"a": 2}, qtype="t1"), label("q2", {"b": 1}, qtype="t1")]
    result = ev.evaluate(labels, {"q1": ["a"], "q2": ["x", "b"]}, {})
    t1 = result["summary"]["t1"]
    assert t1["any"]["raw"]["mrr@5"] == pytest.approx((1 + 1 / 2) / 2)
    assert t1["direct"]["raw"]["mrr@5"] == 1.0  # only q1 has a 2
    assert t1["direct_queries"] == 1 and t1["no_direct_answer"] == 1


@pytest.mark.skipif(not V5.exists(), reason="v5 labels not present")
def test_v5_labels_perfect_run_scores_one():
    labels = ev.read_jsonl(V5)
    runs = {l["query_id"]: sorted(l["relevant"], key=lambda d: -l["relevant"][d])
            for l in labels if l["evaluable"]}  # abstention queries get an empty list
    result = ev.evaluate(labels, runs, {})
    assert len(result["abstain"]) == 4 and all(a["returned"] == 0 for a in result["abstain"])
    assert result["summary"]["all"]["any"]["raw"]["hit@10"] == 1.0
    assert result["summary"]["all"]["direct"]["raw"]["mrr@5"] == 1.0
