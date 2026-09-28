#!/usr/bin/env python3
"""Build and query a maintainable Stage 3 parent-child evidence index.

The index is deliberately separate from Stage 3 and Stage 4 JSONL files.  Stage
3 remains the source of truth; this sidecar only materializes explicit parent
section records and child atomic evidence records for retrieval and generation.
It does not call Hugging Face or an embedding API.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
POOLS = ("core", "low_popularity")
INDEX_SCHEMA_VERSION = 1
INDEX_VERSION = 1


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(path)
    rows: List[Dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: expected an object")
        rows.append(value)
    return rows


def write_jsonl(rows: Iterable[Mapping[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(dict(row), ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")
    temporary.replace(path)


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _heading_path(span: Mapping[str, Any]) -> Tuple[str, ...]:
    value = span.get("heading_path")
    if isinstance(value, list) and value:
        return tuple(str(item).strip() for item in value if str(item).strip()) or ("document",)
    section = str(span.get("parent_section") or "document").strip()
    return (section or "document",)


def _parent_id(model_id: str, heading_path: Sequence[str]) -> str:
    key = digest(list(heading_path))[:12]
    return f"{model_id}::parent::{key}"


def materialize_parent_child_evidence(
    model_id: str, evidence: Mapping[str, Any]
) -> Dict[str, Any]:
    """Add relationship-only parent/child metadata to an existing evidence object.

    Child text stays in the existing ``spans`` list.  Parent records contain
    section identity and child IDs only, so this migration does not duplicate
    README text inside Stage 3 rows.
    """

    result = dict(evidence)
    raw_spans = evidence.get("spans") or []
    spans: List[Dict[str, Any]] = []
    grouped: "OrderedDict[Tuple[str, ...], List[str]]" = OrderedDict()
    for raw_span in raw_spans:
        if not isinstance(raw_span, dict):
            continue
        span = dict(raw_span)
        child_id = str(span.get("evidence_id") or span.get("chunk_id") or "")
        if not child_id:
            spans.append(span)
            continue
        heading_path = _heading_path(span)
        parent_id = _parent_id(model_id, heading_path)
        span["parent_id"] = parent_id
        grouped.setdefault(heading_path, []).append(child_id)
        spans.append(span)

    parents = [
        {
            "parent_id": _parent_id(model_id, heading_path),
            "heading_path": list(heading_path),
            "section": heading_path[-1] if heading_path else "document",
            "child_ids": child_ids,
        }
        for heading_path, child_ids in grouped.items()
    ]
    result["spans"] = spans
    result["parents"] = parents
    result["parent_child_schema_version"] = INDEX_SCHEMA_VERSION
    return result


def build_parent_child_row(stage3_row: Mapping[str, Any]) -> Dict[str, Any]:
    """Materialize one model's explicit parent sections and child spans."""

    model_id = str(stage3_row.get("model_id") or "")
    if not model_id:
        raise ValueError("Stage 3 row is missing model_id")
    raw_evidence = dict(stage3_row.get("evidence") or {})
    raw_spans = []
    for raw_span in raw_evidence.get("spans") or []:
        if isinstance(raw_span, dict):
            clean_span = dict(raw_span)
            clean_span.pop("parent_id", None)
            raw_spans.append(clean_span)
        else:
            raw_spans.append(raw_span)
    raw_evidence["spans"] = raw_spans
    raw_evidence.pop("parents", None)
    raw_evidence.pop("parent_child_schema_version", None)
    evidence = materialize_parent_child_evidence(model_id, raw_evidence)
    raw_spans = evidence.get("spans") or []
    if not isinstance(raw_spans, list):
        raise ValueError(f"{model_id}: evidence.spans must be a list")

    grouped: "OrderedDict[Tuple[str, ...], List[Dict[str, Any]]]" = OrderedDict()
    for span in raw_spans:
        if not isinstance(span, dict):
            continue
        child_id = str(span.get("evidence_id") or span.get("chunk_id") or "")
        text = str(span.get("text") or "").strip()
        if not child_id or not text:
            continue
        heading_path = _heading_path(span)
        parent_id = _parent_id(model_id, heading_path)
        child = {
            "child_id": child_id,
            "parent_id": parent_id,
            "text": text,
            "content_type": span.get("content_type"),
            "content_types": span.get("content_types") or [span.get("content_type")],
            "heading_path": list(heading_path),
            "parent_section": span.get("parent_section") or heading_path[0],
            "routed_fields": list(span.get("routed_fields") or []),
            "token_count": span.get("token_count"),
            "content_hash": span.get("content_hash") or digest(text),
        }
        grouped.setdefault(heading_path, []).append(child)

    parents: List[Dict[str, Any]] = []
    for heading_path, children in grouped.items():
        parent_id = _parent_id(model_id, heading_path)
        parents.append(
            {
                "parent_id": parent_id,
                "heading_path": list(heading_path),
                "section": heading_path[-1] if heading_path else "document",
                "text": "\n\n".join(child["text"] for child in children),
                "child_ids": [child["child_id"] for child in children],
                "children": children,
            }
        )

    # Derived parent/child fields are excluded so the source hash remains
    # stable before and after deterministic migration.
    source_evidence = {"evidence": raw_evidence, "stage3": stage3_row.get("stage3")}
    return {
        "schema_version": INDEX_SCHEMA_VERSION,
        "evidence_index_version": INDEX_VERSION,
        "model_id": model_id,
        "source_pool": stage3_row.get("source_pool"),
        "status": stage3_row.get("status"),
        "source_stage3_version": (stage3_row.get("stage3") or {}).get("stage3_version"),
        "source_stage3_hash": digest(source_evidence),
        "parents": parents,
        "child_count": sum(len(parent["children"]) for parent in parents),
        "parent_count": len(parents),
    }


def validate_index_rows(rows: Sequence[Mapping[str, Any]], pool: str) -> Dict[str, Any]:
    ids = [str(row.get("model_id") or "") for row in rows]
    bad: List[str] = []
    if len(ids) != len(set(ids)):
        bad.append("duplicate_model_id")
    for row in rows:
        model_id = str(row.get("model_id") or "")
        if row.get("source_pool") != pool:
            bad.append(f"pool:{model_id}")
        child_ids: List[str] = []
        for parent in row.get("parents") or []:
            parent_id = parent.get("parent_id")
            for child in parent.get("children") or []:
                child_ids.append(str(child.get("child_id") or ""))
                if child.get("parent_id") != parent_id:
                    bad.append(f"parent_link:{model_id}")
                if child.get("child_id") not in (parent.get("child_ids") or []):
                    bad.append(f"child_link:{model_id}")
        if len(child_ids) != len(set(child_ids)):
            bad.append(f"duplicate_child_id:{model_id}")
        if row.get("child_count") != len(child_ids):
            bad.append(f"child_count:{model_id}")
    return {
        "pool": pool,
        "rows": len(rows),
        "distinct_models": len(set(ids)),
        "parents": sum(int(row.get("parent_count") or 0) for row in rows),
        "children": sum(int(row.get("child_count") or 0) for row in rows),
        "bad_count": len(bad),
        "bad_examples": bad[:20],
    }


def build_pool(pool: str, data_dir: Path = DATA_DIR) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    source = data_dir / f"hf_models_stage3_{pool}.jsonl"
    source_rows = read_jsonl(source)
    index_rows = [build_parent_child_row(row) for row in source_rows]
    for row in index_rows:
        row["source_pool"] = pool
    validation = validate_index_rows(index_rows, pool)
    if validation["bad_count"]:
        raise ValueError(f"{pool}: parent-child validation failed: {validation}")
    return index_rows, validation


def migrate_stage3_pool(
    pool: str, data_dir: Path = DATA_DIR, apply: bool = False
) -> Dict[str, Any]:
    """Add relationship-only parent/child metadata to existing Stage 3 rows."""

    path = data_dir / f"hf_models_stage3_{pool}.jsonl"
    rows = read_jsonl(path)
    stage2_path = data_dir / f"hf_models_stage2_{pool}.jsonl"
    stage2_rows = read_jsonl(stage2_path) if stage2_path.exists() else []
    stage2_by_id = {str(row.get("model_id") or ""): row for row in stage2_rows}
    changed = 0
    migrated: List[Dict[str, Any]] = []
    for row in rows:
        updated = dict(row)
        old_evidence = row.get("evidence") or {}
        new_evidence = materialize_parent_child_evidence(
            str(row.get("model_id") or ""), old_evidence
        )
        updated["evidence"] = new_evidence
        stage = dict(updated.get("stage3") or {})
        stage["parent_child_schema_version"] = INDEX_SCHEMA_VERSION
        current_stage2 = stage2_by_id.get(str(row.get("model_id") or ""))
        if current_stage2 is not None:
            # Establish the current Stage 2 snapshot as the deterministic
            # resume baseline; no semantic LLM output is regenerated here.
            stage["source_stage2_hash"] = digest(current_stage2)
        updated["stage3"] = stage
        if (
            canonical_json(old_evidence) != canonical_json(new_evidence)
            or canonical_json(row.get("stage3") or {}) != canonical_json(stage)
        ):
            changed += 1
        migrated.append(updated)
    if apply:
        write_jsonl(migrated, path)
    return {
        "pool": pool,
        "rows": len(rows),
        "changed": changed,
        "applied": apply,
        "output": str(path),
    }


_TOKEN_RE = re.compile(r"[0-9A-Za-z가-힣][0-9A-Za-z가-힣_./+\-]*", re.UNICODE)


def tokenize(value: Any) -> List[str]:
    return [token.casefold() for token in _TOKEN_RE.findall(str(value or ""))]


def evidence_score(query: str, child: Mapping[str, Any]) -> Tuple[float, List[str]]:
    query_text = " ".join(tokenize(query))
    query_tokens = set(tokenize(query))
    if not query_tokens:
        return 0.0, []
    child_text = str(child.get("text") or "")
    heading_text = " ".join(child.get("heading_path") or [])
    child_tokens = set(tokenize(child_text))
    heading_tokens = set(tokenize(heading_text))
    matched = sorted(query_tokens & child_tokens)
    overlap = len(matched) / max(1, len(query_tokens))
    heading_overlap = len(query_tokens & heading_tokens) / max(1, len(query_tokens))
    phrase = 1.0 if query_text and query_text in " ".join(tokenize(child_text)) else 0.0
    score = min(1.0, 0.72 * overlap + 0.18 * heading_overlap + 0.10 * phrase)
    return score, matched


def search_model_evidence(
    index_row: Mapping[str, Any], query: str, top_k: int = 3
) -> List[Dict[str, Any]]:
    """Return child evidence hits with parent context for one candidate model."""

    hits: List[Dict[str, Any]] = []
    for parent in index_row.get("parents") or []:
        parent_context = {
            "parent_id": parent.get("parent_id"),
            "parent_section": parent.get("section"),
            "heading_path": parent.get("heading_path") or [],
            "parent_text": parent.get("text") or "",
        }
        for child in parent.get("children") or []:
            score, matched = evidence_score(query, child)
            if score <= 0:
                continue
            hits.append(
                {
                    "child_id": child.get("child_id"),
                    "parent_id": parent_context["parent_id"],
                    "parent_section": parent_context["parent_section"],
                    "heading_path": parent_context["heading_path"],
                    "content_type": child.get("content_type"),
                    "routed_fields": child.get("routed_fields") or [],
                    "score": round(score, 6),
                    "matched_terms": matched,
                    "quote": child.get("text") or "",
                    "parent_text": parent_context["parent_text"],
                }
            )
    hits.sort(key=lambda item: (item["score"], item["child_id"]), reverse=True)
    return hits[: max(0, int(top_k))]


def load_index(paths: Iterable[Path]) -> Dict[Tuple[str, str], Dict[str, Any]]:
    catalog: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for path in paths:
        for row in read_jsonl(path):
            key = (str(row.get("source_pool") or ""), str(row.get("model_id") or ""))
            catalog[key] = row
    return catalog


def attach_evidence_hits(
    candidates: Sequence[Mapping[str, Any]],
    query: str,
    catalog: Mapping[Tuple[str, str], Mapping[str, Any]],
    top_k: int = 3,
    candidate_limit: int = 50,
    weight: float = 0.08,
) -> List[Dict[str, Any]]:
    """Apply optional second-stage evidence reranking without changing eligibility."""

    reranked: List[Dict[str, Any]] = []
    for index, candidate in enumerate(candidates):
        result = dict(candidate)
        key = (str(candidate.get("source_pool") or ""), str(candidate.get("model_id") or ""))
        hits = search_model_evidence(catalog[key], query, top_k) if index < candidate_limit and key in catalog else []
        result["_evidence_hits"] = hits
        result["_evidence_score"] = hits[0]["score"] if hits else 0.0
        base_score = float(candidate.get("_adjusted_score", candidate.get("score") or 0.0))
        result["_evidence_adjusted_score"] = base_score + weight * result["_evidence_score"]
        reranked.append(result)
    reranked.sort(
        key=lambda item: (item.get("_evidence_adjusted_score", item.get("_adjusted_score", 0.0)), item.get("model_id", "")),
        reverse=True,
    )
    return reranked


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool", choices=("core", "low_popularity", "all"), default="all")
    parser.add_argument("--output-dir", type=Path, default=DATA_DIR)
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument(
        "--migrate-stage3",
        action="store_true",
        help="add parent/child IDs to existing Stage 3 rows without an LLM call",
    )
    parser.add_argument("--apply", action="store_true", help="write deterministic migration changes")
    args = parser.parse_args()

    pools = POOLS if args.pool == "all" else (args.pool,)
    if args.migrate_stage3:
        summaries = [migrate_stage3_pool(pool, DATA_DIR, apply=args.apply) for pool in pools]
        print(json.dumps({"migration": summaries}, ensure_ascii=False, indent=2))
        return 0

    summaries: List[Dict[str, Any]] = []
    for pool in pools:
        rows, validation = build_pool(pool, DATA_DIR)
        output = args.output_dir / f"hf_models_stage3_parent_child_{pool}.jsonl"
        if not args.validate_only:
            write_jsonl(rows, output)
        summary = dict(validation)
        summary.update({"output": str(output), "written": not args.validate_only})
        print(json.dumps(summary, ensure_ascii=False))
        summaries.append(summary)

    manifest = {
        "schema_version": INDEX_SCHEMA_VERSION,
        "evidence_index_version": INDEX_VERSION,
        "pools": summaries,
        "source": "Stage 3 atomic evidence; Stage 1/2/4 unchanged",
    }
    if not args.validate_only:
        (args.output_dir / "hf_models_stage3_parent_child_manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
