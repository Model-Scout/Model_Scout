---
type: "dataset"
id: "RAS-LAB/KREAP-Korean-MoE-Calibration-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/RAS-LAB/KREAP-Korean-MoE-Calibration-v1"
downloads: 41
summary: "한국어 중심의 합성 데이터와 Qwen3.6 MoE 관찰 테이블로 구성된 K-Guard MoE 보정 데이터셋입니다."
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# RAS-LAB/KREAP-Korean-MoE-Calibration-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/RAS-LAB/KREAP-Korean-MoE-Calibration-v1)

한국어 중심의 합성 데이터와 Qwen3.6 MoE 관찰 테이블로 구성된 K-Guard MoE 보정 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `general capability replay` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Korean-English semantic pairs` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Korean instructions, reasoning, bilingual alignment, code and structured output, tool-style prompts` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:generation = `24,576 deterministic calibration records` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `24,576 deterministic calibration records` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean-centered calibration mixture` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Calibration and evaluation splits were built separately.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
