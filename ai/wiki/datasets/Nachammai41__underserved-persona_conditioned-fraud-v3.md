---
type: "dataset"
id: "Nachammai41/underserved-persona_conditioned-fraud-v3"
source: "huggingface"
url: "https://huggingface.co/datasets/Nachammai41/underserved-persona_conditioned-fraud-v3"
downloads: 32
summary: "실제 근거 기반 페르소나를 활용한 사기 탐지용 거래 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Nachammai41/underserved-persona_conditioned-fraud-v3

> dataset · [Hugging Face](https://huggingface.co/datasets/Nachammai41/underserved-persona_conditioned-fraud-v3)

실제 근거 기반 페르소나를 활용한 사기 탐지용 거래 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Persona-Conditioned Fraud Detection Dataset (v3, Citation-Grounded)` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme, task:tabular_prediction = `Schema (per transaction row)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Schema (per transaction row)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `FinCEN advisories, FDIC microdata, Urban Institute reports, Menjívar et al. TPS survey, Del Real Venezuelan migration interviews, Remitly 10-K, Wise / Inter-Ame` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Persona-Conditioned Fraud Detection Dataset (v3, Citation-Grounded)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
