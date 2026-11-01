---
license: cc0-1.0
pretty_name: Depesche Wikidata Hot Index
tags:
- wikidata
- knowledge-graph
- entity-linking
- entity-resolution
- vector-search
- knowledge-base
size_categories:
- 10M<n<100M
language:
- en
- es
- ru
- fa
- ko
- ar
- zh
- ja
- de
- fr
- pt
- it
- tr
- id
- vi
- th
- hi
- uk
- pl
- nl
- sv
- he
- ms
- bn
- ur
- el
- cs
- ro
- hu
- fi
- nb
- nn
- ca
---

# Depesche Wikidata Hot Index

A prebuilt, file-backed **Wikidata index** optimized for **entity linking (resolve)**, **facet / type checks (`is_a`)**, compositional queries, and **multilingual semantic similarity** — no external database required. Everything is mmap-friendly on-disk artifacts (FST, roaring bitmaps, CSR graphs, usearch vector shards).

**Reader / builder code:** https://github.com/mrink68/depesche-wd-index (Rust crates + `wd` CLI + PyO3 bindings)

## Provenance

- **Source:** official Wikidata JSON dump `latest-all.json.gz` (~155 GB compressed), snapshot from **July 2026**
- **Build floor:** `build_min_sitelinks = 2` → **14,213,939 notable items** kept out of 120,905,360 scanned entities (P279 class edges are collected for *all* entities)
- **Index format:** `format_version 4`
- **Resolve languages:** 34 (aliases ingested for `en es ru fa ko ar zh ja de fr pt it tr id vi th hi uk pl nl sv he ms bn ur el cs ro hu fi no nb nn ca`)
- **License:** Wikidata content is [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/); this dataset is a derived transformation of it.

## Contents (~30 GB)

| File | Size | What it is |
|---|---|---|
| `meta.json` | 3 KB | Build metadata: counts, languages, facet roots, hot properties |
| `entity_hot.bin` | 512 MB | Fixed-width hot rows (36 B/entity) incl. `sitelinks_n` |
| `entity_warm.zst` | 6.4 GB | Per-entity frames: display label + thin claims/sitelinks (zstd, `warm.zdict` dictionary) |
| `entity_dir.bin` | 341 MB | QID → hot/warm offset directory |
| `aliases.fst` | 2.3 GB | `lang\0normalized_surface` → postings offset (resolve index) |
| `alias_postings.bin` | 2.0 GB | Per-surface `(qid u32, sitelinks_n u16)` postings, popularity DESC |
| `edges.csr` | 1.4 GB | Undirected item-claim graph for `path()` BFS |
| `p279_parents.csr` / `p279_children.csr` | 57 / 23 MB | Subclass-of closure graphs |
| `p31_edges.bin` / `p279_edges.bin` / `p131_edges.bin` | 119 / 42 / 27 MB | Raw typed edges |
| `postings/P*.bin` | 95 MB | Filterable postings for P31, P17, P27, P39, P102, P106, P131, P279 (`match`/`inbound`) |
| `facets/*.roaring` + `summary.json` | 20 MB | Precomputed type bitsets (human, city, business, airport, film, …, 28 roots) |
| `coords.bin` | 46 MB | Geohash-bucketed P625 coordinates for `near()` |
| `vectors.f16.matrix` | 10.9 GB | 14,213,256 × 384 fp16 embedding matrix |
| `vectors.shard00..02.usearch` | 3 × 2.5 GB | Sharded ANN indexes (i8, cosine) — sharded because usearch breaks past 4 GiB/index |
| `vectors.shards.json` / `vectors.meta.json` | — | Shard map + embedding provenance |
| `warm.zdict` | 110 KB | zstd dictionary for `entity_warm.zst` |

**Embeddings:** `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, mean pooling, L2-normalized, text template `"{label}. {description}"`.

Two build intermediates are intentionally **not included** because they are regenerable from the files above using the repo code:

- `aliases.tsv` (11.5 GB) — rebuild from warm frames via `wd materialize` (`rebuild_aliases_tsv_from_warm`), or skip it: resolve uses `aliases.fst` directly
- `embed_corpus.tsv` (0.9 GB) — regenerate with `wd export-embed-corpus` (~18 min)

## Usage

Download the dataset into an `index/` directory, then query it with the code from the [GitHub repo](https://github.com/mrink68/depesche-wd-index):

```bash
hf download Somnia/depesche-wd-index --repo-type dataset --local-dir ./index

git clone https://github.com/mrink68/depesche-wd-index
cd depesche-wd-index && cargo build -p wd-cli --release

./target/release/wd resolve --dir ../index "Spain" --lang en --limit 10
./target/release/wd is-a   --dir ../index Q31 sovereign_state
./target/release/wd doctor --dir ../index   # verify every artifact
```

Or from Python (PyO3 bindings, `crates/wd-py`):

```python
from wd_index import Index
idx = Index("./index")

idx.resolve("7-Eleven", lang="th")                        # alias FST, popularity-ranked
idx.match_([("P106", "Q82955"), ("P27", "Q183")])         # German politicians
idx.value_at("Q22686", "P39", 2019)                        # position held in 2019
idx.near(48.1374, 11.5755, radius_km=30, facet="airport")  # geo query
idx.similar("Q90", k=20)                                   # multilingual ANN over MiniLM vectors
```

Full query surface (resolve / get / is_a / match / inbound / instances_of / types / subclasses / neighbors / value_at / top / count_by / near / path / similar) is documented in the repo README.

## Notes

- Artifacts are **little-endian**; build and query on the same endianness (x86_64 is fine).
- Treat the directory as **immutable** — replace atomically on rebuild.
- Run `wd doctor` after download: it verifies every artifact and names what each absence silently breaks.
