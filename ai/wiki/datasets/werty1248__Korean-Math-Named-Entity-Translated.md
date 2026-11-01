---
type: "dataset"
id: "werty1248/Korean-Math-Named-Entity-Translated"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/Korean-Math-Named-Entity-Translated"
downloads: 34
summary: "수학 관련 영어 웹 데이터를 기반으로 수학자, 지명, 수학 공식 등의 올바른 한국어 명칭을 생성하는 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# werty1248/Korean-Math-Named-Entity-Translated

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/Korean-Math-Named-Entity-Translated)

수학 관련 영어 웹 데이터를 기반으로 수학자, 지명, 수학 공식 등의 올바른 한국어 명칭을 생성하는 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `수학자, 지명, 수학자 이름/지명이 포함된 수학 공식이나 이론명 등의 (비교적)올바른 한국어 명칭을 생성` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `수학 관련 영어 웹 데이터를 기반으로` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `(비교적)올바른 한국어 명칭을 생성` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `19` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `수학 관련 영어 웹 데이터를 기반으로` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 29자 ≈ 19 토큰 (viewer statistics, default/train)
