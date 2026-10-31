---
type: "model"
id: "juyoungml/bge-m3-ko-v1.1"
source: "huggingface"
url: "https://huggingface.co/juyoungml/bge-m3-ko-v1.1"
downloads: 81
context_length: 8194
parameters_b: 0.568
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
model_size:
  - "[[초경량 모델]]"
---
# juyoungml/bge-m3-ko-v1.1

> model · [Hugging Face](https://huggingface.co/juyoungml/bge-m3-ko-v1.1)

## 분류

- **작업**: [[임베딩]] — metadata · task.matched = `sentence-similarity` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — metadata · context_length = `8194` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.568` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]]

## 학습 데이터

- [[nlpai-lab__ko-triplet-v1.0|nlpai-lab/ko-triplet-v1.0]]
