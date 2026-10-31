---
type: "dataset"
id: "kaggle/sinakaraji/covid-vaccination-vs-death"
source: "kaggle"
url: "https://www.kaggle.com/datasets/sinakaraji/covid-vaccination-vs-death"
downloads: 10661
summary: "코로나19 백신 접종률과 사망자 수를 비교 분석하는 글로벌 보건 데이터셋입니다."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/sinakaraji/covid-vaccination-vs-death

> dataset · [Kaggle](https://www.kaggle.com/datasets/sinakaraji/covid-vaccination-vs-death)

코로나19 백신 접종률과 사망자 수를 비교 분석하는 글로벌 보건 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `investigate the impact of coronavirus vaccinations on coronavirus mortality` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `| country | iso_code | date | total_vaccinations | people_vaccinated | people_fully_vaccinated | New_deaths | population | ratio |` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `| country | iso_code | date | total_vaccinations | people_vaccinated | people_fully_vaccinated | New_deaths | population | ratio |` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `health` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This data set was generated to investigate the impact of coronavirus vaccinations on coronavirus mortality.` · 신뢰도 low
