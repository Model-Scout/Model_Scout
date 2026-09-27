#!/usr/bin/env python3
"""Stage 3 semantic enrichment using Atomic Evidence v6.

Stage 3 reads Stage 2 Core and Low Popularity JSONL files, routes exact
README evidence spans to a low-cost LLM, and writes semantic summaries with
deterministic supporting quotes. The script supports per-pool resume and is
safe to run with ``--dry-run`` before an API-backed run.

It does not change Stage 1 or Stage 2 files and does not use an LLM to decide
candidate tiers, popularity, Korean support, or model quality.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from dotenv import load_dotenv

from evidence_index import INDEX_SCHEMA_VERSION, materialize_parent_child_evidence


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
SOURCE_POOLS = ("core", "low_popularity")
STAGE3_VERSION = 1
PROMPT_VERSION = "stage3-atomic-evidence-v1"
COMPATIBLE_PROMPT_VERSIONS = {PROMPT_VERSION, "stage3-atomic-evidence-full-readme-v1"}
CHUNKER_VERSION = "atomic-evidence-v1"
DEFAULT_MODEL = "gpt-4o-mini"
MAX_SOURCE_CHARS = 60_000
TARGET_SPAN_CHARS = 1_800

FIELD_CONFIG: Dict[str, Dict[str, Any]] = {
    "documented_strengths": {
        "max_spans": 4,
        "max_claims": 2,
        "keywords": ("feature", "capability", "supported", "strength", "translation", "embedding", "speech recognition", "text generation"),
    },
    "documented_limitations": {
        "max_spans": 3,
        "max_claims": 2,
        "keywords": ("limitation", "known issue", "caveat", "does not support", "constraint"),
    },
    "use_cases": {
        "max_spans": 4,
        "max_claims": 3,
        "keywords": ("usage", "use case", "example", "pipeline", "inference", "application", "translation", "embedding", "transcription"),
    },
    "benchmarks": {
        "max_spans": 4,
        "max_claims": 3,
        "keywords": ("benchmark", "evaluation", "result", "performance", "metric", "score", "bleu", "rouge", "wer", "accuracy", "f1"),
    },
    "license_notes": {
        "max_spans": 2,
        "max_claims": 2,
        "keywords": ("license", "licence", "terms", "restriction", "commercial", "copyright", "apache", "mit", "cc-by"),
    },
    "warnings": {
        "max_spans": 3,
        "max_claims": 2,
        "keywords": ("warning", "safety", "risk", "bias", "disclaimer", "security", "privacy", "limitation"),
    },
}

CLAIM_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "text": {"type": "string"},
        "evidence_refs": {"type": "array", "items": {"type": "string"}},
        "supporting_quote": {"type": "string"},
        "evidence_level": {"type": "string", "enum": ["explicit", "derived", "unknown"]},
    },
    "required": ["text", "evidence_refs", "supporting_quote", "evidence_level"],
}

SEMANTIC_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "summary": {
            "type": "object",
            "additionalProperties": False,
            "properties": {"text": {"type": "string"}, "evidence_refs": {"type": "array", "items": {"type": "string"}}},
            "required": ["text", "evidence_refs"],
        },
        "documented_strengths": {"type": "array", "items": CLAIM_SCHEMA},
        "documented_limitations": {"type": "array", "items": CLAIM_SCHEMA},
        "use_cases": {"type": "array", "items": CLAIM_SCHEMA},
        "benchmarks": {"type": "array", "items": CLAIM_SCHEMA},
        "license_notes": {"type": "array", "items": CLAIM_SCHEMA},
        "unknowns": {"type": "array", "items": {"type": "string"}},
        "warnings": {"type": "array", "items": CLAIM_SCHEMA},
        "evidence_completeness": {"type": "string", "enum": ["high", "medium", "low", "unknown"]},
    },
    "required": ["summary", "documented_strengths", "documented_limitations", "use_cases", "benchmarks", "license_notes", "unknowns", "warnings", "evidence_completeness"],
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def source_stage2_hash(row: Dict[str, Any]) -> str:
    """Return a stable fingerprint for TTL-safe Stage 3 resume decisions."""
    payload = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return digest(payload)


def normalize(value: str) -> str:
    return " ".join(value.casefold().replace("_", " ").replace("-", " ").split())


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def append_jsonl(path: Path, row: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def save_jsonl_atomic(rows: Sequence[Dict[str, Any]], path: Path) -> None:
    """Replace a Stage 3 pool with the current Stage 2-derived snapshot."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    payload = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    temp_path.write_text(payload, encoding="utf-8")
    os.replace(temp_path, path)


def replace_row(path: Path, model_id: str) -> None:
    rows = [row for row in read_jsonl(path) if row.get("model_id") != model_id]
    if rows:
        path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    elif path.exists():
        path.unlink()


def source_path(row: Dict[str, Any]) -> Optional[Path]:
    readme = row.get("source", {}).get("readme", {}) or {}
    relative = readme.get("path")
    if not readme.get("available") or not relative:
        return None
    path = Path(relative)
    return path if path.is_absolute() else ROOT / path


def load_source(row: Dict[str, Any]) -> Tuple[Optional[str], Dict[str, Any]]:
    path = source_path(row)
    readme = dict(row.get("source", {}).get("readme", {}) or {})
    if path is None or not path.exists():
        return None, readme
    text = path.read_text(encoding="utf-8", errors="replace")[:MAX_SOURCE_CHARS]
    readme.update({"used_chars": len(text), "content_hash": digest(text), "stage3_truncated": len(text) >= MAX_SOURCE_CHARS})
    return text, readme


def split_long(text: str) -> List[str]:
    if len(text) <= TARGET_SPAN_CHARS:
        return [text]
    pieces: List[str] = []
    start = 0
    while start < len(text):
        end = min(len(text), start + TARGET_SPAN_CHARS)
        if end < len(text):
            boundary = max(text.rfind(" ", start + TARGET_SPAN_CHARS // 2, end), text.rfind("\n", start + TARGET_SPAN_CHARS // 2, end))
            if boundary > start:
                end = boundary
        piece = text[start:end].strip()
        if piece:
            pieces.append(piece)
        start = end
    return pieces


def sentence_spans(text: str) -> List[str]:
    matches = list(re.finditer(r"[^.!?。！？]+(?:[.!?。！？]+|$)", text, flags=re.S))
    pieces = [match.group(0).strip() for match in matches if match.group(0).strip()]
    return pieces or ([text.strip()] if text.strip() else [])


def atomic_spans(text: str) -> List[Dict[str, Any]]:
    """Split exact README substrings into sentence/list/table/code evidence."""
    lines = text.splitlines(keepends=True)
    raw: List[Tuple[str, str, List[str]]] = []
    heading = ["document"]
    paragraph: List[str] = []
    paragraph_heading = list(heading)
    code: List[str] = []
    code_heading = list(heading)
    table: List[str] = []
    table_heading = list(heading)
    in_code = False

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            for piece in sentence_spans("".join(paragraph)):
                raw.append(("paragraph", piece, list(paragraph_heading)))
            paragraph = []

    def flush_code() -> None:
        nonlocal code
        if code:
            for piece in split_long("".join(code)):
                raw.append(("code", piece, list(code_heading)))
            code = []

    def flush_table() -> None:
        nonlocal table
        if table:
            for line in table:
                if line.strip():
                    raw.append(("table", line.strip(), list(table_heading)))
            table = []

    for line in lines:
        stripped = line.strip()
        heading_match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", stripped)
        if in_code:
            code.append(line)
            if stripped.startswith(("```", "~~~")) and len(code) > 1:
                in_code = False
                flush_code()
            continue
        if stripped.startswith(("```", "~~~")):
            flush_paragraph(); flush_table(); in_code = True; code_heading = list(heading); code = [line]; continue
        if heading_match:
            flush_paragraph(); flush_table(); heading = [heading_match.group(2).strip()]
            raw.append(("heading", stripped, list(heading))); continue
        if stripped.startswith("|") and stripped.count("|") >= 2:
            flush_paragraph()
            if not table: table_heading = list(heading)
            table.append(line); continue
        if table: flush_table()
        if not stripped:
            flush_paragraph(); continue
        if re.match(r"^(?:[-*+] |\d+[.)] )", stripped):
            flush_paragraph(); raw.append(("list", stripped, list(heading))); continue
        if not paragraph: paragraph_heading = list(heading)
        paragraph.append(line)
    if in_code: flush_code()
    flush_paragraph(); flush_table()

    spans: List[Dict[str, Any]] = []
    for kind, value, headings in raw:
        for piece in split_long(value):
            if not piece.strip():
                continue
            evidence_id = f"evidence-{len(spans) + 1:05d}"
            spans.append({
                "chunk_id": evidence_id,
                "evidence_id": evidence_id,
                "heading_path": headings or ["document"],
                "parent_section": (headings or ["document"])[0],
                "content_type": kind,
                "content_types": [kind],
                "text": piece,
                "token_count": max(1, len(re.findall(r"\S+", piece))),
                "content_hash": digest(piece),
            })
    return spans


def score_span(span: Dict[str, Any], keywords: Sequence[str]) -> int:
    haystack = normalize(" ".join(span.get("heading_path", [])) + " " + span.get("text", ""))
    return sum(1 for keyword in keywords if normalize(keyword) in haystack)


def route_spans(spans: Sequence[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, List[str]]]:
    selected: Dict[str, Dict[str, Any]] = {}
    field_ids: Dict[str, List[str]] = {}
    for field, config in FIELD_CONFIG.items():
        ranked = sorted(spans, key=lambda span: (-score_span(span, config["keywords"]), span["evidence_id"]))
        ranked = [span for span in ranked if score_span(span, config["keywords"]) > 0]
        chosen: List[Dict[str, Any]] = []
        sections: set[str] = set()
        for span in ranked:
            section = span.get("parent_section", "document")
            if section in sections and len(sections) < config["max_spans"]:
                continue
            chosen.append(span); sections.add(section)
            if len(chosen) >= config["max_spans"]: break
        if len(chosen) < config["max_spans"]:
            chosen_ids = {span["evidence_id"] for span in chosen}
            for span in ranked:
                if span["evidence_id"] in chosen_ids: continue
                chosen.append(span)
                if len(chosen) >= config["max_spans"]: break
        field_ids[field] = [span["evidence_id"] for span in chosen]
        for span in chosen:
            item = selected.setdefault(span["evidence_id"], dict(span))
            item.setdefault("routed_fields", [])
            if field not in item["routed_fields"]: item["routed_fields"].append(field)
    return list(selected.values()), field_ids


def build_prompt(row: Dict[str, Any], spans: Sequence[Dict[str, Any]], field_ids: Dict[str, List[str]]) -> List[Dict[str, str]]:
    routing = "\n".join(
        f"FIELD={field} MAX_CLAIMS={config['max_claims']} EVIDENCE_IDS={json.dumps(field_ids.get(field, []), ensure_ascii=False)}"
        for field, config in FIELD_CONFIG.items()
    )
    evidence = "\n\n".join(
        f"<EVIDENCE id={span['evidence_id']} heading={json.dumps(span['heading_path'], ensure_ascii=False)} type={span['content_type']}>\n{span['text']}\n</EVIDENCE>"
        for span in spans
    )
    system = (
        "You are a strictly grounded model-card analyst. Use only supplied README evidence. "
        "For every non-unknown claim choose exactly one EVIDENCE id from the routed IDs for "
        "that field. Do not invent IDs or use outside knowledge. Do not write supporting_quote: "
        "return an empty string because the program copies the exact source span. Do not infer "
        "quality, safety, licensing permission, or hardware suitability. Respect MAX_CLAIMS. "
        "If evidence is insufficient, omit the claim or use unknowns. Return only JSON schema."
    )
    user = f"MODEL_ID={row['model_id']}\n\nFIELD_ROUTING:\n{routing}\n\nATOMIC_README_EVIDENCE:\n{evidence}"
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def materialize(semantic: Dict[str, Any], spans: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    by_id = {span["evidence_id"]: span for span in spans}
    for field, config in FIELD_CONFIG.items():
        output: List[Dict[str, Any]] = []
        for claim in (semantic.get(field) or [])[: config["max_claims"]]:
            if not isinstance(claim, dict): continue
            refs = [ref for ref in (claim.get("evidence_refs") or []) if ref in by_id]
            if claim.get("evidence_level") == "unknown":
                text = (claim.get("text") or "").strip()
                if text: semantic.setdefault("unknowns", []).append(text)
                continue
            if not refs: continue
            claim["evidence_refs"] = [refs[0]]
            claim["supporting_quote"] = by_id[refs[0]]["text"]
            output.append(claim)
        semantic[field] = output
    summary = semantic.get("summary") or {}
    summary["evidence_refs"] = [ref for ref in (summary.get("evidence_refs") or []) if ref in by_id][:2]
    semantic["summary"] = summary
    return semantic


def validate(semantic: Dict[str, Any], spans: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    ids = {span["evidence_id"] for span in spans}
    claim_count = 0; invalid = 0; uncited = 0; missing = 0; quote_mismatch = 0
    for field in FIELD_CONFIG:
        for claim in semantic.get(field, []) or []:
            claim_count += 1
            refs = claim.get("evidence_refs") or []
            if not refs or any(ref not in ids for ref in refs): invalid += 1
            if claim.get("evidence_level") != "unknown" and not refs: uncited += 1
            quote = (claim.get("supporting_quote") or "").strip()
            if claim.get("evidence_level") != "unknown" and not quote: missing += 1
            if quote and not any(quote.casefold() in span.get("text", "").casefold() for span in spans if span["evidence_id"] in refs): quote_mismatch += 1
    summary_refs = (semantic.get("summary") or {}).get("evidence_refs") or []
    if any(ref not in ids for ref in summary_refs): invalid += 1
    return {"claim_count": claim_count, "invalid_evidence_refs": invalid, "uncited_claims": uncited, "missing_quotes": missing, "quote_mismatches": quote_mismatch}


def call_llm(client: Any, model: str, messages: Sequence[Dict[str, str]]) -> Dict[str, Any]:
    response = client.chat.completions.create(
        model=model, messages=list(messages), temperature=0, max_tokens=1500,
        response_format={"type": "json_schema", "json_schema": {"name": "stage3_atomic_semantic_enrichment", "strict": True, "schema": SEMANTIC_SCHEMA}},
    )
    value = json.loads(response.choices[0].message.content or "{}")
    if not isinstance(value, dict): raise ValueError("LLM response was not an object")
    return value


def paths(pool: str) -> Tuple[Path, Path, Path]:
    return (DATA_DIR / f"hf_models_stage2_{pool}.jsonl", DATA_DIR / f"hf_models_stage3_{pool}.jsonl", DATA_DIR / f"hf_models_stage3_{pool}_errors.jsonl")


def enrich_pool(pool: str, model: str, limit: Optional[int], dry_run: bool) -> Dict[str, Any]:
    input_path, output_path, error_path = paths(pool)
    source_rows = read_jsonl(input_path)
    source_ids = [row.get("model_id") for row in source_rows]
    if len(source_ids) != len(set(source_ids)):
        raise ValueError(f"[{pool}] Stage 2 contains duplicate model_id values")

    existing = {row.get("model_id"): row for row in read_jsonl(output_path)}
    rows = source_rows[:limit] if limit is not None else source_rows
    selected_ids = {row["model_id"] for row in rows}
    # Keep unselected rows for bounded test runs, but never carry a selected
    # row forward until it is confirmed reusable or regenerated successfully.
    # This prunes models that moved between Core and Low and avoids publishing
    # stale semantic metadata after a failed re-enrichment.
    results_by_id = {
        model_id: existing[model_id]
        for model_id in source_ids
        if model_id in existing and model_id not in selected_ids
    }
    client = None
    if not dry_run:
        from openai import OpenAI
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    stats = {"pool": pool, "total": len(rows), "completed": 0, "skipped": 0, "no_source": 0, "errors": 0, "api_calls": 0}
    for index, row in enumerate(rows, start=1):
        model_id = row["model_id"]
        old = existing.get(model_id)
        old_stage = old.get("stage3", {}) if old else {}
        current_stage2_hash = source_stage2_hash(row)
        previous_stage2_hash = old_stage.get("source_stage2_hash") if old else None
        if previous_stage2_hash is None and old and old.get("source_stage2"):
            previous_stage2_hash = source_stage2_hash(old["source_stage2"])
        if old and old.get("status") == "completed" and old_stage.get("stage3_version") == STAGE3_VERSION and old_stage.get("prompt_version") in COMPATIBLE_PROMPT_VERSIONS and previous_stage2_hash == current_stage2_hash and (old.get("evidence") or {}).get("parent_child_schema_version") == INDEX_SCHEMA_VERSION:
            results_by_id[model_id] = old
            stats["skipped"] += 1
            continue
        text, readme = load_source(row)
        stage = {"source_pool": pool, "source_stage2_version": row.get("stage", {}).get("stage2_version"), "source_stage2_hash": current_stage2_hash, "stage3_version": STAGE3_VERSION, "prompt_version": PROMPT_VERSION, "chunker_version": CHUNKER_VERSION, "parent_child_schema_version": INDEX_SCHEMA_VERSION, "semantic_enriched": False, "enriched_at": utc_now()}
        if not text:
            result = {"model_id": model_id, "source_pool": pool, "status": "no_source", "source_stage2": row, "semantic": None, "evidence": materialize_parent_child_evidence(model_id, {"readme": readme, "spans": []}), "stage3": stage}
            if not dry_run:
                results_by_id[model_id] = result
            stats["completed"] += 1; stats["no_source"] += 1; continue
        spans, field_ids = route_spans(atomic_spans(text))
        messages = build_prompt(row, spans, field_ids)
        try:
            if dry_run:
                semantic = {"summary": {"text": "", "evidence_refs": []}, "documented_strengths": [], "documented_limitations": [], "use_cases": [], "benchmarks": [], "license_notes": [], "unknowns": [], "warnings": [], "evidence_completeness": "unknown"}
            else:
                stats["api_calls"] += 1
                print(f"[{pool}] {index}/{len(rows)} ENRICH {model_id} spans={len(spans)}", flush=True)
                semantic = call_llm(client, model, messages)
            semantic = materialize(semantic, spans)
            checks = validate(semantic, spans)
            stage["semantic_enriched"] = True; stage["enriched_at"] = utc_now()
            evidence = materialize_parent_child_evidence(model_id, {"readme": readme, "field_evidence_ids": field_ids, "spans": spans, "prompt_token_estimate": sum(len(message["content"].split()) for message in messages)})
            result = {"model_id": model_id, "source_pool": pool, "status": "completed", "source_stage2": row, "semantic": semantic, "evidence": evidence, "validation": checks, "stage3": stage}
            if not dry_run:
                results_by_id[model_id] = result
            stats["completed"] += 1
        except Exception as exc:
            error = {"model_id": model_id, "source_pool": pool, "status": "error", "error_type": type(exc).__name__, "error": str(exc), "stage3_version": STAGE3_VERSION, "created_at": utc_now()}
            append_jsonl(error_path, error); stats["errors"] += 1
            print(f"[{pool}] ERROR {model_id}: {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
            time.sleep(0.1)

    if not dry_run:
        ordered_results = [
            results_by_id[model_id]
            for model_id in source_ids
            if model_id in results_by_id
        ]
        save_jsonl_atomic(ordered_results, output_path)

    print(f"[{pool}] FINISHED {json.dumps(stats, ensure_ascii=False)}")
    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool", choices=(*SOURCE_POOLS, "all"), default="all")
    parser.add_argument("--limit", type=int, default=None, help="Optional per-pool limit for a smoke test")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--model", default=None)
    args = parser.parse_args()
    load_dotenv(ROOT / ".env")
    model = args.model or os.getenv("STAGE3_LLM_MODEL") or os.getenv("OPENAI_MODEL") or DEFAULT_MODEL
    if not args.dry_run and not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is required unless --dry-run is used")
    pools = SOURCE_POOLS if args.pool == "all" else (args.pool,)
    summaries = [enrich_pool(pool, model, args.limit, args.dry_run) for pool in pools]
    errors = sum(summary.get("errors", 0) for summary in summaries)
    if errors:
        raise RuntimeError(
            f"Stage 3 failed for {errors} model(s); refusing to continue "
            "with an incomplete semantic snapshot"
        )
    print(json.dumps({"stage3_version": STAGE3_VERSION, "model": model, "summaries": summaries}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
