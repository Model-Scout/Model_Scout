---
type: "dataset"
id: "werty1248/multilingual-instruct-balanced"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/multilingual-instruct-balanced"
downloads: 102
summary: "영어, 한국어, 중국어, 일본어 데이터셋을 통합하여 언어별 균형을 맞춘 다국어 명령어 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# werty1248/multilingual-instruct-balanced

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/multilingual-instruct-balanced)

영어, 한국어, 중국어, 일본어 데이터셋을 통합하여 언어별 균형을 맞춘 다국어 명령어 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `English, Korean, Chinese, and Japanese datasets collected by the HuggingFace Hub and transformed into a unified format` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `a collection of English, Korean, Chinese, and Japanese datasets collected by the HuggingFace Hub and transformed into a unified format` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This repository is a collection of English, Korean, Chinese, and Japanese datasets collected by the HuggingFace Hub` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
