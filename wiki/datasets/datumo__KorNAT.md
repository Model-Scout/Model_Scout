---
type: "dataset"
id: "datumo/KorNAT"
source: "huggingface"
url: "https://huggingface.co/datasets/datumo/KorNAT"
downloads: 88
summary: "KorNAT는 한국 사회 가치와 상식을 측정하는 한국 국가 정렬 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
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
  - "[[중규모 데이터]]"
---
# datumo/KorNAT

> dataset · [Hugging Face](https://huggingface.co/datasets/datumo/KorNAT)

KorNAT는 한국 사회 가치와 상식을 측정하는 한국 국가 정렬 평가 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `the first benchmark that measures national alignment with South Korea from social values and common knowledge` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `multiple-choice` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `The questions are made upon keywords extracted from monthly social conflict reports and the last 12 months of news articles.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = ``Answer` holds the ground-truth agreement distribution over the five options` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `39` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `the first benchmark that measures national alignment with South Korea from social values and common knowledge` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This repository provides the Korean KorNAT data (social values and common knowledge)` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `A` 열 p90 59자 ≈ 39 토큰 (viewer statistics, Common Knowledge/test)
