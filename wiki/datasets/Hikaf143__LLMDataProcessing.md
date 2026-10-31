---
type: "dataset"
id: "Hikaf143/LLMDataProcessing"
source: "huggingface"
url: "https://huggingface.co/datasets/Hikaf143/LLMDataProcessing"
downloads: 80
summary: "Common Crawl 원시 데이터를 전처리해 LLM 사전학습, SFT, DPO용 데이터셋으로 만든 파이프라인 결과물입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Hikaf143/LLMDataProcessing

> dataset · [Hugging Face](https://huggingface.co/datasets/Hikaf143/LLMDataProcessing)

Common Crawl 원시 데이터를 전처리해 LLM 사전학습, SFT, DPO용 데이터셋으로 만든 파이프라인 결과물입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `each pair judged chosen/rejected against a written rubric` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `pretraining corpus` · 신뢰도 medium
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:language_modeling, task:summarization = `raw Common Crawl WARC records` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:summarization = `pretraining-ready corpus` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `real scraped web content` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `pretraining corpus, plus a derived SFT (instruction-tuning) set and a DPO (preference) set` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
