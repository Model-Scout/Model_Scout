#!/usr/bin/env python3
"""Repair only Stage 3 rows whose README was truncated.

The normal Stage 3 job limits README input to 60,000 characters.  This
script reads the full saved README for rows marked ``stage3_truncated`` and
runs the same Atomic Evidence pipeline on those rows only.  Normal rows are
copied unchanged.  By default a complete repaired copy is written beside the
original; ``--apply`` atomically replaces the original only after validation.

This script does not rescan Hugging Face, rerun Stage 1/2, or modify rows that
do not need repair.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
POOLS = ("core", "low_popularity")
REPAIR_PROMPT_VERSION = "stage3-atomic-evidence-full-readme-v1"
REPAIR_CHUNKER_VERSION = "atomic-evidence-full-readme-v1"


def load_stage3_module():
    source = ROOT / "03_generate_semantic_metadata.py"
    spec = importlib.util.spec_from_file_location("stage3_atomic_module", source)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {source}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    rows: List[Dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number}: row is not an object")
            rows.append(value)
    return rows


def write_jsonl_atomic(path: Path, rows: Sequence[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent)
    )
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with temporary.open("w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def stage_paths(pool: str) -> Tuple[Path, Path, Path]:
    return (
        DATA_DIR / f"hf_models_stage2_{pool}.jsonl",
        DATA_DIR / f"hf_models_stage3_{pool}.jsonl",
        DATA_DIR / f"hf_models_stage3_{pool}_truncated_repaired.jsonl",
    )


def stage2_readme_path(stage2_row: Dict[str, Any]) -> Optional[Path]:
    readme = (stage2_row.get("source") or {}).get("readme") or {}
    relative = readme.get("path")
    if not readme.get("available") or not relative:
        return None
    path = Path(relative)
    return path if path.is_absolute() else DATA_DIR.parent / path


def is_truncated(row: Dict[str, Any]) -> bool:
    readme = (row.get("evidence") or {}).get("readme") or {}
    if readme.get("stage3_truncated") is True:
        return True
    original = readme.get("original_chars")
    used = readme.get("used_chars")
    return (
        isinstance(original, (int, float))
        and isinstance(used, (int, float))
        and original > used
    )


def load_full_readme(
    stage2_row: Dict[str, Any],
    old_row: Dict[str, Any],
    stage3: Any,
) -> Tuple[Optional[str], Dict[str, Any]]:
    readme = dict((stage2_row.get("source") or {}).get("readme") or {})
    path = stage2_readme_path(stage2_row)
    if path is None or not path.exists():
        return None, readme
    text = path.read_text(encoding="utf-8", errors="replace")
    readme.update(
        {
            "available": True,
            "path": path.relative_to(DATA_DIR.parent).as_posix() if path.is_absolute() and DATA_DIR.parent in path.parents else str(path),
            "original_chars": len(text),
            "saved_chars": len(text),
            "used_chars": len(text),
            "content_hash": stage3.digest(text),
            "stage3_truncated": False,
            "full_readme_repair": True,
            "error": None,
        }
    )
    return text, readme


def make_repaired_row(
    old_row: Dict[str, Any],
    stage2_row: Dict[str, Any],
    text: str,
    readme: Dict[str, Any],
    client: Any,
    model: str,
    stage3: Any,
) -> Dict[str, Any]:
    spans, field_ids = stage3.route_spans(stage3.atomic_spans(text))
    messages = stage3.build_prompt(stage2_row, spans, field_ids)
    semantic = stage3.call_llm(client, model, messages)
    semantic = stage3.materialize(semantic, spans)
    validation = stage3.validate(semantic, spans)
    if any(validation.get(key, 0) for key in (
        "invalid_evidence_refs",
        "uncited_claims",
        "missing_quotes",
        "quote_mismatches",
    )):
        raise ValueError(f"evidence validation failed: {validation}")

    stage = {
        "source_pool": old_row.get("source_pool", ""),
        "source_stage2_version": (stage2_row.get("stage") or {}).get("stage2_version"),
        "source_stage2_hash": stage3.source_stage2_hash(stage2_row),
        "stage3_version": stage3.STAGE3_VERSION,
        "prompt_version": REPAIR_PROMPT_VERSION,
        "chunker_version": REPAIR_CHUNKER_VERSION,
        "parent_child_schema_version": stage3.INDEX_SCHEMA_VERSION,
        "semantic_enriched": True,
        "enriched_at": stage3.utc_now(),
    }
    return {
        **old_row,
        "model_id": old_row["model_id"],
        "source_pool": old_row.get("source_pool"),
        "status": "completed",
        "source_stage2": stage2_row,
        "semantic": semantic,
        "evidence": stage3.materialize_parent_child_evidence(
            old_row["model_id"],
            {
                "readme": readme,
                "field_evidence_ids": field_ids,
                "spans": spans,
                "prompt_token_estimate": sum(
                    len(message["content"].split()) for message in messages
                ),
            },
        ),
        "validation": validation,
        "stage3": stage,
    }


def validate_merged_rows(
    rows: Sequence[Dict[str, Any]],
    source_rows: Sequence[Dict[str, Any]],
    repaired_ids: set[str],
) -> None:
    source_ids = {row.get("model_id") for row in source_rows}
    row_ids = [row.get("model_id") for row in rows]
    if len(row_ids) != len(set(row_ids)):
        raise ValueError("merged output contains duplicate model_id values")
    if set(row_ids) != source_ids:
        raise ValueError(
            f"merged output IDs differ from Stage 2: missing={len(source_ids - set(row_ids))} "
            f"extra={len(set(row_ids) - source_ids)}"
        )
    for row in rows:
        if row.get("model_id") not in repaired_ids:
            continue
        validation = row.get("validation") or {}
        if any(validation.get(key, 0) for key in (
            "invalid_evidence_refs",
            "uncited_claims",
            "missing_quotes",
            "quote_mismatches",
        )):
            raise ValueError(f"{row.get('model_id')}: invalid repaired evidence")
        readme = (row.get("evidence") or {}).get("readme") or {}
        if readme.get("stage3_truncated") is True:
            raise ValueError(f"{row.get('model_id')}: README remains truncated")


def repair_pool(
    pool: str,
    model: str,
    limit: Optional[int],
    dry_run: bool,
    apply: bool,
    allow_partial: bool,
) -> Dict[str, Any]:
    stage3 = load_stage3_module()
    stage2_path, output_path, repaired_path = stage_paths(pool)
    source_rows = read_jsonl(stage2_path)
    output_rows = read_jsonl(output_path)
    if not source_rows:
        raise FileNotFoundError(f"Missing Stage 2 input: {stage2_path}")
    if not output_rows:
        raise FileNotFoundError(f"Missing Stage 3 output: {output_path}")
    if not allow_partial and len(output_rows) != len(source_rows):
        raise RuntimeError(
            f"[{pool}] Stage 3 is incomplete ({len(output_rows)}/{len(source_rows)}). "
            "Wait for the normal Stage 3 run or use --allow-partial explicitly."
        )

    stage2_by_id = {row["model_id"]: row for row in source_rows}
    targets = [row for row in output_rows if is_truncated(row)]
    if limit is not None:
        targets = targets[:limit]
    target_ids = {row.get("model_id") for row in targets}
    print(f"[{pool}] truncated_targets={len(targets)}", flush=True)
    if dry_run:
        for row in targets:
            stage2_row = stage2_by_id.get(row.get("model_id"), {})
            path = stage2_readme_path(stage2_row)
            size = path.stat().st_size if path and path.exists() else 0
            print(f"[{pool}] SELECT {row.get('model_id')} chars={size}", flush=True)
        return {"pool": pool, "targets": len(targets), "dry_run": True}

    load_dotenv(ROOT / ".env")
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required unless --dry-run is used")
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    merged = list(output_rows)
    by_id = {row["model_id"]: row for row in merged}
    errors: List[str] = []
    repaired = 0
    for index, old_row in enumerate(targets, start=1):
        model_id = old_row["model_id"]
        print(f"[{pool}] REPAIR {index}/{len(targets)} {model_id}", flush=True)
        try:
            stage2_row = stage2_by_id[model_id]
            text, readme = load_full_readme(stage2_row, old_row, stage3)
            if not text:
                raise FileNotFoundError(f"full README not found for {model_id}")
            by_id[model_id] = make_repaired_row(
                old_row, stage2_row, text, readme, client, model, stage3
            )
            repaired += 1
        except Exception as exc:  # keep the original row and abort apply below
            errors.append(f"{model_id}: {type(exc).__name__}: {exc}")
            print(f"[{pool}] ERROR {errors[-1]}", file=sys.stderr, flush=True)

    merged = [by_id[row["model_id"]] for row in output_rows]
    validate_merged_rows(merged, source_rows, target_ids if not errors else set())
    if errors:
        raise RuntimeError(
            f"[{pool}] {len(errors)} repair error(s); original output was not replaced"
        )
    write_jsonl_atomic(repaired_path, merged)
    if apply:
        os.replace(repaired_path, output_path)
        print(f"[{pool}] applied: {output_path}", flush=True)
    else:
        print(f"[{pool}] candidate output: {repaired_path}", flush=True)
    return {
        "pool": pool,
        "targets": len(targets),
        "repaired": repaired,
        "applied": apply,
        "output": str(output_path if apply else repaired_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool", choices=(*POOLS, "all"), default="all")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--apply", action="store_true", help="replace original after validation")
    parser.add_argument("--allow-partial", action="store_true", help="allow incomplete Stage 3 input")
    parser.add_argument("--model", default=None)
    args = parser.parse_args()
    if args.apply and args.limit is not None:
        parser.error("--apply cannot be combined with --limit")
    if args.apply and args.allow_partial:
        parser.error("--apply cannot be combined with --allow-partial")
    load_dotenv(ROOT / ".env")
    model = args.model or os.getenv("STAGE3_LLM_MODEL") or os.getenv("OPENAI_MODEL") or "gpt-4o-mini"
    pools = POOLS if args.pool == "all" else (args.pool,)
    summaries = [
        repair_pool(pool, model, args.limit, args.dry_run, args.apply, args.allow_partial)
        for pool in pools
    ]
    print(json.dumps({"repair": summaries}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
