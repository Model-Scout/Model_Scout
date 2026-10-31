---
type: "dataset"
id: "locuslab/TOFU"
source: "huggingface"
url: "https://huggingface.co/datasets/locuslab/TOFU"
downloads: 53835
summary: "TOFU 데이터셋은 허구의 자서전을 기반으로 한 질의응답 데이터로, 대형 언어 모델의 언러닝 성능 평가용입니다."
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
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# locuslab/TOFU

> dataset · [Hugging Face](https://huggingface.co/datasets/locuslab/TOFU)

TOFU 데이터셋은 허구의 자서전을 기반으로 한 질의응답 데이터로, 대형 언어 모델의 언러닝 성능 평가용입니다.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · readme, tags = `LLM` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, tags, task_categories, task_ids = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `The dataset comprises question-answer pairs based on autobiographies of 200 different authors` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `The dataset comprises question-answer pairs based on autobiographies of 200 different authors` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `64` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The TOFU dataset serves as a benchmark for evaluating unlearning performance of large language models on realistic tasks.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The TOFU dataset serves as a benchmark for evaluating unlearning performance of large language models on realistic tasks.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 257자 ≈ 64 토큰 (viewer statistics, full/train)

## 이 데이터로 학습한 모델

- [[Aya168__aya-expanse-8b-tofu-13lang-v3|Aya168/aya-expanse-8b-tofu-13lang-v3]]
