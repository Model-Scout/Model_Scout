"""승인한 dry-run 번들을 그대로 적재하는 경로.

dry-run 이 Stage 1~4 산출물과 manifest(파일 SHA256·크기, 모델 ID hash, 저장소·main·커밋·run,
Stage 버전, 직전 sync run)를 번들로 묶는다. apply 는 번들을 검증하고 DATA_DIR 에 그대로 놓은
뒤 DB 에만 쓴다. 검증이 하나라도 실패하면 DB 에 쓰기 전에 멈춘다.

DB·HF·LLM·임베딩은 부르지 않는다. 산출물은 작은 가짜 파일이다.

    python test/test_reingest_bundle.py
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, Iterator, Tuple

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
SPEC = importlib.util.spec_from_file_location("sync_for_bundle_test", ROOT / "08_sync_supabase.py")
assert SPEC is not None and SPEC.loader is not None
sync = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = sync
SPEC.loader.exec_module(sync)

IDENTITY = {"repository": "Model-Scout/Model_Scout", "git_sha": "a" * 40, "git_ref": "main", "run_id": "111"}
REINGEST = {"mode": "reingest", "stage1_mode": "full-scan", "source_watermark": "2026-11-20T09:00:00+00:00",
            "removed_ids": ["m/lang"], "requires_sync": True, "stage4_mode": "full"}
SECRET = "sk-test-should-never-appear"


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


def _fill_data(data: Path) -> None:
    for name in sync.BUNDLE_REQUIRED_FILES:
        rows = [{"model_id": f"m/{i}"} for i in range(2)] if name.startswith("hf_models_stage4_") \
            and name.endswith(".jsonl") else [{"name": name}]
        (data / name).write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
    (data / "hf_models_stage4_low_popularity.jsonl").write_text(json.dumps({"model_id": "m/low"}) + "\n")
    (data / ".hf_models_benchmark_state_candidate.json").write_text('{"m/0": "hash"}\n')
    (data / "hf_models_stage2_core_language_excluded.json").write_text('{"m/lang": "ja"}\n')
    for pool in sync.POOLS:
        (data / "readmes" / pool).mkdir(parents=True)
        (data / "readmes" / pool / "m__0.md").write_text(f"# {pool} README\n", encoding="utf-8")


@contextlib.contextmanager
def bundle(identity: Dict[str, str] = IDENTITY, latest: str | None = "sync-1") -> Iterator[Tuple[Path, Path, Dict]]:
    """임시 DATA_DIR 에서 dry-run 번들을 만든다. (data, bundle_dir, manifest)."""
    with tempfile.TemporaryDirectory() as name:
        data = Path(name) / "data"
        data.mkdir()
        _fill_data(data)
        os.environ["OPENAI_API_KEY"] = SECRET
        try:
            with patched(sync, DATA_DIR=data, git_identity=lambda: dict(identity)):
                manifest = sync.write_reingest_bundle(
                    Path(name) / "bundle", refresh_info=REINGEST, report={"apply": False},
                    stage4_ids=["m/0", "m/1", "m/low"], latest_sync_run_id=latest,
                )
                yield data, Path(name) / "bundle", manifest
        finally:
            os.environ.pop("OPENAI_API_KEY", None)


def _verify(bundle_dir: Path, **over: Any) -> Dict[str, Any]:
    expected = {"approved_run_id": "111", "repository": IDENTITY["repository"],
                "git_sha": IDENTITY["git_sha"], "latest_sync_run_id": "sync-1"}
    expected.update(over)
    return sync.verify_reingest_bundle(bundle_dir, **expected)


def _rejected(bundle_dir: Path, fragment: str, **over: Any) -> None:
    try:
        _verify(bundle_dir, **over)
    except sync.BundleError as error:
        assert fragment in str(error), str(error)
    else:
        raise AssertionError(f"'{fragment}' 를 통과시켰다")


def _rewrite_manifest(bundle_dir: Path, **changes: Any) -> None:
    path = bundle_dir / sync.BUNDLE_MANIFEST
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest.update(changes)
    path.write_text(json.dumps(manifest), encoding="utf-8")


# ── 정상 ─────────────────────────────────────────────────────────────────

def test_a_fresh_bundle_verifies_and_records_its_origin():
    with bundle() as (_, bundle_dir, manifest):
        checked = _verify(bundle_dir)
    assert checked["reingest"] == REINGEST
    assert len(checked["bundle_sha256"]) == 64
    for key, value in (("repository", IDENTITY["repository"]), ("git_sha", IDENTITY["git_sha"]),
                       ("git_ref", "main"), ("dry_run_run_id", "111"), ("stage_versions", sync.EXPECTED_VERSIONS),
                       ("stage1_scan_started_at", REINGEST["source_watermark"]),
                       ("supabase_latest_sync_run_id", "sync-1"), ("model_count", 3)):
        assert manifest[key] == value, key
    assert manifest["model_ids_sha256"] == sync.model_ids_sha256({"m/0", "m/1", "m/low"})
    for entry in manifest["files"]:
        assert set(entry) == {"path", "target", "sha256", "bytes"}


def test_bundle_holds_every_file_the_db_load_and_snapshot_commit_need():
    with bundle() as (_, _, manifest):
        targets = {entry["target"] for entry in manifest["files"]}
    assert set(sync.BUNDLE_REQUIRED_FILES) <= targets
    assert ".hf_models_benchmark_state_candidate.json" in targets
    assert "readmes/core/m__0.md" in targets
    paths = {entry["path"] for entry in manifest["files"]}
    assert not any(part.startswith(".") for path in paths for part in path.split("/")), \
        "upload-artifact 가 숨김 파일을 빼므로 번들 안 경로에 점으로 시작하는 이름이 있으면 안 된다"


def test_bundle_contains_no_secrets():
    with bundle() as (_, bundle_dir, _):
        for path in bundle_dir.rglob("*"):
            if path.is_file():
                assert SECRET not in path.read_text(encoding="utf-8", errors="ignore"), path
        assert not list(bundle_dir.rglob(".env"))


def test_install_puts_the_reviewed_files_back_and_mirrors_readmes():
    with bundle() as (data, bundle_dir, _):
        checked = _verify(bundle_dir)
        (data / "hf_models_stage3_core.jsonl").write_text("changed after the dry-run\n")
        (data / "readmes" / "core" / "stale.md").write_text("not in the bundle\n")
        (data / ".hf_models_benchmark_state_candidate.json").unlink()
        sync.install_reingest_bundle(bundle_dir, checked)
        assert json.loads((data / "hf_models_stage3_core.jsonl").read_text())["name"] == "hf_models_stage3_core.jsonl"
        assert not (data / "readmes" / "core" / "stale.md").exists()
        assert (data / ".hf_models_benchmark_state_candidate.json").exists()


# ── 거부 ─────────────────────────────────────────────────────────────────

def test_missing_file_is_rejected():
    with bundle() as (_, bundle_dir, _):
        (bundle_dir / sync.bundle_path("hf_models_stage2_core.jsonl")).unlink()
        _rejected(bundle_dir, "파일 누락")


def test_tampered_file_is_rejected():
    with bundle() as (_, bundle_dir, _):
        path = bundle_dir / sync.bundle_path("hf_models_stage3_core.jsonl")
        text = path.read_text()
        path.write_text(text.replace("stage3", "stageX"))  # 크기는 같고 내용만 다르다
        _rejected(bundle_dir, "SHA256 불일치")


def test_extra_unlisted_file_is_rejected():
    with bundle() as (_, bundle_dir, _):
        (bundle_dir / "data" / "smuggled.jsonl").write_text("{}\n")
        _rejected(bundle_dir, "manifest 에 없는 파일")


def test_different_git_sha_is_rejected():
    with bundle() as (_, bundle_dir, _):
        _rejected(bundle_dir, "dry-run 이후 main 이 바뀌었다", git_sha="b" * 40)


def test_dry_run_from_another_branch_is_rejected():
    with bundle(identity={**IDENTITY, "git_ref": "feature/x"}) as (_, bundle_dir, _):
        _rejected(bundle_dir, "main 에서 만든 dry-run 이 아니다")


def test_another_repository_or_run_is_rejected():
    with bundle() as (_, bundle_dir, _):
        _rejected(bundle_dir, "다른 저장소", repository="someone/fork")
        _rejected(bundle_dir, "승인한 dry-run 이 아니다", approved_run_id="222")


def test_different_stage_versions_are_rejected():
    with bundle() as (_, bundle_dir, _):
        _rewrite_manifest(bundle_dir, stage_versions={**sync.EXPECTED_VERSIONS, "stage2": 6})
        _rejected(bundle_dir, "Stage 버전")


def test_model_id_hash_mismatch_is_rejected():
    with bundle() as (_, bundle_dir, _):
        _rewrite_manifest(bundle_dir, model_ids_sha256=sync.model_ids_sha256({"m/0"}))
        _rejected(bundle_dir, "Stage 4 모델 집합")


def test_stale_supabase_baseline_is_rejected():
    with bundle() as (_, bundle_dir, _):
        _rejected(bundle_dir, "다른 sync 가 DB 를 바꿨다", latest_sync_run_id="sync-2")


def test_missing_manifest_is_rejected():
    with bundle() as (_, bundle_dir, _):
        (bundle_dir / sync.BUNDLE_MANIFEST).unlink()
        try:
            _verify(bundle_dir)
        except sync.BundleError as error:
            assert "manifest" in str(error)
        else:
            raise AssertionError("manifest 없는 번들을 받았다")


def test_writing_a_bundle_refuses_missing_outputs():
    with tempfile.TemporaryDirectory() as name:
        with patched(sync, DATA_DIR=Path(name), git_identity=lambda: dict(IDENTITY)):
            try:
                sync.write_reingest_bundle(Path(name) / "b", refresh_info=REINGEST, report={},
                                           stage4_ids=[], latest_sync_run_id=None)
            except sync.BundleError as error:
                assert "필요한 산출물이 없다" in str(error)
            else:
                raise AssertionError("빈 DATA_DIR 로 번들을 만들었다")


# ── main(): 검증 전에는 DB 에 쓰지 않는다 ─────────────────────────────────

def _main(argv, **patches):
    with patched(sync, load_dotenv=lambda *a, **k: None, **patches), \
            patched(sys, argv=["08_sync_supabase.py", *argv]), contextlib.redirect_stdout(io.StringIO()):
        return sync.main()


def test_apply_with_a_bad_bundle_never_touches_the_db_or_the_pipeline():
    def refuse(*args, **kwargs):
        raise AssertionError("검증 전에 DB 쓰기·파이프라인을 불렀다")

    with bundle() as (data, bundle_dir, _):
        (bundle_dir / sync.bundle_path("hf_models_stage2_core.jsonl")).write_text("tampered\n")
        try:
            _main(["--reingest", "--apply", "--from-bundle", str(bundle_dir), "--approved-run-id", "111"],
                  latest_completed_sync=lambda any_versions=False: {"run_id": "sync-1"},
                  git_identity=lambda: dict(IDENTITY), full_reingest_pipeline=refuse,
                  run_command=refuse, apply_sync=refuse, install_reingest_bundle=refuse)
        except sync.BundleError:
            pass
        else:
            raise AssertionError("변조된 번들로 apply 가 진행됐다")


def test_dry_run_writes_the_bundle_with_the_latest_sync_run():
    seen: Dict[str, Any] = {}

    def capture(bundle_dir, **kwargs):
        seen.update(kwargs, bundle_dir=bundle_dir)
        return {"files": [], "model_ids_sha256": "x"}

    stage4 = [{"model_id": "m/keep", "source_pool": "core"}]
    code = _main(
        ["--reingest", "--bundle-dir", "out-bundle"],
        latest_completed_sync=lambda any_versions=False: {"run_id": "sync-9", "completed_at": "2026-11-06"},
        full_reingest_pipeline=lambda previous, full_stage1=False: dict(REINGEST, stage1_mode="reuse"),
        load_corpora=lambda stage4_delta=False: (stage4, {"m/keep": {}}, {"m/keep": {}}),
        validate_corpus=lambda *a, **k: {"rows": 1}, load_evidence_indices=lambda: {},
        validate_evidence_indices=lambda *a, **k: {}, write_stage4_manifest=lambda *a, **k: None,
        payloads=lambda *a, **k: [], evidence_payloads=lambda *a, **k: [],
        db_active_model_ids=lambda cur=None: {"m/keep"},
        db_storage=lambda cur=None: {"database": 1, "model_rows": 0},
        apply_sync=lambda *a, **k: (_ for _ in ()).throw(AssertionError("dry-run 이 DB 에 썼다")),
        write_reingest_bundle=capture,
    )
    assert code == 0
    assert seen["bundle_dir"] == Path("out-bundle") and seen["latest_sync_run_id"] == "sync-9"
    assert seen["stage4_ids"] == ["m/keep"] and seen["refresh_info"]["stage1_mode"] == "reuse"


def test_checkpointed_dry_run_skips_stage_generation_and_builds_the_bundle():
    seen: Dict[str, Any] = {}

    def capture(bundle_dir, **kwargs):
        seen.update(kwargs, bundle_dir=bundle_dir)
        return {"files": [], "model_ids_sha256": "x"}

    def refuse(*args, **kwargs):
        raise AssertionError("checkpointed dry-run regenerated Stage 1~4")

    stage4 = [{"model_id": "m/keep", "source_pool": "core"}]
    with tempfile.TemporaryDirectory() as name:
        state = Path(name) / "state.json"
        state.write_text(json.dumps({
            "schema_version": 1,
            "identity": IDENTITY,
            "supabase_latest_sync_run_id": "sync-9",
            "refresh_info": REINGEST,
        }), encoding="utf-8")
        code = _main(
            ["--reingest", "--reingest-state", str(state), "--bundle-dir", "out-bundle"],
            latest_completed_sync=lambda any_versions=False: {"run_id": "sync-9", "completed_at": "2026-11-06"},
            git_identity=lambda: dict(IDENTITY),
            full_reingest_pipeline=refuse,
            run_command=refuse,
            load_corpora=lambda stage4_delta=False: (stage4, {"m/keep": {}}, {"m/keep": {}}),
            validate_corpus=lambda *a, **k: {"rows": 1}, load_evidence_indices=lambda: {},
            validate_evidence_indices=lambda *a, **k: {}, write_stage4_manifest=lambda *a, **k: None,
            payloads=lambda *a, **k: [], evidence_payloads=lambda *a, **k: [],
            db_active_model_ids=lambda cur=None: {"m/keep"},
            db_storage=lambda cur=None: {"database": 1, "model_rows": 0},
            apply_sync=refuse,
            write_reingest_bundle=capture,
        )
    assert code == 0
    assert seen["refresh_info"] == REINGEST
    assert seen["latest_sync_run_id"] == "sync-9"


# ── workflow ──────────────────────────────────────────────────────────────

WORKFLOW = ROOT.parent / ".github" / "workflows" / "model-scout-reingest.yml"
PERSIST_SCRIPT = ROOT / "persist_reingest_snapshots.sh"


def _flow():
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def _steps(job):
    return {step["name"]: step for step in _flow()["jobs"][job]["steps"]}


def test_workflow_apply_downloads_the_approved_bundle_before_running():
    flow, steps = _flow(), _steps("apply")
    names = list(steps)
    assert "approved_run_id" in flow[True]["workflow_dispatch"]["inputs"]
    assert flow["permissions"]["actions"] == "read"
    download = steps["Download the approved dry-run bundle"]
    assert flow["jobs"]["apply"]["if"].replace(" ", "") == "${{inputs.mode=='apply'}}"
    assert download["with"]["run-id"] == "${{ inputs.approved_run_id }}"
    assert download["with"]["name"] == "reingest-bundle-${{ inputs.approved_run_id }}"
    assert names.index("Download the approved dry-run bundle") < names.index("Apply the reviewed bundle to Supabase")
    assert "approved_run_id" in steps["Guard the apply mode"]["run"]


def test_workflow_apply_replays_the_bundle_and_has_no_collection_keys():
    flow = _flow()
    run = _steps("apply")["Apply the reviewed bundle to Supabase"]
    assert "--from-bundle reingest-bundle" in run["run"]
    assert "--approved-run-id" in run["run"]
    assert "--full-stage1" not in run["run"]
    for key in ("HF_TOKEN", "OPENAI_API_KEY"):
        assert key not in flow["jobs"]["apply"].get("env", {}), f"{key} 가 apply 에도 주어진다"


def test_workflow_uploads_the_bundle_only_from_a_successful_dry_run():
    upload = _steps("finalize")["Upload the dry-run bundle"]
    assert upload["with"]["name"] == "reingest-bundle-${{ github.run_id }}"
    assert upload["with"]["path"] == "ai/reingest-bundle"


def test_workflow_resumes_stage4_from_a_prior_stage3_checkpoint():
    flow = _flow()
    inputs = flow[True]["workflow_dispatch"]["inputs"]
    assert "resume-finalize" in inputs["mode"]["options"]
    assert "source_run_id" in inputs
    job = flow["jobs"]["resume_finalize"]
    assert job["needs"] == "validate"
    steps = _steps("resume_finalize")
    for name in (
        "Download the source Stage 1 checkpoint",
        "Download the source Core Stage 2 checkpoint",
        "Download the source Low Stage 2 checkpoint",
        "Download the source Stage 3 checkpoint",
    ):
        assert steps[name]["with"]["run-id"] == "${{ inputs.source_run_id }}"
        assert steps[name]["with"]["github-token"] == "${{ github.token }}"
    resume = steps["Validate Stage 3 and resume at Stage 4"]["run"]
    assert "resume-finalize" in resume
    assert "--source-run-id" in resume
    assert "03_generate_semantic_metadata.py" not in str(job)


def test_resumed_bundle_is_rebound_to_the_new_run_for_apply():
    resume_upload = _steps("resume_finalize")["Upload the resumed dry-run bundle"]
    apply_download = _steps("apply")["Download the approved dry-run bundle"]
    assert resume_upload["with"]["name"] == "reingest-bundle-${{ github.run_id }}"
    assert apply_download["with"]["name"] == "reingest-bundle-${{ inputs.approved_run_id }}"
    assert apply_download["with"]["run-id"] == "${{ inputs.approved_run_id }}"


def test_workflow_commits_snapshots_only_after_the_db_step_succeeds():
    steps = _steps("apply")
    names = list(steps)
    persist = steps["Persist snapshots after apply"]
    assert "if" not in persist or ("always()" not in persist["if"] and "failure()" not in persist["if"])
    assert names.index("Persist snapshots after apply") > names.index("Apply the reviewed bundle to Supabase")
    assert "persist_reingest_snapshots.sh" in persist["run"]
    script = PERSIST_SCRIPT.read_text(encoding="utf-8")
    assert "parent_child_core.jsonl" in script
    assert "hf_models_stage4_core.jsonl" not in script
    assert "git restore --worktree ." in script
    assert "automation/reingest-snapshot-" in script
    assert "HEAD:refs/heads/${snapshot_branch}" in script
    assert "HEAD:main" not in script


def test_workflow_can_recover_snapshots_without_reapplying_the_database():
    flow = _flow()
    inputs = flow[True]["workflow_dispatch"]["inputs"]
    assert "persist-snapshots" in inputs["mode"]["options"]
    steps = _steps("persist_snapshots")
    assert "PERSIST" in steps["Guard snapshot recovery"]["run"]
    assert steps["Download the already applied bundle"]["with"]["run-id"] == "${{ inputs.approved_run_id }}"
    verify = steps["Verify the completed DB apply and restore snapshots"]["run"]
    assert "recover-snapshots" in verify
    assert "08_sync_supabase.py" not in verify
    assert "persist_reingest_snapshots.sh" in steps["Persist the recovered snapshots"]["run"]


def test_validate_mode_needs_no_secrets_or_bundle():
    flow = _flow()
    validate = flow["jobs"]["validate"]
    assert not validate.get("env")
    names = set(_steps("validate"))
    assert "Download the approved dry-run bundle" not in names
    assert "Preflight external services" not in names


def test_dry_run_is_split_into_checkpointed_jobs_and_parallel_stage2():
    flow = _flow()
    assert set(flow["jobs"]) == {
        "validate", "prepare", "stage2", "stage3", "finalize", "resume_finalize", "apply",
        "persist_snapshots",
    }
    assert flow["jobs"]["stage2"]["strategy"]["matrix"]["pool"] == ["core", "low_popularity"]
    assert flow["jobs"]["prepare"]["needs"] == "validate"
    assert flow["jobs"]["stage2"]["needs"] == "prepare"
    assert flow["jobs"]["stage3"]["needs"] == "stage2"
    assert flow["jobs"]["finalize"]["needs"] == "stage3"
    assert "Preflight external services" in _steps("prepare")
    stage3_upload = _steps("stage3")["Upload the Stage 3 checkpoint"]
    assert stage3_upload["with"]["name"] == "reingest-stage3-${{ github.run_id }}"
    assert "hf_models_stage3_core.jsonl" in _steps("stage3")["Pack the Stage 3 checkpoint"]["run"]
    assert "Download the Stage 3 checkpoint" in _steps("finalize")
    assert "stage3/stage3.tar.gz" in _steps("finalize")["Restore the checkpointed inputs"]["run"]
    assert "--reingest-state reingest-work/refresh-info.json" in _steps("finalize")["Validate and build the reviewed dry-run bundle"]["run"]


if __name__ == "__main__":
    for name, func in sorted(globals().items()):
        if name.startswith("test_"):
            func()
            print(f"ok  {name}")
