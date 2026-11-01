---
type: "dataset"
id: "kaggle/joohs0505/bugsmusicchart0623"
source: "kaggle"
url: "https://www.kaggle.com/datasets/joohs0505/bugsmusicchart0623"
downloads: 60
summary: "한국 음악 플랫폼 Bugs의 2023년 6월 Top 100 음악 차트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/joohs0505/bugsmusicchart0623

> dataset · [Kaggle](https://www.kaggle.com/datasets/joohs0505/bugsmusicchart0623)

한국 음악 플랫폼 Bugs의 2023년 6월 Top 100 음악 차트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `text classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `There are 4 columns:
Rank(int) : 1~100
Title(str) : 1~100 rank's title
Artist(str) : 1~100 rank's artists(mostly korean singers)
lyric(str) : mostly about korea` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `There are 4 columns:
Rank(int) : 1~100
Title(str) : 1~100 rank's title
Artist(str) : 1~100 rank's artists(mostly korean singers)
lyric(str) : mostly about korea` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Community Data License Agreement - Permissive - Version 1.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `Bugs one of the popular music streaming platforms in South Korea.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is dataset is about Korean music platform call Bugs, top 100 music chart` · 신뢰도 low
