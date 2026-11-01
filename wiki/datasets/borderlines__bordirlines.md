---
type: "dataset"
id: "borderlines/bordirlines"
source: "huggingface"
url: "https://huggingface.co/datasets/borderlines/bordirlines"
downloads: 1354
summary: "BordIRlines는 다국어 정보 검색 데이터셋으로, 쿼리와 문서 랭킹 및 관련도 점수를 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
---
# borderlines/bordirlines

> dataset · [Hugging Face](https://huggingface.co/datasets/borderlines/bordirlines)

BordIRlines는 다국어 정보 검색 데이터셋으로, 쿼리와 문서 랭킹 및 관련도 점수를 포함합니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `The BordIRLines Dataset is an information retrieval (IR) dataset constructed from various language corpora.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering, task:retrieval = `It contains queries and corresponding ranked docs along with their relevance scores.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `It contains queries and corresponding ranked docs along with their relevance scores.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `48 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The BordIRLines Dataset is an information retrieval (IR) dataset constructed from various language corpora.` · 신뢰도 low
