#!/usr/bin/env python3
"""운영 검색과 같은 수식으로 점수를 내고, 가중치는 오프라인에서 쓸어본다.

운영(match_model_scout_models)은 이렇게 점수를 낸다.

    dense_similarity = 1 - (embedding <=> query_embedding)        text-embedding-3-small
    sparse_score     = least(1.0, ts_rank_cd(search_tsv, plainto_tsquery('simple', query_text)))
    similarity       = dense_weight * dense + sparse_weight * sparse

여기서는 질의마다 (model_id, dense, sparse) 를 한 번만 받아 두고, 가중치는
재질의 없이 전부 계산한다. 같은 수식이므로 결과가 운영과 1:1 로 맞는다
(--compare-rpc 로 RPC 와 상위 20개가 같은지 확인한다).

sparse 계산 방식도 바꿔 볼 수 있다. 운영의 plainto(AND)는 한국어가 섞이면
전 행 0이 되므로, 고쳤을 때의 효과를 같은 자리에서 비교하려는 것이다.

    python test/model_retrieval/tools/evaluator.py --types benchmark_lookup --sparse plainto
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

AI = Path(__file__).resolve().parents[3]
QUERIES = AI / "test" / "model_retrieval" / "queries"
CACHE_DIR = AI / "test" / "model_retrieval" / "cache"
sys.path.insert(0, str(Path(__file__).resolve().parent))

SPECS = {"benchmark_lookup": "spec_benchmark.py", "structured_constraint": "spec_structured.py",
         "lexical_exact": "spec_lexical.py", "model_comparison": "spec_comparison.py",
         "semantic_capability": "spec_capability.py", "semantic_constraint": "spec_constraint.py"}
EMBED_MODEL = "text-embedding-3-small"
DENSE_DEPTH = 300   # dense 상위 N. sparse>0 인 행은 전부 더하므로 어떤 가중치에서도 상위 10은 이 안에 있다

# sparse 계산 방식
#   A plainto  운영 그대로. 모든 단어를 AND → 한국어가 섞이면 전 행 0
#   B or       단순 OR + ts_rank_cd. 4017행 100%에 있는 토큰이 순위를 오염시킨다
#   C idf      IDF 가중 매칭 비율. 코퍼스에 없는 질의어는 분모에서 뺀다 (sparse_idf.py)
#   C' idf_all 같은 식이지만 df=0 질의어도 분모에 넣는다 → 한국어 많은 질의가 눌린다
SPARSE_SQL = {
    "plainto": "least(1.0, ts_rank_cd(m.search_tsv, plainto_tsquery('simple', %(q)s)))::real",
    "or": "least(1.0, ts_rank_cd(m.search_tsv, to_tsquery('simple', %(orq)s)))::real",
}
SPARSE_IDF = ("idf", "idf_all")
SPARSE_MODES = tuple(SPARSE_SQL) + SPARSE_IDF


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
    # 시작 옵션의 default_transaction_read_only 는 Supabase 풀러가 버린다(PR #56).
    conn.set_session(readonly=True)
    with conn.cursor() as cur:
        cur.execute("show transaction_read_only")
        if cur.fetchone()[0] != "on":
            conn.close()
            raise SystemExit("읽기 전용 세션을 확인하지 못해 중단한다")
    return conn


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def embed(texts: Sequence[str]) -> Dict[str, List[float]]:
    """질의 임베딩. 디스크에 캐시해 같은 질의는 한 번만 부른다."""
    from dotenv import load_dotenv
    from openai import OpenAI

    load_dotenv(AI / ".env")
    load_dotenv(AI.parent / ".env")

    out: Dict[str, List[float]] = {}
    todo = []
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    for text in texts:
        key = hashlib.sha256(f"{EMBED_MODEL}|{text}".encode()).hexdigest()[:20]
        path = CACHE_DIR / f"emb_{key}.json"
        if path.exists():
            out[text] = json.loads(path.read_text())
        else:
            todo.append((text, path))
    if todo:
        client = OpenAI(timeout=60, max_retries=3)
        for start in range(0, len(todo), 64):
            chunk = todo[start:start + 64]
            got = client.embeddings.create(model=EMBED_MODEL, input=[t for t, _ in chunk])
            for (text, path), item in zip(chunk, got.data):
                out[text] = list(item.embedding)
                path.write_text(json.dumps(out[text]))
            print(f"  임베딩 {min(start + 64, len(todo))}/{len(todo)}", flush=True)
    return out


# 하드 필터 WHERE 절. match_model_scout_models 와 같은 의미여야 한다.
FILTER_SQL = [
    ("tasks", "(m.task->>'primary' = any(%(tasks)s) or exists (select 1 from "
              "jsonb_array_elements_text(coalesce(m.task->'matched','[]'::jsonb)) t where t = any(%(tasks)s)))"),
    ("korean_required", "m.filter_metadata->>'korean_verified' = 'true'"),
    ("max_parameters_billion", "(m.filter_metadata->>'parameter_count_billion')::numeric <= %(max_parameters_billion)s"),
    ("min_parameters_billion", "(m.filter_metadata->>'parameter_count_billion')::numeric >= %(min_parameters_billion)s"),
    ("min_context_length", "(m.filter_metadata->>'context_length')::numeric >= %(min_context_length)s"),
    ("max_context_length", "(m.filter_metadata->>'context_length')::numeric <= %(max_context_length)s"),
    ("popularity_tier", "m.filter_metadata->>'popularity_tier' = %(popularity_tier)s"),
    ("commercial_status", "m.filter_metadata->>'commercial_status' = any(%(commercial_status)s)"),
    ("require_artifact", "(select count(*) from unnest(%(require_artifact)s::text[]) w(name) where exists "
                         "(select 1 from jsonb_array_elements_text(coalesce(m.filter_metadata->'artifact_formats',"
                         "'[]'::jsonb)) p where p.value = w.name)) = cardinality(%(require_artifact)s::text[])"),
    ("max_artifact_gib", "coalesce((m.filter_metadata->>'artifact_runnable_bytes')::numeric,"
                         "(m.filter_metadata->>'artifact_runnable_gib')::numeric * 1073741824) > 0 and "
                         "coalesce((m.filter_metadata->>'artifact_runnable_bytes')::numeric,"
                         "(m.filter_metadata->>'artifact_runnable_gib')::numeric * 1073741824) "
                         "<= (%(max_artifact_gib)s::numeric) * 1073741824"),
    ("exclude_gated", "m.filter_metadata->>'gated' = 'false'"),
]


def score_one(cur, text: str, vector: List[float], conditions: Dict[str, Any],
              sparse_mode: str, index=None) -> List[Tuple[str, float, float]]:
    """(model_id, dense, sparse) — dense 상위 DENSE_DEPTH + sparse>0 인 행 전부.

    어떤 가중치에서도 상위 10 은 이 둘의 합집합 안에 있다. sparse 가 0 인 행이
    dense 상위 300 밖이면, 그 행을 올려 줄 성분이 아무것도 없기 때문이다.
    """
    where = ["m.active"]
    params: Dict[str, Any] = {"vec": str(vector), "q": text,
                              "orq": " | ".join(re.findall(r"[\w.+#-]+", text)) or "x"}
    for key, clause in FILTER_SQL:
        value = conditions.get(key)
        if value in (None, [], False):
            continue
        where.append(clause)
        params[key] = list(value) if isinstance(value, (list, tuple)) else value

    if sparse_mode in SPARSE_IDF:
        # sparse 는 파이썬에서 낸다(IDF 가 필요하다). SQL 은 후보의 dense 만 돌려준다.
        params["cand"] = sorted(index.candidates(text, sparse_mode))
        cur.execute(f"""
            with f as (select * from public.model_scout_models m where {' and '.join(where)}),
            d as (select model_id, (1-(embedding <=> %(vec)s::halfvec(1536)))::real dense
                  from f m order by embedding <=> %(vec)s::halfvec(1536) limit {DENSE_DEPTH}),
            s as (select model_id, (1-(embedding <=> %(vec)s::halfvec(1536)))::real dense
                  from f m where m.model_id = any(%(cand)s::text[]))
            select coalesce(d.model_id, s.model_id), coalesce(d.dense, s.dense)
            from d full outer join s on d.model_id = s.model_id
        """, params)
        rows = [(r[0], float(r[1] or 0)) for r in cur.fetchall()]
        sparse_of = index.scores(text, sparse_mode, [m for m, _ in rows])
        return [(m, d, sparse_of.get(m, 0.0)) for m, d in rows]

    sparse = SPARSE_SQL[sparse_mode]
    cur.execute(f"""
        with f as (select * from public.model_scout_models m where {' and '.join(where)}),
        d as (select model_id, (1-(embedding <=> %(vec)s::halfvec(1536)))::real dense
              from f m order by embedding <=> %(vec)s::halfvec(1536) limit {DENSE_DEPTH}),
        s as (select model_id, {sparse} sparse from f m
              where {sparse} > 0)
        select coalesce(d.model_id, s.model_id),
               coalesce(d.dense, (select (1-(embedding <=> %(vec)s::halfvec(1536)))::real
                                  from public.model_scout_models x where x.model_id = s.model_id)),
               coalesce(s.sparse, 0)
        from d full outer join s on d.model_id = s.model_id
    """, params)
    return [(r[0], float(r[1] or 0), float(r[2] or 0)) for r in cur.fetchall()]


def load_queries(types: Optional[Sequence[str]]) -> List[Dict[str, Any]]:
    cache = json.loads((QUERIES / "decompose_cache.json").read_text(encoding="utf-8"))
    out = []
    for kind, name in SPECS.items():
        if types and kind not in types:
            continue
        spec = importlib.util.spec_from_file_location(name[:-3], QUERIES / name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for item in module.QUERIES:
            entry = cache.get(item["text"]) or {}
            needs = entry.get("needs") or []
            out.append({**item, "model_query": needs[0]["model_query"] if needs else item["text"]})
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--types", default="")
    ap.add_argument("--sparse", default="plainto", choices=sorted(SPARSE_MODES))
    ap.add_argument("--use-raw-text", action="store_true", help="model_query 대신 원문으로 검색")
    ap.add_argument("--conditions", default="oracle", choices=("oracle", "decomposed", "dec_task_fixed"),
                    help="하드 필터를 골든셋이 적어 둔 조건(oracle)에서 가져올지, "
                         "분해가 뽑은 것(decomposed, 운영 경로)에서 가져올지. "
                         "dec_task_fixed 는 분해 조건에 올바른 task 만 끼운다 — "
                         "분해의 분류 키 버그만 고쳤을 때의 값")
    ap.add_argument("--size-guard", action="store_true",
                    help="질문에 한정어가 없으면 크기 상한을 버린다 (17.SIZE_BOUND 와 같은 규칙)")
    ap.add_argument("--no-task-for", default="",
                    help="이 유형들에서 task 하드 필터를 걸지 않는다. 쉼표로 구분")
    ap.add_argument("--tag", default="", help="출력 파일 이름에 붙일 꼬리말")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    types = [t.strip() for t in args.types.split(",") if t.strip()] or None

    import corpus
    import scan

    rows = corpus.load_corpus()
    items = load_queries(types)
    print(f"질의 {len(items)}개 · sparse={args.sparse} · "
          f"검색어={'원문' if args.use_raw_text else 'model_query'} · 조건={args.conditions}")

    # 운영 경로를 재현할 때는 하드 필터도 분해 결과에서 가져온다.
    filters: Dict[str, Dict[str, Any]] = {}
    if args.conditions in ("decomposed", "dec_task_fixed"):
        import preretrieval
        cache = json.loads((QUERIES / "decompose_cache.json").read_text(encoding="utf-8"))
        no_task_for = tuple(t.strip() for t in args.no_task_for.split(",") if t.strip())
        # 유형별 정책은 런타임 분류를 믿는 것이므로, 정답 유형이 아니라 예측 유형을 쓴다.
        predicted: Dict[str, Any] = {}
        if no_task_for:
            fc = _load_module("fc", Path(__file__).resolve().parent / "final_compare.py")
            predicted = fc.predicted_types([i["text"] for i in items])
            print(f"  task 필터를 걸지 않는 유형: {', '.join(no_task_for)} (예측 유형 기준)")
        if args.size_guard:
            print("  질문에 한정어가 없으면 크기 상한을 버린다")
        blocked = 0
        for item in items:
            # dec_task_fixed = 유효하지 않은 분류 키를 코퍼스의 분류로 매핑한 것.
            # 운영에서 MODEL_TASK_FALLBACK 두 줄로 고칠 수 있는 범위다.
            got = preretrieval.conditions_from_decompose(
                cache.get(item["text"]) or {}, fix_task=args.conditions == "dec_task_fixed",
                text=item["text"], size_guard=args.size_guard, no_task_for=no_task_for,
                query_type=predicted.get(item["text"]))
            filters[item["qid"]] = got
            blocked += bool(got["unsupported"])
        print(f"  분해가 코퍼스에 없는 분류를 골라 검색이 아예 없는 질의 {blocked}개 "
              f"→ 결과 0건으로 기록한다")

    texts = [(i["text"] if args.use_raw_text else i["model_query"]) for i in items]
    vectors = embed(sorted(set(texts)))

    conn = connect()
    out: List[Dict[str, Any]] = []
    started = time.perf_counter()
    try:
        with conn.cursor() as cur:
            index = None
            if args.sparse in SPARSE_IDF:
                import sparse_idf
                index = sparse_idf.load(cur, texts)
            for n, (item, text) in enumerate(zip(items, texts), 1):
                query = dict(item)
                query.update(query_id=item["qid"], expected_behavior="recommend", query=item["text"])
                grades = {}
                for model_id, d in scan.scan_query(query, rows)["decisions"].items():
                    if d["class"] == "proposed_grade_2":
                        grades[model_id] = 2
                    elif d["class"] == "proposed_grade_1":
                        grades[model_id] = 1
                if args.conditions in ("decomposed", "dec_task_fixed"):
                    got = filters[item["qid"]]
                    # 운영은 태그가 없으면 unsupported 로 끝낸다. 검색이 없었으니 결과도 없다.
                    conditions = got["conditions"]
                    scored = [] if got["unsupported"] else score_one(
                        cur, text, vectors[text], conditions, args.sparse, index)
                else:
                    scored = score_one(cur, text, vectors[text], item.get("conditions") or {},
                                       args.sparse, index)
                out.append({"qid": item["qid"], "query_type": item["query_type"],
                            "origin": item.get("origin"), "text": item["text"], "search_text": text,
                            "grades": grades, "scored": scored})
                if n % 20 == 0 or n == len(items):
                    print(f"  {n}/{len(items)}  ({time.perf_counter()-started:.0f}s)", flush=True)
    finally:
        conn.rollback()
        conn.close()

    path = args.out or (AI / "test" / "model_retrieval" / "runs" /
                        f"scores_{args.sparse}{'_raw' if args.use_raw_text else ''}"
                        f"{ {'decomposed':'_dec','dec_task_fixed':'_dectf'}.get(args.conditions,'') }"
                        f"{args.tag}.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"sparse_mode": args.sparse,
                                "search_text": "raw" if args.use_raw_text else "model_query",
                                "conditions": args.conditions,
                                "embed_model": EMBED_MODEL, "dense_depth": DENSE_DEPTH,
                                "queries": out}, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"→ {path.relative_to(AI)}  ({path.stat().st_size/1e6:.1f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


def compare_with_rpc(limit: int = 8, types: Optional[Sequence[str]] = None) -> int:
    """평가기와 운영 RPC 의 상위 20개가 같은지 확인한다. 이게 통과해야 측정이 유효하다."""
    items = load_queries(types)[:limit]
    texts = [i["model_query"] for i in items]
    vectors = embed(sorted(set(texts)))
    conn = connect()
    same = diff = 0
    try:
        with conn.cursor() as cur:
            for item, text in zip(items, texts):
                c = item.get("conditions") or {}
                cur.execute(
                    "select model_id from public.match_model_scout_models("
                    "%s::vector, %s::integer, %s::text, %s::text[], %s::boolean, %s::numeric, %s::numeric,"
                    "%s::integer, %s::integer, %s::boolean, %s::boolean, %s::text, %s::text, %s::real,"
                    "%s::real, %s::text[], %s::text[], %s::numeric, %s::boolean)",
                    (str(vectors[text]), 20, None, c.get("tasks"), bool(c.get("korean_required")), None,
                     c.get("max_parameters_billion"), c.get("min_context_length"), c.get("max_context_length"),
                     False, False, c.get("popularity_tier"), text, 0.65, 0.35,
                     c.get("commercial_status"), c.get("require_artifact"), c.get("max_artifact_gib"),
                     bool(c.get("exclude_gated"))))
                rpc = [r[0] for r in cur.fetchall()]
                scored = score_one(cur, text, vectors[text], c, "plainto")
                mine = [m for m, _, _ in sorted(scored, key=lambda r: (-(0.65 * r[1] + 0.35 * r[2]), r[0]))][:len(rpc)]
                if mine == rpc:
                    same += 1
                else:
                    diff += 1
                    print(f"  ❌ {item['qid']}")
    finally:
        conn.rollback()
        conn.close()
    print(f"RPC 대조: 일치 {same} · 불일치 {diff}")
    return 1 if diff else 0
