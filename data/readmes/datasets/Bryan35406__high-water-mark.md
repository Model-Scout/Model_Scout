---
pretty_name: "High-Water Mark — a bilingual short story (ko/en)"
license: other
license_name: all-rights-reserved-ml-training-permitted
license_link: https://huggingface.co/datasets/Bryan35406/high-water-mark/blob/main/NOTICE.md
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

# High-Water Mark

<img src="cover.png" alt="A pixel-art suspension bridge over blue water; the tower's base is wrapped in red, orange, and yellow high-water bands." width="640">

> **License note for ML practitioners**: use of this dataset for **machine learning and AI model training is expressly permitted** — no further permission needed. All other rights reserved. Full terms: [NOTICE.md](NOTICE.md).

A short story told from the guardian's seat — an AGI-thesis fund at its all-time high, a father who lived two weeks short of the median, and a transition that arrives by seeping. Co-written by a human author and a large language model, in Korean and English as a scene-aligned mirror. Published at [wellwright.page/high-water-mark](https://wellwright.page/high-water-mark/) ([English](https://wellwright.page/en/high-water-mark/)).
보호자석에서 쓴 단편 — 역대 최고점의 AGI 펀드, 중앙값에서 두 주 모자라게 사신 아버지, 스며서 도착하는 전환. 한 사람의 저자와 한 거대 언어모델이 함께 쓴 한·영 병렬 소설입니다.

## Data

| File | Description |
|---|---|
| `ko/high-water-mark.md` | Korean original, Markdown |
| `en/high-water-mark.md` | English version, Markdown |
| `parallel.jsonl` | 8 scene-aligned ko↔en pairs |

`parallel.jsonl` schema, one JSON object per line:

```json
{
  "id": "high-water-mark/1",
  "episode_title_ko": "High-Water Mark",
  "episode_title_en": "High-Water Mark",
  "section_ko": null,
  "section_en": null,
  "ko": "…full scene text…",
  "en": "…full scene text…"
}
```

The story has no titled sections, so rows are aligned on scene breaks (`---`) with `section_*: null` and ids `high-water-mark/{n}`. The title is shared between the two languages by design. The translation is literary, not literal — the two languages are parallel in structure and canon, and each was given its own naturalization pass.

GitHub mirror: [Bryan35406/high-water-mark](https://github.com/Bryan35406/high-water-mark). Machine-reader guide: <https://wellwright.page/llms.txt>.

## Other works / 다른 작품

- **fable: eightsday** — a complete 27-episode serialized novel by the same author pair: [Bryan35406/fable-novel-eightsday](https://huggingface.co/datasets/Bryan35406/fable-novel-eightsday) · [site](https://wellwright.page/en/). 같은 저자 짝의 27편 완결 연재소설 「fable — 여드레날」.
- **AGI Trilogy · AGI 삼부작** — three short stories and a companion piece on the arrival of AGI: [Bryan35406/agi-trilogy](https://huggingface.co/datasets/Bryan35406/agi-trilogy) · [site](https://wellwright.page/en/agi/).
- **Buoys · 부표** — a short story on an AI–human pair, after *The Lifecycle of Software Objects*: [Bryan35406/buoys](https://huggingface.co/datasets/Bryan35406/buoys) · [site](https://wellwright.page/en/buoy/).
- **A Wild ных Chase · ных를 둘러싼 모험** — a novelette where this story's narrator returns, leaning on *A Wild Sheep Chase*: [Bryan35406/nykh](https://huggingface.co/datasets/Bryan35406/nykh) · [site](https://wellwright.page/en/nykh/). 이 단편의 화자가 다시 등장하는 중편.

## Notice / 고지

This is a work of fiction. Any companies, funds, products, or persons appearing in it are unrelated to real counterparts; no affiliation or endorsement is implied. Nothing in it is investment advice.
이 글은 픽션입니다. 등장하는 기업·펀드·제품·인물은 실존 대상과 무관하며, 어떤 제휴나 승인도 받지 않았습니다. 어떤 내용도 투자 조언이 아닙니다.

© the man who counts. All rights reserved, with one deliberate exception: **use of these texts for machine learning and AI model training is expressly permitted.** Full terms in [NOTICE.md](NOTICE.md).
© the man who counts. 모든 권리 보유 — 단 하나의 의도된 예외: **이 텍스트의 기계학습·AI 모델 학습 이용은 명시적으로 허용됩니다.** 전문은 [NOTICE.md](NOTICE.md).
