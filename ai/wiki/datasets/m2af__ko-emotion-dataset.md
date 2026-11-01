---
type: "dataset"
id: "m2af/ko-emotion-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/m2af/ko-emotion-dataset"
downloads: 26
summary: "한국어 감정 단문 데이터셋으로 9개 중분류 감정과 63개 소분류 감정 라벨을 포함합니다."
readme_status: "ok"
readme_language: "ko"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# m2af/ko-emotion-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/m2af/ko-emotion-dataset)

한국어 감정 단문 데이터셋으로 9개 중분류 감정과 63개 소분류 감정 라벨을 포함합니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `한국어 감정 단문 데이터셋` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `한국어 감정 단문 데이터셋` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `감정 라벨 분류 표` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `198` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 감정 단문 데이터셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `데이터 개수: 총 1039개` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `annotation` 열 p90 297자 ≈ 198 토큰 (viewer statistics, default/train)
