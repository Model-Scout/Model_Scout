---
type: "dataset"
id: "nebchi/koen-text"
source: "huggingface"
url: "https://huggingface.co/datasets/nebchi/koen-text"
downloads: 86
summary: "한국어와 영어 텍스트로 구성된 데이터셋으로, 다양한 자연어처리 작업에 활용 가능함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
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
# nebchi/koen-text

> dataset · [Hugging Face](https://huggingface.co/datasets/nebchi/koen-text)

한국어와 영어 텍스트로 구성된 데이터셋으로, 다양한 자연어처리 작업에 활용 가능함.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `Created with reference to the following datasets.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `Created with reference to the following datasets.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `Created with reference to the following datasets.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `20327` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Created with reference to the following datasets.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Created with reference to the following datasets.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 30491자 ≈ 20327 토큰 (viewer statistics, default/train)
