---
type: "dataset"
id: "tau/commonsense_qa"
source: "huggingface"
url: "https://huggingface.co/datasets/tau/commonsense_qa"
downloads: 126258
summary: "CommonsenseQA는 상식 지식을 필요로 하는 객관식 질문 답변 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
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
# tau/commonsense_qa

> dataset · [Hugging Face](https://huggingface.co/datasets/tau/commonsense_qa)

CommonsenseQA는 상식 지식을 필요로 하는 객관식 질문 답변 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `multiple-choice question answering dataset` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `multiple-choice question answering dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `predict the correct answers` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `27` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `CommonsenseQA is a new multiple-choice question answering dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `It contains 12,102 questions with one correct answer and four distractor answers.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 108자 ≈ 27 토큰 (viewer statistics, default/validation)
