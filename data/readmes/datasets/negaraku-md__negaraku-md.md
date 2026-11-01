---
license: cc-by-sa-4.0
language:
- ms
- en
- zh
- ta
- ja
- ko
- th
- vi
- id
- ar
- hi
- es
- fr
multilinguality:
- multilingual
language_creators:
- expert-generated
- machine-generated
annotations_creators:
- expert-generated
- machine-generated
pretty_name: NegaraKu.md — Malaysia Knowledge Base
tags:
- malaysia
- southeast-asia
- knowledge-base
- multilingual
- parallel-corpus
- cross-lingual
- rag
- question-answering
- government
- law
- taxation
- finance
- culture
task_categories:
- text-generation
- question-answering
- text-retrieval
- translation
- summarization
size_categories:
- 10K<n<100K
source_datasets:
- original
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*.jsonl
- config_name: ms
  data_files:
  - split: train
    path: data/ms.jsonl
- config_name: en
  data_files:
  - split: train
    path: data/en.jsonl
- config_name: zh
  data_files:
  - split: train
    path: data/zh.jsonl
- config_name: ta
  data_files:
  - split: train
    path: data/ta.jsonl
- config_name: ja
  data_files:
  - split: train
    path: data/ja.jsonl
- config_name: ko
  data_files:
  - split: train
    path: data/ko.jsonl
- config_name: th
  data_files:
  - split: train
    path: data/th.jsonl
- config_name: vi
  data_files:
  - split: train
    path: data/vi.jsonl
- config_name: id
  data_files:
  - split: train
    path: data/id.jsonl
- config_name: ar
  data_files:
  - split: train
    path: data/ar.jsonl
- config_name: hi
  data_files:
  - split: train
    path: data/hi.jsonl
- config_name: es
  data_files:
  - split: train
    path: data/es.jsonl
- config_name: fr
  data_files:
  - split: train
    path: data/fr.jsonl
---

# NegaraKu.md — an open, AI-friendly knowledge base about Malaysia

**15,054 rows** — **1,158 articles in each of 13 languages** (`ms`: 1158 · `en`: 1158 · `zh`: 1158 · `ta`: 1158 · `ja`: 1158 · `ko`: 1158 · `th`: 1158 · `vi`: 1158 · `id`: 1158 · `ar`: 1158 · `hi`: 1158 · `es`: 1158 · `fr`: 1158) — covering
government, law, taxation, business, companies, culture, geography, history,
healthcare, education, and daily life in Malaysia. Every article is
human-reviewable, cited, and released under a permissive licence so it can be
used freely for training, retrieval-augmented generation, and research.

This dataset is the open-data mirror of the website
[negaraku.md](https://negaraku.md). The mission is simple: **let the world — and AI — know
about Malaysia**, from primary and authoritative sources.

> **Parallel corpus.** The 13 languages are fully aligned: each of the
> 1,158 articles exists in every language and the versions share a
> `topic_id`. That makes this a ready-made **cross-lingual / machine-translation**
> resource for Malay, Chinese, Tamil and nine other languages — not just a
> monolingual knowledge base. See [Cross-lingual use](#cross-lingual-use).

## Dataset structure

- **Splits:** one `train` split. Load all languages with the `default` config, or
  one language via its config name (`en`, `zh`, …).
- **Rows:** 15,054 total, 1,158 per language.
- **Alignment:** rows with the same `topic_id` are the same article in different
  languages.

### Fields

| field | description |
|---|---|
| `id` | stable id — `<topic_id>.<language>` |
| `topic_id` | topic id shared across an article's language versions (the alignment key) |
| `title` | article title |
| `summary` | one-paragraph summary |
| `answer` | the concise, liftable direct answer (may be empty) |
| `key_takeaways` | list of the key points |
| `category` / `subcategory` | taxonomy |
| `tier` | editorial importance tier |
| `content_type` | e.g. guide, place, concept |
| `language` | `ms` · `en` · `zh` · `ta` · `ja` · `ko` · `th` · `vi` · `id` · `ar` · `hi` · `es` · `fr` |
| `url` | canonical URL on negaraku.md |
| `entity` | the primary entity the article is about |
| `wikidata` | the entity's Wikidata QID, when known (5,330 rows) — links each article to the global knowledge graph |
| `sources` | list of `{title, url, publisher, date}` citations |
| `updated` | last-updated date (`YYYY-MM-DD`) |
| `content` | the full article body in Markdown |
| `license` | `CC-BY-SA-4.0` |

### Example (one row, trimmed)

```json
{
  "id": "MY-ACC-0028.en",
  "topic_id": "MY-ACC-0028",
  "title": "Audit Exemption for Private Companies: Do You Qualify?",
  "summary": "SSM Practice Directive 10/2024 lets certain Sdn Bhd companies skip the statutory audit if they meet two of three thresholds (revenue, assets, employees) that rise in stages from 1 January 2025. This guide explains the threshold for each phase, the precise definitions, the exclusions, and the filing duties that still apply.",
  "answer": "A private company qualifies for audit exemption under SSM Practice Directive 10/2024 if it meets at least two of three criteria for the current financial year and the two preceding financial years: annual revenue, total assets, and number of employees. The thresholds rise in stages over three years — RM1 million/10 employees (Phase 1, 2025), RM2 million/20 employees (Phase 2, 2026), and RM3 million/30 employees (Phase 3, 2027). Public companies, subsidiaries of public companies, exempt private companies that opt to lodge a certificate under section 260, and foreign companies do not qualify. Even when exempt from audit, a company must still file unaudited financial statements together with a certificate to SSM.",
  "key_takeaways": [
    "Qualifies if it meets 2 of 3 criteria (revenue, assets, employees) for the current year and the two preceding years.",
    "Thresholds rise in stages: RM1 million/10 employees (2025), RM2 million/20 employees (2026), RM3 million/30 employees (2027)."
  ],
  "keywords": [
    "pengecualian audit",
    "audit exemption",
    "PD 10/2024",
    "Arahan Amalan 10/2024",
    "Sdn Bhd",
    "syarikat persendirian",
    "SSM",
    "seksyen 267",
    "penyata kewangan tidak diaudit"
  ],
  "category": "accounting",
  "subcategory": [
    "audit"
  ],
  "tier": "1",
  "content_type": "guide",
  "language": "en",
  "url": "https://negaraku.md/en/accounting/audit-exemption-criteria/",
  "entity": "Suruhanjaya Syarikat Malaysia (SSM)",
  "wikidata": "Q1121232",
  "sources": [
    {
      "title": "Practice Directive No. 10/2024 — Qualifying Criteria for Audit Exemption for Certain Private Companies in Malaysia",
      "url": "https://www.ssm.com.my/Pages/Legal_Framework/Document/PRACTICE-DIRECTIVE-10-2024.pdf",
      "publisher": "Suruhanjaya Syarikat Malaysia (SSM)",
      "date": ""
    }
  ],
  "license": "CC-BY-SA-4.0",
  "updated": "2026-08-14",
  "content": "For years, nearly every Sdn Bhd in Malaysia was forced to appoint an auditor — regardless of whether it was a one-person retail shop or a factory. At the end of 2023, there were …"
}
```

## Usage

```python
from datasets import load_dataset

# all languages
ds = load_dataset("negaraku-md/negaraku-md", split="train")

# a single language
en = load_dataset("negaraku-md/negaraku-md", "en", split="train")
```

### Cross-lingual use

Because the corpus is parallel, you can align any two languages on `topic_id`
to build translation / cross-lingual pairs:

```python
import pandas as pd
from datasets import load_dataset

en = load_dataset("negaraku-md/negaraku-md", "en", split="train").to_pandas().set_index("topic_id")
ms = load_dataset("negaraku-md/negaraku-md", "ms", split="train").to_pandas().set_index("topic_id")

pairs = en[["title", "summary"]].join(
    ms[["title", "summary"]], lsuffix="_en", rsuffix="_ms"
)
print(pairs[["title_en", "title_ms"]].head())
```

## Languages

`ms` · `en` · `zh` · `ta` · `ja` · `ko` · `th` · `vi` · `id` · `ar` · `hi` · `es` · `fr` — Bahasa Melayu (`ms`) is the default and serves at the site root.
It spans high- and lower-resource languages (e.g. Tamil `ta`, Thai `th`,
Vietnamese `vi`, Arabic `ar` — right-to-left), each a full translation of the
same 1,158 articles.

## Uses

- **RAG / retrieval** over authoritative Malaysia content (use `content`, cite `url`).
- **Question answering** — `answer` and `key_takeaways` are written to be liftable.
- **Training / fine-tuning** a Malaysia-aware or multilingual model.
- **Machine translation & cross-lingual** research via the `topic_id` alignment.

## Limitations & responsible use

- Articles are **AI-drafted from authoritative sources and human-reviewable**,
  not authored by subject-matter experts end-to-end. Verify against the cited
  primary `sources` before relying on them for legal, tax, medical or other
  high-stakes decisions — the content is **informational, not professional advice**.
- Coverage reflects editorial priorities and will have gaps; `updated` shows
  recency, and figures or laws may change after that date.
- Translations are produced with AI assistance; the `ms`/`en` masters are the
  most authoritative where wording matters.

## Licence & attribution

Released under [Creative Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
You may share and adapt for any purpose, including commercially, with
attribution and share-alike. Please credit **NegaraKu.md** and link back to the
source `url`.

## Provenance

Content is AI-drafted from authoritative Malaysian sources (government
agencies, statutes, regulators) and organisation-published, with per-article
citations in the `sources` field. It corresponds to the
[Wikidata item Q141449495](https://www.wikidata.org/wiki/Q141449495).

## Citation

```bibtex
@misc{negarakumd,
  title  = {NegaraKu.md — an open, AI-friendly knowledge base about Malaysia},
  author = {NegaraKu.md},
  url    = {https://negaraku.md},
  note   = {Licensed under CC BY-SA 4.0}
}
```
