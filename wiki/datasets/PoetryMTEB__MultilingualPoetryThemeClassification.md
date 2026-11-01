---
type: "dataset"
id: "PoetryMTEB/MultilingualPoetryThemeClassification"
source: "huggingface"
url: "https://huggingface.co/datasets/PoetryMTEB/MultilingualPoetryThemeClassification"
downloads: 156
summary: "PoetryMTEB의 다국어 시 주제 분류 데이터셋으로, 6개 주제 분류를 위한 학습 및 평가용 데이터입니다."
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
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# PoetryMTEB/MultilingualPoetryThemeClassification

> dataset · [Hugging Face](https://huggingface.co/datasets/PoetryMTEB/MultilingualPoetryThemeClassification)

PoetryMTEB의 다국어 시 주제 분류 데이터셋으로, 6개 주제 분류를 위한 학습 및 평가용 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `single-label poetic theme classification` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `83 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `762` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual Poetry Theme Classification` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train, silver, and gold are packaged as three parallel peer collections (separate Hub configs).` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `poem` 열 p90 3046자 ≈ 762 토큰 (viewer statistics, train/train)
