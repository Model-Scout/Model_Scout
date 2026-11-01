---
type: "dataset"
id: "moche-ai/hax-measured-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/moche-ai/hax-measured-dataset"
downloads: 41
summary: "Hax에서 직접 측정한 로컬 AI 및 AI 서버 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[시계열 예측]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# moche-ai/hax-measured-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/moche-ai/hax-measured-dataset)

Hax에서 직접 측정한 로컬 AI 및 AI 서버 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `benchmark/operations records` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `local-AI and ai-server benchmark/operations records` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Every row is measured and carries its `source`, `date`, and `method`` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:language_modeling = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Every row is measured and carries its `source`, `date`, and `method`` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:language_modeling = `text` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `part of the moche-ai ecosystem — a Korean-first, edge-first open model lab` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Every row is measured and carries its `source`, `date`, and `method` - no fabricated numbers` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
