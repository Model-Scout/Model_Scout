---
type: "dataset"
id: "ENERZAiKR/LGUplus_rolling_persona_aug"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/LGUplus_rolling_persona_aug"
downloads: 69
summary: "LG U+ 시청 프로그램 표를 실제 시청기록으로 보정한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ENERZAiKR/LGUplus_rolling_persona_aug

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/LGUplus_rolling_persona_aug)

LG U+ 시청 프로그램 표를 실제 시청기록으로 보정한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `[주요 시청 프로그램] 표를 실제 시청기록으로 양방향 재구성한 판.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `[주요 시청 프로그램] 표를 실제 시청기록으로 양방향 재구성한 판.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
