---
type: "dataset"
id: "HanzhiZhang/Poly-FEVER"
source: "huggingface"
url: "https://huggingface.co/datasets/HanzhiZhang/Poly-FEVER"
downloads: 130
summary: "Poly-FEVER는 11개 언어로 된 77,973개의 사실성 판단 및 환각 탐지용 다국어 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# HanzhiZhang/Poly-FEVER

> dataset · [Hugging Face](https://huggingface.co/datasets/HanzhiZhang/Poly-FEVER)

Poly-FEVER는 11개 언어로 된 77,973개의 사실성 판단 및 환각 탐지용 다국어 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each claim shares the same binary label across languages and includes topic metadata from a 22-topic LDA model` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each claim shares the same binary label across languages` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `82` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Poly-FEVER is a controlled multilingual benchmark for factuality judgment and hallucination detection.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Poly-FEVER is a controlled multilingual benchmark for factuality judgment and hallucination detection.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `ta` 열 p90 328자 ≈ 82 토큰 (viewer statistics, default/train)
