---
type: "model"
id: "daekeun-ml/koelectra-small-v3-nsmc"
source: "huggingface"
url: "https://huggingface.co/daekeun-ml/koelectra-small-v3-nsmc"
downloads: 1465292
context_length: 512
parameters_b: 0.014
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# daekeun-ml/koelectra-small-v3-nsmc

> model · [Hugging Face](https://huggingface.co/daekeun-ml/koelectra-small-v3-nsmc)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — metadata · context_length = `512` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.014` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]]

## 학습 데이터

- [[e9t__nsmc|e9t/nsmc]]
