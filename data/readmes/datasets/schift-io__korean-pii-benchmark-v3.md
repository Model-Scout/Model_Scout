---
language: ko
license: cc-by-sa-4.0
task_categories:
  - token-classification
tags:
  - pii
  - korean
  - ner
  - de-identification
  - benchmark
size_categories:
  - n<1K
---

# Korean PII Benchmark v3

**473 cases for evaluating Korean PII (person, organization, address) detection models.**

Covers court judgments, news articles, administrative documents, medical/insurance records, transcripts, and negative examples (law names, case numbers, titles that should NOT be detected).

## Entity Distribution

| Entity | Spans |
|---|---|
| private_person | 411 |
| private_organization | 182 |
| private_address | 141 |
| private_phone | 65 |
| (negative) | 59 |

## Categories

| Category | Count | Description |
|---|---|---|
| person_court | 60 | Court judgment style (plaintiff, defendant, witness) |
| person_news | 40 | News article style |
| person_admin | 30 | Administrative/civil petition style |
| person_short | 10 | 2-character names |
| person_double_surname | 7 | Double surnames (남궁, 제갈, etc.) |
| person_foreign | 8 | Foreign names |
| org_* | 60 | Organization patterns (주식회사, (주), 법인, banks, bare) |
| address_only | 20 | Address-only cases |
| complex | 30 | Mixed person + org + address |
| medical_insurance | 30 | Hospital/insurance domain |
| transcript | 30 | Transcription/verbatim style |
| negative | 48 | Law names, case numbers, titles (should NOT be detected) |
| T01-T12, N01-N04 | 100 | 창녕군 administrative patterns (contributed by 지방자치혁신연구원) |

## Format

JSONL, one case per line:


 gives the entity surface form.

## Sources

- Synthetic cases based on real Korean court judgment, news, and administrative document patterns
- 창녕군 정보공개청구 데이터 기반 합성 데이터 (contributed by 지방자치혁신연구원, 출처 표기)
- KLUE NER (CC-BY-SA-4.0) entity patterns

## License

CC-BY-SA-4.0
