---
type: "dataset"
id: "luizapzbn/from-one-to-many-toxicity-mitigation"
source: "huggingface"
url: "https://huggingface.co/datasets/luizapzbn/from-one-to-many-toxicity-mitigation"
downloads: 130
summary: "다국어 독성 완화 연구를 위한 번역된 독성 데이터셋으로, 언어 모델의 안전성 향상에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[hi]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[ru]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
---
# luizapzbn/from-one-to-many-toxicity-mitigation

> dataset · [Hugging Face](https://huggingface.co/datasets/luizapzbn/from-one-to-many-toxicity-mitigation)

다국어 독성 완화 연구를 위한 번역된 독성 데이터셋으로, 언어 모델의 안전성 향상에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `toxicity classification` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `toxicity classification` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `toxicity mitigation in language models has almost entirely been focused on single-language settings` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `eval: a random subset of 200 samples of holistic bias (English) translated with Google Translate to each of the target languages.` · 신뢰도 medium
