---
type: "dataset"
id: "maywell/ko_Ultrafeedback_binarized"
source: "huggingface"
url: "https://huggingface.co/datasets/maywell/ko_Ultrafeedback_binarized"
downloads: 245
summary: "Synatra-7B-Translation 모델로 번역·정제한 Ultrafeedback_binarized 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
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
# maywell/ko_Ultrafeedback_binarized

> dataset · [Hugging Face](https://huggingface.co/datasets/maywell/ko_Ultrafeedback_binarized)

Synatra-7B-Translation 모델로 번역·정제한 Ultrafeedback_binarized 데이터셋입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `본 데이터는 Synatra-7B-Translation 모델을 통해 Ultrafeedback_binarized를 번역하고 정제한 데이터셋입니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `본 데이터는 Synatra-7B-Translation 모델을 통해 Ultrafeedback_binarized를 번역하고 정제한 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `본 데이터는 Synatra-7B-Translation 모델을 통해 Ultrafeedback_binarized를 번역하고 정제한 데이터셋입니다.` · 신뢰도 medium
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1125` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `데이터를 이용하여 훈련된 모델에 대한 상업적 사용은 허용됩니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 4499자 ≈ 1125 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[QuantFactory__Linkbricks-Horizon-AI-Korean-Advanced-12B-GGUF|QuantFactory/Linkbricks-Horizon-AI-Korean-Advanced-12B-GGUF]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Advanced-12B|Saxo/Linkbricks-Horizon-AI-Korean-Advanced-12B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Advanced-27B|Saxo/Linkbricks-Horizon-AI-Korean-Advanced-27B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Advanced-56B|Saxo/Linkbricks-Horizon-AI-Korean-Advanced-56B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Advanced-70B|Saxo/Linkbricks-Horizon-AI-Korean-Advanced-70B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Advanced-8B|Saxo/Linkbricks-Horizon-AI-Korean-Advanced-8B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Gemma-2-sft-dpo-27B|Saxo/Linkbricks-Horizon-AI-Korean-Gemma-2-sft-dpo-27B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Mistral-Nemo-sft-dpo-12B|Saxo/Linkbricks-Horizon-AI-Korean-Mistral-Nemo-sft-dpo-12B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Mixtral-sft-dpo-8x7b|Saxo/Linkbricks-Horizon-AI-Korean-Mixtral-sft-dpo-8x7b]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-llama-3.1-sft-dpo-8B|Saxo/Linkbricks-Horizon-AI-Korean-llama-3.1-sft-dpo-8B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-llama3.1-sft-dpo-70B|Saxo/Linkbricks-Horizon-AI-Korean-llama3.1-sft-dpo-70B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-llama3.1-sft-rlhf-dpo-8B|Saxo/Linkbricks-Horizon-AI-Korean-llama3.1-sft-rlhf-dpo-8B]]
- [[bartowski__Linkbricks-Horizon-AI-Japanese-Pro-V3-70B-GGUF|bartowski/Linkbricks-Horizon-AI-Japanese-Pro-V3-70B-GGUF]]
- [[pathcosmos__frankenstallm|pathcosmos/frankenstallm]]
- [[tensorblock__Linkbricks-Horizon-AI-Korean-Pro-12B-GGUF|tensorblock/Linkbricks-Horizon-AI-Korean-Pro-12B-GGUF]]
- [[tensorblock__Mistral-instruct-Y24-DPO-GGUF|tensorblock/Mistral-instruct-Y24-DPO-GGUF]]
- [[tensorblock__OPEN_SOLAR_KO_10.7B_DPO_Adapter_Attach-GGUF|tensorblock/OPEN_SOLAR_KO_10.7B_DPO_Adapter_Attach-GGUF]]
- [[tensorblock__Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF|tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF]]
