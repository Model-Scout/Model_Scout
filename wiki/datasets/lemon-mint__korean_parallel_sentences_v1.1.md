---
type: "dataset"
id: "lemon-mint/korean_parallel_sentences_v1.1"
source: "huggingface"
url: "https://huggingface.co/datasets/lemon-mint/korean_parallel_sentences_v1.1"
downloads: 57
summary: "한국어와 영어 병렬 문장 데이터셋으로 기계 번역 및 다국어 모델 개발에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
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
# lemon-mint/korean_parallel_sentences_v1.1

> dataset · [Hugging Face](https://huggingface.co/datasets/lemon-mint/korean_parallel_sentences_v1.1)

한국어와 영어 병렬 문장 데이터셋으로 기계 번역 및 다국어 모델 개발에 활용됨.

## 분류

- **작업**: [[임베딩]] — tag_match · readme, tags = `embedding` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — ner · readme = `Developing language models that can understand and generate both Korean and English text` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:translation = `parallel sentences in Korean and English` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `parallel sentences in Korean and English` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `241` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Korean Parallel Sentences Ver 1.1 dataset is a collection of parallel sentences in Korean and English.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training machine translation models for Korean-English translation.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 361자 ≈ 241 토큰 (viewer statistics, default/train)
