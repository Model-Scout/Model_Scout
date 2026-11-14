import importlib.util
import json
import sys
import types
from pathlib import Path

import openai
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


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


def test_stage3_reuses_legacy_full_hash_for_an_unchanged_long_readme(tmp_path, monkeypatch):
    stage3 = load_module("03_generate_semantic_metadata.py", "stage3_legacy_long_readme_test")
    stage3.DATA_DIR = tmp_path
    readme = tmp_path / "long.md"
    text = "# Model\n" + ("documented capability and usage.\n" * 3000)
    assert len(text) > stage3.MAX_SOURCE_CHARS
    readme.write_text(text, encoding="utf-8")
    source = {
        "model_id": "org/long",
        "source": {"readme": {"available": True, "path": str(readme)}},
        "stage": {"stage2_version": 7},
    }
    old = {
        "model_id": "org/long",
        "status": "completed",
        "semantic": {},
        "evidence": {
            "readme": {"content_hash": stage3.digest(text)},
            "parent_child_schema_version": stage3.INDEX_SCHEMA_VERSION,
        },
        "stage3": {
            "stage3_version": stage3.STAGE3_VERSION,
            "prompt_version": "stage3-atomic-evidence-full-readme-v1",
        },
    }
    (tmp_path / "hf_models_stage2_core.jsonl").write_text(json.dumps(source) + "\n", encoding="utf-8")
    (tmp_path / "hf_models_stage3_core.jsonl").write_text(json.dumps(old) + "\n", encoding="utf-8")

    class FakeOpenAI:
        def __init__(self, **kwargs):
            pass

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setattr(openai, "OpenAI", FakeOpenAI)
    monkeypatch.setattr(
        stage3,
        "call_llm",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("unchanged README called the LLM")),
    )

    stats = stage3.enrich_pool("core", "test-model", limit=None, dry_run=False)
    row = json.loads((tmp_path / "hf_models_stage3_core.jsonl").read_text(encoding="utf-8"))
    assert stats["skipped"] == 1 and stats["api_calls"] == 0
    assert row["stage3"]["source_stage2_hash_version"] == stage3.STAGE2_HASH_VERSION


def test_stage3_records_actual_chat_token_usage():
    stage3 = load_module("03_generate_semantic_metadata.py", "stage3_usage_test")
    usage = types.SimpleNamespace(prompt_tokens=11, completion_tokens=7, total_tokens=18)
    response = types.SimpleNamespace(
        usage=usage,
        choices=[types.SimpleNamespace(message=types.SimpleNamespace(content='{"ok": true}'))],
    )
    client = types.SimpleNamespace(
        chat=types.SimpleNamespace(
            completions=types.SimpleNamespace(create=lambda **kwargs: response)
        )
    )
    totals = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    assert stage3.call_llm(client, "test", [], totals) == {"ok": True}
    assert totals == {"prompt_tokens": 11, "completion_tokens": 7, "total_tokens": 18}


def test_stage4_records_actual_embedding_token_usage(monkeypatch):
    stage4 = load_module("04_build_embeddings.py", "stage4_usage_test")
    usage = types.SimpleNamespace(prompt_tokens=9, total_tokens=9)
    response = types.SimpleNamespace(
        usage=usage,
        data=[types.SimpleNamespace(index=0, embedding=[0.1, 0.2])],
    )

    class FakeOpenAI:
        def __init__(self, **kwargs):
            self.embeddings = types.SimpleNamespace(create=lambda **call: response)

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setattr(openai, "OpenAI", FakeOpenAI)
    documents = [{"model_id": "org/model", "embedding_text": "hello"}]
    totals = stage4.embed_documents(documents, "test", batch_size=32)
    assert totals == {"api_calls": 1, "prompt_tokens": 9, "total_tokens": 9}
    assert documents[0]["embedding"] == [0.1, 0.2]


def test_stage2_rewrite_removes_rows_no_longer_in_current_pool(tmp_path, monkeypatch):
    stage2 = load_module("02_enrich_metadata.py", "stage2_pool_rewrite_test")
    input_path = tmp_path / "hf_models_stage1_core.jsonl"
    output_path = tmp_path / "hf_models_stage2_core.jsonl"
    input_path.write_text(
        json.dumps({"model_id": "org/current"}) + "\n", encoding="utf-8"
    )
    output_path.write_text(
        json.dumps({"model_id": "org/stale"}) + "\n", encoding="utf-8"
    )
    stage2.POOL_CONFIGS["core"] = {
        "input": input_path,
        "output": output_path,
        "contract_output": tmp_path / "hf_models_stage2_contract_core.jsonl",
        "readme_dir": tmp_path / "readmes",
    }
    stage2.TEST_LIMIT = None
    stage2.CHECKPOINT_EVERY = 25
    monkeypatch.setattr(
        stage2,
        "enrich",
        lambda source_row, source_pool: {
            "model_id": source_row["model_id"],
            "contract": {"model_id": source_row["model_id"]},
        },
    )
    monkeypatch.setattr(stage2, "validate_stage2_rows", lambda rows, pool: None)
    monkeypatch.setattr(stage2, "print_pool_stats", lambda *args: None)

    stage2.process_pool("core")

    rows = [
        json.loads(line)
        for line in output_path.read_text(encoding="utf-8").splitlines()
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


def test_stage4_db_cache_only_requests_non_reusable_documents():
    stage4 = load_module("04_build_embeddings.py", "stage4_db_cache_candidates_test")
    documents = [
        {"model_id": "org/reuse", "document_hash": "hash-1"},
        {"model_id": "org/changed", "document_hash": "hash-2"},
        {"model_id": "org/missing", "document_hash": "hash-3"},
    ]
    existing = {
        "org/reuse": {
            "model_id": "org/reuse",
            "document_hash": "hash-1",
            "embedding_model": "test-model",
            "embedding": [0.1],
        },
        "org/changed": {
            "model_id": "org/changed",
            "document_hash": "old-hash",
            "embedding_model": "test-model",
            "embedding": [0.1],
        },
    }

    assert stage4.db_cache_candidate_ids(documents, existing, "test-model") == [
        "org/changed",
        "org/missing",
    ]


def test_stage4_allows_small_incremental_db_cache_gaps():
    stage4 = load_module("04_build_embeddings.py", "stage4_db_cache_guard_test")

    assert stage4.should_refuse_db_reembedding(1477, 50, 30) is False
    assert stage4.should_refuse_db_reembedding(3567, 3567, 30) is True
    assert stage4.should_refuse_db_reembedding(1477, 200, 150) is True


def test_stage4_full_scan_accepts_cache_churn_within_the_reviewed_guard():
    stage4 = load_module("04_build_embeddings.py", "stage4_full_scan_cache_guard_test")

    # The failed production dry-run had 1,457 cached vectors for 1,720
    # candidates: 15.3% misses. A full scan with the reviewed 30% replacement
    # guard may embed those genuinely new/changed rows.
    assert stage4.should_refuse_db_reembedding(
        1720, 1720, 1457, max_miss_fraction=0.30
    ) is False
    assert stage4.should_refuse_db_reembedding(
        1720, 1720, 1100, max_miss_fraction=0.30
    ) is True

    # Pool-local skew may exceed 30%, while the complete catalog stays inside
    # the reviewed 30% full-scan churn budget. The production guard is global.
    assert stage4.should_refuse_db_reembedding(
        2291, 2291, 1482, max_miss_fraction=0.30
    ) is True
    assert stage4.should_refuse_db_reembedding(
        4011, 4011, 2939, max_miss_fraction=0.30
    ) is False


def test_stage4_ignores_git_lfs_pointer_snapshot(tmp_path):
    stage4 = load_module("04_build_embeddings.py", "stage4_lfs_pointer_test")
    snapshot = tmp_path / "hf_models_stage4_core.jsonl"
    snapshot.write_text(
        "version https://git-lfs.github.com/spec/v1\n"
        "oid sha256:" + "a" * 64 + "\n"
        "size 123\n",
        encoding="utf-8",
    )

    assert stage4.is_git_lfs_pointer(snapshot) is True
    assert stage4.load_snapshot_by_id(snapshot) == {}


def test_stage4_does_not_hide_non_lfs_snapshot_corruption(tmp_path):
    stage4 = load_module("04_build_embeddings.py", "stage4_bad_snapshot_test")
    snapshot = tmp_path / "hf_models_stage4_core.jsonl"
    snapshot.write_text("not json\n", encoding="utf-8")

    with pytest.raises(RuntimeError, match="Invalid Stage 4 snapshot"):
        stage4.load_snapshot_by_id(snapshot)


def test_sync_rejects_missing_stage3_or_stage4_rows():
    sync = load_module("08_sync_supabase.py", "sync_corpus_coverage_test")

    with pytest.raises(ValueError, match="missing Stage 3 rows"):
        sync.validate_corpus(
            stage4=[],
            stage2={"org/current": {}},
            stage3={},
        )


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
