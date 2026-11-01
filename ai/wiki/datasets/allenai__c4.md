---
type: "dataset"
id: "allenai/c4"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/c4"
downloads: 727689
summary: "Common Crawl 웹 크롤링 데이터를 정제한 대규모 영어 및 다국어 말뭉치로, 언어 모델 사전학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# allenai/c4

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/c4)

Common Crawl 웹 크롤링 데이터를 정제한 대규모 영어 및 다국어 말뭉치로, 언어 모델 사전학습에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `The data have several fields: - `url`: url of the source as a string - `text`: text content as a string - `timestamp`: timestamp as a string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `The data have several fields: - `url`: url of the source as a string - `text`: text content as a string - `timestamp`: timestamp as a string` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `103 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3776` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A colossal, cleaned version of Common Crawl's web crawl corpus.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `C4 and mC4 are mainly intended to pretrain language models and word representations.` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `99999999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 15104자 ≈ 3776 토큰 (viewer statistics, ko/validation)

## 이 데이터로 학습한 모델

- [[pathcosmos__frankenstallm|pathcosmos/frankenstallm]]
