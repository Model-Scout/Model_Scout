import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

import huggingface_hub
import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_module(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def configure_stage1_paths(module, data_dir: Path) -> None:
    module.DATA_DIR = data_dir
    module.CORE_OUTPUT = data_dir / "hf_models_stage1_core.jsonl"
    module.LOW_POPULARITY_OUTPUT = data_dir / "hf_models_stage1_low_popularity.jsonl"
    module.LIKELY_OUTPUT = data_dir / "hf_models_stage1_likely.jsonl"
    module.FALLBACK_OUTPUT = data_dir / "hf_models_stage1_fallback.jsonl"
    module.GROUP_OUTPUT = data_dir / "hf_models_stage1_groups.jsonl"
    module.STATE_OUTPUT = data_dir / "hf_models_stage1_state.json"


class EmptyApi:
    def __init__(self, **kwargs):
        pass

    def list_models(self, **kwargs):
        return iter(())


def test_empty_full_collection_cannot_replace_published_snapshot(tmp_path):
    stage1 = load_module("01_collect_models.py", "stage1_empty_collection_test")
    configure_stage1_paths(stage1, tmp_path)
    stage1.TASKS = ["text-generation"]
    stage1.TASK_SLEEP_SECONDS = 0
    stage1.api = EmptyApi()

    sentinel = "existing published snapshot\n"
    stage1.CORE_OUTPUT.write_text(sentinel, encoding="utf-8")

    with pytest.raises((AssertionError, RuntimeError)):
        stage1.run_collection()

    assert stage1.CORE_OUTPUT.read_text(encoding="utf-8") == sentinel
    state = json.loads(
        (tmp_path / ".stage1_v7_checkpoint" / "hf_models_stage1_state.json")
        .read_text(encoding="utf-8")
    )
    assert state["task_stats"]["text-generation"]["scanned"] == 0
    assert state["task_stats"]["text-generation"]["error"]


def test_incremental_no_changed_models_is_valid_when_every_task_was_observed():
    sync = load_module("08_sync_supabase.py", "sync_incremental_no_change_test")
    sync.validate_incremental_scan(
        {"text-generation": True, "translation": True},
        existing_count=10,
    )


def test_incremental_scan_rejects_unobserved_task():
    sync = load_module("08_sync_supabase.py", "sync_incremental_scan_test")
    with pytest.raises(RuntimeError, match="translation"):
        sync.validate_incremental_scan(
            {"text-generation": True, "translation": False},
        existing_count=10,
    )


def test_incremental_scan_removes_existing_model_that_is_no_longer_candidate(
    tmp_path, monkeypatch
):
    sync = load_module("08_sync_supabase.py", "sync_removed_candidate_test")

    class FakeStage1:
        TASKS = ("text-generation",)
        MIN_DOWNLOADS = 80
        CANDIDATE_TYPES = {
            "A_verified": set(),
            "B_likely": set(),
            "C_fallback": set(),
        }

        @staticmethod
        def is_noise_model(model_id):
            return False

        @staticmethod
        def classify_candidate(model):
            return None

    class FakeApi:
        def __init__(self, **kwargs):
            pass

        def list_models(self, **kwargs):
            return [
                SimpleNamespace(
                    id="org/qwen-fallback",
                    downloads=1000,
                    last_modified="2099-01-01T00:00:00Z",
                )
            ]

    row = {
        "model_id": "org/qwen-fallback",
        "candidate": {"tier": "C_fallback"},
        "popularity": {"downloads": 1000},
    }
    for filename in (
        "hf_models_stage1_core.jsonl",
        "hf_models_stage1_low_popularity.jsonl",
        "hf_models_stage1_likely.jsonl",
        "hf_models_stage1_fallback.jsonl",
    ):
        (tmp_path / filename).write_text(json.dumps(row) + "\n", encoding="utf-8")
    (tmp_path / "hf_models_stage1_state.json").write_text("{}", encoding="utf-8")

    published = {}
    monkeypatch.setattr(sync, "DATA_DIR", tmp_path)
    monkeypatch.setattr(sync, "load_stage1_module", lambda: FakeStage1)
    monkeypatch.setattr(
        sync,
        "publish_stage1_snapshot",
        lambda stage1, all_models, state: published.update(
            all_models=all_models.copy(), state=state.copy()
        ),
    )
    monkeypatch.setattr(huggingface_hub, "HfApi", FakeApi)

    result = sync.incremental_stage1_update("2020-01-01T00:00:00Z")

    assert result["removed_ids"] == ["org/qwen-fallback"]
    assert "org/qwen-fallback" not in published["all_models"]


def test_snapshot_drop_guard_rejects_suspicious_decrease():
    stage1 = load_module("01_collect_models.py", "stage1_drop_guard_test")
    core_name = stage1.CORE_OUTPUT.name
    with pytest.raises(RuntimeError, match="dropped too sharply"):
        stage1.validate_snapshot_drop(
            {core_name: 1000},
            {core_name: 499},
        )


def test_snapshot_drop_guard_allows_small_decrease():
    stage1 = load_module("01_collect_models.py", "stage1_drop_guard_ok_test")
    core_name = stage1.CORE_OUTPUT.name
    stage1.validate_snapshot_drop(
        {core_name: 1000},
        {core_name: 500},
    )
