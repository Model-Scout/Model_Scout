---
type: "dataset"
id: "yjoonjang/ko-en-vdr-private"
source: "huggingface"
url: "https://huggingface.co/datasets/yjoonjang/ko-en-vdr-private"
downloads: 15
summary: "한국어-영어 혼합 시각 문서 검색을 위한 멀티모달 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
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
  - "[[영어]]"
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
  - "[[중규모 데이터]]"
---
# yjoonjang/ko-en-vdr-private

> dataset · [Hugging Face](https://huggingface.co/datasets/yjoonjang/ko-en-vdr-private)

한국어-영어 혼합 시각 문서 검색을 위한 멀티모달 학습 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `sentence-similarity` · 신뢰도 low
- **작업**: [[문서 검색]] — tag_match · readme, tags = `retrieval` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `the document is a page image (PDF screenshot / slide / report / chart / invoice / etc.)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval, task:visual_qa = `the query is text` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `the document is a page image (PDF screenshot / slide / report / chart / invoice / etc.)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `the query is text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `mixed Korean and English visual-document retrieval` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Multimodal retrieval training set used to fine-tune Qwen/Qwen3-VL-Embedding-2B` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
