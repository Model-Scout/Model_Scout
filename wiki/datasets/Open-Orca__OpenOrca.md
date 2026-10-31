---
type: "dataset"
id: "Open-Orca/OpenOrca"
source: "huggingface"
url: "https://huggingface.co/datasets/Open-Orca/OpenOrca"
downloads: 12999
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
  - "[[요약]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Open-Orca/OpenOrca

> dataset · [Hugging Face](https://huggingface.co/datasets/Open-Orca/OpenOrca)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 high
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 high
- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 high
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 high
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding, task:generation, task:information_extraction, task:question_answering, task:summarization, task:table_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:summarization, task:table_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[daekeun-ml__phi-2-ko-v0.1|daekeun-ml/phi-2-ko-v0.1]]
