---
type: "model"
id: "blueapple8259/TinyKo"
source: "huggingface"
url: "https://huggingface.co/blueapple8259/TinyKo"
downloads: 173
context_length: 16384
parameters_b: 0.026
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[비상업 전용]]"
model_size:
  - "[[초경량 모델]]"
---
# blueapple8259/TinyKo

> model · [Hugging Face](https://huggingface.co/blueapple8259/TinyKo)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — metadata · context_length = `16384` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.026` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]]

## 학습 데이터

- [[Bingsu__ko_alpaca_data|Bingsu/ko_alpaca_data]]
- [[beomi__KoAlpaca-v1.1a|beomi/KoAlpaca-v1.1a]]
- [[klue__klue|klue/klue]]
- [[maywell__ko_wikidata_QA|maywell/ko_wikidata_QA]]
