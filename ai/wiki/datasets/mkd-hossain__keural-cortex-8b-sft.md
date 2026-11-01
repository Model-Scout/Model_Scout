---
type: "dataset"
id: "mkd-hossain/keural-cortex-8b-sft"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-hossain/keural-cortex-8b-sft"
downloads: 172
summary: "한국어 중심의 64K 컨텍스트 윈도우와 도구 호출 기능을 갖춘 Keural-Cortex-8B 모델 학습용 감독 학습 데이터셋입니다."
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mkd-hossain/keural-cortex-8b-sft

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-hossain/keural-cortex-8b-sft)

한국어 중심의 64K 컨텍스트 윈도우와 도구 호출 기능을 갖춘 Keural-Cortex-8B 모델 학습용 감독 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[도구 호출]] — tag_match · tags = `tool-calling` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `One JSON object per line, OpenAI-style messages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `One JSON object per line, OpenAI-style messages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a Korean-first bilingual model` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The supervised fine-tuning set used to train Keural-Cortex-8B` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
