---
type: "dataset"
id: "E-Park/KOCOH"
source: "huggingface"
url: "https://huggingface.co/datasets/E-Park/KOCOH"
downloads: 34
summary: "한국어 문맥 의존 혐오 표현 데이터셋으로, 혐오 발언 판별 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# E-Park/KOCOH

> dataset · [Hugging Face](https://huggingface.co/datasets/E-Park/KOCOH)

한국어 문맥 의존 혐오 표현 데이터셋으로, 혐오 발언 판별 연구에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Hate speech
Verbal or non-verbal expressions that, based on prejudice or discrimination` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Context
Comment` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Hate speech
Whether it is hate speech (0 or 1 labeling)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is Korean context-dependent hate speech dataset, KOCOH.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `First public release of the dataset` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
