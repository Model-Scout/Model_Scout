#!/usr/bin/env python3
"""운영 검색의 sparse 채널이 실제로 동작하는지 잰다(읽기 전용).

match_model_scout_models 는 아래처럼 점수를 낸다.

    dense_similarity = 1 - (embedding <=> query_embedding)
    sparse_score     = least(1.0, ts_rank_cd(search_tsv, plainto_tsquery('simple', query_text)))
    similarity       = dense_weight * dense_similarity + sparse_weight * sparse_score

plainto_tsquery 는 모든 단어를 AND 로 묶는다. search_tsv 는 영어 메타데이터로만
만들어진 생성 컬럼이라 한국어 토큰이 거의 없고, 질의에 한국어가 하나라도 섞이면
AND 가 통째로 실패해 sparse_score 가 전 행 0 이 된다.

    python test/model_retrieval/tools/diagnose_sparse.py

임베딩(OpenAI) 호출 없이 sparse 만 본다. --with-dense 를 주면 dense 범위도 잰다.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List

AI = Path(__file__).resolve().parents[3]

# 서비스가 실제로 만드는 질의 형식. 17_recommend_graph.DECOMPOSE_PROMPT 가
# "model_query: Korean and English keywords mixed" 로 지시한다.
PROBES = [
    ("순수 한국어", "한국어 문서 검색에 쓸 문장 임베딩 모델"),
    ("혼합(그래프 예시)", "한국어 문서 임베딩 embedding retrieval"),
    ("혼합(음성인식)", "한국어 음성 인식 korean speech recognition ASR"),
    ("혼합(번역)", "한영 번역 korean english translation"),
    ("순수 영어", "korean sentence embedding model for document retrieval"),
]


def connect():
    from dotenv import load_dotenv
    import psycopg2

    load_dotenv(AI / ".env")
    load_dotenv(AI.parent / ".env")
    conn = psycopg2.connect(
        host=os.environ["SUPABASE_DB_HOST"], port=int(os.environ["SUPABASE_DB_PORT"]),
        dbname=os.environ["SUPABASE_DB_NAME"], user=os.environ["SUPABASE_DB_USER"],
        password=os.environ["SUPABASE_PASSWORD"], sslmode="require", connect_timeout=20,
        options="-c statement_timeout=180000",
    )
    # 시작 옵션의 default_transaction_read_only 는 Supabase 풀러가 버린다(PR #56 에서 확인됨).
    # 세션 단위로 걸어야 서버가 실제로 쓰기를 거부한다. supabase_db.db_connection 과 같은 방식이다.
    conn.set_session(readonly=True)
    with conn.cursor() as cur:            # 실제로 읽기 전용인지 확인하고 아니면 멈춘다
        cur.execute("show transaction_read_only")
        if cur.fetchone()[0] != "on":
            conn.close()
            raise SystemExit("읽기 전용 세션을 확인하지 못해 중단한다")
    return conn


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--with-dense", action="store_true", help="dense 범위도 잰다(OpenAI 임베딩 1회)")
    ap.add_argument("--json", type=Path, help="결과를 JSON 으로도 저장")
    args = ap.parse_args()

    conn = connect()
    out: Dict[str, Any] = {"probes": []}
    try:
        cur = conn.cursor()
        cur.execute("select count(*) from public.model_scout_models where active")
        total = cur.fetchone()[0]
        out["active_rows"] = total
        print(f"운영 코퍼스 active {total}행\n")

        print(f"{'질의 형태':22s} {'plainto 매칭':>12s} {'sparse 최대':>11s} {'OR 매칭':>9s} {'OR 최대':>9s}")
        print("-" * 72)
        for name, query in PROBES:
            cur.execute(
                "select count(*), coalesce(max(least(1.0, ts_rank_cd(search_tsv,"
                " plainto_tsquery('simple', %s)))), 0)::real"
                " from public.model_scout_models"
                " where active and search_tsv @@ plainto_tsquery('simple', %s)",
                (query, query))
            and_rows, and_max = cur.fetchone()
            or_query = " | ".join(t for t in query.replace(",", " ").split() if t)
            cur.execute(
                "select count(*), coalesce(max(least(1.0, ts_rank_cd(search_tsv,"
                " to_tsquery('simple', %s)))), 0)::real"
                " from public.model_scout_models"
                " where active and search_tsv @@ to_tsquery('simple', %s)",
                (or_query, or_query))
            or_rows, or_max = cur.fetchone()
            print(f"{name:22s} {and_rows:>12d} {and_max:>11.4f} {or_rows:>9d} {or_max:>9.4f}")
            out["probes"].append({"name": name, "query": query,
                                  "and_rows": and_rows, "and_max": round(float(and_max), 6),
                                  "or_rows": or_rows, "or_max": round(float(or_max), 6)})

        cur.execute("select plainto_tsquery('simple', %s)::text", (PROBES[1][1],))
        print(f"\nplainto_tsquery('{PROBES[1][1]}')\n  → {cur.fetchone()[0]}")
        print("  AND 로 묶이므로 한국어 토큰 하나가 전체를 무효화한다.")

        print("\nsearch_tsv 의 토큰 분포 (영어 vs 한국어)")
        for term in ("korean", "한국어", "embedding", "임베딩", "translation", "번역"):
            cur.execute("select count(*) from public.model_scout_models"
                        " where active and search_tsv @@ plainto_tsquery('simple', %s)", (term,))
            n = cur.fetchone()[0]
            print(f"  {term:12s} {n:>5d}행 ({n / total * 100:5.1f}%)")
            out.setdefault("term_coverage", {})[term] = n

        if args.with_dense:
            from openai import OpenAI
            query = PROBES[0][1]
            vec = OpenAI(timeout=40).embeddings.create(
                model="text-embedding-3-small", input=[query]).data[0].embedding
            cur.execute("select min(d), max(d), avg(d) from (select"
                        " (1-(embedding <=> %s::halfvec(1536)))::real d"
                        " from public.model_scout_models where active) t", (str(vec),))
            lo, hi, avg = cur.fetchone()
            print(f"\ndense ({query})\n  min {lo:.4f}  max {hi:.4f}  평균 {avg:.4f}")
            print(f"  0.65 × dense 기여: {0.65*lo:.4f} ~ {0.65*hi:.4f}")
            print(f"  0.35 × sparse 기여: 0.0000 ~ 0.0000   ← sparse 가 0 이므로")
            out["dense"] = {"query": query, "min": round(float(lo), 6),
                            "max": round(float(hi), 6), "avg": round(float(avg), 6)}
    finally:
        conn.rollback()
        conn.close()

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\n→ {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
