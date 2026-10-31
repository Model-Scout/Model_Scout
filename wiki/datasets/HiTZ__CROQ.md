---
type: "dataset"
id: "HiTZ/CROQ"
source: "huggingface"
url: "https://huggingface.co/datasets/HiTZ/CROQ"
downloads: 154
summary: "CROQ는 다국어 문화 관련 개방형 질문 데이터셋으로 LLM의 문화적 편향 평가용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[문화·관광]]"
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# HiTZ/CROQ

> dataset · [Hugging Face](https://huggingface.co/datasets/HiTZ/CROQ)

CROQ는 다국어 문화 관련 개방형 질문 데이터셋으로 LLM의 문화적 편향 평가용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `a multilingual benchmark for evaluating cultural and regional biases in large language models through open-ended cultural questions` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `open-ended cultural questions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Model responses are subsequently processed to identify the country or region referenced` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `24 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `21` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — tag_match · readme, tags = `culture` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `multilingual dataset designed to uncover cultural and regional biases in large language models` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `A multilingual benchmark for evaluating cultural and regional biases in large language models` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `fr` 열 p90 82자 ≈ 21 토큰 (viewer statistics, default/eval)
