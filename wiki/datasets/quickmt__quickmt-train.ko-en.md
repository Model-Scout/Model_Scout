---
type: "dataset"
id: "quickmt/quickmt-train.ko-en"
source: "huggingface"
url: "https://huggingface.co/datasets/quickmt/quickmt-train.ko-en"
downloads: 40
summary: "quickmt ko-en 학습 코퍼스로 다양한 OPUS 데이터셋을 중복 제거 후 필터링하여 번역 모델 학습에 사용."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
  - "[[대규모 데이터]]"
---
# quickmt/quickmt-train.ko-en

> dataset · [Hugging Face](https://huggingface.co/datasets/quickmt/quickmt-train.ko-en)

quickmt ko-en 학습 코퍼스로 다양한 OPUS 데이터셋을 중복 제거 후 필터링하여 번역 모델 학습에 사용.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `quickmt ko-en Training Corpus` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `quickmt ko-en Training Corpus` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `130` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `quickmt ko-en Training Corpus` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `quickmt ko-en Training Corpus` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `en` 열 p90 195자 ≈ 130 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[quickmt__quickmt-en-ko|quickmt/quickmt-en-ko]]
