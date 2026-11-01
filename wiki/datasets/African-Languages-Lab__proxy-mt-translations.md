---
type: "dataset"
id: "African-Languages-Lab/proxy-mt-translations"
source: "huggingface"
url: "https://huggingface.co/datasets/African-Languages-Lab/proxy-mt-translations"
downloads: 40
summary: "영어에서 119개 언어로 50개 LLM이 생성한 기계 번역 결과 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# African-Languages-Lab/proxy-mt-translations

> dataset · [Hugging Face](https://huggingface.co/datasets/African-Languages-Lab/proxy-mt-translations)

영어에서 119개 언어로 50개 LLM이 생성한 기계 번역 결과 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `English source sentence` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `model-generated translation` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `92 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `English→X machine translations generated with vLLM across 50 open-weight LLMs on three evaluation benchmarks.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset holds the raw model outputs (one CSV per model × dataset × target language)` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
