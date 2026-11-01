---
type: "dataset"
id: "PoetryMTEB/KPoEMEmotionClassification"
source: "huggingface"
url: "https://huggingface.co/datasets/PoetryMTEB/KPoEMEmotionClassification"
downloads: 31
summary: "한국 현대시 감정 다중분류 데이터셋으로, PoetryMTEB용 KPoEM에서 파생됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# PoetryMTEB/KPoEMEmotionClassification

> dataset · [Hugging Face](https://huggingface.co/datasets/PoetryMTEB/KPoEMEmotionClassification)

한국 현대시 감정 다중분류 데이터셋으로, PoetryMTEB용 KPoEM에서 파생됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = ``poem` holds the work/segment text.` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `26` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `Korean modern poetry emotion classification` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `train=5638; validation=575; test=794` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train=5638; validation=575; test=794` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `poem` 열 p90 39자 ≈ 26 토큰 (viewer statistics, line/validation)
