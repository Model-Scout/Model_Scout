#!/usr/bin/env python3
"""Build judging pools for the public-data golden set (no API key).

For each query in labels/public_data_queries.jsonl:
1. Corpus = public datasets in the hypergraph (seoul_open_data, data_go_kr). These are the
   canonical rows the recommender can return; cross-listed copies are already folded into
   one entity and kept in its `duplicates`, so a judged id also covers its copies.
2. Rank the corpus two ways and interleave them until POOL_SIZE candidates are chosen:
   - BM25 over title + card text, query text and pool_terms, Korean char bigrams
   - title match: how many pool_terms appear in the title (ties: shorter title first)
   - region (queries with a region condition): BM25 order restricted to that region
   When data/dataset_index/embeddings.npy and OPENAI_API_KEY are both present, the dense
   ranking (hypergraph_search.dense_scores) is interleaved as a third source.
3. Attach the facts a judge needs (publisher, region, delivery, license, fields, regional
   copies) and shuffle the display order with a fixed seed so judges are not anchored.

Conditions (region, delivery, realtime, commercial) are not used as filters here: a
candidate that misses a hard condition must be judged 0 with that reason, and it is only
in the pool if a ranker surfaced it. pool_terms only steer pooling and are never scored.
Abstention queries get a pool too, so judges can confirm nothing fits.

    python test/public_data/build_public_pool.py
"""

from __future__ import annotations

import argparse
import json
import math
import os
import random
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "test" / "public_data"
QUERY_PATH = HERE / "labels" / "public_data_queries.jsonl"
OUTPUT_PATH = HERE / "reports" / "public_pool.json"
ENTITIES = ROOT.parent / "backend" / "data" / "hypergraph" / "entities.jsonl"
CHUNKS = ROOT.parent / "backend" / "data" / "dataset_index" / "chunks.jsonl"
STAGE1 = ROOT.parent / "backend" / "data" / "public_datasets_stage1.jsonl"
PUBLIC_SOURCES = {"seoul_open_data", "data_go_kr"}
POOL_SIZE = 12
SEED = 20261101
K1, B = 1.2, 0.75
DESCRIPTION_CHARS = 300

sys.path.insert(0, str(ROOT))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def tokens(text: str) -> list[str]:
    """Whole words plus Korean char bigrams: there is no morpheme analyzer, and bigrams let
    '주차장정보' match '주차장'."""
    out: list[str] = []
    for word in re.findall(r"[0-9A-Za-z]+|[가-힣]+", text.lower()):
        out.append(word)
        if re.fullmatch(r"[가-힣]+", word) and len(word) > 2:
            out += [word[i : i + 2] for i in range(len(word) - 1)]
    return out


class BM25:
    def __init__(self, docs: list[list[str]]):
        self.tf = [Counter(d) for d in docs]
        self.len = [len(d) for d in docs]
        self.avg = sum(self.len) / max(len(docs), 1)
        df = Counter(t for d in self.tf for t in d)
        n = len(docs)
        self.idf = {t: math.log(1 + (n - c + 0.5) / (c + 0.5)) for t, c in df.items()}

    def scores(self, query: list[str]) -> list[float]:
        q = Counter(query)
        out = []
        for tf, length in zip(self.tf, self.len, strict=True):
            s = 0.0
            for t, qn in q.items():
                if t in tf:
                    f = tf[t]
                    s += qn * self.idf[t] * f * (K1 + 1) / (f + K1 * (1 - B + B * length / self.avg))
            out.append(s)
        return out


def load_corpus() -> list[dict[str, Any]]:
    import hypergraph_search as hs

    stage1 = {r["dataset_id"]: r for r in read_jsonl(STAGE1)}
    cards = {}
    with open(CHUNKS, encoding="utf-8") as f:
        for line in f:
            if '#card"' not in line[:200]:
                continue
            row = json.loads(line)
            if row["kind"] == "card":
                cards[row["dataset_id"]] = row["text"]
    corpus = []
    for e in read_jsonl(ENTITIES):
        if e["kind"] != "dataset" or e.get("source") not in PUBLIC_SOURCES:
            continue
        row = stage1.get(e["name"], {})
        title = e.get("title") or row.get("card_data", {}).get("pretty_name") or e["name"]
        description = row.get("description") or ""
        corpus.append(
            {
                "dataset_id": e["name"],
                "title": title,
                "source": e["source"],
                "url": e["url"],
                "publisher": row.get("org") or ("서울특별시" if e["source"] == "seoul_open_data" else None),
                "category": row.get("category"),
                "regions": sorted(hs.dataset_regions(e)) or ["전국"],  # from source + title, like the retriever
                "delivery": row.get("formats") or [],
                "list_type": row.get("list_type") or ("openapi" if e["source"] == "seoul_open_data" else None),
                "tier": row.get("tier"),
                "licenses": e.get("licenses") or [],
                "last_modified": row.get("last_modified"),
                "field_count": row.get("field_count"),
                "description": description[:DESCRIPTION_CHARS],
                "regional_variant_count": row.get("regional_variant_count") or 0,
                "duplicates": e.get("duplicates") or [],
                "_text": " ".join([title, title, " ".join(row.get("tags") or []), cards.get(e["name"], description)]),
            }
        )
    return corpus


def dense_ranking(query: str, corpus: list[dict[str, Any]]) -> list[int] | None:
    if not ((ROOT.parent / "backend" / "data" / "dataset_index" / "embeddings.npy").exists() and os.environ.get("OPENAI_API_KEY")):
        return None
    import hypergraph_search as hs

    sims = hs.dense_scores(hs.embed_query(query))
    return sorted(range(len(corpus)), key=lambda i: -sims.get(corpus[i]["dataset_id"], -1.0))


def title_ranking(terms: list[str], corpus: list[dict[str, Any]]) -> list[int]:
    hits = [(sum(t in d["title"] for t in terms), i) for i, d in enumerate(corpus)]
    hits = [(n, i) for n, i in hits if n]
    hits.sort(key=lambda x: (-x[0], len(corpus[x[1]]["title"]), corpus[x[1]]["dataset_id"]))
    return [i for _, i in hits]


def interleave(rankings: dict[str, list[int]], size: int) -> list[tuple[int, list[str]]]:
    chosen: dict[int, list[str]] = {}
    cursors = dict.fromkeys(rankings, 0)
    while len(chosen) < size and any(cursors[k] < len(r) for k, r in rankings.items()):
        for name, ranking in rankings.items():
            while cursors[name] < len(ranking):
                i = ranking[cursors[name]]
                cursors[name] += 1
                if i in chosen:
                    chosen[i].append(name)
                    continue
                chosen[i] = [name]
                break
            if len(chosen) >= size:
                break
    # Record later hits too, so pool_sources says which rankers agreed.
    for name, ranking in rankings.items():
        for i in ranking[: size * 2]:
            if i in chosen and name not in chosen[i]:
                chosen[i].append(name)
    return list(chosen.items())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--queries", type=Path, default=QUERY_PATH)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    parser.add_argument("--pool-size", type=int, default=POOL_SIZE)
    args = parser.parse_args()

    queries = read_jsonl(args.queries)
    corpus = load_corpus()
    bm25 = BM25([tokens(d["_text"]) for d in corpus])
    rng = random.Random(SEED)
    out_queries = []
    for q in queries:
        scores = bm25.scores(tokens(q["query"] + " " + " ".join(q["pool_terms"])))
        rankings = {
            "bm25": [i for i in sorted(range(len(corpus)), key=lambda i: -scores[i]) if scores[i] > 0],
            "title": title_ranking(q["pool_terms"], corpus),
        }
        if region := q["conditions"].get("region"):
            # Region is a hard condition: give in-region datasets their own lane, or a crowded
            # national topic (버스 정류소) can fill the pool before the one regional match appears.
            # Title matches first, then strong BM25 hits: char bigrams make almost every in-region
            # row score above 0, and a weak one is off-topic (낚시금지구역 for 어린이 보호구역).
            in_region = {i for i in range(len(corpus)) if region in corpus[i]["regions"]}
            titled = [i for i in title_ranking(q["pool_terms"], corpus) if i in in_region]
            floor = 0.5 * max((scores[i] for i in in_region), default=0.0)
            strong = [i for i in sorted(in_region, key=lambda i: -scores[i]) if scores[i] >= floor > 0]
            rankings["region"] = titled + [i for i in strong if i not in set(titled)]
        if (dense := dense_ranking(q["query"], corpus)) is not None:
            rankings["dense"] = dense
        picked = interleave(rankings, args.pool_size)
        candidates = []
        for i, sources in picked:
            card = {k: v for k, v in corpus[i].items() if not k.startswith("_")}
            card["pool_sources"] = sources
            candidates.append(card)
        rng.shuffle(candidates)
        out_queries.append(
            {
                **{k: q[k] for k in ("query_id", "query_type", "query", "domain", "conditions", "aspects")},
                "expected_behavior": q["expected_behavior"],
                "candidates": candidates,
            }
        )
    payload = {
        "seed": SEED,
        "pool_size": args.pool_size,
        "corpus_size": len(corpus),
        "corpus_sources": dict(Counter(d["source"] for d in corpus)),
        "rankers": sorted({s for q in out_queries for c in q["candidates"] for s in c["pool_sources"]}),
        "queries": out_queries,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    short = [q["query_id"] for q in out_queries if len(q["candidates"]) < args.pool_size]
    print(f"{len(out_queries)} queries, corpus {len(corpus)} {payload['corpus_sources']}, rankers {payload['rankers']}")
    print(f"pool < {args.pool_size}: {short or 'none'} -> {args.output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
