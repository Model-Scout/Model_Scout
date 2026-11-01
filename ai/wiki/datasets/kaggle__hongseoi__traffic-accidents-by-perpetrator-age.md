---
type: "dataset"
id: "kaggle/hongseoi/traffic-accidents-by-perpetrator-age"
source: "kaggle"
url: "https://www.kaggle.com/datasets/hongseoi/traffic-accidents-by-perpetrator-age"
downloads: 106
summary: "한국에서 2012~2021년 가해자 연령별 교통사고 통계 데이터셋입니다."
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
  - "[[법률]]"
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/hongseoi/traffic-accidents-by-perpetrator-age

> dataset · [Kaggle](https://www.kaggle.com/datasets/hongseoi/traffic-accidents-by-perpetrator-age)

한국에서 2012~2021년 가해자 연령별 교통사고 통계 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `It contains the number of traffic accidents, the number of fatalities, the number of serious injuries, the number of minor injuries, and the number of reported ` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `| feature name | description |` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `| feature name | description |` · 신뢰도 low
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · tags = `law` · 신뢰도 medium
- **도메인**: [[교통·모빌리티]] — ner · readme = `Traffic accident Dataset for 20 years(2012~2021) in South Korea` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This data is statistical information on traffic accidents investigated and handled by the police` · 신뢰도 low
