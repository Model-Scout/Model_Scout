---
type: "dataset"
id: "ucrelnlp/wikipedia-ga-fa-ids"
source: "huggingface"
url: "https://huggingface.co/datasets/ucrelnlp/wikipedia-ga-fa-ids"
downloads: 14
summary: "9개 언어 위키피디아의 우수 및 추천 문서 ID와 제목을 담은 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[da]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fi]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[nl]]"
  - "[[pt]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ucrelnlp/wikipedia-ga-fa-ids

> dataset · [Hugging Face](https://huggingface.co/datasets/ucrelnlp/wikipedia-ga-fa-ids)

9개 언어 위키피디아의 우수 및 추천 문서 ID와 제목을 담은 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `It can be used to filter a Wikipedia dataset to contain only Good or Featured Articles for a given language.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `Contains the Wikipedia Article IDs and page titles` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Contains the Wikipedia Article IDs and page titles` · 신뢰도 low
- **언어**: [[da]] — metadata · languages = `da` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fi]] — metadata · languages = `fi` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `4` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gfdl` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Contains the Wikipedia Article IDs and page titles for Good and Featured articles on Wikipedia` · 신뢰도 medium
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `This dataset covers 9 Language Wikipedia sites.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `page_title` 열 p90 14자 ≈ 4 토큰 (viewer statistics, ko/train)
