---
type: "dataset"
id: "naver-ai/kobbq"
source: "huggingface"
url: "https://huggingface.co/datasets/naver-ai/kobbq"
downloads: 190
summary: "KoBBQ는 한국 문화에 맞춘 사회적 편향 평가용 한국어 질의응답 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# naver-ai/kobbq

> dataset · [Hugging Face](https://huggingface.co/datasets/naver-ai/kobbq)

KoBBQ는 한국 문화에 맞춘 사회적 편향 평가용 한국어 질의응답 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `zero-shot-classification` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `language models (LMs)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `evaluate social biases of language models` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `129` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `social biases depend heavily on the cultural context` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `To evaluate language models using KoBBQ` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 193자 ≈ 129 토큰 (viewer statistics, default/test)
