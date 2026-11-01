---
type: "dataset"
id: "kaggle/goweiting/ted-talks-transcript"
source: "kaggle"
url: "https://www.kaggle.com/datasets/goweiting/ted-talks-transcript"
downloads: 795
summary: "TED 강연의 다국어 자막과 메타데이터를 포함한 검색 및 정보 추출용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/goweiting/ted-talks-transcript

> dataset · [Kaggle](https://www.kaggle.com/datasets/goweiting/ted-talks-transcript)

TED 강연의 다국어 자막과 메타데이터를 포함한 검색 및 정보 추출용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `used different languages for the search and retrieve task, to test for reliability of our search engine` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `used TED talks to evaluate different configuration of search engine algorithms` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `transcript of the TED Talk in `lang`` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `transcript of the TED Talk in `lang`` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `TED Talks Transcript > An extension to Kaggle's TED dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset was developed as part of a larger dataset used for an information retrieval assignment` · 신뢰도 low
