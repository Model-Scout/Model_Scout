"""검색 모듈의 코퍼스 선택 회귀 테스트. 유료·외부 호출 없음 (모의 임베딩).

    python -m pytest -q test/test_corpus_selection.py
"""

import importlib.util
import json
import os
import sys
from pathlib import Path

import numpy as np
import pytest

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))

import corpus_manifest as cm  # noqa: E402
import hypergraph_search as hs  # noqa: E402

_spec = importlib.util.spec_from_file_location("chunks14_select", AI / "14_build_dataset_chunks.py")
chunks14 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chunks14)

MODEL = "fake-embedding-model"


def vector(text):
    return [1.0, float(len(text) % 7), 0.5]


def build_v2(root, monkeypatch, names=("org/a", "org/b"), embed=True):
    """13-like graph + 14 documents (+ mock vectors) under root, with their build records."""
    root.mkdir(parents=True, exist_ok=True)
    hf, graph_dir, docs_dir = root / "hf.jsonl", root / "graph_v2", root / "docs_v2"
    rows = [{"dataset_id": n, "description": f"{n} 설명", "downloads": 1} for n in names]
    hf.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    graph_dir.mkdir(parents=True, exist_ok=True)
    entities = [{"entity_id": f"dataset:{n}", "kind": "dataset", "name": n, "readme_status": "missing"} for n in names]
    (graph_dir / "entities.jsonl").write_text("".join(json.dumps(e) + "\n" for e in entities), encoding="utf-8")
    for name in ("concepts.jsonl", "links.jsonl", "relations.jsonl"):
        (graph_dir / name).write_text("", encoding="utf-8")
    outputs = [graph_dir / n for n in ("entities.jsonl", "concepts.jsonl", "links.jsonl", "relations.jsonl")]
    cm.write_manifest(graph_dir, stage="hypergraph", corpus="v2", options={}, inputs=[hf], code=[], outputs=outputs, counts={})
    with monkeypatch.context() as m:
        m.setattr(chunks14, "CORPUS_DIRS", {"v2": (graph_dir, docs_dir)})
        m.setattr(chunks14, "DATA_DIR", root)
        m.setattr(chunks14, "DATASET_INPUT", hf)
        m.setattr(chunks14, "KAGGLE_INPUT", root / "none.jsonl")
        m.setattr(chunks14, "PUBLIC_INPUTS", {"v2": root / "none.jsonl"})
        m.setattr(chunks14, "EMBEDDING_MODEL", MODEL)
        m.setattr(chunks14, "embed", lambda texts, model: [vector(t) for t in texts])
        m.setattr(chunks14, "db_vectors", lambda hashes, required=False: ({}, "not_configured"))
        m.setattr("dotenv.load_dotenv", lambda *a, **k: None)
        m.setattr(sys, "argv", ["14", "--corpus", "v2", *(["--embed"] if embed else [])])
        chunks14.main()
    return graph_dir, docs_dir


@pytest.fixture
def corpora(tmp_path, monkeypatch):
    """A v1 graph with local vectors and a checked v2 build; the module is restored afterwards."""
    v1_graph, v1_docs = tmp_path / "graph_v1", tmp_path / "docs_v1"
    v1_graph.mkdir()
    v1_docs.mkdir()
    (v1_graph / "entities.jsonl").write_text(json.dumps({"entity_id": "dataset:old/x", "kind": "dataset"}) + "\n", encoding="utf-8")
    for name in ("concepts.jsonl", "links.jsonl", "relations.jsonl"):
        (v1_graph / name).write_text("", encoding="utf-8")
    np.save(v1_docs / "embeddings.npy", np.array([[1.0, 0.0, 0.0]], dtype=np.float16))
    (v1_docs / "manifest.json").write_text(json.dumps({"model": "v1-model", "chunk_ids": ["old/x#card"]}), encoding="utf-8")
    v2_graph, v2_docs = build_v2(tmp_path, monkeypatch)
    for name in ("CORPUS", "HYPERGRAPH_DIR", "DATASET_INDEX_DIR"):
        monkeypatch.setattr(hs, name, getattr(hs, name))
    monkeypatch.setattr(hs, "CORPORA", {"v1": (v1_graph, v1_docs), "v2": (v2_graph, v2_docs)})
    monkeypatch.setattr(hs, "_supabase_dense_scores", lambda q: pytest.fail("Supabase 벡터로 넘어감"))
    hs.use_corpus("v1")
    yield tmp_path, (v2_graph, v2_docs)
    for cached in (hs.load_graph, hs.load_link_evidence, hs.load_dataset_vectors, hs.corpus_identity):
        cached.cache_clear()


def test_default_corpus_is_v1_and_bad_values_fail_at_import(monkeypatch):
    assert os.environ.get("MODEL_SCOUT_CORPUS", "v1") == "v1" and hs.CORPUS == "v1"
    monkeypatch.setenv("MODEL_SCOUT_CORPUS", "v3")
    spec = importlib.util.spec_from_file_location("hs_bad_env", AI / "hypergraph_search.py")
    with pytest.raises(ValueError, match="MODEL_SCOUT_CORPUS"):
        spec.loader.exec_module(importlib.util.module_from_spec(spec))


def test_env_selects_v2_paths_together(monkeypatch):
    monkeypatch.setenv("MODEL_SCOUT_CORPUS", "v2")
    spec = importlib.util.spec_from_file_location("hs_v2_env", AI / "hypergraph_search.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert (module.HYPERGRAPH_DIR.name, module.DATASET_INDEX_DIR.name) == ("hypergraph_v2", "dataset_index_v2")


def test_switching_corpus_switches_graph_vectors_and_query_model(corpora):
    _, (graph_dir, docs_dir) = corpora
    assert set(hs.load_graph()[0]) == {"dataset:old/x"} and hs.query_model() == "v1-model"
    identity = hs.use_corpus("v2")
    assert identity == {"corpus": "v2", "corpus_id": cm.load_manifest(graph_dir)["stage_id"],
                        "documents_id": cm.load_manifest(docs_dir)["stage_id"], "vectors": "local"}
    assert set(hs.load_graph()[0]) == {"dataset:org/a", "dataset:org/b"}
    assert hs.query_model() == MODEL
    scores = hs.dense_scores(vector("org/a"))
    assert set(scores) == {"org/a", "org/b"}
    hs.use_corpus("v1")
    assert set(hs.load_graph()[0]) == {"dataset:old/x"} and set(hs.dense_scores([1.0, 0.0, 0.0])) == {"old/x"}


def test_query_embedding_cache_is_per_model(corpora, monkeypatch):
    calls = []
    monkeypatch.setattr(hs, "_embed_query", lambda text, model: calls.append((text, model)) or [0.0])
    hs.embed_query("질의")
    hs.use_corpus("v2")
    hs.embed_query("질의")
    assert calls == [("질의", "v1-model"), ("질의", MODEL)]


def test_v2_without_vectors_refuses_instead_of_using_supabase(tmp_path, monkeypatch, corpora):
    graph_dir, docs_dir = build_v2(tmp_path / "plain", monkeypatch, embed=False)
    monkeypatch.setattr(hs, "CORPORA", {**hs.CORPORA, "v2": (graph_dir, docs_dir)})
    with pytest.raises(hs.CorpusMismatch, match="벡터 없음"):
        hs.use_corpus("v2")
    with pytest.raises(hs.CorpusMismatch):
        hs.dense_scores([1.0, 0.0, 0.0])
    with pytest.raises(hs.CorpusMismatch):
        hs.load_graph()


def test_v2_graph_changed_after_documents_is_refused(corpora):
    _, (graph_dir, _) = corpora
    with open(graph_dir / "entities.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"entity_id": "dataset:org/c", "kind": "dataset"}) + "\n")
    with pytest.raises(hs.CorpusMismatch, match="entities.jsonl 변경됨"):
        hs.use_corpus("v2")


def test_v2_vectors_of_other_documents_are_refused(corpora, tmp_path, monkeypatch):
    _, (_, docs_dir) = corpora
    other_graph, other_docs = build_v2(tmp_path / "other", monkeypatch, names=("org/a", "org/z"))
    (docs_dir / "embeddings.npy").write_bytes((other_docs / "embeddings.npy").read_bytes())
    (docs_dir / "manifest.json").write_text((other_docs / "manifest.json").read_text(encoding="utf-8"), encoding="utf-8")
    with pytest.raises(hs.CorpusMismatch, match="documents_id"):
        hs.use_corpus("v2")


def test_unknown_corpus_name_is_rejected(corpora):
    with pytest.raises(ValueError):
        hs.use_corpus("v3")
