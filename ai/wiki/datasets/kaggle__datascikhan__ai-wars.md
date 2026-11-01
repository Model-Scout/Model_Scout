---
type: "dataset"
id: "kaggle/datascikhan/ai-wars"
source: "kaggle"
url: "https://www.kaggle.com/datasets/datascikhan/ai-wars"
downloads: 323
summary: "2018~2026년 글로벌 AI 기업 50곳의 LLM, 벤치마크, 하드웨어, API 비용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[평가용]]"
---
# kaggle/datascikhan/ai-wars

> dataset · [Kaggle](https://www.kaggle.com/datasets/datascikhan/ai-wars)

2018~2026년 글로벌 AI 기업 50곳의 LLM, 벤치마크, 하드웨어, API 비용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `🎯 Classification : Predict model_archetype or open_source_status based on feature sets.` · 신뢰도 medium
- **작업**: [[시계열 예측]] — ner · readme = `⏱️ Time-Series : Forecast cost degradation per million tokens over 2018–2026.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `470+ Structured Columns` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `470+ Structured Columns` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `science and technology, artificial intelligence, exploratory data analysis, nlp, benchmark` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
