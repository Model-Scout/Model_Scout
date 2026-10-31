---
license: cc-by-4.0
language:
- ko
task_categories:
- sentence-similarity
- text-retrieval
- feature-extraction
size_categories:
- 10K<n<100K
tags:
- finance
- korean
- embedding
- training-corpus
- retrieval-corpus
- instruction-backtranslation
- lumber-chunker
pretty_name: BCAI Finance Kor Embedding Pair
---

# 1. Overview
Korean financial-domain **(anchor, positive) pair** dataset for sentence-embedding model training and as a **retrieval corpus** for evaluation.

This dataset acts in two roles:
1. **Training input** - 45,589 `(anchor, positive)` pairs for in-batch / hard-negative contrastive learning.
2. **Retrieval corpus** - `source_chunk_id` (≈36k unique chunks after q-variant dedupe) is the candidate pool for IR evaluation in the companion [`BCCard/BCAI-Finance-Kor-Embedding-Triplet`](https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Triplet) dataset.

## 1.1. TL;DR
* **45,589 records** - 1 row = (anchor, positive) pair with full chunker metadata
* **36,281 unique `source_chunk_id`** - the retrieval corpus (after dedupe of `q1`/`q2`/`q3` variants)
* **Mixed sources** - BCAI Q&A (BCCard's internal QA) + BC Card website crawl (cards, FAQ, notice, terms)
* **Multi-source chunking** - LumberChunker (LLM-guided semantic boundaries) + Multi-Query Instruction Backtranslation (q1/q2/q3 variants)

## 1.2. Schema
### (1) Columns

| column | type | description |
|--------|------|-------------|
| `anchor` | string | query text - either the raw chunk text (training) or its instruction-backtranslated variant (q1/q2/q3) |
| `positive` | string | doc text (chunker output - the chunk content itself) |
| `source` | string | `base` (BCAI raw) / `synth` (LLM-processed crawl or BCAI) |
| `chunk_id` | string | unique row id (includes `q_variant` suffix) |
| `source_chunk_id` | string | **chunk-level source id (q-variant stripped)** - this is the corpus entry key |
| `chunk_method` | string | `base_skip` / `base_long_llm` / `llm_pipeline` / `faq_direct` |
| `chunk_index` | int | sub-chunk index within `source_chunk_id` |
| `total_chunks` | int | total sub-chunks for this `source_chunk_id` |
| `query_variant` | float | `1.0` / `2.0` / `3.0` (synth q-variant) or `null` (raw) |
| `section_id` / `context_summary` | string | LumberChunker metadata |
| `chunking_config_hash` | string | chunker config hash (reproducibility) |
| `page_type` / `source_url` / `title` / `breadcrumb` | string | crawl metadata (null for BCAI base) |

### (2) `source_chunk_id` - the corpus key

After dedupe of q-variants (1 product = 1 doc text, 3 query variants per chunk), the unique `source_chunk_id` set is the retrieval corpus:

```
crawl_..._credit-card_29000   ← LumberChunker sub-chunk 0 of product 29 (= source)
crawl_..._credit-card_29008   ← sub-chunk 8 of product 29
base_bcai_011324_000          ← BCAI raw row 11324 (no chunking)
crawl_..._faq_197000          ← FAQ direct Q&A (no LLM, self-source)
```

* Trailing number multiple of 1000 = product/article boundary (for `crawl_*`)
* Trailing number = `src_idx * 1000 + sub_chunk_idx` (combined encoding by LumberChunker)
* Companion Triplet dataset's `relevant_chunk_ids` references these `source_chunk_id` values

## 1.3. Quick Start
### (1) As a corpus for retrieval evaluation

```python
from datasets import load_dataset

pair = load_dataset("BCCard/BCAI-Finance-Kor-Embedding-Pair", split="train")

# Build the corpus dict (key = source_chunk_id, value = doc text)
corpus = {}
for r in pair:
    corpus.setdefault(r["source_chunk_id"], r["positive"])

print(f"Corpus size: {len(corpus):,} unique chunks")        # 36,281

# Use with the companion Triplet dataset for IR evaluation
triplet = load_dataset("BCCard/BCAI-Finance-Kor-Embedding-Triplet")
for row in triplet["test"]:
    qrels = dict(zip(row["relevant_chunk_ids"], row["relevance_scores"]))
    # rank corpus by similarity to row["anchor"] / compute NDCG, MRR, Recall, P@1
```

### (2) As contrastive training data

```python
from datasets import load_dataset
from sentence_transformers import SentenceTransformer, losses
from sentence_transformers.training_args import SentenceTransformerTrainingArguments
from sentence_transformers.trainer import SentenceTransformerTrainer

pair = load_dataset("BCCard/BCAI-Finance-Kor-Embedding-Pair", split="train")

# Use anchor / positive only (in-batch negatives)
model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")
loss = losses.MultipleNegativesRankingLoss(model)

# Or use with the companion Triplet dataset (with explicit hard negatives)
triplet = load_dataset("BCCard/BCAI-Finance-Kor-Embedding-Triplet", split="train")
# triplet has (anchor, positive, negative) - explicit hard negatives from FAISS + LLM judge
```

## 1.4. Methodology
### (1) Data pipeline (`hopper` module of [MokaGrinder](https://github.com/<owner>/mog))

```
BCAI Q&A + BC Card site crawl (4 sites: personal/merchant/corporation/VIP)
   ↓ structuring + text-noise removal + PII masking
   ↓ LumberChunker (LLM-guided semantic chunking; dual cap 512/1024 tokens)
   ↓ Multi-Query Instruction Backtranslation (3 query variants per chunk)
   ↓ Cross-source dedupe + integration
This dataset (Pair pool)
   ↓ Hybrid Hard-Negative Mining (FAISS top-K + Claude Sonnet judge)
Companion Triplet dataset (BCCard/BCAI-Finance-Kor-Embedding-Triplet)
```

### (2) Chunking policy

* **LumberChunker** - LLM (Claude Sonnet) detects semantic boundaries within long pages
* **Dual cap** - pass-through chunks ≤ 512 tokens, LLM-based chunks ≤ 1024 tokens (aligned with `MAX_SEQ_LENGTH=1024`)
* **`faq_direct`** - FAQ Q&A pairs bypass LLM (already discrete units)
* **Multi-Query Instruction Backtranslation** - 3 query variants per chunk for instruction-tuned diversity

<br>

# 2. Evaluation
## 2.1. Distribution Stats
### (1) Records per source prefix

| `chunk_id` prefix | records | unique `source_chunk_id` | description |
|-------------------|--------:|-------------------------:|-------------|
| `base_*` | 31,048 | 31,048 | BCAI raw Q&A rows (LLM ✗, 1 row = 1 chunk) |
| `synth_base_*` | 1,737 | 579 | BCAI rows processed by LumberChunker + q-variants |
| `synth_crawl_*` | 12,226 | 4,076 | BC Card crawl processed by LumberChunker + q-variants |
| `crawl_*` (FAQ direct) | 578 | 578 | BC Card FAQ Q&A direct (LLM ✗, 1 Q&A = 1 source) |
| **total** | **45,589** | **36,281** | |

## 2.2. Quality Self-Assessment (LLM-assisted audit)

The dataset was audited with `Claude Fable 5` (2026-06-12): integrity checks (id uniqueness / empty rows / degenerate rows / q-variant consistency / metadata sanity), corpus duplicate-document detection, and cross-dataset referential integrity against the companion Triplet dataset.

**Overall score: 82 / 100** - scored against the bar for public datasets, on the same rubric as the companion Triplet dataset (78/100). Pair scores higher because it carries no relevance labels - the Triplet's weakest pillar does not apply here.

| dimension | score | rationale |
|-----------|-------|-----------|
| Data integrity | 9.5/10 | all 45,589 `chunk_id` unique; 0 empty values; 0 degenerate rows (anchor==positive); `chunk_index` / `total_chunks` consistent |
| Corpus quality | 8/10 | 36,281 unique `source_chunk_id`, exactly 1 doc text per id (q-variant consistent: 0 mismatches); deducted for 1.06% exact-duplicate doc texts (finding below) |
| Cross-dataset referential integrity | 10/10 | every `relevant_chunk_ids` reference in the companion Triplet qrels (validation 830 / test 816 unique chunks) resolves in this corpus - 0 missing |
| Composition & metadata | 9/10 | source distribution matches this card (`base` 32,785 / `synth` 12,804); full chunker metadata incl. `chunking_config_hash` for reproducibility |
| Documentation | 9/10 | Limitations with measured numbers + Future Work |

### (1) Audit finding - corpus exact-duplicate documents

* **1.06% of the corpus (386 chunks in 189 groups) share byte-identical doc text under different `source_chunk_id`** - the same content published on multiple pages (same root cause as the cross-split duplicate queries reported in the companion Triplet dataset)
* Impact on IR evaluation: qrels label specific `source_chunk_id` values, so a model that retrieves an unlabeled twin of a relevant chunk is scored rel=0 despite returning the right content (unjudged-relevant)
* Remedy is shared with the Triplet's pooling-based qrels enrichment plan (duplicate twins get judged and labeled); a corpus-side dedupe by doc text is the alternative for a future version

## 2.3. Limitations
* **Domain**: Korean financial services (BC Card products, FAQs, terms, BCAI Q&A) - narrow domain; generalization to other domains not guaranteed
* **Query style heterogeneity**: `base` anchors are real user questions while `synth` anchors are LLM-generated queries - the two have measurable stylistic differences (see companion Triplet dataset for surface-signal measurements)
* **Corpus duplicate documents**: 1.06% of corpus chunks are byte-identical twins under different ids (see audit finding above) - relevant for IR evaluation against this corpus

<br>

# 3. Future Work
## 3.1. Shared upgrades with the companion Triplet dataset
Planned upgrades shared with the companion Triplet dataset (surface-signal suppression + semantic-signal enrichment):

1. **Query style diversification** - reduce the stylistic gap between `base` (real user questions) and `synth` (LLM-generated queries) via paraphrase / backtranslation
2. **Lexically-hard negatives** (Triplet v4) - BM25-mined negatives built on top of this corpus to close the lexical-overlap shortcut
3. **LLM-judge label verification** - sample-audit of the distance-based graded relevance labels used by the companion Triplet dataset

<br>

# 4. Meta Info
## 4.1. Citation

```bibtex
@dataset{bccard_bcai_finance_kor_embedding_pair,
  title  = {BCAI Finance Kor Embedding Pair},
  author = {BC Card AX Team},
  year   = {2026},
  url    = {https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Pair},
  note   = {Companion evaluation dataset: BCCard/BCAI-Finance-Kor-Embedding-Triplet}
}
```

## 4.2. See Also

* **Triplet (queries + graded labels)**: [`BCCard/BCAI-Finance-Kor-Embedding-Triplet`](https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Triplet)
* **Pipeline code**: [MokaGrinder (MoG)](https://github.com/<owner>/mog)
