---
type: "dataset"
id: "lilacai/glaive-function-calling-v2-sharegpt"
source: "huggingface"
url: "https://huggingface.co/datasets/lilacai/glaive-function-calling-v2-sharegpt"
downloads: 78
summary: "glaive/glaive-function-calling-v2 데이터를 ShareGPT 형식으로 변환한 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
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
# lilacai/glaive-function-calling-v2-sharegpt

> dataset · [Hugging Face](https://huggingface.co/datasets/lilacai/glaive-function-calling-v2-sharegpt)

glaive/glaive-function-calling-v2 데이터를 ShareGPT 형식으로 변환한 대화 데이터셋입니다.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `The original columns "system" and "chat" still exist on the dataset.` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1144` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset takes the glaive/glaive-function-calling-v2 dataset and formats it with ShareGPT using Lilac` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `chat` 열 p90 4575자 ≈ 1144 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[QuantFactory__Linkbricks-Horizon-AI-Korean-Advanced-12B-GGUF|QuantFactory/Linkbricks-Horizon-AI-Korean-Advanced-12B-GGUF]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Advanced-12B|Saxo/Linkbricks-Horizon-AI-Korean-Advanced-12B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Advanced-27B|Saxo/Linkbricks-Horizon-AI-Korean-Advanced-27B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Advanced-56B|Saxo/Linkbricks-Horizon-AI-Korean-Advanced-56B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Advanced-70B|Saxo/Linkbricks-Horizon-AI-Korean-Advanced-70B]]
- [[Saxo__Linkbricks-Horizon-AI-Korean-Advanced-8B|Saxo/Linkbricks-Horizon-AI-Korean-Advanced-8B]]
- [[bartowski__Linkbricks-Horizon-AI-Japanese-Pro-V3-70B-GGUF|bartowski/Linkbricks-Horizon-AI-Japanese-Pro-V3-70B-GGUF]]
- [[tensorblock__Linkbricks-Horizon-AI-Korean-Pro-12B-GGUF|tensorblock/Linkbricks-Horizon-AI-Korean-Pro-12B-GGUF]]
- [[tensorblock__Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF|tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF]]
