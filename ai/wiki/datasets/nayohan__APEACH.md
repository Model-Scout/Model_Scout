---
type: "dataset"
id: "nayohan/APEACH"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/APEACH"
downloads: 19
summary: "혐오 표현 평가를 위한 군중 생성 데이터셋 분석과 공격 연구 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nayohan/APEACH

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/APEACH)

혐오 표현 평가를 위한 군중 생성 데이터셋 분석과 공격 연구 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Attacking Pejorative Expressions with Analysis on Crowd-Generated Hate Speech Evaluation Datasets` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `hate speech evaluation datasets` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `hate speech evaluation datasets` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `49` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `crowd-generated hate speech evaluation datasets` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `crowd-generated hate speech evaluation datasets` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 73자 ≈ 49 토큰 (viewer statistics, default/train)
