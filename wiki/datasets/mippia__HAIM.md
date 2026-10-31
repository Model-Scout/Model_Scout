---
type: "dataset"
id: "mippia/HAIM"
source: "huggingface"
url: "https://huggingface.co/datasets/mippia/HAIM"
downloads: 775
summary: "음악 제작 과정에서 AI 개입 단계를 세분화하여 추적하는 인간-AI 음악 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# mippia/HAIM

> dataset · [Hugging Face](https://huggingface.co/datasets/mippia/HAIM)

음악 제작 과정에서 AI 개입 단계를 세분화하여 추적하는 인간-AI 음악 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `Beyond binary "AI-or-human" — granular, role-level tracking of AI intervention across the music production workflow.` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification = `67,000 with audio ≈ 229 GB + 86,686 link-based` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Human-AI Music Datasets for AI Music Production Tracking Benchmark` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
