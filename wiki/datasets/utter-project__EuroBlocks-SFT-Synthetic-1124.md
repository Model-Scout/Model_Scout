---
type: "dataset"
id: "utter-project/EuroBlocks-SFT-Synthetic-1124"
source: "huggingface"
url: "https://huggingface.co/datasets/utter-project/EuroBlocks-SFT-Synthetic-1124"
downloads: 134
summary: "EuroLLM 9B Instruct 학습용으로 제작된 다국어 합성 SFT 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# utter-project/EuroBlocks-SFT-Synthetic-1124

> dataset · [Hugging Face](https://huggingface.co/datasets/utter-project/EuroBlocks-SFT-Synthetic-1124)

EuroLLM 9B Instruct 학습용으로 제작된 다국어 합성 SFT 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Synthethic data used to train EuroLLM 9B Instruct.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `List with messages (from both user and assistant)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `language of the instruction/answer` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `EuroLLM Synthetic SFT data` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Synthethic data used to train EuroLLM 9B Instruct.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[martinsu__tildeopen-30b-mu-instruct|martinsu/tildeopen-30b-mu-instruct]]
