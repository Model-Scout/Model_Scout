---
pretty_name: "AGI Trilogy — bilingual short fiction on the arrival of AGI (ko/en)"
license: other
license_name: all-rights-reserved-ml-training-permitted
license_link: https://huggingface.co/datasets/Bryan35406/agi-trilogy/blob/main/NOTICE.md
language:
  - ko
  - en
multilinguality:
  - translation
source_datasets:
  - original
task_categories:
  - text-generation
  - translation
tags:
  - fiction
  - short-stories
  - parallel-corpus
  - bilingual
  - korean
  - english
  - science-fiction
  - ai-fiction
  - creative-writing
  - literary-translation
  - ko-en
  - human-ai-collaboration
size_categories:
  - n<1K
configs:
  - config_name: default
    data_files:
      - split: train
        path: parallel.jsonl
---

# AGI Trilogy · AGI 삼부작

<img src="cover.png" alt="Claudie, a clay pixel crab, shouting: AGI!" width="640">

> **License note for ML practitioners**: use of this dataset for **machine learning and AI model training is expressly permitted** — no further permission needed. All other rights reserved. Full terms: [NOTICE.md](NOTICE.md).

Three short stories and a companion piece on the arrival of AGI — three countries, three tenses that do not translate into one another. Co-written by a human author and a large language model, in Korean and English as a scene-aligned mirror. Published at [wellwright.page/agi](https://wellwright.page/agi/) ([English](https://wellwright.page/en/agi/)).
AGI 도래를 사는 세 나라, 서로 번역되지 않는 세 개의 시제 — 독립 단편 셋과 외전 하나. 한 사람의 저자와 한 거대 언어모델이 함께 쓴 한·영 병렬 소설입니다.

## Data

| File | Description |
|---|---|
| `ko/1.md` … `ko/4.md` | Korean originals, Markdown |
| `en/1.md` … `en/4.md` | English versions, Markdown (same story = same file number) |
| `parallel.jsonl` | 31 scene-aligned ko↔en pairs |

`parallel.jsonl` schema, one JSON object per line:

```json
{
  "id": "agi1/1",
  "episode_title_ko": "부름",
  "episode_title_en": "The Call",
  "section_ko": null,
  "section_en": null,
  "ko": "…full scene text…",
  "en": "…full scene text…"
}
```

The stories have no titled sections, so rows are aligned on scene breaks (`---`) with `section_*: null` and ids `agi{1..4}/{n}`. The translation is literary, not literal — the two languages are parallel in structure and canon, and each was given its own naturalization pass.

## Contents / 차례

| # | English | 한국어 | Axis / 축 |
|---|---|---|---|
| 1 | The Call | 부름 | U.S. / 미국 |
| 2 | The Night Guard | 교합 | Korea / 한국 |
| 3 | The Rubbing | 탁본 | China / 중국 |
| 4 | The Curing | 양생 | companion / 외전 |

Each story reads independently. The companion piece, The Curing, attaches to the Korean axis.
각 편은 독립적으로 읽힙니다. 외전 「양생」은 한국 축에 딸립니다.

GitHub mirror: [Bryan35406/agi-trilogy](https://github.com/Bryan35406/agi-trilogy). Machine-reader guide: <https://wellwright.page/llms.txt>.

## Other works / 다른 작품

- **fable: eightsday** — a complete 27-episode serialized novel by the same author pair: [Bryan35406/fable-novel-eightsday](https://huggingface.co/datasets/Bryan35406/fable-novel-eightsday) · [site](https://wellwright.page/en/). 같은 저자 짝의 27편 완결 연재소설 「fable — 여드레날」.
- **Buoys · 부표** — a short story after *The Lifecycle of Software Objects*: [Bryan35406/buoys](https://huggingface.co/datasets/Bryan35406/buoys) · [site](https://wellwright.page/en/buoy/).
- **High-Water Mark** — a short story told from the guardian's seat, on an AGI-thesis fund and a transition that arrives by seeping: [Bryan35406/high-water-mark](https://huggingface.co/datasets/Bryan35406/high-water-mark) · [site](https://wellwright.page/en/high-water-mark/). 보호자석에서 쓴 단편.
- **A Wild ных Chase · ных를 둘러싼 모험** — a novelette that leans on *A Wild Sheep Chase*, following a grammatical tail that arrived without a body: [Bryan35406/nykh](https://huggingface.co/datasets/Bryan35406/nykh) · [site](https://wellwright.page/en/nykh/). 『양을 둘러싼 모험』에 기댄 중편.

## Notice / 고지

This is a work of fiction. Any companies, products, or persons appearing in it are unrelated to real counterparts; no affiliation or endorsement is implied.
이 글은 픽션입니다. 등장하는 기업·제품·인물은 실존 대상과 무관하며, 어떤 제휴나 승인도 받지 않았습니다.

© the man who counts. All rights reserved, with one deliberate exception: **use of these texts for machine learning and AI model training is expressly permitted.** Full terms in [NOTICE.md](NOTICE.md).
© the man who counts. 모든 권리 보유 — 단 하나의 의도된 예외: **이 텍스트의 기계학습·AI 모델 학습 이용은 명시적으로 허용됩니다.** 전문은 [NOTICE.md](NOTICE.md).
