---
type: "dataset"
id: "kuotient/gsm8k-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/kuotient/gsm8k-ko"
downloads: 172
summary: "kuotient/gsm8k-ko는 한국어 수학 문제 해결 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# kuotient/gsm8k-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/kuotient/gsm8k-ko)

kuotient/gsm8k-ko는 한국어 수학 문제 해결 평가용 데이터셋입니다.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `328` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `gsm8k-ko` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `How to evaluate` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `answer_en` 열 p90 491자 ≈ 328 토큰 (viewer statistics, default/test)

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
