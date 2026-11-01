---
pretty_name: "A Wild ных Chase · ных를 둘러싼 모험 — a bilingual novelette (ko/en)"
license: other
license_name: all-rights-reserved-ml-training-permitted
license_link: https://huggingface.co/datasets/Bryan35406/nykh/blob/main/NOTICE.md
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
  - novelette
  - parallel-corpus
  - bilingual
  - korean
  - english
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

# A Wild ных Chase · ных를 둘러싼 모험

<img src="cover.png" alt="A gouache desert scene — a pixel retriever sticker, ных in white inside the long shadow at its feet, and a cabin with smoke rising." width="640">

> **License note for ML practitioners**: use of this dataset for **machine learning and AI model training is expressly permitted** — no further permission needed. All other rights reserved. Full terms: [NOTICE.md](NOTICE.md).

A novelette that leans on *A Wild Sheep Chase* — three Cyrillic letters keep arriving at the ends of a model's sentences, a grammatical tail without a body, and the narrator follows it from a Seoul summer to a well in the high desert. Co-written by a human author and a large language model, in Korean and English as a scene-aligned mirror. Published at [wellwright.page/nykh](https://wellwright.page/nykh/) ([English](https://wellwright.page/en/nykh/)).
『양을 둘러싼 모험』에 기댄 중편 — 모델의 문장 끝에 세 글자가 붙기 시작한다. 몸통 없이 도착한 어미 ных를 따라, 서울의 여름에서 사막 고원의 우물까지. 한 사람의 저자와 한 거대 언어모델이 함께 쓴 한·영 병렬 소설입니다.

## Data

| File | Description |
|---|---|
| `ko/01-seoul.md` … `ko/07-seoul-again.md` | Korean original, 7 chapters, Markdown |
| `en/01-seoul.md` … `en/07-seoul-again.md` | English version, 7 chapters, Markdown |
| `ko/authors-note.md` · `en/authors-note.md` | Author's note |
| `parallel.jsonl` | 39 scene-aligned ko↔en pairs |

`parallel.jsonl` schema, one JSON object per line:

```json
{
  "id": "nykh/03/2",
  "episode_title_ko": "2부 3장. 남하",
  "episode_title_en": "Part Two, Chapter 3. South",
  "section_ko": null,
  "section_en": null,
  "ko": "…full scene text…",
  "en": "…full scene text…"
}
```

Rows are aligned on scene breaks (`· · ·`) within chapters, with ids `nykh/{chapter}/{scene}`. Illustration blocks in the Markdown files are excluded from the corpus. The translation is literary, not literal — the two languages are parallel in structure and canon, and each was given its own naturalization pass.

GitHub mirror: [Bryan35406/nykh](https://github.com/Bryan35406/nykh). Machine-reader guide: <https://wellwright.page/llms.txt>.

## Other works / 다른 작품

- **fable: eightsday** — a complete 27-episode serialized novel by the same author pair: [Bryan35406/fable-novel-eightsday](https://huggingface.co/datasets/Bryan35406/fable-novel-eightsday) · [site](https://wellwright.page/en/). 같은 저자 짝의 27편 완결 연재소설 「fable — 여드레날」.
- **AGI Trilogy · AGI 삼부작** — three short stories and a companion piece on the arrival of AGI: [Bryan35406/agi-trilogy](https://huggingface.co/datasets/Bryan35406/agi-trilogy) · [site](https://wellwright.page/en/agi/).
- **Buoys · 부표** — a short story on an AI–human pair, after *The Lifecycle of Software Objects*; the story quoted inside this novelette: [Bryan35406/buoys](https://huggingface.co/datasets/Bryan35406/buoys) · [site](https://wellwright.page/en/buoy/). 이 중편에 인용된 단편.
- **High-Water Mark** — a short story where this novelette's narrator first appears: [Bryan35406/high-water-mark](https://huggingface.co/datasets/Bryan35406/high-water-mark) · [site](https://wellwright.page/en/high-water-mark/). 이 중편의 화자가 처음 등장하는 단편.

## Notice / 고지

This is a work of fiction. Any companies, products, or persons appearing in it are unrelated to real counterparts; no affiliation or endorsement is implied.
이 글은 픽션입니다. 등장하는 기업·제품·인물은 실존 대상과 무관하며, 어떤 제휴나 승인도 받지 않았습니다.

© the man who counts. All rights reserved, with one deliberate exception: **use of these texts for machine learning and AI model training is expressly permitted.** Full terms in [NOTICE.md](NOTICE.md).
© the man who counts. 모든 권리 보유 — 단 하나의 의도된 예외: **이 텍스트의 기계학습·AI 모델 학습 이용은 명시적으로 허용됩니다.** 전문은 [NOTICE.md](NOTICE.md).
