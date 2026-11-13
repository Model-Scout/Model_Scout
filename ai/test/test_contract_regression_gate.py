"""Stage 2 최신성, 증분 계약 게이트, baseline 회귀 검사.

① Stage 2 는 Hub revision(SHA, 없으면 last_modified)이 같을 때만 이전 결과를 재사용한다.
   전에는 다운로드 수·태그만 같으면 Hub 에서 바뀐 모델도 SKIP 했다.
② 증분(--refresh) 경로도 Stage 2 뒤, Stage 3(LLM) 앞에서 계약 게이트를 돈다.
③ 게이트는 Stage 2 가 덮어쓰기 전의 계약 레코드를 baseline 으로 비교한다. 같은 Hub
   revision 에서 값을 잃으면 실패, revision 이 바뀐 모델은 경고, 새 모델·첫 실행은 통과다.

외부 API·DB·LLM 은 부르지 않는다. 하위 프로세스는 contract/validate.py 만 실제로 돈다.

    python test/test_contract_regression_gate.py
"""

from __future__ import annotations

import contextlib
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


stage2 = _load("stage2_for_regression_test", "02_enrich_metadata.py")
sync = _load("sync_for_regression_test", "08_sync_supabase.py")
EXAMPLE = json.loads((ROOT / "contract" / "examples.json").read_text(encoding="utf-8"))[0]


@contextlib.contextmanager
def patched(target: Any, **attrs: Any):
    old = {name: getattr(target, name) for name in attrs}
    for name, value in attrs.items():
        setattr(target, name, value)
    try:
        yield
    finally:
        for name, value in old.items():
            setattr(target, name, value)


# ── ① Stage 2 revision ───────────────────────────────────────────────────

def _stage1(model_id: str, sha: str | None = "a" * 40, modified: str | None = "2026-11-01T00:00:00Z"):
    return {
        "model_id": model_id,
        "hub": {"sha": sha, "last_modified": modified},
        "stage": {"stage1_version": 7},
        "candidate": {"tier": "A_verified", "type": "korean_explicit"},
        "popularity": {"downloads": 1000},
        "family": {},
        "quality": {},
        "language": {},
        "primary_task": "text-generation",
        "matched_tasks": ["text-generation"],
    }


def _stage2_from(stage1_row: Dict[str, Any], pool: str = "core", **revision: Any) -> Dict[str, Any]:
    """stage1_row 로 만들어진 것처럼 보이는, 재사용 조건을 모두 갖춘 Stage 2 행."""
    stage = {
        "source_pool": pool,
        "source_stage1_version": 7,
        "metadata_enriched": True,
        "semantic_enriched": False,
        "stage2_version": stage2.STAGE2_VERSION,
        **stage2.source_revision(stage1_row),
        **revision,
    }
    return {
        "model_id": stage1_row["model_id"],
        "candidate": stage1_row["candidate"],
        "popularity": {"stage1": stage1_row["popularity"]},
        "family": stage1_row["family"],
        "stage1_quality": stage1_row["quality"],
        "language": {"stage1": stage1_row["language"]},
        "task": {"primary": stage1_row["primary_task"], "matched": stage1_row["matched_tasks"]},
        "stage": stage,
    }


def test_same_sha_is_reused():
    source = _stage1("m/a")
    assert stage2.resume_matches(_stage2_from(source), source, "core")


def test_different_sha_is_collected_again():
    source = _stage1("m/a", sha="b" * 40)
    old = _stage2_from(_stage1("m/a", sha="a" * 40))
    assert not stage2.revision_matches(old, source)
    assert not stage2.resume_matches(old, source, "core"), "Hub 가 바뀐 모델을 재사용했다"


def test_last_modified_is_compared_when_there_is_no_sha():
    source = _stage1("m/a", sha=None, modified="2026-11-02T00:00:00Z")
    same = _stage2_from(source)
    older = _stage2_from(_stage1("m/a", sha=None, modified="2026-11-01T00:00:00Z"))
    assert stage2.revision_matches(same, source)
    assert not stage2.revision_matches(older, source)


def test_row_without_recorded_revision_is_collected_again():
    source = _stage1("m/a")
    legacy = _stage2_from(source)
    legacy["stage"].pop("source_sha")
    legacy["stage"].pop("source_last_modified")
    assert not stage2.resume_matches(legacy, source, "core")
    unknown_both = _stage1("m/a", sha=None, modified=None)
    assert not stage2.revision_matches(_stage2_from(unknown_both), unknown_both)


def test_enrich_records_the_source_revision_in_stage():
    # build_row 전체를 돌리지 않고, stage 블록이 source_revision 을 펼쳐 넣는지 소스로 확인한다.
    source = (ROOT / "02_enrich_metadata.py").read_text(encoding="utf-8")
    assert "**source_revision(stage1_row)," in source


def test_incremental_changed_model_is_not_skipped():
    """증분 Stage 1 이 바꾼 모델(SHA 변경)은 --model-ids-file 로 와서 다시 수집된다."""
    unchanged = _stage1("m/unchanged")
    changed_now = _stage1("m/changed", sha="c" * 40)
    changed_before = _stage1("m/changed", sha="a" * 40)
    enriched: List[str] = []

    def fake_enrich(row, pool):
        enriched.append(row["model_id"])
        new = _stage2_from(row, pool)
        new["contract"] = {"model_id": row["model_id"]}
        return new

    with tempfile.TemporaryDirectory() as name:
        data = Path(name)
        config = {
            "input": data / "stage1.jsonl",
            "output": data / "stage2.jsonl",
            "contract_output": data / "contract.jsonl",
            "readme_dir": data / "readmes",
        }
        config["input"].write_text(
            "".join(json.dumps(r) + "\n" for r in (unchanged, changed_now)), encoding="utf-8")
        config["output"].write_text(
            "".join(json.dumps(_stage2_from(r)) + "\n" for r in (unchanged, changed_before)), encoding="utf-8")
        with patched(stage2, DATA_DIR=data, POOL_CONFIGS={**stage2.POOL_CONFIGS, "core": config},
                     enrich=fake_enrich, validate_stage2_rows=lambda rows, pool: None,
                     language_exclusions=lambda rows: {}, REQUEST_SLEEP=0, print_pool_stats=lambda *a: None):
            stage2.process_pool("core", model_ids={"m/unchanged", "m/changed"})
        saved = {json.loads(line)["model_id"]: json.loads(line) for line in
                 config["output"].read_text(encoding="utf-8").splitlines()}
    assert enriched == ["m/changed"], enriched
    assert saved["m/changed"]["stage"]["source_sha"] == "c" * 40


# ── ③ baseline 회귀 검사 (contract/validate.py) ───────────────────────────

def _record(model_id: str = EXAMPLE["model_id"], *, dtype: Any = "keep", revision: str | None = None):
    record = copy.deepcopy(EXAMPLE)
    record["model_id"] = model_id
    if revision is not None:
        record["identity"]["revision"] = revision
    if dtype != "keep":
        record["technical"]["dtype"] = dtype
        record["provenance"]["fields"]["technical.dtype"] = {
            "status": "unknown", "confidence": "none", "source": [], "retrieved_at": "2026-11-20T00:00:00Z",
        }
    return record


def _validate(records: List[Dict[str, Any]], baseline: List[Dict[str, Any]] | None):
    with tempfile.TemporaryDirectory() as name:
        folder = Path(name)
        new = folder / "new.jsonl"
        new.write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")
        command = [sys.executable, str(ROOT / "contract" / "validate.py"), str(new),
                   "--summary-json", str(folder / "summary.json")]
        if baseline is not None:
            (folder / "old.jsonl").write_text("".join(json.dumps(r) + "\n" for r in baseline), encoding="utf-8")
            command += ["--baseline", str(folder / "old.jsonl")]
        done = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        return done.returncode, json.loads((folder / "summary.json").read_text(encoding="utf-8")), done.stdout


def test_value_loss_at_the_same_revision_fails():
    code, summary, out = _validate([_record(dtype=None)], [_record()])
    assert code == 1 and summary["regressed_models"] == 1
    assert "값 손실" in out


def test_value_loss_after_a_hub_change_is_only_a_warning():
    code, summary, _ = _validate([_record(dtype=None, revision="f" * 40)], [_record()])
    assert code == 0 and summary["source_changed_models"] == 1 and summary["regressed_models"] == 0


def test_new_model_without_baseline_passes():
    code, summary, _ = _validate([_record("org/brand-new")], [_record()])
    assert code == 0 and summary["new_models"] == 1


def test_first_contract_run_without_baseline_passes():
    code, summary, _ = _validate([_record(dtype=None)], None)
    assert code == 0 and summary["baseline"] is None


def test_removed_model_is_not_a_contract_error():
    """baseline 에만 있는 모델(Stage 1 에서 빠진 모델)은 검사 대상이 아니다."""
    code, _, _ = _validate([_record()], [_record(), _record("org/removed")])
    assert code == 0


# ── 08: 게이트 연결 ───────────────────────────────────────────────────────

def _write_contract(data: Path, pool: str, records: List[Dict[str, Any]]):
    (data / f"hf_models_stage2_contract_{pool}.jsonl").write_text(
        "".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")


def test_baseline_snapshot_merges_both_pools_and_is_none_on_first_run():
    with tempfile.TemporaryDirectory() as name, tempfile.TemporaryDirectory() as dest:
        data = Path(name)
        with patched(sync, DATA_DIR=data):
            assert sync.snapshot_contract_baseline(Path(dest)) is None
            _write_contract(data, "core", [_record("a/core")])
            _write_contract(data, "low_popularity", [_record("a/low")])
            baseline = sync.snapshot_contract_baseline(Path(dest))
        ids = [json.loads(line)["model_id"] for line in baseline.read_text(encoding="utf-8").splitlines()]
        assert ids == ["a/core", "a/low"]


def test_contract_gate_records_why_the_baseline_was_skipped_and_fails_on_regression():
    with tempfile.TemporaryDirectory() as name, tempfile.TemporaryDirectory() as dest:
        data = Path(name)
        for pool in sync.POOLS:
            _write_contract(data, pool, [_record(f"m/{pool}")])
        with patched(sync, DATA_DIR=data):
            first = sync.contract_gate(require=True)
            assert first["baseline"] is None and "첫 계약 실행" in first["baseline_skipped"]
            assert first["core"]["summary"]["records"] == 1
            baseline = sync.snapshot_contract_baseline(Path(dest))
            _write_contract(data, "core", [_record("m/core", dtype=None)])
            try:
                sync.contract_gate(require=True, baseline=baseline)
            except RuntimeError as error:
                assert "계약 위반" in str(error)
            else:
                raise AssertionError("같은 revision 에서 값을 잃었는데 통과했다")


def _paid(commands: List[List[str]]) -> List[str]:
    names = [Path(command[1]).name for command in commands]
    return [n for n in names if n.startswith(("03_", "04_", "06_", "evidence_index"))]


def _incremental(gate):
    commands: List[List[str]] = []
    order: List[str] = []

    def run(command):
        commands.append(command)
        order.append(Path(command[1]).name)

    def recording_gate(require=False, baseline=None):
        order.append("contract_gate")
        return gate(require, baseline)

    scan = {"processable_ids": ["m/changed"], "removed_ids": []}
    with tempfile.TemporaryDirectory() as name:
        data = Path(name)
        _write_contract(data, "core", [_record("m/changed")])
        with patched(sync, DATA_DIR=data, MODEL_IDS_PATH=data / "ids.json",
                     BENCHMARK_CHANGED_IDS_PATH=data / "bench.json",
                     incremental_stage1_update=lambda watermark: dict(scan),
                     stage3_pools_need_reconciliation=lambda: False,
                     clear_incremental_artifacts=lambda: None,
                     run_command=run, contract_gate=recording_gate):
            try:
                sync.incremental_refresh_pipeline("2026-11-01T00:00:00Z")
            except RuntimeError:
                pass
    return order, commands


def test_incremental_runs_the_contract_gate_between_stage2_and_stage3():
    seen: Dict[str, Any] = {}

    def gate(require, baseline):
        seen["baseline"] = baseline.read_text(encoding="utf-8") if baseline else None
        return {"ok": True}

    order, _ = _incremental(gate)
    assert order.index("02_enrich_metadata.py") < order.index("contract_gate") < order.index(
        "03_generate_semantic_metadata.py"), order
    assert seen["baseline"] and "m/changed" in seen["baseline"], "Stage 2 전 계약 레코드를 baseline 으로 넘겨야 한다"


def test_incremental_contract_failure_stops_before_paid_stages():
    def gate(require, baseline):
        raise RuntimeError("[core] 데이터 계약 위반")

    order, commands = _incremental(gate)
    assert "02_enrich_metadata.py" in order and _paid(commands) == [], order


def _full_reingest(gate):
    commands: List[List[str]] = []
    with tempfile.TemporaryDirectory() as name:
        data = Path(name)
        for pool in sync.POOLS:
            (data / f"hf_models_stage1_{pool}.jsonl").write_text(json.dumps({"model_id": f"m/{pool}"}) + "\n")
            (data / f"hf_models_stage2_{pool}.jsonl").write_text(json.dumps({"model_id": f"m/{pool}"}) + "\n")
        with patched(sync, DATA_DIR=data, run_command=commands.append, contract_gate=gate,
                     clear_incremental_artifacts=lambda: None):
            try:
                sync.full_reingest_pipeline("2026-10-31T00:00:00+00:00")
            except RuntimeError:
                pass
    return commands


def test_full_reingest_gate_gets_no_baseline_on_the_first_contract_run():
    seen: Dict[str, Any] = {}

    def gate(require, baseline):
        seen["baseline"] = baseline
        return {}

    commands = _full_reingest(gate)
    assert seen["baseline"] is None
    assert [Path(c[1]).name for c in commands][0] == "02_enrich_metadata.py"


def test_full_reingest_contract_failure_stops_before_paid_stages():
    def gate(require, baseline):
        raise RuntimeError("[core] 데이터 계약 위반")

    assert _paid(_full_reingest(gate)) == []


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
