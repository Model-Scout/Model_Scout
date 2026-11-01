---
type: "dataset"
id: "hugmanskj/korean-ner"
source: "huggingface"
url: "https://huggingface.co/datasets/hugmanskj/korean-ner"
downloads: 46
summary: "한국어 뉴스 헤드라인 스타일 합성 데이터 기반 개체명 인식(NER) 교육용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
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
# hugmanskj/korean-ner

> dataset · [Hugging Face](https://huggingface.co/datasets/hugmanskj/korean-ner)

한국어 뉴스 헤드라인 스타일 합성 데이터 기반 개체명 인식(NER) 교육용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Token Classification: 각 토큰에 대해 개체명 태그 예측` · 신뢰도 medium
- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories, task_ids = `token-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `Token Classification: 각 토큰에 대해 개체명 태그 예측` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Token Classification: 각 토큰에 대해 개체명 태그 예측` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `17` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · tags = `education` · 신뢰도 medium
- **도메인**: [[뉴스·미디어]] — ner · readme = `도메인: 뉴스 헤드라인 스타일` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `validation | 500 | 검증용 데이터` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train | 5,000 | 학습용 데이터` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 25자 ≈ 17 토큰 (viewer statistics, default/validation)
