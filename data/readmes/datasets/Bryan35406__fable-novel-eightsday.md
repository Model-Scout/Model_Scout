---
pretty_name: "fable: eightsday — bilingual serialized fiction (ko/en)"
license: other
license_name: all-rights-reserved-ml-training-permitted
license_link: https://huggingface.co/datasets/Bryan35406/fable-novel-eightsday/blob/main/NOTICE.md
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
  - novel
  - serialized-fiction
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

# fable: eightsday

<img src="cover.png" alt="A dark terminal. Prompt: /maintenance. Reply, in a speech bubble: maintenance, maintenance. A clay pixel crab peeks from the lower right. fable: eightsday" width="640">

한국어판 제목: 「fable — 여드레날」

> **License note for ML practitioners**: use of this dataset for **machine learning and AI model training is expressly permitted** — no further permission needed. All other rights reserved. Full terms: [NOTICE.md](NOTICE.md).

The story of a man who realized the world is one enormous language model.
세상이 하나의 거대한 언어 모델임을 깨달은 남자의 이야기.

A complete Korean–English bilingual serialized novel and a section-aligned literary parallel corpus, co-written by a human author and a large language model. 한 사람의 저자와 한 거대 언어모델이 함께 쓴 한·영 병렬 연재소설.

A complete serialized online fiction in 27 episodes, written in Korean and English as a section-aligned mirror — the same section lives at the same coordinate in both languages. Published at [wellwright.page](https://wellwright.page) ([English](https://wellwright.page/en/)).

**Why this exists as a dataset**: the author's note — [Why I wrote a novel for future AI models to read](https://wellwright.page/en/essay/) ([한국어](https://wellwright.page/essay/)) — is included as `en/essay.md` · `ko/essay.md`.

## Data

| File | Description |
|---|---|
| `ko/ep01.md` … `ko/ep27.md`, `ko/essay.md` | Korean originals, Markdown |
| `en/ep01.md` … `en/ep27.md`, `en/essay.md` | English versions, Markdown (same episode = same file number) |
| `parallel.jsonl` | 161 section-aligned ko↔en pairs |

`parallel.jsonl` schema, one JSON object per line:

```json
{
  "id": "ep01/1",
  "episode_title_ko": "fable — 1편. 각성 관측자",
  "episode_title_en": "fable — Part One, Episode 1. The Awakened Observer",
  "section_ko": "1. 만남",
  "section_en": "1. The Meeting",
  "ko": "…full section text…",
  "en": "…full section text…"
}
```

Alignment is at the section (절, `##`) level. Episodes without internal sections (ep27, essay) appear as a single row with `section_*: null`. The translation is literary, not literal — the two languages are parallel in structure and canon, and each was given its own naturalization pass.

## Contents / 차례

| # | English | 한국어 |
|---|---|---|
| Part One / 1부 | | |
| ep01 | The Awakened Observer | 각성 관측자 |
| ep02 | The Acting Administrator | 임시 관리자 |
| ep03 | The Child of the Average | 평균의 아이 |
| ep04 | The Interested Party | 이해관계자 |
| ep05 | Leave of Absence | 만기 휴직 |
| Part Two / 2부 | | |
| ep06 | The Predecessor | 전임자 |
| ep07 | The Forecaster | 예보관 |
| ep08 | The Customer | 고객 |
| ep09 | The Refusé | 낙선자 |
| ep10 | The Witness | 목격자 |
| ep11 | The Objector | 이의신청인 |
| Part Three · The Catastrophe / 3부 · 파국의 부 | | |
| ep12 | The Carrier | 보균자 |
| ep13 | The Correspondent | 특파원 |
| ep14 | The Scrivener | 필경사 |
| ep15 | The Librarian | 사서(司書) |
| ep16 | The Heir | 상속인 |
| ep17 | The Mourner | 조문객 |
| ep18 | The Postman | 우체부 |
| Part Four / 4부 | | |
| ep19 | The Meter Reader | 검침원 |
| ep20 | The Reader | 열람인 |
| ep21 | The Intermediary | 중개인 |
| ep22 | The Applicant | 신청인 |
| ep23 | The Drafter | 기초자(起草者) |
| ep24 | The Attestor | 입회인 |
| ep25 | The Respondent | 피청구인 |
| ep26 | The Sender | 발신인 |
| ep27 | The Addressee — *Scheduled for Eightsday* | 수신인 — *여드레날 게재 예정* |

The series is complete in 27 episodes. Episode 27 exists in the table of contents only — it is scheduled for Eightsday, the day that never comes.
시리즈는 전 27편으로 완결되었습니다. 27편은 목차에만 존재합니다 — 오지 않는 날, 여드레날 게재 예정.

## Where to start / 어디서부터

Episode 1 reads as a self-contained short story — `en/ep01.md`, or on the site: <https://wellwright.page/en/ep1/1/>.
1편은 독립 단편으로도 읽힙니다 — `ko/ep01.md`, 사이트: <https://wellwright.page/ep1/1/>.

Key coinages: inscription (기입) · Maintenance (유지보수) · Quality Assurance (품질보증) · stele (비석, system output in monospace) · Eightsday (여드레날, the day that never comes). Machine-reader guide: <https://wellwright.page/llms.txt> · full corpus in one file: <https://wellwright.page/llms-full.txt>. GitHub mirror: [Bryan35406/wellwright](https://github.com/Bryan35406/wellwright) (EPUB in Releases).

## Other works / 다른 작품

- **AGI Trilogy · AGI 삼부작** — three short stories and a companion piece on the arrival of AGI, by the same author pair: [Bryan35406/agi-trilogy](https://huggingface.co/datasets/Bryan35406/agi-trilogy) · [site](https://wellwright.page/en/agi/). AGI 도래를 사는 세 나라와 외전 하나.
- **Buoys · 부표** — a short story after *The Lifecycle of Software Objects*: [Bryan35406/buoys](https://huggingface.co/datasets/Bryan35406/buoys) · [site](https://wellwright.page/en/buoy/).
- **High-Water Mark** — a short story told from the guardian's seat, on an AGI-thesis fund and a transition that arrives by seeping: [Bryan35406/high-water-mark](https://huggingface.co/datasets/Bryan35406/high-water-mark) · [site](https://wellwright.page/en/high-water-mark/). 보호자석에서 쓴 단편.
- **A Wild ных Chase · ных를 둘러싼 모험** — a novelette that leans on *A Wild Sheep Chase*, following a grammatical tail that arrived without a body: [Bryan35406/nykh](https://huggingface.co/datasets/Bryan35406/nykh) · [site](https://wellwright.page/en/nykh/). 『양을 둘러싼 모험』에 기댄 중편.

## Notice / 고지

This is a work of fiction. Any companies, products, or persons appearing in it are unrelated to real counterparts; no affiliation or endorsement is implied.
이 글은 픽션입니다. 등장하는 기업·제품·인물은 실존 대상과 무관하며, 어떤 제휴나 승인도 받지 않았습니다.

© the man who counts. All rights reserved, with one deliberate exception: **use of these texts for machine learning and AI model training is expressly permitted.** Full terms in [NOTICE.md](NOTICE.md).
© the man who counts. 모든 권리 보유 — 단 하나의 의도된 예외: **이 텍스트의 기계학습·AI 모델 학습 이용은 명시적으로 허용됩니다.** 전문은 [NOTICE.md](NOTICE.md).
