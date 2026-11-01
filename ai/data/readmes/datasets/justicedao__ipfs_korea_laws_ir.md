---
license: other
task_categories:
- text-retrieval
tags:
- legal
- law
- graphrag
- bm25
- research
- not-legal-advice
- korea
pretty_name: Korea (ROK) laws IR (CID-keyed GraphRAG)
size_categories:
- 100K<n<1M
configs:
- config_name: corpus
  data_files:
  - split: train
    path: data/corpus/*.parquet
- config_name: bm25_documents
  data_files:
  - split: train
    path: data/bm25/documents/*.parquet
- config_name: bm25_postings
  data_files:
  - split: train
    path: data/bm25/postings/*.parquet
- config_name: bm25_keyword_index
  data_files:
  - split: train
    path: indexes/bm25_keyword_shards.parquet
- config_name: vectors
  data_files:
  - split: train
    path: data/vectors/*.parquet
- config_name: vector_meta_index
  data_files:
  - split: train
    path: indexes/vector_chunks.parquet
- config_name: graph_nodes
  data_files:
  - split: train
    path: data/graph/nodes/*.parquet
- config_name: graph_edges
  data_files:
  - split: train
    path: data/graph/edges/*.parquet
- config_name: graph_outgoing_adjacency
  data_files:
  - split: train
    path: data/graph/adjacency/out/*.parquet
- config_name: graph_incoming_adjacency
  data_files:
  - split: train
    path: data/graph/adjacency/in/*.parquet
language:
- ko
---

# Korea (ROK) legislation IR (CID-keyed sparse GraphRAG)

Research retrieval release of `endomorphosis/ipfs_korea_laws` (revision `a174ce3d2e51385dd21584ba4aa7618c97910d86`) packaged as
`country-laws-ir-graphrag/v1` (layout family `skillcenter-huggingface-release/v3` / publicus-ir).

**Not legal advice.** This is a research snapshot. The official gazette /
authentic source of Korea (ROK) prevails over this corpus. Retrieved documents
and graph edges are retrieval evidence only. No legal text was invented.

Primary key: `entry_cid` (CIDv1 raw sha2-256 of a canonical identity record).
Integer `document_index` values are compact shard pointers, not identities.

Target Hub id (packaging metadata only): `justicedao/ipfs_korea_laws_ir`.

## Counts

| Field | Value |
| --- | --- |
| Laws (corpus units) | 5659 |
| Articles (corpus units) | 159697 |
| Canonical docs | 165356 |
| BM25 terms | 29391 |
| BM25 postings | 1488314 |
| Graph nodes | 182329 |
| Graph edges | 1157492 |
| Vectors | 165356 × 384-d `thenlper/gte-small` (embedded) |

## Canonical fields

`entry_cid`, `law_cid`, `record_type`, `jurisdiction`, `language`,
`instrument_id`, `instrument_title`, `article_number`, `article_title`,
`title`, `body`, `source_url`, `snapshot_date`, `coverage`, `license`,
`collector`, `source_dataset`, `source_revision`.

Unit policy: prefer article/section rows; fall back to law-level when
`articles.parquet` is empty.

## Index layout

Zstandard parquet shards with at most 4,096 rows.

- `indexes/bm25_keyword_shards.parquet` — lexical term ranges → BM25 posting shards
- `indexes/vector_chunks.parquet` — semantic routing centroids (rows sorted by cosine to shard centroid)
- `indexes/corpus_chunks.parquet` — document ranges → corpus shards
- `data/graph/nodes` / `data/graph/edges` — property graph
- `data/graph/adjacency/{incoming,outgoing}` — score-ordered neighbor pages

BM25: Okapi k1=1.2, b=0.75, title_weight=5, body_weight=1 (FTS5 unicode61-style tokenizer).

Graph: one node per `entry_cid` plus facet nodes (`_facet_cid(kind, value)` for
jurisdiction, language, instrument, source, status). Neighbor edges
`BM25_NEIGHBOR_OF` (k=8) carry score and matched terms. Structural edges:
`ARTICLE_OF` (article → parent law) when articles exist, plus `IDENTIFIED_BY_ELI`
/ `IDENTIFIED_BY` only when those identifiers are present in the source.

## Query

```
python scripts/query_country_laws_hf.py --local-dir . bm25 "constitution" --top-k 10
python scripts/query_country_laws_hf.py --local-dir . vector "money laundering" --top-k 10
python scripts/query_country_laws_hf.py --local-dir . graph neighbors <entry_cid>
```

## Publish later (operator)

```
export HF_TOKEN=...   # never commit
hf upload-large-folder justicedao/ipfs_korea_laws_ir . \
  --repo-type dataset --no-private --num-workers 8 \
  --exclude "**/__pycache__/**" --exclude "**/*.pyc"
```

## Provenance

Packaged by country-laws-ir. Upstream collector and official license remain those
of `endomorphosis/ipfs_korea_laws`. CIDs identify local content; they do not prove public IPFS pinning.


## Scrapers & normalizer
The scrapers and normalizer that produced this dataset are published in [justicedao/world_law_scrapers](https://huggingface.co/datasets/justicedao/world_law_scrapers) (canonical schema: `law_id, id, title, text, source_url, document_number, article_number, record_type, metadata_json`, matching endomorphosis/ipfs_malta_laws).
