---
type: "model"
id: "nvidia/NVIDIA-Nemotron-Nano-12B-v2-Base"
source: "huggingface"
url: "https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-Base"
downloads: 5153
context_length: 131072
parameters_b: 12.31
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
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
model_size:
  - "[[중형 모델]]"
---
# nvidia/NVIDIA-Nemotron-Nano-12B-v2-Base

> model · [Hugging Face](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-Base)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `16 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `131072` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **모델 크기**: [[중형 모델]] — metadata · parameter_count_billion = `12.31` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[nvidia__Nemotron-CC-Math-v1|nvidia/Nemotron-CC-Math-v1]]
- [[nvidia__Nemotron-CC-v2|nvidia/Nemotron-CC-v2]]
- [[nvidia__Nemotron-Pretraining-Code-v1|nvidia/Nemotron-Pretraining-Code-v1]]
- [[nvidia__Nemotron-Pretraining-Dataset-sample|nvidia/Nemotron-Pretraining-Dataset-sample]]
- [[nvidia__Nemotron-Pretraining-SFT-v1|nvidia/Nemotron-Pretraining-SFT-v1]]
