---
type: "dataset"
id: "nayohan/preference-collection-ko-full"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/preference-collection-ko-full"
downloads: 33
summary: "prometheus-eval/Preference-Collection 데이터를 nayohan/llama3-instrucTrans-enko-8b 모델로 번역한 데이터셋입니다."
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
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nayohan/preference-collection-ko-full

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/preference-collection-ko-full)

prometheus-eval/Preference-Collection 데이터를 nayohan/llama3-instrucTrans-enko-8b 모델로 번역한 데이터셋입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `Translate prometheus-eval/Preference-Collection using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `Translate prometheus-eval/Preference-Collection using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Translate prometheus-eval/Preference-Collection using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 medium
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1579` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 6317자 ≈ 1579 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[pathcosmos__frankenstallm|pathcosmos/frankenstallm]]
