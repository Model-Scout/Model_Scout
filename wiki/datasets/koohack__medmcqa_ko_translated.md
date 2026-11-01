---
type: "dataset"
id: "koohack/medmcqa_ko_translated"
source: "huggingface"
url: "https://huggingface.co/datasets/koohack/medmcqa_ko_translated"
downloads: 9
summary: "의료 분야 다지선다형 질문응답 데이터로 번역 및 생성 작업에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# koohack/medmcqa_ko_translated

> dataset · [Hugging Face](https://huggingface.co/datasets/koohack/medmcqa_ko_translated)

의료 분야 다지선다형 질문응답 데이터로 번역 및 생성 작업에 활용됨

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:question_answering, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:translation = `task_categories:
- question-answering
- translation
- text-generation
- text2text-generation` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1344` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `splits:
- name: train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `exp` 열 p90 2017자 ≈ 1344 토큰 (viewer statistics, default/train)
