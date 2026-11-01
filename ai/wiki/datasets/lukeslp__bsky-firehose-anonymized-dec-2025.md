---
type: "dataset"
id: "lukeslp/bsky-firehose-anonymized-dec-2025"
source: "huggingface"
url: "https://huggingface.co/datasets/lukeslp/bsky-firehose-anonymized-dec-2025"
downloads: 40
summary: "2025년 12월 Bluesky AT 프로토콜을 통해 수집한 익명화된 게시글 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lukeslp/bsky-firehose-anonymized-dec-2025

> dataset · [Hugging Face](https://huggingface.co/datasets/lukeslp/bsky-firehose-anonymized-dec-2025)

2025년 12월 Bluesky AT 프로토콜을 통해 수집한 익명화된 게시글 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `Post content` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `sentiment scores (VADER)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `101,040 Bluesky posts collected via the AT Protocol firehose` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `101,040 Bluesky posts collected via the AT Protocol firehose, December 2-25, 2025.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
