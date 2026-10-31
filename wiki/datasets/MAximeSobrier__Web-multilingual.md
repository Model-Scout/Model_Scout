---
type: "dataset"
id: "MAximeSobrier/Web-multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/MAximeSobrier/Web-multilingual"
downloads: 211
summary: "다국어 웹페이지 1,141개로 2개 이상의 주요 언어 텍스트 포함 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# MAximeSobrier/Web-multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/MAximeSobrier/Web-multilingual)

다국어 웹페이지 1,141개로 2개 이상의 주요 언어 텍스트 포함 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This dataset contains 1,141 multilingual web pages.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `Each page contains the visible text extracted from the page.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each page contains the visible text extracted from the page.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `35 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2754` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains 1,141 multilingual web pages.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains 1,141 multilingual web pages.` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 11016자 ≈ 2754 토큰 (viewer statistics, default/train)
