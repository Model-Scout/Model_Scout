---
type: "dataset"
id: "google/boolq"
source: "huggingface"
url: "https://huggingface.co/datasets/google/boolq"
downloads: 87314
summary: "BoolQ는 자연 발생적인 예/아니오 질문에 답하는 질의응답 데이터셋입니다."
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
# google/boolq

> dataset · [Hugging Face](https://huggingface.co/datasets/google/boolq)

BoolQ는 자연 발생적인 예/아니오 질문에 답하는 질의응답 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **작업**: [[질의응답]] — ner · readme = `BoolQ is a question answering dataset for yes/no questions containing 15942 examples.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `Each example is a triplet of (question, passage, answer), with the title of the page as optional additional context.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Each example is a triplet of (question, passage, answer), with the title of the page as optional additional context.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `242` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `These questions are naturally occurring ---they are generated in unprompted and unconstrained settings.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `BoolQ is a question answering dataset for yes/no questions containing 15942 examples.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `passage` 열 p90 969자 ≈ 242 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
