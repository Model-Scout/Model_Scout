---
type: "dataset"
id: "cluesurf/textsurf"
source: "huggingface"
url: "https://huggingface.co/datasets/cluesurf/textsurf"
downloads: 70
summary: "text.surf 아카이브의 324개 언어 21318판 19204작품의 텍스트 구절 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# cluesurf/textsurf

> dataset · [Hugging Face](https://huggingface.co/datasets/cluesurf/textsurf)

text.surf 아카이브의 324개 언어 21318판 19204작품의 텍스트 구절 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `22380444 passages, one row each` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `22380444 passages, one row each` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `283 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `21318 editions of 19204 works in 324 languages from the text.surf archive` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
