---
type: "model"
id: "Huffon/klue-roberta-base-nli"
source: "huggingface"
url: "https://huggingface.co/Huffon/klue-roberta-base-nli"
downloads: 1325
context_length: 512
parameters_b: 0.11
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
# Huffon/klue-roberta-base-nli

> model · [Hugging Face](https://huggingface.co/Huffon/klue-roberta-base-nli)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — metadata · context_length = `512` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.11` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]]

## 학습 데이터

- [[klue__klue|klue/klue]]
