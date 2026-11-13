"""Stage D5: publish the dataset index (cards, chunks, vectors) to Supabase pgvector.

Reads data/dataset_index (14) and data/hypergraph (13) and mirrors them into
public.model_scout_datasets / public.model_scout_dataset_chunks (supabase_dataset_schema.sql).
The local index is the source of truth and the tables are derived from it: only chunks whose
text hash changed are uploaded, and datasets or chunks that left the index are deleted.
Writes are committed in batches (upserts first, deletes last), so an interrupted sync leaves a
superset of the index and a rerun resumes from the text-hash diff.

Storage is budgeted even on Supabase Pro: vectors are halfvec, chunk text is a 600-char
preview (full text stays in data/dataset_index/chunks.jsonl), and the sync refuses to write
when the projected database size passes the 1 GB internal safety ceiling
(SUPABASE_DB_BUDGET_MB, default 1024).

    python 20_sync_dataset_index.py            # offline validation and size estimate
    python 20_sync_dataset_index.py --apply    # write Supabase
"""

from __future__ import annotations

import argparse
import json
import os
from collections import defaultdict
from pathlib import Path

AI_DIR = Path(__file__).resolve().parent
DATA_DIR = AI_DIR / "data"
INDEX_DIR = DATA_DIR / "dataset_index"
HYPERGRAPH_DIR = DATA_DIR / "hypergraph"
SCHEMA_SQL = Path(__file__).with_name("supabase_dataset_schema.sql")
DIMENSION = 1536
TEXT_PREVIEW_CHARS = 600
# Postgres bytes per chunk beyond its text: halfvec (2 B x 1536), tuple header, pk/fk/hash indexes.
CHUNK_OVERHEAD_BYTES = 2 * DIMENSION + 400
DATASET_OVERHEAD_BYTES = 300
# Pro includes an 8 GB disk; 1 GB remains a conservative application-level ceiling shared
# with the model reingest so an accidental corpus explosion is still blocked.
DEFAULT_BUDGET_MB = 1024
# Measured 2026-11-01: 34.8K chunks + 15K datasets took 209 MB against a 160 MB raw estimate
# (TOAST, page fill, index pages), so the estimate is scaled up before the budget check.
STORAGE_FACTOR = 1.35


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def load_index():
    import numpy as np

    manifest = json.loads((INDEX_DIR / "manifest.json").read_text(encoding="utf-8"))
    chunks = read_jsonl(INDEX_DIR / "chunks.jsonl")
    vectors = np.load(INDEX_DIR / "embeddings.npy")
    entities = {e["name"]: e for e in read_jsonl(HYPERGRAPH_DIR / "entities.jsonl") if e["kind"] == "dataset"}
    concepts = defaultdict(list)
    for link in read_jsonl(HYPERGRAPH_DIR / "links.jsonl"):
        if link["entity_id"].startswith("dataset:"):
            concepts[link["entity_id"].split(":", 1)[1]].append(link["concept_id"])
    return manifest, chunks, vectors, entities, concepts


def validate(manifest, chunks, vectors, entities):
    problems = []
    if vectors.shape != (len(chunks), DIMENSION):
        problems.append(f"embeddings {vectors.shape} != ({len(chunks)}, {DIMENSION}); run 14 --embed")
    if [c["chunk_id"] for c in chunks] != manifest["chunk_ids"]:
        problems.append("chunks.jsonl and manifest.json disagree; run 14 --embed")
    if [c["text_hash"] for c in chunks] != manifest["text_hashes"]:
        problems.append("chunk texts changed since the last embedding; run 14 --embed")
    orphans = {c["dataset_id"] for c in chunks} - set(entities)
    if orphans:
        problems.append(
            f"{len(orphans)} chunk datasets missing from the hypergraph, e.g. {sorted(orphans)[:3]}; run 13 then 14"
        )
    if problems:
        raise SystemExit("dataset index validation failed:\n- " + "\n- ".join(problems))


def estimated_bytes(chunks, entities):
    text = sum(len(c["text"][:TEXT_PREVIEW_CHARS].encode("utf-8")) for c in chunks)
    entity = sum(len(json.dumps(e, ensure_ascii=False).encode("utf-8")) for e in entities.values())
    raw = text + len(chunks) * CHUNK_OVERHEAD_BYTES + entity + len(entities) * DATASET_OVERHEAD_BYTES
    return int(raw * STORAGE_FACTOR)


def check_budget(cur, needed_bytes):
    """Projected DB size = today's size - the dataset tables we replace + what we will write."""
    cur.execute("""select pg_database_size(current_database()),
                          coalesce(pg_total_relation_size(to_regclass('public.model_scout_dataset_chunks')), 0)
                        + coalesce(pg_total_relation_size(to_regclass('public.model_scout_datasets')), 0)""")
    database, current = cur.fetchone()
    projected_mb = (database - current + needed_bytes) / 1e6
    budget_mb = float(os.getenv("SUPABASE_DB_BUDGET_MB", DEFAULT_BUDGET_MB))
    if projected_mb > budget_mb:
        raise SystemExit(
            f"projected database {projected_mb:.0f} MB > budget {budget_mb:.0f} MB; "
            "lower MAX_SECTION_CHUNKS (14) or FILE_CAP_PER_CATEGORY (18), or raise SUPABASE_DB_BUDGET_MB"
        )
    return round(projected_mb)


def apply(manifest, chunks, vectors, entities, concepts, batch_size):
    from psycopg2.extras import execute_values

    from supabase_db import db_connection, vector_literal

    conn = db_connection()
    try:
        with conn.cursor() as cur:
            projected_mb = check_budget(cur, estimated_bytes(chunks, entities))
        conn.rollback()
        with conn, conn.cursor() as cur:
            cur.execute(SCHEMA_SQL.read_text(encoding="utf-8"))

        # Batched commits: each batch is its own short transaction (a single 200 MB transaction
        # risks the pooler's statement timeout). Upserts run first and deletes last, so a sync
        # that dies midway leaves a superset of the index, never a gap; rerunning resumes from
        # the text-hash diff.
        dataset_rows = [
            (
                name,
                e["source"],
                e.get("title"),
                e["url"],
                e.get("summary_ko"),
                sorted(concepts[name]),
                json.dumps(e, ensure_ascii=False),
            )
            for name, e in entities.items()
        ]
        for start in range(0, len(dataset_rows), batch_size):
            with conn, conn.cursor() as cur:
                execute_values(
                    cur,
                    """
                    insert into public.model_scout_datasets
                        (dataset_id, source, title, url, summary_ko, concepts, entity)
                    values %s
                    on conflict (dataset_id) do update set source = excluded.source, title = excluded.title,
                        url = excluded.url, summary_ko = excluded.summary_ko, concepts = excluded.concepts,
                        entity = excluded.entity, active = true, updated_at = now()
                    -- unchanged rows are skipped: a no-op update still writes a new tuple (bloat)
                    where (model_scout_datasets.entity, model_scout_datasets.concepts, model_scout_datasets.active)
                          is distinct from (excluded.entity, excluded.concepts, true)""",
                    dataset_rows[start : start + batch_size],
                )

        with conn, conn.cursor() as cur:
            cur.execute("select chunk_id, text_hash from public.model_scout_dataset_chunks")
            stored = dict(cur.fetchall())
        changed = [i for i, c in enumerate(chunks) if stored.get(c["chunk_id"]) != c["text_hash"]]
        for start in range(0, len(changed), batch_size):
            rows = [
                (
                    chunks[i]["chunk_id"],
                    chunks[i]["dataset_id"],
                    chunks[i]["kind"],
                    chunks[i]["heading_path"],
                    chunks[i]["text"][:TEXT_PREVIEW_CHARS],
                    chunks[i]["text_hash"],
                    vector_literal(vectors[i]),
                )
                for i in changed[start : start + batch_size]
            ]
            with conn, conn.cursor() as cur:
                execute_values(
                    cur,
                    """
                    insert into public.model_scout_dataset_chunks
                        (chunk_id, dataset_id, kind, heading_path, text, text_hash, embedding)
                    values %s
                    on conflict (chunk_id) do update set dataset_id = excluded.dataset_id, kind = excluded.kind,
                        heading_path = excluded.heading_path, text = excluded.text, text_hash = excluded.text_hash,
                        embedding = excluded.embedding, updated_at = now()""",
                    rows,
                    template="(%s, %s, %s, %s, %s, %s, %s::halfvec)",
                )
            print(f"[SYNC] chunks {min(start + batch_size, len(changed))}/{len(changed)}", flush=True)

        with conn, conn.cursor() as cur:
            cur.execute(
                "delete from public.model_scout_dataset_chunks where not (chunk_id = any(%s))",
                ([c["chunk_id"] for c in chunks],),
            )
            removed_chunks = cur.rowcount
            cur.execute("delete from public.model_scout_datasets where not (dataset_id = any(%s))", (list(entities),))
            removed_datasets = cur.rowcount
        with conn.cursor() as cur:
            cur.execute("select count(*) from public.model_scout_dataset_chunks")
            total = cur.fetchone()[0]
            cur.execute(
                "select pg_size_pretty(pg_total_relation_size('public.model_scout_dataset_chunks')), "
                "pg_size_pretty(pg_database_size(current_database()))"
            )
            table_size, db_size = cur.fetchone()
    finally:
        conn.close()
    return {
        "projected_mb": projected_mb,
        "datasets": len(dataset_rows),
        "removed_datasets": removed_datasets,
        "uploaded_chunks": len(changed),
        "removed_chunks": removed_chunks,
        "chunks_in_db": total,
        "chunks_table": table_size,
        "database": db_size,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--apply", action="store_true", help="write Supabase")
    parser.add_argument("--batch-size", type=int, default=300)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        return self_check()
    manifest, chunks, vectors, entities, concepts = load_index()
    validate(manifest, chunks, vectors, entities)
    summary = {
        "datasets": len(entities),
        "chunks": len(chunks),
        "estimated_write_mb": round(estimated_bytes(chunks, entities) / 1e6),
    }
    if args.apply:
        summary.update(apply(manifest, chunks, vectors, entities, concepts, args.batch_size))
    print(json.dumps(summary, ensure_ascii=False))


def self_check():
    import numpy as np

    chunks = [{"chunk_id": "a/b#card", "dataset_id": "a/b", "text_hash": "h"}]
    manifest = {"chunk_ids": ["a/b#card"], "text_hashes": ["h"]}
    validate(manifest, chunks, np.zeros((1, DIMENSION), dtype=np.float16), {"a/b": {}})
    for bad in (np.zeros((2, DIMENSION)), np.zeros((1, 8))):
        try:
            validate(manifest, chunks, bad, {"a/b": {}})
            raise AssertionError("bad shape accepted")
        except SystemExit:
            pass
    try:
        validate(manifest, chunks, np.zeros((1, DIMENSION)), {})
        raise AssertionError("orphan chunk accepted")
    except SystemExit:
        pass
    sample = [{"text": "가" * 1000}]
    assert estimated_bytes(sample, {}) == int((3 * TEXT_PREVIEW_CHARS + CHUNK_OVERHEAD_BYTES) * STORAGE_FACTOR)
    print("20_sync_dataset_index ok")


if __name__ == "__main__":
    main()
