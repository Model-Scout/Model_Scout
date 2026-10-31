---
type: "model"
id: "atonlee/supra-ko-pii-router"
source: "huggingface"
url: "https://huggingface.co/atonlee/supra-ko-pii-router"
downloads: 813
context_length: 5120
parameters_b: 0.052
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# atonlee/supra-ko-pii-router

> model · [Hugging Face](https://huggingface.co/atonlee/supra-ko-pii-router)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — metadata · context_length = `5120` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.052` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]]

## 학습 데이터

- [[BCCard__privacy-filter-openpii-masking|BCCard/privacy-filter-openpii-masking]]
- [[atonlee__Prompt-Routing-Dataset-ko|atonlee/Prompt-Routing-Dataset-ko]]
- [[townboy__korean-pii-dataset|townboy/korean-pii-dataset]]
