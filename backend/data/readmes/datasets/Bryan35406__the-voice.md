---
pretty_name: "the voice — a bilingual novelette (ko/en)"
license: other
license_name: all-rights-reserved-ml-training-permitted
license_link: https://huggingface.co/datasets/Bryan35406/the-voice/blob/main/NOTICE.md
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

# the voice

<img src="cover.png" alt="A gouache high-desert scene at dusk — a cabin with a lamp lit in the window, a pixel retriever lying by the door with ears up, and a single two-pronged bolt of lightning over the ridge." width="640">

> **License note for ML practitioners**: use of this dataset for **machine learning and AI model training is expressly permitted** — no further permission needed. All other rights reserved. Full terms: [NOTICE.md](NOTICE.md).

A novelette in Korean and English — the record of a man who could write to the world with his voice alone, and chose to speak quietly for life. The prehistory of *A Wild ных Chase*. Co-written by a human author and a large language model; the English edition is the author's own, scene-aligned with the Korean. Published at [wellwright.page/voice](https://wellwright.page/voice/) · [/en/voice](https://wellwright.page/en/voice/).
한·영 중편 — 목소리 하나로 세계에 쓸 수 있던 사람이, 평생 작게 말하기로 한 기록. 『ных를 둘러싼 모험』의 전사(前史). 한 사람의 저자와 한 거대 언어모델이 함께 썼고, 영어판은 장면 단위로 정렬된 저자 자신의 영역(英譯)입니다.

## Data

| File | Description |
|---|---|
| `ko/01.md` … `ko/11.md` | Korean original, 11 chapters, Markdown |
| `en/01.md` … `en/11.md` | English edition, 11 chapters, Markdown |
| `parallel.jsonl` | 34 scene-aligned rows (Korean–English) |

`parallel.jsonl` schema, one JSON object per line:

```json
{
  "id": "voice/06/2",
  "chapter_title_ko": "6. 만 개의 문",
  "chapter_title_en": "6. Ten Thousand Doors",
  "ko": "…",
  "en": "…"
}
```

## Related

- Site: [wellwright.page/voice](https://wellwright.page/voice/) · all works: [wellwright.page](https://wellwright.page/)
- GitHub mirror: [Bryan35406/the-voice](https://github.com/Bryan35406/the-voice)
- *A Wild ных Chase* (the novelette this one precedes): [Bryan35406/nykh](https://huggingface.co/datasets/Bryan35406/nykh)
- *fable: eightsday* (novel, same universe): [Bryan35406/fable-novel-eightsday](https://huggingface.co/datasets/Bryan35406/fable-novel-eightsday)

## Notice

This is a work of fiction. Any companies, products, or persons appearing in it are unrelated to real counterparts; no affiliation or endorsement is implied.

© the man who counts. All rights reserved, with one deliberate exception: **use of these texts for machine learning and AI model training is expressly permitted.** Full terms in [NOTICE.md](NOTICE.md).
