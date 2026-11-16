#!/usr/bin/env python3
"""최신 completed reingest 의 active 모델 전체를 골든셋 v3 기준 코퍼스로 덤프한다.

Supabase 는 읽기 전용 트랜잭션으로만 연다. embedding 벡터는 담지 않는다(판정에
dense 채널을 쓰지 않는다). README 근거는 ``model_scout_evidence.parents`` 를
``evidence_spans`` 로 같이 담는다.

    python test/golden/v3/tools/dump_corpus.py            # 메타가 없을 때 처음 고정
    python test/golden/v3/tools/dump_corpus.py --restore  # 커밋된 메타와 같은 스냅샷 복구
    python test/golden/v3/tools/dump_corpus.py --check    # 로컬 스냅샷이 메타와 같은지만 검사

``--restore`` 는 DB 의 최신 reingest run 이 메타의 sync_run_id 와 다르거나, 덤프한
파일의 SHA256 이 메타와 다르면 실패한다. 그 경우 기준 코퍼스가 바뀐 것이므로
골든셋 전체를 다시 만들어야 한다.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus  # noqa: E402

ENV_NAMES = ("SUPABASE_DB_HOST", "SUPABASE_DB_PORT", "SUPABASE_DB_NAME", "SUPABASE_DB_USER", "SUPABASE_PASSWORD")
MODEL_COLUMNS = (
    "model_id", "source_pool", "source_stage1_version", "source_stage2_version",
    "source_stage3_version", "source_stage4_version", "candidate", "task", "language",
    "popularity", "family", "filter_metadata", "technical_metadata", "semantic_metadata",
    "evidence", "benchmark_metadata", "source_provenance", "task_consistency",
    "document_hash", "embedding_model", "embedding_dimensions", "active",
)
RUN_SQL = """
select run_id::text, completed_at, stage_versions, row_count
from public.model_scout_sync_runs
where status = 'completed' and stage_versions->>'sync_mode' = 'reingest'
order by completed_at desc limit 1
"""


def connect():
    from dotenv import load_dotenv

    load_dotenv(corpus.AI_ROOT / ".env")
    load_dotenv(corpus.AI_ROOT.parent / ".env")
    missing = [name for name in ENV_NAMES if not os.getenv(name)]
    if missing:
        raise SystemExit("Supabase 접속 정보 없음. 필요한 환경변수: " + ", ".join(missing))
    import psycopg2

    conn = psycopg2.connect(
        host=os.environ["SUPABASE_DB_HOST"], port=int(os.environ["SUPABASE_DB_PORT"]),
        dbname=os.environ["SUPABASE_DB_NAME"], user=os.environ["SUPABASE_DB_USER"],
        password=os.environ["SUPABASE_PASSWORD"], sslmode="require", connect_timeout=15,
        options="-c default_transaction_read_only=on -c statement_timeout=300000",
    )
    conn.set_session(readonly=True, autocommit=False)
    with conn.cursor() as cur:
        cur.execute("show transaction_read_only")
        if cur.fetchone()[0] != "on":
            conn.close()
            raise SystemExit("read-only 트랜잭션을 확인하지 못해 중단한다")
    return conn


def dump(snapshot: Path, expected_run: str | None) -> dict:
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute(RUN_SQL)
            found = cur.fetchone()
            if not found:
                raise SystemExit("completed reingest run 이 없다")
            run_id, completed_at, stage_versions, row_count = found
            if expected_run and run_id != expected_run:
                raise SystemExit(f"DB 최신 reingest run {run_id} ≠ 메타 {expected_run}. 기준 코퍼스가 바뀌었다")
            cur.execute(
                f"select {', '.join('m.' + c for c in MODEL_COLUMNS)}, m.last_seen_run::text, "
                "m.refreshed_at from public.model_scout_models as m where m.active order by m.model_id")
            names = (*MODEL_COLUMNS, "last_seen_run", "refreshed_at")
            rows = [dict(zip(names, record)) for record in cur.fetchall()]
            cur.execute("select model_id, parents, parent_count, child_count, source_stage3_hash "
                        "from public.model_scout_evidence where active")
            spans = {mid: {"parents": parents, "parent_count": pc, "child_count": cc, "source_stage3_hash": h}
                     for mid, parents, pc, cc, h in cur.fetchall()}
    finally:
        conn.rollback()
        conn.close()

    stray = sorted({r["last_seen_run"] for r in rows} - {run_id})
    if stray:
        raise SystemExit(f"active 행 중 기준 reingest 이후 run 이 쓴 행이 있다: {stray[:3]}. 기준을 다시 정한다")
    if row_count != len(rows):
        raise SystemExit(f"run row_count {row_count} ≠ active {len(rows)}")
    missing = [r["model_id"] for r in rows if r["model_id"] not in spans]
    for row in rows:
        row["evidence_spans"] = spans.get(row["model_id"])
    tmp = snapshot.with_suffix(".jsonl.tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(corpus.canonical_line(row) + "\n")
    tmp.replace(snapshot)

    refreshed = sorted(str(r["refreshed_at"]) for r in rows)
    pools: dict = {}
    for r in rows:
        pools[r["source_pool"]] = pools.get(r["source_pool"], 0) + 1
    return {
        "source": "supabase (read-only): public.model_scout_models active + public.model_scout_evidence active",
        "corpus_schema_version": corpus.CORPUS_SCHEMA_VERSION,
        "sync_run_id": run_id,
        "sync_mode": stage_versions.get("sync_mode"),
        "stage1_mode": stage_versions.get("stage1_mode"),
        "sync_completed_at": str(completed_at),
        "stage_versions": {k: stage_versions.get(k) for k in ("stage1", "stage2", "stage3", "stage4")},
        "approved_dry_run_id": stage_versions.get("approved_dry_run_id"),
        "active_row_count": len(rows),
        "pool_counts": dict(sorted(pools.items())),
        "model_ids_sha256": corpus.model_ids_sha256(r["model_id"] for r in rows),
        "snapshot_file": corpus.SNAPSHOT.name,
        "snapshot_sha256": corpus.file_sha256(snapshot),
        "snapshot_bytes": snapshot.stat().st_size,
        "snapshot_created_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "refreshed_at_min": refreshed[0] if refreshed else None,
        "refreshed_at_max": refreshed[-1] if refreshed else None,
        "evidence_rows": len(spans),
        "models_without_evidence": missing,
        "columns": [*MODEL_COLUMNS, "last_seen_run", "refreshed_at", "evidence_spans"],
        "excluded": "embedding 벡터(판정에 dense 채널을 쓰지 않는다)",
        "restore": "python test/golden/v3/tools/dump_corpus.py --restore",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--restore", action="store_true", help="커밋된 메타와 같은 스냅샷을 다시 받는다")
    mode.add_argument("--check", action="store_true", help="로컬 스냅샷이 메타와 같은지만 본다")
    args = parser.parse_args()

    if args.check:
        rows = corpus.load_corpus()
        print(f"✅ 일치: {len(rows):,}행, sync_run_id={corpus.load_meta()['sync_run_id']}")
        return 0
    if args.restore:
        meta = corpus.load_meta()
        fresh = dump(corpus.SNAPSHOT, meta["sync_run_id"])
        if fresh["snapshot_sha256"] != meta["snapshot_sha256"]:
            raise SystemExit("복구한 스냅샷 SHA256 이 메타와 다르다. 같은 run 이지만 행 내용이 바뀌었다")
        corpus.load_corpus()
        print(f"✅ 복구: {fresh['active_row_count']:,}행, SHA256 일치")
        return 0
    if corpus.META.exists():
        raise SystemExit(f"{corpus.META} 가 이미 있다. 같은 코퍼스는 --restore, 기준을 바꾸려면 메타를 지우고 다시 만든다")
    meta = dump(corpus.SNAPSHOT, None)
    corpus.META.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in meta.items() if k != "models_without_evidence"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
