---
type: "dataset"
id: "HPLT/HPLT2.0_cleaned"
source: "huggingface"
url: "https://huggingface.co/datasets/HPLT/HPLT2.0_cleaned"
downloads: 213857
summary: "HPLT 프로젝트가 제작한 191개 언어의 웹 크롤링 문서 대규모 데이터셋으로, 언어 모델 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
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
dataset_size:
  - "[[초대규모 데이터]]"
---
# HPLT/HPLT2.0_cleaned

> dataset · [Hugging Face](https://huggingface.co/datasets/HPLT/HPLT2.0_cleaned)

HPLT 프로젝트가 제작한 191개 언어의 웹 크롤링 문서 대규모 데이터셋으로, 언어 모델 학습에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `This is a large-scale collection of web-crawled documents in 191 world languages` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — metadata · modality = `timeseries` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `We train 1.7B decoder-only LMs using 100B/30B tokens sampled from the English/Norwegian parts of our HPLT v2 dataset respectively.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `186 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a large-scale collection of web-crawled documents in 191 world languages, produced by the HPLT project.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `We train 1.7B decoder-only LMs using 100B/30B tokens sampled from the English/Norwegian parts of our HPLT v2 dataset respectively.` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high
