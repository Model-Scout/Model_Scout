---
type: "dataset"
id: "Volt-AI/tremorwatch-supply-chain-risk-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/Volt-AI/tremorwatch-supply-chain-risk-v1"
downloads: 28
summary: "글로벌 공급망 위험 이벤트와 전략적 병목지점 노출 정보를 AI가 요약한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[시계열 예측]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[상거래·상품]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Volt-AI/tremorwatch-supply-chain-risk-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/Volt-AI/tremorwatch-supply-chain-risk-v1)

글로벌 공급망 위험 이벤트와 전략적 병목지점 노출 정보를 AI가 요약한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[시계열 예측]] — metadata · task_categories = `time-series-forecasting` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `AI-summarized global supply chain risk events with chokepoint exposure mapping.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `Risk events with AI-generated summaries, ticker / commodity / chokepoint mapping` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Risk events with AI-generated summaries, ticker / commodity / chokepoint mapping` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `575` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `global supply chain risk events` · 신뢰도 low
- **도메인**: [[뉴스·미디어]] — tag_match · tags = `news` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The Parquet bundle below is a point-in-time snapshot.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `ai_summary` 열 p90 2298자 ≈ 575 토큰 (viewer statistics, chokepoints/train)
