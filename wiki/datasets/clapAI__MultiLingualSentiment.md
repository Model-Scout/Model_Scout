---
type: "dataset"
id: "clapAI/MultiLingualSentiment"
source: "huggingface"
url: "https://huggingface.co/datasets/clapAI/MultiLingualSentiment"
downloads: 319
summary: "MultilingualSentiment은 다국어 감정 분류 데이터셋으로 긍정, 중립, 부정 레이블을 포함합니다."
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
  - "[[영어]]"
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
  - "[[대규모 데이터]]"
---
# clapAI/MultiLingualSentiment

> dataset · [Hugging Face](https://huggingface.co/datasets/clapAI/MultiLingualSentiment)

MultilingualSentiment은 다국어 감정 분류 데이터셋으로 긍정, 중립, 부정 레이블을 포함합니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `MultilingualSentiment is a sentiment classification dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `MultilingualSentiment is a sentiment classification dataset that encompasses three sentiment labels: Positive, Neutral, Negative` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `510` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset spans multiple languages and covers a wide range of domains` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset is divided into three subsets: train, validation, and test, with a ratio of 8:1:1` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2042자 ≈ 510 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[clapAI__mmBERT-small-multilingual-sentiment|clapAI/mmBERT-small-multilingual-sentiment]]
- [[clapAI__modernBERT-base-multilingual-sentiment|clapAI/modernBERT-base-multilingual-sentiment]]
- [[clapAI__modernBERT-large-multilingual-sentiment|clapAI/modernBERT-large-multilingual-sentiment]]
- [[clapAI__roberta-base-multilingual-sentiment|clapAI/roberta-base-multilingual-sentiment]]
- [[clapAI__roberta-large-multilingual-sentiment|clapAI/roberta-large-multilingual-sentiment]]
