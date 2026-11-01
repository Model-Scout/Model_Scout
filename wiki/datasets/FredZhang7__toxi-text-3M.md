---
type: "dataset"
id: "FredZhang7/toxi-text-3M"
source: "huggingface"
url: "https://huggingface.co/datasets/FredZhang7/toxi-text-3M"
downloads: 497
summary: "55개 언어로 된 300만 건의 다국어 독성 텍스트 데이터셋으로 독성 분류에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# FredZhang7/toxi-text-3M

> dataset · [Hugging Face](https://huggingface.co/datasets/FredZhang7/toxi-text-3M)

55개 언어로 된 300만 건의 다국어 독성 텍스트 데이터셋으로 독성 분류에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `3M rows of text data from 55 natural languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `416,529 are classified as toxic, while the remaining 2,463,773 are considered neutral.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `55 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a large multilingual toxicity dataset with 3M rows of text data from 55 natural languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The preprocessed training data alone consists of 2,880,667 rows of comments, tweets, and messages.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
