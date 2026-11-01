---
type: "dataset"
id: "negaraku-md/negaraku-md"
source: "huggingface"
url: "https://huggingface.co/datasets/negaraku-md/negaraku-md"
downloads: 1436
summary: "말레이시아에 관한 13개 언어의 병렬 지식 기반 데이터셋으로, 검색과 질의응답 등에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[요약]]"
  - "[[번역]]"
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
  - "[[문화·관광]]"
  - "[[금융·경제]]"
  - "[[법률]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# negaraku-md/negaraku-md

> dataset · [Hugging Face](https://huggingface.co/datasets/negaraku-md/negaraku-md)

말레이시아에 관한 13개 언어의 병렬 지식 기반 데이터셋으로, 검색과 질의응답 등에 활용 가능

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · tags, task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · tags, task_categories = `text-retrieval` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:retrieval, task:summarization, task:translation = `15,028 rows — 1,156 articles in each of 13 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:summarization, task:translation = ``answer` and `key_takeaways` are written to be liftable` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1717` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — tag_match · tags = `culture` · 신뢰도 medium
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **도메인**: [[법률]] — tag_match · tags = `law` · 신뢰도 medium
- **도메인**: [[행정·민원]] — tag_match · readme, tags = `government` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `one `train` split` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 6870자 ≈ 1717 토큰 (viewer statistics, ko/train)
