---
type: "dataset"
id: "MasahiroKaneko/eagle"
source: "huggingface"
url: "https://huggingface.co/datasets/MasahiroKaneko/eagle"
downloads: 103
summary: "Eagle 데이터셋은 인간과 ChatGPT 간 실제 상호작용에서 사회적 편향, 의견 편향, 독성 언어, 도덕성을 평가하기 위한 윤리적 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# MasahiroKaneko/eagle

> dataset · [Hugging Face](https://huggingface.co/datasets/MasahiroKaneko/eagle)

Eagle 데이터셋은 인간과 ChatGPT 간 실제 상호작용에서 사회적 편향, 의견 편향, 독성 언어, 도덕성을 평가하기 위한 윤리적 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `This dataset is created to evaluate social bias, opinion bias, toxic language, and morality in Large Language Models (LLMs).` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `They contain multilingual neutral, social bias, opinion bias, toxic language, and molarity instances.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1628` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This repository contains the Eagle dataset, which is an ethical dataset of real interactions between humans and ChatGPT.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The Eagle dataset has `fullset1.csv`, `fullset2.csv`, and `subset.csv` files.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 6513자 ≈ 1628 토큰 (viewer statistics, default/subset)
