---
type: "dataset"
id: "afkfatih/turkish-gemma-51k"
source: "huggingface"
url: "https://huggingface.co/datasets/afkfatih/turkish-gemma-51k"
downloads: 33
summary: "Türkçe sohbet ve talimat takip görevleri için 51,914개 대화 예제를 포함한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[tr]]"
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
# afkfatih/turkish-gemma-51k

> dataset · [Hugging Face](https://huggingface.co/datasets/afkfatih/turkish-gemma-51k)

Türkçe sohbet ve talimat takip görevleri için 51,914개 대화 예제를 포함한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Format: Chat/Conversation` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Format: Chat/Conversation` · 신뢰도 medium
- **언어**: [[tr]] — metadata · languages = `tr` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Türkçe sohbet ve talimat takip etme görevleri için hazırlanmış 51.914 konuşma örneği içerir.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Türkçe sohbet botları eğitimi
Instruction-tuning
Fine-tuning LLM modelleri (Gemma, Llama, vb.)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[mradermacher__LFM2-8B-A1B-TR-GGUF|mradermacher/LFM2-8B-A1B-TR-GGUF]]
