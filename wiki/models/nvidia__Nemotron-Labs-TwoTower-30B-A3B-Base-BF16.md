---
type: "model"
id: "nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16"
source: "huggingface"
url: "https://huggingface.co/nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16"
downloads: 548
context_length: 262144
parameters_b: 63.186
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
  - "[[극장문]]"
commercial_use:
  - "[[조건부 이용]]"
model_size:
  - "[[대형 모델]]"
---
# nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16

> model · [Hugging Face](https://huggingface.co/nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `16 languages` · 신뢰도 high
- **입력 길이**: [[극장문]] — metadata · context_length = `262144` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **모델 크기**: [[대형 모델]] — metadata · parameter_count_billion = `63.186` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]] · [[극장문]]

## 학습 데이터

- [[nvidia__Nemotron-CC-Code-v1|nvidia/Nemotron-CC-Code-v1]]
- [[nvidia__Nemotron-CC-Math-v1|nvidia/Nemotron-CC-Math-v1]]
- [[nvidia__Nemotron-CC-v2|nvidia/Nemotron-CC-v2]]
- [[nvidia__Nemotron-CC-v2.1|nvidia/Nemotron-CC-v2.1]]
- [[nvidia__Nemotron-Pretraining-Code-v1|nvidia/Nemotron-Pretraining-Code-v1]]
- [[nvidia__Nemotron-Pretraining-Code-v2|nvidia/Nemotron-Pretraining-Code-v2]]
- [[nvidia__Nemotron-Pretraining-Dataset-sample|nvidia/Nemotron-Pretraining-Dataset-sample]]
- [[nvidia__Nemotron-Pretraining-SFT-v1|nvidia/Nemotron-Pretraining-SFT-v1]]
- [[nvidia__Nemotron-Pretraining-Specialized-v1|nvidia/Nemotron-Pretraining-Specialized-v1]]
