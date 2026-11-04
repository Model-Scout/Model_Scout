#!/usr/bin/env python3
"""Supabase의 확정 코퍼스를 골든셋 v2의 판정 기준 파일로 덤프한다.

GitHub Actions를 멈춘 시점의 ``model_scout_models`` active 행이 최종 후보
집합이다. 이 스냅샷을 파일로 고정해 두면 판정 중에 기준이 흔들리지 않고,
팀원이 같은 파일로 같은 숫자를 볼 수 있다.

OpenAI 임베딩 벡터는 담지 않는다. 판정은 메타데이터와 claim, evidence로만
하고 dense 채널은 쓰지 않으므로 1536차원 × 3,872행을 복사할 이유가 없다.

    python test/golden/v2/tools/dump_corpus.py          # 덤프
    python test/golden/v2/tools/dump_corpus.py --check  # 기존 덤프 검증만
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # ai/
V2 = Path(__file__).resolve().parents[1]
SNAPSHOT = V2 / "corpus_snapshot.jsonl"
META = V2 / "corpus_snapshot.meta.json"

# 05_validate_retrieval.hard_filter와 retrieval_lab이 읽는 필드만 옮긴다.
COLUMNS = (
    "model_id",
    "source_pool",
    "source_stage1_version",
    "source_stage2_version",
    "source_stage3_version",
    "source_stage4_version",
    "candidate",
    "task",
    "language",
    "popularity",
    "family",
    "filter_metadata",
    "technical_metadata",
    "semantic_metadata",
    "evidence",
    "benchmark_metadata",
    "source_provenance",
    "task_consistency",
    "document_hash",
    "embedding_model",
    "embedding_dimensions",
)


def connect():
    sys.path.insert(0, str(ROOT))
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")
    load_dotenv(ROOT.parent / ".env")
    import supabase_db

    if not supabase_db.configured():
        raise SystemExit("Supabase 접속 정보가 없습니다. ai/.env를 확인하세요.")
    return supabase_db.db_connection()


def dump() -> None:
    with connect() as conn:
        cur = conn.cursor()
        cur.execute(
            f"select {', '.join(COLUMNS)} from public.model_scout_models "
            "where active order by source_pool, model_id"
        )
        rows = [dict(zip(COLUMNS, record)) for record in cur.fetchall()]

        cur.execute(
            "select model_id, parents, parent_count, child_count "
            "from public.model_scout_evidence where active"
        )
        spans = {
            model_id: {"parents": parents, "parent_count": pc, "child_count": cc}
            for model_id, parents, pc, cc in cur.fetchall()
        }

        cur.execute(
            "select run_id, started_at, stage_versions, row_count "
            "from public.model_scout_sync_runs where status = 'completed' "
            "order by started_at desc limit 1"
        )
        run_id, started_at, stage_versions, row_count = cur.fetchone()

        cur.execute("select max(refreshed_at) from public.model_scout_models where active")
        refreshed_at = cur.fetchone()[0]

    # evidence는 README 원문 span이다. 규칙 스캔 5단계의 최후 근거이므로 같이 담는다.
    missing_evidence = []
    with SNAPSHOT.open("w", encoding="utf-8") as handle:
        for row in rows:
            span = spans.get(row["model_id"])
            if span is None:
                missing_evidence.append(row["model_id"])
            row["evidence_spans"] = span
            handle.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")

    pools: dict[str, int] = {}
    for row in rows:
        pools[row["source_pool"]] = pools.get(row["source_pool"], 0) + 1

    meta = {
        "source": "supabase.public.model_scout_models",
        "filter": "active = true",
        "rows": len(rows),
        "pool_counts": pools,
        "evidence_rows": len(spans),
        "models_without_evidence": missing_evidence,
        "last_sync_run_id": str(run_id),
        "last_sync_started_at": str(started_at),
        "last_sync_stage_versions": stage_versions,
        "last_sync_row_count": row_count,
        "corpus_refreshed_at": str(refreshed_at),
        "github_actions": "disabled (팀 결정). 이 스냅샷이 확정 후보 집합이다.",
        "note": "OpenAI 임베딩 벡터는 제외. 판정은 메타데이터/claim/evidence로만 한다.",
    }
    META.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({k: v for k, v in meta.items() if k != "models_without_evidence"},
                     ensure_ascii=False, indent=2))
    if missing_evidence:
        print(f"\n⚠️ evidence 없는 모델 {len(missing_evidence)}개: {missing_evidence[:10]}")


def check() -> None:
    if not SNAPSHOT.exists():
        raise SystemExit(f"{SNAPSHOT} 없음. 먼저 덤프하세요.")
    meta = json.loads(META.read_text(encoding="utf-8"))
    count = 0
    pools: dict[str, int] = {}
    no_filter = []
    with SNAPSHOT.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            count += 1
            pools[row["source_pool"]] = pools.get(row["source_pool"], 0) + 1
            if not row.get("filter_metadata"):
                no_filter.append(row["model_id"])
    print(f"행 수            {count}  (메타 기록: {meta['rows']})")
    print(f"pool별           {pools}  (메타 기록: {meta['pool_counts']})")
    print(f"filter_metadata 없음  {len(no_filter)}")
    print(f"기준 시각        {meta['corpus_refreshed_at']}")
    ok = count == meta["rows"] and pools == meta["pool_counts"] and not no_filter
    print("\n" + ("✅ 일치" if ok else "❌ 불일치"))
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="덤프하지 않고 기존 파일만 검증")
    args = parser.parse_args()
    check() if args.check else dump()
