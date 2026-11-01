---
type: "dataset"
id: "pviechn1/ParaBLoCC"
source: "huggingface"
url: "https://huggingface.co/datasets/pviechn1/ParaBLoCC"
downloads: 241
summary: "영어와 26개 언어의 병렬 기본 위치 구문을 포함한 다국어 말뭉치입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[번역]]"
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
  - "[[학습용]]"
---
# pviechn1/ParaBLoCC

> dataset · [Hugging Face](https://huggingface.co/datasets/pviechn1/ParaBLoCC)

영어와 26개 언어의 병렬 기본 위치 구문을 포함한 다국어 말뭉치입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `zero-shot-classification` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:translation = `Parallel basic locative constructions in English and 26 target languages.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Parallel basic locative constructions in English and 26 target languages.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `27 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Parallel basic locative constructions in English and 26 target languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `the first multilingual compendium of this important grammatico-functional construction` · 신뢰도 low
