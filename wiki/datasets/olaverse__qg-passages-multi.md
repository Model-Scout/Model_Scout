---
type: "dataset"
id: "olaverse/qg-passages-multi"
source: "huggingface"
url: "https://huggingface.co/datasets/olaverse/qg-passages-multi"
downloads: 50
summary: "25개 언어의 지문과 해당 지문이 직접 답하는 질문 2~3개로 구성된 다국어 질문 생성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
  - "[[중규모 데이터]]"
---
# olaverse/qg-passages-multi

> dataset · [Hugging Face](https://huggingface.co/datasets/olaverse/qg-passages-multi)

25개 언어의 지문과 해당 지문이 직접 답하는 질문 2~3개로 구성된 다국어 질문 생성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `~50,000 passages, each with 2–3 natural-language questions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `2–3 natural-language questions that the passage answers` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `25 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `462` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `passages paired with search-style questions they directly answer, across 25 languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The training set behind olaverse/mist-qg-1.5b` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `passage` 열 p90 1848자 ≈ 462 토큰 (viewer statistics, default/train)
