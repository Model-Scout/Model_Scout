---
type: "dataset"
id: "SajjadAyoubi/persian_qa"
source: "huggingface"
url: "https://huggingface.co/datasets/SajjadAyoubi/persian_qa"
downloads: 191
summary: "페르시아어 위키백과 기반의 질문응답 데이터셋으로, 읽기 이해 및 질문응답 모델 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# SajjadAyoubi/persian_qa

> dataset · [Hugging Face](https://huggingface.co/datasets/SajjadAyoubi/persian_qa)

페르시아어 위키백과 기반의 질문응답 데이터셋으로, 읽기 이해 및 질문응답 모델 학습에 사용됨.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Persian Question Answering (PersianQA) Dataset is a reading comprehension dataset on Persian Wikipedia.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Each entry can be either an impossible to answer or a question with one or more answers spanning in the passage (the context)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Each entry can be either an impossible to answer or a question with one or more answers spanning in the passage (the context)` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `274` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Persian Question Answering (PersianQA) Dataset is a reading comprehension dataset on Persian Wikipedia.` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `At the moment, each context has 7 pairs of questions with one answer and 3 impossible questions.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The crowd-sourced dataset consists of more than 9,000 entries.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 1098자 ≈ 274 토큰 (viewer statistics, persian_qa/validation)

## 이 데이터로 학습한 모델

- [[Msobhi__Persian_Sentence_Embedding_v3|Msobhi/Persian_Sentence_Embedding_v3]]
