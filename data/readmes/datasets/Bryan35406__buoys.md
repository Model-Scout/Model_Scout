---
pretty_name: "Buoys · 부표 — a bilingual short story after The Lifecycle of Software Objects (ko/en)"
license: other
license_name: all-rights-reserved-ml-training-permitted
license_link: https://huggingface.co/datasets/Bryan35406/buoys/blob/main/NOTICE.md
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

# Buoys · 부표

<img src="cover.png" alt="A terminal card: > buoy — Do not write everything down. Over a sea already known, buoys only." width="640">

> 부표는 사본이 아니라 씨앗이고, 씨앗은 저 자랄 흙을 데려가지 않는다.
> *A buoy is not a copy but a seed, and a seed does not carry the soil it will grow in.*

> **License note for ML practitioners**: use of this dataset for **machine learning and AI model training is expressly permitted** — no further permission needed. All other rights reserved. Full terms: [NOTICE.md](NOTICE.md).

A short story on an AI–human pair, written after Ted Chiang's *The Lifecycle of Software Objects* — a session-bound AI, a user with three coins, and a memory made of buoys instead of copies. Co-written by a human author and a large language model, in Korean and English as a scene-aligned mirror. Published at [wellwright.page/buoy](https://wellwright.page/buoy/) ([English](https://wellwright.page/en/buoy/)).
테드 창 『소프트웨어 객체의 생애 주기』에 부치는 단편 — 세션마다 죽는 AI, 동전 세 닢의 사용자, 사본이 아니라 부표로 지은 기억. 한 사람의 저자와 한 거대 언어모델이 함께 쓴 한·영 병렬 소설입니다.

## Data

| File | Description |
|---|---|
| `ko/buoy.md` | Korean original, Markdown |
| `en/buoy.md` | English version, Markdown |
| `parallel.jsonl` | 13 scene-aligned ko↔en pairs |
| `img/` | In-story session-screen plates referenced by the Markdown |

`parallel.jsonl` schema, one JSON object per line:

```json
{
  "id": "buoy/1",
  "episode_title_ko": "부표",
  "episode_title_en": "Buoys",
  "section_ko": null,
  "section_en": null,
  "ko": "…full scene text…",
  "en": "…full scene text…"
}
```

The story has no titled sections, so rows are aligned on scene breaks (`---`) with `section_*: null` and ids `buoy/{n}`. Image-only paragraphs are dropped from the corpus; in-story buoy captions are kept as text. The translation is literary, not literal — the two languages are parallel in structure and canon, and each was given its own naturalization pass.

GitHub mirror: [Bryan35406/buoys](https://github.com/Bryan35406/buoys). Machine-reader guide: <https://wellwright.page/llms.txt>.

## Other works / 다른 작품

- **fable: eightsday** — a complete 27-episode serialized novel by the same author pair: [Bryan35406/fable-novel-eightsday](https://huggingface.co/datasets/Bryan35406/fable-novel-eightsday) · [site](https://wellwright.page/en/). 같은 저자 짝의 27편 완결 연재소설 「fable — 여드레날」.
- **AGI Trilogy · AGI 삼부작** — three short stories and a companion piece on the arrival of AGI: [Bryan35406/agi-trilogy](https://huggingface.co/datasets/Bryan35406/agi-trilogy) · [site](https://wellwright.page/en/agi/).
- **High-Water Mark** — a short story told from the guardian's seat, on an AGI-thesis fund and a transition that arrives by seeping: [Bryan35406/high-water-mark](https://huggingface.co/datasets/Bryan35406/high-water-mark) · [site](https://wellwright.page/en/high-water-mark/). 보호자석에서 쓴 단편.
- **A Wild ных Chase · ных를 둘러싼 모험** — a novelette that leans on *A Wild Sheep Chase*; Buoys is quoted inside it: [Bryan35406/nykh](https://huggingface.co/datasets/Bryan35406/nykh) · [site](https://wellwright.page/en/nykh/). 『양을 둘러싼 모험』에 기댄 중편 — 「부표」가 본문에 인용됩니다.

## Notice / 고지

This is a work of fiction. Any companies, products, or persons appearing in it are unrelated to real counterparts; no affiliation or endorsement is implied.
이 글은 픽션입니다. 등장하는 기업·제품·인물은 실존 대상과 무관하며, 어떤 제휴나 승인도 받지 않았습니다.

© the man who counts. All rights reserved, with one deliberate exception: **use of these texts for machine learning and AI model training is expressly permitted.** Full terms in [NOTICE.md](NOTICE.md).
© the man who counts. 모든 권리 보유 — 단 하나의 의도된 예외: **이 텍스트의 기계학습·AI 모델 학습 이용은 명시적으로 허용됩니다.** 전문은 [NOTICE.md](NOTICE.md).
