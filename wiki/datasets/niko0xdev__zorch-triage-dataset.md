---
type: "dataset"
id: "niko0xdev/zorch-triage-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/niko0xdev/zorch-triage-dataset"
downloads: 103
summary: "Zorch SDLC 환경에서 소프트웨어 티켓 분류를 위한 다국어 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[vi]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# niko0xdev/zorch-triage-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/niko0xdev/zorch-triage-dataset)

Zorch SDLC 환경에서 소프트웨어 티켓 분류를 위한 다국어 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `chat `messages`, short titles, deduplicated, leak-free` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A synthetic, multilingual (English, Vietnamese, Korean) dataset for triaging software tickets in the Zorch SDLC orchestration setting.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training and benchmarking small classifiers or SFT models for role / action / risk ticket triage.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
