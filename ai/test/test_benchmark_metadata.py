#!/usr/bin/env python3
"""Offline regression tests for conservative README benchmark extraction."""

from pathlib import Path
import importlib.util
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark_metadata import benchmark_matches, extract_benchmarks


_VALIDATOR_SPEC = importlib.util.spec_from_file_location(
    "stage4_validator", Path(__file__).resolve().parents[1] / "05_validate_retrieval.py"
)
_VALIDATOR = importlib.util.module_from_spec(_VALIDATOR_SPEC)
assert _VALIDATOR_SPEC.loader is not None
_VALIDATOR_SPEC.loader.exec_module(_VALIDATOR)


def row(model_id: str, quantized: bool = False):
    return {
        "model_id": model_id,
        "quantization": {"enabled": quantized},
    }


def test_model_index_numeric_result_is_eligible():
    text = """---
model-index:
  - name: multilingual-e5-base
    results:
      - task: sentence-similarity
        dataset:
          name: MTEB ArguAna
        metrics:
          - type: ndcg_at_10
            value: 44.23
---
"""
    metadata = extract_benchmarks(
        row("intfloat/multilingual-e5-base"), text, "README.md"
    )
    assert len(metadata["results"]) == 1
    record = metadata["results"][0]
    assert record["benchmark"] == "MTEB"
    assert record["ranking_eligible"] is True
    assert benchmark_matches(
        record,
        {"benchmark": "MTEB", "dataset": "MTEB ArguAna", "metric": "ndcg_at_10"},
    )


def test_missing_score_is_a_mention_only():
    text = """---
model-index:
  - name: multilingual-e5-base
    results:
      - task: sentence-similarity
        dataset:
          name: MTEB ArguAna
        metrics:
          - type: ndcg_at_10
---
"""
    metadata = extract_benchmarks(
        row("intfloat/multilingual-e5-base"), text, "README.md"
    )
    assert metadata["results"] == []
    assert any(m["reason"] == "score_missing_or_non_numeric" for m in metadata["mentions"])


def test_comparison_table_uses_current_model_column_only():
    text = """# Benchmark Results

| Model | Score |
|---|---:|
| my-model-GGUF | 80 |
| other-model | 90 |
"""
    metadata = extract_benchmarks(
        row("org/my-model-GGUF", quantized=True), text, "README.md"
    )
    assert len(metadata["results"]) == 2
    assert metadata["results"][0]["ranking_eligible"] is True
    assert metadata["results"][1]["ranking_eligible"] is False


def test_quantized_base_name_is_not_attributed_to_artifact():
    text = """# Benchmark Results

| Model | Score |
|---|---:|
| my-model | 80 |
"""
    metadata = extract_benchmarks(
        row("org/my-model-GGUF", quantized=True), text, "README.md"
    )
    assert metadata["results"][0]["ranking_eligible"] is False
    assert metadata["results"][0]["comparability"] == "variant_ambiguous"


def test_metadata_table_is_not_a_benchmark():
    text = """# Benchmark Results

| Architecture | Parameters | Quantization |
|---|---:|---|
| transformer | 1.2B | int4 |
"""
    metadata = extract_benchmarks(row("org/model"), text, "README.md")
    assert metadata["results"] == []


def test_retrieval_hydration_covers_stage4_rows():
    root = Path(__file__).resolve().parents[1]
    catalog = _VALIDATOR.load_catalog(root.parent / "backend" / "data")
    data_dir = root.parent / "backend" / "data"
    for pool in ("core", "low_popularity"):
        stage2_ids = {
            json.loads(line)["model_id"]
            for line in (data_dir / f"hf_models_stage2_{pool}.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip()
        }
        rows = [
            json.loads(line)
            for line in (data_dir / f"hf_models_stage4_{pool}.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        assert {row["model_id"] for row in rows} == stage2_ids
        assert all((pool, row["model_id"]) in catalog for row in rows)


def test_retrieval_hydration_includes_evidence():
    root = Path(__file__).resolve().parents[1]
    catalog = _VALIDATOR.load_catalog(root.parent / "backend" / "data")
    row = json.loads(
        (root.parent / "backend" / "data" / "hf_models_stage4_core.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()[0]
    )
    hydrated = _VALIDATOR.hydrate_result(row, catalog)
    assert hydrated["detail_joined"] is True
    assert hydrated["technical"]["model"]
    assert "claims" in hydrated["evidence"]
    assert hydrated["provenance"]["stage2_version"] == 6


if __name__ == "__main__":
    tests = [value for name, value in globals().items() if name.startswith("test_")]
    for test in tests:
        test()
    print(f"benchmark metadata tests passed: {len(tests)}")
