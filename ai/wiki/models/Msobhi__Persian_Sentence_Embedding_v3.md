---
type: "model"
id: "Msobhi/Persian_Sentence_Embedding_v3"
source: "huggingface"
url: "https://huggingface.co/Msobhi/Persian_Sentence_Embedding_v3"
downloads: 585
context_length: 514
parameters_b: 0.56
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
model_size:
  - "[[초경량 모델]]"
---
# Msobhi/Persian_Sentence_Embedding_v3

> model · [Hugging Face](https://huggingface.co/Msobhi/Persian_Sentence_Embedding_v3)

## 분류

- **작업**: [[임베딩]] — metadata · task.matched = `sentence-similarity` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `16 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `514` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.56` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[Gholamreza__pquad|Gholamreza/pquad]]
- [[SajjadAyoubi__persian_qa|SajjadAyoubi/persian_qa]]
- [[persiannlp__parsinlu_entailment|persiannlp/parsinlu_entailment]]
- [[sentence-transformers__miracl|sentence-transformers/miracl]]
- [[sinarashidi__alpaca-persian|sinarashidi/alpaca-persian]]
