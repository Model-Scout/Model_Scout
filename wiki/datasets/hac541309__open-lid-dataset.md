---
type: "dataset"
id: "hac541309/open-lid-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/hac541309/open-lid-dataset"
downloads: 1458
summary: "201개 언어의 언어 식별 모델 학습용 오픈 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[aa]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[hi]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# hac541309/open-lid-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/hac541309/open-lid-dataset)

201개 언어의 언어 식별 모델 학습용 오픈 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Original authors built the dataset for LID models for 201 languages.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `"text" column contains the sentence.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Original authors built the dataset for LID models for 201 languages.` · 신뢰도 low
- **언어**: [[aa]] — metadata · languages = `aa` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2244` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `gpl-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `An Open Dataset and Model for Language Identification` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Original authors built the dataset for LID models for 201 languages.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 8975자 ≈ 2244 토큰 (viewer statistics, default/train)
