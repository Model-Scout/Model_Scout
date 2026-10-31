"""Stage D5: publish the dataset index (cards, chunks, vectors) to Supabase pgvector.

Reads data/dataset_index (14) and data/hypergraph (13) and mirrors them into
public.model_scout_datasets / public.model_scout_dataset_chunks (supabase_dataset_schema.sql).
The local index is the source of truth and the tables are derived from it: only chunks whose
text hash changed are uploaded, and datasets or chunks that left the index are deleted.
Everything runs in one transaction, so a failed sync leaves the previous index intact.

    python 20_sync_dataset_index.py            # offline validation and size estimate
    python 20_sync_dataset_index.py --apply    # write Supabase
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

DATA_DIR = Path("data")
INDEX_DIR = DATA_DIR / "dataset_index"
HYPERGRAPH_DIR = DATA_DIR / "hypergraph"
SCHEMA_SQL = Path(__file__).with_name("supabase_dataset_schema.sql")
DIMENSION = 1536
# Rough Postgres bytes per chunk row: halfvec (2 B x 1536) + text + overhead.
BYTES_PER_CHUNK = 2 * DIMENSION + 1200


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
        problems.append(f"{len(orphans)} chunk datasets missing from the hypergraph, e.g. {sorted(orphans)[:3]}; run 13 then 14")
    if problems:
        raise SystemExit("dataset index validation failed:\n- " + "\n- ".join(problems))


def apply(manifest, chunks, vectors, entities, concepts, batch_size):
    from psycopg2.extras import execute_values

    from supabase_db import db_connection, vector_literal

    conn = db_connection()
    try:
        with conn, conn.cursor() as cur:  # one transaction
            cur.execute(SCHEMA_SQL.read_text(encoding="utf-8"))
            dataset_rows = [(name, e["source"], e.get("title"), e["url"], e.get("summary_ko"), sorted(concepts[name]),
                             json.dumps(e, ensure_ascii=False)) for name, e in entities.items()]
            for start in range(0, len(dataset_rows), batch_size):
                execute_values(cur, """
                    insert into public.model_scout_datasets
                        (dataset_id, source, title, url, summary_ko, concepts, entity)
                    values %s
                    on conflict (dataset_id) do update set source = excluded.source, title = excluded.title,
                        url = excluded.url, summary_ko = excluded.summary_ko, concepts = excluded.concepts,
                        entity = excluded.entity, active = true, updated_at = now()""",
                    dataset_rows[start:start + batch_size])
            cur.execute("delete from public.model_scout_datasets where not (dataset_id = any(%s))", (list(entities),))
            removed_datasets = cur.rowcount

            cur.execute("select chunk_id, text_hash from public.model_scout_dataset_chunks")
            stored = dict(cur.fetchall())
            changed = [i for i, c in enumerate(chunks) if stored.get(c["chunk_id"]) != c["text_hash"]]
            for start in range(0, len(changed), batch_size):
                rows = [(chunks[i]["chunk_id"], chunks[i]["dataset_id"], chunks[i]["kind"], chunks[i]["heading_path"],
                         chunks[i]["text"], chunks[i]["text_hash"], vector_literal(vectors[i]))
                        for i in changed[start:start + batch_size]]
                execute_values(cur, """
                    insert into public.model_scout_dataset_chunks
                        (chunk_id, dataset_id, kind, heading_path, text, text_hash, embedding)
                    values %s
                    on conflict (chunk_id) do update set dataset_id = excluded.dataset_id, kind = excluded.kind,
                        heading_path = excluded.heading_path, text = excluded.text, text_hash = excluded.text_hash,
                        embedding = excluded.embedding, updated_at = now()""",
                    rows, template="(%s, %s, %s, %s, %s, %s, %s::halfvec)")
                print(f"[SYNC] chunks {min(start + batch_size, len(changed))}/{len(changed)}", flush=True)
            cur.execute("delete from public.model_scout_dataset_chunks where not (chunk_id = any(%s))",
                        ([c["chunk_id"] for c in chunks],))
            removed_chunks = cur.rowcount
        with conn.cursor() as cur:
            cur.execute("select count(*) from public.model_scout_dataset_chunks")
            total = cur.fetchone()[0]
            cur.execute("select pg_size_pretty(pg_total_relation_size('public.model_scout_dataset_chunks')), "
                        "pg_size_pretty(pg_database_size(current_database()))")
            table_size, db_size = cur.fetchone()
    finally:
        conn.close()
    return {"datasets": len(dataset_rows), "removed_datasets": removed_datasets, "uploaded_chunks": len(changed),
            "removed_chunks": removed_chunks, "chunks_in_db": total, "chunks_table": table_size, "database": db_size}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--apply", action="store_true", help="write Supabase")
    parser.add_argument("--batch-size", type=int, default=200)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        return self_check()
    manifest, chunks, vectors, entities, concepts = load_index()
    validate(manifest, chunks, vectors, entities)
    summary = {"datasets": len(entities), "chunks": len(chunks),
               "estimated_table_mb": round(len(chunks) * BYTES_PER_CHUNK / 1e6)}
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
    print("20_sync_dataset_index ok")


if __name__ == "__main__":
    main()
