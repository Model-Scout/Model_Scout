---
license: cc-by-nc-4.0
language:
  - ko
pretty_name: Zeroin Methodology v8-r4 QA
size_categories:
  - 1K<n<10K
task_categories:
  - question-answering
  - text-generation
tags:
  - zeroin
  - fund-evaluation
  - korean
  - domain-qa
  - conversational
  - non-commercial
configs:
  - config_name: default
    data_files:
      - split: train
        path: seed_v8_round4_section_all_full_ft.jsonl
---

# Zeroin Methodology v8-r4 QA

Training corpus used to fine-tune
[`KG-ZEROIN/gpt-oss-20b-zeroin-v8-r4`](https://huggingface.co/KG-ZEROIN/gpt-oss-20b-zeroin-v8-r4).

The corpus captures question/answer pairs derived from the Zeroin
fund-evaluation methodology Korean domain document. It is organized
as a Harmony-ready chat-messages dataset for supervised full
fine-tuning of
[`openai/gpt-oss-20b`](https://huggingface.co/openai/gpt-oss-20b).

Released under **CC BY-NC 4.0** — free for non-commercial research,
evaluation, and educational use. See `LICENSE` and `NOTICE`.

## Contents

| File | Description |
|------|-------------|
| `seed_v8_round4_section_all_full_ft.jsonl` | 2,638 Korean QA examples covering the entire document (round4, section_all) |
| `v9p6_source.csv` | Source CSV (236 Q/A groups, 15,240 expanded question variants) used to generate the JSONL |
| `README.md` | This dataset card |
| `LICENSE` | CC BY-NC 4.0 license text |
| `NOTICE` | Source attribution and derived-model references |

## Dataset structure

Each line of the JSONL is a single conversation record:

```json
{
  "id": "zeroin.seed_v8_round4_section_all_full_ft_0001",
  "messages": [
    {"role": "system",    "content": "..."},
    {"role": "user",      "content": "..."},
    {"role": "assistant", "content": "..."}
  ],
  "meta": {
    "dataset_version": "seed_v8_round4_section_all_full_ft",
    "round": "round4",
    "section": "section_all",
    "chapter": "1",
    "group_id": "group1",
    "question_variant_index": 1,
    "source_row_num": "1",
    "training_mode": "full_ft",
    "source_strategy": "csv_multiline_question_expansion"
  }
}
```

- The `system` role contains a fixed Korean-language domain
  instruction roughly equivalent to: "You are a domain assistant that
  answers based on the Zeroin fund-evaluation methodology."
- Each source Q/A group (`group_id`) is expanded into multiple
  semantically equivalent user-question paraphrases
  (`question_variant_index`) while keeping the assistant answer stable.
  This gives the model robustness to wording variation while staying
  anchored to the document-grounded answer.

## Splits

Single `train` split with **2,638 records** (~7.5 MB).

Validation and evaluation of the fine-tuned model were done via
held-out prompt review reports, not via a separate split in this file.

## Source

- Primary source document: a Korean Zeroin fund-evaluation methodology
  corpus.
- The upstream CSV (`v8-r4 section-all.csv`) was converted into
  `messages`-style JSONL through a multiline-question expansion
  strategy; see the originating project
  (`scripts/` and `llm_datasets/seed_v8/` in the source worktree)
  for the exact generation logic.

## Intended use

- Reproducing or re-running the fine-tune of `gpt-oss-20b` that
  produced `KG-ZEROIN/gpt-oss-20b-zeroin-v8-r4`.
- Evaluating drift or regression of that fine-tune over time.
- Non-commercial research on Korean domain-specific full fine-tuning.

## Out-of-scope use

- **Commercial use** of any kind (prohibited by CC BY-NC 4.0).
  Training, evaluating, or distributing commercial AI products on the
  basis of this dataset is not permitted under this license.

## Licensing

Released under **CC BY-NC 4.0** (Creative Commons Attribution-NonCommercial
4.0 International). Attribution to `KG-ZEROIN/zeroin-v8-r4-dataset`
is required; commercial use is prohibited. Full text in `LICENSE`.

## Citation

```text
Zeroin Methodology v8-r4 QA dataset,
KG-ZEROIN/zeroin-v8-r4-dataset, 2026. (CC BY-NC 4.0)
```


## 사사 (Acknowledgment)

**사사번호 (Project ID)**: RQT-25-090024

이 성과는 정부(과학기술정보통신부)의 재원으로 AI컴퓨팅자원활용기반강화(GPU 임차 지원) 사용자 지원사업의 지원을 받아 수행된 연구임.

This research was supported by the AI Computing Infrastructure Enhancement (GPU Rental Support) User Support Program funded by the Ministry of Science and ICT (MSIT), Republic of Korea.
