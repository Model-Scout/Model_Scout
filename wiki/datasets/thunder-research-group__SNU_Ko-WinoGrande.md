---
type: "dataset"
id: "thunder-research-group/SNU_Ko-WinoGrande"
source: "huggingface"
url: "https://huggingface.co/datasets/thunder-research-group/SNU_Ko-WinoGrande"
downloads: 69
summary: "Ko-WinoGrande는 한국어로 번역·현지화된 대명사 해소를 통한 상식 추론 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# thunder-research-group/SNU_Ko-WinoGrande

> dataset · [Hugging Face](https://huggingface.co/datasets/thunder-research-group/SNU_Ko-WinoGrande)

Ko-WinoGrande는 한국어로 번역·현지화된 대명사 해소를 통한 상식 추론 평가 데이터셋입니다.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `Each item is a fill-in-the-blank sentence with two possible antecedents.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Models must determine which choice best fits the blank given the context.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Ko-WinoGrande is a Korean adaptation of the WinoGrande dataset` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Single evaluation set (`test` set)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
