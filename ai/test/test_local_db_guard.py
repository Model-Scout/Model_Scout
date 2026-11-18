"""Local validation (MODEL_SCOUT_LOCAL=1): writes go to a local Postgres only, Supabase reads are read-only."""

import importlib.util
import sys
from pathlib import Path

import pytest

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))
import supabase_db  # noqa: E402

spec = importlib.util.spec_from_file_location("rg_guard", AI / "17_recommend_graph.py")
rg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rg)

SUPABASE = {"SUPABASE_DB_HOST": "db.example.supabase.co", "SUPABASE_DB_PORT": "5432", "SUPABASE_DB_NAME": "postgres",
            "SUPABASE_DB_USER": "u", "SUPABASE_PASSWORD": "p"}


@pytest.fixture
def env(monkeypatch):
    for k, v in SUPABASE.items():
        monkeypatch.setenv(k, v)
    monkeypatch.delenv("CHECKPOINT_DATABASE_URL", raising=False)
    monkeypatch.delenv("MODEL_SCOUT_LOCAL", raising=False)
    return monkeypatch


def test_service_default_unchanged(env):
    assert "host=db.example.supabase.co" in rg.checkpoint_conninfo()


def test_local_without_checkpoint_url_refuses(env):
    env.setenv("MODEL_SCOUT_LOCAL", "1")
    with pytest.raises(RuntimeError, match="CHECKPOINT_DATABASE_URL"):
        rg.checkpoint_conninfo()


def test_local_rejects_non_local_checkpoint_host(env):
    env.setenv("MODEL_SCOUT_LOCAL", "1")
    env.setenv("CHECKPOINT_DATABASE_URL", "postgresql://u:p@db.example.supabase.co:5432/postgres")
    with pytest.raises(RuntimeError, match="local Postgres"):
        rg.checkpoint_conninfo()


def test_local_checkpoint_url_keeps_schema(env):
    env.setenv("MODEL_SCOUT_LOCAL", "1")
    env.setenv("CHECKPOINT_DATABASE_URL", "postgresql://m:x@postgres:5432/model_scout?sslmode=disable")
    info = rg.checkpoint_conninfo()
    assert "host=postgres" in info and "search_path=langgraph" in info and "sslmode=disable" in info


def test_local_supabase_reads_are_read_only(env):
    seen = {}

    class FakePsycopg2:
        @staticmethod
        def connect(**kwargs):
            seen.update(kwargs)

    env.setitem(sys.modules, "psycopg2", FakePsycopg2)
    supabase_db.db_connection()
    assert "options" not in seen  # the service and the pipeline stages connect as before
    env.setenv("MODEL_SCOUT_LOCAL", "1")
    supabase_db.db_connection()
    assert seen["options"] == "-c default_transaction_read_only=on"
