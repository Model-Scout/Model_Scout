---
type: "dataset"
id: "m-a-p/CodeFeedback-Filtered-Instruction"
source: "huggingface"
url: "https://huggingface.co/datasets/m-a-p/CodeFeedback-Filtered-Instruction"
downloads: 22241
summary: "OpenCodeInterpreter의 코드 생성 및 실행 기능을 위한 고품질 코드 명령어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
# m-a-p/CodeFeedback-Filtered-Instruction

> dataset · [Hugging Face](https://huggingface.co/datasets/m-a-p/CodeFeedback-Filtered-Instruction)

OpenCodeInterpreter의 코드 생성 및 실행 기능을 위한 고품질 코드 명령어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The code queries are evaluated along with their corresponding responses within the compiled datasets by the LLM, assigning a complexity score ranging from 1 to ` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `OpenCodeInterpreter is a family of open-source code generation systems` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `code instruction queries extracted from four prominent open-source code instruction tuning datasets` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `we retained all responses to provide users with more convenient usage options` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `714` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `OpenCodeInterpreter is a family of open-source code generation systems designed to bridge the gap between large language models and advanced proprietary systems` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `a final collection of 156k high-quality single-turn code instructions` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 2857자 ≈ 714 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[FINAL-Bench__Darwin-28B-Coder|FINAL-Bench/Darwin-28B-Coder]]
- [[usermma__Darwin-28B-Coder-mlx-fp16|usermma/Darwin-28B-Coder-mlx-fp16]]
