---
type: "dataset"
id: "BCCard/BCAI-Finance-Kor-Embedding-Triplet"
source: "huggingface"
url: "https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Triplet"
downloads: 82
summary: "한국 금융 도메인 문장 임베딩 모델 미세조정용 삼중항 데이터셋으로, 검증 및 테스트에 등급화된 관련성 레이블 포함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
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
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# BCCard/BCAI-Finance-Kor-Embedding-Triplet

> dataset · [Hugging Face](https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Triplet)

한국 금융 도메인 문장 임베딩 모델 미세조정용 삼중항 데이터셋으로, 검증 및 테스트에 등급화된 관련성 레이블 포함.

## 분류

- **작업**: [[임베딩]] — metadata · readme, tags, task_categories = `sentence-similarity` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `graded relevance labels for validation / test splits` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `332` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `validation / test splits` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `negative` 열 p90 497자 ≈ 332 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[BCCard__MoAI-Embedding-0.6B|BCCard/MoAI-Embedding-0.6B]]
- [[BCCard__MoAI-Embedding-4B|BCCard/MoAI-Embedding-4B]]
- [[mradermacher__MoAI-Embedding-0.6B-GGUF|mradermacher/MoAI-Embedding-0.6B-GGUF]]
- [[mradermacher__MoAI-Embedding-4B-GGUF|mradermacher/MoAI-Embedding-4B-GGUF]]
