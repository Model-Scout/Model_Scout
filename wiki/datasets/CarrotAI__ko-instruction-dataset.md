---
type: "dataset"
id: "CarrotAI/ko-instruction-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/CarrotAI/ko-instruction-dataset"
downloads: 142
summary: "WizardLM 모델로 생성된 고품질 한국어 명령어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
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
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# CarrotAI/ko-instruction-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/CarrotAI/ko-instruction-dataset)

WizardLM 모델로 생성된 고품질 한국어 명령어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `한국어로 이루어진 고품질 한국어 데이터셋 입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `한국어로 이루어진 고품질 한국어 데이터셋 입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1468` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어로 이루어진 고품질 한국어 데이터셋 입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `고품질 한국어 데이터셋 입니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 2201자 ≈ 1468 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[CarrotAI__Carrot-Ko-2B-Instruct|CarrotAI/Carrot-Ko-2B-Instruct]]
- [[tensorblock__Llama-3.2-Rabbit-Ko-1B-Instruct-GGUF|tensorblock/Llama-3.2-Rabbit-Ko-1B-Instruct-GGUF]]
