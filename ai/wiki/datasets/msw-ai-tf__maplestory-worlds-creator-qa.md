---
type: "dataset"
id: "msw-ai-tf/maplestory-worlds-creator-qa"
source: "huggingface"
url: "https://huggingface.co/datasets/msw-ai-tf/maplestory-worlds-creator-qa"
downloads: 22
summary: "MapleStory Worlds Creator Center 문서 기반의 한영 병렬 질의응답 데이터셋으로, 지침 튜닝과 QA, 검색에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# msw-ai-tf/maplestory-worlds-creator-qa

> dataset · [Hugging Face](https://huggingface.co/datasets/msw-ai-tf/maplestory-worlds-creator-qa)

MapleStory Worlds Creator Center 문서 기반의 한영 병렬 질의응답 데이터셋으로, 지침 튜닝과 QA, 검색에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, tags, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `Intended for instruction tuning, QA, and retrieval.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:retrieval = `Questions are generated to be self-contained and grounded in the source docs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `answers avoid source/meta references so they read like an expert explanation.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `343` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Synthetic question-answer dataset built from the official MapleStory Worlds Creator Center documentation.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Synthetic question-answer dataset built from the official MapleStory Worlds Creator Center documentation.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 515자 ≈ 343 토큰 (viewer statistics, ko/train)
