---
language:
- ko
license: apache-2.0
task_categories:
- question-answering
- text-retrieval
task_ids:
- extractive-qa
- document-retrieval
pretty_name: RegOps-Bench (Korean R&D Regulation QA)
size_categories:
- n<1K
tags:
- legal
- regulation
- korean
- benchmark
- knowledge-graph
- retrieval-augmented-generation
- emnlp2026
configs:
- config_name: default
  data_files:
  - split: corpus
    path: articles.jsonl
  - split: test
    path: regops_bench.jsonl
---

# RegOps-Bench: A Korean National R&D Regulation Benchmark for Regulatory Compliance QA

RegOps-Bench is a Regulatory Compliance QA benchmark for evaluating retrieval-augmented systems on **Korean national R&D regulations** (국가연구개발혁신법 and related decrees, rules, notices, and operational manuals). Each question targets a specific procedural decision a researcher or administrator would face when conducting government-funded research in Korea — e.g., personnel cost calculation, equipment procurement, travel expense reimbursement, indirect-cost rules. Unlike conventional multi-hop or legal QA, every question requires **structured procedural lookups and evidence-set closure** across a multi-tiered authority structure (statute → decree → rule → notice → manual), with ground-truth citations attached at the article and clause level.

> **Citation-Closure Retrieval and Per-Rule Attribution for Real-World Regulatory Compliance Question Answering**
>
> Deploying Large Language Models (LLMs) for regulatory compliance demands rigorous traceability via comprehensive citations across multi-tiered authority structures. Unlike traditional multi-hop or legal QA, this task requires structured procedural lookups and evidence-set closure rather than entity resolution or case-law reasoning. Existing RAG systems struggle here due to flattened citation edges, fragmented retrieval expansions, and fragile post-hoc attribution. We formalize Regulatory Compliance QA with **RegOps-Bench**, a novel benchmark featuring an Operational Knowledge Graph derived from complex national R&D regulations. To address these bottlenecks, we propose **RefWalk**, a unified framework driven by a shared topic anchor. RefWalk traverses cross-document citations, fuses multi-view candidates via max-based aggregation, and enforces per-rule attribution to explicitly map claims to sources. We establish a strong baseline with substantial improvements in retrieval recall and citation accuracy. Finally, a contrastive evaluation on a U.S. health compliance dataset (HIPAA) reveals that existing systems exhibit saturation on flat-structure rules, underscoring the need for RegOps-Bench.
>

[[Paper]](https://arxiv.org/abs/2605.29742) / 
[[Code]](https://github.com/yeongjoonJu/RefWalk)

## Dataset Overview

| | Count |
|---|---|
| **Corpus articles** (`corpus` split) | 718 |
| **QA pairs** (`test` split) | 231 |
| **Source regulations** | 12 documents (6 statutes/decrees + 4 rules + 1 notice + 1 manual) |
| **Languages** | Korean (`ko`) |

### Source documents covered by the corpus

| Document | Authority level | Articles |
|---|---|---|
| 국가연구개발사업 연구개발비 사용기준 | NOTICE | 125 |
| 부가가치세법 | STATUTE | 85 |
| 부가가치세법 시행규칙 | RULE | 85 |
| 국가연구개발혁신법 시행령 | DECREE | 75 |
| 과학기술기본법 시행령 | DECREE | 72 |
| 과학기술기본법 | STATUTE | 71 |
| 국가연구개발 시설장비의 관리 등에 관한 표준지침 | NOTICE | 56 |
| 정보통신방송 연구개발 관리규정 | NOTICE | 54 |
| 국가연구개발혁신법 | STATUTE | 42 |
| 국가연구개발혁신법 매뉴얼 (2025) | MANUAL | 40 |
| 과학기술기본법 시행규칙 | RULE | 9 |
| 국가연구개발혁신법 시행규칙 | RULE | 4 |

## Splits

This dataset uses a single config (`default`) with two splits:

- **`corpus`** (`articles.jsonl`, 718 rows) — the article-level regulatory corpus that QA systems retrieve from
- **`test`** (`regops_bench.jsonl`, 231 rows) — evaluation QA pairs with ground-truth references back into the corpus

```python
from datasets import load_dataset

corpus = load_dataset("Y-J-Ju/RegOps-Bench", split="corpus")
test   = load_dataset("Y-J-Ju/RegOps-Bench", split="test")
```

## Difficulty Levels (L1–L4)

Each QA pair carries a `difficulty` label following the **RegOps difficulty taxonomy** (also encoded in the `qa_id` prefix):

| Level | Description | Count |
|---|---|---|
| **L1** | Single-clause factual lookup — answer is contained in one article | 48 |
| **L2** | Multi-facet reasoning within a single document | 81 |
| **L3** | Cross-document reference traversal (statute ↔ decree ↔ notice) | 45 |
| **L4** | Conditional / exception-paired reasoning with procedural chains | 57 |

`difficulty` is the auto-assigned label used for per-level evaluation. A separate `target_difficulty` field records the difficulty the generator was asked to hit (L1 51 / L2 45 / L3 36 / L4 43); it is `null` for the 56 IITP-seed questions, which were not generated from a difficulty target.

133 of 231 QA pairs are flagged `conditional=true`, meaning the correct answer depends on satisfying one or more preconditions (temporal, qualification, quantitative, procedural, or approval-based).

### Question-type distribution

| `question_type` | Count |
|---|---|
| multi_facet | 53 |
| single_clause | 50 |
| general_principle | 24 |
| exception_paired | 26 |
| institution_specific | 22 |
| *unlabeled (IITP seed)* | 56 |

### Institution-specific subset

22 questions are scoped to a specific institution type, distributed as:
대학 (8), 정부출연 (10), 비영리 (6), 영리 (5). This subset tests whether systems can apply regulations differently based on the asking institution's category.

## Schema

### `corpus` split — `articles.jsonl`

| Field | Type | Description |
|---|---|---|
| `node_id` | string | Hierarchical identifier, e.g. `국가연구개발혁신법_제10조_제1항` |
| `document_name` | string | Source document slug |
| `authority_level` | enum | `STATUTE`, `DECREE`, `RULE`, `NOTICE`, `MANUAL` |
| `effective_date` | string (`YYYY-MM-DD`) | Date the article became effective |
| `hierarchy_path` | list[string] | Article address path (장/조/항/호) |
| `text_ko` | string | Korean article text |
| `text_en` | string \| null | English translation (when available) |
| `sub_items` | list[object] | Paragraph/clause breakdown |
| `has_table` / `table_text` | bool / string \| null | Embedded table content |
| `source_page` | int \| null | Page number in original PDF |
| `image_count` | int | Number of embedded images |

### `test` split — `regops_bench.jsonl`

| Field | Type | Description |
|---|---|---|
| `qa_id` | string | Stable ID, e.g. `L1_ko_001` |
| `language` | enum | `ko` |
| `question_type` | enum \| null | See table above |
| `difficulty` | enum | `L1` / `L2` / `L3` / `L4` — assigned difficulty label used for per-level evaluation |
| `target_difficulty` | enum \| null | Difficulty the generator targeted; `null` for IITP-seed questions |
| `domain` | string | `default` |
| `facets` | object | Question-specific facet annotations |
| `institutions` | list[string] | Applicable institution types (`대학`, `정부출연`, ...) |
| `question` | string | Question (Korean) |
| `answer` | string | Reference answer (Korean) |
| `question_en` / `answer_en` | string \| null | English translation (when available) |
| `conditional` | bool | Whether the answer depends on preconditions |
| `gt_references` | list[string] | Ground-truth corpus `node_id`s the answer cites |
| `anchor_node` | string | Primary anchor article in the corpus |
| `extra_anchors` | list[string] | Additional relevant anchors |
| `granularity` | string | Article-level vs. clause-level reference |
| `hop_count` | int | Minimum reference hops to reach all `gt_references` |
| `cross_document` | bool | Whether `gt_references` span multiple documents |
| `has_chain` | bool | Whether the answer requires a procedural chain |
| `verified` | bool | Manual verification flag |
| `source_seed` / `provenance` / `sampler_meta` / `validation` / `source_stage` / `docs_count` | various | Generation-pipeline provenance fields |

## Data Sources & Attribution

This dataset is derived from publicly released Korean government materials and FAQ documents.

- **Legal corpus** — All regulation texts in `articles.jsonl` are sourced from the **Korean National Law Information Center (국가법령정보센터, https://www.law.go.kr)**, published by the Ministry of Government Legislation (법제처) under the **Korea Open Government License Type 1 (공공누리 제1유형: 출처표시)**. The KOGL Type 1 license permits free use, including commercial use and modification, conditional on source attribution.
- **QA seed data** — A portion of the QA seeds are derived from the Institute of Information & Communications Technology Planning & Evaluation (IITP) FAQ release on national R&D innovation regulations: [국가연구개발혁신법 FAQ (IITP)](https://www.iitp.kr/web/lay1/bbs/S1T46C59/A/13/view.do?article_seq=4331&sort=latest&cpage=1&rows=10).

When using this dataset, please retain attribution to the original Korean government sources and IITP as listed above, in addition to citing this dataset.