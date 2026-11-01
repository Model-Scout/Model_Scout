---
type: "dataset"
id: "whybe-choi/ko-triplet-hn"
source: "huggingface"
url: "https://huggingface.co/datasets/whybe-choi/ko-triplet-hn"
downloads: 58
summary: "한국어 텍스트 임베딩 모델 미세조정을 위한 하드 네거티브가 포함된 삼중항 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# whybe-choi/ko-triplet-hn

> dataset · [Hugging Face](https://huggingface.co/datasets/whybe-choi/ko-triplet-hn)

한국어 텍스트 임베딩 모델 미세조정을 위한 하드 네거티브가 포함된 삼중항 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `sentence-similarity` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · tags, task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `anchor (string): Query` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `620` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean text embedding models` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `intended for fine-tuning Korean text embedding models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `negative_4` 열 p90 930자 ≈ 620 토큰 (viewer statistics, percpos/train)
