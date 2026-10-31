---
type: "dataset"
id: "jhu-clsp/megawika-2"
source: "huggingface"
url: "https://huggingface.co/datasets/jhu-clsp/megawika-2"
downloads: 9743
summary: "MegaWika 2는 위키피디아 문서와 인용 웹 출처를 포함한 다국어 텍스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# jhu-clsp/megawika-2

> dataset · [Hugging Face](https://huggingface.co/datasets/jhu-clsp/megawika-2)

MegaWika 2는 위키피디아 문서와 인용 웹 출처를 포함한 다국어 텍스트 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Each sentence contains the sentence text, translated (English) sentence text, and a list of citations.` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `MegaWika 2 captures not just passage/source pairs, but the structure and relationship of the text---and the sources cited in that text---to the surrounding Wiki` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `MegaWika 2 is an improved multilingual text dataset containing a structured view of Wikipedia articles, the web sources they cite` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `The MegaWika 2 dataset consists of a list of directories, one for each language, designated by its language code.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:information_extraction, task:retrieval = `Each line of a chunk file is a distinct JSON-encoded Wikipedia article` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each sentence contains the sentence text, translated (English) sentence text, and a list of citations.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `50 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MegaWika 2 is an improved multilingual text dataset containing a structured view of Wikipedia articles` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The initial data release is based on Wikipedia dumps from May 1, 2024.` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
