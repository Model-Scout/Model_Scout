---
type: "model"
id: "cadazar/han2han-it"
source: "huggingface"
url: "https://huggingface.co/cadazar/han2han-it"
downloads: 187
context_length: 2048
parameters_b: 0.189
task:
  - "[[임베딩]]"
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
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# cadazar/han2han-it

> model · [Hugging Face](https://huggingface.co/cadazar/han2han-it)

## 분류

- **작업**: [[임베딩]] — metadata · task.matched = `feature-extraction` · 신뢰도 high
- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `2048` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.189` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[seyoungsong__Open-Korean-Historical-Corpus|seyoungsong/Open-Korean-Historical-Corpus]]
