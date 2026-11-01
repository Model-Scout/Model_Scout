---
type: "dataset"
id: "upskyy/ko-wiki-reranking"
source: "huggingface"
url: "https://huggingface.co/datasets/upskyy/ko-wiki-reranking"
downloads: 48
summary: "maywell/ko_wikidata_QA 데이터셋을 샘플링해 만든 5만개 한국어 리랭킹 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# upskyy/ko-wiki-reranking

> dataset · [Hugging Face](https://huggingface.co/datasets/upskyy/ko-wiki-reranking)

maywell/ko_wikidata_QA 데이터셋을 샘플링해 만든 5만개 한국어 리랭킹 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `50,000개의 reranking 학습 데이터셋` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:reranking = `maywell/ko_wikidata_QA 데이터셋을 랜덤 샘플링하여 50,000개의 reranking 학습 데이터셋` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `50,000개의 reranking 학습 데이터셋` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `30` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `50,000개의 reranking 학습 데이터셋` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 45자 ≈ 30 토큰 (viewer statistics, data/train)
