---
type: "dataset"
id: "lmms-lab/LLaVA-OneVision-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Data"
downloads: 50070
summary: "LLaVA-OneVision 데이터셋은 이미지와 텍스트를 포함한 멀티모달 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# lmms-lab/LLaVA-OneVision-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Data)

LLaVA-OneVision 데이터셋은 이미지와 텍스트를 포함한 멀티모달 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset is used for the training of the LLaVA-OneVision model.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `During LLaVA-OneVision training, we use the `json` and `image/video` folder to store the data.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `During LLaVA-OneVision training, we use the `json` and `image/video` folder to store the data.` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `During LLaVA-OneVision training, we use the `json` and `image/video` folder to store the data.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `This dataset is used for the training of the LLaVA-OneVision model.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset is used for the training of the LLaVA-OneVision model.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[nc-ai-consortium__VAETKI-VL-7B-A1B|nc-ai-consortium/VAETKI-VL-7B-A1B]]
