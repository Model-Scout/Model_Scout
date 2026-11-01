---
type: "dataset"
id: "Multilingual-NLP/M-ABSA"
source: "huggingface"
url: "https://huggingface.co/datasets/Multilingual-NLP/M-ABSA"
downloads: 26706
summary: "M-ABSA는 21개 언어, 7개 도메인에 대한 다국어 관점 기반 감성 분석 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Multilingual-NLP/M-ABSA

> dataset · [Hugging Face](https://huggingface.co/datasets/Multilingual-NLP/M-ABSA)

M-ABSA는 21개 언어, 7개 도메인에 대한 다국어 관점 기반 감성 분석 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:information_extraction = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `21 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `158` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a dataset suitable for the multilingual ABSA task with triplet extraction.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Each dataset is divided into training, validation, and test sets.` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 631자 ≈ 158 토큰 (viewer statistics, default/validation)
