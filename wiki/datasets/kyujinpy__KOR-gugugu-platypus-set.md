---
type: "dataset"
id: "kyujinpy/KOR-gugugu-platypus-set"
source: "huggingface"
url: "https://huggingface.co/datasets/kyujinpy/KOR-gugugu-platypus-set"
downloads: 27
summary: "한국어 및 영어 외 특수문자 제거한 GPT4 번역 결과 약 2만 샘플 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kyujinpy/KOR-gugugu-platypus-set

> dataset · [Hugging Face](https://huggingface.co/datasets/kyujinpy/KOR-gugugu-platypus-set)

한국어 및 영어 외 특수문자 제거한 GPT4 번역 결과 약 2만 샘플 데이터셋입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `번역 task 최대한 제거. (~번역 task는 한국어로 번역하면 거의 100% 오류)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `한국어 및 영어를 제외한 다양한 외국어, 이모지, 특수 문자 등등 제거` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `GPT4 번역 결과에서 약 20k sampling` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `212` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `데이터셋 이용하셔서 모델이나 데이터셋을 만드실 때` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 846자 ≈ 212 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[tensorblock__PracticeLLM_Custom-KoLLM-13B-v5-GGUF|tensorblock/PracticeLLM_Custom-KoLLM-13B-v5-GGUF]]
