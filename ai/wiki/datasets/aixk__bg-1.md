---
type: "dataset"
id: "aixk/bg-1"
source: "huggingface"
url: "https://huggingface.co/datasets/aixk/bg-1"
downloads: 106
summary: "AI 자율 봇넷, 내부 침투, 크리덴셜 탈취, 복합 L7 DoS 공격 패킷 트래픽 시계열 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# aixk/bg-1

> dataset · [Hugging Face](https://huggingface.co/datasets/aixk/bg-1)

AI 자율 봇넷, 내부 침투, 크리덴셜 탈취, 복합 L7 DoS 공격 패킷 트래픽 시계열 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Ground-Truth Class Mapping` · 신뢰도 low
- **작업**: [[시계열 예측]] — metadata · readme, task_categories = `time-series-forecasting` · 신뢰도 medium
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality, task:tabular_prediction = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `듀얼 시계열 데이터셋입니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Ground-Truth Class Mapping` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `실제 공격 패킷 트래픽을 종합 반영한 듀얼 시계열 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 기존의 단순 웹/스캔 공격을 넘어 AI 자율 봇넷(Botnet), 내부 침투(Infiltration), 크리덴셜 탈취(Patator), 복합 L7 DoS 등 실제 공격 패킷 트래픽을 종합 반영한 듀얼 시계열 데이터셋입니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
