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
    python 20_sync_dataset_index.py --corpus v2 [--apply]   # the frozen v2 build into the *_v2 tables

--corpus v2 reads data/dataset_index_v2 + data/hypergraph_v2, refuses a build whose graph,
documents or vectors do not check out (corpus_manifest), writes only the *_v2 tables of
supabase_dataset_schema_v2.sql, and records the build's ids in model_scout_dataset_index_v2_meta.

    python 20_sync_dataset_index.py --corpus v2 --restore-vectors   # embeddings.npy from the v2 tables

embeddings.npy is not in git. --restore-vectors rebuilds it from the loaded v2 tables with no embedding
call: the DB build must be the pinned one, with the same model, every chunk's vector present, in the
local chunk order, and the result must hash to the recorded vectors_sha256, or nothing is written.
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
# Every folder and table a corpus reads or writes; SQL is built from these names only.
TARGETS = {
    "v1": {"index": INDEX_DIR, "graph": HYPERGRAPH_DIR, "schema": SCHEMA_SQL,
           "datasets": "model_scout_datasets", "chunks": "model_scout_dataset_chunks", "meta": None,
           "text_chars": TEXT_PREVIEW_CHARS, "match": "match_model_scout_datasets"},
    "v2": {"index": DATA_DIR / "dataset_index_v2", "graph": DATA_DIR / "hypergraph_v2",
           "schema": Path(__file__).with_name("supabase_dataset_schema_v2.sql"),
           "datasets": "model_scout_datasets_v2", "chunks": "model_scout_dataset_chunks_v2",
           "meta": "model_scout_dataset_index_v2_meta",
           "match": "match_model_scout_datasets_v2",
           "text_chars": None},  # whole chunk: conditions late in a card stay readable from the DB
}
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


def load_index(target=None):
    target = target or TARGETS["v1"]
    import numpy as np

    manifest = json.loads((target["index"] / "manifest.json").read_text(encoding="utf-8"))
    chunks = read_jsonl(target["index"] / "chunks.jsonl")
    vectors = np.load(target["index"] / "embeddings.npy")
    entities = {e["name"]: e for e in read_jsonl(target["graph"] / "entities.jsonl") if e["kind"] == "dataset"}
    concepts = defaultdict(list)
    for link in read_jsonl(target["graph"] / "links.jsonl"):
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


def estimated_bytes(chunks, entities, text_chars=TEXT_PREVIEW_CHARS):
    text = sum(len(c["text"][:text_chars].encode("utf-8")) for c in chunks)
    entity = sum(len(json.dumps(e, ensure_ascii=False).encode("utf-8")) for e in entities.values())
    raw = text + len(chunks) * CHUNK_OVERHEAD_BYTES + entity + len(entities) * DATASET_OVERHEAD_BYTES
    return int(raw * STORAGE_FACTOR)


def check_budget(cur, needed_bytes, target=None):
    target = target or TARGETS["v1"]
    """Projected DB size = today's size - the dataset tables we replace + what we will write."""
    cur.execute(f"""select pg_database_size(current_database()),
                          coalesce(pg_total_relation_size(to_regclass('public.{target["chunks"]}')), 0)
                        + coalesce(pg_total_relation_size(to_regclass('public.{target["datasets"]}')), 0)""")
    database, current = cur.fetchone()
    projected_mb = (database - current + needed_bytes) / 1e6
    budget_mb = float(os.getenv("SUPABASE_DB_BUDGET_MB", DEFAULT_BUDGET_MB))
    if projected_mb > budget_mb:
        raise SystemExit(
            f"projected database {projected_mb:.0f} MB > budget {budget_mb:.0f} MB; "
            "lower MAX_SECTION_CHUNKS (14) or FILE_CAP_PER_CATEGORY (18), or raise SUPABASE_DB_BUDGET_MB"
        )
    return round(projected_mb)


def apply(manifest, chunks, vectors, entities, concepts, batch_size, target=None, build=None):
    target = target or TARGETS["v1"]
    datasets_table, chunks_table = target["datasets"], target["chunks"]
    from psycopg2.extras import execute_values

    from supabase_db import db_connection, vector_literal

    conn = db_connection()
    try:
        with conn.cursor() as cur:
            projected_mb = check_budget(cur, estimated_bytes(chunks, entities, target["text_chars"]), target)
        conn.rollback()
        with conn, conn.cursor() as cur:
            cur.execute(target["schema"].read_text(encoding="utf-8"))

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
                    f"""
                    insert into public.{datasets_table}
                        (dataset_id, source, title, url, summary_ko, concepts, entity)
                    values %s
                    on conflict (dataset_id) do update set source = excluded.source, title = excluded.title,
                        url = excluded.url, summary_ko = excluded.summary_ko, concepts = excluded.concepts,
                        entity = excluded.entity, active = true, updated_at = now()
                    -- unchanged rows are skipped: a no-op update still writes a new tuple (bloat)
                    where ({datasets_table}.entity, {datasets_table}.concepts, {datasets_table}.active)
                          is distinct from (excluded.entity, excluded.concepts, true)""",
                    dataset_rows[start : start + batch_size],
                )

        with conn, conn.cursor() as cur:
            cur.execute(f"select chunk_id, text_hash from public.{chunks_table}")
            stored = dict(cur.fetchall())
        previous = None
        if target["meta"]:
            with conn, conn.cursor() as cur:
                cur.execute(f"select value from public.{target['meta']} where key = 'build'")
                found = cur.fetchone()
                previous = found[0] if found else None
        # A text hash cannot see a vector change (another model, or the same model run again), so a
        # different vector file than the last load re-uploads every vector.
        # ponytail: whole-table re-upload (~280 MB); store a per-row vector hash if loads become frequent.
        if previous and build and (previous.get("embedding_model"), previous.get("vectors_sha256")) != (
                build.get("embedding_model"), build.get("vectors_sha256")):
            changed = list(range(len(chunks)))
        else:
            changed = [i for i, c in enumerate(chunks) if stored.get(c["chunk_id"]) != c["text_hash"]]
        for start in range(0, len(changed), batch_size):
            rows = [
                (
                    chunks[i]["chunk_id"],
                    chunks[i]["dataset_id"],
                    chunks[i]["kind"],
                    chunks[i]["heading_path"],
                    chunks[i]["text"][: target["text_chars"]],
                    chunks[i]["text_hash"],
                    vector_literal(vectors[i]),
                )
                for i in changed[start : start + batch_size]
            ]
            with conn, conn.cursor() as cur:
                execute_values(
                    cur,
                    f"""
                    insert into public.{chunks_table}
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
                f"delete from public.{chunks_table} where not (chunk_id = any(%s))",
                ([c["chunk_id"] for c in chunks],),
            )
            removed_chunks = cur.rowcount
            cur.execute(f"delete from public.{datasets_table} where not (dataset_id = any(%s))", (list(entities),))
            removed_datasets = cur.rowcount
            if target["meta"] and build:
                cur.execute(
                    f"insert into public.{target['meta']} (key, value) values ('build', %s) "
                    "on conflict (key) do update set value = excluded.value, updated_at = now()",
                    (json.dumps(build, ensure_ascii=False),),
                )
        with conn.cursor() as cur:
            cur.execute(f"select count(*) from public.{chunks_table}")
            total = cur.fetchone()[0]
            cur.execute(
                f"select pg_size_pretty(pg_total_relation_size('public.{chunks_table}')), "
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
    # dataset-refresh.yml publishes v1; v2 goes to its own tables until the service is switched.
    parser.add_argument("--corpus", choices=sorted(TARGETS), default="v1")
    parser.add_argument("--restore-vectors", action="store_true", help="v2: rebuild embeddings.npy from the v2 tables")
    parser.add_argument("--restore-to", type=Path, help="with --restore-vectors: write here instead of the index folder")
    args = parser.parse_args()
    if args.self_check:
        return self_check()
    target = TARGETS[args.corpus]
    if args.restore_vectors:
        if not target["meta"]:
            raise SystemExit("--restore-vectors needs a corpus with a build record (v2)")
        return print(json.dumps(restore_vectors(target, args.restore_to), ensure_ascii=False))
    build = verified_build(target) if args.corpus != "v1" else None
    manifest, chunks, vectors, entities, concepts = load_index(target)
    validate(manifest, chunks, vectors, entities)
    summary = {
        "corpus": args.corpus,
        "tables": [target["datasets"], target["chunks"]],
        **({"documents_id": build["documents_id"][:16]} if build else {}),
        "datasets": len(entities),
        "chunks": len(chunks),
        "estimated_write_mb": round(estimated_bytes(chunks, entities, target["text_chars"]) / 1e6),
    }
    if args.apply:
        summary.update(apply(manifest, chunks, vectors, entities, concepts, args.batch_size, target, build))
        if build:
            summary["loaded_check"] = check_loaded(target, chunks, vectors, entities, build)
    print(json.dumps(summary, ensure_ascii=False))


def verified_build(target):
    """Ids of a build whose graph, documents and vectors check out; a mismatched build is never published."""
    from corpus_manifest import check_corpus, check_vectors, load_manifest

    import public_v2_pipeline

    problems = check_corpus(target["graph"], target["index"]) + check_vectors(target["index"])
    problems += public_v2_pipeline.verify_pin()
    if problems:
        raise SystemExit("v2 build does not check out (rebuild 13/14, then 14 --embed):\n- " + "\n- ".join(problems))
    graph, documents = load_manifest(target["graph"]), load_manifest(target["index"])
    pin = AI_DIR / "test" / "public_data" / "corpus_v2" / "data_version.json"
    vectors = json.loads((target["index"] / "manifest.json").read_text(encoding="utf-8"))["embedding_run"]
    return {
        "corpus_id": graph["stage_id"],
        "documents_id": documents["stage_id"],
        "data_version": json.loads(pin.read_text(encoding="utf-8"))["data_version"],
        "models": {k: graph["counts"].get(k) for k in ("model_source", "models", "model_ids_sha256")},
        "vectors_sha256": vectors["vectors_sha256"],
        "embedding_model": json.loads((target["index"] / "manifest.json").read_text(encoding="utf-8"))["model"],
        "text_chars": target["text_chars"],
    }


def restore_vectors(target, out=None):
    """Rebuild the frozen embeddings.npy from the loaded tables; refuse anything that is not that build."""
    import hashlib
    import tempfile

    import numpy as np

    import public_v2_pipeline
    from corpus_manifest import load_manifest
    from supabase_db import db_connection, parse_vector

    index = target["index"]
    record = json.loads((index / "manifest.json").read_text(encoding="utf-8"))  # the vector record, in git
    documents = load_manifest(index)
    problems = public_v2_pipeline.verify_pin()
    if record.get("documents_id") != documents["stage_id"]:
        problems.append("vector record is not for these documents")
    if problems:
        raise SystemExit("local v2 build is not the pinned one:\n- " + "\n- ".join(problems))
    conn = db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(f"select value from public.{target['meta']} where key = 'build'")
            found = cur.fetchone()
        build = found[0] if found else {}
        mismatch = [k for k, local in (("documents_id", documents["stage_id"]), ("embedding_model", record["model"]),
                                       ("vectors_sha256", record["embedding_run"]["vectors_sha256"]))
                    if build.get(k) != local]
        if mismatch:
            raise SystemExit(f"v2 tables hold another build ({', '.join(mismatch)} differ); restore from the kept copy instead")
        vectors = {}
        with conn.cursor(name="restore_vectors") as cur:  # server-side: ~41K rows of 1536 halves, streamed
            cur.itersize = 2000
            cur.execute(f"select chunk_id, embedding::text from public.{target['chunks']}")
            for chunk_id, text in cur:
                vectors[chunk_id] = parse_vector(text).astype(np.float16)
    finally:
        conn.close()
    missing = [c for c in record["chunk_ids"] if c not in vectors]
    if missing:  # never fill a gap with a new embedding
        raise SystemExit(f"{len(missing)} chunks have no vector in the v2 tables, e.g. {missing[:3]}")
    matrix = np.stack([vectors[c] for c in record["chunk_ids"]]).astype(np.float16)
    if matrix.shape != (record["rows"], record["dimension"]):
        raise SystemExit(f"restored shape {matrix.shape} != recorded ({record['rows']}, {record['dimension']})")
    out = Path(out) if out else index / "embeddings.npy"
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=out.parent, suffix=".npy", delete=False) as handle:
        tmp = Path(handle.name)
    np.save(tmp, matrix)
    digest = hashlib.sha256(tmp.read_bytes()).hexdigest()
    if digest != record["embedding_run"]["vectors_sha256"]:
        tmp.unlink()
        raise SystemExit(f"restored vectors hash {digest[:16]} != frozen {record['embedding_run']['vectors_sha256'][:16]}")
    tmp.replace(out)
    return {"restored": str(out), "rows": int(matrix.shape[0]), "vectors_sha256": digest[:16], "documents_id": documents["stage_id"][:16]}


TIE = 1e-4  # halfvec rounding: identical vectors may differ in the 4th decimal


def check_loaded(target, chunks, vectors, entities, build):
    """Read back what was written (ids, the stored text itself, the build record, one search) and compare.

    A failure leaves the committed batches in place: do not connect v2 to the service, fix, rerun.
    """
    from supabase_db import db_connection, vector_literal

    probe = chunks[0]
    conn = db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(f"select dataset_id from public.{target['datasets']}")
            datasets = {r[0] for r in cur.fetchall()}
            cur.execute(f"select chunk_id, text from public.{target['chunks']}")
            stored = dict(cur.fetchall())
            cur.execute(f"select value from public.{target['meta']} where key = 'build'")
            meta = cur.fetchone()[0]
            cur.execute(f"select dataset_id, similarity from public.{target['match']}(%s::halfvec) "
                        "order by similarity desc limit 20", (vector_literal(vectors[0]),))
            ranked = cur.fetchall()
    finally:
        conn.close()
    return compare_loaded(target, chunks, entities, build, datasets, stored, meta, ranked)


def compare_loaded(target, chunks, entities, build, datasets, stored, meta, ranked):
    expected = {c["chunk_id"]: c["text"][: target["text_chars"]] for c in chunks}
    probe = chunks[0]
    problems = []
    if datasets != set(entities):
        problems.append(f"datasets differ: missing {len(set(entities) - datasets)}, extra {len(datasets - set(entities))}")
    if set(stored) != set(expected):
        problems.append(f"chunk ids differ: missing {len(set(expected) - set(stored))}, extra {len(set(stored) - set(expected))}")
    wrong = [k for k, text in expected.items() if k in stored and stored[k] != text]
    if wrong:
        problems.append(f"{len(wrong)} stored texts differ from the local chunks, e.g. {wrong[:3]}")
    if (meta or {}).get("documents_id") != build["documents_id"]:
        problems.append("build record is not this build")
    # The probe's own dataset must score the top similarity; another dataset with the same text may tie.
    top = ranked[0][1] if ranked else None
    own = next((s for d, s in ranked if d == probe["dataset_id"]), None)
    if top is None or own is None or own < top - TIE:
        problems.append(f"search on {probe['chunk_id']}'s own vector: top {ranked[:3]}, own {own}")
    if problems:
        raise SystemExit("loaded v2 tables do not match the build:\n- " + "\n- ".join(problems))
    return {"datasets": len(datasets), "chunks": len(stored), "texts_compared": len(expected),
            "documents_id": meta["documents_id"][:16], "search_probe": [probe["dataset_id"], own, top]}


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
