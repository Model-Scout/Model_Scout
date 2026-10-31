---
type: "dataset"
id: "Gholamreza/pquad"
source: "huggingface"
url: "https://huggingface.co/datasets/Gholamreza/pquad"
downloads: 88
summary: "페르시아어 위키백과 기반 독해 질문-응답 데이터셋으로, 독해 및 질의응답 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[fa]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Gholamreza/pquad

> dataset · [Hugging Face](https://huggingface.co/datasets/Gholamreza/pquad)

페르시아어 위키백과 기반 독해 질문-응답 데이터셋으로, 독해 및 질의응답 연구에 활용됨.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering = `PQuAD is stored in the JSON format and consists of passages where each passage is linked to a set of questions.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Answer(s) of the questions is specified with answer's span (start and end point of answer in paragraph).` · 신뢰도 medium
- **언어**: [[fa]] — metadata · languages = `fa` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `PQuAD's questions are based on Persian Wikipedia articles and cover a wide variety of subjects.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset is divided into three categories including train, validation, and test sets` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Msobhi__Persian_Sentence_Embedding_v3|Msobhi/Persian_Sentence_Embedding_v3]]
