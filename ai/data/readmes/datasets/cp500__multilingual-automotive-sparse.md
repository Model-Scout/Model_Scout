---
license: apache-2.0
task_categories:
  - sentence-similarity
  - text-retrieval
language:
  - en
  - ja
  - ko
size_categories:
  - 10K<n<100K
tags:
  - splade
  - sparse-retrieval
  - cross-lingual
  - automotive
  - supply-chain
pretty_name: Multilingual Automotive Sparse Retrieval Corpus
---

# Multilingual Automotive Sparse Retrieval Corpus

A synthetic training corpus for fine-tuning multilingual sparse retrieval
models (SPLADE-family) on automotive, supply-chain, and geopolitics content.
Designed to teach a model cross-lingual alignment: a Japanese query should
retrieve the right English passage, and vice versa.

## Corpus contents

| File | Rows | Purpose |
|------|------|---------|
| `concepts.jsonl` | 4995 | Raw concept records |
| `train_triplets.jsonl` | 134880 | Flattened (query, positive, negative) triplets |
| `eval_pairs.jsonl` | 4491 | Held-out 10% for retrieval evaluation |

## Concept record schema (`concepts.jsonl`)

```json
{
  "query":          {"en": str, "ja": str, "ko": str},
  "positive":       {"en": str, "ja": str, "ko": str},
  "hard_negatives": [{"en": str, "ja": str, "ko": str}, × 5],
  "easy_negative":  {"en": str},
  "_meta": {
    "concept_id": str,
    "category": str,
    "tags": [str],
    "subject": str, "predicate": str, "object": str,
    "model": "us.anthropic.claude-haiku-4-5-20251001-v1:0",
    "usage": {"input_tokens": int, "output_tokens": int, ...}
  }
}
```

## Training triplet schema (`train_triplets.jsonl`)

```json
{
  "query": str,
  "positive": str,
  "negative": str,
  "query_lang": "en"|"ja"|"ko",
  "positive_lang": "en"|"ja"|"ko",
  "negative_lang": "en"|"ja"|"ko",
  "concept_id": str,
  "category": str,
  "negative_kind": "hard"|"easy",
  "negative_rank": int
}
```

Each concept fans out into up to 30 training triplets covering all 9
query×positive language-pair combinations, with hard negatives preferentially
matching the query language.

## Category distribution

| category | count |
|----------|-------|
| energy_commodities | 850 |
| pharma_biotech | 843 |
| semiconductors_hardware | 842 |
| geopolitics_defense | 840 |
| automotive_mobility | 828 |
| finance_capital_markets | 792 |

## Generation method

Records were synthesized via **Anthropic Claude Haiku 4.5** on AWS Bedrock,
using a deterministic stratified sample of 2500 concept seeds drawn from
8 automotive / supply-chain / geopolitics scenarios. The
model was prompted to produce faithful translations across EN/JA/KO with
native hard-negative phrasing (not translated-from-English).

### Hard negative taxonomy

Each concept has 5 hard negatives, deliberately varied:
1. Same entity / different action
2. Similar action / different entity
3. Same region / unrelated industry
4. Similar entity + topic / different polarity or timeframe
5. Adjacent domain

## Usage

```python
from datasets import load_dataset

# Full corpus
ds = load_dataset("cp500/multilingual-automotive-sparse")

# Training triplets only
triplets = load_dataset("cp500/multilingual-automotive-sparse", data_files="train_triplets.jsonl")

# Held-out eval pairs
eval_ = load_dataset("cp500/multilingual-automotive-sparse", data_files="eval_pairs.jsonl")
```

## Intended use

- Fine-tuning multilingual SPLADE / sparse retrieval models (MarginMSE,
  contrastive loss, in-batch negatives).
- Cross-lingual retrieval research: measure whether models learn
  lexical-vocab-space alignment across scripts.
- FLOPS-regularization experiments in the automotive-intelligence domain.

## Limitations

- All passages are **synthetic** — companies, dollar amounts, and events are
  plausible but fictional. Not suitable for factual question answering.
- Machine-generated CJK may have occasional register issues — native-speaker
  review has not been performed.
- Domain is narrow (automotive / supply chain / geopolitics). Performance on
  out-of-domain text will require additional corpora.

## License

Apache 2.0. Generated with Anthropic Claude — users should review Anthropic's
[Acceptable Use Policy](https://www.anthropic.com/legal/aup) for downstream
applications.

## Citation

```bibtex
@misc{cp500-multilingual-automotive-sparse-2026,
  author = {Charles P},
  title  = {Multilingual Automotive Sparse Retrieval Corpus},
  year   = {2026},
  publisher = {HuggingFace},
  url    = {https://huggingface.co/datasets/cp500/multilingual-automotive-sparse}
}
```
