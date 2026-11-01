---
type: "dataset"
id: "kaggle/yasunorim/wbc-2026-scouting"
source: "kaggle"
url: "https://www.kaggle.com/datasets/yasunorim/wbc-2026-scouting"
downloads: 423
summary: "WBC 2026 참가 선수들의 MLB Statcast 피치별 데이터로 국가별 타격 및 투구 분석에 활용."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[요약]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
  - "[[뉴스·미디어]]"
---
# kaggle/yasunorim/wbc-2026-scouting

> dataset · [Kaggle](https://www.kaggle.com/datasets/yasunorim/wbc-2026-scouting)

WBC 2026 참가 선수들의 MLB Statcast 피치별 데이터로 국가별 타격 및 투구 분석에 활용.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Build country-level offensive and defensive strength indexes` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Full Statcast columns: pitch type, speed, movement, launch angle, exit velocity, expected stats, bat tracking (2024+), and more` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Analyze pitching arsenals and velocity distributions by country` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Pitch-by-pitch MLB Statcast data for players selected to the **WBC 2026 (World Baseball Classic)** rosters` · 신뢰도 low
- **작업**: [[요약]] — ner · readme = `Per-player batting summary: **109 batters** across 19 countries` · 신뢰도 medium
- **작업**: [[이미지 이해]] — ner · readme = `Batter dashboards: spray charts, zone heatmaps, count-based performance` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Files > statcast_batters.csv (37 MB)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:question_answering, task:retrieval, task:summarization, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Per-player batting summary: **109 batters** across 19 countries` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering, task:summarization, task:visual_qa = `text` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Statcast pitch-by-pitch data for WBC 2026 roster players, 20 countries` · 신뢰도 low
- **도메인**: [[뉴스·미디어]] — tag_match · tags = `news` · 신뢰도 medium
