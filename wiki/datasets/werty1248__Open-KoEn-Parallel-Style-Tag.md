---
type: "dataset"
id: "werty1248/Open-KoEn-Parallel-Style-Tag"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/Open-KoEn-Parallel-Style-Tag"
downloads: 26
summary: "한국어 텍스트 스타일을 태그 형태로 분류한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
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
# werty1248/Open-KoEn-Parallel-Style-Tag

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/Open-KoEn-Parallel-Style-Tag)

한국어 텍스트 스타일을 태그 형태로 분류한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `한국어 텍스트의 스타일을 태그 형태로 제안하도록 요청하였습니다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `한국어 텍스트의 스타일을 태그 형태로 제안하도록 요청하였습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `분류 결과를 python Dict[List] 형태로 출력합니다.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `694` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 텍스트의 스타일을 태그 형태로 제안하도록 요청하였습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `gemini-1.5-flash를 이용하여, 한국어 텍스트의 스타일을 태그 형태로 제안하도록 요청하였습니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `source_text` 열 p90 1041자 ≈ 694 토큰 (viewer statistics, default/train)
