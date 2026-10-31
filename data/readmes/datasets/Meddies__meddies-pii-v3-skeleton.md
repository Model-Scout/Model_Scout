---
pretty_name: Meddies PII v3 Skeletons
language:
- vi
- en
- zh
- ja
- ko
- th
- lo
- my
- km
- ta
- fil
- ms
- id
- jv
- su
- pt
- es
- fr
- de
- ru
license: cc-by-nc-4.0
annotations_creators:
- machine-generated
language_creators:
- machine-generated
multilinguality: multilingual
configs:
- config_name: vi
  data_files:
  - split: train
    path: vi/train-*
- config_name: en
  data_files:
  - split: train
    path: en/train-*
- config_name: zh
  data_files:
  - split: train
    path: zh/train-*
- config_name: ja
  data_files:
  - split: train
    path: ja/train-*
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*
- config_name: th
  data_files:
  - split: train
    path: th/train-*
- config_name: lo
  data_files:
  - split: train
    path: lo/train-*
- config_name: my
  data_files:
  - split: train
    path: my/train-*
- config_name: km
  data_files:
  - split: train
    path: km/train-*
- config_name: ta
  data_files:
  - split: train
    path: ta/train-*
- config_name: fil
  data_files:
  - split: train
    path: fil/train-*
- config_name: ms
  data_files:
  - split: train
    path: ms/train-*
- config_name: id
  data_files:
  - split: train
    path: id/train-*
- config_name: jv
  data_files:
  - split: train
    path: jv/train-*
- config_name: su
  data_files:
  - split: train
    path: su/train-*
- config_name: pt
  data_files:
  - split: train
    path: pt/train-*
- config_name: es
  data_files:
  - split: train
    path: es/train-*
- config_name: fr
  data_files:
  - split: train
    path: fr/train-*
- config_name: de
  data_files:
  - split: train
    path: de/train-*
- config_name: ru
  data_files:
  - split: train
    path: ru/train-*
size_categories:
- 1K<n<10K
---

# Meddies PII v3 — Skeleton Corpus

Typed-placeholder document skeletons for multilingual synthetic PII/PHI
training data. Every PII-shaped slot is a `⟦label.subtype#id⟧` placeholder —
no real values exist in this corpus by construction. A deterministic filler
substitutes values downstream.

- **350,174 documents · 20 languages** (incl. Khmer, Javanese, Sundanese)
- 9 coarse labels: address, company_name, date, email_address, human_name,
  id_number, phone_number, private_url, secret — plus `op:`/`neg:`/`trap:`/
  `link:`/`frag`/`mod` annotations for contextual judgments
- Generated across 16 free-tier provider lanes via meddies-llm-runtime
- `accepted`/`violations` flag contract quality; `provenance` marks
  corpus/pilot/matrix/smoke; `content_sha256` dedupes

Sister dataset to Meddies/meddies-pii (filled/labelled corpus). Generated
2026-09 by the meddies-pii v3 pipeline.
