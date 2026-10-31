---
type: "dataset"
id: "bltlab/ParaNames"
source: "huggingface"
url: "https://huggingface.co/datasets/bltlab/ParaNames"
downloads: 259
summary: "ParaNames 데이터셋은 데이터셋 카드의 기본 템플릿으로 제공됩니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
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
  - "[[초대규모 데이터]]"
---
# bltlab/ParaNames

> dataset · [Hugging Face](https://huggingface.co/datasets/bltlab/ParaNames)

ParaNames 데이터셋은 데이터셋 카드의 기본 템플릿으로 제공됩니다.

## 분류

- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:information_extraction = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `377 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `6` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · tags = `wikipedia` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `eng` 열 p90 25자 ≈ 6 토큰 (viewer statistics, default/train)
