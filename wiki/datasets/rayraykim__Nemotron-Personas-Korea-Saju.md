---
type: "dataset"
id: "rayraykim/Nemotron-Personas-Korea-Saju"
source: "huggingface"
url: "https://huggingface.co/datasets/rayraykim/Nemotron-Personas-Korea-Saju"
downloads: 362
summary: "한국어 LLM의 페르소나 다양성 및 문화적 컨텍스트 표현을 위한 사주명리 분석 포함 합성 페르소나 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# rayraykim/Nemotron-Personas-Korea-Saju

> dataset · [Hugging Face](https://huggingface.co/datasets/rayraykim/Nemotron-Personas-Korea-Saju)

한국어 LLM의 페르소나 다양성 및 문화적 컨텍스트 표현을 위한 사주명리 분석 포함 합성 페르소나 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `결정론적 사주 4주·오행·십신 + LLM 서사의 사실 정합성·환각 평가` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:reranking, task:summarization = `페르소나 + 사주 페어링 데이터로 (1) 한국 문화 도메인 LLM의 지식·표현 능력, (2) 결정론적 구조 + 생성 서사의 사실 정합성, (3) 페르소나-조건부 한국어 NLG 벤치마크를 가능하게 합니다` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `페르소나 + 사주 컨텍스트를 활용한 한국어 페르소나-조건 생성` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `사주명리(四柱命理)라는 한국 전통 문화 차원으로 확장합니다` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `한국어 LLM의 페르소나 다양성·문화적 컨텍스트 표현·합성 인구 모델링 능력을 평가·강화한다` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 단계적으로 확장되어 NVIDIA Nemotron-Personas-Korea의 원본 규모(100만 페르소나)와 1:1 대응하는 100만 사주 페어링 공개 데이터셋을 목표로` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
