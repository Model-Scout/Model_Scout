---
type: "dataset"
id: "yhavinga/ccmatrix"
source: "huggingface"
url: "https://huggingface.co/datasets/yhavinga/ccmatrix"
downloads: 4587
summary: "CCMatrix는 웹에서 80개 언어의 고품질 병렬 문장 108억 개를 추출한 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
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
dataset_role:
  - "[[학습용]]"
---
# yhavinga/ccmatrix

> dataset · [Hugging Face](https://huggingface.co/datasets/yhavinga/ccmatrix)

CCMatrix는 웹에서 80개 언어의 고품질 병렬 문장 108억 개를 추출한 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `margin-based bitext mining in LASER's multilingual sentence space can be applied to monolingual corpora of billions of sentences to produce high quality aligned` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval, task:translation = `monolingual corpora of billions of sentences` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `high quality aligned translation data` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `91 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `We were able to mine 10.8 billion parallel sentences` · 신뢰도 low

## 같은 데이터의 사본·중복 등록

- `xezpeleta/ccmatrix`
