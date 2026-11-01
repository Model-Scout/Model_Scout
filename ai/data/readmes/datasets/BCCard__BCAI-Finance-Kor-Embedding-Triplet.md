---
license: cc-by-4.0
language:
- ko
task_categories:
- sentence-similarity
- text-retrieval
size_categories:
- 10K<n<100K
tags:
- finance
- korean
- embedding
- retrieval-evaluation
- triplet
- hard-negative-mining
- graded-relevance
pretty_name: BCAI Finance Kor Embedding Triplet
---

# 1. Overview
Korean financial-domain triplet dataset for fine-tuning sentence-embedding models, with graded relevance labels for `validation` / `test` splits. This is the **queries + labels** dataset; the **retrieval corpus** is the companion [`BCCard/BCAI-Finance-Kor-Embedding-Pair`](https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Pair) dataset.

## 1.1. TL;DR
* **45,394 triplets** (anchor / positive / negative) - mined with FAISS top-K + Claude Sonnet LLM judge (Hybrid Hard-Negative mining)
* **3 splits** : `train` (43,394) / `validation` (1,000) / **`test` (1,000) = Golden set**
* **Source-disjoint** at the **`anchor_parent_doc_id` level** (no sibling leakage across splits)
* **Graded relevance** : `validation` / `test` carry `relevant_chunk_ids` + `relevance_scores` columns (rel ∈ {1, 2, 3}; rel=0 sparse)
* **Corpus** : Pair dataset's `source_chunk_id` set (≈36k unique chunks)

## 1.2. Splits
> **`test` split is the Golden set** - the sealed reference benchmark used to report final retrieval quality. Do not train on it; do not select hyperparameters on it.

| split | rows | role | use case |
|-------|------|------|----------|
| `train` | 43,394 | training input | MNRL with hard negatives - no relevance labels |
| `validation` | 1,000 | dev set | HPO / checkpoint selection (IR metric on `relevance_*` columns) |
| `test` | 1,000 | **Golden set** | **Final retrieval evaluation** - report NDCG@10 / MRR@10 / Recall@10 / P@1 against this only |

* FAQ-direct subset cap: 50 each in `validation` / `test` (single-positive sweet spot for P@1 / MRR).
* Disjoint split unit = `anchor_parent_doc_id` (sibling-leakage prevention; see [Methodology](#16-methodology)).

### (1) Why `test` is the Golden set
1. **Sealed during training** - `train` / `validation` consumed by the model pipeline; `test` is never accessed until the final evaluation step.
2. **Source-disjoint from training** - no `anchor_parent_doc_id` overlap with `train` / `validation`, so reported scores reflect true generalization (not memorization).
3. **Graded relevance labels** - each query carries `relevant_chunk_ids` + `relevance_scores` (rel ∈ {1, 2, 3}) sufficient to compute the full IR metric suite without external annotation.
4. **Composition mirrors `validation`** - same `parent_doc`-level split policy, FAQ-cap, and graded scope rules, so HPO findings on `validation` transfer to `test`.

## 1.3. Schema
### (1) Common columns (all splits)

| column | type | description |
|--------|------|-------------|
| `anchor` | string | query text (= chunk text or its instruction-backtranslated variant `_q1/_q2/_q3`) |
| `positive` | string | paired correct doc text |
| `negative` | string | hard negative (LLM-judged from FAISS top-K candidates) |
| `anchor_chunk_id` | string | unique query id |
| `negative_chunk_id` | string | negative's chunk id |
| `negative_rank` | int | hardness rank among selected negatives (1 = highest hardness; currently single - rank=1) |
| `hardness` | string | `high` / `medium` / `low` (LLM judge) |
| `rationale` | string | LLM rationale for negative selection |
| `judge_source` | string | `llm` / `fallback` |
| `anchor_parent_doc_id` | string | sibling-leakage prevention unit (1000-floor of trailing number for crawl; row id for base) |

### (2) Additional columns (`validation` / `test` only)

| column | type | description |
|--------|------|-------------|
| `relevant_chunk_ids` | `list<string>` | candidate chunk_ids with rel > 0 (sparse) - references `source_chunk_id` of the [Pair dataset](https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Pair) |
| `relevance_scores` | `list<int>` | parallel array; `rel ∈ {1, 2, 3}` |

Parallel-array form (NER-style HF Datasets convention) - 1 row = self-contained query + qrels.

## 1.4. Relevance Grading

Per `(query, candidate_chunk)` pair, graded by **chunk distance** within the same parent_doc:

| rel | meaning | example |
|-----|---------|---------|
| **3** | paired positive (the query's own source chunk) | `query=_126006_q1` → candidate `_126006` |
| **2** | adjacent sibling (`chunk_distance ≤ 1` within same parent_doc) | `_126005`, `_126007` |
| **1** | non-adjacent same parent_doc | `_126000`, `_126001`, ..., `_126009` |
| **0** | different parent_doc | all other corpus chunks (sparse - omitted from arrays) |

`chunk_distance = abs(extract_chunk_idx(a) - extract_chunk_idx(b))`

## 1.5. Quick Start - Retrieval Evaluation against the Golden set

End-to-end IR evaluation = rank the **Pair corpus** for each `test` query (the Golden set) and compare against `relevance_scores`:

```python
from datasets import load_dataset

# (1) Load queries + graded labels (this dataset)
triplet = load_dataset("BCCard/BCAI-Finance-Kor-Embedding-Triplet")

# (2) Load retrieval corpus (companion Pair dataset)
pair = load_dataset("BCCard/BCAI-Finance-Kor-Embedding-Pair", split="train")

# (3) Build corpus dict (dedupe q-variants → unique source_chunk_id)
corpus = {}
for r in pair:
    corpus.setdefault(r["source_chunk_id"], r["positive"])
# ~36k unique chunks

# (4) Evaluate each Golden-set (test) query against the corpus
import numpy as np
from your_embedding_model import encode

corpus_ids = list(corpus.keys())
corpus_embs = encode([corpus[c] for c in corpus_ids])      # [N_corpus, D]

for row in triplet["test"]:                                 # ← Golden set
    query_emb = encode([row["anchor"]])                     # [1, D]
    scores = (query_emb @ corpus_embs.T).flatten()          # cosine / dot
    top_k_idx = np.argsort(-scores)[:10]                    # top-10
    top_k_chunk_ids = [corpus_ids[i] for i in top_k_idx]

    # Build qrels dict for this query (Golden ground truth)
    qrels = dict(zip(row["relevant_chunk_ids"], row["relevance_scores"]))

    # Compute NDCG@10 / MRR@10 / Recall@10 / P@1 against qrels
    # ...
```

### (1) Recommended metrics

| metric | use case |
|--------|----------|
| **NDCG@10** | graded ranking quality (primary; MTEB / BEIR standard) |
| **MRR@10** | first relevant position |
| **Recall@10** | coverage of relevant chunks |
| **P@1** | top-1 accuracy (sweet spot for FAQ-direct subset) |

The dataset is in **case A** (P90 of rel_total ≤ 10) - `k=10` is a safe primary cutoff (3-7% R-cap risk).

## 1.6. Methodology
### (1) Data pipeline (`hopper` module of [MokaGrinder](https://github.com/<owner>/mog))

```
BCAI Q&A + BC Card site crawl
   ↓ structuring / text-noise / PII masking
LumberChunker (LLM-guided semantic chunking; dual cap 512/1024 tokens)
   ↓ Multi-Query Instruction Backtranslation (q1/q2/q3)
Pair pool (45,589 records → 36,281 unique source_chunk_ids = corpus)
   ↓ Hybrid Hard-Negative Mining (FAISS top-K + Claude Sonnet judge)
Triplet pool (45,394 triplets)
   ↓ Phase 1 split (parent_doc-disjoint, FAQ cap=50)
   ↓ Phase 2 enrich (graded relevance_labels for val/test)
This dataset
```

### (2) Splitting strategy (Phase 1)
* Unit of disjoint partition: `anchor_parent_doc_id` (NOT `anchor_chunk_id`) - prevents sibling leakage (same product's q1/q2/q3 don't end up in different splits)
* FAQ-direct subset (≈578 single-positive Q&A pairs): hard-capped at 50 per split for P@1 / MRR diagnostic
* Random seed = 42 (deterministic)

### (3) Naming convention - `source_chunk_id`

```
crawl_..._credit-card_29000   ← 1 product/article (multiple of 1000)
crawl_..._credit-card_29001   ← LumberChunker sub-chunk 1 (within same product)
crawl_..._credit-card_29008   ← sub-chunk 8

synth_crawl_..._29000_q1      ← Instruction-backtranslated query variant 1
synth_crawl_..._29008_q1      ← variant of sub-chunk 8

base_bcai_011324_000          ← BCAI raw row (no LLM, no chunking)
synth_base_bcai_011324_000_q1 ← BCAI row's query variant
```

`anchor_parent_doc_id` is derived by **flooring the trailing number to the nearest 1000** (for `crawl_*`) or by stripping the chunk_idx (for `base_*`).

<br>

# 2. Evaluation
## 2.1. Distribution Stats
### (1) Triplet counts per source prefix

| prefix | train | validation | test |
|--------|------:|-----------:|-----:|
| `base_*` (BCAI raw) | 29,669 | 695 | 671 |
| `synth_base_*` | 1,676 | 42 | 15 |
| `synth_crawl_*` | 11,571 | 213 | 264 |
| `crawl_*` (FAQ direct) | 478 | 50 | 50 |
| **total** | **43,394** | **1,000** | **1,000** |

### (2) rel_total distribution (`validation` + `test`)

| split | mean | median | P90 | P95 | P99 | max |
|-------|------|--------|-----|-----|-----|-----|
| validation | 2.70 | 1 | 8 | 11 | 12 | 12 |
| test | 2.62 | 1 | 8 | 10 | 11 | 11 |

R-cap @ k=10: validation 6.90% / test 3.30% of queries have `rel_total > 10`.

## 2.2. Quality Self-Assessment (LLM-assisted audit)

The dataset was audited with `Claude Fable 5` (2026-06-12): integrity checks (duplicates / empty rows / degenerate rows / parallel-array consistency / cross-split text leakage) plus the surface-signal measurements reported in Limitations.

**Overall score: 78 / 100** - scored against the bar for public datasets: clearly above typical first-iteration internal datasets (≈60), below human-verified benchmarks such as MS MARCO / BEIR (≈90).

| dimension | score | rationale |
|-----------|-------|-----------|
| Data integrity | 9.5/10 | all 43,394 train rows unique (triplet and (anchor, positive) level); 0 empty values; 0 degenerate rows (pos==neg / anchor==pos); 0 parallel-array mismatches |
| Split design & Golden-set discipline | 8/10 | parent_doc-disjoint + fixed seed + FAQ cap + sealed test - solid design; deducted for the cross-split duplicate-query finding below |
| Label (qrels) validity | 6/10 | weakest pillar - distance-based heuristic grades not yet LLM/human-verified, and the parent-doc-local labeling scope misses cross-document relevant chunks (evidenced below) |
| Surface-signal robustness | 7.5/10 | length / style clean; only the lexical shortcut remains (≈73% lexically solvable) - a level common in public benchmarks |
| Scale & composition | 8/10 | 45k triplets / 36k corpus chunks / 75% high-hardness negatives - sufficient for a domain dataset |
| Documentation | 9/10 | Limitations with measured numbers + Future Work - above the typical HF dataset card |
| Reproducibility & engineering | 9/10 | seed / versioning / split_meta / standard parquet layout |

### (1) Audit finding - cross-split duplicate queries

* The split is disjoint at the `anchor_parent_doc_id` level, but **identical anchor texts appear across splits: train ∩ test 60 queries (6.0%) / train ∩ validation 50 queries (5.0%)** - the same question is duplicated on different pages or rows, hence under different parent_docs
* No `(anchor, positive)` pair-level leakage (0 rows) - the eval positive always differs from the train positive
* Impact is two-way noise:
  1. **Memorization**: ≈6% of test queries are seen verbatim during training, which may slightly inflate scores
  2. **Qrels false negatives** (more structural): the duplicate question's train positive also lives in the shared corpus but is labeled rel=0 for the eval query (labeling is parent-doc-local), so a model that retrieves that genuinely relevant chunk is unfairly penalized. This extends beyond the 60 queries to any content duplicated across pages - the classic unjudged-relevant problem. See Future Work for the pooling-based remedy

## 2.3. Limitations
* **Domain**: Korean financial services (BC Card products, FAQs, terms, BCAI Q&A) - narrow domain; generalization to other domains not guaranteed
* **Hard-negative leakage**: ≈2% of `train` negatives belong to `validation` / `test` `anchor_parent_doc_id` (HN mining ran pre-split over full corpus, standard BEIR / MTEB practice). For larger split sizes (5k+ each), consider split-aware mining.
* **Lexical overlap bias** (measured 2026-06-12): mean word-level Jaccard of anchor-positive is 0.072 vs anchor-negative 0.032 (≈2.2x) - a trivial lexical matcher resolves ≈73-77% of triplets (train 75.7% / validation 77.0% / test 72.6%). Negatives were mined by embedding similarity, so they are lexically more distant than positives. When evaluating on this dataset, report a BM25 baseline alongside to isolate semantic gains
* **Length / style bias**: measured as negligible - P(len(pos) > len(neg)) ≈ 0.46-0.50 (chance level), and 80.5% of positive-negative pairs share the same source prefix, so neither length nor source style works as a shortcut. Individual triplets may still show large pos-neg length gaps when eyeballing samples - that is natural per-pair variance, not bias: a learnable shortcut requires a directionally consistent correlation across the dataset, which the chance-level P rules out
* **Label (qrels) validity**: relevance grades are distance-based heuristics (not yet LLM/human-verified), and the labeling scope is parent-doc-local - relevant chunks under other parent_docs remain unlabeled (false negatives). To be addressed via pooling-based qrels enrichment (see Future Work)
* **Cross-split duplicate queries**: 6.0% of `test` / 5.0% of `validation` anchor texts also appear verbatim in `train` (same question duplicated across pages); no `(anchor, positive)` pair-level leakage. Consider reporting metrics both with and without these queries

<br>

# 3. Future Work
## 3.1. Surface-signal shortcuts
Planned upgrades to further suppress surface-signal shortcuts (length / lexical / style) and sharpen semantic discrimination:

1. **Lexically-hard negatives** (v4) - mix in BM25-mined negatives (high lexical overlap, wrong meaning) alongside the current embedding-mined ones (semantically close, lexically distant) to close the lexical shortcut measured above. This is a data-side mining change - distinct from serving-side hybrid retrieval (BM25 + dense score fusion), which is a system-level concern outside this dataset
2. **Query style diversification** - reduce the stylistic gap between `base` (real user questions) and `synth` (LLM-generated queries) via paraphrase / backtranslation
3. **LLM-judge label verification** - sample-audit the current distance-based graded relevance labels with an LLM judge
4. **Split-aware HN mining** - eliminate the ≈2% cross-split hard-negative leakage noted in Limitations

## 3.2. Qrels enrichment - pooling-based false-negative recovery
The standard remedy for relevant chunks missed by parent-doc-local labeling is **TREC-style pooling**:

1. Retrieve top-10 for every `validation` / `test` query with multiple retrievers (BM25 + baseline Qwen3-Embedding-0.6B + the fine-tuned model when available)
2. Take the union (pool) of the results and keep only chunks not already in the qrels (typically 5-15 per query)
3. Grade the pooled candidates 0-3 with an LLM judge → add chunks with rel > 0 to the qrels (existing parent-doc-local labels are kept; this is enrichment only)
4. Re-run the `relevant_chunk_ids` / `relevance_scores` enrichment → version bump to Triplet v3.1 (or v4)

This directly fixes the "relevant but labeled rel=0" problem evidenced by the duplicate-query audit finding above. Estimated cost: 2,000 queries × ≈10 candidates ≈ 20k judgments - manageable with a small LLM judge in batch mode. Note that enriching `test` qrels does **not** violate Golden-set discipline: improving label quality raises evaluation validity; what is forbidden is training or hyperparameter selection on `test`.

<br>

# 4. Meta Info
## 4.1. Citation
```bibtex
@dataset{bccard_bcai_finance_kor_embedding_triplet,
  title  = {BCAI Finance Kor Embedding Triplet},
  author = {BC Card AX Team},
  year   = {2026},
  url    = {https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Triplet},
  note   = {Companion corpus: BCCard/BCAI-Finance-Kor-Embedding-Pair}
}
```

## 4.2. See Also
* **Corpus dataset**: [`BCCard/BCAI-Finance-Kor-Embedding-Pair`](https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Pair)
* **Pipeline code**: [MokaGrinder (MoG)](https://github.com/<owner>/mog) - the open-source toolkit that produced this dataset

<br>

