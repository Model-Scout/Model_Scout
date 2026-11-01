---
type: "dataset"
id: "rmyeid/polyglot_ner"
source: "huggingface"
url: "https://huggingface.co/datasets/rmyeid/polyglot_ner"
downloads: 345
summary: "위키피디아와 Freebase에서 자동 생성된 40개 언어의 개체명 인식 학습 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
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
dataset_role:
  - "[[학습용]]"
---
# rmyeid/polyglot_ner

> dataset · [Hugging Face](https://huggingface.co/datasets/rmyeid/polyglot_ner)

위키피디아와 Freebase에서 자동 생성된 40개 언어의 개체명 인식 학습 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, task_categories, task_ids = `token-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction = `The dataset contains the basic Wikipedia based training data for 40 languages` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `the task of named entity recognition` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `40 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `A training dataset automatically generated from Wikipedia and Freebase` · 신뢰도 medium
