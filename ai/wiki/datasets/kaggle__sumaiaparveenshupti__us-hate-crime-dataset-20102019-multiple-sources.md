---
type: "dataset"
id: "kaggle/sumaiaparveenshupti/us-hate-crime-dataset-20102019-multiple-sources"
source: "kaggle"
url: "https://www.kaggle.com/datasets/sumaiaparveenshupti/us-hate-crime-dataset-20102019-multiple-sources"
downloads: 1791
summary: "2010-2019년 미국 증오범죄 데이터를 다양한 편견 유형별로 분류한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/sumaiaparveenshupti/us-hate-crime-dataset-20102019-multiple-sources

> dataset · [Kaggle](https://www.kaggle.com/datasets/sumaiaparveenshupti/us-hate-crime-dataset-20102019-multiple-sources)

2010-2019년 미국 증오범죄 데이터를 다양한 편견 유형별로 분류한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Crime Type: Category of crime defined by the FBI, including Crimes Against Persons (crimes targeting individuals or groups of individuals), and Property Crimes.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `New_York_Hate_Crimes_by_County_and_Bias_Type_2010-2019.csv` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Count of incidents with a reported Anti-Male bias.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `County: Location where the crime was reported.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `US Hate Crime Dataset 2010-2019 (Multiple Sources)` · 신뢰도 low
