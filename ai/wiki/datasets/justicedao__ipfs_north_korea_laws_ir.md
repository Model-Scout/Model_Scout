---
type: "dataset"
id: "justicedao/ipfs_north_korea_laws_ir"
source: "huggingface"
url: "https://huggingface.co/datasets/justicedao/ipfs_north_korea_laws_ir"
downloads: 244
summary: "북한 법률 문서와 조항을 포함한 법률 정보 검색용 데이터셋입니다."
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
# justicedao/ipfs_north_korea_laws_ir

> dataset · [Hugging Face](https://huggingface.co/datasets/justicedao/ipfs_north_korea_laws_ir)

북한 법률 문서와 조항을 포함한 법률 정보 검색용 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `Canonical fields `entry_cid`, `law_cid`, `record_type`, `jurisdiction`, `language`, `instrument_id`, `instrument_title`, `article_number`, `article_title`, `tit` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Retrieved documents and graph edges are retrieval evidence only.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `43` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Research retrieval release of `endomorphosis/ipfs_north_korea_laws` (revision `59ceccb763e1c02be7e3b8c01e6e6ae7aa37ef76`)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `body_sha256` 열 p90 64자 ≈ 43 토큰 (viewer statistics, bm25_documents/train)
