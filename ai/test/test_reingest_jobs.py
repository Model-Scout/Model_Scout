"""Checkpointed reingest job safety tests (network-free)."""

from __future__ import annotations

import importlib.util
import os
import sys
import tempfile
import types
from contextlib import contextmanager
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("reingest_jobs_tested", ROOT / "reingest_jobs.py")
assert SPEC is not None and SPEC.loader is not None
jobs = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = jobs
SPEC.loader.exec_module(jobs)


@contextmanager
def patched(target, **attrs):
    old = {name: getattr(target, name) for name in attrs}
    for name, value in attrs.items():
        setattr(target, name, value)
    try:
        yield
    finally:
        for name, value in old.items():
            setattr(target, name, value)


def identity(run_id="10"):
    return {"repository": "Model-Scout/Model_Scout", "git_sha": "a" * 40, "git_ref": "main", "run_id": run_id}


def state(run_id="10", sync_id="sync-1"):
    return {"schema_version": 1, "identity": identity(run_id), "supabase_latest_sync_run_id": sync_id}


def test_checkpoint_rejects_another_workflow_run():
    with patched(jobs.sync, git_identity=lambda: identity("11")):
        try:
            jobs.assert_same_run(state("10"))
        except RuntimeError as error:
            assert "run_id" in str(error)
        else:
            raise AssertionError("another workflow run reused the checkpoint")


def test_checkpoint_rejects_a_changed_supabase_baseline():
    with patched(jobs.sync, latest_completed_sync=lambda any_versions=False: {"run_id": "sync-2"}):
        try:
            jobs.assert_sync_baseline(state(sync_id="sync-1"))
        except RuntimeError as error:
            assert "Supabase changed" in str(error)
        else:
            raise AssertionError("stale checkpoint passed")


def test_preflight_calls_hf_chat_embedding_and_database_without_exposing_keys():
    calls = []

    class FakeHfApi:
        def __init__(self, token):
            assert token == "hf-secret"

        def model_info(self, model, files_metadata=False):
            calls.append(("hf", model, files_metadata))
            return types.SimpleNamespace(id=model)

    usage = types.SimpleNamespace(total_tokens=3)

    class FakeOpenAI:
        def __init__(self, api_key):
            assert api_key == "sk-secret"
            self.chat = types.SimpleNamespace(
                completions=types.SimpleNamespace(
                    create=lambda **kwargs: calls.append(("chat", kwargs["model"]))
                    or types.SimpleNamespace(usage=usage)
                )
            )
            self.embeddings = types.SimpleNamespace(
                create=lambda **kwargs: calls.append(("embedding", kwargs["model"]))
                or types.SimpleNamespace(usage=usage)
            )

    class Cursor:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def execute(self, sql):
            calls.append(("db", sql))

        def fetchone(self):
            return (1,)

    class Connection:
        def cursor(self):
            return Cursor()

        def close(self):
            calls.append(("db-close",))

    old_hf = sys.modules.get("huggingface_hub")
    old_openai = sys.modules.get("openai")
    sys.modules["huggingface_hub"] = types.SimpleNamespace(HfApi=FakeHfApi)
    sys.modules["openai"] = types.SimpleNamespace(OpenAI=FakeOpenAI)
    old_env = {key: os.environ.get(key) for key in ("HF_TOKEN", "OPENAI_API_KEY")}
    os.environ["HF_TOKEN"] = "hf-secret"
    os.environ["OPENAI_API_KEY"] = "sk-secret"
    try:
        with patched(jobs.sync, db_connection=lambda: Connection()):
            result = jobs.preflight()
    finally:
        for key, value in old_env.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        if old_hf is None:
            sys.modules.pop("huggingface_hub", None)
        else:
            sys.modules["huggingface_hub"] = old_hf
        if old_openai is None:
            sys.modules.pop("openai", None)
        else:
            sys.modules["openai"] = old_openai

    assert result["ok"] is True
    assert {call[0] for call in calls} >= {"hf", "chat", "embedding", "db", "db-close"}
    assert "secret" not in str(result)


def test_stage4_is_built_before_benchmark_integration():
    calls = []

    def capture(command):
        calls.append((Path(command[1]).name, command[2:]))

    with patched(jobs.sync, run_command=capture):
        jobs.run_stage4_pipeline(0.30)

    assert [name for name, _ in calls] == [
        "04_build_embeddings.py",
        "06_extract_benchmark_metadata.py",
    ]
    assert "--execute" in calls[0][1]
    assert "--max-db-cache-miss-fraction" in calls[0][1]
    assert calls[0][1][calls[0][1].index("--max-db-cache-miss-fraction") + 1] == "0.3"
    assert "--apply" in calls[1][1]


def test_full_scan_uses_the_reviewed_reingest_churn_limit():
    with patched(jobs.sync, REINGEST_MAX_DEACTIVATION_FRACTION=0.30):
        assert jobs.stage4_cache_miss_fraction({"stage1_mode": "full-scan"}) == 0.30
        assert jobs.stage4_cache_miss_fraction({"stage1_mode": "reuse"}) == 0.10


def test_resume_accepts_only_an_ancestor_with_recovery_only_changes():
    source = state("43534633028")
    current = identity("77") | {"git_sha": "b" * 40, "git_ref": "main"}
    completed = types.SimpleNamespace(returncode=0)
    with patched(jobs.sync, git_identity=lambda: current), patched(
        jobs.subprocess, run=lambda *args, **kwargs: completed
    ), patched(
        jobs,
        git_changed_paths=lambda old, new: {
            "ai/reingest_jobs.py",
            ".github/workflows/model-scout-reingest.yml",
        },
    ):
        assert jobs.assert_resumable_source(source, "43534633028") == current


def test_resume_rejects_unrelated_changes_after_the_checkpoint():
    source = state("43534633028")
    current = identity("77") | {"git_sha": "b" * 40, "git_ref": "main"}
    completed = types.SimpleNamespace(returncode=0)
    with patched(jobs.sync, git_identity=lambda: current), patched(
        jobs.subprocess, run=lambda *args, **kwargs: completed
    ), patched(
        jobs,
        git_changed_paths=lambda old, new: {"ai/02_enrich_metadata.py"},
    ):
        try:
            jobs.assert_resumable_source(source, "43534633028")
        except RuntimeError as error:
            assert "start a new dry-run" in str(error)
            assert "02_enrich_metadata.py" in str(error)
        else:
            raise AssertionError("an unrelated pipeline change reused the Stage 3 checkpoint")


def test_resume_rebinds_the_bundle_state_to_the_recovery_run():
    source_identity = identity("43534633028")
    current_identity = identity("77") | {"git_sha": "b" * 40, "git_ref": "main"}
    source_state = {
        "schema_version": 1,
        "identity": source_identity,
        "started_at": "2026-11-13T00:00:00+00:00",
        "stage1_mode": "full-scan",
        "stage1_scan": {"scan_started_at": "2026-11-13T00:00:00+00:00", "diff": {}},
        "previous_watermark": "2026-10-01T00:00:00+00:00",
        "supabase_latest_sync_run_id": "sync-1",
    }
    joined = {
        "latest": {"run_id": "sync-1"},
        "produced": 3886,
        "language_excluded": set(),
        "excluded_in_stage1": 0,
        "stage1_processable": 3886,
        "gate": {"ok": True},
    }
    calls = []
    with tempfile.TemporaryDirectory() as directory:
        state_path = Path(directory) / "context.json"
        output_path = Path(directory) / "refresh-info.json"
        state_path.write_text(__import__("json").dumps(source_state), encoding="utf-8")
        with patched(jobs, assert_resumable_source=lambda state, run: current_identity), patched(
            jobs, validate_joined_stage2=lambda state, check_same_run=False: joined
        ), patched(
            jobs, assert_stage3_checkpoint=lambda state, produced: calls.append(("stage3", produced))
        ), patched(
            jobs, run_stage4_pipeline=lambda limit: calls.append(("stage4", limit))
        ), patched(
            jobs.sync,
            REINGEST_MAX_DEACTIVATION_FRACTION=0.30,
            reingest_result=lambda **kwargs: {"mode": "reingest", "steps": kwargs["steps"]},
        ):
            result = jobs.resume_finalize(state_path, "43534633028", output_path)

        assert __import__("json").loads(output_path.read_text())["identity"] == current_identity

    assert calls == [("stage3", 3886), ("stage4", 0.30)]
    assert result["identity"] == current_identity
    assert result["resumed_from"] == source_identity
    assert "resume-finalize:43534633028" in result["refresh_info"]["steps"]


def test_stage3_checkpoint_is_separate_from_stage4_work():
    calls = []

    def capture(command):
        calls.append(Path(command[1]).name)

    with patched(jobs.sync, run_command=capture, POOLS=("core", "low_popularity")):
        jobs.run_stage3_pipeline()

    assert calls == [
        "03_generate_semantic_metadata.py",
        "03_repair_truncated_semantic.py",
        "03_repair_truncated_semantic.py",
        "evidence_index.py",
    ]
    assert "04_build_embeddings.py" not in calls
    assert "06_extract_benchmark_metadata.py" not in calls


def test_benchmark_reader_rejects_a_clean_checkout_lfs_pointer():
    spec = importlib.util.spec_from_file_location(
        "benchmark_lfs_pointer_test", ROOT / "06_extract_benchmark_metadata.py"
    )
    assert spec is not None and spec.loader is not None
    benchmark = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(benchmark)

    with tempfile.TemporaryDirectory() as directory:
        pointer = Path(directory) / "stage4.jsonl"
        pointer.write_text(
            "version https://git-lfs.github.com/spec/v1\n"
            "oid sha256:" + "a" * 64 + "\n"
            "size 123\n",
            encoding="utf-8",
        )
        try:
            benchmark.read_jsonl(pointer)
        except RuntimeError as error:
            assert "Git LFS pointer" in str(error)
            assert "Stage 4 checkpoint" in str(error)
        else:
            raise AssertionError("Git LFS pointer was parsed as model JSONL")


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
