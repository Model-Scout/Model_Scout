---
type: "dataset"
id: "sardinelab/DocBlocks"
source: "huggingface"
url: "https://huggingface.co/datasets/sardinelab/DocBlocks"
downloads: 239
summary: "DocBlocks는 긴 문맥 번역을 위한 다국어 문서 수준 기계 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[nl]]"
  - "[[pt]]"
  - "[[ru]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# sardinelab/DocBlocks

> dataset · [Hugging Face](https://huggingface.co/datasets/sardinelab/DocBlocks)

DocBlocks는 긴 문맥 번역을 위한 다국어 문서 수준 기계 번역 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `It contains full documents with natural discourse structures and contextual alignment` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `helping models maintain coherence, consistency, and high translation quality across longer texts` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `DocBlocks is a high-quality, multilingual document-level machine translation (MT) dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `designed to fine-tune large language models (LLMs) on long-context translation tasks` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[mradermacher__Tower-7B-d2d-GGUF|mradermacher/Tower-7B-d2d-GGUF]]
- [[ynklab__Qwen2.5-7B-Sep_0c1t|ynklab/Qwen2.5-7B-Sep_0c1t]]
- [[ynklab__Qwen2.5-7B-Sep_1c1t|ynklab/Qwen2.5-7B-Sep_1c1t]]
- [[ynklab__Qwen2.5-7B-Sep_2c1t|ynklab/Qwen2.5-7B-Sep_2c1t]]
- [[ynklab__Qwen2.5-7B-Stair_2c1t|ynklab/Qwen2.5-7B-Stair_2c1t]]
- [[ynklab__Qwen2.5-7B-Stair_FS4|ynklab/Qwen2.5-7B-Stair_FS4]]
- [[ynklab__Qwen2.5-7B-d2d|ynklab/Qwen2.5-7B-d2d]]
- [[ynklab__Tower-7B-Sep_0c1t|ynklab/Tower-7B-Sep_0c1t]]
- [[ynklab__Tower-7B-Sep_1c1t|ynklab/Tower-7B-Sep_1c1t]]
- [[ynklab__Tower-7B-Sep_2c1t|ynklab/Tower-7B-Sep_2c1t]]
- [[ynklab__Tower-7B-Stair_2c1t|ynklab/Tower-7B-Stair_2c1t]]
- [[ynklab__Tower-7B-Stair_FS4|ynklab/Tower-7B-Stair_FS4]]
- [[ynklab__Tower-7B-Uni_2c1t|ynklab/Tower-7B-Uni_2c1t]]
- [[ynklab__Tower-7B-d2d|ynklab/Tower-7B-d2d]]
