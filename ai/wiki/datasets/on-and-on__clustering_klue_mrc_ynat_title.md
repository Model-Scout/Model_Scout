---
type: "dataset"
id: "on-and-on/clustering_klue_mrc_ynat_title"
source: "huggingface"
url: "https://huggingface.co/datasets/on-and-on/clustering_klue_mrc_ynat_title"
downloads: 7
summary: "KLUE 데이터셋을 가공한 뉴스 제목 클러스터링 임베딩 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# on-and-on/clustering_klue_mrc_ynat_title

> dataset · [Hugging Face](https://huggingface.co/datasets/on-and-on/clustering_klue_mrc_ynat_title)

KLUE 데이터셋을 가공한 뉴스 제목 클러스터링 임베딩 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `processed using the categories from the KLUE-mrc & KLUE-ynat dataset` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `It is a dataset for embedding evaluation` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `Task: Clustering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:retrieval = `processed using the categories from the KLUE-mrc & KLUE-ynat dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `processed using the categories from the KLUE-mrc & KLUE-ynat dataset` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `32` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `News_category: IT/Science, Sports, Media/Culture, Ecomomy/Finance, Real Estate` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a processed and redistributed version of the KLUE dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 48자 ≈ 32 토큰 (viewer statistics, kor-Hang/test)
