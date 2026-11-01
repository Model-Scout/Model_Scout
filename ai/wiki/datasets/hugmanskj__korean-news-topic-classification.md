---
type: "dataset"
id: "hugmanskj/korean-news-topic-classification"
source: "huggingface"
url: "https://huggingface.co/datasets/hugmanskj/korean-news-topic-classification"
downloads: 44
summary: "한국어 뉴스 토픽 분류를 위한 템플릿 기반 합성 데이터셋으로 교육용입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# hugmanskj/korean-news-topic-classification

> dataset · [Hugging Face](https://huggingface.co/datasets/hugmanskj/korean-news-topic-classification)

한국어 뉴스 토픽 분류를 위한 템플릿 기반 합성 데이터셋으로 교육용입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `뉴스 스타일의 한국어 문장` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `카테고리 레이블 (0-3)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `19` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · tags = `education` · 신뢰도 medium
- **도메인**: [[뉴스·미디어]] — tag_match · readme, tags = `news` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `validation | 500 | 검증용 데이터` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train | 5,000 | 학습용 데이터` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 29자 ≈ 19 토큰 (viewer statistics, default/validation)
