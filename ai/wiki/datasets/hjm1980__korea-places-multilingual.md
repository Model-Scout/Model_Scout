---
type: "dataset"
id: "hjm1980/korea-places-multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/hjm1980/korea-places-multilingual"
downloads: 46
summary: "한국 내 16,126개 장소의 한글명과 영어 로마자명, 일본어·중국어명, 좌표, 주소, 지하철 정보 등을 포함한 다국어 지명 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[위치·좌표 (입력 형식)|위치·좌표]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[th]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[지리·위치]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# hjm1980/korea-places-multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/hjm1980/korea-places-multilingual)

한국 내 16,126개 장소의 한글명과 영어 로마자명, 일본어·중국어명, 좌표, 주소, 지하철 정보 등을 포함한 다국어 지명 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `Search an English name, get the Hangul back, and hand it straight to KakaoMap, Naver Map or a taxi driver.` · 신뢰도 low
- **입력 형식**: [[위치·좌표 (입력 형식)|위치·좌표]] — metadata · modality = `geospatial` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `16,126 places in South Korea with their Korean (Hangul) name next to the romanized English name, plus Japanese and Chinese names where the source has them, coor` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Search an English name, get the Hangul back, and hand it straight to KakaoMap, Naver Map or a taxi driver.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `16` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[지리·위치]] — ner · readme = `16,126 places in South Korea with their Korean (Hangul) name next to the romanized English name, plus Japanese and Chinese names where the source has them, coor` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `address_en` 열 p90 65자 ≈ 16 토큰 (viewer statistics, default/train)
