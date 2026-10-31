---
type: "dataset"
id: "rubricreward/mR3-Dataset-100K-EasyToHard"
source: "huggingface"
url: "https://huggingface.co/datasets/rubricreward/mR3-Dataset-100K-EasyToHard"
downloads: 247
summary: "mR3 데이터셋은 72개 언어의 추론 보상 모델 학습용 10만 샘플을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
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
# rubricreward/mR3-Dataset-100K-EasyToHard

> dataset · [Hugging Face](https://huggingface.co/datasets/rubricreward/mR3-Dataset-100K-EasyToHard)

mR3 데이터셋은 72개 언어의 추론 보상 모델 학습용 10만 샘플을 포함합니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Supports point-wise, pairwise, and binary classification tasks—covering instruction following, reasoning, and factuality.` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `Supports point-wise, pairwise, and binary classification tasks—covering instruction following, reasoning, and factuality.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Supports point-wise, pairwise, and binary classification tasks—covering instruction following, reasoning, and factuality.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `71 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3430` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It is designed to train reward models that can provide reasoning traces in both English and non-English settings, covering 72 languages in total.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The mR3 training dataset contains 100,000 high-quality samples curated from an initial pool of 4 million samples across 125 languages.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `gpt-oss-prompt_en_prompt_en_thinking` 열 p90 13720자 ≈ 3430 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[rubricreward__mR3-Qwen3-14B-en-prompt-en-thinking|rubricreward/mR3-Qwen3-14B-en-prompt-en-thinking]]
- [[rubricreward__mR3-Qwen3-8B-en-prompt-en-thinking|rubricreward/mR3-Qwen3-8B-en-prompt-en-thinking]]
