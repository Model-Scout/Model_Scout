---
type: "dataset"
id: "beomi/kowikitext-qa-ref-detail-preview"
source: "huggingface"
url: "https://huggingface.co/datasets/beomi/kowikitext-qa-ref-detail-preview"
downloads: 8
summary: "한국어 위키피디아 텍스트를 추론 과정이 포함된 QA 형식으로 변환한 데이터셋입니다."
readme_status: "thin"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# beomi/kowikitext-qa-ref-detail-preview

> dataset · [Hugging Face](https://huggingface.co/datasets/beomi/kowikitext-qa-ref-detail-preview)

한국어 위키피디아 텍스트를 추론 과정이 포함된 QA 형식으로 변환한 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Korean Wikipedia texts into QA-like with reasoning process dataset.` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Korean Wikipedia texts` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `QA-like with reasoning process dataset` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Wikipedia texts` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This release is preview released.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[idah4__etm-korean-tiny|idah4/etm-korean-tiny]]
