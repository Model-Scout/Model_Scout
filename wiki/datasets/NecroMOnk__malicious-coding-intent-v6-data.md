---
type: "dataset"
id: "NecroMOnk/malicious-coding-intent-v6-data"
source: "huggingface"
url: "https://huggingface.co/datasets/NecroMOnk/malicious-coding-intent-v6-data"
downloads: 177
summary: "악성 코드 의도 분류를 위한 코드 스니펫 데이터셋입니다."
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
# NecroMOnk/malicious-coding-intent-v6-data

> dataset · [Hugging Face](https://huggingface.co/datasets/NecroMOnk/malicious-coding-intent-v6-data)

악성 코드 의도 분류를 위한 코드 스니펫 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = ``text` - prompt/code snippet.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = ``malicious` - `1` malicious intent/code, `0` benign.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Malicious Coding Intent Classifier Data` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `data/train.parquet
222,950
train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
