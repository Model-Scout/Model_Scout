---
type: "dataset"
id: "kaggle/muutyy/seoulmmod"
source: "kaggle"
url: "https://www.kaggle.com/datasets/muutyy/seoulmmod"
downloads: 101
summary: "서울시의 2023~2025년 도시 내 6개 교통수단의 시간별 다중모달 이동 데이터 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/muutyy/seoulmmod

> dataset · [Kaggle](https://www.kaggle.com/datasets/muutyy/seoulmmod)

서울시의 2023~2025년 도시 내 6개 교통수단의 시간별 다중모달 이동 데이터 벤치마크입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Large-scale public benchmark for citywide multimodal mobility in Seoul.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Hourly multimodal origin-destination flows within Seoul from 2023 to 2025.` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Hourly multimodal origin-destination flows within Seoul from 2023 to 2025.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `Large-scale public benchmark for citywide multimodal mobility in Seoul.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `SeoulMMOD contains hourly multimodal origin-destination flows within Seoul from 2023 to 2025.` · 신뢰도 low
