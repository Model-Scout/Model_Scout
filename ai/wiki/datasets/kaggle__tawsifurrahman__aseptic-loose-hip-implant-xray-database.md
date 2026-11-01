---
type: "dataset"
id: "kaggle/tawsifurrahman/aseptic-loose-hip-implant-xray-database"
source: "kaggle"
url: "https://www.kaggle.com/datasets/tawsifurrahman/aseptic-loose-hip-implant-xray-database"
downloads: 1470
summary: "고관절 인공관절의 무균성 느슨함 진단을 위한 X선 영상 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[교육]]"
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/tawsifurrahman/aseptic-loose-hip-implant-xray-database

> dataset · [Kaggle](https://www.kaggle.com/datasets/tawsifurrahman/aseptic-loose-hip-implant-xray-database)

고관절 인공관절의 무균성 느슨함 진단을 위한 X선 영상 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `classification` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `A team of researchers and doctors from Qatar University, Doha, Qatar, have collected and indexed this dataset of X-ray images for hip implants` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `These collected images were manually annotated by the team and finally validated by an orthopedic surgeon` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **도메인**: [[의료·보건]] — tag_match · tags = `health` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Authors managed to collect 200 hip implant X-ray images from published articles [1-4], online resources [5-8], and Radiopaedia [9] and are also available the co` · 신뢰도 low
