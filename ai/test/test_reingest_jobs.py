"""Checkpointed reingest job safety tests (network-free)."""

from __future__ import annotations

import importlib.util
import os
import sys
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


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
