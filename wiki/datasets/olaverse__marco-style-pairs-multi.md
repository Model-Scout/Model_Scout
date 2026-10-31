---
type: "dataset"
id: "olaverse/marco-style-pairs-multi"
source: "huggingface"
url: "https://huggingface.co/datasets/olaverse/marco-style-pairs-multi"
downloads: 52
summary: "25개 언어로 된 MS MARCO 스타일 (질문, 정답 문서) 쌍으로 임베딩 및 검색 모델 미세조정용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
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
# olaverse/marco-style-pairs-multi

> dataset · [Hugging Face](https://huggingface.co/datasets/olaverse/marco-style-pairs-multi)

25개 언어로 된 MS MARCO 스타일 (질문, 정답 문서) 쌍으로 임베딩 및 검색 모델 미세조정용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, tags, task_categories = `sentence-similarity` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:retrieval = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `25 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `462` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual, not cross-lingual — see that dataset's card for detail.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Built for fine-tuning embedders/retrievers` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `positive` 열 p90 1847자 ≈ 462 토큰 (viewer statistics, default/train)
