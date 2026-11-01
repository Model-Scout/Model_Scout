---
type: "dataset"
id: "ysenarath/moosa2022multilingual-cross-lingual-archived"
source: "huggingface"
url: "https://huggingface.co/datasets/ysenarath/moosa2022multilingual-cross-lingual-archived"
downloads: 25
summary: "다국어 혐오 발언 데이터셋으로, 여러 언어 간 번역을 포함한 교차 언어 자원입니다."
readme_status: "template"
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
# ysenarath/moosa2022multilingual-cross-lingual-archived

> dataset · [Hugging Face](https://huggingface.co/datasets/ysenarath/moosa2022multilingual-cross-lingual-archived)

다국어 혐오 발언 데이터셋으로, 여러 언어 간 번역을 포함한 교차 언어 자원입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Multilingual Hate Speech Dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Multilingual Hate Speech Dataset` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `103` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual Hate Speech Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset card provides information about the Multilingual Hate Speech Dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 412자 ≈ 103 토큰 (viewer statistics, default/test)
