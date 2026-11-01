---
type: "model"
id: "tobykim/koelectra-44emotions"
source: "huggingface"
url: "https://huggingface.co/tobykim/koelectra-44emotions"
downloads: 126
context_length: 512
parameters_b: 0.113
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
model_size:
  - "[[초경량 모델]]"
---
# tobykim/koelectra-44emotions

> model · [Hugging Face](https://huggingface.co/tobykim/koelectra-44emotions)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — metadata · context_length = `512` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.113` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]]

## 학습 데이터

- [[searle-j__kote|searle-j/kote]]
