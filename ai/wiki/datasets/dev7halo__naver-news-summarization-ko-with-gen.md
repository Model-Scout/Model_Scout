---
type: "dataset"
id: "dev7halo/naver-news-summarization-ko-with-gen"
source: "huggingface"
url: "https://huggingface.co/datasets/dev7halo/naver-news-summarization-ko-with-gen"
downloads: 29
summary: "네이버 뉴스 기사와 요약문, 생성 요약문을 포함한 한국어 뉴스 요약 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# dev7halo/naver-news-summarization-ko-with-gen

> dataset · [Hugging Face](https://huggingface.co/datasets/dev7halo/naver-news-summarization-ko-with-gen)

네이버 뉴스 기사와 요약문, 생성 요약문을 포함한 한국어 뉴스 요약 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `gen_text` · 신뢰도 low
- **작업**: [[요약]] — ner · readme = `summary` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:summarization = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:summarization = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2382` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `document` 열 p90 3574자 ≈ 2382 토큰 (viewer statistics, default/train)
