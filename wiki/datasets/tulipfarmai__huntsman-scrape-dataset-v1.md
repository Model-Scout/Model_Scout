---
type: "dataset"
id: "tulipfarmai/huntsman-scrape-dataset-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/tulipfarmai/huntsman-scrape-dataset-v1"
downloads: 26
summary: "웹 스크래핑 엔진의 콘텐츠 품질 평가를 위한 다국어 웹 페이지 스크래핑 벤치마크 데이터셋입니다."
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
  - "[[중규모 데이터]]"
---
# tulipfarmai/huntsman-scrape-dataset-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/tulipfarmai/huntsman-scrape-dataset-v1)

웹 스크래핑 엔진의 콘텐츠 품질 평가를 위한 다국어 웹 페이지 스크래핑 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = ``truth_text`: ~100-word core snippet (main content)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = ``truth_text`: ~100-word core snippet (main content)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `63 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `255` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A benchmark for evaluating web scraping engines on content quality, balanced across language, script direction, rendering technology, page type, media format, d` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Use `dev` for tuning and report scores on `test`.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `truth_text` 열 p90 1019자 ≈ 255 토큰 (viewer statistics, default/test)
