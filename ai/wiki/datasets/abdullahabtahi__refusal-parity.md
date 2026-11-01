---
type: "dataset"
id: "abdullahabtahi/refusal-parity"
source: "huggingface"
url: "https://huggingface.co/datasets/abdullahabtahi/refusal-parity"
downloads: 75
summary: "Refusal Parity 데이터셋은 다국어 안전성 수정을 평가하는 감사 데이터로, 언어별 공정성을 분석함."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# abdullahabtahi/refusal-parity

> dataset · [Hugging Face](https://huggingface.co/datasets/abdullahabtahi/refusal-parity)

Refusal Parity 데이터셋은 다국어 안전성 수정을 평가하는 감사 데이터로, 언어별 공정성을 분석함.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `the evaluation prompts` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `one label row per model response for every run: refusal and harm under each judge, plus the response language` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
