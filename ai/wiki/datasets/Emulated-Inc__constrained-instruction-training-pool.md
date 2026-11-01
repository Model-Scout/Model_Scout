---
type: "dataset"
id: "Emulated-Inc/constrained-instruction-training-pool"
source: "huggingface"
url: "https://huggingface.co/datasets/Emulated-Inc/constrained-instruction-training-pool"
downloads: 167
summary: "여러 데이터셋에서 제약 조건이 포함된 글쓰기 과제용 공개 프롬프트 모음으로, 제약 조건 검증과 응답 평가에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
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
# Emulated-Inc/constrained-instruction-training-pool

> dataset · [Hugging Face](https://huggingface.co/datasets/Emulated-Inc/constrained-instruction-training-pool)

여러 데이터셋에서 제약 조건이 포함된 글쓰기 과제용 공개 프롬프트 모음으로, 제약 조건 검증과 응답 평가에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `A row with constraints can be scored without a reference answer, by running the named checker over a generated response with the arguments beside it` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `Both are decided by reading the response alone, so either can be used as a training reward` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:reranking = `Every source rewritten into one shape, 462652 rows, one JSON object per line, with these fields.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `a row identifier unique within this file… See the full description on the dataset page` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Public prompts for writing tasks, many of them carrying a constraint a program can check, from ten datasets` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train on either layer or on both.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
