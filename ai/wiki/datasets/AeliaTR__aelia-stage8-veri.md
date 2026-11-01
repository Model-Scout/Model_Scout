---
type: "dataset"
id: "AeliaTR/aelia-stage8-veri"
source: "huggingface"
url: "https://huggingface.co/datasets/AeliaTR/aelia-stage8-veri"
downloads: 56
summary: "AeliaTR의 AeLLM 1.08 에이전트 모델 학습용 다국어 및 다범주 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# AeliaTR/aelia-stage8-veri

> dataset · [Hugging Face](https://huggingface.co/datasets/AeliaTR/aelia-stage8-veri)

AeliaTR의 AeLLM 1.08 에이전트 모델 학습용 다국어 및 다범주 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `kategori: tool 9000, rag 2250, kimlik 1500, sohbet 1500, replay 750` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `Satir semasi (`messages` OpenAI sohbet formatinda)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = ``beklenen`/`cevap` alanlari odul fonksiyonuna kwargs olarak gecer` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AeliaTR ajan modeli (AeLLM 1.08) icin iki dosya` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `SFT QLoRA` · 신뢰도 medium
