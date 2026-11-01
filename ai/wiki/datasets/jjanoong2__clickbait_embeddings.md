---
type: "dataset"
id: "jjanoong2/clickbait_embeddings"
source: "huggingface"
url: "https://huggingface.co/datasets/jjanoong2/clickbait_embeddings"
downloads: 42
summary: "한국어 뉴스 제목 낚시성 분류를 위한 SBERT 임베딩 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jjanoong2/clickbait_embeddings

> dataset · [Hugging Face](https://huggingface.co/datasets/jjanoong2/clickbait_embeddings)

한국어 뉴스 제목 낚시성 분류를 위한 SBERT 임베딩 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — tag_match · readme, tags = `embeddings` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding = `한국어 뉴스 기사의 제목과 본문을 SBERT 모델로 임베딩한 결과물` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — tag_match · readme, tags = `news` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `Validation | 116,588 | 58,294 | 50% | 50%` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train | 466,344 | 233,172 | 50% | 50%` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
