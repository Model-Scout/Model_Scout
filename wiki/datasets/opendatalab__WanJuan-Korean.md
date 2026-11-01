---
type: "dataset"
id: "opendatalab/WanJuan-Korean"
source: "huggingface"
url: "https://huggingface.co/datasets/opendatalab/WanJuan-Korean"
downloads: 206
summary: "WanJuan-Korean 코퍼스는 역사, 정치, 문화 등 7개 분야 34개 하위분류의 280GB 한국어 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
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
  - "[[환경·기상]]"
  - "[[금융·경제]]"
  - "[[일반]]"
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
---
# opendatalab/WanJuan-Korean

> dataset · [Hugging Face](https://huggingface.co/datasets/opendatalab/WanJuan-Korean)

WanJuan-Korean 코퍼스는 역사, 정치, 문화 등 7개 분야 34개 하위분류의 280GB 한국어 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `the corpus can adapt to diverse research requirements across various fields` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `The rich thematic classification not only facilitates researchers in retrieving data according to specific needs` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:retrieval = `WanJuan-Korean(万卷丝路-韩语) corpus, with a volume exceeding 280GB, comprises 7 major categories and 34 subcategories` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The rich thematic classification not only facilitates researchers in retrieving data according to specific needs but also ensures that the corpus can adapt to d` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · tags = `climate` · 신뢰도 medium
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `It covers a wide range of local-specific content, including history, politics, culture, real estate, shopping, weather, dining, encyclopedias, and professional ` · 신뢰도 low
- **도메인**: [[법률]] — tag_match · tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `WanJuan-Korean(万卷丝路-韩语) corpus, with a volume exceeding 280GB, comprises 7 major categories and 34 subcategories` · 신뢰도 low
