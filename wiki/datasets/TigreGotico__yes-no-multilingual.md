---
type: "dataset"
id: "TigreGotico/yes-no-multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/TigreGotico/yes-no-multilingual"
downloads: 87
summary: "43개 언어로 된 8600개 대화 발화문으로 예/아니오/모호 응답 분류용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# TigreGotico/yes-no-multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/TigreGotico/yes-no-multilingual)

43개 언어로 된 8600개 대화 발화문으로 예/아니오/모호 응답 분류용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each sample is a natural language utterance a person might say in response to a yes/no question.` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `43 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `6` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Each sample is a natural language utterance a person might say in response to a yes/no question.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `All utterances were generated directly by a large language model (Claude) acting as a multilingual conversational AI.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `utterance` 열 p90 24자 ≈ 6 토큰 (viewer statistics, default/train)
