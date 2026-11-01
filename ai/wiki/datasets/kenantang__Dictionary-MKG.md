---
type: "dataset"
id: "kenantang/Dictionary-MKG"
source: "huggingface"
url: "https://huggingface.co/datasets/kenantang/Dictionary-MKG"
downloads: 28
summary: "Dictionary-MKG는 LLM으로 생성된 다국어 사전 데이터셋으로 언어 학습에 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[es]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# kenantang/Dictionary-MKG

> dataset · [Hugging Face](https://huggingface.co/datasets/kenantang/Dictionary-MKG)

Dictionary-MKG는 LLM으로 생성된 다국어 사전 데이터셋으로 언어 학습에 활용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Words are labeled with a `day_index`` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Dictionary-MKG: An LLM-Generated Multilingual Dictionary for Language Learners` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding, task:generation, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:translation = `text` · 신뢰도 medium
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `Education` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset construction followed a two-step LLM pipeline` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
