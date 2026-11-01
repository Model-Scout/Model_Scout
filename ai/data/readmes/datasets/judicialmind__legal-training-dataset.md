---
license: cc-by-nc-nd-4.0
task_categories:
  - text-retrieval
  - question-answering
  - sentence-similarity
language:
  - ar
  - bg
  - zh
  - hr
  - cs
  - da
  - nl
  - en
  - et
  - fi
  - fr
  - de
  - el
  - hi
  - hu
  - ga
  - it
  - ko
  - lv
  - lt
  - mt
  - pl
  - pt
  - ro
  - ru
  - sk
  - sl
  - es
  - sv
  - th
  - tr
  - vi
size_categories:
  - 1M<n<10M
tags:
  - legal
  - law
  - legal-nlp
  - legaltech
  - legal-ai
  - legal-research
  - legal-ir
  - case-law
  - judiciary
  - judicial
  - jurisprudence
  - statutes
  - regulations
  - contracts
  - compliance
  - litigation
  - dispute-resolution
  - odr
  - adr
  - multilingual
  - cross-lingual
  - retrieval
  - dense-retrieval
  - semantic-search
  - question-answering
  - rag
  - information-retrieval
  - text-similarity
  - jurisdiction
  - legal-reasoning
pretty_name: JudicialMind Legal Training Dataset
---

# JudicialMind Legal Training Dataset

A large-scale, multilingual **query–passage** corpus for training and evaluating
**legal information-retrieval** and **question-answering** systems.

- **3.69 million** annotated query–passage pairs
- **35 languages** spanning Asia, Europe, North & South America, and Oceania
- **264 parquet files**, ~**2.6 GB** on disk
- File-level **A / B / C bucket split** for clean train / validation / test partitioning
- Rich metadata per row: `query_type`, `legal_domain`, `difficulty`, `jurisdiction`, `token_count`, …

> Use this dataset to fine-tune dense retrievers (BGE / E5 / GTE / Multilingual-E5),
> reranker cross-encoders, multilingual legal-QA LLMs, and to benchmark RAG pipelines
> for legal use-cases.

---

## 📐 Schema

| Column | Type | Description |
|---|---|---|
| `chunk_id` | string | Unique identifier for the text chunk |
| `doc_id` | string | Parent document identifier |
| `query` | string | Legal query (synthetic or curated) |
| `positive` | string | Passage that answers / is relevant to the query |
| `query_type` | string | One of: `application`, `procedural`, `interpretation`, `statutory`, `comparative`, `scenario`, `edge_case`, `definition` |
| `legal_domain` | string | Area of law (e.g. constitutional, contract, criminal, tax, IP, …) |
| `difficulty` | string | `easy` · `medium` · `hard` |
| `token_count` | int | Approx. token count of the positive passage |
| `bucket` | string | Split bucket: `A`, `B`, or `C` (file-level partition) |
| `language` | string | Row language (e.g. `english`, `hindi`, …) |
| `country` | string | ISO-style country code (`IN`, `US`, `EU`, …) |
| `jurisdiction` | string | Legal jurisdiction label |

### Bucket split

| Bucket | Files | Suggested use |
|---|---:|---|
| **A** | 89 | Primary training partition |
| **B** | 88 | Validation / additional training |
| **C** | 87 | Held-out evaluation / test |

Splits are applied **per underlying corpus**, so each bucket keeps proportional
representation across languages, jurisdictions, and legal domains.

---

## 🌐 Language & Jurisdiction Coverage

| Language | Jurisdictions | Files | Size |
|---|---|---:|---:|
| Arabic | EG | 3 | 14 MB |
| Bulgarian | EU | 6 | 5.6 MB |
| Chinese | CN | 9 | 61 MB |
| Croatian | EU | 6 | 4.7 MB |
| Czech | EU | 6 | 4.7 MB |
| Danish | EU | 3 | 2.6 MB |
| Dutch | EU | 6 | 20 MB |
| English (India) | IN | 6 | 456 MB |
| English (USA) | US | 42 | 1.1 GB |
| English (World) | AU, CA, EU, IE, UK | 27 | 422 MB |
| Estonian | EU | 6 | 5.3 MB |
| Finnish | EU | 6 | 5.5 MB |
| French | BE, EU, FR | 15 | 43 MB |
| German | CH, EU | 12 | 59 MB |
| Greek | EU, GR | 9 | 7.2 MB |
| Hindi | IN | 6 | 131 MB |
| Hungarian | EU | 6 | 4.6 MB |
| Irish | IE | 6 | 9.6 MB |
| Italian | EU, IT | 12 | 30 MB |
| Korean | KR | 6 | 55 MB |
| Latvian | EU | 6 | 4.8 MB |
| Lithuanian | EU | 6 | 4.8 MB |
| Maltese | EU | 6 | 4.8 MB |
| Polish | EU | 6 | 21 MB |
| Portuguese | BR | 3 | 70 MB |
| Romanian | EU | 6 | 5.0 MB |
| Russian | RU | 3 | 19 MB |
| Slovak | EU | 6 | 5.0 MB |
| Slovenian | EU | 6 | 5.0 MB |
| Spanish | EU | 3 | 9.9 MB |
| Swedish | EU | 6 | 5.0 MB |
| Thai | TH | 3 | 8.2 MB |
| Turkish | TR | 3 | 6.5 MB |
| Vietnamese | VN | 3 | 8.7 MB |
| **Total** | — | **264** | **~2.6 GB** |

---

## 📁 File Layout

```
├── arabic/eg/
├── bulgarian/eu/
├── chinese/cn/
├── english_india/in/
├── english_usa/us/
├── english_world/{au,ca,eu,ie,uk}/
├── french/{be,eu,fr}/
├── german/{ch,eu}/
├── greek/{eu,gr}/
├── hindi/in/
├── italian/{eu,it}/
├── ...
└── vietnamese/vn/
```

Each language directory contains jurisdiction subdirectories with parquet files
named `{dataset}_{A|B|C}.parquet`.

---

## 🚀 Quick Start

```python
from datasets import load_dataset

# 1. Load everything
ds = load_dataset("judicialmind/legal-training-dataset")

# 2. Stream a single language (recommended for fast iteration)
ds = load_dataset(
    "judicialmind/legal-training-dataset",
    data_files="english_usa/**/*.parquet",
    streaming=True,
)

# 3. Use bucket A as the train split
ds_train = load_dataset(
    "judicialmind/legal-training-dataset",
    data_files="**/*_A.parquet",
)
ds_val = load_dataset(
    "judicialmind/legal-training-dataset",
    data_files="**/*_B.parquet",
)
ds_test = load_dataset(
    "judicialmind/legal-training-dataset",
    data_files="**/*_C.parquet",
)
```

### Direct file access

```
https://huggingface.co/datasets/judicialmind/legal-training-dataset/resolve/main/<path>.parquet
```

### Git clone

```bash
git lfs install
git clone https://huggingface.co/datasets/judicialmind/legal-training-dataset
```

---

## 🎯 Suggested Use Cases

- Fine-tune **multilingual dense retrievers** (e.g. `intfloat/multilingual-e5-large`, `BAAI/bge-m3`) for legal IR.
- Train **cross-encoder rerankers** on (query, positive) + mined hard-negatives.
- Build **multilingual legal RAG** with cross-jurisdiction grounding.
- Probe **legal-domain LLMs** for procedural / interpretive / statutory reasoning.
- Stress-test on `difficulty=hard` and `query_type=edge_case` for OOD evaluation.

---

## ⚠️ Limitations

- Queries are partly **synthetically generated**; verify suitability for compliance-critical tasks.
- Coverage is **uneven** across languages — English (USA) dominates by volume.
- Jurisdictional labels follow source granularity (e.g. EU-wide vs. member-state vs. court level).
- This is **not legal advice**; consult primary sources and qualified counsel for real cases.

---

## 📜 License

Released under **cc-by-nc-nd-4.0**. Underlying source texts remain governed by their
original licences (most are public-domain government / court materials, but
verify per jurisdiction before redistribution).

---

## 🧑‍⚖️ Citation

```bibtex
@misc{judicialmind_legal_training_2026,
  title  = {JudicialMind Legal Training Dataset: A Multilingual Corpus for Legal Retrieval and QA},
  author = {JudicialMind},
  year   = {2026},
  url    = {https://huggingface.co/datasets/judicialmind/legal-training-dataset}
}
```

## 🔗 Related

- 🤗 [`judicialmind/india-acts`](https://huggingface.co/datasets/judicialmind/india-acts) — raw PDF corpus of Indian central + state acts (English & Hindi, ~22 GB).
