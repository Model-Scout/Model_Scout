"""A server serves v2 only when the deployed graph, documents record, vector file and the Supabase v2
build record are the same frozen version; any mismatch stops it (never a silent fall back to v1)."""

import json
import sys
import types
from pathlib import Path

import numpy as np
import pytest

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))
import corpus_manifest  # noqa: E402
import hypergraph_search as hs  # noqa: E402

GRAPH = {"stage_id": "graph-1"}
DOCUMENTS = {"stage_id": "04239c20eb394c12abcd", "upstream": {"corpus_id": "graph-1"}, "options": {"embedding_model": "m"}}


@pytest.fixture
def server(tmp_path, monkeypatch):
    """A deployed v2: graph dir + documents dir with a recorded vector file, Supabase holding the same build."""
    graph_dir, docs_dir = tmp_path / "hypergraph_v2", tmp_path / "dataset_index_v2"
    graph_dir.mkdir()
    docs_dir.mkdir()
    np.save(docs_dir / "embeddings.npy", np.zeros((2, 4), dtype=np.float16))
    sha = corpus_manifest.sha256_file(docs_dir / "embeddings.npy")
    (docs_dir / "manifest.json").write_text(json.dumps({
        "documents_id": DOCUMENTS["stage_id"], "model": "m", "chunk_ids": ["a#card", "b#card"],
        "embedding_run": {"vectors_sha256": sha}}), encoding="utf-8")
    manifests = {graph_dir: GRAPH, docs_dir: DOCUMENTS}
    monkeypatch.setattr(corpus_manifest, "load_manifest", lambda d: manifests.get(Path(d)))
    monkeypatch.setattr(corpus_manifest, "check_manifest", lambda d, **kw: [])
    monkeypatch.setattr(hs, "CORPUS", "v2")
    monkeypatch.setattr(hs, "HYPERGRAPH_DIR", graph_dir)
    monkeypatch.setattr(hs, "DATASET_INDEX_DIR", docs_dir)
    monkeypatch.setenv("MODEL_SCOUT_DATA_VERSION", "04239c20eb394c12")
    build = {"corpus_id": "graph-1", "documents_id": DOCUMENTS["stage_id"], "embedding_model": "m", "vectors_sha256": sha}
    state = {"build": build, "reachable": True}

    class Cur:
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def execute(self, *a):
            pass

        def fetchone(self):
            return (state["build"],)

    class Conn:
        def cursor(self):
            return Cur()

        def close(self):
            pass

    def connect():
        if not state["reachable"]:
            raise OSError("connection refused")
        return Conn()

    monkeypatch.setitem(sys.modules, "supabase_db", types.SimpleNamespace(db_connection=connect))
    hs.corpus_identity.cache_clear()
    yield state, docs_dir
    hs.corpus_identity.cache_clear()


def test_a_matching_deployment_serves_from_the_local_vector_file(server):
    identity = hs.corpus_identity()
    assert identity["vectors"] == "local" and identity["documents_id"].startswith("04239c20") and identity["embedding_model"] == "m"


@pytest.mark.parametrize("change, message", [
    (lambda s, d, mp: mp.setenv("MODEL_SCOUT_DATA_VERSION", "deadbeefdeadbeef"), "are not data_version"),
    (lambda s, d, mp: np.save(d / "embeddings.npy", np.ones((2, 4), dtype=np.float16)), "not the recorded file"),
    (lambda s, d, mp: s["build"].update(documents_id="other"), "holds another build"),
    (lambda s, d, mp: s["build"].update(vectors_sha256="other"), "holds another build"),
    (lambda s, d, mp: s.update(reachable=False), "unreachable"),
])
def test_any_mismatch_stops_v2(server, monkeypatch, change, message):
    state, docs_dir = server
    change(state, docs_dir, monkeypatch)
    with pytest.raises(hs.CorpusMismatch, match=message):
        hs.corpus_identity()


def test_v2_without_its_vector_file_does_not_start(server):
    state, docs_dir = server
    (docs_dir / "embeddings.npy").unlink()
    with pytest.raises(hs.CorpusMismatch, match="벡터 없음"):
        hs.corpus_identity()
