import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_hybrid_ranking_exposes_dense_and_sparse_components():
    retrieval = load_module("05_validate_retrieval.py", "recommendation_quality_retrieval")
    row = {
        "model_id": "org/model",
        "embedding_text": "한국어 문장 임베딩 sentence similarity",
        "embedding": [1.0, 0.0],
        "filter_metadata": {"korean_verified": True},
    }
    query = {
        "text": "한국어 문장 임베딩",
        "routing_hint": {
            "primary": "hybrid",
            "dense_bias": "medium",
            "sparse_bias": "medium",
        },
    }

    raw, adjusted, signal = retrieval.ranking_score(row, query, [1.0, 0.0])

    assert adjusted == raw
    assert signal["retrieval_route"] == "hybrid"
    assert 0.0 <= signal["dense_score"] <= 1.0
    assert 0.0 <= signal["sparse_score"] <= 1.0
    assert signal["dense_weight"] + signal["sparse_weight"] == 1.0


def test_supabase_rpc_params_preserve_query_constraints():
    retrieval = load_module("05_validate_retrieval.py", "recommendation_quality_rpc")
    params = retrieval.supabase_rpc_params(
        {
            "text": "한국어 문장 임베딩",
            "tasks": ["sentence-similarity"],
            "korean_required": True,
            "max_parameters_billion": 1.0,
            "min_context_length": 512,
            "require_known_parameters": True,
            "require_known_context": True,
            "pools": ["core"],
            "routing_hint": {
                "primary": "hybrid",
                "dense_bias": "medium",
                "sparse_bias": "medium",
            },
        },
        [0.1, 0.2],
        match_count=500,
    )

    assert params["pool_filter"] == "core"
    assert params["task_filters"] == ["sentence-similarity"]
    assert params["korean_required"] is True
    assert params["max_parameter_count_billion"] == 1.0
    assert params["require_known_context"] is True
    assert params["match_count"] == 100
    assert {"한국어", "ko", "kor"}.issubset(set(params["query_text"].split()))


def test_diversify_results_limits_same_author_and_canonical_duplicates():
    retrieval = load_module("05_validate_retrieval.py", "recommendation_quality_diversity")
    rows = [
        {
            "model_id": "same/one",
            "filter_metadata": {"canonical_model_id": "same/base"},
        },
        {
            "model_id": "same/two",
            "filter_metadata": {"canonical_model_id": "same/two"},
        },
        {
            "model_id": "same/three",
            "filter_metadata": {"canonical_model_id": "same/three"},
        },
        {
            "model_id": "other/model",
            "filter_metadata": {"canonical_model_id": "other/model"},
        },
    ]

    selected = retrieval.diversify_results(rows, limit=3, max_per_author=2)

    assert [row["model_id"] for row in selected] == [
        "same/one",
        "same/two",
        "other/model",
    ]


def test_empty_query_returns_safe_relaxation_suggestions():
    retrieval = load_module("05_validate_retrieval.py", "recommendation_quality_empty")
    rows = [
        {
            "model_id": "org/small-generator",
            "source_pool": "core",
            "task": {"primary": "text-generation", "matched": ["text-generation"]},
            "filter_metadata": {
                "korean_verified": True,
                "parameter_count_billion": 0.005,
                "context_length": 4096,
            },
        },
        {
            "model_id": "org/long-generator",
            "source_pool": "core",
            "task": {"primary": "text-generation", "matched": ["text-generation"]},
            "filter_metadata": {
                "korean_verified": True,
                "parameter_count_billion": 0.02,
                "context_length": 131072,
            },
        },
    ]
    query = {
        "tasks": ["text-generation"],
        "korean_required": True,
        "max_parameters_billion": 0.01,
        "min_context_length": 131072,
        "require_known_parameters": True,
        "require_known_context": True,
        "pools": ["core"],
    }

    suggestions = retrieval.relaxation_suggestions(rows, query)
    codes = {item["code"] for item in suggestions}

    assert "remove_min_context" in codes
    assert "remove_parameter_ceiling" in codes
    assert all(item["candidate_count"] > 0 for item in suggestions)


def test_hydrated_result_contains_grounded_llm_context_and_source_urls():
    retrieval = load_module("05_validate_retrieval.py", "recommendation_quality_context")
    compact = {
        "model_id": "org/model",
        "source_pool": "core",
        "task": "sentence-similarity",
        "evidence_completeness": "high",
    }
    catalog = {
        ("core", "org/model"): {
            "stage2": {
                "source": {"readme": {"available": True}},
                "model": {"parameter_count": 100},
            },
            "stage3": {
                "status": "completed",
                "semantic": {
                    "summary": {"text": "문장 유사도 모델", "evidence_refs": ["e1"]},
                    "documented_strengths": [
                        {
                            "text": "문장 유사도에 사용 가능",
                            "evidence_refs": ["e1"],
                            "evidence_level": "explicit",
                        }
                    ],
                },
                "evidence": {
                    "readme": {"available": True},
                    "spans": [
                        {
                            "evidence_id": "e1",
                            "text": "문장 유사도에 사용 가능",
                            "heading_path": ["Usage"],
                        }
                    ],
                },
            },
        }
    }

    result = retrieval.hydrate_result(compact, catalog)

    assert result["provenance"]["model_url"] == "https://huggingface.co/org/model"
    assert result["provenance"]["readme_url"].endswith("/blob/main/README.md")
    assert result["llm_context"]["evidence"]["claims"]["documented_strengths"][0]["supporting_spans"]


def test_supabase_rpc_exposes_hard_filters_and_grounding_payload():
    sql = (ROOT / "supabase_schema.sql").read_text(encoding="utf-8")

    assert "task_filters text[]" in sql
    assert "korean_required boolean" in sql
    assert "require_known_parameters boolean" in sql
    assert "query_text text" in sql
    assert "dense_weight real" in sql
    assert "plainto_tsquery('simple', coalesce(query_text, ''))" in sql
    assert "source_provenance jsonb" in sql
    assert "evidence_index jsonb" in sql
    assert "m.filter_metadata->>'korean_verified' = 'true'" in sql


def test_benchmark_projection_is_bounded_and_deduplicated():
    benchmark = load_module(
        "06_extract_benchmark_metadata.py", "recommendation_quality_benchmark"
    )
    results = [
        {
            "benchmark": "MTEB",
            "dataset": f"dataset-{index}",
            "metric": "ndcg_at_10",
            "score": index,
            "ranking_eligible": True,
        }
        for index in range(300)
    ]
    results.extend(results[:10])
    compact = benchmark.compact_sidecar({"results": results, "summary": {}})

    assert len(compact["results"]) == benchmark.MAX_COMPACT_RESULTS
    assert compact["summary"]["original_result_count"] == 310
    assert compact["summary"]["results_truncated"] is True


def test_sync_schema_never_recreates_supabase_vector_extension():
    sync = load_module("08_sync_supabase.py", "recommendation_quality_sync")
    assert "create extension" not in sync.schema_sql_without_extension().lower()
