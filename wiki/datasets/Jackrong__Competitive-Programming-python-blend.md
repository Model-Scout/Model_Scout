---
type: "dataset"
id: "Jackrong/Competitive-Programming-python-blend"
source: "huggingface"
url: "https://huggingface.co/datasets/Jackrong/Competitive-Programming-python-blend"
downloads: 631
summary: "Python 중심의 경쟁 프로그래밍 및 코드 추론용 혼합 감독 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Jackrong/Competitive-Programming-python-blend

> dataset · [Hugging Face](https://huggingface.co/datasets/Jackrong/Competitive-Programming-python-blend)

Python 중심의 경쟁 프로그래밍 및 코드 추론용 혼합 감독 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `supervised fine-tuning dataset centered on competitive programming, code reasoning` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `Each line in `clean.jsonl` is one JSON object with a `messages` field` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `instruction-style problem solving` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `competitive programming, code reasoning, and instruction-style problem solving` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset is intended for supervised fine-tuning or continued instruction tuning of code-capable models` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Jackrong__Qwen3.5-4B-Neo|Jackrong/Qwen3.5-4B-Neo]]
- [[Jackrong__Qwen3.5-4B-Neo-GGUF|Jackrong/Qwen3.5-4B-Neo-GGUF]]
- [[bartowski__Jackrong_Qwen3.5-4B-Neo-GGUF|bartowski/Jackrong_Qwen3.5-4B-Neo-GGUF]]
