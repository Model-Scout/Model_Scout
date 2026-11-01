---
type: "dataset"
id: "olaverse/qg-eval-multi-fresh"
source: "huggingface"
url: "https://huggingface.co/datasets/olaverse/qg-eval-multi-fresh"
downloads: 60
summary: "25개 언어의 평가용 미사용 문장 625개로 구성된 질문 생성 모델 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
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
  - "[[소규모 데이터]]"
---
# olaverse/qg-eval-multi-fresh

> dataset · [Hugging Face](https://huggingface.co/datasets/olaverse/qg-eval-multi-fresh)

25개 언어의 평가용 미사용 문장 625개로 구성된 질문 생성 모델 평가 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Evaluating question-generation models via round-trip self-consistency: generate questions on these passages, embed the questions and the passage pool, and check` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval = `625 passages (~25 per language, 25 languages)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Evaluation is done by generating questions with the model under test and checking round-trip retrieval` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `25 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `479` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `sampled from the same source as the training data` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Held-out evaluation passages for olaverse/mist-qg-1.5b — provably never seen during training, used to compute the model's published round-trip keep-rate.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `passage` 열 p90 1916자 ≈ 479 토큰 (viewer statistics, default/train)
