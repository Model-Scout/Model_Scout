---
type: "dataset"
id: "jobs-git/HPLT2.0_cleaned"
source: "huggingface"
url: "https://huggingface.co/datasets/jobs-git/HPLT2.0_cleaned"
downloads: 836
summary: "191개 언어로 된 대규모 웹 크롤링 문서 모음으로, 다국어 언어 모델 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
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
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# jobs-git/HPLT2.0_cleaned

> dataset · [Hugging Face](https://huggingface.co/datasets/jobs-git/HPLT2.0_cleaned)

191개 언어로 된 대규모 웹 크롤링 문서 모음으로, 다국어 언어 모델 학습에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `compared the utility of various multilingual corpora for training large language models` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:language_modeling = `web-crawled documents` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `training large language models` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `186 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a large-scale collection of web-crawled documents in 191 world languages` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `training large language models with the same architecture and pretraining configuration` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `inf` · 신뢰도 high
