---
type: "dataset"
id: "CAMUS-LAB/seoul-travel-demand-2024"
source: "huggingface"
url: "https://huggingface.co/datasets/CAMUS-LAB/seoul-travel-demand-2024"
downloads: 68
summary: "서울특별시 통행수요 모델링을 위한 공간·인구·도로·토지이용 통합 원시 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교통·모빌리티]]"
---
# CAMUS-LAB/seoul-travel-demand-2024

> dataset · [Hugging Face](https://huggingface.co/datasets/CAMUS-LAB/seoul-travel-demand-2024)

서울특별시 통행수요 모델링을 위한 공간·인구·도로·토지이용 통합 원시 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `서울특별시 통행수요 모델링 을 위한 공간·인구·도로·토지이용 통합 raw 데이터셋.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `SGIS 집계구 (2025) | 19,097 폴리곤` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `서울특별시 통행수요 모델링 을 위한 공간·인구·도로·토지이용 통합 raw 데이터셋.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — tag_match · readme, tags = `transportation` · 신뢰도 medium
