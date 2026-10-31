---
type: "dataset"
id: "lmms-lab/LLaVA-OneVision-Mid-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Mid-Data"
downloads: 559
summary: "LLaVA-OneVision 데이터셋은 중간 단계 모델 학습용 이미지-텍스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lmms-lab/LLaVA-OneVision-Mid-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Mid-Data)

LLaVA-OneVision 데이터셋은 중간 단계 모델 학습용 이미지-텍스트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `we directly upload the json files and image folders` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `This dataset is used for the training of the LLaVA-OneVision Mid-Stage model.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `10` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset is used for the training of the LLaVA-OneVision Mid-Stage model.` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `webdataset` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `__key__` 열 p90 41자 ≈ 10 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[nc-ai-consortium__VAETKI-VL-7B-A1B|nc-ai-consortium/VAETKI-VL-7B-A1B]]
