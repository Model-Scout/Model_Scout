---
type: "dataset"
id: "DigitalLearningGmbH/MATH-lighteval"
source: "huggingface"
url: "https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval"
downloads: 29097
summary: "수학 경시대회 문제와 단계별 해답으로 답안 유도 및 설명 생성 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# DigitalLearningGmbH/MATH-lighteval

> dataset · [Hugging Face](https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval)

수학 경시대회 문제와 단계별 해답으로 답안 유도 및 설명 생성 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Each problem in MATH has a full step-by-step solution, which can be used to teach models to generate answer derivations and explanations.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `A data instance consists of a competition math problem and its step-by-step solution written in LaTeX and natural language.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Each problem in MATH has a full step-by-step solution, which can be used to teach models to generate answer derivations and explanations.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `266` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `The Mathematics Aptitude Test of Heuristics (MATH) dataset consists of problems from mathematics competitions, including the AMC 10, AMC 12, AIME, and more.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This version of the dataset contains appropriate builder configs s.t. it can be used as a drop-in replacement for the inexplicably missing `lighteval/MATH` data` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `solution` 열 p90 1066자 ≈ 266 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[PeterAM4__Qwen3-Embedding-0.6B-GGUF|PeterAM4/Qwen3-Embedding-0.6B-GGUF]]
- [[zhiqian99__Qwen3-Embedding-0.6B-GGUF|zhiqian99/Qwen3-Embedding-0.6B-GGUF]]
