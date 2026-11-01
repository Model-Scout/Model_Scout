---
type: "model"
id: "bespin-global/klue-sentence-roberta-base-kornlu"
source: "huggingface"
url: "https://huggingface.co/bespin-global/klue-sentence-roberta-base-kornlu"
downloads: 108
context_length: 514
parameters_b: 0.11
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
model_size:
  - "[[초경량 모델]]"
---
# bespin-global/klue-sentence-roberta-base-kornlu

> model · [Hugging Face](https://huggingface.co/bespin-global/klue-sentence-roberta-base-kornlu)

## 분류

- **작업**: [[임베딩]] — metadata · task.matched = `sentence-similarity` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **입력 길이**: [[중문]] — metadata · context_length = `514` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.11` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[kakaobrain__kor_nlu|kakaobrain/kor_nlu]]
