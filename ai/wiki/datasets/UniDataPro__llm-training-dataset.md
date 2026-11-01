---
type: "dataset"
id: "UniDataPro/llm-training-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/UniDataPro/llm-training-dataset"
downloads: 67
summary: "32개 언어로 된 400만 개 이상의 로그와 응답 쌍으로 LLM 미세조정용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# UniDataPro/llm-training-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/UniDataPro/llm-training-dataset)

32개 언어로 된 400만 개 이상의 로그와 응답 쌍으로 LLM 미세조정용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — tag_match · tags = `question answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `28 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `488` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset contains over 4 million+ logs written in 32 languages and is tailored for LLM training.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The text corpus supports instruction tuning and supervised fine-tuning for larger language models` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 1952자 ≈ 488 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `kaggle/unidpro/llm-training-dataset`
