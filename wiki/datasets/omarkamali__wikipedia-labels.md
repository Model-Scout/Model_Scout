---
type: "dataset"
id: "omarkamali/wikipedia-labels"
source: "huggingface"
url: "https://huggingface.co/datasets/omarkamali/wikipedia-labels"
downloads: 116
summary: "358개 위키백과 언어의 구조적 라벨(네임스페이스 및 별칭) 데이터셋으로, 위키백과 콘텐츠 정리에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# omarkamali/wikipedia-labels

> dataset · [Hugging Face](https://huggingface.co/datasets/omarkamali/wikipedia-labels)

358개 위키백과 언어의 구조적 라벨(네임스페이스 및 별칭) 데이터셋으로, 위키백과 콘텐츠 정리에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `It is designed to help researchers and developers clean Wikipedia content by identifying and removing structural noise (e.g., "Category:", "File:", "Template:")` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction, task:retrieval = `structural labels (namespaces and their aliases) for 358 Wikipedia languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `structural labels (namespaces and their aliases) for 358 Wikipedia languages` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `352 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `9` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `atj` 열 p90 38자 ≈ 9 토큰 (viewer statistics, default/train)
