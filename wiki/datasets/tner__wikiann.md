---
type: "dataset"
id: "tner/wikiann"
source: "huggingface"
url: "https://huggingface.co/datasets/tner/wikiann"
downloads: 1382
summary: "WikiAnn은 LOC, ORG, PER 3개 개체명 인식 태그를 가진 위키피디아 기반 다국어 NER 데이터셋입니다."
readme_status: "ok"
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
# tner/wikiann

> dataset · [Hugging Face](https://huggingface.co/datasets/tner/wikiann)

WikiAnn은 LOC, ORG, PER 3개 개체명 인식 태그를 가진 위키피디아 기반 다국어 NER 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · task_categories, task_ids = `token-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction = `WikiAnn NER dataset` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Entity Types: `LOC`, `ORG`, `PER`` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `166 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `| train | validation | test |` · 신뢰도 medium
