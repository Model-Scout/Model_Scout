---
type: "dataset"
id: "JooYoon/riidolaya-statehint-pilot100-development"
source: "huggingface"
url: "https://huggingface.co/datasets/JooYoon/riidolaya-statehint-pilot100-development"
downloads: 614
summary: "AI 어시스턴트가 작성한 100개의 가상 개발 메시지 데이터셋으로 분류 모델 개발에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# JooYoon/riidolaya-statehint-pilot100-development

> dataset · [Hugging Face](https://huggingface.co/datasets/JooYoon/riidolaya-statehint-pilot100-development)

AI 어시스턴트가 작성한 100개의 가상 개발 메시지 데이터셋으로 분류 모델 개발에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Primary intent labels are author judgments.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `This dataset contains original fictional development messages authored and labeled by an AI assistant before predictions.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Primary intent labels are author judgments.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It is not real-user data, independent human ground truth or a production qualification benchmark.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains original fictional development messages authored and labeled by an AI assistant before predictions.` · 신뢰도 low
