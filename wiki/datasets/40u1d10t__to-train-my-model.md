---
type: "dataset"
id: "40u1d10t/to-train-my-model"
source: "huggingface"
url: "https://huggingface.co/datasets/40u1d10t/to-train-my-model"
downloads: 1172
summary: "75개 언어로 된 대규모 정제 다국어 데이터셋 CulturaY로 언어 모델 학습에 활용 가능"
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# 40u1d10t/to-train-my-model

> dataset · [Hugging Face](https://huggingface.co/datasets/40u1d10t/to-train-my-model)

75개 언어로 된 대규모 정제 다국어 데이터셋 CulturaY로 언어 모델 학습에 활용 가능

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_categories, task_ids = `fill-mask` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `The dataset has a total of 6 columns, including: - 2 columns `text, url` will be the two main columns in this dataset.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `- 2 columns `text, url` will be the two main columns in this dataset.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `75 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This data was copied from the HPLT project, which in turn used the data from Common Crawl and the Internet Archive.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high
