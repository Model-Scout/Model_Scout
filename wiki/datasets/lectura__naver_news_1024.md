---
type: "dataset"
id: "lectura/naver_news_1024"
source: "huggingface"
url: "https://huggingface.co/datasets/lectura/naver_news_1024"
downloads: 11
summary: "daekeun-ml/naver-news-summarization-ko 데이터셋을 전처리하고 토크나이징하여 사전학습용으로 만든 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lectura/naver_news_1024

> dataset · [Hugging Face](https://huggingface.co/datasets/lectura/naver_news_1024)

daekeun-ml/naver-news-summarization-ko 데이터셋을 전처리하고 토크나이징하여 사전학습용으로 만든 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Preprocessed and tokenized daekeun-ml/naver-news-summarization-ko dataset for pretraining.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Concatenated all text and split into chunk size of 1024.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Preprocessed and tokenized daekeun-ml/naver-news-summarization-ko dataset for pretraining.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `naver-news-summarization-ko dataset` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Preprocessed and tokenized daekeun-ml/naver-news-summarization-ko dataset for pretraining.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
