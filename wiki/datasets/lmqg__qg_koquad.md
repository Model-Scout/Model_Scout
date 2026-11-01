---
type: "dataset"
id: "lmqg/qg_koquad"
source: "huggingface"
url: "https://huggingface.co/datasets/lmqg/qg_koquad"
downloads: 382
summary: "KorQuAD 데이터셋을 기반으로 한 질문 생성(QG)용 한국어 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lmqg/qg_koquad

> dataset · [Hugging Face](https://huggingface.co/datasets/lmqg/qg_koquad)

KorQuAD 데이터셋을 기반으로 한 질문 생성(QG)용 한국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[언어 모델링]] — metadata · task_ids = `language-modeling` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `The data fields are the same among all splits. - `question`: a `string` feature. - `paragraph`: a `string` feature. - `answer`: a `string` feature.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Each of `paragraph_answer`, `paragraph_sentence`, and `sentence_answer` feature is assumed to be used to train a question generation model` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `573` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Since the original dataset only contains training/validation set, we manually sample test set from training set` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `paragraph_question` 열 p90 860자 ≈ 573 토큰 (viewer statistics, qg_koquad/validation)
