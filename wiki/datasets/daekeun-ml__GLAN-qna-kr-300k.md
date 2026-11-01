---
type: "dataset"
id: "daekeun-ml/GLAN-qna-kr-300k"
source: "huggingface"
url: "https://huggingface.co/datasets/daekeun-ml/GLAN-qna-kr-300k"
downloads: 40
summary: "GLAN-QnA-KR은 30만 건 이상의 한국어 질문-답변 데이터로, 일반화된 지침 튜닝에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# daekeun-ml/GLAN-qna-kr-300k

> dataset · [Hugging Face](https://huggingface.co/datasets/daekeun-ml/GLAN-qna-kr-300k)

GLAN-QnA-KR은 30만 건 이상의 한국어 질문-답변 데이터로, 일반화된 지침 튜닝에 활용됨.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Korean question/answer text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Korean question/answer text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `10624` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `openrail` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `a single `train` split` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 15936자 ≈ 10624 토큰 (viewer statistics, default/train)
