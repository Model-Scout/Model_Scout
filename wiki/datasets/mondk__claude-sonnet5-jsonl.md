---
type: "dataset"
id: "mondk/claude-sonnet5-jsonl"
source: "huggingface"
url: "https://huggingface.co/datasets/mondk/claude-sonnet5-jsonl"
downloads: 197
summary: "Claude Sonnet 5와의 채팅에서 수집한 대화 데이터셋으로, instruction과 output 형식으로 구성됨."
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
  - "[[다국어]]"
  - "[[vi]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# mondk/claude-sonnet5-jsonl

> dataset · [Hugging Face](https://huggingface.co/datasets/mondk/claude-sonnet5-jsonl)

Claude Sonnet 5와의 채팅에서 수집한 대화 데이터셋으로, instruction과 output 형식으로 구성됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset was collected during a chat with Claude Sonnet 5.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Format:
{"instruction": "...", "output": "..."}` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Format:
{"instruction": "...", "output": "..."}` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `715` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset was collected during a chat with Claude Sonnet 5.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 2860자 ≈ 715 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[mondk__claude-llama-8B-think|mondk/claude-llama-8B-think]]
- [[mondk__claude-llama-8B-think-GGuf|mondk/claude-llama-8B-think-GGuf]]
- [[mondk__claude-llama-8B-think-mlx-4Bit|mondk/claude-llama-8B-think-mlx-4Bit]]
