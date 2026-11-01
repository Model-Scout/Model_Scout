---
type: "dataset"
id: "kaggle/sharad5/korean-band-bts-members-face-recognition"
source: "kaggle"
url: "https://www.kaggle.com/datasets/sharad5/korean-band-bts-members-face-recognition"
downloads: 348
summary: "BTS 멤버 7명의 얼굴 인식용 이미지 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
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
# kaggle/sharad5/korean-band-bts-members-face-recognition

> dataset · [Kaggle](https://www.kaggle.com/datasets/sharad5/korean-band-bts-members-face-recognition)

BTS 멤버 7명의 얼굴 인식용 이미지 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Facial recognition` · 신뢰도 low
- **작업**: [[이미지 인식]] — tag_match · tags = `image classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `Images of the seven band members of BTS` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Facial recognition` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `Korean Band BTS Members` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `put together by scraping Google Images` · 신뢰도 low
