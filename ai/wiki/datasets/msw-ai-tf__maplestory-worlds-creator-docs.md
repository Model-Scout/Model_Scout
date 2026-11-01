---
type: "dataset"
id: "msw-ai-tf/maplestory-worlds-creator-docs"
source: "huggingface"
url: "https://huggingface.co/datasets/msw-ai-tf/maplestory-worlds-creator-docs"
downloads: 46
summary: "MapleStory Worlds Creator Center 공식 문서의 한영 병렬 데이터셋으로 검색, 임베딩, 언어모델 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# msw-ai-tf/maplestory-worlds-creator-docs

> dataset · [Hugging Face](https://huggingface.co/datasets/msw-ai-tf/maplestory-worlds-creator-docs)

MapleStory Worlds Creator Center 공식 문서의 한영 병렬 데이터셋으로 검색, 임베딩, 언어모델 학습에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `intended for RAG, search, embeddings, and domain language-model training` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `intended for RAG, search, embeddings, and domain language-model training` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:language_modeling, task:retrieval = `Body in Markdown. Code blocks are normalized to mlua` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Body in Markdown. Code blocks are normalized to mlua` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4329` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A curated dataset built from the official documentation of the MapleStory Worlds Creator Center.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Each config has a single `train` split and contains all three document types.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 6493자 ≈ 4329 토큰 (viewer statistics, ko/train)
