---
type: "model"
id: "Dongjin-kr/ko-reranker"
source: "huggingface"
url: "https://huggingface.co/Dongjin-kr/ko-reranker"
downloads: 20437
context_length: 514
parameters_b: 0.56
task:
  - "[[텍스트 분류]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# Dongjin-kr/ko-reranker

> model · [Hugging Face](https://huggingface.co/Dongjin-kr/ko-reranker)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **작업**: [[리랭킹]] — name_rule · model_id = `reranking` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:reranking = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `514` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.56` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]
