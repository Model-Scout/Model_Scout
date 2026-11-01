---
type: "dataset"
id: "cadazar/han2han-rl-data"
source: "huggingface"
url: "https://huggingface.co/datasets/cadazar/han2han-rl-data"
downloads: 86
summary: "한자-한글 혼합 문장과 한국어 지시문 대화 데이터를 포함한 Han2Han RL 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
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
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# cadazar/han2han-rl-data

> dataset · [Hugging Face](https://huggingface.co/datasets/cadazar/han2han-rl-data)

한자-한글 혼합 문장과 한국어 지시문 대화 데이터를 포함한 Han2Han RL 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `instruction-following example framed as Han2Han's IT stage framed it` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `a pool of Hanja-Hangul mixed sentences for the transcription tasks and a set of instruction-following chat turns` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `instruction-following chat turns for the replay term` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The open data subset of Han2Han's GRPO stage is a pool of Hanja-Hangul mixed sentences for the transcription tasks` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = ``pool/eval.parquet` | 1,024 | evaluation sentences from documents that contribute no training sentence` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = ``pool/train.parquet` | 40,000 | training sentences` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
