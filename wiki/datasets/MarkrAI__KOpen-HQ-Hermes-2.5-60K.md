---
type: "dataset"
id: "MarkrAI/KOpen-HQ-Hermes-2.5-60K"
source: "huggingface"
url: "https://huggingface.co/datasets/MarkrAI/KOpen-HQ-Hermes-2.5-60K"
downloads: 43
summary: "MarkrAI가 개발한 한국어 고품질 LLM 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# MarkrAI/KOpen-HQ-Hermes-2.5-60K

> dataset · [Hugging Face](https://huggingface.co/datasets/MarkrAI/KOpen-HQ-Hermes-2.5-60K)

MarkrAI가 개발한 한국어 고품질 LLM 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `we used SOTA LLMs (GPT-4 Turbo, Gemini, Wizard LM, Llama 3.1 405B) to score the data with Alpaca form prompts` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling, task:question_answering = `performed translation tasks using the DeepL API with 8 multiprocessing threads` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:question_answering = `performed translation tasks using the DeepL API with 8 multiprocessing threads` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `we then evaluated the appropriateness of these prompts and extracted and published the data with high scores` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
