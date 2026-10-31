---
type: "dataset"
id: "daekeun-ml/naver-news-summarization-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/daekeun-ml/naver-news-summarization-ko"
downloads: 649
summary: "네이버 뉴스에서 수집한 27,400개의 한국어 뉴스 기사와 요약문 쌍 데이터셋으로, 뉴스 요약 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# daekeun-ml/naver-news-summarization-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/daekeun-ml/naver-news-summarization-ko)

네이버 뉴스에서 수집한 27,400개의 한국어 뉴스 기사와 요약문 쌍 데이터셋으로, 뉴스 요약 연구에 활용됨.

## 분류

- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:summarization = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:summarization = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1485` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — tag_match · readme, tags = `news` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `It was originally built for a Korean NLP hands-on lab and has been publicly hosted on the Hugging Face Hub since January 2023.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `document` 열 p90 2228자 ≈ 1485 토큰 (viewer statistics, default/validation)
