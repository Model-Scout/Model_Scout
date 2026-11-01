---
type: "dataset"
id: "jukofyork/slop-fiction-paragraphs"
source: "huggingface"
url: "https://huggingface.co/datasets/jukofyork/slop-fiction-paragraphs"
downloads: 26
summary: "내러티브 소설의 중간 단락을 모은 데이터셋으로 텍스트 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# jukofyork/slop-fiction-paragraphs

> dataset · [Hugging Face](https://huggingface.co/datasets/jukofyork/slop-fiction-paragraphs)

내러티브 소설의 중간 단락을 모은 데이터셋으로 텍스트 분석에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Only non-first and non-final paragraphs (ie: each story's "inner" paragraphs only) between 75 and 2000 characters were then retained in the "text" field.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation = `Only non-first and non-final paragraphs (ie: each story's "inner" paragraphs only) between 75 and 2000 characters were then retained in the "text" field.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Only non-first and non-final paragraphs (ie: each story's "inner" paragraphs only) between 75 and 2000 characters were then retained in the "text" field.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset was created by combining: ajibawa-2023/General-Stories-Collection ajibawa-2023/Children-Stories-Collection` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset was created by combining: ajibawa-2023/General-Stories-Collection ajibawa-2023/Children-Stories-Collection` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[jukofyork__command-a-03-2025-writer-v1|jukofyork/command-a-03-2025-writer-v1]]
