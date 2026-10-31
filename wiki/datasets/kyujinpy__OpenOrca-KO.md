---
type: "dataset"
id: "kyujinpy/OpenOrca-KO"
source: "huggingface"
url: "https://huggingface.co/datasets/kyujinpy/OpenOrca-KO"
downloads: 169
summary: "OpenOrca 데이터셋 중 약 2만개를 번역한 한국어 데이터셋으로 자연어처리 모델 학습에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
  - "[[요약]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kyujinpy/OpenOrca-KO

> dataset · [Hugging Face](https://huggingface.co/datasets/kyujinpy/OpenOrca-KO)

OpenOrca 데이터셋 중 약 2만개를 번역한 한국어 데이터셋으로 자연어처리 모델 학습에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `This dataset supports a range of tasks including language modeling, text generation, and text augmentation.` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:information_extraction, task:language_modeling, task:question_answering, task:summarization, task:table_qa = `A data instance in this dataset represents entries from the FLAN collection which have been augmented by submitting the listed question to either GPT-4 or GPT-3` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:question_answering, task:summarization, task:table_qa = `The response is then entered into the response field.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `571` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The data is primarily used for training and evaluation in the field of natural language processing.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The data is primarily used for training and evaluation in the field of natural language processing.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 856자 ≈ 571 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Edentns__DataVortexTL-1.1B-v0.1|Edentns/DataVortexTL-1.1B-v0.1]]
- [[TheBloke__PiVoT-0.1-Evil-a-GGUF|TheBloke/PiVoT-0.1-Evil-a-GGUF]]
- [[TheBloke__PiVoT-0.1-early-GGUF|TheBloke/PiVoT-0.1-early-GGUF]]
- [[maywell__PiVoT-0.1-Evil-a|maywell/PiVoT-0.1-Evil-a]]
- [[mradermacher__DataVortexTL-1.1B-v0.1-GGUF|mradermacher/DataVortexTL-1.1B-v0.1-GGUF]]
- [[mradermacher__DataVortexTL-1.1B-v0.1-i1-GGUF|mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF]]
- [[tensorblock__DataVortexTL-1.1B-v0.1-GGUF|tensorblock/DataVortexTL-1.1B-v0.1-GGUF]]
- [[tensorblock__Mistral-instruct-Y24-DPO-GGUF|tensorblock/Mistral-instruct-Y24-DPO-GGUF]]
- [[tensorblock__Mistral-instruct-Y24-v5-GGUF|tensorblock/Mistral-instruct-Y24-v5-GGUF]]
- [[tensorblock__PiVoT-0.1-early-GGUF|tensorblock/PiVoT-0.1-early-GGUF]]
- [[tensorblock__mncai_Mistral-7B-v0.1-orca_platy-1k-GGUF|tensorblock/mncai_Mistral-7B-v0.1-orca_platy-1k-GGUF]]
