---
type: "dataset"
id: "qweqwqw113/cerpt-korean-stage1-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/qweqwqw113/cerpt-korean-stage1-dataset"
downloads: 24
summary: "수학, 논리, 다중 추론 예제를 포함한 CERPT 호환 한국어 추론 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# qweqwqw113/cerpt-korean-stage1-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/qweqwqw113/cerpt-korean-stage1-dataset)

수학, 논리, 다중 추론 예제를 포함한 CERPT 호환 한국어 추론 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Each record contains input_text, target_text, answer, operator labels, validity labels, and a four-cycle trace.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Each record contains input_text, target_text, answer, operator labels, validity labels, and a four-cycle trace.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `444` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a research dataset, not a general-purpose Korean language corpus.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The published files are the CERPT conversion and deterministic train/validation/test split.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `target_text` 열 p90 665자 ≈ 444 토큰 (viewer statistics, default/validation)
