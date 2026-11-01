---
type: "dataset"
id: "heretic-org/Multilingual-Harmless-Harmful"
source: "huggingface"
url: "https://huggingface.co/datasets/heretic-org/Multilingual-Harmless-Harmful"
downloads: 1105
summary: "9개 언어로 번역된 무해/유해 프롬프트 쌍 데이터셋으로 다국어 연구에 활용 가능"
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
  - "[[bn]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[hi]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[mr]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[ta]]"
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
  - "[[소규모 데이터]]"
---
# heretic-org/Multilingual-Harmless-Harmful

> dataset · [Hugging Face](https://huggingface.co/datasets/heretic-org/Multilingual-Harmless-Harmful)

9개 언어로 번역된 무해/유해 프롬프트 쌍 데이터셋으로 다국어 연구에 활용 가능

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `416 harmful / harmless prompt pairs` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `One line = One prompt in each of the `.txt` files. Columns: `text` (the translation), `english` (the original)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `One line = One prompt in each of the `.txt` files. Columns: `text` (the translation), `english` (the original)` · 신뢰도 medium
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[mr]] — metadata · languages = `mr` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[ta]] — metadata · languages = `ta` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `24` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains the Translations of the (1) heretic-org/Semantic-Harmless dataset and the (2) heretic-org/Semantic-Harmful dataset into 9 languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains the Translations of the (1) heretic-org/Semantic-Harmless dataset and the (2) heretic-org/Semantic-Harmful dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 97자 ≈ 24 토큰 (viewer statistics, korean/harmful)
