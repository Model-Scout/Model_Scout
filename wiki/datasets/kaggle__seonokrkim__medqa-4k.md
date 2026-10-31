---
type: "dataset"
id: "kaggle/seonokrkim/medqa-4k"
source: "kaggle"
url: "https://www.kaggle.com/datasets/seonokrkim/medqa-4k"
downloads: 74
summary: "영어, 중국어, 한국어로 된 다국어 의료 다지선다형 질문답변 데이터셋으로 언어모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/seonokrkim/medqa-4k

> dataset · [Kaggle](https://www.kaggle.com/datasets/seonokrkim/medqa-4k)

영어, 중국어, 한국어로 된 다국어 의료 다지선다형 질문답변 데이터셋으로 언어모델 학습용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `multiple-choice medical questions` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `multiple-choice medical questions` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:question_answering = `multiple-choice medical questions` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `corresponding correct answers for each question` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `health` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Training and fine-tuning multilingual language models` · 신뢰도 medium
