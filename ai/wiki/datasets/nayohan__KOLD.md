---
type: "dataset"
id: "nayohan/KOLD"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/KOLD"
downloads: 109
summary: "KOLD는 한국어 공격적 언어 데이터셋으로, 공격적 언어 탐지 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
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
  - "[[중규모 데이터]]"
---
# nayohan/KOLD

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/KOLD)

KOLD는 한국어 공격적 언어 데이터셋으로, 공격적 언어 탐지 연구에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `KOLD: Korean Offensive Language Dataset` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `KOLD: Korean Offensive Language Dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `KOLD: Korean Offensive Language Dataset` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `67` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KOLD: Korean Offensive Language Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `KOLD: Korean Offensive Language Dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `comment` 열 p90 100자 ≈ 67 토큰 (viewer statistics, default/train)
