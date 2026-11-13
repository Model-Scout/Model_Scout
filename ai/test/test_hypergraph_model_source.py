"""하이퍼그래프의 모델 원본(--model-source)과 운영 정합성.

Stage 4 파일은 Git LFS 라서 LFS 없이 checkout 하면 그 경로에 pointer 가 있다. "파일이 있다"를
"데이터가 있다"로 읽으면 pointer 를 JSON 으로 파싱하다 죽거나, 옛 로컬 스냅샷으로 운영 DB 와 다른
모델 집합의 그래프를 게시한다. 운영(dataset-refresh.yml)은 Supabase active 행만 쓴다.

DB 는 부르지 않는다. Supabase 조회는 가짜로 바꾼다.

    python -m pytest test/test_hypergraph_model_source.py -q
"""

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI))

from corpus_manifest import LFS_POINTER_PREFIX, read_jsonl_snapshot, sha256_text  # noqa: E402

LFS_POINTER = LFS_POINTER_PREFIX.decode() + "\noid sha256:abc\nsize 123\n"


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, AI / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


graph13 = load("graph13_model_source", "13_build_hypergraph.py")


def model(model_id, task="sentence-similarity"):
    return {"model_id": model_id, "source_pool": "core", "task": {"primary": task, "matched": [task]},
            "filter_metadata": {"license": "mit"}}


def write_jsonl(path, rows):
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


@pytest.fixture
def stage4(tmp_path, monkeypatch):
    """임시 Stage 4 두 파일과 가짜 Supabase. supabase["calls"] 로 조회 여부를 본다."""
    paths = (tmp_path / "hf_models_stage4_core.jsonl", tmp_path / "hf_models_stage4_low_popularity.jsonl")
    monkeypatch.setattr(graph13, "MODEL_INPUTS", paths)
    supabase = {"calls": 0, "rows": [model("db/a"), model("db/b"), model("db/c")]}

    def fake_supabase():
        supabase["calls"] += 1
        return list(supabase["rows"])

    monkeypatch.setattr(graph13, "load_supabase_models", fake_supabase)
    return paths, supabase


def real_local(paths):
    write_jsonl(paths[0], [model("local/core")])
    write_jsonl(paths[1], [model("local/low")])


# ── 공용 helper ──────────────────────────────────────────────────────────

def test_snapshot_status_tells_the_cases_apart(tmp_path):
    path = tmp_path / "s.jsonl"
    assert read_jsonl_snapshot(path) == ("missing", None)
    path.write_text("", encoding="utf-8")
    assert read_jsonl_snapshot(path) == ("empty", None)
    path.write_text("\n  \n", encoding="utf-8")
    assert read_jsonl_snapshot(path)[0] == "empty"
    path.write_text(LFS_POINTER, encoding="utf-8")
    assert read_jsonl_snapshot(path) == ("lfs_pointer", None)
    path.write_text('{"model_id": "a"}\n{"model_id": \n', encoding="utf-8")
    assert read_jsonl_snapshot(path) == ("corrupt", None)
    path.write_text('{"model_id": "a"}\n[1, 2]\n', encoding="utf-8")
    assert read_jsonl_snapshot(path)[0] == "corrupt"
    write_jsonl(path, [{"model_id": "a"}, {"model_id": "b"}])
    status, rows = read_jsonl_snapshot(path)
    assert status == "jsonl" and [r["model_id"] for r in rows] == ["a", "b"]


# ── --model-source ──────────────────────────────────────────────────────

def test_auto_uses_a_real_local_snapshot(stage4):
    paths, supabase = stage4
    real_local(paths)
    rows, info = graph13.load_model_rows("auto")
    assert [r["model_id"] for r in rows] == ["local/core", "local/low"]
    assert info["source"] == "local_stage4" and supabase["calls"] == 0


def test_auto_falls_back_to_supabase_without_local_files(stage4):
    _, supabase = stage4
    rows, info = graph13.load_model_rows("auto")
    assert info["source"] == "supabase" and supabase["calls"] == 1
    assert info["local_status"] == {"hf_models_stage4_core.jsonl": "missing",
                                    "hf_models_stage4_low_popularity.jsonl": "missing"}


def test_auto_treats_an_lfs_pointer_as_no_snapshot(stage4):
    paths, supabase = stage4
    for path in paths:
        path.write_text(LFS_POINTER, encoding="utf-8")
    rows, info = graph13.load_model_rows("auto")
    assert info["source"] == "supabase" and len(rows) == 3
    assert set(info["local_status"].values()) == {"lfs_pointer"}


def test_auto_needs_both_files_to_be_real(stage4):
    paths, supabase = stage4
    write_jsonl(paths[0], [model("local/core")])
    paths[1].write_text(LFS_POINTER, encoding="utf-8")
    _, info = graph13.load_model_rows("auto")
    assert info["source"] == "supabase"


def test_local_refuses_an_lfs_pointer(stage4):
    paths, supabase = stage4
    for path in paths:
        path.write_text(LFS_POINTER, encoding="utf-8")
    with pytest.raises(SystemExit, match="lfs_pointer"):
        graph13.load_model_rows("local")
    assert supabase["calls"] == 0, "local 은 Supabase 로 내려가지 않는다"


def test_corrupt_local_file_fails_local_and_is_skipped_by_auto(stage4):
    paths, supabase = stage4
    real_local(paths)
    paths[1].write_text('{"model_id": "x"\n', encoding="utf-8")
    with pytest.raises(SystemExit, match="corrupt"):
        graph13.load_model_rows("local")
    _, info = graph13.load_model_rows("auto")
    assert info["source"] == "supabase" and info["local_status"]["hf_models_stage4_low_popularity.jsonl"] == "corrupt"


def test_supabase_ignores_real_local_files(stage4):
    paths, supabase = stage4
    real_local(paths)
    rows, info = graph13.load_model_rows("supabase")
    assert [r["model_id"] for r in rows] == ["db/a", "db/b", "db/c"]
    assert info["source"] == "supabase" and info["requested_source"] == "supabase"
    assert info["local_status"] == {}, "로컬 파일을 열어 보지도 않는다"
    assert "where active" in info["selection"]


def test_model_id_hash_is_order_independent(stage4):
    _, supabase = stage4
    _, first = graph13.load_model_rows("supabase")
    supabase["rows"] = list(reversed(supabase["rows"]))
    _, second = graph13.load_model_rows("supabase")
    assert first["model_ids_sha256"] == second["model_ids_sha256"] == sha256_text(["db/a", "db/b", "db/c"])
    assert first["count"] == 3


# ── main(): v1 report 에 원본을 남긴다 ───────────────────────────────────

def test_v1_report_records_the_model_source(stage4, tmp_path, monkeypatch):
    paths, supabase = stage4
    real_local(paths)  # 로컬이 있어도 supabase 를 지정하면 무시한다
    out = tmp_path / "graph"
    monkeypatch.setattr(graph13, "CORPUS_DIRS", {"v1": out, "v2": tmp_path / "graph_v2"})
    for name in ("LENGTH_INPUT", "NER_INPUT", "DATASET_INPUT", "KAGGLE_INPUT"):
        monkeypatch.setattr(graph13, name, tmp_path / f"{name}.jsonl")
    monkeypatch.setattr(graph13, "PUBLIC_INPUTS", {"v1": tmp_path / "public.jsonl", "v2": tmp_path / "v2.jsonl"})
    monkeypatch.setattr(sys, "argv", ["13", "--model-source", "supabase"])
    graph13.main()
    report = json.loads((out / "report.json").read_text(encoding="utf-8"))
    assert report["models"]["source"] == "supabase" and report["models"]["count"] == 3
    assert report["entities"]["model"] == 3
    assert report["models"]["model_ids_sha256"] == sha256_text(["db/a", "db/b", "db/c"])
    entities = [json.loads(line) for line in (out / "entities.jsonl").read_text(encoding="utf-8").splitlines()]
    assert sorted(e["entity_id"] for e in entities if e["kind"] == "model") == ["model:db/a", "model:db/b", "model:db/c"]
    assert not (tmp_path / "graph_v2").exists(), "기본 corpus 는 v1 이다"


def test_defaults_stay_v1_and_auto():
    source = (AI / "13_build_hypergraph.py").read_text(encoding="utf-8")
    assert 'default="v1"' in source and 'choices=MODEL_SOURCES, default="auto"' in source
    with pytest.raises(ValueError):
        graph13.load_model_rows("remote")


# ── 운영 workflow ────────────────────────────────────────────────────────

WORKFLOW = AI.parent / ".github" / "workflows" / "dataset-refresh.yml"


def test_dataset_refresh_builds_every_graph_from_supabase():
    flow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
    runs = [step.get("run", "") for step in flow["jobs"]["refresh"]["steps"]]
    calls = [line.strip() for run in runs for line in run.splitlines() if "13_build_hypergraph.py" in line]
    builds = [call for call in calls if "--self-check" not in call and not call.startswith("for ")]
    assert len(builds) == 2, builds  # full 수집 경로와 rebuild 경로
    assert all(call.endswith("--model-source supabase") for call in builds), builds
    assert not any("--corpus v2" in run for run in runs), "공공데이터 v2 로 전환하지 않는다"
    assert "model_ids_sha256" in "".join(runs)


def test_dataset_refresh_schedule_is_unchanged():
    flow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
    crons = [entry["cron"] for entry in flow[True]["schedule"]]  # yaml 은 `on` 을 True 로 읽는다
    assert crons == ["0 19 * * *", "30 17 * * 0"]


def test_dataset_index_sync_has_no_public_v2_cutover():
    source = (AI / "20_sync_dataset_index.py").read_text(encoding="utf-8")
    assert "hypergraph_v2" not in source and "dataset_index_v2" not in source
