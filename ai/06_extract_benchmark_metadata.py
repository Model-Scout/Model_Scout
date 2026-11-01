#!/usr/bin/env python3
"""Extract and compact benchmark metadata for the Stage 4 corpus.

This is the single canonical benchmark step. It first refreshes the deterministic
Stage 2 sidecars, then embeds a bounded, ranking-safe projection into Stage 4.
The full README remains available through its existing provenance path.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from benchmark_metadata import extract_benchmarks


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT.parent / "backend" / "data"
POOLS = ("core", "low_popularity")
MAX_COMPACT_RESULTS = 256
CHANGED_IDS_PATH = DATA_DIR / ".benchmark_changed_model_ids.json"
STATE_PATH = DATA_DIR / "hf_models_benchmark_state.json"
STATE_CANDIDATE_PATH = DATA_DIR / ".hf_models_benchmark_state_candidate.json"


def metadata_fingerprint(row: Dict[str, Any]) -> str:
    payload = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def read_state(path: Path) -> Dict[str, str]:
    if not path.exists():
        return {}
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a model_id to fingerprint mapping")
    return {str(key): str(item) for key, item in value.items()}


def load_model_ids(path: Optional[Path]) -> Optional[Set[str]]:
    if path is None:
        return None
    if not path.exists():
        raise FileNotFoundError(path)
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ValueError(f"{path}: expected a JSON list of model IDs")
    return {item for item in value if item}


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def write_jsonl_atomic(rows: List[Dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    os.close(fd)
    temporary = Path(name)
    try:
        with temporary.open("w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
                handle.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def read_readme(row: Dict[str, Any]) -> tuple[str, str]:
    readme = ((row.get("source") or {}).get("readme") or {})
    relative = readme.get("path")
    if not relative:
        return "", ""
    path = DATA_DIR.parent / relative
    if not path.exists():
        return "", str(relative)
    return path.read_text(encoding="utf-8", errors="replace"), str(relative)


def process_pool(
    pool: str,
    model_ids: Optional[Set[str]] = None,
) -> Dict[str, Any]:
    source_path = DATA_DIR / f"hf_models_stage2_{pool}.jsonl"
    rows = read_jsonl(source_path)
    if model_ids is not None:
        rows = [row for row in rows if row.get("model_id") in model_ids]
    output_path = (
        DATA_DIR / f".hf_models_benchmark_delta_{pool}.jsonl"
        if model_ids is not None
        else DATA_DIR / f"hf_models_benchmark_{pool}.jsonl"
    )
    canonical_path = DATA_DIR / f"hf_models_benchmark_{pool}.jsonl"
    if model_ids is not None and canonical_path.exists():
        canonical_rows = [
            row
            for row in read_jsonl(canonical_path)
            if row.get("model_id") in model_ids
        ]
        persisted = []
        for item in canonical_rows:
            compact = compact_sidecar(item)
            compact["model_id"] = item.get("model_id")
            compact["source_pool"] = pool
            persisted.append(compact)
        write_jsonl_atomic(persisted, output_path)
        return {
            "pool": pool,
            "rows": len(canonical_rows),
            "readme_available": sum(bool(row.get("readme_available")) for row in canonical_rows),
            "numeric_results": sum((row.get("summary") or {}).get("numeric_results", 0) for row in canonical_rows),
            "ranking_eligible": sum((row.get("summary") or {}).get("ranking_eligible", 0) for row in canonical_rows),
            "mentions_only": sum((row.get("summary") or {}).get("mentions_only", 0) for row in canonical_rows),
            "variant_ambiguous": sum((row.get("summary") or {}).get("quantized_ambiguous", 0) for row in canonical_rows),
            "errors": 0,
            "incremental": True,
            "from_canonical": True,
            "output": str(output_path),
        }
    previous = (
        {row.get("model_id"): row for row in read_jsonl(output_path)}
        if model_ids is None and output_path.exists()
        else {}
    )
    previous_hashes = read_state(STATE_PATH)
    if not previous_hashes and previous:
        previous_hashes = {
            model_id: metadata_fingerprint(row)
            for model_id, row in previous.items()
        }
    output: List[Dict[str, Any]] = []
    stats = {
        "pool": pool,
        "rows": len(rows),
        "readme_available": 0,
        "numeric_results": 0,
        "ranking_eligible": 0,
        "mentions_only": 0,
        "variant_ambiguous": 0,
        "errors": 0,
        "incremental": model_ids is not None,
    }
    for row in rows:
        try:
            text, relative_path = read_readme(row)
            if text:
                stats["readme_available"] += 1
            metadata = extract_benchmarks(row, text, relative_path)
            metadata["model_id"] = row.get("model_id")
            metadata["source_pool"] = pool
            metadata["source_stage1_version"] = (row.get("stage") or {}).get("source_stage1_version")
            metadata["source_stage2_version"] = (row.get("stage") or {}).get("stage2_version")
            output.append(metadata)
            summary = metadata["summary"]
            stats["numeric_results"] += summary["numeric_results"]
            stats["ranking_eligible"] += summary["ranking_eligible"]
            stats["mentions_only"] += summary["mentions_only"]
            stats["variant_ambiguous"] += summary["quantized_ambiguous"]
        except Exception as exc:
            stats["errors"] += 1
            output.append({
                "model_id": row.get("model_id"),
                "source_pool": pool,
                "benchmark_version": 1,
                "readme_available": False,
                "results": [],
                "mentions": [],
                "summary": {"numeric_results": 0, "ranking_eligible": 0, "mentions_only": 0, "quantized_ambiguous": 0},
                "error": {"type": type(exc).__name__, "message": str(exc)},
            })
    if model_ids is not None:
        persisted = []
        for item in output:
            compact = compact_sidecar(item)
            compact["model_id"] = item.get("model_id")
            compact["source_pool"] = pool
            persisted.append(compact)
    else:
        persisted = output
    write_jsonl_atomic(persisted, output_path)
    if model_ids is None:
        changed_model_ids = sorted(
            row.get("model_id")
            for row in output
            if row.get("model_id")
            and previous_hashes.get(row.get("model_id")) != metadata_fingerprint(row)
        )
        changed_ids_path = DATA_DIR / f".hf_models_benchmark_changed_ids_{pool}.json"
        changed_ids_path.write_text(
            json.dumps(changed_model_ids, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        stats["changed_count"] = len(changed_model_ids)
        stats["changed_ids_path"] = str(changed_ids_path)
        # Keep the changed benchmark rows beside the canonical sidecar. The
        # incremental sync can reuse this delta instead of parsing the same
        # README files a second time with --model-ids-file.
        delta_path = DATA_DIR / f".hf_models_benchmark_delta_{pool}.jsonl"
        changed_set = set(changed_model_ids)
        write_jsonl_atomic(
            [row for row in output if row.get("model_id") in changed_set],
            delta_path,
        )
        stats["delta_output"] = str(delta_path)
        state_path = DATA_DIR / f".hf_models_benchmark_state_{pool}.json"
        state_path.write_text(
            json.dumps(
                {
                    row["model_id"]: metadata_fingerprint(row)
                    for row in output
                    if row.get("model_id")
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    stats["output"] = str(output_path)
    return stats


def _compact_result(result: Dict[str, Any]) -> Dict[str, Any]:
    fields = (
        "benchmark", "dataset", "metric", "score", "higher_is_better",
        "split", "config", "evidence_ref", "model_name", "variant_kind",
        "variant_safe", "comparability", "self_reported", "ranking_eligible",
    )
    return {field: result.get(field) for field in fields if field in result}


def _compact_mention(mention: Dict[str, Any]) -> Dict[str, Any]:
    fields = (
        "benchmark", "dataset", "metric", "model_name", "evidence_ref",
        "comparability", "reason", "self_reported",
    )
    return {field: mention.get(field) for field in fields if field in mention}


def compact_sidecar(sidecar: Dict[str, Any]) -> Dict[str, Any]:
    """Keep only ranking/display fields and bound pathological model cards."""
    seen = set()
    compact_results = []
    original_results = [
        result
        for result in (sidecar.get("results") or [])
        if isinstance(result, dict) and result.get("ranking_eligible") is True
    ]
    for result in original_results:
        compact = _compact_result(result)
        identity = tuple(
            (key, json.dumps(compact.get(key), ensure_ascii=False, sort_keys=True))
            for key in (
                "benchmark", "dataset", "metric", "score", "model_name",
                "variant_kind", "split", "config",
            )
        )
        if identity in seen:
            continue
        seen.add(identity)
        compact_results.append(compact)
        if len(compact_results) >= MAX_COMPACT_RESULTS:
            break
    original_count = len(original_results)
    return {
        "benchmark_version": sidecar.get("benchmark_version"),
        "readme_available": bool(sidecar.get("readme_available")),
        "readme_path": sidecar.get("readme_path"),
        "readme_sha256": sidecar.get("readme_sha256"),
        "summary": {
            **(sidecar.get("summary") or {}),
            "original_result_count": original_count,
            "retained_result_count": len(compact_results),
            "results_truncated": original_count > len(compact_results),
        },
        "results": compact_results,
        "mentions": [
            _compact_mention(mention)
            for mention in sidecar.get("mentions", [])
            if isinstance(mention, dict)
        ],
    }


def integrate_pool(pool: str, apply: bool) -> Dict[str, Any]:
    stage4_path = DATA_DIR / f"hf_models_stage4_{pool}.jsonl"
    sidecar_path = DATA_DIR / f"hf_models_benchmark_{pool}.jsonl"
    rows = read_jsonl(stage4_path)
    sidecars = {row.get("model_id"): row for row in read_jsonl(sidecar_path)}
    stage4_ids = {row.get("model_id") for row in rows}
    sidecar_ids = set(sidecars)
    if stage4_ids != sidecar_ids:
        missing = sorted(stage4_ids - sidecar_ids)[:5]
        extra = sorted(sidecar_ids - stage4_ids)[:5]
        raise ValueError(
            f"[{pool}] model_id mismatch: missing={missing} extra={extra}"
        )

    merged = []
    for row in rows:
        updated = dict(row)
        updated["benchmark_metadata"] = compact_sidecar(sidecars[row["model_id"]])
        merged.append(updated)
    if apply:
        write_jsonl_atomic(merged, stage4_path)
    metadata = [row["benchmark_metadata"] for row in merged]
    return {
        "pool": pool,
        "rows": len(rows),
        "ranking_eligible_results": sum(len(item["results"]) for item in metadata),
        "mentions": sum(len(item["mentions"]) for item in metadata),
        "truncated_models": sum(
            bool((item.get("summary") or {}).get("results_truncated"))
            for item in metadata
        ),
        "apply": apply,
        "output": str(stage4_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool", choices=("core", "low_popularity", "all"), default="all")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write compact benchmark metadata into the Stage 4 snapshots",
    )
    parser.add_argument(
        "--model-ids-file",
        type=Path,
        default=None,
        help="extract only the model IDs in a JSON list into benchmark delta sidecars",
    )
    args = parser.parse_args()
    pools = POOLS if args.pool == "all" else (args.pool,)
    model_ids = load_model_ids(args.model_ids_file)
    summaries = [process_pool(pool, model_ids) for pool in pools]
    integrated = (
        [integrate_pool(pool, args.apply) for pool in pools]
        if model_ids is None and args.apply
        else []
    )
    if model_ids is None:
        changed_ids = set()
        for pool in pools:
            changed_ids_path = DATA_DIR / f".hf_models_benchmark_changed_ids_{pool}.json"
            if changed_ids_path.exists():
                value = json.loads(changed_ids_path.read_text(encoding="utf-8"))
                if isinstance(value, list):
                    changed_ids.update(item for item in value if isinstance(item, str))
        changed_ids = sorted(changed_ids)
        CHANGED_IDS_PATH.write_text(
            json.dumps(changed_ids, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        state = {}
        for pool in pools:
            pool_state_path = DATA_DIR / f".hf_models_benchmark_state_{pool}.json"
            state.update(read_state(pool_state_path))
        STATE_CANDIDATE_PATH.write_text(
            json.dumps(state, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps({
        "benchmark_metadata_version": 1,
        "max_compact_results": MAX_COMPACT_RESULTS,
        "extracted": summaries,
        "integrated": integrated,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
