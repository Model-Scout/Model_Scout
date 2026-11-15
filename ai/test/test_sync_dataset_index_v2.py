"""--corpus v2 writes only the *_v2 tables: v1 (what the service reads) is never written or deleted."""

import importlib.util
import json
import re
import sys
import types
from pathlib import Path

import numpy as np
import pytest

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))
spec = importlib.util.spec_from_file_location("sync20_v2", AI / "20_sync_dataset_index.py")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)

V1_NAMES = re.compile(r"model_scout_datasets(?!_v2)|model_scout_dataset_chunks(?!_v2)|match_model_scout_datasets(?!_v2)")


class Cursor:
    def __init__(self, log):
        self.log, self.rowcount = log, 0

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def execute(self, sql, params=None):
        self.log.append(sql)

    def fetchone(self):
        return (0, 0)

    def fetchall(self):
        return []


class Conn:
    def __init__(self, log):
        self.log = log

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def cursor(self):
        return Cursor(self.log)

    def rollback(self):
        pass

    def close(self):
        pass


@pytest.fixture
def captured(monkeypatch):
    log = []
    monkeypatch.setitem(sys.modules, "supabase_db", types.SimpleNamespace(db_connection=lambda: Conn(log), vector_literal=str))
    import psycopg2.extras

    monkeypatch.setattr(psycopg2.extras, "execute_values", lambda cur, sql, rows, template=None: log.append(sql))
    return log


def run(target, build=None):
    chunks = [{"chunk_id": "a/b#card", "dataset_id": "a/b", "kind": "card", "heading_path": [], "text": "t", "text_hash": "h"}]
    entities = {"a/b": {"source": "s", "url": "u"}}
    sync.apply({}, chunks, np.zeros((1, sync.DIMENSION), dtype=np.float16), entities, {"a/b": []}, 300, target, build)


def test_v2_never_names_a_v1_table(captured):
    run(sync.TARGETS["v2"], build={"documents_id": "d"})
    sql = "\n".join(captured)
    assert "model_scout_datasets_v2" in sql and "model_scout_dataset_chunks_v2" in sql and "model_scout_dataset_index_v2_meta" in sql
    assert not V1_NAMES.search(sql)


def test_v1_default_is_unchanged(captured):
    run(sync.TARGETS["v1"])
    sql = "\n".join(captured)
    assert "public.model_scout_datasets" in sql and "_v2" not in sql


def test_v2_schema_file_only_creates_v2_objects():
    text = sync.TARGETS["v2"]["schema"].read_text(encoding="utf-8")
    assert not V1_NAMES.search(re.sub(r"--.*", "", text))
    assert "create or replace function public.match_model_scout_datasets_v2" in text


def test_v2_refuses_a_build_that_does_not_check_out(monkeypatch, tmp_path):
    import corpus_manifest

    monkeypatch.setattr(corpus_manifest, "check_corpus", lambda *a: ["검색 문서가 지금의 그래프로 만들어지지 않음"])
    monkeypatch.setattr(corpus_manifest, "check_vectors", lambda *a: [])
    with pytest.raises(SystemExit, match="does not check out"):
        sync.verified_build(sync.TARGETS["v2"])


def test_v2_refuses_a_consistent_build_that_is_not_the_pinned_one(monkeypatch):
    import corpus_manifest
    import public_v2_pipeline

    monkeypatch.setattr(corpus_manifest, "check_corpus", lambda *a: [])
    monkeypatch.setattr(corpus_manifest, "check_vectors", lambda *a: [])
    monkeypatch.setattr(public_v2_pipeline, "verify_pin", lambda: ["documents: 고정된 버전과 다름"])
    with pytest.raises(SystemExit, match="고정된 버전과 다름"):
        sync.verified_build(sync.TARGETS["v2"])


def test_v2_stores_the_whole_chunk_and_v1_a_preview():
    assert sync.TARGETS["v2"]["text_chars"] is None and sync.TARGETS["v1"]["text_chars"] == 600
    long = [{"text": "가" * 1000}]
    assert sync.estimated_bytes(long, {}, None) > sync.estimated_bytes(long, {}, 600)


def test_a_new_embedding_model_re_uploads_every_vector(monkeypatch):
    # same text, other model: every stored vector is stale even though text_hash matches
    uploaded = []

    class MetaCursor(Cursor):
        def execute(self, sql, params=None):
            self.last = sql

        def fetchone(self):
            return ({"embedding_model": "old-model"},) if "where key = 'build'" in getattr(self, "last", "") else (0, 0)

        def fetchall(self):
            return [("a/b#card", "h")]  # stored row already has this text hash

    class MetaConn(Conn):
        def cursor(self):
            return MetaCursor(self.log)

    monkeypatch.setitem(sys.modules, "supabase_db", types.SimpleNamespace(db_connection=lambda: MetaConn([]), vector_literal=str))
    import psycopg2.extras

    monkeypatch.setattr(psycopg2.extras, "execute_values", lambda cur, sql, rows, template=None: uploaded.append((sql, len(rows))))
    run(sync.TARGETS["v2"], build={"documents_id": "d", "embedding_model": "new-model"})
    assert any("model_scout_dataset_chunks_v2" in sql and n == 1 for sql, n in uploaded)


def loaded_parts(**override):
    chunks = [{"chunk_id": "a/b#card", "dataset_id": "a/b", "text": "원문 전체", "text_hash": "h"},
              {"chunk_id": "c/d#card", "dataset_id": "c/d", "text": "다른 문서", "text_hash": "g"}]
    parts = {"target": sync.TARGETS["v2"], "chunks": chunks, "entities": {"a/b": {}, "c/d": {}},
             "build": {"documents_id": "doc"}, "datasets": {"a/b", "c/d"},
             "stored": {"a/b#card": "원문 전체", "c/d#card": "다른 문서"}, "meta": {"documents_id": "doc"},
             "ranked": [("a/b", 1.0), ("c/d", 0.4)]}
    parts.update(override)
    return parts


def test_loaded_check_compares_the_stored_text_itself():
    assert sync.compare_loaded(**loaded_parts())["texts_compared"] == 2
    same_length_other_text = {"a/b#card": "원문 전부", "c/d#card": "다른 문서"}
    with pytest.raises(SystemExit, match="stored texts differ"):
        sync.compare_loaded(**loaded_parts(stored=same_length_other_text))


def test_loaded_check_allows_a_tied_top_search():
    # another dataset with the same text/vector may come first at the same score
    assert sync.compare_loaded(**loaded_parts(ranked=[("c/d", 1.0), ("a/b", 0.99995)]))
    with pytest.raises(SystemExit, match="own vector"):
        sync.compare_loaded(**loaded_parts(ranked=[("c/d", 1.0), ("a/b", 0.9)]))


def test_a_new_vector_file_with_the_same_model_re_uploads_every_vector(monkeypatch):
    uploaded = []

    class MetaCursor(Cursor):
        def execute(self, sql, params=None):
            self.last = sql

        def fetchone(self):
            build = {"embedding_model": "m", "vectors_sha256": "old"}
            return (build,) if "where key = 'build'" in getattr(self, "last", "") else (0, 0)

        def fetchall(self):
            return [("a/b#card", "h")]

    class MetaConn(Conn):
        def cursor(self):
            return MetaCursor(self.log)

    monkeypatch.setitem(sys.modules, "supabase_db", types.SimpleNamespace(db_connection=lambda: MetaConn([]), vector_literal=str))
    import psycopg2.extras

    monkeypatch.setattr(psycopg2.extras, "execute_values", lambda cur, sql, rows, template=None: uploaded.append((sql, len(rows))))
    run(sync.TARGETS["v2"], build={"documents_id": "d", "embedding_model": "m", "vectors_sha256": "new"})
    assert any("model_scout_dataset_chunks_v2" in sql and n == 1 for sql, n in uploaded)


def restore_setup(monkeypatch, tmp_path, build, rows):
    """A v2 target in tmp_path whose DB holds `build` and the vectors `rows` (chunk_id -> list)."""
    import corpus_manifest
    import public_v2_pipeline

    index = tmp_path / "index"
    index.mkdir()
    (index / "manifest.json").write_text(json.dumps({
        "documents_id": "doc", "model": "m", "rows": 2, "dimension": 2,
        "chunk_ids": ["a#card", "b#card"], "embedding_run": {"vectors_sha256": "frozen"}}), encoding="utf-8")
    monkeypatch.setattr(public_v2_pipeline, "verify_pin", lambda: [])
    monkeypatch.setattr(corpus_manifest, "load_manifest", lambda d: {"stage_id": "doc"})

    class RestoreCursor(Cursor):
        def fetchone(self):
            return (build,)

        def __iter__(self):
            return iter([(k, "[" + ",".join(map(str, v)) + "]") for k, v in rows.items()])

    class RestoreConn(Conn):
        def cursor(self, name=None):
            return RestoreCursor(self.log)

    import supabase_db

    monkeypatch.setitem(sys.modules, "supabase_db", types.SimpleNamespace(
        db_connection=lambda: RestoreConn([]), parse_vector=supabase_db.parse_vector))
    return {**sync.TARGETS["v2"], "index": index}


def test_restore_refuses_another_build_in_the_tables(monkeypatch, tmp_path):
    target = restore_setup(monkeypatch, tmp_path, {"documents_id": "other", "embedding_model": "m", "vectors_sha256": "frozen"},
                           {"a#card": [0.5, 0.25], "b#card": [1.0, 0.0]})
    with pytest.raises(SystemExit, match="another build"):
        sync.restore_vectors(target, tmp_path / "out.npy")
    assert not (tmp_path / "out.npy").exists()


def test_restore_never_fills_a_missing_vector(monkeypatch, tmp_path):
    target = restore_setup(monkeypatch, tmp_path, {"documents_id": "doc", "embedding_model": "m", "vectors_sha256": "frozen"},
                           {"a#card": [0.5, 0.25]})
    with pytest.raises(SystemExit, match="1 chunks have no vector"):
        sync.restore_vectors(target, tmp_path / "out.npy")
    assert not (tmp_path / "out.npy").exists()


def test_restore_writes_nothing_when_the_hash_differs(monkeypatch, tmp_path):
    target = restore_setup(monkeypatch, tmp_path, {"documents_id": "doc", "embedding_model": "m", "vectors_sha256": "frozen"},
                           {"a#card": [0.5, 0.25], "b#card": [1.0, 0.0]})
    with pytest.raises(SystemExit, match="restored vectors hash"):
        sync.restore_vectors(target, tmp_path / "out.npy")
    assert not (tmp_path / "out.npy").exists() and not list(tmp_path.glob("*.npy"))
