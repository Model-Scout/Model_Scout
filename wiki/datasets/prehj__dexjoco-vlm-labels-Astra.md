---
type: "dataset"
id: "prehj/dexjoco-vlm-labels-Astra"
source: "huggingface"
url: "https://huggingface.co/datasets/prehj/dexjoco-vlm-labels-Astra"
downloads: 57
summary: "DexJoCo 단일 팔 작업 6종에 대한 VLM 라벨 13,352개를 포함한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# prehj/dexjoco-vlm-labels-Astra

> dataset · [Hugging Face](https://huggingface.co/datasets/prehj/dexjoco-vlm-labels-Astra)

DexJoCo 단일 팔 작업 6종에 대한 VLM 라벨 13,352개를 포함한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Actual VLM labels, grades A–D, conf, instruction, measured facts, camera names and prompt/image hashes` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Actual VLM labels, grades A–D, conf, instruction, measured facts, camera names and prompt/image hashes` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Actual VLM labels, grades A–D, conf, instruction, measured facts, camera names and prompt/image hashes` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `These are annotation sidecars, not robot images, action trajectories, contact ground truth, or compression-speed labels.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `These are annotation sidecars` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
