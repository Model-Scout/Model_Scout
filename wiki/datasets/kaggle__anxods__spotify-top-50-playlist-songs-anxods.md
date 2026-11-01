---
type: "dataset"
id: "kaggle/anxods/spotify-top-50-playlist-songs-anxods"
source: "kaggle"
url: "https://www.kaggle.com/datasets/anxods/spotify-top-50-playlist-songs-anxods"
downloads: 7946
summary: "Spotify Top 50 플레이리스트 국가별 인기곡 데이터를 모은 음악 차트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/anxods/spotify-top-50-playlist-songs-anxods

> dataset · [Kaggle](https://www.kaggle.com/datasets/anxods/spotify-top-50-playlist-songs-anxods)

Spotify Top 50 플레이리스트 국가별 인기곡 데이터를 모은 음악 차트 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `Are you interested in knowing how's your favorite song performing in **Spotify's Top 50** Songs Chart Playlists?` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `collected into one individual CSV file per country` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `collected into one individual CSV file per country` · 신뢰도 low
- **상업 이용**: [[비상업 전용]] — metadata · license = `CC BY-NC-SA 4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `popular culture, arts and entertainment, music` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This data is retrieved by the Spotify API and then collected into one individual CSV file per country.` · 신뢰도 low
