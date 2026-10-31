---
type: "dataset"
id: "MyeongHo0621/korean-quality-cleaned"
source: "huggingface"
url: "https://huggingface.co/datasets/MyeongHo0621/korean-quality-cleaned"
downloads: 37
summary: "여러 고품질 한국어 데이터셋을 정제·표준화한 한국어 instruction 데이터셋으로, 한국어 언어 모델 파인튜닝 등에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# MyeongHo0621/korean-quality-cleaned

> dataset · [Hugging Face](https://huggingface.co/datasets/MyeongHo0621/korean-quality-cleaned)

여러 고품질 한국어 데이터셋을 정제·표준화한 한국어 instruction 데이터셋으로, 한국어 언어 모델 파인튜닝 등에 사용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Korean language model fine-tuning
- Instruction tuning
- Conversational AI training
- Question-answering systems
- General-purpose Korean LLM training` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:question_answering = `Standardized messages format (OpenAI-compatible)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Standardized messages format (OpenAI-compatible)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a cleaned and standardized Korean instruction dataset, combining multiple high-quality open-source Korean datasets` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Korean language model fine-tuning
- Instruction tuning
- Conversational AI training
- Question-answering systems
- General-purpose Korean LLM training` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
