---
type: "dataset"
id: "jason9693/APEACH"
source: "huggingface"
url: "https://huggingface.co/datasets/jason9693/APEACH"
downloads: 345
summary: "한국어 혐오 표현 평가를 위한 APEACH 데이터셋으로 BEEP! 학습 후 평가에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jason9693/APEACH

> dataset · [Hugging Face](https://huggingface.co/datasets/jason9693/APEACH)

한국어 혐오 표현 평가를 위한 APEACH 데이터셋으로 BEEP! 학습 후 평가에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Korean Hate Speech Evaluation Datasets` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Korean Hate Speech Evaluation Datasets` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `49` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Hate Speech Evaluation Datasets` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `valid (APEACH) | 3770` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train (binarized BEEP!) | 7896` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 73자 ≈ 49 토큰 (viewer statistics, default/test)
