---
type: "dataset"
id: "SamsungSDS-Research/SDS-KoPub-VDR-Benchmark"
source: "huggingface"
url: "https://huggingface.co/datasets/SamsungSDS-Research/SDS-KoPub-VDR-Benchmark"
downloads: 429
summary: "한국 공공 문서의 시각 문서 검색을 위한 멀티모달 QA 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[일반]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# SamsungSDS-Research/SDS-KoPub-VDR-Benchmark

> dataset · [Hugging Face](https://huggingface.co/datasets/SamsungSDS-Research/SDS-KoPub-VDR-Benchmark)

한국 공공 문서의 시각 문서 검색을 위한 멀티모달 QA 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Pairs textual queries with page-level visual evidence and answers` · 신뢰도 low
- **작업**: [[질의응답]] — tag_match · readme, tags = `question-answering` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `visual-document-retrieval` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `page images, OCR text, and metadata` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `real-world government document images` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:question_answering, task:retrieval = `textual queries` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `natural-language queries, corresponding answer pages, and ground-truth answers` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `376` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `Domains | 6 (Society, Environment, Education, Industry, Diplomacy, Finance)` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `real-world government document images` · 신뢰도 low
- **도메인**: [[행정·민원]] — ner · readme = `Korean public documents` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `benchmark dataset` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The SDS-KoPub-VDR QA dataset was constructed through a multi-stage pipeline` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 565자 ≈ 376 토큰 (viewer statistics, SDS-KoPub-QA/test)
