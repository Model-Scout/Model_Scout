---
type: "dataset"
id: "deokhk/multilingual_reasoning_gap_outputs"
source: "huggingface"
url: "https://huggingface.co/datasets/deokhk/multilingual_reasoning_gap_outputs"
downloads: 152
summary: "Qwen3-4B 모델의 다국어 추론 격차 분석을 위한 실험 출력 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[bn]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[sw]]"
  - "[[te]]"
  - "[[th]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# deokhk/multilingual_reasoning_gap_outputs

> dataset · [Hugging Face](https://huggingface.co/datasets/deokhk/multilingual_reasoning_gap_outputs)

Qwen3-4B 모델의 다국어 추론 격차 분석을 위한 실험 출력 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Prober checkpoints trained for understanding-failure analysis` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Auxiliary artifacts used for probing and analysis` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Signals for understanding failure detection` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:generation, task:information_extraction = `Model inference outputs` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Model inference outputs` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[sw]] — metadata · languages = `sw` · 신뢰도 high
- **언어**: [[te]] — metadata · languages = `te` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `study on multilingual reasoning gaps` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `experiment outputs for Qwen3-4B used in our study` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Prober checkpoints trained for understanding-failure analysis` · 신뢰도 medium
