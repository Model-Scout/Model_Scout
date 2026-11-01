---
type: "dataset"
id: "jongrock17/KoPolNLI-pre-v0.9"
source: "huggingface"
url: "https://huggingface.co/datasets/jongrock17/KoPolNLI-pre-v0.9"
downloads: 86
summary: "KoPolNLI-pre-v0.9은 한국어 정치·사회 이슈 전제-가설 데이터셋으로 NLI 연구용입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jongrock17/KoPolNLI-pre-v0.9

> dataset · [Hugging Face](https://huggingface.co/datasets/jongrock17/KoPolNLI-pre-v0.9)

KoPolNLI-pre-v0.9은 한국어 정치·사회 이슈 전제-가설 데이터셋으로 NLI 연구용입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each public row has `premise_ko`, `hypothesis_ko`, `entailment`, and `task`.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each public row has `premise_ko`, `hypothesis_ko`, `entailment`, and `task`.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `validation | 8,904 | 4,452 | 4,452 | Provisional model selection; not gold` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train | 71,216 | 35,608 | 35,608 | Provisional training` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
