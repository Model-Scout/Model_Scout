"""코퍼스 빌드 기록 회귀 테스트. 외부 호출 없음.

    python -m pytest -q test/test_corpus_manifest.py
"""

import json
import sys
from pathlib import Path

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))

import corpus_manifest as cm  # noqa: E402


def build(tmp_path, source_text="입력\n", output_text="산출\n", options=None):
    (tmp_path / "docs").mkdir(exist_ok=True)
    (tmp_path / "docs" / "a.md").write_text("문서", encoding="utf-8")
    source, code, out = tmp_path / "in.jsonl", tmp_path / "code.py", tmp_path / "out"
    source.write_text(source_text, encoding="utf-8")
    code.write_text("x = 1\n", encoding="utf-8")
    out.mkdir(exist_ok=True)
    (out / "chunks.jsonl").write_text(output_text, encoding="utf-8")
    return cm.write_manifest(
        out,
        stage="documents",
        corpus="v2",
        options=options or {"embed": False},
        inputs=[source, tmp_path / "docs"],
        code=[code],
        outputs=[out / "chunks.jsonl"],
        counts={"chunks": 1},
        upstream={"corpus_id": "graph-id"},
        root=tmp_path,
    )


def test_manifest_records_what_later_stages_compare(tmp_path):
    manifest = build(tmp_path)
    assert manifest["corpus"] == "v2" and manifest["options"] == {"embed": False}
    assert manifest["created_at"] and manifest["counts"] == {"chunks": 1}
    assert manifest["inputs"][0]["rows"] == 1 and manifest["inputs"][1]["files"] == 1
    assert manifest["outputs"][0]["sha256"] == cm.sha256_file(tmp_path / "out" / "chunks.jsonl")
    assert json.loads((tmp_path / "out" / cm.MANIFEST_NAME).read_text(encoding="utf-8"))["stage_id"] == manifest["stage_id"]
    assert cm.check_manifest(tmp_path / "out", tmp_path) == []


def test_stage_id_ignores_time_and_git_but_not_content(tmp_path):
    first = build(tmp_path)
    assert build(tmp_path)["stage_id"] == first["stage_id"]
    assert build(tmp_path, source_text="다른 입력\n")["stage_id"] != first["stage_id"]
    assert build(tmp_path, output_text="다른 산출\n")["stage_id"] != first["stage_id"]
    assert build(tmp_path, options={"embed": True})["stage_id"] != first["stage_id"]


def test_check_finds_changed_files(tmp_path):
    for name, change in (
        ("out/chunks.jsonl", "바뀜\n"),
        ("in.jsonl", "바뀜\n"),
        ("code.py", "x = 2\n"),
        ("docs/a.md", "바뀜"),
    ):
        build(tmp_path)
        assert cm.check_manifest(tmp_path / "out", tmp_path) == []
        (tmp_path / name).write_text(change, encoding="utf-8")
        assert cm.check_manifest(tmp_path / "out", tmp_path), name


def test_missing_or_tampered_manifest_is_a_problem(tmp_path):
    assert cm.check_manifest(tmp_path, tmp_path)
    build(tmp_path)
    path = tmp_path / "out" / cm.MANIFEST_NAME
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["counts"]["chunks"] = 1
    manifest["options"]["embed"] = True
    path.write_text(json.dumps(manifest), encoding="utf-8")
    assert any("stage_id" in problem for problem in cm.check_manifest(tmp_path / "out", tmp_path))


def test_documents_must_come_from_this_graph(tmp_path):
    graph_root = tmp_path / "graph"
    graph_root.mkdir()
    graph = build(graph_root)
    documents_root = tmp_path / "documents"
    documents_root.mkdir()
    build(documents_root)
    problems = cm.check_corpus(graph_root / "out", documents_root / "out", root=graph_root)
    assert any("그래프" in problem for problem in problems)
    assert graph["stage_id"]


def test_git_state_identifies_uncommitted_work():
    state = cm.git_state()
    assert state is None or {"commit", "branch", "dirty", "tracked_diff_sha256", "untracked_files"} <= state.keys()


# 14가 그래프 생성 이후 바뀐 원본·코드·그래프를 감지하고 문서 생성·임베딩 전에 멈추는지
import importlib.util  # noqa: E402

import pytest  # noqa: E402

_spec = importlib.util.spec_from_file_location("chunks14_gate", AI / "14_build_dataset_chunks.py")
chunks14 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chunks14)
REAL_DB_VECTORS = chunks14.db_vectors


def graph(tmp_path):
    source, code, graph_dir, out_dir = tmp_path / "src.jsonl", tmp_path / "13.py", tmp_path / "graph", tmp_path / "docs"
    source.write_text('{"dataset_id": "a"}\n', encoding="utf-8")
    code.write_text("x = 1\n", encoding="utf-8")
    graph_dir.mkdir()
    (graph_dir / "entities.jsonl").write_text("", encoding="utf-8")
    cm.write_manifest(graph_dir, stage="hypergraph", corpus="v2", options={}, inputs=[source], code=[code],
                      outputs=[graph_dir / "entities.jsonl"], counts={})
    return {"input": source, "code": code, "output": graph_dir / "entities.jsonl"}, graph_dir, out_dir


def run_14(monkeypatch, graph_dir, out_dir):
    monkeypatch.setattr(chunks14, "CORPUS_DIRS", {"v2": (graph_dir, out_dir)})
    monkeypatch.setattr(chunks14, "embed", lambda *a, **k: pytest.fail("임베딩까지 진행됨"))
    monkeypatch.setattr(sys, "argv", ["14", "--corpus", "v2", "--embed"])
    with pytest.raises(SystemExit) as stop:
        chunks14.main()
    return str(stop.value)


@pytest.mark.parametrize("changed", ["input", "code", "output"])
def test_14_stops_before_documents_when_graph_is_stale(tmp_path, monkeypatch, changed):
    files, graph_dir, out_dir = graph(tmp_path)
    files[changed].write_text(files[changed].read_text(encoding="utf-8") + "\n", encoding="utf-8")
    message = run_14(monkeypatch, graph_dir, out_dir)
    assert "stale" in message and f"{files[changed].name} 변경됨" in message
    assert not (out_dir / "chunks.jsonl").exists() and not (out_dir / "embeddings.npy").exists()


def test_14_stops_when_a_recorded_source_is_gone(tmp_path, monkeypatch):
    files, graph_dir, out_dir = graph(tmp_path)
    files["input"].unlink()
    assert "src.jsonl 없음" in run_14(monkeypatch, graph_dir, out_dir)


def test_14_passes_gate_when_nothing_changed(tmp_path, monkeypatch):
    _, graph_dir, out_dir = graph(tmp_path)
    assert "stale" not in run_14(monkeypatch, graph_dir, out_dir)  # 빈 그래프라 다음 단계에서 멈춤


def test_graph_code_list_covers_local_imports():
    source = (AI / "13_build_hypergraph.py").read_text(encoding="utf-8")
    for module in ("dataset_dedup.py", "taxonomy.py", "retrieval_metadata.py", "corpus_manifest.py"):
        assert f'"{module}"' in source


# 임베딩 전후 documents_id와 고정 버전이 유지되고, 벡터 기록이 그 문서에 연결되는지 (유료 호출 없음)


@pytest.fixture
def tiny_corpus(tmp_path, monkeypatch):
    hf, graph_dir, out_dir = tmp_path / "hf.jsonl", tmp_path / "graph", tmp_path / "docs"
    rows = [{"dataset_id": "org/a", "description": "알파 데이터", "downloads": 1},
            {"dataset_id": "org/b", "description": "베타 데이터", "downloads": 2}]
    hf.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    graph_dir.mkdir()
    entities = [{"entity_id": f"dataset:{r['dataset_id']}", "kind": "dataset", "readme_status": "missing"} for r in rows]
    (graph_dir / "entities.jsonl").write_text("".join(json.dumps(e) + "\n" for e in entities), encoding="utf-8")
    for name in ("concepts.jsonl", "links.jsonl"):
        (graph_dir / name).write_text("", encoding="utf-8")
    outputs = [graph_dir / n for n in ("entities.jsonl", "concepts.jsonl", "links.jsonl")]
    cm.write_manifest(graph_dir, stage="hypergraph", corpus="v2", options={}, inputs=[hf], code=[], outputs=outputs, counts={})
    monkeypatch.setattr(chunks14, "CORPUS_DIRS", {"v2": (graph_dir, out_dir)})
    monkeypatch.setattr(chunks14, "DATA_DIR", tmp_path)  # no real README folders
    monkeypatch.setattr(chunks14, "DATASET_INPUT", hf)
    monkeypatch.setattr(chunks14, "KAGGLE_INPUT", tmp_path / "none.jsonl")
    monkeypatch.setattr(chunks14, "PUBLIC_INPUTS", {"v2": tmp_path / "none.jsonl"})
    embedded = []

    def fake_embed(texts, model):
        embedded.extend(texts)
        return [[float(len(t)), 1.0, 0.0] for t in texts]

    monkeypatch.setattr(chunks14, "embed", fake_embed)
    monkeypatch.setattr(chunks14, "db_vectors", lambda hashes, required=False: ({}, "not_configured"))
    monkeypatch.setattr("dotenv.load_dotenv", lambda *a, **k: None)
    return graph_dir, out_dir, embedded


def run_docs(monkeypatch, *flags):
    monkeypatch.setattr(sys, "argv", ["14", "--corpus", "v2", *flags])
    chunks14.main()


def test_embedding_keeps_documents_id_and_the_pin(tiny_corpus, monkeypatch, tmp_path):
    import public_v2_pipeline as pipeline

    graph_dir, out_dir, embedded = tiny_corpus
    run_docs(monkeypatch)
    before = cm.load_manifest(out_dir)["stage_id"]
    assert cm.check_vectors(out_dir) == ["벡터 없음 (14 --embed 전)"]
    monkeypatch.setattr(pipeline, "STAGES", (("hypergraph", graph_dir), ("documents", out_dir)))
    monkeypatch.setattr(pipeline, "PIN", tmp_path / "data_version.json")
    pin = {"stages": {"hypergraph": {"stage_id": cm.load_manifest(graph_dir)["stage_id"]}, "documents": {"stage_id": before}}}
    (tmp_path / "data_version.json").write_text(json.dumps(pin), encoding="utf-8")

    run_docs(monkeypatch, "--embed")
    assert cm.load_manifest(out_dir)["stage_id"] == before and pipeline.verify_pin() == []
    record = json.loads((out_dir / "manifest.json").read_text(encoding="utf-8"))
    assert record["documents_id"] == before and record["corpus_id"] == cm.load_manifest(graph_dir)["stage_id"]
    assert record["embedding_run"]["embedded"] == 2 and record["embedding_run"]["reused_local"] == 0
    assert cm.check_vectors(out_dir) == [] and len(embedded) == 2

    run_docs(monkeypatch, "--embed")  # 같은 문서: 다시 임베딩하지 않고 ID도 그대로
    record = json.loads((out_dir / "manifest.json").read_text(encoding="utf-8"))
    assert record["embedding_run"]["embedded"] == 0 and record["embedding_run"]["reused_local"] == 2
    assert cm.load_manifest(out_dir)["stage_id"] == before and len(embedded) == 2 and cm.check_vectors(out_dir) == []


def test_documents_id_follows_the_embedding_model(tiny_corpus, monkeypatch):
    _, out_dir, _ = tiny_corpus
    run_docs(monkeypatch)
    before = cm.load_manifest(out_dir)["stage_id"]
    monkeypatch.setattr(chunks14, "EMBEDDING_MODEL", "another-embedding-model")
    run_docs(monkeypatch)
    assert cm.load_manifest(out_dir)["stage_id"] != before


@pytest.mark.parametrize("break_it", ["documents", "vectors", "order"])
def test_vectors_that_do_not_belong_to_the_documents_are_rejected(tiny_corpus, monkeypatch, break_it):
    import numpy as np

    _, out_dir, _ = tiny_corpus
    run_docs(monkeypatch, "--embed")
    if break_it == "documents":  # 문서를 다시 만들었는데 벡터는 예전 것
        (out_dir / "build_manifest.json").write_text(
            (out_dir / "build_manifest.json").read_text(encoding="utf-8").replace('"stage_id": "', '"stage_id": "x'), encoding="utf-8")
    elif break_it == "vectors":
        np.save(out_dir / "embeddings.npy", np.zeros((2, 3), dtype=np.float16))
    else:
        record = json.loads((out_dir / "manifest.json").read_text(encoding="utf-8"))
        record["text_hashes"].reverse()
        (out_dir / "manifest.json").write_text(json.dumps(record), encoding="utf-8")
    assert cm.check_vectors(out_dir)


def edit_json(path, change):
    data = json.loads(path.read_text(encoding="utf-8"))
    change(data)
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


@pytest.mark.parametrize("where", ["record", "chunks"])
def test_same_texts_under_other_chunk_ids_are_rejected(tiny_corpus, monkeypatch, where):
    _, out_dir, _ = tiny_corpus
    run_docs(monkeypatch, "--embed")
    assert cm.check_vectors(out_dir) == []
    if where == "record":  # 벡터 기록에서 두 청크의 ID만 맞바꿈 (텍스트 해시는 그대로)
        edit_json(out_dir / "manifest.json", lambda r: r["chunk_ids"].reverse())
    else:  # 청크 파일이 같은 텍스트를 다른 데이터 ID로 들고 있음
        rows = [json.loads(line) for line in (out_dir / "chunks.jsonl").read_text(encoding="utf-8").splitlines()]
        rows[0]["chunk_id"] = "org/other#card"
        (out_dir / "chunks.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    problems = cm.check_vectors(out_dir)
    assert problems == ["벡터 기록의 chunk_ids가 chunks.jsonl의 청크 ID·순서와 다름"]


def test_vector_rows_and_dimension_are_checked_against_the_file(tiny_corpus, monkeypatch):
    import numpy as np

    _, out_dir, _ = tiny_corpus
    run_docs(monkeypatch, "--embed")
    edit_json(out_dir / "manifest.json", lambda r: r.update(dimension=1536))
    assert any("벡터 차원 다름" in p for p in cm.check_vectors(out_dir))
    edit_json(out_dir / "manifest.json", lambda r: r.update(dimension=3))
    # 기록된 해시까지 맞춘 파일이라도 행 수가 다르면 거부
    np.save(out_dir / "embeddings.npy", np.zeros((3, 3), dtype=np.float16))
    edit_json(out_dir / "manifest.json", lambda r: r["embedding_run"].update(vectors_sha256=cm.sha256_file(out_dir / "embeddings.npy")))
    assert any("벡터 행 수 다름" in p for p in cm.check_vectors(out_dir))


def plan_of(capsys):
    line = next(l for l in capsys.readouterr().out.splitlines() if l.startswith("[EMBED PLAN] "))
    return json.loads(line[len("[EMBED PLAN] "):])


@pytest.mark.parametrize("flags", [("--dry-run",), ("--embed", "--dry-run")])
def test_dry_run_plans_without_the_api_or_saving_vectors(tiny_corpus, monkeypatch, capsys, flags):
    _, out_dir, embedded = tiny_corpus
    run_docs(monkeypatch)
    before = cm.load_manifest(out_dir)["stage_id"]
    capsys.readouterr()
    run_docs(monkeypatch, *flags)
    plan = plan_of(capsys)
    assert plan["dry_run"] and plan["db_read"] == "not_configured"
    assert (plan["unique_texts"], plan["reused_local"], plan["reused_db"], plan["new"]) == (2, 0, 0, 2)
    assert plan["documents_id"] == before == cm.load_manifest(out_dir)["stage_id"]
    assert embedded == [] and not (out_dir / "embeddings.npy").exists() and not (out_dir / "manifest.json").exists()


def test_dry_run_after_embedding_counts_local_reuse(tiny_corpus, monkeypatch, capsys):
    _, out_dir, embedded = tiny_corpus
    run_docs(monkeypatch, "--embed")
    record = (out_dir / "manifest.json").read_text(encoding="utf-8")
    capsys.readouterr()
    run_docs(monkeypatch, "--dry-run")
    plan = plan_of(capsys)
    assert (plan["reused_local"], plan["new"]) == (2, 0) and len(embedded) == 2
    assert (out_dir / "manifest.json").read_text(encoding="utf-8") == record  # 벡터 기록 그대로


@pytest.mark.parametrize("flags", [("--embed",), ("--dry-run",)])
def test_max_new_stops_before_the_api(tiny_corpus, monkeypatch, flags):
    _, out_dir, embedded = tiny_corpus
    with pytest.raises(SystemExit, match="exceed --max-new 1"):
        run_docs(monkeypatch, *flags, "--max-new", "1")
    assert embedded == [] and not (out_dir / "embeddings.npy").exists()


def test_max_new_within_the_limit_embeds(tiny_corpus, monkeypatch):
    _, out_dir, embedded = tiny_corpus
    run_docs(monkeypatch, "--embed", "--max-new", "2")
    assert len(embedded) == 2 and cm.check_vectors(out_dir) == []


def unreachable():
    raise ConnectionError("db down")


@pytest.mark.parametrize("configured, connect", [(False, None), (True, unreachable)])
def test_required_db_reuse_stops_when_the_db_cannot_be_read(tiny_corpus, monkeypatch, configured, connect):
    import supabase_db

    _, out_dir, embedded = tiny_corpus
    monkeypatch.setattr(chunks14, "db_vectors", REAL_DB_VECTORS)
    monkeypatch.setattr(supabase_db, "configured", lambda: configured)
    if connect:
        monkeypatch.setattr(supabase_db, "db_connection", connect)
    for flags in (("--embed",), ("--dry-run",)):
        with pytest.raises(SystemExit, match="DB reuse required but unavailable"):
            run_docs(monkeypatch, *flags, "--require-db-reuse")
    assert embedded == [] and not (out_dir / "embeddings.npy").exists()


def test_best_effort_db_reuse_is_unchanged_without_the_flag(tiny_corpus, monkeypatch, capsys):
    import supabase_db

    _, out_dir, embedded = tiny_corpus
    monkeypatch.setattr(chunks14, "db_vectors", REAL_DB_VECTORS)
    monkeypatch.setattr(supabase_db, "configured", lambda: False)
    run_docs(monkeypatch, "--embed")  # dataset-refresh.yml의 `14 --embed`와 같은 동작
    assert plan_of(capsys)["db_read"] == "not_configured" and len(embedded) == 2
