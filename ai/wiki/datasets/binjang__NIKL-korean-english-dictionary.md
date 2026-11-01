---
type: "dataset"
id: "binjang/NIKL-korean-english-dictionary"
source: "huggingface"
url: "https://huggingface.co/datasets/binjang/NIKL-korean-english-dictionary"
downloads: 160
summary: "한국어 단어와 품사, 정의, 예문, 난이도, 의미 범주를 포함한 한국어-영어 사전 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
  - "[[문서 검색]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# binjang/NIKL-korean-english-dictionary

> dataset · [Hugging Face](https://huggingface.co/datasets/binjang/NIKL-korean-english-dictionary)

한국어 단어와 품사, 정의, 예문, 난이도, 의미 범주를 포함한 한국어-영어 사전 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `해당 단어의 예문 (문장 또는 대화 형식)` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction, task:retrieval, task:translation = `Registered word entry
단어` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Definition of the word in Korean
해당 단어의 한글 정의` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `286` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `단어의 난이도 ('초급', '중급', '고급')` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Column Name
Type
Description
설명` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `Usages` 열 p90 429자 ≈ 286 토큰 (viewer statistics, default/train)
