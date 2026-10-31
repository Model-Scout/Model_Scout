---
type: "dataset"
id: "beomi/KoAlpaca-v1.1a"
source: "huggingface"
url: "https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a"
downloads: 1015
summary: "KoAlpaca-v1.1a는 한국어 지침-응답 데이터셋으로 텍스트 생성에 활용됩니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
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
# beomi/KoAlpaca-v1.1a

> dataset · [Hugging Face](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a)

KoAlpaca-v1.1a는 한국어 지침-응답 데이터셋으로 텍스트 생성에 활용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `features: ['instruction', 'input', 'output']` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `features: ['instruction', 'input', 'output']` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `399` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `>>> ds = load_dataset("beomi/KoAlpaca-v1.1a", split="train")` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 599자 ≈ 399 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Edentns__DataVortexTL-1.1B-v0.1|Edentns/DataVortexTL-1.1B-v0.1]]
- [[blueapple8259__TinyKo|blueapple8259/TinyKo]]
- [[heegyu__llama-2-ko-7b-chat|heegyu/llama-2-ko-7b-chat]]
- [[mradermacher__DataVortexM-7B-Instruct-v0.1-GGUF|mradermacher/DataVortexM-7B-Instruct-v0.1-GGUF]]
- [[mradermacher__DataVortexM-7B-Instruct-v0.1-i1-GGUF|mradermacher/DataVortexM-7B-Instruct-v0.1-i1-GGUF]]
- [[mradermacher__DataVortexTL-1.1B-v0.1-GGUF|mradermacher/DataVortexTL-1.1B-v0.1-GGUF]]
- [[mradermacher__DataVortexTL-1.1B-v0.1-i1-GGUF|mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF]]
- [[shopkeeper__kor-finewiki-1b-chat|shopkeeper/kor-finewiki-1b-chat]]
- [[tensorblock__DataVortexTL-1.1B-v0.1-GGUF|tensorblock/DataVortexTL-1.1B-v0.1-GGUF]]
- [[tensorblock__Mistral-instruct-Y24-DPO-GGUF|tensorblock/Mistral-instruct-Y24-DPO-GGUF]]
- [[tensorblock__Mistral-instruct-Y24-v5-GGUF|tensorblock/Mistral-instruct-Y24-v5-GGUF]]
- [[tensorblock__yunsung-llama-2-koen-13b-linkbricks-sft-basic-v1-GGUF|tensorblock/yunsung-llama-2-koen-13b-linkbricks-sft-basic-v1-GGUF]]
