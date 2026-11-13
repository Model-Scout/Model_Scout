#!/usr/bin/env python3
"""Checkpointed GitHub Actions jobs for a full Model Scout reingest.

The old workflow ran Stage 1 through Stage 4 in one GitHub-hosted job. A full
catalog refresh can legitimately exceed GitHub's six-hour job limit, so this
module splits the work into restartable artifacts:

* ``preflight`` verifies the actual HF, OpenAI chat, OpenAI embedding and DB
  credentials before a multi-hour run starts.
* ``prepare`` optionally rebuilds Stage 1 and freezes the Supabase/contract
  baseline used by every later job.
* ``stage2`` runs one pool. GitHub Actions runs Core and Low in parallel.
* ``finalize`` joins both pools, runs the paid stages and writes a small state
  file consumed by ``08_sync_supabase.py --reingest-state``.

No secret value is written to an artifact or log.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
WORK_DIR = ROOT / "reingest-work"
STATE_VERSION = 1
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def load_sync_module() -> Any:
    spec = importlib.util.spec_from_file_location("model_scout_reingest_sync", ROOT / "08_sync_supabase.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("08_sync_supabase.py could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sync = load_sync_module()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def read_state(path: Path) -> Dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("schema_version") != STATE_VERSION:
        raise RuntimeError(f"unsupported or invalid reingest state: {path}")
    return value


def assert_same_run(state: Dict[str, Any]) -> Dict[str, str]:
    expected = state.get("identity") or {}
    current = sync.git_identity()
    for key in ("repository", "git_sha", "git_ref", "run_id"):
        if str(expected.get(key)) != str(current.get(key)):
            raise RuntimeError(
                f"reingest artifact identity mismatch for {key}: "
                f"expected {expected.get(key)!r}, got {current.get(key)!r}"
            )
    return current


def assert_sync_baseline(state: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    latest = sync.latest_completed_sync(any_versions=True)
    expected = state.get("supabase_latest_sync_run_id")
    actual = (latest or {}).get("run_id")
    if str(expected or "") != str(actual or ""):
        raise RuntimeError(
            "Supabase changed after the dry-run started; discard these artifacts "
            "and start a new dry-run"
        )
    return latest


def preflight() -> Dict[str, Any]:
    """Make one tiny call to each paid/external dependency."""
    hf_token = os.getenv("HF_TOKEN")
    openai_key = os.getenv("OPENAI_API_KEY")
    if not hf_token:
        raise RuntimeError("HF_TOKEN repository secret is missing")
    if not openai_key:
        raise RuntimeError("OPENAI_API_KEY repository secret is missing")

    from huggingface_hub import HfApi
    from openai import OpenAI

    hf_model = os.getenv("REINGEST_PREFLIGHT_HF_MODEL") or "google-bert/bert-base-multilingual-cased"
    chat_model = os.getenv("STAGE3_LLM_MODEL") or os.getenv("OPENAI_MODEL") or "gpt-4o-mini"
    embedding_model = os.getenv("STAGE4_EMBEDDING_MODEL") or "text-embedding-3-small"

    model_info = HfApi(token=hf_token).model_info(hf_model, files_metadata=False)
    client = OpenAI(api_key=openai_key)
    chat = client.chat.completions.create(
        model=chat_model,
        messages=[{"role": "user", "content": "Reply with OK."}],
        temperature=0,
        max_tokens=1,
    )
    embedding = client.embeddings.create(model=embedding_model, input=["model scout preflight"])

    conn = sync.db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("select 1")
            row = cur.fetchone()
        if not row or int(row[0]) != 1:
            raise RuntimeError("Supabase preflight returned an unexpected result")
    finally:
        conn.close()

    chat_usage = getattr(chat, "usage", None)
    embedding_usage = getattr(embedding, "usage", None)
    result = {
        "ok": True,
        "huggingface": {"model": getattr(model_info, "id", hf_model)},
        "openai_chat": {
            "model": chat_model,
            "total_tokens": int(getattr(chat_usage, "total_tokens", 0) or 0),
        },
        "openai_embedding": {
            "model": embedding_model,
            "total_tokens": int(getattr(embedding_usage, "total_tokens", 0) or 0),
        },
        "supabase": {"select_1": True},
    }
    return result


def prepare(state_path: Path, full_stage1: bool) -> Dict[str, Any]:
    identity = sync.git_identity()
    if identity.get("git_ref") != "main":
        raise RuntimeError("costly reingest dry-runs must start from main")
    latest = sync.latest_completed_sync(any_versions=True)
    if latest is None:
        raise RuntimeError("no completed Supabase sync exists; this is not a reingest target")

    WORK_DIR.mkdir(parents=True, exist_ok=True)
    sync.clear_incremental_artifacts()
    baseline = sync.snapshot_contract_baseline(WORK_DIR)
    started_at = datetime.now(timezone.utc).isoformat()
    stage1_scan = None
    if full_stage1:
        try:
            stage1_scan = sync.run_full_stage1_scan()
        except sync.Stage1RemovalGuardError as error:
            sync.write_reingest_report(
                sync.stage1_guard_failure_result(error),
                WORK_DIR / "prepare-report.json",
            )
            raise

    stage1_processable = sum(
        len(sync.read_jsonl(DATA_DIR / f"hf_models_stage1_{pool}.jsonl"))
        for pool in sync.POOLS
    )
    state = {
        "schema_version": STATE_VERSION,
        "identity": identity,
        "started_at": started_at,
        "stage1_mode": "full-scan" if full_stage1 else "reuse",
        "stage1_scan": stage1_scan,
        "stage1_processable": stage1_processable,
        "previous_watermark": sync.carried_watermark(latest),
        "supabase_latest_sync_run_id": latest.get("run_id"),
        "contract_baseline": baseline.name if baseline is not None else None,
    }
    write_json(state_path, state)
    return state


def validate_contract_pool(pool: str, baseline: Optional[Path]) -> Dict[str, Any]:
    path = DATA_DIR / f"hf_models_stage2_contract_{pool}.jsonl"
    if not path.exists():
        raise RuntimeError(f"{path.name} is missing after Stage 2")
    summary_path = WORK_DIR / f"contract_{pool}_summary.json"
    command = [
        sys.executable,
        str(ROOT / "contract" / "validate.py"),
        str(path),
        "--summary-json",
        str(summary_path),
    ]
    if baseline is not None:
        command += ["--baseline", str(baseline)]
    subprocess.run(command, cwd=ROOT, check=True)
    return json.loads(summary_path.read_text(encoding="utf-8"))


def stage2(pool: str, state_path: Path) -> Dict[str, Any]:
    state = read_state(state_path)
    assert_same_run(state)
    assert_sync_baseline(state)
    baseline_name = state.get("contract_baseline")
    baseline = WORK_DIR / baseline_name if baseline_name else None
    if baseline is not None and not baseline.exists():
        raise RuntimeError("contract baseline artifact is missing")

    sync.run_command([sys.executable, str(ROOT / "02_enrich_metadata.py"), "--pool", pool])
    expected_ids = {
        row["model_id"]
        for row in sync.read_jsonl(DATA_DIR / f"hf_models_stage1_{pool}.jsonl")
    }
    produced = len(sync.read_jsonl(DATA_DIR / f"hf_models_stage2_{pool}.jsonl"))
    report = DATA_DIR / f"hf_models_stage2_{pool}_language_excluded.json"
    excluded_ids = set(json.loads(report.read_text(encoding="utf-8"))) if report.exists() else set()
    excluded = len(expected_ids & excluded_ids)
    sync.assert_stage2_volume(len(expected_ids), produced, excluded)
    contract = validate_contract_pool(pool, baseline)
    result = {
        "pool": pool,
        "stage1_rows": len(expected_ids),
        "stage2_rows": produced,
        "language_excluded": excluded,
        "contract": contract,
    }
    write_json(WORK_DIR / f"stage2_{pool}.json", result)
    return result


def finalize(state_path: Path, output_path: Path) -> Dict[str, Any]:
    state = read_state(state_path)
    assert_same_run(state)
    latest = assert_sync_baseline(state)
    baseline_name = state.get("contract_baseline")
    baseline = WORK_DIR / baseline_name if baseline_name else None

    stage1_ids = {
        row["model_id"]
        for pool in sync.POOLS
        for row in sync.read_jsonl(DATA_DIR / f"hf_models_stage1_{pool}.jsonl")
    }
    produced = sum(
        len(sync.read_jsonl(DATA_DIR / f"hf_models_stage2_{pool}.jsonl"))
        for pool in sync.POOLS
    )
    language_excluded = sync.language_excluded_ids()
    excluded_in_stage1 = len(language_excluded & stage1_ids)
    sync.assert_stage2_volume(len(stage1_ids), produced, excluded_in_stage1)
    gate = sync.contract_gate(require=True, baseline=baseline)

    sync.run_command([
        sys.executable,
        str(ROOT / "03_generate_semantic_metadata.py"),
        "--pool", "all",
        "--metrics", str(WORK_DIR / "stage3-metrics.json"),
    ])
    for pool in sync.POOLS:
        sync.run_command([
            sys.executable,
            str(ROOT / "03_repair_truncated_semantic.py"),
            "--pool", pool,
            "--apply",
        ])
    sync.run_command([sys.executable, str(ROOT / "evidence_index.py"), "--pool", "all"])
    sync.run_command([
        sys.executable,
        str(ROOT / "06_extract_benchmark_metadata.py"),
        "--pool", "all",
        "--apply",
    ])
    sync.run_command([
        sys.executable,
        str(ROOT / "04_build_embeddings.py"),
        "--pool", "all",
        "--execute",
        "--db-cache",
        "--metrics", str(WORK_DIR / "stage4-metrics.json"),
    ])

    refresh_info = sync.reingest_result(
        previous_watermark=state.get("previous_watermark"),
        started_at=state["started_at"],
        steps=[
            *(("stage1:full-scan",) if state.get("stage1_scan") is not None else ()),
            "stage2:parallel",
            f"stage2:{produced}rows",
            "contract_gate",
            "stage3:readme-delta",
            "stage3.5:benchmark",
            "stage4:hash-delta",
        ],
        contract_gate_report=gate,
        language_excluded=language_excluded,
        stage2_rows=produced,
        stage1_scan=state.get("stage1_scan"),
        stage1_processable=len(stage1_ids),
        language_excluded_in_stage1=excluded_in_stage1,
    )
    result = {
        "schema_version": STATE_VERSION,
        "identity": state["identity"],
        "supabase_latest_sync_run_id": (latest or {}).get("run_id"),
        "refresh_info": refresh_info,
    }
    write_json(output_path, result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    preflight_parser = subparsers.add_parser("preflight")
    preflight_parser.add_argument("--output", type=Path, default=WORK_DIR / "preflight.json")

    prepare_parser = subparsers.add_parser("prepare")
    prepare_parser.add_argument("--state", type=Path, default=WORK_DIR / "context.json")
    prepare_parser.add_argument("--full-stage1", action="store_true")

    stage2_parser = subparsers.add_parser("stage2")
    stage2_parser.add_argument("--pool", choices=sync.POOLS, required=True)
    stage2_parser.add_argument("--state", type=Path, default=WORK_DIR / "context.json")

    finalize_parser = subparsers.add_parser("finalize")
    finalize_parser.add_argument("--state", type=Path, default=WORK_DIR / "context.json")
    finalize_parser.add_argument("--output", type=Path, default=WORK_DIR / "refresh-info.json")

    args = parser.parse_args()
    if args.command == "preflight":
        result = preflight()
        write_json(args.output, result)
    elif args.command == "prepare":
        result = prepare(args.state, args.full_stage1)
    elif args.command == "stage2":
        result = stage2(args.pool, args.state)
    else:
        result = finalize(args.state, args.output)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
