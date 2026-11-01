---
type: "dataset"
id: "kaggle/subhankarsen/novel-covid19-chestxray-repository"
source: "kaggle"
url: "https://www.kaggle.com/datasets/subhankarsen/novel-covid19-chestxray-repository"
downloads: 515
summary: "COVID-19, 폐렴, 정상 흉부 엑스레이 이미지로 구성된 공개 의료 영상 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/subhankarsen/novel-covid19-chestxray-repository

> dataset · [Kaggle](https://www.kaggle.com/datasets/subhankarsen/novel-covid19-chestxray-repository)

COVID-19, 폐렴, 정상 흉부 엑스레이 이미지로 구성된 공개 의료 영상 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `classification` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `a public chestxray dataset` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The combined dataset includes chest X-ray images of COVID-19,Pneumonia and Normal (healthy) classes` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Database: Open Database, Contents: Database Contents` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `health` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `If you are using this dataset for your research papers and find it useful for your publications, please consider citing` · 신뢰도 low
