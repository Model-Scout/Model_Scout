---
type: "dataset"
id: "junyoungson/KomuRetrieval"
source: "huggingface"
url: "https://huggingface.co/datasets/junyoungson/KomuRetrieval"
downloads: 37
summary: "한국어 커뮤니티 스타일 질의 검색 평가용 BEIR 형식 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# junyoungson/KomuRetrieval

> dataset · [Hugging Face](https://huggingface.co/datasets/junyoungson/KomuRetrieval)

한국어 커뮤니티 스타일 질의 검색 평가용 BEIR 형식 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `나무위키 문서를 기반으로 하여 다양한 스타일의 질의와 관련 문서 쌍을 포함하고 있습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `나무위키 문서를 기반으로 하여 다양한 스타일의 질의와 관련 문서 쌍을 포함하고 있습니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `8` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `나무위키 문서를 기반으로 하여 다양한 스타일의 질의와 관련 문서 쌍을 포함하고 있습니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `한국어 정보 검색 모델의 성능을 평가하기 위해 구축된 BEIR 형식의 벤치마크 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `query-id` 열 p90 12자 ≈ 8 토큰 (viewer statistics, default/test)
