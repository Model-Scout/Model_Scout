---
type: "dataset"
id: "kyujinpy/KOR-OpenOrca-Platypus-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/kyujinpy/KOR-OpenOrca-Platypus-v2"
downloads: 44
summary: "KOR-OpenOrca-Platypus-v2는 수작업으로 번역 오류를 수정한 고품질 한국어 자연어처리 학습 데이터셋입니다."
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kyujinpy/KOR-OpenOrca-Platypus-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/kyujinpy/KOR-OpenOrca-Platypus-v2)

KOR-OpenOrca-Platypus-v2는 수작업으로 번역 오류를 수정한 고품질 한국어 자연어처리 학습 데이터셋입니다.

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
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `716` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The data is primarily used for training and evaluation in the field of natural language processing.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The data is primarily used for training and evaluation in the field of natural language processing.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The data is primarily used for training and evaluation in the field of natural language processing.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1074자 ≈ 716 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[tensorblock__yunsung-llama-2-koen-13b-linkbricks-sft-basic-v1-GGUF|tensorblock/yunsung-llama-2-koen-13b-linkbricks-sft-basic-v1-GGUF]]
