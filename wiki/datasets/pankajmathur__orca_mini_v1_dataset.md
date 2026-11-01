---
type: "dataset"
id: "pankajmathur/orca_mini_v1_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/pankajmathur/orca_mini_v1_dataset"
downloads: 172
summary: "Orca 스타일 데이터셋으로, 기본 모델 미세조정에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# pankajmathur/orca_mini_v1_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/pankajmathur/orca_mini_v1_dataset)

Orca 스타일 데이터셋으로, 기본 모델 미세조정에 사용됨.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `prompt format.
### System:
<system>

### User:
<instruction>` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `### Assistant:
<output>` · 신뢰도 low
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `544` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `can be used to fine tuned base models` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 2175자 ≈ 544 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[pankajmathur__RenCoder-Ministral-8B-Instruct-2410-GGUF|pankajmathur/RenCoder-Ministral-8B-Instruct-2410-GGUF]]
