---
type: "dataset"
id: "kaggle/bradklassen/official-world-golf-ranking-data"
source: "kaggle"
url: "https://www.kaggle.com/datasets/bradklassen/official-world-golf-ranking-data"
downloads: 1166
summary: "남자 프로 골퍼들의 공식 세계 골프 랭킹 데이터를 주간 단위로 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/bradklassen/official-world-golf-ranking-data

> dataset · [Kaggle](https://www.kaggle.com/datasets/bradklassen/official-world-golf-ranking-data)

남자 프로 골퍼들의 공식 세계 골프 랭킹 데이터를 주간 단위로 제공하는 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Can this dataset be used to predict who will win upcoming PGA Tour tournaments?` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Stored in a long data format.` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Players are then ranked; a higher average yields a higher rank.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `CC BY-NC-SA 4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Official World Golf Ranking is a system for rating the performance level of male professional golfers.` · 신뢰도 low
- **도메인**: [[뉴스·미디어]] — tag_match · tags = `news` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Please contribute analysis and findings as a kernel.` · 신뢰도 low
