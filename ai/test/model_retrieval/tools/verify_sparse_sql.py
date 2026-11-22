#!/usr/bin/env python3
"""마이그레이션의 sparse 식이 측정과 같은 값을 내는지 대조한다. 쓰기는 하지 않는다.

supabase_migration_sparse_idf.sql 은 df 표를 만들지만, 적용은 사람이 한다. 적용
전에 식이 맞는지 확인해야 하므로, 표 대신 df 를 인자로 넘기는 같은 모양의 질의를
읽기 전용으로 돌려 sparse_idf.py 가 파이썬에서 낸 값과 비교한다.

둘이 소수점 아래까지 같으면, 표를 채웠을 때 측정과 같은 순위가 나온다는 뜻이다.

    python test/model_retrieval/tools/verify_sparse_sql.py
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

AI = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# 마이그레이션의 CTE 와 같은 모양. df 표 조회만 unnest 로 바꿨다.
SQL = """
with query_terms as (
    select distinct u.lexeme as term
    from unnest(to_tsvector('simple', coalesce(%(q)s, ''))) as u
),
df as (
    select t.term, t.df
    from unnest(%(terms)s::text[], %(dfs)s::integer[]) as t(term, df)
),
query_idf as (
    select
        qt.term,
        ln(1 + ((select count(*) from public.model_scout_models where active = true)::numeric
                - d.df + 0.5) / (d.df + 0.5)) as idf
    from query_terms as qt
    join df as d on d.term = qt.term
    where d.df > 0
),
query_idf_total as (select sum(idf) as total_idf from query_idf),
sparse_hit as (
    select hits.model_id, sum(query_idf.idf) as matched_idf
    from query_idf
    join public.model_scout_models as hits
      on hits.active = true
     and hits.search_tsv @@ plainto_tsquery('simple', query_idf.term)
    group by hits.model_id
)
select
    m.model_id,
    case
        when (select total_idf from query_idf_total) is null then least(
            1.0, ts_rank_cd(m.search_tsv, plainto_tsquery('simple', coalesce(%(q)s, '')))::real
        )::real
        else (coalesce(sh.matched_idf, 0) / (select total_idf from query_idf_total))::real
    end as sparse_score
from public.model_scout_models as m
left join sparse_hit as sh on sh.model_id = m.model_id
where m.active = true and sh.matched_idf is not null
"""


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--queries", type=int, default=12)
    ap.add_argument("--tolerance", type=float, default=1e-6)
    args = ap.parse_args()

    ev = _load("ev", HERE / "evaluator.py")
    import sparse_idf

    items = ev.load_queries(None)
    texts = [i["model_query"] for i in items]
    index = sparse_idf.load(None, texts)          # 캐시에서 읽는다(DB 불필요)
    terms = sorted(index.df)
    dfs = [index.df[t] for t in terms]

    conn = ev.connect()
    checked = same = 0
    worst = 0.0
    try:
        with conn.cursor() as cur:
            for text in list(dict.fromkeys(texts))[:args.queries]:
                cur.execute(SQL, {"q": text, "terms": terms, "dfs": dfs})
                from_sql = {model_id: float(score) for model_id, score in cur.fetchall()}
                from_py = index.scores(text, "idf", from_sql.keys())
                checked += 1
                gaps = [abs(from_sql[m] - from_py.get(m, 0.0)) for m in from_sql]
                gap = max(gaps) if gaps else 0.0
                worst = max(worst, gap)
                missing = set(from_py) - set(from_sql)
                if gap <= args.tolerance and not missing:
                    same += 1
                else:
                    print(f"  ❌ {text[:46]}")
                    print(f"     최대 차이 {gap:.2e} · SQL 에 없는 행 {len(missing)}개 "
                          f"(SQL {len(from_sql)} / 파이썬 {len(from_py)})")
    finally:
        conn.rollback()
        conn.close()

    print(f"질의 {checked}개 대조 · 일치 {same}개 · 최대 차이 {worst:.2e}")
    if same != checked:
        print("\n식이 다르다. 마이그레이션을 적용하면 측정과 다른 순위가 나온다.")
        return 1
    print("\n마이그레이션의 sparse 식이 측정과 같은 값을 낸다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
