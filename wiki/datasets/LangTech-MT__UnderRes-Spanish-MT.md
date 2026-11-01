---
type: "dataset"
id: "LangTech-MT/UnderRes-Spanish-MT"
source: "huggingface"
url: "https://huggingface.co/datasets/LangTech-MT/UnderRes-Spanish-MT"
downloads: 56
summary: "AI-TraLow 프로젝트의 스페인어 중심 저자원 언어 병렬 말뭉치로 기계 번역 학습용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
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
  - "[[초대규모 데이터]]"
---
# LangTech-MT/UnderRes-Spanish-MT

> dataset · [Hugging Face](https://huggingface.co/datasets/LangTech-MT/UnderRes-Spanish-MT)

AI-TraLow 프로젝트의 스페인어 중심 저자원 언어 병렬 말뭉치로 기계 번역 학습용 데이터입니다.

## 분류

- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This corpus was compiled as part of the AI-TraLow project, funded by MCIN/AEI.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is intended as a training resource for machine translation systems, comprising approximately 175.3 million sentence pairs across 16 language pairs,` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high
