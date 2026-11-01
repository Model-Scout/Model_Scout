---
type: "dataset"
id: "swiss-ai/MSafeTemp"
source: "huggingface"
url: "https://huggingface.co/datasets/swiss-ai/MSafeTemp"
downloads: 125
summary: "MSafeTemp는 60개 언어의 유해 프롬프트 기반 다국어 안전성 훈련 및 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# swiss-ai/MSafeTemp

> dataset · [Hugging Face](https://huggingface.co/datasets/swiss-ai/MSafeTemp)

MSafeTemp는 60개 언어의 유해 프롬프트 기반 다국어 안전성 훈련 및 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `MSafeTemp is released to train and evaluate safer multilingual models: refusal training on harmful prompts, over-refusal control on benign pairs, and evaluation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `English harmful seed prompts are turned into safe templates with typed slots, the templates are translated, and the slots are filled again in every language.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `English harmful seed prompts are turned into safe templates with typed slots, the templates are translated, and the slots are filled again in every language.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `60 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MSafeTemp is the dataset of "How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates"` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = ``wildguard` | WildGuardMix, 500 source prompts | `test` | 368,820 | 44 | evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = ``wildguard` | WildGuardMix, 2,000 source prompts | `train` | 1,551,799 | 44 | safety training` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
