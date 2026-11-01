---
type: "dataset"
id: "NLPatVCU/korean_proverb"
source: "huggingface"
url: "https://huggingface.co/datasets/NLPatVCU/korean_proverb"
downloads: 76
summary: "우리말샘 속담을 영어로 기계번역한 데이터셋으로, 속담 번역 및 의미 추론에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# NLPatVCU/korean_proverb

> dataset · [Hugging Face](https://huggingface.co/datasets/NLPatVCU/korean_proverb)

우리말샘 속담을 영어로 기계번역한 데이터셋으로, 속담 번역 및 의미 추론에 활용됨

## 분류

- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `Every proverb (속담) entry in the Urimalsaem dictionary (우리말샘, National Institute of Korean Language)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `English translation of the proverb, thinking off` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Every proverb (속담) entry in the Urimalsaem dictionary (우리말샘, National Institute of Korean Language)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
