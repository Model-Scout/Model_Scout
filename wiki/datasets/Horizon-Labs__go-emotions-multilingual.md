---
type: "dataset"
id: "Horizon-Labs/go-emotions-multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/Horizon-Labs/go-emotions-multilingual"
downloads: 121
summary: "GoEmotions 데이터셋을 35개 언어로 기계 번역한 감정 분류 학습용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
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
# Horizon-Labs/go-emotions-multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/Horizon-Labs/go-emotions-multilingual)

GoEmotions 데이터셋을 35개 언어로 기계 번역한 감정 분류 학습용 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `the translated comment` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `GoEmotions labels of the source comment (list of label names, from the "simplified" config)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `35 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `33` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `English Reddit comments with 28 emotion labels from human annotators` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `We made it to train Horizon-Labs/multilingual-emotions-small and -base.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `source_text` 열 p90 131자 ≈ 33 토큰 (viewer statistics, default/train)
