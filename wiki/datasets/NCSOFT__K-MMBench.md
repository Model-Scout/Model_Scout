---
type: "dataset"
id: "NCSOFT/K-MMBench"
source: "huggingface"
url: "https://huggingface.co/datasets/NCSOFT/K-MMBench"
downloads: 617
summary: "K-MMBench는 한국어로 번역된 MMBench로, 한국어 시각-언어 모델 평가용 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# NCSOFT/K-MMBench

> dataset · [Hugging Face](https://huggingface.co/datasets/NCSOFT/K-MMBench)

K-MMBench는 한국어로 번역된 MMBench로, 한국어 시각-언어 모델 평가용 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `K-MMBench consists of questions across 20 evaluation dimensions, such as identity reasoning, image emotion, and attribute recognition` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `designed for evaluating vision-language models` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `designed for evaluating vision-language models` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `evaluating vision-language models` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:reranking, task:retrieval = `By translating the dev subset of MMBench into Korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `K-MMBench consists of questions across 20 evaluation dimensions` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `30` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `we developed a novel robust evaluation benchmark specifically for Korean language` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `A` 열 p90 46자 ≈ 30 토큰 (viewer statistics, default/dev)
