---
type: "dataset"
id: "Bingsu/laion2B-multi-korean-subset"
source: "huggingface"
url: "https://huggingface.co/datasets/Bingsu/laion2B-multi-korean-subset"
downloads: 111
summary: "laion/laion2B-multi의 한국어 데이터만 포함한 이미지-텍스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Bingsu/laion2B-multi-korean-subset

> dataset · [Hugging Face](https://huggingface.co/datasets/Bingsu/laion2B-multi-korean-subset)

laion/laion2B-multi의 한국어 데이터만 포함한 이미지-텍스트 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `[img2dataset](https://github.com/rom1504/img2dataset)을 사용하여 URL로된 이미지들을 데이터셋 형태로 만들 수 있습니다.` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `'TEXT': `string`` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `[img2dataset](https://github.com/rom1504/img2dataset)을 사용하여 URL로된 이미지들을 데이터셋 형태로 만들 수 있습니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `'TEXT': `string`` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `124` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a subset data of laion/laion2B-multi, including only korean` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `| # of data | 11376263 |` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `TEXT` 열 p90 186자 ≈ 124 토큰 (viewer statistics, default/train)
