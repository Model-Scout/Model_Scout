---
type: "dataset"
id: "kaggle/alephantonio/korea-game-ratings-grac"
source: "kaggle"
url: "https://www.kaggle.com/datasets/alephantonio/korea-game-ratings-grac"
downloads: 4
summary: "한국 게임물관리위원회(GRAC)의 2007~2026년 게임 등급 데이터셋으로 연령, 플랫폼, 장르 정보를 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
  - "[[행정·민원]]"
---
# kaggle/alephantonio/korea-game-ratings-grac

> dataset · [Kaggle](https://www.kaggle.com/datasets/alephantonio/korea-game-ratings-grac)

한국 게임물관리위원회(GRAC)의 2007~2026년 게임 등급 데이터셋으로 연령, 플랫폼, 장르 정보를 포함합니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `33,000+ official Korean game ratings with English labels: age, platform, genre` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Every official game rating decision published by Korea's Game Rating and Administration Committee (GRAC, 게임물관리위원회) Open API since 2007` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `in one clean CSV` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `in one clean CSV` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · tags = `law` · 신뢰도 medium
- **도메인**: [[행정·민원]] — tag_match · readme, tags = `government` · 신뢰도 medium
