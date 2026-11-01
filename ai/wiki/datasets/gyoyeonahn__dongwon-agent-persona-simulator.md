---
type: "dataset"
id: "gyoyeonahn/dongwon-agent-persona-simulator"
source: "huggingface"
url: "https://huggingface.co/datasets/gyoyeonahn/dongwon-agent-persona-simulator"
downloads: 54
summary: "LLM 기반 가상 소비자 시뮬레이션으로 신제품 출시 전 수요 예측 시스템입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[시계열 예측]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# gyoyeonahn/dongwon-agent-persona-simulator

> dataset · [Hugging Face](https://huggingface.co/datasets/gyoyeonahn/dongwon-agent-persona-simulator)

LLM 기반 가상 소비자 시뮬레이션으로 신제품 출시 전 수요 예측 시스템입니다.

## 분류

- **작업**: [[시계열 예측]] — metadata · task_categories = `time-series-forecasting` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality, task:tabular_prediction = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `LLM 기반 가상 소비자(Persona) 시뮬레이션` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Persona distribution
- Flavor preference prediction
- 시나리오별 수요 변화 그래프(옵션)` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `제품 기획 / 마케팅 / 타겟 세그먼트 전략 수립을 위해 설계되었습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Dongwon X KAIST AI Competition에서 개발되었으며` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
