---
type: "dataset"
id: "ENERZAiKR/UltraData-SFT-Agent-2609-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/UltraData-SFT-Agent-2609-ko"
downloads: 32
summary: "UltraData-SFT-Agent-2609의 한국어 현지화 데이터셋으로, 사용자 메시지와 어시스턴트 응답을 번역함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ENERZAiKR/UltraData-SFT-Agent-2609-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/UltraData-SFT-Agent-2609-ko)

UltraData-SFT-Agent-2609의 한국어 현지화 데이터셋으로, 사용자 메시지와 어시스턴트 응답을 번역함.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · tags = `tool-use` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Only the natural-language surface was translated: user messages, assistant replies, assistant reasoning` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Only the natural-language surface was translated: user messages, assistant replies, assistant reasoning` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Translator: Qwen3.8-27B (FP8) via vLLM, temperature 0, one request per user turn` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
