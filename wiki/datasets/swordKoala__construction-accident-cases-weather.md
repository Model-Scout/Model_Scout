---
type: "dataset"
id: "swordKoala/construction-accident-cases-weather"
source: "huggingface"
url: "https://huggingface.co/datasets/swordKoala/construction-accident-cases-weather"
downloads: 45
summary: "건설현장 사고사례와 사고 시점 기상 정보를 결합한 한국어 데이터셋으로 안전 분석에 활용 가능"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# swordKoala/construction-accident-cases-weather

> dataset · [Hugging Face](https://huggingface.co/datasets/swordKoala/construction-accident-cases-weather)

건설현장 사고사례와 사고 시점 기상 정보를 결합한 한국어 데이터셋으로 안전 분석에 활용 가능

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality, task:tabular_prediction = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `과거 건설현장 사고사례(현장·공종·작업·피해·사고유형 등) 레코드에 발생 시점의 기상 정보(기온·체감온도·풍속·습도) 를 결합한 한국어 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `사고-기상 상관관계 분석, 위험요인 모델링, 건설안전 분석용 LLM/ML 학습의 원천 데이터로 활용할 수 있습니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `137` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · tags = `weather` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `사고-기상 상관관계 분석, 위험요인 모델링, 건설안전 분석용 LLM/ML 학습의 원천 데이터로 활용할 수 있습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `사고경위` 열 p90 206자 ≈ 137 토큰 (viewer statistics, default/train)
