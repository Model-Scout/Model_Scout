---
type: "model"
id: "google/madlad400-8b-lm"
source: "huggingface"
url: "https://huggingface.co/google/madlad400-8b-lm"
downloads: 465
context_length: 512
parameters_b: 8.634
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[중형 모델]]"
---
# google/madlad400-8b-lm

> model · [Hugging Face](https://huggingface.co/google/madlad400-8b-lm)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `417 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — metadata · context_length = `512` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[중형 모델]] — metadata · parameter_count_billion = `8.634` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]]

## 학습 데이터

- [[allenai__MADLAD-400|allenai/MADLAD-400]]
