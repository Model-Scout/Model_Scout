---
type: "model"
id: "north-wind/TinyStories-Korean-800K"
source: "huggingface"
url: "https://huggingface.co/north-wind/TinyStories-Korean-800K"
downloads: 157
context_length: 512
parameters_b: 0.001
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# north-wind/TinyStories-Korean-800K

> model · [Hugging Face](https://huggingface.co/north-wind/TinyStories-Korean-800K)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — metadata · context_length = `512` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.001` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]]

## 학습 데이터

- [[g0ster__TinyStories-Korean|g0ster/TinyStories-Korean]]
