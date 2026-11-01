---
type: "dataset"
id: "HPLT/OpenLID-v3"
source: "huggingface"
url: "https://huggingface.co/datasets/HPLT/OpenLID-v3"
downloads: 284
summary: "OpenLID-v3는 194개 언어 변종의 언어 식별 모델 학습용 데이터셋입니다."
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
  - "[[장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# HPLT/OpenLID-v3

> dataset · [Hugging Face](https://huggingface.co/datasets/HPLT/OpenLID-v3)

OpenLID-v3는 194개 언어 변종의 언어 식별 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each entry in the dataset consists of a line of data (`text`), a language label` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `a language label consisting of an ISO 639-3 language code plus an ISO 15924 script code (`language`)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `273 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `9425` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `language identification models` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset is intended for training high-coverage language identification models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 37700자 ≈ 9425 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[HPLT__OpenLID-v3|HPLT/OpenLID-v3]]
