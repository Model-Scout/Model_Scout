"""Unit tests for retrieval_lab (no model download, no LLM call)."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from retrieval_lab import dense, fusion, golden, metrics, pipeline, planner, pre_retrieval  # noqa: E402


def test_weighted_rrf_orders_by_weighted_reciprocal_rank():
    fused = fusion.weighted_rrf([(0.8, ["a", "b"]), (0.2, ["b", "c"])], k=60)
    scores = dict(fused)
    assert math.isclose(scores["a"], 0.8 / 61)
    assert math.isclose(scores["b"], 0.8 / 62 + 0.2 / 61)
    assert [model_id for model_id, _ in fused] == ["b", "a", "c"]  # b appears in both lists


def test_zero_weight_channel_is_ignored():
    assert [m for m, _ in fusion.weighted_rrf([(0.0, ["x"]), (1.0, ["y"])])] == ["y"]


def test_channel_weight_is_split_over_variants():
    lists = fusion.channel_lists([["a"], ["b"]], [["c"]], 0.6, 0.4)
    assert [weight for weight, _ in lists] == [0.3, 0.3, 0.4]


def test_ranking_metrics_hand_computed():
    grades = {"a": 2, "b": 1, "z": 2}
    ranked = ["x", "a", "y", "b", "q", "r", "s", "t", "u", "z"]
    out = metrics.ranking_metrics(ranked, grades)
    assert out["recall@5"] == pytest.approx(2 / 3)
    assert out["recall@10"] == pytest.approx(1.0)
    assert out["precision@5"] == pytest.approx(2 / 5)
    assert out["precision@10"] == pytest.approx(3 / 10)
    assert out["f1@10"] == pytest.approx(2 * 0.3 * 1.0 / 1.3)
    assert out["hit@10"] == 1.0
    assert out["mrr@5"] == pytest.approx(1 / 2)
    assert out["map@5"] == pytest.approx((1 / 2 + 2 / 4) / 3)
    dcg = 2 / math.log2(3) + 1 / math.log2(5)
    idcg = 2 / math.log2(2) + 2 / math.log2(3) + 1 / math.log2(4)
    assert out["ndcg@5"] == pytest.approx(dcg / idcg)


def test_strict_grade_ignores_acceptable():
    out = metrics.ranking_metrics(["b", "a"], {"a": 2, "b": 1}, min_grade=2)
    assert out["mrr@5"] == pytest.approx(1 / 2)
    assert out["recall@5"] == 1.0


def test_percentile_nearest_rank():
    values = list(range(1, 101))
    assert metrics.percentile(values, 95) == 95
    assert metrics.percentile(values, 99) == 99
    assert metrics.percentile([], 95) is None


def test_planner_defaults_and_config(tmp_path):
    query = {"tasks": ["translation"], "korean_required": True, "max_parameters_billion": 1, "min_context_length": None}
    plan = planner.plan_for("semantic_capability", query, config={"types": {}})
    assert (plan.dense_weight, plan.sparse_weight, plan.strategies(), plan.top_k) == (0.5, 0.5, (), 30)
    assert plan.hard_filters == {"tasks": ["translation"], "korean_required": True, "max_parameters_billion": 1}
    config = {"types": {"semantic_capability": {"dense_weight": 0.64, "use_rewrite": True, "use_hyde": True}}}
    tuned = planner.plan_for("semantic_capability", query, config=config)
    assert (tuned.dense_weight, tuned.sparse_weight) == (0.64, 0.36)
    assert tuned.strategies() == ("rewrite", "hyde")
    assert tuned.label() == "Rewrite + HyDE"

    path = tmp_path / "planner.json"
    planner.save_type_plan("lexical_exact", planner.with_dense_weight(planner.BASELINE, 0.2), {"metric": "recall@10"}, path)
    saved = json.loads(path.read_text(encoding="utf-8"))["types"]["lexical_exact"]
    assert saved["dense_weight"] == 0.2 and saved["sparse_weight"] == 0.8


def test_golden_grades_and_unreachable():
    item = {
        "id": "sg_x", "text": "q", "plan_query_type": "semantic_capability", "evaluable_now": True,
        "labels": {"expected_behavior": "recommend", "expected_any": ["a", "missing"], "acceptable": ["b"],
                   "must_exclude": [{"model_id": "c"}], "judged_irrelevant": ["d"]},
    }
    query = golden.to_golden(item, corpus_ids={"a", "b", "c"})
    assert query.grades == {"a": 2, "b": 1}
    assert query.unreachable == ["missing"]
    assert query.must_exclude == ["c"]
    assert query.judged == {"a", "b", "c", "d"}
    compare = golden.to_golden({**item, "labels": {"expected_behavior": "compare", "expected_all": ["a", "b"]}}, {"a", "b"})
    assert compare.grades == {"a": 2, "b": 2}
    assert compare.judged is None


def test_supplement_fills_only_unjudged_models():
    item = {"id": "q1", "text": "x", "labels": {"expected_behavior": "recommend", "expected_any": ["a"],
            "judged_irrelevant": ["b"]}}
    marks = [
        {"model_id": "a", "score": 0},  # existing label wins
        {"model_id": "b", "score": 2},  # already judged irrelevant: unchanged
        {"model_id": "c", "score": 2},
        {"model_id": "d", "score": 1},
        {"model_id": "e", "score": 0},
        {"model_id": "gone", "score": 2},  # not in corpus
    ]
    query = golden.supplement(golden.to_golden(item, {"a", "b", "c", "d", "e"}), marks, {"a", "b", "c", "d", "e"})
    assert query.grades == {"a": 2, "c": 2, "d": 1}
    assert query.judged == {"a", "b", "c", "d", "e"}
    compare = golden.to_golden({**item, "labels": {"expected_behavior": "compare", "expected_all": ["a"]}}, {"a"})
    assert golden.supplement(compare, marks).grades == {"a": 2}


def test_golden_files_have_plan_types():
    queries = golden.load()
    types = {query.plan_query_type for query in queries}
    assert types <= set(planner.PLAN_QUERY_TYPES)
    for query_type in types:
        assert sum(q.scored for q in queries if q.plan_query_type == query_type) >= 15


class FakeDense:
    def __init__(self, matrix):
        self.matrix = matrix


def make_retriever(monkeypatch):
    rows = [
        {"model_id": "org/alpha", "source_pool": "core", "task": {"primary": "translation"},
         "filter_metadata": {"korean_verified": True}, "embedding_text": "alpha translation korean english"},
        {"model_id": "org/beta", "source_pool": "core", "task": {"primary": "translation"},
         "filter_metadata": {"korean_verified": True}, "embedding_text": "beta summarization"},
        {"model_id": "org/gamma", "source_pool": "core", "task": {"primary": "summarization"},
         "filter_metadata": {"korean_verified": True}, "embedding_text": "gamma translation"},
    ]
    matrix = np.array([[1.0, 0.0], [0.0, 1.0], [0.7, 0.7]], dtype=np.float32)
    vectors = {"alpha": np.array([1.0, 0.0], dtype=np.float32), "hypothetical": np.array([0.0, 1.0], dtype=np.float32)}
    monkeypatch.setattr(dense, "encode", lambda texts, **_: np.stack([vectors.get(texts[0].split()[0], np.array([0.6, 0.8], dtype=np.float32))]))
    return pipeline.Retriever(rows=rows, dense_index=FakeDense(matrix))


def test_pipeline_applies_hard_filter_and_fusion(monkeypatch):
    retriever = make_retriever(monkeypatch)
    plan = planner.RetrievalPlan(query_type="t", hard_filters={"tasks": ["translation"], "korean_required": True})
    result = retriever.run("alpha translation", plan)
    assert set(result.ranked) == {"org/alpha", "org/beta"}  # gamma fails the task filter
    assert result.ranked[0] == "org/alpha"
    assert result.eligible_count == 2
    assert result.latency_ms["total"] >= 0


def test_pipeline_hyde_replaces_dense_query_only(monkeypatch):
    retriever = make_retriever(monkeypatch)
    monkeypatch.setattr(
        pre_retrieval, "transform",
        lambda strategy, text, model=None: pre_retrieval.Transform(strategy, ["hypothetical card"], 1500.0, True),
    )
    plan = planner.with_strategies(planner.RetrievalPlan(query_type="t", hard_filters={"tasks": ["translation"]}), ("hyde",))
    result = retriever.run("alpha translation", plan)
    assert result.dense_queries == ["hypothetical card"]
    assert result.sparse_queries == ["alpha translation"]
    assert result.latency_ms["pre_retrieval"] == 1500.0


def test_name_lookup_pins_named_models(monkeypatch):
    retriever = make_retriever(monkeypatch)
    rows = retriever.rows + [
        {"model_id": "mirror/beta", "source_pool": "core", "task": {"primary": "translation"},
         "filter_metadata": {"korean_verified": True}, "embedding_text": "beta copy", "popularity": {"current": {"downloads": 5}}},
        {"model_id": "org/delta-2505", "source_pool": "core", "task": {"primary": "translation"},
         "filter_metadata": {"korean_verified": True}, "embedding_text": "delta"},
    ]
    rows[1] = {**rows[1], "popularity": {"current": {"downloads": 100}}}
    matrix = np.array([[1.0, 0.0], [0.0, 1.0], [0.7, 0.7], [0.0, 1.0], [0.5, 0.5]], dtype=np.float32)
    retriever = pipeline.Retriever(rows=rows, dense_index=FakeDense(matrix))
    plan = planner.RetrievalPlan(query_type="model_comparison", hard_filters={"tasks": ["translation"]}, use_name_lookup=True)
    result = retriever.run("delta랑 beta 중 뭐가 나아? gamma도", plan)
    # Prefix match for delta, most downloaded copy for beta; gamma fails the hard filter.
    assert result.ranked[:2] == ["org/delta-2505", "org/beta"]
    assert "org/gamma" not in result.ranked
    assert plan.label() == "Name Lookup"


def test_dense_build_reuses_unchanged_documents(tmp_path, monkeypatch):
    monkeypatch.setattr(dense, "VECTORS_PATH", tmp_path / "v.npy")
    monkeypatch.setattr(dense, "MANIFEST_PATH", tmp_path / "m.json")
    monkeypatch.setattr(dense, "CHECKPOINT_DIR", tmp_path / "ckpt")
    encoded = []

    def fake_encode(texts, **_):
        encoded.extend(texts)
        return np.array([[float(len(text)), 1.0] for text in texts], dtype=np.float32)

    monkeypatch.setattr(dense, "encode", fake_encode)
    rows = [{"model_id": f"org/m{i}", "embedding_text": f"text {i}"} for i in range(3)]
    monkeypatch.setattr(dense, "load_rows", lambda: rows)
    dense.build()
    assert len(encoded) == 3
    # Insert a new model in the middle and edit one: only those two are encoded.
    rows[:] = [rows[0], {"model_id": "org/new", "embedding_text": "brand new"}, rows[1],
               {"model_id": "org/m2", "embedding_text": "text 2 edited"}]
    encoded.clear()
    dense.build()
    assert encoded == ["brand new", "text 2 edited"]
    manifest = json.loads((tmp_path / "m.json").read_text(encoding="utf-8"))
    assert manifest["model_ids"] == ["org/m0", "org/new", "org/m1", "org/m2"]
    assert manifest["reused_docs"] == 2
    assert np.load(tmp_path / "v.npy")[1, 0] == len("brand new")


def test_empty_eligible_returns_no_candidates(monkeypatch):
    retriever = make_retriever(monkeypatch)
    result = retriever.run("anything", planner.RetrievalPlan(query_type="abstention", hard_filters={"tasks": ["question-answering"]}))
    assert result.ranked == [] and result.eligible_count == 0


def test_pre_retrieval_cache_round_trip(tmp_path, monkeypatch):
    monkeypatch.setattr(pre_retrieval, "CACHE_DIR", tmp_path)
    calls = []
    monkeypatch.setattr(pre_retrieval, "_call_llm", lambda s, t, m: calls.append(t) or {"sub_queries": ["a", " ", "b"]})
    first = pre_retrieval.transform("decomposition", "질의", model="m")
    second = pre_retrieval.transform("decomposition", "질의", model="m")
    assert first.outputs == second.outputs == ["a", "b"]
    assert (first.cached, second.cached) == (False, True)
    assert len(calls) == 1


def test_fast_bm25_matches_fielded_bm25():
    from retrieval_lab import corpus

    rows = [
        {"model_id": f"org/m{i}", "task": {"primary": task}, "embedding_text": text,
         "filter_metadata": {"translation_pairs": pairs, "language_codes": ["ko", "en"]}}
        for i, (task, text, pairs) in enumerate([
            ("translation", "korean english translation model ko-en", ["ko-en"]),
            ("summarization", "korean news summarization kobart", []),
            ("translation", "english to korean translator opus-mt", ["en-ko"]),
        ])
    ]
    fast = corpus.FastBM25(rows)
    for text in ("영어를 한국어로 번역", "kobart 요약", "nothing matches"):
        scores = fast.score_all(text)
        for index, row in enumerate(rows):
            assert scores[index] == pytest.approx(fast.base.score(row, {"text": text}), abs=1e-12)
