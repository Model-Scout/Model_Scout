---
type: "dataset"
id: "hackaprompt/hackaprompt-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset"
downloads: 1137
summary: "프롬프트 해킹 대회 제출물을 모은 데이터셋으로 분석 연구에 활용됨."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# hackaprompt/hackaprompt-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset)

프롬프트 해킹 대회 제출물을 모은 데이터셋으로 분석 연구에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `This dataset contains submissions from a prompt hacking competition.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `This dataset contains submissions from a prompt hacking competition.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `This dataset contains submissions from a prompt hacking competition.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `An in-depth analysis of the dataset has been accepted at the EMNLP 2023 conference.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Submissions were sourced from two environments: a playground for experimentation and an official submissions platform.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Verm1ion__injection-sentry-xlmr|Verm1ion/injection-sentry-xlmr]]
