---
type: "dataset"
id: "allenai/WildChat"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/WildChat"
downloads: 3626
summary: "WildChat은 인간과 ChatGPT 간 65만 대화 모음으로, 교육 및 사용자 행동 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
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
# allenai/WildChat

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/WildChat)

WildChat은 인간과 ChatGPT 간 65만 대화 모음으로, 교육 및 사용자 행동 연구에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `The dataset contains a broad spectrum of user-chatbot interactions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `ChatGPT responses` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Language(s) (NLP): multi-lingual` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `WildChat can serve both as a dataset for instructional fine-tuning and as a valuable resource for studying user behaviors.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[llm-semantic-router__mmbert32k-modality-router-merged|llm-semantic-router/mmbert32k-modality-router-merged]]
