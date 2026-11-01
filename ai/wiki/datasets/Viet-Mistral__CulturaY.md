---
type: "dataset"
id: "Viet-Mistral/CulturaY"
source: "huggingface"
url: "https://huggingface.co/datasets/Viet-Mistral/CulturaY"
downloads: 4990
summary: "75개 언어의 대규모 정제된 다국어 텍스트 데이터셋으로, 머신러닝 연구용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# Viet-Mistral/CulturaY

> dataset · [Hugging Face](https://huggingface.co/datasets/Viet-Mistral/CulturaY)

75개 언어의 대규모 정제된 다국어 텍스트 데이터셋으로, 머신러닝 연구용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_categories, task_ids = `fill-mask` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `- 2 columns `text, url` will be the two main columns in this dataset.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `- 2 columns `text, url` will be the two main columns in this dataset.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `75 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4310` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This data was copied from the HPLT project, which in turn used the data from Common Crawl and the Internet Archive.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `We make the data available for fair use machine learning research.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 17238자 ≈ 4310 토큰 (viewer statistics, ko/train)

## 같은 데이터의 사본·중복 등록

- `40u1d10t/to-train-my-model`
