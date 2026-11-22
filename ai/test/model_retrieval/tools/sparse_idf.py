#!/usr/bin/env python3
"""C안 — IDF 가중 매칭 비율로 sparse 점수를 낸다.

운영의 sparse 는 두 가지가 동시에 고장나 있다.

  ① plainto_tsquery 가 모든 단어를 AND 로 묶는다 → 한 단어라도 없으면 전 행 0
  ② search_tsv 는 JSON 전체를 텍스트로 캐스팅해 넣는다 → 키 이름과
     technical_metadata.contract 의 한국어 안내 문구가 4017행 전부에 들어 있다

②때문에 ①을 단순 OR 로 바꾸면(B안) 4017행 100%에 있는 토큰이 순위를 오염시킨다.
그래서 C안은 OR 로 넓히면서 **각 단어의 희소성으로 가중**한다.

    df(t)      t 를 가진 활성 행 수
    idf(t)     ln(1 + (N - df + 0.5)/(df + 0.5))          BM25 식
    terms_eff  질의 렉심 중 df > 0 인 것만            ← idf 모드
    sparse(d)  Σ(t ∈ terms_eff ∩ d) idf(t) / Σ(t ∈ terms_eff) idf(t)   ∈ [0,1]

세 성질이 한 식에서 같이 나온다.
  · IDF 가중   df=4017 인 상용구는 idf≈0 이라 저절로 무시된다
  · 매칭 비율   질의어를 많이 맞춘 행이 높다(ts_rank_cd 의 빈도·근접도가 아니라)
  · 질의별 정규화  분모가 질의마다 달라 [0,1] 로 떨어진다 → dense 와 같은 자리

df=0 인 질의어(코퍼스에 아예 없는 한국어 등)를 분모에 넣을지가 설계 선택이다.
넣으면(idf_all) 한국어가 많은 질의는 sparse 가 구조적으로 눌린다. 빼면(idf)
"가를 수 있는 단어"만으로 비율을 본다. 둘 다 재서 비교한다.

    python test/model_retrieval/tools/sparse_idf.py          # 캐시 만들고 분포 출력
    python test/model_retrieval/tools/sparse_idf.py --check  # 렉심 왕복이 맞는지 검증
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Set, Tuple

AI = Path(__file__).resolve().parents[3]
CACHE = AI / "test" / "model_retrieval" / "cache" / "sparse_idf.json"
MODES = ("idf", "idf_all")


# --------------------------------------------------------------------------- 지수

class IdfIndex:
    """질의 렉심 → idf, 그리고 렉심을 가진 model_id 집합."""

    def __init__(self, n: int, df: Dict[str, int], postings: Dict[str, Sequence[str]],
                 lexemes: Dict[str, List[str]]):
        self.n = n
        self.df = df
        self.postings = {t: set(ids) for t, ids in postings.items()}
        self.lexemes = lexemes

    def idf(self, term: str) -> float:
        df = self.df.get(term, 0)
        return math.log(1 + (self.n - df + 0.5) / (df + 0.5))

    def terms_for(self, text: str, mode: str) -> List[str]:
        """질의문의 렉심. idf 모드는 코퍼스에 없는 단어를 뺀다."""
        terms = self.lexemes.get(text) or []
        if mode == "idf":
            return [t for t in terms if self.df.get(t, 0) > 0]
        return terms

    def candidates(self, text: str, mode: str) -> Set[str]:
        """sparse > 0 이 될 수 있는 model_id. 하나라도 맞은 행이다."""
        out: Set[str] = set()
        for term in self.terms_for(text, mode):
            out |= self.postings.get(term, set())
        return out

    def scores(self, text: str, mode: str, model_ids: Iterable[str]) -> Dict[str, float]:
        terms = self.terms_for(text, mode)
        weights = [(t, self.idf(t)) for t in terms]
        total = sum(w for _, w in weights)
        if total <= 0:
            return {}
        hit = {t: self.postings.get(t, set()) for t, _ in weights}
        out: Dict[str, float] = {}
        for model_id in model_ids:
            got = sum(w for t, w in weights if model_id in hit[t])
            if got > 0:
                out[model_id] = got / total
        return out


# --------------------------------------------------------------------------- 만들기

def _query_lexemes(cur, texts: Sequence[str]) -> Dict[str, List[str]]:
    """운영과 같은 'simple' 설정으로 질의문을 렉심으로 쪼갠다."""
    cur.execute("""
        select t.txt, coalesce(array_agg(u.lexeme order by u.lexeme), '{}')
        from unnest(%(texts)s::text[]) t(txt)
        left join lateral unnest(to_tsvector('simple', t.txt)) u on true
        group by t.txt
    """, {"texts": list(texts)})
    return {txt: list(lex) for txt, lex in cur.fetchall()}


def _postings(cur, terms: Sequence[str]) -> Tuple[int, Dict[str, int], Dict[str, List[str]]]:
    """렉심별 df 와 model_id 목록. search_tsv 의 GIN 색인을 그대로 쓴다."""
    cur.execute("select count(*) from public.model_scout_models where active")
    n = int(cur.fetchone()[0])
    cur.execute("""
        select t.term, array_agg(m.model_id)
        from unnest(%(terms)s::text[]) t(term)
        join public.model_scout_models m
          on m.active and m.search_tsv @@ plainto_tsquery('simple', t.term)
        group by t.term
    """, {"terms": list(terms)})
    postings = {term: list(ids) for term, ids in cur.fetchall()}
    df = {term: len(ids) for term, ids in postings.items()}
    for term in terms:                      # 코퍼스에 없는 단어도 기록해 둔다
        df.setdefault(term, 0)
    return n, df, postings


def build(cur, texts: Sequence[str]) -> Dict[str, Any]:
    lexemes = _query_lexemes(cur, sorted(set(texts)))
    terms = sorted({t for lex in lexemes.values() for t in lex})
    n, df, postings = _postings(cur, terms)
    return {"n": n, "df": df, "postings": postings, "lexemes": lexemes}


def load(cur=None, texts: Sequence[str] = ()) -> IdfIndex:
    """캐시를 읽는다. 질의문이 캐시에 없으면 cur 로 다시 만든다."""
    data = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else None
    if data is not None and all(t in data["lexemes"] for t in texts):
        return IdfIndex(data["n"], data["df"], data["postings"], data["lexemes"])
    if cur is None:
        raise SystemExit(f"{CACHE.name} 가 없거나 질의가 더 많다. --sparse idf 는 DB 연결이 필요하다")
    data = build(cur, texts)
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(data, ensure_ascii=False) + "\n", encoding="utf-8")
    return IdfIndex(data["n"], data["df"], data["postings"], data["lexemes"])


# --------------------------------------------------------------------------- 보기

def _load_texts() -> Tuple[List[str], Any]:
    import importlib.util
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    spec = importlib.util.spec_from_file_location("ev", Path(__file__).resolve().parent / "evaluator.py")
    ev = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ev)
    return [i["model_query"] for i in ev.load_queries(None)], ev


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="렉심 왕복(to_tsvector→plainto_tsquery)이 맞는지 검증")
    args = ap.parse_args()

    texts, ev = _load_texts()
    conn = ev.connect()
    try:
        with conn.cursor() as cur:
            index = load(cur, texts)
            if args.check:
                return _check(cur, index)
    finally:
        conn.rollback()
        conn.close()

    terms = sorted({t for text in texts for t in index.lexemes.get(text, [])})
    absent = [t for t in terms if index.df.get(t, 0) == 0]
    ubiquitous = [t for t in terms if index.df.get(t, 0) == index.n]
    print(f"질의 {len(set(texts))}개 · 렉심 {len(terms)}개 · 활성 {index.n}행\n")
    print(f"  코퍼스에 없음 (df=0)   {len(absent):5d}개  → idf 모드는 분모에서 뺀다")
    print(f"  전 행에 있음 (df=N)    {len(ubiquitous):5d}개  → idf≈0 이라 저절로 무시된다")
    print(f"  가를 수 있음           {len(terms)-len(absent)-len(ubiquitous):5d}개")

    print("\n질의당 sparse 가 0 이 아닐 수 있는가")
    for mode in MODES:
        alive = sum(1 for t in set(texts) if index.terms_for(t, mode)
                    and any(index.df.get(x, 0) > 0 for x in index.terms_for(t, mode)))
        print(f"  {mode:8s} {alive:3d} / {len(set(texts))}")

    print("\nidf 가 가장 높은 질의어(희소) / 가장 낮은 질의어(상용구)")
    ranked = sorted(((index.idf(t), t, index.df.get(t, 0)) for t in terms if index.df.get(t, 0) > 0),
                    reverse=True)
    for w, t, df in ranked[:6]:
        print(f"  {t:28s} df {df:5d}  idf {w:5.2f}")
    print("  ...")
    for w, t, df in ranked[-6:]:
        print(f"  {t:28s} df {df:5d}  idf {w:5.2f}")
    return 0


def _check(cur, index: IdfIndex) -> int:
    """plainto_tsquery('simple', 렉심) 이 to_tsvector 의 렉심을 되돌려주는지 본다.

    되돌려주지 않는 렉심이 있으면 df 가 과소 집계된다. 그 목록을 보여 준다.
    """
    terms = sorted(index.df)
    cur.execute("""
        select t.term, (select array_agg(u.lexeme) from unnest(
                 to_tsvector('simple', t.term)) u)
        from unnest(%(terms)s::text[]) t(term)
    """, {"terms": terms})
    bad = []
    for term, back in cur.fetchall():
        if list(back or []) != [term]:
            bad.append((term, list(back or [])))
    print(f"렉심 {len(terms)}개 중 왕복이 깨진 것 {len(bad)}개")
    for term, back in bad[:20]:
        print(f"  {term!r:30s} → {back}")
    if bad:
        print("\n이 렉심들은 df 가 과소 집계된다. 질의에서 차지하는 비중을 확인해야 한다.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
