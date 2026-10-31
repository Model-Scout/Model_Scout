---
type: "dataset"
id: "Gugu8/Scraped-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/Gugu8/Scraped-Data"
downloads: 36
summary: "1TB 목표로 지속 확장 중인 위키피디아 및 인터넷 아카이브 텍스트 크롤링 데이터셋입니다."
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# Gugu8/Scraped-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/Gugu8/Scraped-Data)

1TB 목표로 지속 확장 중인 위키피디아 및 인터넷 아카이브 텍스트 크롤링 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `A continuously-growing, cleaned text corpus scraped, parsed, cleaned, losslessly-zipped, and auto-pushed from a CPU-only Google Colab pipeline.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:language_modeling = `A continuously-growing, cleaned text corpus scraped, parsed, cleaned` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `cleaned plain-text body` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `24 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `A continuously-growing, cleaned text corpus scraped, parsed, cleaned, losslessly-zipped, and auto-pushed from a CPU-only Google Colab pipeline.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high
