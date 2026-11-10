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


def item(result, evidence="카드 근거", source="card"):
    return {"result": result, "evidence": evidence, "source": source}


def j(rid="p1|a", score="1", reason="", note="근거", status="not_needed", items=None, pending=None, kind="llm_first_pass"):
    return {"review_id": rid, "score": score, "reason": reason, "note": note, "judgment_kind": kind,
            "verification": {"status": status, "items": items or {}, "pending": pending or []}}


def violations_of(judgment, checks):
    return [m for _, m in rb.validate([judgment], {judgment["review_id"]: checks})[0]]


# ---------------------------------------------------------------- 명시적 필수 조건


@pytest.mark.parametrize("key", ["region", "district", "commercial", "kogl_type1_only", "delivery", "language", "period", "spatial_unit"])
@pytest.mark.parametrize("score", ["1", "2"])
def test_every_unmet_explicit_condition_blocks_a_positive_score(key, score):
    assert any(f"필수 조건 '{key}' 불충족" in m for m in violations_of(j(score=score), sug(**{key: "불충족"})))


def test_unmet_condition_can_only_be_overturned_by_a_confirmed_record():
    overturned = j(score="1", status="confirmed", items={"region": item("충족", "필드 '구'가 인천 연수구")})
    assert violations_of(overturned, sug(region="불충족")) == []


# ---------------------------------------------------------------- 미확인 조건의 확인 기록


def test_unknown_condition_needs_a_structured_confirmation_for_a_positive_score():
    assert any("미확인 조건 'realtime'" in m for m in violations_of(j(score="2"), sug(realtime="미확인")))
    ok = j(score="2", status="confirmed", items={"realtime": item("충족", "필드 '현재 주차가능면수'")})
    assert violations_of(ok, sug(realtime="미확인")) == []


def test_confirmation_must_be_complete_and_marked_confirmed():
    half = j(score="1", status="not_needed", items={"realtime": item("충족")})
    assert any("미확인 조건 'realtime'" in m for m in violations_of(half, sug(realtime="미확인")))
    no_evidence = j(score="1", status="confirmed", items={"realtime": {"result": "충족", "evidence": "", "source": "card"}})
    assert any("evidence" in m for m in violations_of(no_evidence, sug(realtime="미확인")))


def test_zero_for_an_unknown_condition_needs_an_unmet_record():
    zero = j(score="0", reason="wrong_delivery", note="월별 평균")
    assert any("불충족 확인 기록 없음" in m for m in violations_of(zero, sug(realtime="미확인")))
    ok = {**zero, "verification": {"status": "confirmed", "items": {"realtime": item("불충족", "제목 '월별 평균'")}, "pending": []}}
    assert violations_of(ok, sug(realtime="미확인")) == []
    off_topic = j(score="0", reason="off_topic", note="무관")  # 미확인 조건과 무관한 0점은 기록 불필요
    assert violations_of(off_topic, sug(realtime="미확인")) == []


def test_zero_already_carried_by_an_unmet_condition_needs_no_other_record():
    # API 필수인데 CSV만 있음: 실시간이 미확인이어도 wrong_delivery는 제공 방식 불충족으로 충분
    zero = j(score="0", reason="wrong_delivery", note="CSV만 제공")
    assert violations_of(zero, sug(delivery="불충족", realtime="미확인")) == []


@pytest.mark.parametrize("text, region, warned", [
    ("주차장 위치를 찾아주는 앱", None, True),       # 범위를 말하지 않음: 지역 한정으로 감점하면 경고
    ("전국 CCTV 설치 위치가 필요해", None, False),   # 질문이 범위를 명시
    ("인천 어린이 보호구역", "인천", False),         # 지역 조건이 있음
])
def test_scope_the_question_never_stated_is_flagged(text, region, warned):
    judged = j("p1|a", "1", status="confirmed", items={"region_scope": item("부분", "대전만")})
    queries = {"p1": {"query": text, "conditions": {"region": region}, "expected_behavior": "recommend"}}
    _, warnings = rb.validate([judged], {"p1|a": sug(region_scope="목적 판단")}, queries)
    assert any(w[0] == "unstated_scope:p1|a" for w in warnings) == warned


def test_queue_takes_answers_related_zeros_holds_and_revisions():
    suggestions = {"p1|a": {"topic": {"full": [], "partial": []}}, "p1|b": {"topic": {"full": ["주차장"], "partial": []}},
                   "p1|c": {"topic": {"full": [], "partial": []}}, "p1|d": {"topic": {}}, "p1|e": {"topic": {}}}
    judgments = [j("p1|a", "0", reason="off_topic"), j("p1|b", "0", reason="off_topic"), j("p1|c", "2"),
                 j("p1|d", "?"), j("p1|e", "0", reason="wrong_region")]
    queue = {q["review_id"]: q["queue_reasons"] for q in rb.review_queue(judgments, suggestions, revised={"p1|c"})}
    assert "p1|a" not in queue  # 주제 단어도 없는 off_topic
    assert queue == {"p1|b": ["related_topic_zero"], "p1|c": ["positive", "revised"],
                     "p1|d": ["pending_official_check"], "p1|e": ["condition_zero"]}


def test_consistency_compares_recorded_findings_and_skips_off_topic():
    same = {"region_scope": item("부분", "경기만"), "aspects": item("부분", "일부")}
    differs = {"region_scope": item("충족", "전국"), "aspects": item("충족", "전부")}
    suggestions = {f"p1|{x}": sug(region_scope="목적 판단") for x in "abcd"}
    judgments = [j("p1|a", "1", status="confirmed", items=same), j("p1|b", "2", status="confirmed", items=differs),
                 j("p1|c", "0", reason="off_topic", note="무관")]
    assert not [w for w in rb.validate(judgments, suggestions)[1] if w[0].startswith("inconsistent")]
    judgments.append(j("p1|d", "2", status="confirmed", items=same))  # 같은 기록인데 점수가 다름
    assert [w for w in rb.validate(judgments, suggestions)[1] if w[0].startswith("inconsistent")]


@pytest.mark.parametrize("note", ["정류소 좌표는 원문 확인 권장", "원문 확인 필요", "추가 확인 예정"])
def test_open_checking_text_does_not_pass_a_settled_score(note):
    settled = j(score="2", note=note, status="confirmed", items={"region": item("충족")})
    assert any("미결 확인 문구" in m for m in violations_of(settled, sug(region="충족")))


def test_hold_must_list_what_is_pending_and_settled_scores_must_not():
    assert any("보류인데" in m for m in violations_of(j(score="?", note="모름"), sug()))
    assert violations_of(j(score="?", note="모름", status="pending", pending=["좌표 항목"]), sug()) == []
    assert any("미결 항목" in m for m in violations_of(j(score="1", pending=["좌표"]), sug()))


# ---------------------------------------------------------------- 기타 규칙


@pytest.mark.parametrize("judgment, message", [
    (j(note=""), "부분 적합 내용"),
    (j(note="정보 부족으로 판단 불가"), "정보 부족을 1점"),
    (j(score="0", reason="nope"), "0점 사유"),
    (j(score="3"), "점수"),
    (j(kind="codex"), "judgment_kind"),
])
def test_other_criteria(judgment, message):
    assert any(message in m for m in violations_of(judgment, sug()))


def test_warnings_have_ids_and_cover_purpose_inconsistency_and_abstention():
    judgments = [j("p1|a", "2", note="주제 일치"), j("p1|b", "1"), j("p9|z", "1", note="대전 한정 일부")]
    suggestions = {"p1|a": sug(region_scope="목적 판단"), "p1|b": sug(region_scope="목적 판단"), "p9|z": sug()}
    queries = {"p9": {"expected_behavior": "abstain"}}
    _, warnings = rb.validate(judgments, suggestions, queries)
    ids = [w[0] for w in warnings]
    assert "purpose_basis:p1|a" in ids and "abstain_relevant:p9|z" in ids and any(i.startswith("inconsistent:p1:") for i in ids)


# ---------------------------------------------------------------- 라벨 발행


def golden():
    return [{"query_id": "p1", "expected_behavior": "recommend", "relevant": {"a": 2, "b": 1}, "must_exclude": [],
             "judged_irrelevant": ["c"], "unjudged": ["d"], "answer_grade": "full", "evaluable": True},
            {"query_id": "p9", "expected_behavior": "abstain", "relevant": {}, "must_exclude": [],
             "judged_irrelevant": [], "unjudged": ["z"], "answer_grade": None, "evaluable": False}]


def test_labels_take_reviewed_judgments_and_record_who_judged():
    before = json.dumps(golden())
    out = {l["query_id"]: l for l in rb.build_labels(
        [j("p1|d", "2"), j("p1|b", "0", reason="wrong_region"), j("p1|e", "?"), j("p9|z", "0", reason="off_topic")],
        golden())}
    assert json.dumps(golden()) == before  # 원본 라벨 객체는 그대로
    assert out["p1"]["relevant"] == {"a": 2, "d": 2} and out["p1"]["must_exclude"] == ["b"]
    assert out["p1"]["unjudged"] == ["e"] and out["p1"]["judged_irrelevant"] == ["c"]
    assert out["p9"]["unjudged"] == [] and out["p9"]["evaluable"] is True
    assert out["p1"]["review_provenance"]["d"]["judgment_kind"] == "llm_first_pass"
    assert "a" not in out["p1"]["review_provenance"]  # 검토하지 않은 기존 라벨


def run_labels(tmp_path, monkeypatch, judgments, checks, resolutions=None, out=None):
    prep = tmp_path / "prep"
    prep.mkdir(exist_ok=True)
    (prep / "review_suggestions.jsonl").write_text(
        "".join(json.dumps({"review_id": x["review_id"], **checks}) + "\n" for x in judgments), encoding="utf-8")
    monkeypatch.setattr(rb, "PREP", prep)
    monkeypatch.setattr(rb, "GOLDEN", tmp_path / "golden.jsonl")
    rb.GOLDEN.write_text("".join(json.dumps(g) + "\n" for g in golden()), encoding="utf-8")
    src = tmp_path / "judgments.jsonl"
    src.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in judgments), encoding="utf-8")
    argv = ["rb", "labels", str(src), "--out", str(out or tmp_path / "out.jsonl")]
    if resolutions is not None:
        (tmp_path / "res.json").write_text(json.dumps(resolutions, ensure_ascii=False), encoding="utf-8")
        argv += ["--resolutions", str(tmp_path / "res.json")]
    monkeypatch.setattr(sys, "argv", argv)
    rb.main()


def test_labels_refuse_violations(tmp_path, monkeypatch):
    with pytest.raises(SystemExit, match="violations"):
        run_labels(tmp_path, monkeypatch, [j("p1|a", "1")], sug(delivery="불충족"))


def test_labels_wait_for_every_warning_to_have_a_resolution(tmp_path, monkeypatch):
    judged = [j("p1|a", "2", note="주제 일치")]
    with pytest.raises(SystemExit, match="unresolved warnings"):
        run_labels(tmp_path, monkeypatch, judged, sug(region_scope="목적 판단"))
    with pytest.raises(SystemExit, match="unresolved warnings"):
        run_labels(tmp_path, monkeypatch, judged, sug(region_scope="목적 판단"), {"purpose_basis:p1|a": " "})
    run_labels(tmp_path, monkeypatch, judged, sug(region_scope="목적 판단"), {"purpose_basis:p1|a": "지역 서비스 질문이라 서울 데이터로 충분"})
    meta = json.loads((tmp_path / "out.meta.json").read_text(encoding="utf-8"))
    assert meta["warnings_resolved"] == {"purpose_basis:p1|a": "지역 서비스 질문이라 서울 데이터로 충분"}
    assert meta["judgment_kinds"] == {"llm_first_pass": 1}


def test_labels_never_overwrite_the_original_file(tmp_path, monkeypatch):
    with pytest.raises(SystemExit, match="refusing"):
        run_labels(tmp_path, monkeypatch, [j("p1|a", "0", reason="off_topic")], sug(), out=tmp_path / "golden.jsonl")


@pytest.mark.parametrize("target", ["base.jsonl", "judgments.jsonl", "items.jsonl", "base.meta.json", "judgments.meta.json"])
def test_labels_never_overwrite_their_base_or_judgments(tmp_path, monkeypatch, target):
    base = tmp_path / "base.jsonl"
    base.write_text("".join(json.dumps(g) + "\n" for g in golden()), encoding="utf-8")
    run_labels(tmp_path, monkeypatch, [j("p1|a", "0", reason="off_topic")], sug())  # sets up prep, golden, judgments
    before = {p: p.read_bytes() for p in (base, tmp_path / "judgments.jsonl")}
    monkeypatch.setattr(sys, "argv", ["rb", "labels", str(tmp_path / "judgments.jsonl"), "--base", str(base),
                                      "--out", str(tmp_path / target)])
    with pytest.raises(SystemExit, match="refusing"):
        rb.main()
    assert {p: p.read_bytes() for p in before} == before


def test_batch_must_cover_the_expected_rows_exactly_once():
    rows = [j("p1|a", "0", reason="off_topic"), j("p1|b", "0", reason="off_topic")]
    assert rb.coverage(rows, ["p1|a", "p1|b"]) == []
    assert rb.coverage(rows + [rows[0]], ["p1|a", "p1|b"]) == [("p1|a", "판정이 2번 있음 (중복)")]
    assert rb.coverage(rows[:1], ["p1|a", "p1|b"]) == [("p1|b", "배치 후보인데 판정이 없음 (누락)")]
    assert rb.coverage(rows, ["p1|a"]) == [("p1|b", "배치 후보 목록에 없는 판정")]
    assert rb.coverage(rows + [rows[1]], None) == [("p1|b", "판정이 2번 있음 (중복)")]  # no list: duplicates still caught


def test_labels_refuse_a_batch_with_a_missing_row(tmp_path, monkeypatch):
    (tmp_path / "items.jsonl").write_text(json.dumps({"review_id": "p1|a"}) + "\n" + json.dumps({"review_id": "p1|b"}) + "\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="violations"):
        run_labels(tmp_path, monkeypatch, [j("p1|a", "0", reason="off_topic")], sug())


def test_a_row_without_automatic_checks_is_a_violation_not_a_crash():
    violations, _ = rb.validate([j("p9|zzz", "0", reason="off_topic")], sug())
    assert violations == [("p9|zzz", "자동 검사(review_suggestions)에 없는 후보 — --suggestions를 확인")]
