---
type: "dataset"
id: "nayohan/Evol-Instruct-Code-80k-v1-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/Evol-Instruct-Code-80k-v1-ko"
downloads: 27
summary: "nickrosh/Evol-Instruct-Code-80k-v1 데이터셋을 한국어로 번역한 원시 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nayohan/Evol-Instruct-Code-80k-v1-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/Evol-Instruct-Code-80k-v1-ko)

nickrosh/Evol-Instruct-Code-80k-v1 데이터셋을 한국어로 번역한 원시 번역 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `This is a raw translation dataset.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `This is a raw translation dataset.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `This is a raw translation dataset.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2160` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This is a raw translation dataset.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 3241자 ≈ 2160 토큰 (viewer statistics, default/train)
