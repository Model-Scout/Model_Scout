---
type: "dataset"
id: "WUCAPITALLIMITED/pit-fundamentals-sample"
source: "huggingface"
url: "https://huggingface.co/datasets/WUCAPITALLIMITED/pit-fundamentals-sample"
downloads: 123
summary: "뉴질랜드 등록 자선단체 포함 84개 기업의 공식 재무제표 데이터를 시장별로 제공하는 공개 샘플 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[da]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[nl]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# WUCAPITALLIMITED/pit-fundamentals-sample

> dataset · [Hugging Face](https://huggingface.co/datasets/WUCAPITALLIMITED/pit-fundamentals-sample)

뉴질랜드 등록 자선단체 포함 84개 기업의 공식 재무제표 데이터를 시장별로 제공하는 공개 샘플 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `Company accounts by filing date: public sample` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme = ``trial_all_markets.csv`: 1,447 rows, 19 columns, UTF-8 with a header row` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Every row carries its filing date, the register it came from, a link to the register's own page and the source notice that must travel with it.` · 신뢰도 low
- **언어**: [[da]] — metadata · languages = `da` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This is the public sample of Trading Agent Data` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
