---
type: "dataset"
id: "schneiderkamplab/dfm14-ko-span-filling-r1"
source: "huggingface"
url: "https://huggingface.co/datasets/schneiderkamplab/dfm14-ko-span-filling-r1"
downloads: 34
summary: "Gemma 4 26B-A4B 자동 검토를 거친 DFM14 한국어 스팬 채우기 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# schneiderkamplab/dfm14-ko-span-filling-r1

> dataset · [Hugging Face](https://huggingface.co/datasets/schneiderkamplab/dfm14-ko-span-filling-r1)

Gemma 4 26B-A4B 자동 검토를 거친 DFM14 한국어 스팬 채우기 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Training supervises the indicated final assistant.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Complete chat history is preserved.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `All final assistant targets fit the native Gemma 4 template within 4,096 tokens` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1660` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Training supervises the indicated final assistant.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `messages_json` 열 p90 2490자 ≈ 1660 토큰 (viewer statistics, default/train)
