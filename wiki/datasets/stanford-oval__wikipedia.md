---
type: "dataset"
id: "stanford-oval/wikipedia"
source: "huggingface"
url: "https://huggingface.co/datasets/stanford-oval/wikipedia"
downloads: 1206
summary: "25개 언어의 위키피디아 HTML 덤프를 전처리 및 청크화한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# stanford-oval/wikipedia

> dataset · [Hugging Face](https://huggingface.co/datasets/stanford-oval/wikipedia)

25개 언어의 위키피디아 HTML 덤프를 전처리 및 청크화한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Open-Domain Question Answering from Heterogeneous Data Sources with Retrieval and Semantic Parsing` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:retrieval = `Wikipedia HTML dumps` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Open-Domain Question Answering from Heterogeneous Data Sources with Retrieval and Semantic Parsing` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `25 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `790` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Wikipedia HTML dumps from 25 languages` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains preprocessed and chunked Wikipedia HTML dumps from 25 languages.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 3162자 ≈ 790 토큰 (viewer statistics, 20241101/train)
