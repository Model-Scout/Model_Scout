---
type: "dataset"
id: "google-research-datasets/paws-x"
source: "huggingface"
url: "https://huggingface.co/datasets/google-research-datasets/paws-x"
downloads: 9435
summary: "PAWS-X는 6개 언어로 된 문장 유사도 판별용 교차언어 역대결 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# google-research-datasets/paws-x

> dataset · [Hugging Face](https://huggingface.co/datasets/google-research-datasets/paws-x)

PAWS-X는 6개 언어로 된 문장 유사도 판별용 교차언어 역대결 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — metadata · task_ids = `semantic-similarity-scoring` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `label | Label for each pair` · 신뢰도 low
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `24` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains 23,659 human translated PAWS evaluation pairs and 296,406 machine translated training pairs in six typologically distinct languages: Frenc` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `296,406 machine translated training pairs in six typologically distinct languages` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `sentence1` 열 p90 95자 ≈ 24 토큰 (viewer statistics, ko/validation)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
