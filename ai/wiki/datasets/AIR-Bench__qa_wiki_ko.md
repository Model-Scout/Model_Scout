---
type: "dataset"
id: "AIR-Bench/qa_wiki_ko"
source: "huggingface"
url: "https://huggingface.co/datasets/AIR-Bench/qa_wiki_ko"
downloads: 25
readme_status: "thin"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# AIR-Bench/qa_wiki_ko

> dataset · [Hugging Face](https://huggingface.co/datasets/AIR-Bench/qa_wiki_ko)

## 분류

- **작업**: [[문서 검색]] — metadata · task_categories, task_ids = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1362` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2043자 ≈ 1362 토큰 (viewer statistics, AIR-Bench_24.05/corpus_default)
