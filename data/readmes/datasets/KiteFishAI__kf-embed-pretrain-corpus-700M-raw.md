---
license: mit
language:
  - en
  - hi
  - bn
  - mr
  - ta
  - te
  - gu
  - pa
  - ml
  - kn
  - or
  - as
  - ur
  - ar
  - zh
  - fr
  - de
  - es
  - pt
  - ru
  - ja
  - ko
  - id
  - sw
  - yo
  - fa
  - fi
  - th
  - vi
  - nl
  - it
  - tr
  - pl
  - ro
  - sv
  - da
  - no
  - fi
  - cs
  - sk
  - hr
  - bg
  - uk
  - ms
  - tl
  - ne
  - si
tags:
  - embedding
  - retrieval
  - multilingual
  - indic
  - pretraining
  - contrastive-learning
  - sentence-similarity
  - text-retrieval
  - information-retrieval
  - question-answering
size_categories:
  - 100M<n<1B
task_categories:
  - text-retrieval
  - sentence-similarity
  - feature-extraction
pretty_name: KF-Embed Pretrain Corpus 700M
dataset_info:
  - config_name: default
    splits:
      - name: train
        num_examples: 710388432
---

# KF-Embed Pretraining Corpus

<div align="center">

**710 Million (query, positive) pairs · 128 GB · 50+ Languages · 16 Sources**

*Pretraining data for [Minnow-Em-v1](https://huggingface.co/KiteFishAI/Minnow-Em-v1) — part of KiteFishAI's Minnow family of sovereign small language models*

[![KiteFishAI](https://img.shields.io/badge/KiteFishAI-kitefishai.com-orange?style=flat-square)](https://kitefishai.com)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](https://opensource.org/licenses/MIT)
[![Records](https://img.shields.io/badge/Records-710M-green?style=flat-square)]()
[![Size](https://img.shields.io/badge/Size-128%20GB-purple?style=flat-square)]()

</div>

---

## Overview

This dataset is the **stage-1 pretraining corpus** used to train **[Minnow-Em-v1](https://huggingface.co/KiteFishAI/Minnow-Em-v1)**, KiteFishAI's multilingual embedding model and part of the **Minnow family** of sovereign small language models (SLMs). It aggregates 16 diverse open-source datasets into a unified collection of `(query, positive)` pairs spanning web text, scientific literature, code, multilingual news, Wikipedia, Q&A pairs, and Indian regional language content.

The corpus is specifically designed to support contrastive pretraining of multilingual embedding models with strong coverage of **Indic languages** (Hindi, Bengali, Marathi, Tamil, Telugu, Gujarati, Punjabi, Malayalam, Kannada, Odia, and more) alongside broad multilingual and English-language coverage.

Each record follows a simple, consistent schema:

```json
{
  "source": "dataset_name",
  "query": "...",
  "positive": "..."
}
```

---

## Dataset Statistics

| File | Records | Size (GB) | Domain | Language(s) |
|------|--------:|----------:|--------|-------------|
| `amazon_user_reviews.jsonl` | 571,497,789 | 88.14 | E-commerce reviews | English |
| `s2orc.jsonl` | 51,030,086 | 11.66 | Scientific literature | English |
| `paq_pairs.jsonl` | 64,371,441 | 10.00 | Q&A pairs | English |
| `xP3all.jsonl` | 9,200,000 | 9.10 | Instruction following | 46 languages |
| `wikipedia.jsonl` | 6,407,814 | 2.28 | Encyclopedic | English |
| `arxiv.jsonl` | 2,989,022 | 3.42 | Scientific abstracts | English |
| `hindi.jsonl` | 333,242 | 1.62 | News articles | Hindi |
| `tamil_news.jsonl` | 300,000 | 1.07 | News articles | Tamil |
| `codesearchnet.jsonl` | 1,880,853 | 2.01 | Code + docstrings | 6 prog. languages |
| `swim-ir-monolingual.jsonl` | 902,504 | 0.83 | IR passages | 10 languages |
| `multilingual_cc_news.jsonl` | 154,086 | 0.45 | News | 100+ languages |
| `telugu_news.jsonl` | 102,332 | 0.35 | News articles | Telugu |
| `swim-ir-cross-lingual.jsonl` | 850,000 | 0.14 | Cross-lingual IR | 17 languages |
| `bengaliNews.jsonl` | 114,434 | 0.10 | News articles | Bengali |
| `marathi.jsonl` | 99,957 | 0.26 | Instruction Q&A | Marathi |
| `refinedweb.jsonl` | 154,872 | 0.29 | Web crawl | English |
| **Total** | **710,388,432** | **128** | | |

---

## Source Datasets

| # | Source | HuggingFace / Origin | Query Field | Positive Field |
|---|--------|----------------------|-------------|----------------|
| 1 | Amazon Reviews 2023 | `McAuley-Lab/Amazon-Reviews-2023` | Review title | Review text |
| 2 | Semantic Scholar ORC | `sentence-transformers/s2orc` | Paper title | Citation text |
| 3 | PAQ Pairs | `embedding-data/PAQ_pairs` | Question | Answer |
| 4 | xP3all | `bigscience/xP3all` | Prompt input | Target output |
| 5 | Wikipedia (EN) | `wikimedia/wikipedia` | Article title | First section |
| 6 | ArXiv | Cornell University / Kaggle | Paper title | Abstract |
| 7 | Hindi News | `harshitkaran/Hindi` | Headline | Article |
| 8 | Tamil News | `livinNector/tamil_news_dataset` | News title | Article |
| 9 | CodeSearchNet | `code-search-net/code_search_net` | Docstring | Function code |
| 10 | SWIM-IR Monolingual | `nthakur/swim-ir-monolingual` | Query | Passage |
| 11 | Multilingual CC News | `intfloat/multilingual_cc_news` | Title | Main text |
| 12 | Telugu News | `saidines12/telugu_news_dataset` | Headline | Article |
| 13 | SWIM-IR Cross-Lingual | `nthakur/swim-ir-cross-lingual` | Language | Query |
| 14 | Bengali News | `Hiraishin/BengaliNews` | Headline | Highlights |
| 15 | Marathi Orca | `amitagh/marathi-orca-v05` | Question (Mar) | Response (Mar) |
| 16 | Falcon RefinedWeb | `andersonbcdefg/falcon-refinedweb-labeled` | URL-derived title | Web content |

---

## Language Coverage

### Indic Languages (native coverage)
`Hindi` · `Bengali` · `Marathi` · `Tamil` · `Telugu` · `Gujarati` · `Punjabi` · `Malayalam` · `Kannada` · `Odia` · `Assamese` · `Urdu` · `Nepali` · `Sinhala`

### Other Languages (via multilingual subsets)
`Arabic` · `Chinese` · `French` · `German` · `Spanish` · `Portuguese` · `Russian` · `Japanese` · `Korean` · `Indonesian` · `Swahili` · `Yoruba` · `Persian` · `Finnish` · `Thai` · `Vietnamese` · `Dutch` · `Italian` · `Turkish` · `Polish` · `Romanian` · and 80+ more via `multilingual_cc_news` and `xP3all`.

---

## Data Format

All files are in **JSONL** format (one JSON object per line). Each record contains:

```json
{
  "source": "wikipedia_20231101_en",
  "query": "Quantum entanglement",
  "positive": "Quantum entanglement is a phenomenon where two particles become interconnected..."
}
```

- `source` — identifier of the originating dataset and subset
- `query` — short anchor text (title, headline, question, docstring, etc.)
- `positive` — longer associated passage (article body, answer, code, abstract, etc.)

---

## Intended Use

This corpus is intended for:

- **Contrastive pretraining** of embedding models like Minnow-Em-v1 (e.g., using InfoNCE / NT-Xent losses)
- **Multilingual dense retrieval** model training
- **Sentence similarity** and **semantic search** model development
- **Indic NLP** research requiring large-scale multilingual training data

It is **not** intended for:
- Direct use as a question-answering or generative LLM training corpus
- Any use that violates the licenses of the constituent source datasets

---

## Preprocessing Notes

- **Amazon Reviews**: User reviews and item metadata are processed separately. Review title → text as query → positive pairs.
- **Wikipedia**: Only the first section (before first double newline) is used as the positive to avoid very long documents.
- **ArXiv**: Title → abstract pairs. Text is whitespace-normalized and stripped.
- **RefinedWeb**: URL paths are parsed and cleaned into human-readable titles as the query field.
- **CodeSearchNet**: Source language is encoded in the `source` field (e.g., `codesearch_python`).
- **Multilingual CC News**: Subsets exceeding 10,000 records are capped at 10,000 per language to maintain balance.
- **SWIM-IR**: Cross-lingual subsets are capped at 50,000 per language; monolingual at 100,000 per language.
- **xP3all**: Capped at 200,000 records per language subset.
- **Tamil News**: Capped at 300,000 records.

---

## Citation

If you use this dataset, please cite KiteFishAI and the respective source datasets:

```bibtex
@dataset{kitefishai_kfembed_corpus_2026,
  author       = {KiteFishAI},
  title        = {KF-Embed Pretraining Corpus},
  year         = {2026},
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/KiteFishAI/kf-embed-pretrain-corpus-700M},
  note         = {Aggregated pretraining corpus for KF-Embed multilingual embedding models. 710M (query, positive) pairs across 16 source datasets.}
}
```

Please also cite the individual source datasets as appropriate (McAuley-Lab Amazon Reviews 2023, Semantic Scholar ORC, PAQ, xP3, WikiMedia, ArXiv, CodeSearchNet, SWIM-IR, Falcon RefinedWeb, and regional news datasets).

---

## License

This dataset is released under the [MIT License](https://opensource.org/licenses/MIT). Individual source datasets retain their original licenses. Users are responsible for ensuring compliance with the licenses of constituent sources before use in downstream applications.

---

## About KiteFishAI

[KiteFishAI](https://kitefishai.com) builds sovereign, domain-specific small language models (SLMs) fine-tuned for Indian BFSI, healthcare, and pharma verticals. All SLMs are part of the **Minnow family** — including Minnow-Math-1.5B, Minnow-Math-2B, and Minnow-Em-v1 (embedding). The Minnow series is designed for air-gapped, on-premise enterprise deployments with strong Indic language coverage.

- 🌐 [kitefishai.com](https://kitefishai.com)
- 🤗 [huggingface.co/KiteFishAI](https://huggingface.co/KiteFishAI)