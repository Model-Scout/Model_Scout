---
type: "model"
id: "Infinity08/KAWK-500M-Korean-Instruct-v1"
source: "huggingface"
url: "https://huggingface.co/Infinity08/KAWK-500M-Korean-Instruct-v1"
downloads: 229
context_length: 2048
parameters_b: 0.505
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
model_size:
  - "[[초경량 모델]]"
---
# Infinity08/KAWK-500M-Korean-Instruct-v1

> model · [Hugging Face](https://huggingface.co/Infinity08/KAWK-500M-Korean-Instruct-v1)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `2048` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.505` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[Infinity08__KAWK500M-Korean-Pretraining-10B|Infinity08/KAWK500M-Korean-Pretraining-10B]]
- [[Infinity08__KAWK500M-Korean-SFT-v1|Infinity08/KAWK500M-Korean-SFT-v1]]
