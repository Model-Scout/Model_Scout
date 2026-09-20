"""Repair missing Stage 2 metadata without rewriting the original corpora.

This script reads the current Stage 2 rows and writes separate ``*_repaired``
files.  It only visits rows whose parameter count or context length is missing.
It never runs Stage 1, never fetches README files, and never replaces the
original Stage 2 JSONL files.

Run after activating the project environment, for example:

    python 03_repair_missing_metadata.py --pool core
    python 03_repair_missing_metadata.py --pool all

The first run is intentionally explicit: it makes the repaired artifact easy
to compare with the original before adopting it downstream.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from huggingface_hub import hf_hub_download

import importlib.util


_SPEC = importlib.util.spec_from_file_location("stage2_helpers", "02_enrich_metadata.py")
if _SPEC is None or _SPEC.loader is None:  # pragma: no cover - import guard
    raise RuntimeError("Could not load 02_enrich_metadata.py")
_STAGE2 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_STAGE2)


DATA_DIR = Path("data")
SOURCE_STAGE1_VERSION = 7
SOURCE_STAGE2_VERSION = 6
REPAIR_VERSION = 1
POOLS = ("core", "low_popularity")
CONFIG_FILENAMES = ("config.json", "tokenizer_config.json")
CONTEXT_KEYS = (
    "max_position_embeddings", "n_positions", "max_seq_len",
    "max_sequence_length", "seq_length", "model_max_length",
    "context_length", "max_context_length", "max_seq_len_total",
)
NESTED_CONFIG_KEYS = (
    "text_config", "language_config", "decoder", "llm_config",
    "config", "model_config",
)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    temp.replace(path)


def fetch_json(model_id: str, filename: str) -> tuple[dict[str, Any], str | None]:
    try:
        local = hf_hub_download(repo_id=model_id, filename=filename, token=_STAGE2.HF_TOKEN)
        with Path(local).open(encoding="utf-8") as handle:
            value = json.load(handle)
        return value if isinstance(value, dict) else {}, filename
    except Exception:
        return {}, None


def valid_number(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and 0 < value < 10_000_000


def valid_parameter_count(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def config_sections(config: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    sections = [("config", config)]
    pending = [(key, config.get(key)) for key in NESTED_CONFIG_KEYS]
    seen: set[int] = {id(config)}
    while pending:
        prefix, value = pending.pop(0)
        if not isinstance(value, dict) or id(value) in seen:
            continue
        seen.add(id(value))
        sections.append((prefix, value))
        pending.extend((f"{prefix}.{key}", value.get(key)) for key in NESTED_CONFIG_KEYS)
    return sections


def find_context(config: dict[str, Any], tokenizer: dict[str, Any]) -> tuple[int | None, str | None, list[dict[str, Any]]]:
    candidates: list[dict[str, Any]] = []
    for prefix, section in config_sections(config):
        for key in CONTEXT_KEYS:
            value = section.get(key)
            if valid_number(value):
                candidates.append({"value": value, "source": f"config.{prefix}.{key}"})
    for key in ("model_max_length", "max_seq_length", "model_max_seq_length"):
        value = tokenizer.get(key)
        if valid_number(value) and value < 10_000_000:
            candidates.append({"value": value, "source": f"tokenizer_config.{key}"})
    if not candidates:
        return None, None, []
    best = max(candidates, key=lambda item: item["value"])
    return best["value"], best["source"], candidates


def parameter_from_index(index: dict[str, Any]) -> tuple[int | None, str | None]:
    """Use an authoritative parameter field when present; never confuse bytes with params."""
    metadata = index.get("metadata") if isinstance(index.get("metadata"), dict) else {}
    for key in ("total_parameters", "parameters"):
        value = metadata.get(key, index.get(key))
        if valid_parameter_count(value):
            return value, f"safetensors.index.{key}"
    # total_size is bytes, not a parameter count. Preserve it as evidence only.
    return None, None


def estimate_parameters(config: dict[str, Any]) -> tuple[int | None, str | None]:
    """Conservative architecture estimate; caller marks this as estimated."""
    hidden = config.get("hidden_size")
    layers = config.get("num_hidden_layers", config.get("num_layers"))
    vocab = config.get("vocab_size")
    if not all(valid_number(value) for value in (hidden, layers, vocab)):
        return None, None
    # Approximate dense transformer weights: embeddings + 12*hidden^2 per layer.
    estimate = int(vocab * hidden + layers * 12 * hidden * hidden)
    return estimate, "config.hidden_size*num_layers*vocab_size_estimate"


def repair_row(row: dict[str, Any]) -> dict[str, Any]:
    repaired = json.loads(json.dumps(row))
    model_id = row["model_id"]
    model = repaired.setdefault("model", {})
    detail = repaired.setdefault("metadata_repair", {})
    detail.update({"repair_version": REPAIR_VERSION, "model_id": model_id})

    if model.get("parameter_count") is None:
        parameter = None
        source = None
        for filename in ("model.safetensors.index.json", "pytorch_model.bin.index.json"):
            index, loaded = fetch_json(model_id, filename)
            if loaded:
                parameter, source = parameter_from_index(index)
                if parameter is not None:
                    break
                detail.setdefault("evidence", []).append(f"{filename}:index_present_no_parameter_count")
        if parameter is None:
            config, loaded = fetch_json(model_id, "config.json")
            if loaded:
                parameter, source = estimate_parameters(config)
        if parameter is not None:
            model["parameter_count"] = parameter
            model["parameter_count_billion"] = round(parameter / 1e9, 3)
            detail["parameter_count"] = {"value": parameter, "source": source, "confidence": "medium" if "estimate" in source else "high", "estimated": "estimate" in source}
        else:
            detail["parameter_count"] = {"value": None, "source": None, "confidence": "unknown", "estimated": False}

    if model.get("context_length") is None:
        config, _ = fetch_json(model_id, "config.json")
        tokenizer, _ = fetch_json(model_id, "tokenizer_config.json")
        value, source, candidates = find_context(config, tokenizer)
        if value is not None:
            model["context_length"] = value
            model["context_evidence"] = candidates
        detail["context_length"] = {"value": value, "source": source, "confidence": "high" if source else "unknown"}

    detail["readme_used"] = False
    return repaired


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool", choices=(*POOLS, "all"), default="all")
    args = parser.parse_args()
    pools = POOLS if args.pool == "all" else (args.pool,)
    for pool in pools:
        source = DATA_DIR / f"hf_models_stage2_{pool}.jsonl"
        output = DATA_DIR / f"hf_models_stage2_{pool}_repaired.jsonl"
        errors = DATA_DIR / f"hf_models_stage2_{pool}_repair_errors.jsonl"
        rows = read_jsonl(source)
        current = [row for row in rows if row.get("stage", {}).get("source_stage1_version") == SOURCE_STAGE1_VERSION and row.get("stage", {}).get("stage2_version") == SOURCE_STAGE2_VERSION]
        repaired = []
        error_rows = []
        for row in current:
            if row.get("model", {}).get("parameter_count") is not None and row.get("model", {}).get("context_length") is not None:
                repaired.append(row)
                continue
            try:
                repaired.append(repair_row(row))
            except Exception as exc:
                error_rows.append({"model_id": row.get("model_id"), "error_type": type(exc).__name__, "error": str(exc), "repair_version": REPAIR_VERSION})
                repaired.append(row)
        write_jsonl(output, repaired)
        write_jsonl(errors, error_rows)
        print(f"[{pool}] source={len(rows)} current={len(current)} repaired={len(repaired)} errors={len(error_rows)} -> {output}")


if __name__ == "__main__":
    main()
