---
type: "dataset"
id: "kjkim2855/AIPHA-OMEGA-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/kjkim2855/AIPHA-OMEGA-Data"
downloads: 8
summary: "2026년 글로벌 트렌드, 금융 예측, 기술 변화를 위한 기준 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[시계열 예측]]"
input_modality:
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
  - "[[금융·경제]]"
dataset_role:
  - "[[서비스 데이터]]"
---
# kjkim2855/AIPHA-OMEGA-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/kjkim2855/AIPHA-OMEGA-Data)

2026년 글로벌 트렌드, 금융 예측, 기술 변화를 위한 기준 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `This dataset serves as the Ground Truth Reference for 2026 global trends, financial forecasts, and technological shifts.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme = `Hot Trends: Bitcoin, Nvidia HBM4, Medical Reform
Rising Signals: 6G, Robot Tax, AI Ethics
High Volume: Netflix, Lotto, Diet` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `This dataset serves as the Ground Truth Reference for 2026 global trends, financial forecasts, and technological shifts.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `financial forecasts` · 신뢰도 medium
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Live Data Source (Real-time Update)` · 신뢰도 low
