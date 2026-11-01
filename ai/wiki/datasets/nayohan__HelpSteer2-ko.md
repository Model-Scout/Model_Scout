---
type: "dataset"
id: "nayohan/HelpSteer2-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/HelpSteer2-ko"
downloads: 28
summary: "nvidia/HelpSteer2 데이터셋을 번역한 원시 데이터로 보상 모델 학습용입니다."
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
# nayohan/HelpSteer2-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/HelpSteer2-ko)

nvidia/HelpSteer2 데이터셋을 번역한 원시 데이터로 보상 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Translated nvidia/HelpSteer2 using nayohan/llama3-instrucTrans-enko-8b` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Translated nvidia/HelpSteer2 using nayohan/llama3-instrucTrans-enko-8b` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `17226` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Open-source dataset for training top-performing reward models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 25839자 ≈ 17226 토큰 (viewer statistics, default/train)
