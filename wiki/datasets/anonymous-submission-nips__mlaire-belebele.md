---
type: "dataset"
id: "anonymous-submission-nips/mlaire-belebele"
source: "huggingface"
url: "https://huggingface.co/datasets/anonymous-submission-nips/mlaire-belebele"
downloads: 74
summary: "MLAIRE-BELEBELE은 122개 언어로 된 488개 문서로 구성된 언어 인지 검색 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# anonymous-submission-nips/mlaire-belebele

> dataset · [Hugging Face](https://huggingface.co/datasets/anonymous-submission-nips/mlaire-belebele)

MLAIRE-BELEBELE은 122개 언어로 된 488개 문서로 구성된 언어 인지 검색 평가용 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `488 underlying passages, each available in 122 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Relevance is encoded by group_id matching.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `115 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `188` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `488 underlying passages, each available in 122 languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This repository is part of the MLAIRE benchmark, submitted anonymously to the NeurIPS 2026 Evaluations & Datasets Track.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 753자 ≈ 188 토큰 (viewer statistics, corpus/test)
