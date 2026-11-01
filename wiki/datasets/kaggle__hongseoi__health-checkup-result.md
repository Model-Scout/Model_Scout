---
type: "dataset"
id: "kaggle/hongseoi/health-checkup-result"
source: "kaggle"
url: "https://www.kaggle.com/datasets/hongseoi/health-checkup-result"
downloads: 837
summary: "한국 국민건강보험공단의 2002~2020년 건강검진 결과 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/hongseoi/health-checkup-result

> dataset · [Kaggle](https://www.kaggle.com/datasets/hongseoi/health-checkup-result)

한국 국민건강보험공단의 2002~2020년 건강검진 결과 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `This dataset is the result of a random sampling of 1 million people per year from 2002 to 2021 among those who underwent basic health checkups provided by the N` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `This dataset consists of a total of 19 csv files for each year, and each csv file contains only the health checkup results for that year.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `This dataset consists of a total of 19 csv files for each year, and each csv file contains only the health checkup results for that year.` · 신뢰도 low
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `healthcare` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is the result of a random sampling of 1 million people per year from 2002 to 2021 among those who underwent basic health checkups provided by the N` · 신뢰도 low
