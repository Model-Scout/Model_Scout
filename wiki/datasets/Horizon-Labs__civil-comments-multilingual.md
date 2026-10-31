---
type: "dataset"
id: "Horizon-Labs/civil-comments-multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/Horizon-Labs/civil-comments-multilingual"
downloads: 171
summary: "33개 언어로 기계 번역된 Civil Comments 데이터로, 혐오 표현 탐지 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
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
  - "[[중규모 데이터]]"
---
# Horizon-Labs/civil-comments-multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/Horizon-Labs/civil-comments-multilingual)

33개 언어로 기계 번역된 Civil Comments 데이터로, 혐오 표현 탐지 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `390,862 translations of comments from Civil Comments` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `the original fractional annotator scores for the 7 Detoxify labels` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `32 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `187` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Civil Comments, machine-translated into 33 languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `We made it to train Horizon-Labs/multilingual-toxicity-small and -base.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `source_text` 열 p90 746자 ≈ 187 토큰 (viewer statistics, default/train)
