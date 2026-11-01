---
type: "dataset"
id: "kaggle/tyndale/survey-on-ethnic-homogeneity-among-korean-students"
source: "kaggle"
url: "https://www.kaggle.com/datasets/tyndale/survey-on-ethnic-homogeneity-among-korean-students"
downloads: 30
summary: "한국 학생들의 민족 동질성에 대한 인식을 조사한 2021년 학생 설문조사 데이터입니다."
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
  - "[[비상업 전용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/tyndale/survey-on-ethnic-homogeneity-among-korean-students

> dataset · [Kaggle](https://www.kaggle.com/datasets/tyndale/survey-on-ethnic-homogeneity-among-korean-students)

한국 학생들의 민족 동질성에 대한 인식을 조사한 2021년 학생 설문조사 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The students provided their responses to the following three questions on a Likert scale.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `**Table ID** DT_154020_22BB190100` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `**Table ID** DT_154020_22BB190100` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `CC BY-NC-SA 4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `태그: culture and humanities, korea` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `출처: Kaggle (tyndale/survey-on-ethnic-homogeneity-among-korean-students)` · 신뢰도 low
