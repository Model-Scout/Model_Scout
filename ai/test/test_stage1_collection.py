import importlib.util
import json
import subprocess
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


# ── --reingest --full-stage1 ──────────────────────────────────────────────

def _write_stage1(data_dir: Path, sync, core_ids, low_ids=()):
    rows = {
        "core": core_ids,
        "low_popularity": low_ids,
        "likely": [],
        "fallback": [],
    }
    for partition, filename in sync.STAGE1_PARTITIONS.items():
        (data_dir / filename).write_text(
            "".join(json.dumps({"model_id": model_id}) + "\n" for model_id in rows[partition]),
            encoding="utf-8",
        )
    (data_dir / "hf_models_stage1_groups.jsonl").write_text("", encoding="utf-8")
    (data_dir / "hf_models_stage1_state.json").write_text('{"v": "old"}', encoding="utf-8")


def _snapshot(data_dir: Path, sync):
    return {
        name: (data_dir / name).read_text(encoding="utf-8")
        for name in sync.STAGE1_SNAPSHOT_FILES
    }


def test_full_stage1_scan_failure_keeps_the_published_snapshot(tmp_path, monkeypatch):
    sync = load_module("08_sync_supabase.py", "sync_full_scan_failure_test")
    monkeypatch.setattr(sync, "DATA_DIR", tmp_path)
    _write_stage1(tmp_path, sync, [f"a/{i}" for i in range(5)])
    before = _snapshot(tmp_path, sync)
    commands = []

    def failing_collect(command):
        commands.append(command)
        raise subprocess.CalledProcessError(1, command)

    monkeypatch.setattr(sync, "run_command", failing_collect)
    with pytest.raises(subprocess.CalledProcessError):
        sync.run_full_stage1_scan()
    assert _snapshot(tmp_path, sync) == before
    assert commands[0][-2:] == [str(sync.ROOT / "01_collect_models.py"), "--no-resume"]
    assert not list(tmp_path.glob(".stage1_reingest_backup_*"))


def test_full_stage1_removal_guard_restores_the_previous_snapshot(tmp_path, monkeypatch):
    """01 은 50% 가드만 본다. 그 안쪽의 20% 감소는 재적재 가드가 막고 되돌린다."""
    sync = load_module("08_sync_supabase.py", "sync_full_scan_guard_test")
    monkeypatch.setattr(sync, "DATA_DIR", tmp_path)
    previous_ids = [f"a/{i}" for i in range(1000)]
    _write_stage1(tmp_path, sync, previous_ids)
    before = _snapshot(tmp_path, sync)

    def collect_with_mass_drop(command):
        _write_stage1(tmp_path, sync, previous_ids[:800])
        (tmp_path / "hf_models_stage1_state.json").write_text('{"v": "new"}', encoding="utf-8")

    monkeypatch.setattr(sync, "run_command", collect_with_mass_drop)
    with pytest.raises(RuntimeError, match="200"):
        sync.run_full_stage1_scan()
    assert _snapshot(tmp_path, sync) == before


def test_full_stage1_scan_reports_the_diff_and_the_scan_start(tmp_path, monkeypatch):
    sync = load_module("08_sync_supabase.py", "sync_full_scan_diff_test")
    monkeypatch.setattr(sync, "DATA_DIR", tmp_path)
    _write_stage1(tmp_path, sync, ["a/stay", "a/down"], ["a/up", "a/gone"])
    moments = []

    def collect(command):
        moments.append(sync.datetime.now(sync.timezone.utc))
        _write_stage1(tmp_path, sync, ["a/stay", "a/up", "a/new"], ["a/down"])

    monkeypatch.setattr(sync, "run_command", collect)
    scan = sync.run_full_stage1_scan()
    assert sync.parse_utc(scan["scan_started_at"]) <= moments[0]
    diff = scan["diff"]
    assert diff["added_ids"] == ["a/new"] and diff["removed_ids"] == ["a/gone"]
    assert diff["core_to_low_ids"] == ["a/down"] and diff["low_to_core_ids"] == ["a/up"]
    assert diff["removal_guard"]["blocked"] is False


def test_stage1_no_resume_ignores_an_incomplete_checkpoint(tmp_path, monkeypatch):
    stage1 = load_module("01_collect_models.py", "stage1_no_resume_test")
    configure_stage1_paths(stage1, tmp_path)
    checkpoint = tmp_path / f".stage1_v{stage1.STAGE1_VERSION}_checkpoint"
    checkpoint.mkdir()
    (checkpoint / stage1.STATE_OUTPUT.name).write_text(
        json.dumps({"stage1_version": stage1.STAGE1_VERSION, "completed_tasks": []}),
        encoding="utf-8",
    )
    seen = []

    def fake_main(resume=False):
        seen.append(resume)
        raise RuntimeError("stop after main")

    monkeypatch.setattr(stage1, "main", fake_main)
    for resume in (True, False):
        with pytest.raises(RuntimeError):
            stage1.run_collection(resume=resume)
    assert seen == [True, False]


def test_incremental_after_full_scan_rechecks_models_changed_during_the_scan(
    tmp_path, monkeypatch
):
    """전체 재스캔의 watermark 는 스캔 시작 시각이다.

    스캔 도중(시작 이후) 바뀐 모델은 다음 --refresh 가 다시 본다. 완료 시각을
    썼다면 이 모델은 영원히 건너뛰었을 것이다.
    """
    sync = load_module("08_sync_supabase.py", "sync_watermark_gap_test")
    scan_started = "2026-11-20T09:00:00+00:00"
    scan_finished = "2026-11-20T13:00:00+00:00"

    class FakeStage1:
        TASKS = ("text-generation",)
        MIN_DOWNLOADS = 80
        CANDIDATE_TYPES = {"A_verified": set()}

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
            # last_modified 내림차순. 스캔 도중 수정 1건, 스캔 전 수정 1건.
            return [
                SimpleNamespace(id="org/edited-mid-scan", downloads=1000,
                                last_modified="2026-11-20T11:30:00Z"),
                SimpleNamespace(id="org/edited-before", downloads=1000,
                                last_modified="2026-11-20T08:00:00Z"),
            ]

    for filename in (
        "hf_models_stage1_core.jsonl",
        "hf_models_stage1_low_popularity.jsonl",
        "hf_models_stage1_likely.jsonl",
        "hf_models_stage1_fallback.jsonl",
    ):
        (tmp_path / filename).write_text("", encoding="utf-8")
    (tmp_path / "hf_models_stage1_state.json").write_text("{}", encoding="utf-8")
    monkeypatch.setattr(sync, "DATA_DIR", tmp_path)
    monkeypatch.setattr(sync, "load_stage1_module", lambda: FakeStage1)
    monkeypatch.setattr(sync, "publish_stage1_snapshot", lambda *args: None)
    monkeypatch.setattr(huggingface_hub, "HfApi", FakeApi)

    refresh_info = {"mode": "reingest", "stage1_mode": "full-scan",
                    "source_watermark": scan_started, "started_at": scan_started}
    watermark = sync.resolved_source_watermark(refresh_info)
    assert watermark == scan_started
    result = sync.incremental_stage1_update(watermark)
    assert result["changed_ids"] == ["org/edited-mid-scan"]

    late = sync.incremental_stage1_update(scan_finished)
    assert late["changed_ids"] == [], "완료 시각 기준이면 스캔 중 변경을 놓친다"
