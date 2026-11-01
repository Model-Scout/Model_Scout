---
type: "dataset"
id: "neuralfoundry-coder/banking77-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/neuralfoundry-coder/banking77-ko"
downloads: 97
summary: "Banking77 데이터셋의 한국어 번역 버전으로, 은행 고객 질의를 77개 인텐트로 분류하는 텍스트 분류용 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# neuralfoundry-coder/banking77-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/neuralfoundry-coder/banking77-ko)

Banking77 데이터셋의 한국어 번역 버전으로, 은행 고객 질의를 77개 인텐트로 분류하는 텍스트 분류용 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[번역]] — tag_match · tags = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:translation = `고객 질의 (번역된 한국어)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `인텐트 분류 ID (0-76)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `61` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `학습용 · Banking77-ko (한국어 번역 버전)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text_original` 열 p90 91자 ≈ 61 토큰 (viewer statistics, default/test)
