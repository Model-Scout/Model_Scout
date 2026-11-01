---
type: "dataset"
id: "zeroshot/twitter-financial-news-sentiment"
source: "huggingface"
url: "https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment"
downloads: 6989
summary: "금융 관련 트윗의 감성 분류를 위한 영어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# zeroshot/twitter-financial-news-sentiment

> dataset · [Hugging Face](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment)

금융 관련 트윗의 감성 분류를 위한 영어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `finance-related tweets` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `annotated with 3 labels` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `33` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `There are 2 splits: train and validation.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 134자 ≈ 33 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[PeterAM4__Qwen3-Embedding-0.6B-GGUF|PeterAM4/Qwen3-Embedding-0.6B-GGUF]]
- [[zhiqian99__Qwen3-Embedding-0.6B-GGUF|zhiqian99/Qwen3-Embedding-0.6B-GGUF]]
