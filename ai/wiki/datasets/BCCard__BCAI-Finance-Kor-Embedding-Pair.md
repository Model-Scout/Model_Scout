---
type: "dataset"
id: "BCCard/BCAI-Finance-Kor-Embedding-Pair"
source: "huggingface"
url: "https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Pair"
downloads: 58
summary: "한국 금융 도메인 문장 임베딩 학습 및 검색 평가용 (anchor, positive) 쌍 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
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
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# BCCard/BCAI-Finance-Kor-Embedding-Pair

> dataset · [Hugging Face](https://huggingface.co/datasets/BCCard/BCAI-Finance-Kor-Embedding-Pair)

한국 금융 도메인 문장 임베딩 학습 및 검색 평가용 (anchor, positive) 쌍 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, tags, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `query text - either the raw chunk text (training) or its instruction-backtranslated variant (q1/q2/q3)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `doc text (chunker output - the chunk content itself)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `379` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `Retrieval corpus - source_chunk_id (≈36k unique chunks after q-variant dedupe) is the candidate pool for IR evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Training input - 45,589 (anchor, positive) pairs for in-batch / hard-negative contrastive learning.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `positive` 열 p90 569자 ≈ 379 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[BCCard__MoAI-Embedding-0.6B|BCCard/MoAI-Embedding-0.6B]]
- [[BCCard__MoAI-Embedding-4B|BCCard/MoAI-Embedding-4B]]
- [[mradermacher__MoAI-Embedding-0.6B-GGUF|mradermacher/MoAI-Embedding-0.6B-GGUF]]
- [[mradermacher__MoAI-Embedding-4B-GGUF|mradermacher/MoAI-Embedding-4B-GGUF]]
