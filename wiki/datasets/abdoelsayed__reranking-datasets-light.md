---
type: "dataset"
id: "abdoelsayed/reranking-datasets-light"
source: "huggingface"
url: "https://huggingface.co/datasets/abdoelsayed/reranking-datasets-light"
downloads: 1160
summary: "다양한 검색 및 리랭킹 데이터셋을 제공하는 연구용 데이터 모음집입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[리랭킹]]"
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# abdoelsayed/reranking-datasets-light

> dataset · [Hugging Face](https://huggingface.co/datasets/abdoelsayed/reranking-datasets-light)

다양한 검색 및 리랭킹 데이터셋을 제공하는 연구용 데이터 모음집입니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `ReRanking Datasets : A comprehensive collection of retrieval and reranking datasets with full passage contexts` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `A curated collection of ready-to-use datasets for retrieval and reranking research.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:reranking, task:retrieval = `including titles, text, and metadata for in-depth research.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `including titles, text, and metadata for in-depth research.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `110 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `25` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A curated collection of ready-to-use datasets for retrieval and reranking research.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A curated collection of ready-to-use datasets for retrieval and reranking research.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 101자 ≈ 25 토큰 (viewer statistics, 2WikimultihopQA/train)
