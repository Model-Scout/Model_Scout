---
type: "dataset"
id: "hyokwan/common"
source: "huggingface"
url: "https://huggingface.co/datasets/hyokwan/common"
downloads: 25
summary: "이 데이터셋은 한국어 문서 요약을 위한 데이터입니다."
readme_status: "thin"
readme_language: "en"
korean_focus: "not_ko"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# hyokwan/common

> dataset · [Hugging Face](https://huggingface.co/datasets/hyokwan/common)

이 데이터셋은 한국어 문서 요약을 위한 데이터입니다.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `25` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 99자 ≈ 25 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[tensorblock__hyokwan_familidata_gemma7b-GGUF|tensorblock/hyokwan_familidata_gemma7b-GGUF]]
