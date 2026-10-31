---
type: "dataset"
id: "nayohan/Magpie-Phi3-Pro-300K-Filtered-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/Magpie-Phi3-Pro-300K-Filtered-ko"
downloads: 25
summary: "Magpie-Align/Magpie-Phi3-Pro-300K-Filtered 데이터셋을 번역한 원시 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nayohan/Magpie-Phi3-Pro-300K-Filtered-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/Magpie-Phi3-Pro-300K-Filtered-ko)

Magpie-Align/Magpie-Phi3-Pro-300K-Filtered 데이터셋을 번역한 원시 번역 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `Translate Magpie-Align/Magpie-Phi3-Pro-300K-Filtered using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `Translate Magpie-Align/Magpie-Phi3-Pro-300K-Filtered` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `This is a raw translation dataset.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `27616` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This is a raw translation dataset.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 41423자 ≈ 27616 토큰 (viewer statistics, default/train)
