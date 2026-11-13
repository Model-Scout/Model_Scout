import importlib.util
from pathlib import Path

import pytest

AI = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("eval_recommendations", AI / "22_eval_recommendations.py")
ev = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ev)


def test_recall_uses_all_relevant_and_grade2_is_separate():
    relevant = {f"r{i}": 1 for i in range(20)} | {"a": 2}
    top = ["x", "a"] + [f"r{i}" for i in range(8)]  # 9 hits, first grade-2 at rank 2
    p, r, mrr, _, p2, mrr2 = ev._metrics(top, relevant, relevant)
    assert (p, mrr, p2, mrr2) == (0.9, 1 / 2, 0.1, 1 / 2)
    assert r == pytest.approx(9 / 21)  # old hits/min(10, n) gave 0.9


def test_only_alternatives_score_zero_on_grade2():
    grades = {"b": 1}
    assert ev._metrics(["b"], grades, grades)[4:] == (0.0, 0.0)


def test_cross_listed_copies_count_once():
    alias = {"a": {"a", "a2"}, "a2": {"a", "a2"}}
    assert ev._distinct_relevant({"a": 1, "a2": 2, "b": 1}, alias) == {"a": 2, "b": 1}
