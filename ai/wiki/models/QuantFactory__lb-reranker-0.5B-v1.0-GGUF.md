---
type: "model"
id: "QuantFactory/lb-reranker-0.5B-v1.0-GGUF"
source: "huggingface"
url: "https://huggingface.co/QuantFactory/lb-reranker-0.5B-v1.0-GGUF"
downloads: 956
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
---
# QuantFactory/lb-reranker-0.5B-v1.0-GGUF

> model · [Hugging Face](https://huggingface.co/QuantFactory/lb-reranker-0.5B-v1.0-GGUF)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **작업**: [[리랭킹]] — name_rule · model_id = `reranking` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:reranking = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `96 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high

## 학습 데이터

- [[lightblue__reranker_continuous_filt_max7_train|lightblue/reranker_continuous_filt_max7_train]]
