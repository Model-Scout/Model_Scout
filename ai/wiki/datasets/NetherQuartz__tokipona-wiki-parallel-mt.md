---
type: "dataset"
id: "NetherQuartz/tokipona-wiki-parallel-mt"
source: "huggingface"
url: "https://huggingface.co/datasets/NetherQuartz/tokipona-wiki-parallel-mt"
downloads: 44
summary: "Toki Pona 중심 20개 언어 병렬 문장 데이터셋으로 기계 번역 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
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
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# NetherQuartz/tokipona-wiki-parallel-mt

> dataset · [Hugging Face](https://huggingface.co/datasets/NetherQuartz/tokipona-wiki-parallel-mt)

Toki Pona 중심 20개 언어 병렬 문장 데이터셋으로 기계 번역 연구에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `validated with LaBSE-tokipona` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Sentence-level bitext mining from Toki Pona Wikipedia using margin-based scoring + mutual nearest neighbors` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval, task:translation = `Each row contains parallel text in 20 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Each row contains parallel text in 20 languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `20 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `109` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `mined from Wikipedia` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `validation 583` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train 11,429` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `fr` 열 p90 436자 ≈ 109 토큰 (viewer statistics, default/validation)
