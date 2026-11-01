---
type: "dataset"
id: "CaveduckAI/simplified_soda_kr"
source: "huggingface"
url: "https://huggingface.co/datasets/CaveduckAI/simplified_soda_kr"
downloads: 30
summary: "SODA 데이터셋의 한국어 번역본으로, 화자와 대화 문맥을 포함한 40722개 샘플로 구성됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# CaveduckAI/simplified_soda_kr

> dataset · [Hugging Face](https://huggingface.co/datasets/CaveduckAI/simplified_soda_kr)

SODA 데이터셋의 한국어 번역본으로, 화자와 대화 문맥을 포함한 40722개 샘플로 구성됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[번역]] — tag_match · readme, tags = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `Each sample contains speakers, narrative context, and dialogue translated to Korean.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `Each sample contains speakers, narrative context, and dialogue translated to Korean.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
