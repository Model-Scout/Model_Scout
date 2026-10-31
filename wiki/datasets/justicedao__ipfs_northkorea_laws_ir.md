---
type: "dataset"
id: "justicedao/ipfs_northkorea_laws_ir"
source: "huggingface"
url: "https://huggingface.co/datasets/justicedao/ipfs_northkorea_laws_ir"
downloads: 320
summary: "북한 법률 문서와 조항을 CID 기반 그래프 구조로 구성한 법률 정보 검색 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# justicedao/ipfs_northkorea_laws_ir

> dataset · [Hugging Face](https://huggingface.co/datasets/justicedao/ipfs_northkorea_laws_ir)

북한 법률 문서와 조항을 CID 기반 그래프 구조로 구성한 법률 정보 검색 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Retrieved documents and graph edges are retrieval evidence only.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `43` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Research retrieval release of endomorphosis/ipfs_northkorea_laws (revision 54c354ba4bef8d1987e62d94eccc180ac3a9ad59)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `body_sha256` 열 p90 64자 ≈ 43 토큰 (viewer statistics, bm25_documents/train)
