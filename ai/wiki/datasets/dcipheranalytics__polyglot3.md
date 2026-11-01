---
type: "dataset"
id: "dcipheranalytics/polyglot3"
source: "huggingface"
url: "https://huggingface.co/datasets/dcipheranalytics/polyglot3"
downloads: 52
summary: "polyglot3의 사전학습된 단어 임베딩, 개체명 인식, 품사 태깅, 감성 사전 모델 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[서비스 데이터]]"
---
# dcipheranalytics/polyglot3

> dataset · [Hugging Face](https://huggingface.co/datasets/dcipheranalytics/polyglot3)

polyglot3의 사전학습된 단어 임베딩, 개체명 인식, 품사 태깅, 감성 사전 모델 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `word embeddings` · 신뢰도 medium
- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:information_extraction = `word embeddings, named entity recognition, part of speech tagging and sentiment lexicons` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `word embeddings, named entity recognition, part of speech tagging and sentiment lexicons` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `trained on Wikipedia (embeddings, NER, POS) and derived from it and other resources (sentiment)` · 신뢰도 medium
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `The files are meant to be downloaded by polyglot3` · 신뢰도 low
