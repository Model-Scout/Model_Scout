---
type: "dataset"
id: "whybe-choi/ko-vdr-hn"
source: "huggingface"
url: "https://huggingface.co/datasets/whybe-choi/ko-vdr-hn"
downloads: 57
summary: "한국어 문서 페이지 이미지와 텍스트 쿼리를 활용한 시각 문서 검색 임베딩 모델 학습용 하드 네거티브 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# whybe-choi/ko-vdr-hn

> dataset · [Hugging Face](https://huggingface.co/datasets/whybe-choi/ko-vdr-hn)

한국어 문서 페이지 이미지와 텍스트 쿼리를 활용한 시각 문서 검색 임베딩 모델 학습용 하드 네거티브 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `sentence-similarity` · 신뢰도 high
- **작업**: [[문서 검색]] — tag_match · readme, tags = `retrieval` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `the document is a page image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval, task:visual_qa = `the query is text` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `the document is a page image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `the query is text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Visual Document Retrieval (VDR) Hard Negatives` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Multimodal retrieval training set used to fine-tune visual-document retrieval embedding models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[whybe-choi__kovre|whybe-choi/kovre]]
