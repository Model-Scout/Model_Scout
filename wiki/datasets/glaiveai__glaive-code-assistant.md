---
type: "dataset"
id: "glaiveai/glaive-code-assistant"
source: "huggingface"
url: "https://huggingface.co/datasets/glaiveai/glaive-code-assistant"
downloads: 944
summary: "Glaive-code-assistant는 약 14만 개의 코드 문제와 해답으로 구성된 코드 어시스턴트용 QA 형식 데이터셋입니다."
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
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# glaiveai/glaive-code-assistant

> dataset · [Hugging Face](https://huggingface.co/datasets/glaiveai/glaive-code-assistant)

Glaive-code-assistant는 약 14만 개의 코드 문제와 해답으로 구성된 코드 어시스턴트용 QA 형식 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `The data is structured in a QA format where the questions are worded similar to how real users will ask code related questions.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `the questions are worded similar to how real users will ask code related questions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `code problems and solutions` · 신뢰도 medium
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `592` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The data is intended to be used to make models act as code assistants` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The data is intended to be used to make models act as code assistants` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 2367자 ≈ 592 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[yasserrmd__Coder-GRPO-3B|yasserrmd/Coder-GRPO-3B]]
