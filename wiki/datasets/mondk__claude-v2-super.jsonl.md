---
type: "dataset"
id: "mondk/claude-v2-super.jsonl"
source: "huggingface"
url: "https://huggingface.co/datasets/mondk/claude-v2-super.jsonl"
downloads: 81
summary: "Claude Sonnet 5/Fable 5와의 채팅에서 수집한 대화 데이터셋입니다."
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
# mondk/claude-v2-super.jsonl

> dataset · [Hugging Face](https://huggingface.co/datasets/mondk/claude-v2-super.jsonl)

Claude Sonnet 5/Fable 5와의 채팅에서 수집한 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset was collected during a chat with Claude Sonnet 5/Fable 5.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Format:
{"instruction": "...", "output": "..."}` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Format:
{"instruction": "...", "output": "..."}` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1147` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Created/Collected by: mondk` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 4586자 ≈ 1147 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[mondk__claude-sonnet-qwen2.5-7B-it|mondk/claude-sonnet-qwen2.5-7B-it]]
