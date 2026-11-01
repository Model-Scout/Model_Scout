---
type: "dataset"
id: "Bryan35406/agi-trilogy"
source: "huggingface"
url: "https://huggingface.co/datasets/Bryan35406/agi-trilogy"
downloads: 57
summary: "AGI 도래를 주제로 한 한·영 병렬 단편 소설 데이터셋으로 AI 학습용임."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Bryan35406/agi-trilogy

> dataset · [Hugging Face](https://huggingface.co/datasets/Bryan35406/agi-trilogy)

AGI 도래를 주제로 한 한·영 병렬 단편 소설 데이터셋으로 AI 학습용임.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `Korean originals, Markdown` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `Korean originals, Markdown` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Three short stories and a companion piece on the arrival of AGI — three countries, three tenses that do not translate into one another.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `use of this dataset for machine learning and AI model training is expressly permitted` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
