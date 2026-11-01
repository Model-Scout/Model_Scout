---
type: "dataset"
id: "Gabrui/multilingual_TinyStories"
source: "huggingface"
url: "https://huggingface.co/datasets/Gabrui/multilingual_TinyStories"
downloads: 913
summary: "3~4세 아동용 짧은 이야기 다국어 번역 데이터로 다국어 소형 언어모델 학습에 적합합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Gabrui/multilingual_TinyStories

> dataset · [Hugging Face](https://huggingface.co/datasets/Gabrui/multilingual_TinyStories)

3~4세 아동용 짧은 이야기 다국어 번역 데이터로 다국어 소형 언어모델 학습에 적합합니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Evaluating language models' fluency, consistency, reasoning, and creativity across multiple languages` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Exploring the scaling laws and interpretability of small language models with fewer than 10 million parameters` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `171` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cdla-sharing-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Multilingual TinyStories dataset contains translations of the original TinyStories dataset` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Training and Test splits are present. The test split is a hold-out for final evaluation after training and hyper-param selection` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is ideal for training and evaluating small language models (SLMs) in multiple languages` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `story` 열 p90 682자 ≈ 171 토큰 (viewer statistics, korean/test)
