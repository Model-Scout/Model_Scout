---
type: "dataset"
id: "kaggle/kukuroo3/bts-youtube-channel-dataset-thumnails-img"
source: "kaggle"
url: "https://www.kaggle.com/datasets/kukuroo3/bts-youtube-channel-dataset-thumnails-img"
downloads: 604
summary: "BTS 유튜브 채널 영상 데이터와 썸네일 이미지로 다중 분류 문제를 위한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
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
# kaggle/kukuroo3/bts-youtube-channel-dataset-thumnails-img

> dataset · [Kaggle](https://www.kaggle.com/datasets/kukuroo3/bts-youtube-channel-dataset-thumnails-img)

BTS 유튜브 채널 영상 데이터와 썸네일 이미지로 다중 분류 문제를 위한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `classification` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `thumbnails : thumbnais url` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The tabular data contains 16 columns` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `category : BB : bangtan bomb , CG : choreography , RV : review , EP : episode, vlog : daily vlog , FESTA :FESTA , NA : else` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `BTS (a seven-member South Korean boy band debuted in 2013-06-13)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Using YOUTUBE API, scrap video's data.` · 신뢰도 low
