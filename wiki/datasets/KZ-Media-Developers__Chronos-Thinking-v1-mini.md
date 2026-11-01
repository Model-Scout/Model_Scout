---
type: "dataset"
id: "KZ-Media-Developers/Chronos-Thinking-v1-mini"
source: "huggingface"
url: "https://huggingface.co/datasets/KZ-Media-Developers/Chronos-Thinking-v1-mini"
downloads: 15
summary: "Chronos-Thinking-v1-mini은 LLM의 깊은 추론을 위한 고밀도 다국어 구조적 사고 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[no]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KZ-Media-Developers/Chronos-Thinking-v1-mini

> dataset · [Hugging Face](https://huggingface.co/datasets/KZ-Media-Developers/Chronos-Thinking-v1-mini)

Chronos-Thinking-v1-mini은 LLM의 깊은 추론을 위한 고밀도 다국어 구조적 사고 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `The dataset is presented in the `JSONL` (JSON Lines) format` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Structured thinking process + final response` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[no]] — metadata · languages = `no` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1153` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Chronos-Thinking-v1-mini is a fundamental, high—density dataset designed to initialize deep reasoning processes in large language models (LLM).` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is presented in the `JSONL` (JSON Lines) format, ideal for Supervised Fine-Tuning (SFT).` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 4614자 ≈ 1153 토큰 (viewer statistics, default/train)
