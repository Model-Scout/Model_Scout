---
type: "model"
id: "BCCard/MoAI-Embedding-0.6B"
source: "huggingface"
url: "https://huggingface.co/BCCard/MoAI-Embedding-0.6B"
downloads: 139
context_length: 32768
parameters_b: 0.596
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# BCCard/MoAI-Embedding-0.6B

> model · [Hugging Face](https://huggingface.co/BCCard/MoAI-Embedding-0.6B)

## 분류

- **작업**: [[임베딩]] — metadata · task.matched = `sentence-similarity` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `32768` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.596` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[BCCard__BCAI-Finance-Kor-Embedding-Pair|BCCard/BCAI-Finance-Kor-Embedding-Pair]]
- [[BCCard__BCAI-Finance-Kor-Embedding-Triplet|BCCard/BCAI-Finance-Kor-Embedding-Triplet]]
