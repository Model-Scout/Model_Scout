---
type: "dataset"
id: "DaehanKim/korean-jev-benchmark"
source: "huggingface"
url: "https://huggingface.co/datasets/DaehanKim/korean-jev-benchmark"
downloads: 1071
summary: "9개 공개 데이터셋에서 추출한 25,418개 한국어 평가 문항으로 선택지 기반 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# DaehanKim/korean-jev-benchmark

> dataset · [Hugging Face](https://huggingface.co/datasets/DaehanKim/korean-jev-benchmark)

9개 공개 데이터셋에서 추출한 25,418개 한국어 평가 문항으로 선택지 기반 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · tags, task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — metadata · modality = `document` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `25,418 Korean text-only evaluation items` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `normalized to finite-choice decisions such as A, B, or C.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `529` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `25,418 Korean text-only evaluation items from 9 public datasets and 22 subsets` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `25,418 Korean text-only evaluation items from 9 public datasets and 22 subsets` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `provenance_json` 열 p90 794자 ≈ 529 토큰 (viewer statistics, default/test)
