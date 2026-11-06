"""V2 골든셋 후보 스캔의 경계·출처 판정 회귀 테스트."""

from pathlib import Path
import sys


TOOLS = Path(__file__).resolve().parent / "golden" / "v2" / "tools"
sys.path.insert(0, str(TOOLS))

from scan import Rule, scan_row  # noqa: E402


def _row(results=None, *, semantic=None, model_id="org/model", filter_metadata=None):
    return {
        "model_id": model_id,
        "filter_metadata": filter_metadata or {},
        "semantic_metadata": semantic or {},
        "benchmark_metadata": {"results": results or []},
        "evidence_spans": {},
    }


MMLU_RULE = Rule(
    must_any=("mmlu",),
    grade_2_any=("mmlu",),
    weak_any=("mmlu-pro", "mmmlu", "kmmlu"),
    reliable_stages=(4,),
    benchmark_terms=("mmlu",),
    benchmark_exclude=("mmlu-pro", "mmlu pro", "mmmlu", "kmmlu"),
)


def test_safe_exact_benchmark_is_a_grade_two_proposal():
    hit = scan_row(_row([{"dataset": "MMLU", "score": 61.2, "ranking_eligible": True}]), MMLU_RULE)
    assert hit.pile == "flag"
    assert hit.proposal == 2
    assert hit.stages == {4: ["mmlu"]}


def test_benchmark_variant_is_not_mistaken_for_the_exact_benchmark():
    hit = scan_row(_row([{"dataset": "MMLU-Pro", "score": 55.0, "ranking_eligible": True}]), MMLU_RULE)
    assert hit.pile == "unsure"
    assert hit.proposal is None


def test_unsafe_benchmark_result_needs_human_review_not_auto_grade_two():
    hit = scan_row(
        _row([{"dataset": "MMLU", "score": 61.2, "ranking_eligible": False}]),
        MMLU_RULE,
    )
    assert hit.pile == "unsure"
    assert hit.proposal is None


def test_unsure_reason_keeps_exact_and_adjacent_benchmark_evidence():
    rule = Rule(
        must_any=("gpqa",),
        grade_2_any=("gpqa",),
        weak_any=("mmlu-pro",),
        reliable_stages=(4,),
        benchmark_terms=("gpqa",),
    )
    hit = scan_row(
        _row([{"dataset": "GPQA MMLU-Pro", "score": 41.1, "ranking_eligible": False}]),
        rule,
    )
    assert hit.pile == "unsure"
    assert "gpqa" in hit.reason
    assert "mmlu-pro" in hit.reason


def test_korean_sts_does_not_accept_generic_stsbenchmark():
    rule = Rule(
        must_any=("korsts", "klue-sts"),
        grade_2_any=("korsts", "klue-sts"),
        weak_any=("stsb", "sts-b", "stsbenchmark"),
        reliable_stages=(4,),
        benchmark_terms=("korsts", "klue-sts"),
    )
    exact = scan_row(_row([{"dataset": "KorSTS", "score": 0.84}]), rule)
    generic = scan_row(_row([{"dataset": "MTEB STSBenchmark", "score": 84.0}]), rule)
    assert (exact.pile, exact.proposal) == ("flag", 2)
    assert (generic.pile, generic.proposal) == ("unsure", None)


def test_benchmark_alias_uses_token_boundary():
    # MMMLU는 MMLU의 오타/변형으로 보이지만, 원본 MMLU 질의의 자동 정답은 아니다.
    hit = scan_row(_row([{"dataset": "MMMLU", "score": 55.0}]), MMLU_RULE)
    assert hit.pile == "unsure"
    assert hit.proposal is None


COMPARISON_RULE = Rule(
    must_any=("bge-m3", "multilingual-e5"),
    comparison_groups={
        "BGE-M3": ("bge-m3",),
        "multilingual-E5": ("multilingual-e5",),
    },
)


def test_comparison_ignores_readme_mentions_of_another_model_family():
    hit = scan_row(
        _row(
            model_id="omai-research/milco-300m",
            semantic={"benchmarks": [{"text": "outperforms BGE-M3"}]},
        ),
        COMPARISON_RULE,
    )
    assert hit.pile == "reject"
    assert hit.proposal is None


def test_comparison_exact_model_id_is_a_grouped_grade_two_candidate():
    hit = scan_row(
        _row(
            model_id="intfloat/multilingual-e5-large",
            filter_metadata={
                "canonical_model_id": "intfloat/multilingual-e5-large",
                "is_variant": False,
            },
        ),
        COMPARISON_RULE,
    )
    assert (hit.pile, hit.proposal) == ("flag", 2)
    assert hit.comparison_groups == ("multilingual-E5",)


def test_comparison_canonical_only_variant_is_a_grade_one_candidate():
    hit = scan_row(
        _row(
            model_id="nlpai-lab/KoE5",
            filter_metadata={
                "canonical_model_id": "intfloat/multilingual-e5-large",
                "is_variant": True,
            },
        ),
        COMPARISON_RULE,
    )
    assert (hit.pile, hit.proposal) == ("flag", 1)
    assert hit.comparison_groups == ("multilingual-E5",)


def test_comparison_conversion_marker_is_a_grade_one_candidate_even_if_metadata_misses_it():
    hit = scan_row(
        _row(
            model_id="OpenNMT/nllb-200-distilled-1.3B-ct2-int8",
            filter_metadata={
                "canonical_model_id": "OpenNMT/nllb-200-distilled-1.3B-ct2-int8",
                "is_variant": False,
            },
        ),
        Rule(must_any=("nllb",), comparison_groups={"NLLB": ("nllb",)}),
    )
    assert (hit.pile, hit.proposal) == ("flag", 1)
    assert "변환·양자화 표지" in hit.reason


def test_comparison_can_restrict_a_named_group_to_grade_one():
    rule = Rule(
        must_any=("koelectra", "mdeberta"),
        comparison_groups={"KoELECTRA": ("koelectra",), "mDeBERTa": ("mdeberta",)},
        comparison_grade_2_groups=("KoELECTRA",),
    )
    hit = scan_row(
        _row(
            model_id="org/mdeberta-v3-base-squad2",
            filter_metadata={"canonical_model_id": "org/mdeberta-v3-base-squad2", "is_variant": False},
        ),
        rule,
    )
    assert (hit.pile, hit.proposal) == ("flag", 1)
    assert hit.comparison_groups == ("mDeBERTa",)
