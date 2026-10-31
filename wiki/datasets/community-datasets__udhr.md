---
type: "dataset"
id: "community-datasets/udhr"
source: "huggingface"
url: "https://huggingface.co/datasets/community-datasets/udhr"
downloads: 160
summary: "세계 인권 선언문(UDHR)의 464개 이상 언어 번역문 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# community-datasets/udhr

> dataset · [Hugging Face](https://huggingface.co/datasets/community-datasets/udhr)

세계 인권 선언문(UDHR)의 464개 이상 언어 번역문 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:translation = `This plain text version prepared by the “UDHR in Unicode” project` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `The dataset includes translations of the document in 464+ languages and dialects.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `414 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[법률]] — ner · readme = `The Universal Declaration of Human Rights (UDHR) is a milestone document in the history of human rights.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This plain text version prepared by the “UDHR in Unicode” project` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
