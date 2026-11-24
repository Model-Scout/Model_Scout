"""검색 측정 도구(test/model_retrieval/tools/)의 규칙을 확인한다.

정답 집합이 완전하려면 세 가지가 깨지지 않아야 한다. ① 하드 필터가 운영 SQL 과 같은
unknown 의미를 갖는다 ② eligible 전수가 네 분류 중 하나에 정확히 들어간다 ③ 사람이 말하지
않은 조건이 conditions 에 들어가지 않는다. 기준 코퍼스 없이 합성 행으로 검사한다.

골든셋 자체의 불변식(질의 수, ID 중복, 조건 근거, 비교 양쪽 정답, eligible 밖 정답)은
실제 240문항을 상대로 verify_goldenset.py 가 본다. 여기서는 도구의 규칙만 본다.

    python test/test_retrieval_corpus.py
"""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "test" / "model_retrieval" / "tools"
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(ROOT))

sys.modules.pop("scan", None)  # test/golden/v2/tools/scan.py shares the name; a full run imports it first
import corpus  # noqa: E402
import scan  # noqa: E402

RUN = "11111111-1111-1111-1111-111111111111"


def row(model_id: str, **meta: Any) -> Dict[str, Any]:
    task = meta.pop("task", "text-generation")
    family = meta.pop("family", {})
    semantic = meta.pop("semantic", {})
    results = meta.pop("results", [])
    base = {"korean_verified": True, "parameter_count_billion": 1.0, "context_length": 4096, "license": "apache-2.0",
            "commercial_status": "permitted", "gated": False, "artifact_formats": ["safetensors"],
            "artifact_runnable_gib": 2.0, "canonical_model_id": model_id, "is_variant": False, "languages": ["ko"]}
    base.update(meta)
    return {"model_id": model_id, "source_pool": "core", "active": True, "last_seen_run": RUN,
            "task": {"primary": task, "matched": [task]}, "filter_metadata": base, "family": family,
            "technical_metadata": {}, "semantic_metadata": semantic, "benchmark_metadata": {"results": results},
            "source_provenance": {}, "evidence_spans": {"parents": []}}


def recommend(qtype: str, rule: Dict[str, Any], conditions: Dict[str, Any] | None = None, **extra: Any) -> Dict[str, Any]:
    return {"query_id": "t01", "query_type": qtype, "query": "질문", "expected_behavior": "recommend",
            "conditions": conditions or {}, "conditions_fidelity": {}, "relevance_rule": rule, **extra}


# --------------------------------------------------------------------------- 하드 필터

def test_hard_filter_unknown_semantics_match_sql():
    unknown = row("a/unknown", parameter_count_billion=None, context_length=None, artifact_runnable_gib=None,
                  commercial_status="unknown", gated=None)
    # 수치 상·하한이 걸리면 값이 없는 모델은 탈락한다(SQL 의 NULL 비교)
    for cond in ({"max_parameters_billion": 3}, {"min_parameters_billion": 1}, {"min_context_length": 8192},
                 {"max_artifact_gib": 4}, {"commercial_status": ["permitted"]}, {"exclude_gated": True}):
        assert corpus.condition_failures(unknown, cond) == list(cond), cond
    # 조건이 없으면 값이 없어도 통과한다. unknown 을 permitted·false 로 바꿔 읽지 않는다
    assert corpus.hard_filter(unknown, {})
    assert corpus.hard_filter(unknown, {"tasks": []}), "tasks 가 비면 SQL 처럼 통과"
    assert not corpus.hard_filter(row("a/gated", gated="auto"), {"exclude_gated": True})
    assert not corpus.hard_filter(row("a/inactive") | {"active": False}, {})


def test_hard_filter_agrees_with_05_where_semantics_overlap():
    spec = importlib.util.spec_from_file_location("validate_retrieval_probe", ROOT / "05_validate_retrieval.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    rows = [row("a/1"), row("a/2", parameter_count_billion=None), row("a/3", commercial_status="unknown"),
            row("a/4", gated="manual"), row("a/5", artifact_formats=["gguf"], artifact_runnable_gib=None),
            row("a/6", task="translation", context_length=None),
            # 과거 결함 데이터의 "실측 0 GiB". 05 는 PR #52 이후 이것을 크기 미상으로 본다
            row("a/7", artifact_formats=["gguf"], artifact_runnable_gib=0.0)]
    conditions = [{"tasks": ["text-generation"], "max_parameters_billion": 3},
                  {"tasks": ["text-generation", "translation"], "min_context_length": 2048},
                  {"tasks": ["text-generation"], "commercial_status": ["permitted"], "exclude_gated": True},
                  {"tasks": ["text-generation"], "require_artifact": ["gguf"], "max_artifact_gib": 4}]
    for cond in conditions:
        for r in rows:
            ours = corpus.hard_filter(r, cond)
            theirs = module.hard_filter(r, {**cond, "pools": ["core", "low_popularity"]})[0]
            assert ours == theirs, (r["model_id"], cond, ours, theirs)


def test_zero_artifact_size_is_unknown_not_tiny():
    """0 GiB 는 '아주 작은 모델' 이 아니라 '크기를 모름' 이다. 과거 결함 데이터가 통과하면 안 된다."""
    zero = row("a/zero", artifact_runnable_gib=0.0)
    assert corpus.condition_failures(zero, {"max_artifact_gib": 4}) == ["max_artifact_gib"]
    assert not corpus.hard_filter(zero, {"max_artifact_gib": 4})
    # 음수도 마찬가지로 측정값이 아니다
    assert not corpus.hard_filter(row("a/neg", artifact_runnable_gib=-1.0), {"max_artifact_gib": 4})
    # 양수는 그대로 통과한다
    assert corpus.hard_filter(row("a/small", artifact_runnable_gib=0.004), {"max_artifact_gib": 4})
    # 크기 조건이 없으면 0 이어도 탈락시키지 않는다
    assert corpus.hard_filter(zero, {})


def test_unknown_exclusion_count():
    rows = [row("a/1", parameter_count_billion=None), row("a/2", parameter_count_billion=9.0), row("a/3")]
    assert corpus.unknown_exclusions(rows, {"max_parameters_billion": 3}) == 1


# --------------------------------------------------------------------------- 전수 분류

def test_every_eligible_model_gets_exactly_one_class():
    rows = [row("a/ko-sentiment", task="text-classification"),
            row("a/multilingual-sentiment", task="text-classification", languages=["ko", "en", "de", "fr"]),
            row("a/news-topic", task="text-classification", semantic={"use_cases": [{"text": "news topic"}]}),
            row("a/readme-only", task="text-classification")]
    rows[3]["evidence_spans"] = {"parents": [{"text": "This model does sentiment analysis of reviews."}]}
    scan.bind(rows)
    query = recommend("semantic_capability", {"grade_2": "x", "grade_1": "y", "grade_2_requires_korean_specific": True,
                                              "scan": {"must_any": ["sentiment"], "grade_2_any": ["sentiment"]}},
                      {"tasks": ["text-classification"]})
    result = scan.scan_query(query, rows)
    assert result["invariant_ok"] and sum(result["counts"].values()) == result["eligible_count"] == 4
    assert result["classes"]["proposed_grade_2"] == ["a/ko-sentiment"]
    assert result["classes"]["proposed_grade_1"] == ["a/multilingual-sentiment"]
    assert result["classes"]["unresolved_for_human"] == ["a/readme-only"]
    assert result["classes"]["auto_rejected"] == ["a/news-topic"]
    assert result["decisions"]["a/news-topic"]["reason"] == "no_supporting_evidence"


def test_negated_claim_is_not_evidence():
    r = row("a/general", semantic={"use_cases": [{"text": "It is not recommended for critical scenarios such as medical diagnosis."}]})
    scan.bind([r])
    query = recommend("semantic_capability", {"grade_2": "x", "grade_1": "y",
                                              "scan": {"must_any": [r"medical diagnosis"]}})
    assert scan.classify(r, query)["class"] == "auto_rejected"


def test_conversion_versus_finetune():
    original = row("org/Base-1B")
    gguf = row("someone/Base-1B-GGUF", canonical_model_id="org/Base-1B", is_variant=True)
    finetune = row("someone/Base-1B-ko-chat", canonical_model_id="org/Base-1B", is_variant=True)
    scan.bind([original, gguf, finetune])
    assert scan.is_conversion(gguf) and not scan.is_conversion(finetune) and not scan.is_conversion(original)
    rule = {"grade_2": "x", "grade_1": "y", "families": [{"name": "Base-1B", "id_regex": r"org/base-1b$|base-1b-gguf"}],
            "originals": [r"org/Base-1B"]}
    q = recommend("lexical_exact", rule)
    assert scan.classify(original, q)["class"] == "proposed_grade_2"
    assert scan.classify(gguf, q)["class"] == "proposed_grade_1"
    decision = scan.classify(finetune, q)
    assert decision["class"] == "auto_rejected" and decision["reason"] == "variant_mismatch", decision


def test_requested_format_makes_conversion_grade_2():
    gguf = row("someone/Base-1B-GGUF", artifact_formats=["gguf"], is_variant=True)
    scan.bind([gguf])
    rule = {"grade_2": "x", "grade_1": "y", "scan": {}}
    assert scan.classify(gguf, recommend("structured_constraint", rule))["class"] == "proposed_grade_1"
    assert scan.classify(gguf, recommend("structured_constraint", rule, {"require_artifact": ["gguf"]}))["class"] == "proposed_grade_2"


def test_benchmark_requires_same_dataset_and_metric():
    spec = {"dataset_regex": r"^kmmlu$", "metric_regex": r"^score$"}
    same = row("a/1", results=[{"dataset": "KMMLU", "metric": "score", "score": 50, "comparability": "safe_same_source"}])
    other_metric = row("a/2", results=[{"dataset": "KMMLU", "metric": "exact-match", "score": 50}])
    other_dataset = row("a/3", results=[{"dataset": "kmmlu (chat CoT)", "metric": "score", "score": 50}])
    none = row("a/4")
    assert scan.matching_results(same, spec)[0]
    assert scan.matching_results(other_metric, spec) == ([], "other_metric")
    assert scan.matching_results(other_dataset, spec) == ([], "other_benchmark_dataset")
    assert scan.matching_results(none, spec) == ([], "no_benchmark_results")


# --------------------------------------------------------------------------- abstention

def test_single_relaxation_and_near_miss():
    rows = [row("a/gguf-big", artifact_formats=["gguf"], parameter_count_billion=8.0),
            row("a/small-st", parameter_count_billion=0.5),
            row("a/gguf-mit", artifact_formats=["gguf"], parameter_count_billion=0.5, license="mit")]
    for i in range(6):
        rows.append(row(f"a/filler-{i}", artifact_formats=["gguf"], parameter_count_billion=0.4 + i, license="mit"))
        rows.append(row(f"a/apache-big-{i}", parameter_count_billion=7.0 + i))  # apache 이지만 GGUF·1B 둘 다 불충족
        rows.append(row(f"a/mit-small-{i}", parameter_count_billion=0.3, license="mit"))  # 1B 이하지만 GGUF·apache 불충족
    cond = {"require_artifact": ["gguf"], "max_parameters_billion": 1, "licenses": ["apache-2.0"]}
    assert not corpus.eligible(rows, cond)
    relax = scan.relaxations(rows, cond)
    assert relax["relaxed_candidate_counts"]["licenses"] == 2  # gguf-mit + filler-0
    assert relax["near_miss_by_condition"]["max_parameters_billion"] == ["a/gguf-big"]
    assert relax["near_miss_by_condition"]["require_artifact"] == ["a/small-st"]
    assert scan.extreme_reasons(rows, cond, relax) == []


def test_extreme_abstention_is_caught():
    rows = [row(f"a/{i}", parameter_count_billion=float(i + 1)) for i in range(200)]
    tiny = {"max_parameters_billion": 0.001}
    assert any("하위 1%" in r for r in scan.extreme_reasons(rows, tiny, scan.relaxations(rows, tiny)))
    contradiction = {"min_parameters_billion": 10, "max_parameters_billion": 5}
    assert any("직접 모순" in r for r in scan.extreme_reasons(rows, contradiction, scan.relaxations(rows, contradiction)))
    rare = {"licenses": ["wtfpl"], "max_parameters_billion": 50}
    assert any("비현실적" in r for r in scan.extreme_reasons(rows, rare, scan.relaxations(rows, rare)))


# --------------------------------------------------------------------------- 스냅샷

def _write_snapshot(tmp: Path, rows: List[Dict[str, Any]], **meta_override: Any) -> tuple:
    snap, meta_path = tmp / "corpus_snapshot.jsonl", tmp / "corpus_snapshot.meta.json"
    snap.write_text("".join(corpus.canonical_line(r) + "\n" for r in rows), encoding="utf-8")
    meta = {"sync_run_id": RUN, "active_row_count": len(rows), "corpus_schema_version": 1,
            "model_ids_sha256": corpus.model_ids_sha256(r["model_id"] for r in rows),
            "snapshot_sha256": corpus.file_sha256(snap)}
    meta.update(meta_override)
    meta_path.write_text(json.dumps(meta), encoding="utf-8")
    return snap, meta_path


def test_snapshot_mismatch_and_missing_fail_loudly():
    rows = [row("a/1"), row("a/2")]
    with tempfile.TemporaryDirectory() as tmp:
        snap, meta_path = _write_snapshot(Path(tmp), rows)
        assert len(corpus.load_corpus(snap, meta_path)) == 2
        for override in ({"snapshot_sha256": "0" * 64}, {"active_row_count": 3}, {"model_ids_sha256": "0" * 64},
                         {"sync_run_id": "other-run"}):
            corpus._CACHE.clear()
            snap, meta_path = _write_snapshot(Path(tmp), rows, **override)
            try:
                corpus.load_corpus(snap, meta_path)
            except corpus.CorpusError:
                continue
            raise AssertionError(f"불일치를 통과시켰다: {override}")
        snap.unlink()
        try:
            corpus.load_corpus(snap, meta_path)
        except corpus.CorpusError as exc:
            assert "dump_corpus.py" in str(exc)
        else:
            raise AssertionError("스냅샷이 없는데 통과했다")


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
