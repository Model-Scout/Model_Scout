---
type: "dataset"
id: "rajpurkar/squad_v2"
source: "huggingface"
url: "https://huggingface.co/datasets/rajpurkar/squad_v2"
downloads: 48090
summary: "SQuAD 2.0은 위키피디아 문서 기반의 질문응답 데이터셋으로, 답변이 없을 수도 있음."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
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
# rajpurkar/squad_v2

> dataset · [Hugging Face](https://huggingface.co/datasets/rajpurkar/squad_v2)

SQuAD 2.0은 위키피디아 문서 기반의 질문응답 데이터셋으로, 답변이 없을 수도 있음.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `questions posed by crowdworkers on a set of Wikipedia articles` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `the answer to every question is a segment of text, or span, from the corresponding reading passage` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `314` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `questions posed by crowdworkers on a set of Wikipedia articles` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `SQuAD 2.0 combines the 100,000 questions in SQuAD1.1 with over 50,000 unanswerable questions` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 1257자 ≈ 314 토큰 (viewer statistics, squad_v2/validation)

## 이 데이터로 학습한 모델

- [[timpal0l__mdeberta-v3-base-squad2|timpal0l/mdeberta-v3-base-squad2]]
