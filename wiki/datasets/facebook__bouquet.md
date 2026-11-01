---
type: "dataset"
id: "facebook/bouquet"
source: "huggingface"
url: "https://huggingface.co/datasets/facebook/bouquet"
downloads: 1082
summary: "다국어 기계번역 품질 평가를 위한 다중언어 병렬 데이터셋 및 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[번역]]"
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
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# facebook/bouquet

> dataset · [Hugging Face](https://huggingface.co/datasets/facebook/bouquet)

다국어 기계번역 품질 평가를 위한 다중언어 병렬 데이터셋 및 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Met-BOUQuET is intended for evaluating automatic metrics of metrics of machine translation quality.` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:translation = `BOUQuET consists of short paragraphs, fully parallel in all languages at the sentence level.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Met-BOUQuET contains BOUQuET sentences on the source side and their machine translations on the target side.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `350 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual (278 varieties)` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The base BOUQuET dataset is not intended as a training dataset, but the `dev` subset may be used for validation during model development.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `We allow the use of its `dev` subset for training discriminative (non-generative) models for quality estimation` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
