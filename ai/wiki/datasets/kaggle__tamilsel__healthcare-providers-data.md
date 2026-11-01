---
type: "dataset"
id: "kaggle/tamilsel/healthcare-providers-data"
source: "kaggle"
url: "https://www.kaggle.com/datasets/tamilsel/healthcare-providers-data"
downloads: 5355
summary: "의료 제공자 사기 탐지를 위한 비지도 학습 기반 이상치 탐지 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[정보 추출]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/tamilsel/healthcare-providers-data

> dataset · [Kaggle](https://www.kaggle.com/datasets/tamilsel/healthcare-providers-data)

의료 제공자 사기 탐지를 위한 비지도 학습 기반 이상치 탐지 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Healthcare Provider Fraud Detection Using Unsupervised Learning` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Try out various unsupervised techniques to find the anomalies in the data.` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `The following variables are included in the detailed Physician and Other Supplier data file` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The following variables are included in the detailed Physician and Other Supplier data file` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Try out various unsupervised techniques to find the anomalies in the data.` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Database: Open Database, Contents: Database Contents` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `healthcare` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Try out various unsupervised techniques to find the anomalies in the data.` · 신뢰도 low
