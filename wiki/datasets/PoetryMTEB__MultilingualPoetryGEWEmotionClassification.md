---
type: "dataset"
id: "PoetryMTEB/MultilingualPoetryGEWEmotionClassification"
source: "huggingface"
url: "https://huggingface.co/datasets/PoetryMTEB/MultilingualPoetryGEWEmotionClassification"
downloads: 217
summary: "다국어 시 감정 분류 데이터셋으로, Geneva Emotion Wheel 기반 다중 레이블 감정 분류에 사용됨."
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# PoetryMTEB/MultilingualPoetryGEWEmotionClassification

> dataset · [Hugging Face](https://huggingface.co/datasets/PoetryMTEB/MultilingualPoetryGEWEmotionClassification)

다국어 시 감정 분류 데이터셋으로, Geneva Emotion Wheel 기반 다중 레이블 감정 분류에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Multi-label GEW ids (centrality desc)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `24 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual Poetry GEW Emotion Classification` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train, silver, and gold are packaged as three parallel peer collections (separate Hub configs).` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
