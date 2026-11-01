---
type: "dataset"
id: "neogenesislab/cross-agent-review-queue-2026"
source: "huggingface"
url: "https://huggingface.co/datasets/neogenesislab/cross-agent-review-queue-2026"
downloads: 82
summary: "Codex와 Claude 간 다중 에이전트 코드 리뷰 대화록 데이터셋으로 에이전트 협업 연구용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# neogenesislab/cross-agent-review-queue-2026

> dataset · [Hugging Face](https://huggingface.co/datasets/neogenesislab/cross-agent-review-queue-2026)

Codex와 Claude 간 다중 에이전트 코드 리뷰 대화록 데이터셋으로 에이전트 협업 연구용입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[리랭킹]] — metadata · task_categories = `text-ranking` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation, task:reranking = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `the outcome is recorded as `new_signal` / `no_new_signal` / `failed`` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1084` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a real production AI-native company operating 11 business units` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 1627자 ≈ 1084 토큰 (viewer statistics, checkpoints/train)
