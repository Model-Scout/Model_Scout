---
type: "dataset"
id: "Seungjun/Korean-Olympiad-TDCS-3K"
source: "huggingface"
url: "https://huggingface.co/datasets/Seungjun/Korean-Olympiad-TDCS-3K"
downloads: 38
summary: "한국 올림피아드 수학 추론 문제로 구성된 균형 잡힌 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[교육]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Seungjun/Korean-Olympiad-TDCS-3K

> dataset · [Hugging Face](https://huggingface.co/datasets/Seungjun/Korean-Olympiad-TDCS-3K)

한국 올림피아드 수학 추론 문제로 구성된 균형 잡힌 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `A balanced Korean Olympiad mathematics reasoning dataset` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Problem embeddings: Qwen/Qwen3-Embedding-4B, 1,024 dimensions` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation = `Korean Olympiad mathematics reasoning dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Korean Olympiad mathematics reasoning dataset` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1724` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `Korean Olympiad mathematics reasoning dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `solution_ko` 열 p90 2587자 ≈ 1724 토큰 (viewer statistics, default/validation)
