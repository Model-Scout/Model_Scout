---
type: "dataset"
id: "hugmanskj/korean-date-translation"
source: "huggingface"
url: "https://huggingface.co/datasets/hugmanskj/korean-date-translation"
downloads: 8
summary: "한국어 날짜 표현을 ISO 8601 형식으로 변환하는 교육용 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# hugmanskj/korean-date-translation

> dataset · [Hugging Face](https://huggingface.co/datasets/hugmanskj/korean-date-translation)

한국어 날짜 표현을 ISO 8601 형식으로 변환하는 교육용 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · readme, tags = `text2text-generation` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `한국어 날짜 표현 (다양한 형식)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `ISO 8601 형식의 날짜 (YYYY-MM-DD)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `11` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · tags = `education` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `도메인: 날짜 표현 정규화` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `validation | 500 | 검증용 데이터` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train | 5,000 | 학습용 데이터` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `input` 열 p90 16자 ≈ 11 토큰 (viewer statistics, default/validation)
