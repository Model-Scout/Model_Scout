---
type: "model"
id: "likeyellow/klue-review-star"
source: "huggingface"
url: "https://huggingface.co/likeyellow/klue-review-star"
downloads: 185
context_length: 512
parameters_b: 0.111
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
model_size:
  - "[[초경량 모델]]"
---
# likeyellow/klue-review-star

> model · [Hugging Face](https://huggingface.co/likeyellow/klue-review-star)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — metadata · context_length = `512` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.111` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]]

## 학습 데이터

- [[leey4n__KR3|leey4n/KR3]]
