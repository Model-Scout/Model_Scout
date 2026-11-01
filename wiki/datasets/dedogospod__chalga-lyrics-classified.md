---
type: "dataset"
id: "dedogospod/chalga-lyrics-classified"
source: "huggingface"
url: "https://huggingface.co/datasets/dedogospod/chalga-lyrics-classified"
downloads: 34
summary: "발칸 찰가/팝 노래 가사 7,132개를 언어별로 분류한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# dedogospod/chalga-lyrics-classified

> dataset · [Hugging Face](https://huggingface.co/datasets/dedogospod/chalga-lyrics-classified)

발칸 찰가/팝 노래 가사 7,132개를 언어별로 분류한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `Each entry contains the original URL, title, artist name, full lyrics text` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:language_modeling = `full lyrics text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:language_modeling = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `786` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `a multilingual lyrics website covering Balkan and Eastern European music` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train / Val / Test split | 80% / 10% / 10%` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `lyrics` 열 p90 3144자 ≈ 786 토큰 (viewer statistics, default/validation)
