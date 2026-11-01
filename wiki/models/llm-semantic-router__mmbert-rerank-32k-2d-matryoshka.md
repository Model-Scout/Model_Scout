---
type: "model"
id: "llm-semantic-router/mmbert-rerank-32k-2d-matryoshka"
source: "huggingface"
url: "https://huggingface.co/llm-semantic-router/mmbert-rerank-32k-2d-matryoshka"
downloads: 100
context_length: 32768
parameters_b: 0.307
task:
  - "[[텍스트 분류]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[hi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# llm-semantic-router/mmbert-rerank-32k-2d-matryoshka

> model · [Hugging Face](https://huggingface.co/llm-semantic-router/mmbert-rerank-32k-2d-matryoshka)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **작업**: [[리랭킹]] — name_rule · model_id = `reranking` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:reranking = `text` · 신뢰도 medium
- **언어**: [[ar]] — metadata · language_codes = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · language_codes = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · language_codes = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · language_codes = `fr` · 신뢰도 high
- **언어**: [[hi]] — metadata · language_codes = `hi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · language_codes = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `10 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · language_codes = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · language_codes = `zh` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `32768` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.307` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]
