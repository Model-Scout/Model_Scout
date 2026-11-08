"""공공데이터 우선 검토 배치(review_batch.py) 회귀 테스트. 외부 호출 없음.

    python -m pytest -q test/test_review_batch.py
"""

import importlib.util
import json
import sys
from pathlib import Path

import pytest

AI = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("review_batch", AI / "test" / "public_data" / "corpus_v2" / "review_batch.py")
rb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rb)


def ctx(rid, sources, discovery=None):
    return {"review_id": rid, "review_sources": sources, "discovery": discovery}


def test_batch_takes_every_hold_and_high_row_and_only_top5_new_rows():
    context = [
        ctx("p1|a", ["existing_hold"]),  # 검색에 안 나와도 포함
        ctx("p1|b", ["high_review"], {"pool_terms": 9}),
        ctx("p1|c", ["new_unjudged"], {"question_only": 5}),
        ctx("p1|d", ["new_unjudged"], {"question_only": 6, "pool_terms": 2}),
        ctx("p1|e", ["new_unjudged"], {"question_only": 6}),
    ]
    assert rb.select(context) == {"p1|a": ["existing_hold"], "p1|b": ["high_review"],
                                  "p1|c": ["new_top5"], "p1|d": ["new_top5"]}


def test_pilot_is_fixed_and_spread_over_sources_and_conditions():
    chosen = {f"p{i}|d": [src] for i, src in enumerate(["existing_hold"] * 10 + ["high_review"] * 10 + ["new_top5"] * 20)}
    kinds = ["delivery", "realtime", "region", "region_scope"]
    suggestions = {rid: {"checks": {kinds[i % 4]: {}}} for i, rid in enumerate(chosen)}
    first = rb.pilot(chosen, suggestions, size=12)
    assert first == rb.pilot(chosen, suggestions, size=12) and len(first) == 12
    assert {chosen[r][0] for r in first} == {"existing_hold", "high_review", "new_top5"}
    assert len({next(iter(suggestions[r]["checks"])) for r in first}) == 4


def sug(**statuses):
    return {"checks": {k: {"status": v} for k, v in statuses.items()}}


def j(rid, score, reason="", note="근거"):
    return {"review_id": rid, "score": score, "reason": reason, "note": note}


@pytest.mark.parametrize("judgment, checks, message", [
    (j("p1|a", "1"), sug(delivery="불충족"), "delivery 필수 조건 불충족"),
    (j("p026|a", "2"), sug(kogl_type1_only="불충족"), "kogl_type1_only 필수 조건 불충족"),
    (j("p1|a", "1"), sug(region="불충족"), "다른 지역"),
    (j("p1|a", "1", note=""), sug(), "부분 적합 내용"),
    (j("p1|a", "1", note="정보 부족으로 판단 불가"), sug(), "정보 부족을 1점"),
    (j("p1|a", "0", reason="nope"), sug(), "0점 사유"),
    (j("p1|a", "3"), sug(), "점수"),
])
def test_criteria_violations(judgment, checks, message):
    violations, _ = rb.validate([judgment], {judgment["review_id"]: checks})
    assert any(message in m for _, m in violations)


def test_partial_note_that_mentions_missing_information_is_allowed():
    violations, _ = rb.validate([j("p1|a", "1", note="경기 한정 일부만 제공, 요금은 확인 불가")], {"p1|a": sug()})
    assert violations == []


def test_warnings_for_unconfirmed_two_and_inconsistent_scores():
    judgments = [j("p1|a", "2", note="주제 일치"), j("p1|b", "1"), j("p2|a", "?", note="")]
    suggestions = {"p1|a": sug(region="미확인"), "p1|b": sug(region="미확인"), "p2|a": sug()}
    _, warnings = rb.validate(judgments, suggestions)
    text = " ".join(m for _, m in warnings)
    assert "원문 확인 근거" in text and "점수가 다름" in text and "보류인데" in text


def golden():
    return [{"query_id": "p1", "expected_behavior": "recommend", "relevant": {"a": 2, "b": 1}, "must_exclude": [],
             "judged_irrelevant": ["c"], "unjudged": ["d"], "answer_grade": "full", "evaluable": True},
            {"query_id": "p9", "expected_behavior": "abstain", "relevant": {}, "must_exclude": [],
             "judged_irrelevant": [], "unjudged": ["z"], "answer_grade": None, "evaluable": False}]


def test_labels_take_reviewed_judgments_and_leave_the_rest():
    before = json.dumps(golden())
    out = {l["query_id"]: l for l in rb.build_labels(
        [j("p1|d", "2"), j("p1|b", "0", reason="wrong_region"), j("p1|e", "?"), j("p9|z", "0", reason="off_topic")],
        golden())}
    assert json.dumps(golden()) == before  # 원본 라벨 객체는 그대로
    assert out["p1"]["relevant"] == {"a": 2, "d": 2} and out["p1"]["must_exclude"] == ["b"]
    assert out["p1"]["unjudged"] == ["e"] and out["p1"]["judged_irrelevant"] == ["c"]
    assert out["p9"]["unjudged"] == [] and out["p9"]["evaluable"] is True


def test_labels_command_refuses_violations_and_the_original_file(tmp_path, monkeypatch):
    prep = tmp_path / "prep"
    prep.mkdir()
    (prep / "review_suggestions.jsonl").write_text(json.dumps({"review_id": "p1|a", **sug(delivery="불충족")}) + "\n", encoding="utf-8")
    monkeypatch.setattr(rb, "PREP", prep)
    bad = tmp_path / "bad.jsonl"
    bad.write_text(json.dumps(j("p1|a", "1")) + "\n", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["rb", "labels", str(bad), "--out", str(tmp_path / "out.jsonl")])
    with pytest.raises(SystemExit, match="violations"):
        rb.main()
    ok = tmp_path / "ok.jsonl"
    ok.write_text(json.dumps(j("p1|a", "0", reason="wrong_delivery")) + "\n", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["rb", "labels", str(ok), "--out", str(rb.GOLDEN)])
    with pytest.raises(SystemExit, match="refusing"):
        rb.main()
