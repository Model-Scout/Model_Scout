import importlib.util
import json
from pathlib import Path

import openai
import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_module(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_stage3_rewrite_removes_rows_no_longer_in_current_pool(tmp_path, monkeypatch):
    stage3 = load_module("03_generate_semantic_metadata.py", "stage3_pool_rewrite_test")
    stage3.DATA_DIR = tmp_path

    current_stage2 = {
        "model_id": "org/current",
        "source": {},
        "stage": {"stage2_version": 6},
    }
    (tmp_path / "hf_models_stage2_core.jsonl").write_text(
        json.dumps(current_stage2) + "\n", encoding="utf-8"
    )
    (tmp_path / "hf_models_stage3_core.jsonl").write_text(
        json.dumps({"model_id": "org/stale", "status": "completed"}) + "\n",
        encoding="utf-8",
    )

    class FakeOpenAI:
        def __init__(self, **kwargs):
            pass

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setattr(openai, "OpenAI", FakeOpenAI)

    stage3.enrich_pool("core", "test-model", limit=None, dry_run=False)

    rows = [
        json.loads(line)
        for line in (tmp_path / "hf_models_stage3_core.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    assert [row["model_id"] for row in rows] == ["org/current"]


def test_stage4_rejects_duplicate_ids_across_pools(tmp_path):
    stage4 = load_module("04_build_embeddings.py", "stage4_pool_disjointness_test")
    stage4.DATA_DIR = tmp_path
    duplicate = {"model_id": "org/duplicate"}
    (tmp_path / "hf_models_stage3_core.jsonl").write_text(
        json.dumps(duplicate) + "\n", encoding="utf-8"
    )
    (tmp_path / "hf_models_stage3_low_popularity.jsonl").write_text(
        json.dumps(duplicate) + "\n", encoding="utf-8"
    )

    with pytest.raises(ValueError, match="duplicate model_id"):
        stage4.validate_stage3_pool_disjointness(("core", "low_popularity"))


def test_sync_detects_persisted_cross_pool_stage3_overlap(tmp_path):
    sync = load_module("08_sync_supabase.py", "sync_stage3_overlap_test")
    sync.DATA_DIR = tmp_path
    duplicate = {"model_id": "org/duplicate"}
    (tmp_path / "hf_models_stage3_core.jsonl").write_text(
        json.dumps(duplicate) + "\n", encoding="utf-8"
    )
    (tmp_path / "hf_models_stage3_low_popularity.jsonl").write_text(
        json.dumps(duplicate) + "\n", encoding="utf-8"
    )

    assert sync.stage3_pools_need_reconciliation() is True
