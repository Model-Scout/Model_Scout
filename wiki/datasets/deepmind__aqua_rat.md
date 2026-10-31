---
type: "dataset"
id: "deepmind/aqua_rat"
source: "huggingface"
url: "https://huggingface.co/datasets/deepmind/aqua_rat"
downloads: 19455
summary: "약 10만 개의 대수학 문제와 단계별 해설로 구성된 데이터셋으로, 문제 해결 프로그램 생성 학습에 사용됨."
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
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# deepmind/aqua_rat

> dataset · [Hugging Face](https://huggingface.co/datasets/deepmind/aqua_rat)

약 10만 개의 대수학 문제와 단계별 해설로 구성된 데이터셋으로, 문제 해결 프로그램 생성 학습에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This data is used to train a program generation model that learns to generate the explanation, while generating the program that solves the question.` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories, task_ids = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `- `question` : (str) A natural language definition of the problem to solve` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `- `rationale` : (str) A natural language description of the solution to the problem` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `84` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `A large-scale dataset consisting of approximately 100,000 algebraic word problems.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `| Examples | 97467 | 254 | 254 |` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 337자 ≈ 84 토큰 (viewer statistics, raw/validation)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
