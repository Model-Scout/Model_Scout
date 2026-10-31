---
type: "dataset"
id: "Jongbin-kr/lg-longtail-data-selection-experiment-archive-20260829"
source: "huggingface"
url: "https://huggingface.co/datasets/Jongbin-kr/lg-longtail-data-selection-experiment-archive-20260829"
downloads: 221
summary: "ConvFinQA 데이터 선택 예산 확장 실험을 위한 LG 롱테일 데이터 선택 아카이브입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
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
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
---
# Jongbin-kr/lg-longtail-data-selection-experiment-archive-20260829

> dataset · [Hugging Face](https://huggingface.co/datasets/Jongbin-kr/lg-longtail-data-selection-experiment-archive-20260829)

ConvFinQA 데이터 선택 예산 확장 실험을 위한 LG 롱테일 데이터 선택 아카이브입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The main question is whether accuracy-, diversity-, anti-diversity-, and random selection retain similar behavior as the selected-data budget changes.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `selected subsets, selection manifests, LoRA adapters, DeepSpeed optimizer states, trainer states, logs, raw Core16 evaluation artifacts` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Final three-epoch Core16 results Values below are unweighted group macro averages.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `This public repository is the canonical, self-contained archive for the ConvFinQA data-selection budget-scaling experiments` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training is controlled at three epochs so smaller subsets are not exposed to a fixed number of optimizer steps many more times than larger subsets.` · 신뢰도 medium
