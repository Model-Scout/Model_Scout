---
type: "dataset"
id: "hyeonski/multilexnorm-synthetic-stage-a-mini-trainonly"
source: "huggingface"
url: "https://huggingface.co/datasets/hyeonski/multilexnorm-synthetic-stage-a-mini-trainonly"
downloads: 20
summary: "MultiLexNorm 2026 팀용 소규모 합성 데이터셋으로 빠른 실험과 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# hyeonski/multilexnorm-synthetic-stage-a-mini-trainonly

> dataset · [Hugging Face](https://huggingface.co/datasets/hyeonski/multilexnorm-synthetic-stage-a-mini-trainonly)

MultiLexNorm 2026 팀용 소규모 합성 데이터셋으로 빠른 실험과 학습에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `MultiLexNorm 2026 — Team Mini Subset (Synthetic Only)` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `Token-aligned: `len(raw) == len(norm)`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `Token-aligned: `len(raw) == len(norm)`` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MultiLexNorm 2026 — Team Mini Subset (Synthetic Only)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Intended to be combined with the authentic weerayut/multilexnorm2026-dev-pub train split at training time.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
