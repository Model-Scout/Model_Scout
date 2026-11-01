---
type: "dataset"
id: "ThakiCloud/quantization-rebuild-noise-floor"
source: "huggingface"
url: "https://huggingface.co/datasets/ThakiCloud/quantization-rebuild-noise-floor"
downloads: 115
summary: "Qwen3.8-27B 모델의 동일 양자화 레시피 반복 실행 시 발생하는 차이를 측정한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ThakiCloud/quantization-rebuild-noise-floor

> dataset · [Hugging Face](https://huggingface.co/datasets/ThakiCloud/quantization-rebuild-noise-floor)

Qwen3.8-27B 모델의 동일 양자화 레시피 반복 실행 시 발생하는 차이를 측정한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `We evaluated both builds in a single serving run so no engine or configuration difference could leak in, then measured how far apart they landed.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `We quantized Qwen3.8-27B to W4A16 with GPTQ, then ran the exact same recipe a second time` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `We evaluated both builds in a single serving run so no engine or configuration difference could leak in, then measured how far apart they landed.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Part of [Evals & Reproducibility](https://huggingface.co/collections/ThakiCloud/evals-and-reproducibility-6a9e6effa3c3b027077af99e).` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is the measurement.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
